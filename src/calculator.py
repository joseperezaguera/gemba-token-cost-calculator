"""
Calculator — núcleo de la calculadora.

Toma un texto, una lista de modelos y devuelve, para cada modelo:
  - número de tokens del texto
  - coste estimado en USD y EUR según el catálogo de precios

El asumido por defecto es que todos los tokens son "input" (más típico para
estimar coste de prompts). El parámetro role permite calcular output.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml

from .tokenizers import OpenAITokenizer, HFTokenizer, AnthropicTokenizer


PRICES_PATH = Path(__file__).parent / "prices.yaml"


@dataclass
class ModelCost:
    model: str
    provider: str
    n_tokens: int
    cost_usd: float
    cost_eur: float
    role: str  # "input" o "output"
    notes: str = ""


def load_prices(path: Optional[Path] = None) -> dict:
    path = path or PRICES_PATH
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_tokenizer(provider: str, tokenizer_id: str,
                   anthropic_approx: bool = False):
    if provider == "openai":
        return OpenAITokenizer(model_id=tokenizer_id)
    elif provider == "hf":
        return HFTokenizer(model_id=tokenizer_id)
    elif provider == "anthropic":
        return AnthropicTokenizer(model_id=tokenizer_id, approx=anthropic_approx)
    raise ValueError(f"Provider desconocido: {provider}")


def calculate(text: str, models: list, role: str = "input",
              prices_data: Optional[dict] = None,
              anthropic_approx: bool = False,
              eur_rate: Optional[float] = None) -> list:
    """Calcula coste por modelo.

    Args:
        text: texto a evaluar
        models: lista de IDs de modelo del prices.yaml (ej. ["gpt-4o", "claude-opus-4-7"])
        role: "input" o "output" (afecta qué precio se aplica)
        prices_data: dict cargado de prices.yaml (si None, se carga del default)
        anthropic_approx: si True, los modelos Anthropic usan cl100k_base como proxy
        eur_rate: tipo de cambio USD->EUR; si None, se usa el del prices.yaml

    Returns:
        lista de ModelCost
    """
    if prices_data is None:
        prices_data = load_prices()
    if eur_rate is None:
        eur_rate = prices_data["exchange"]["usd_to_eur"]

    results = []
    for model_id in models:
        if model_id not in prices_data["models"]:
            raise ValueError(
                f"Modelo '{model_id}' no encontrado en prices.yaml. "
                f"Modelos disponibles: {list(prices_data['models'].keys())}"
            )
        spec = prices_data["models"][model_id]
        provider = spec["provider"]
        tok = get_tokenizer(provider, spec["tokenizer_id"],
                            anthropic_approx=anthropic_approx)
        try:
            n_tokens = tok.count(text)
        except Exception as e:
            # Si un proveedor falla (auth, deps, red, etc.) lo reportamos
            # pero seguimos con los demás modelos.
            results.append(ModelCost(
                model=model_id, provider=provider, n_tokens=-1,
                cost_usd=0.0, cost_eur=0.0, role=role,
                notes=f"ERROR: {e}"
            ))
            continue

        price_key = f"{role}_per_million_usd"
        rate_per_million = spec.get(price_key, 0.0)
        cost_usd = (n_tokens / 1_000_000) * rate_per_million
        cost_eur = cost_usd * eur_rate

        results.append(ModelCost(
            model=model_id,
            provider=provider,
            n_tokens=n_tokens,
            cost_usd=cost_usd,
            cost_eur=cost_eur,
            role=role,
            notes=spec.get("notes", ""),
        ))

    return results
