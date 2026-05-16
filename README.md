# gemba-token-cost-calculator

> **Calculadora de coste real por token, multimodelo y multiidioma.** Usa los tokenizadores reales —`tiktoken` para OpenAI, `transformers` de HuggingFace para Llama 3, Qwen, Mistral, T5 y BERT, y la API oficial de Anthropic para Claude— combinados con una tabla de precios actualizable. Material complementario del artículo de [Gemba](https://www.gemba.es/) [«¿Qué es un token?»](https://www.gemba.es/p/que-es-un-token) (18 mayo 2026).

Si lo que quieres es **entender cómo funcionan los tokenizadores por dentro**, el repo hermano es [`gemba-tokenizers-from-scratch`](https://github.com/josemerca/gemba-tokenizers-from-scratch). Este de aquí es para **decidir presupuesto con número**.

## Para qué sirve

- Saber **cuánto te cobraría** cada modelo por un texto representativo de tu producto.
- **Comparar coste** entre proveedores con el mismo prompt.
- **Comparar coste por idioma** (la misma idea en español vs inglés) para entender el sesgo de corpus que cuesta dinero.
- Tomar decisiones de presupuesto con datos, no con intuición.

## Quickstart

```bash
git clone https://github.com/josemerca/gemba-token-cost-calculator.git
cd gemba-token-cost-calculator

# Instala con todos los proveedores
python3 -m venv .venv
.venv/bin/pip install -e .[all]

# Lista los modelos disponibles
.venv/bin/gemba-tokens --list-models

# Calcula coste de un prompt en tres modelos
.venv/bin/gemba-tokens --text "Tu prompt aquí" --models gpt-4o,claude-sonnet-4-6,qwen-2-5-7b
```

Salida ejemplo:

```
Texto: 67 caracteres (12 palabras)
Rol: input

Modelo                  Proveedor   #Tokens     Coste (EUR)
------------------------------------------------------------
gpt-4o                  openai           15     0.000035 €
claude-sonnet-4-6       anthropic        14     0.000039 €
qwen-2-5-7b             hf               12     0.000002 €

→ Más caro: claude-sonnet-4-6 (0.000039 €)
→ Más barato: qwen-2-5-7b (0.000002 €)
→ Diferencia: 16.7x
```

## Instalación por proveedor

Si no quieres tirarte de cabeza, instala solo lo que vayas a usar:

```bash
# Solo OpenAI (más liviano)
.venv/bin/pip install -e .[openai]

# Solo HuggingFace (incluye sentencepiece)
.venv/bin/pip install -e .[hf]

# Solo Anthropic
.venv/bin/pip install -e .[anthropic]

# Todo a la vez
.venv/bin/pip install -e .[all]
```

## Autenticación

Algunos modelos requieren credenciales:

- **HuggingFace gated models** (Llama 3, algunas variantes de Qwen): necesitas haber aceptado la licencia en su página y exportar `HF_TOKEN`:

  ```bash
  export HF_TOKEN=hf_xxxxx
  ```

- **Anthropic Claude** (modo exacto): necesitas `ANTHROPIC_API_KEY`:

  ```bash
  export ANTHROPIC_API_KEY=sk-ant-xxxxx
  ```

  Si no quieres usar la API, pasa `--anthropic-approx` y la calculadora usará `cl100k_base` como proxy. Cifra aproximada (±10% típicamente), no exacta.

## Uso desde Python

```python
from src.calculator import calculate

results = calculate(
    text="Llevamos dos años pagando IA en una moneda que casi nadie entiende.",
    models=["gpt-4o", "claude-opus-4-7", "qwen-2-5-7b"],
    role="input",
)
for r in results:
    print(f"{r.model}: {r.n_tokens} tokens = {r.cost_eur:.6f} EUR")
```

## Estructura

```
gemba-token-cost-calculator/
├── src/
│   ├── tokenizers/
│   │   ├── openai_tok.py        # tiktoken
│   │   ├── hf_tok.py            # transformers.AutoTokenizer
│   │   └── anthropic_tok.py     # Anthropic count_tokens API
│   ├── prices.yaml              # precios actualizables a mano
│   ├── calculator.py            # núcleo del cálculo
│   └── cli.py                   # CLI con click
├── examples/
│   ├── demo_es_en.md            # mismo texto en es/en → ver diferencia
│   └── sample_product_prompt.txt
├── claude-skill/                # skill de Claude Code: /calcular-tokens
└── tests/
    └── test_calculator.py
```

## Skill de Claude Code

Carga el plugin para invocar la calculadora conversacionalmente:

```bash
claude --plugin claude-skill
```

Luego en la conversación:

```
/calcular-tokens "este es mi prompt típico" --models gpt-4o,claude-opus,qwen-2-5-7b
```

Ver detalles en [`claude-skill/`](claude-skill/).

## Actualización de precios

Los precios cambian. El fichero [`src/prices.yaml`](src/prices.yaml) es texto plano y se edita a mano. Si te animas, abre un PR con la actualización y la fuente.

## Limitaciones honestas

- Las cifras para modelos open source self-hosted (Llama 3, Qwen, Mistral) son **estimaciones de coste por inferencia en GPU propia**. Tu coste real depende de tu utilización, tipo de GPU, energía, etc. Edita `prices.yaml` con tu coste real.
- Anthropic no publica su tokenizer. El modo exacto consume API; el modo `--anthropic-approx` es un proxy aproximado (±10%).
- Modelos gated requieren autenticación manual previa.

## Tests

```bash
.venv/bin/python -m unittest discover tests -v
```

## Licencia

MIT.

---

*José Ramón Pérez Agüera — Gemba · gemba.es*
