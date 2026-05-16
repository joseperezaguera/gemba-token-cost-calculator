"""Adaptador para tokenizadores de Anthropic Claude.

Anthropic no publica su tokenizer. La única forma oficial de contar tokens
exactos es la API /v1/messages/count_tokens, que requiere clave de API.

Si no quieres consumir API, puedes usar el modo --approx que se apoya en
cl100k_base (tiktoken) como proxy. La cifra aproximada suele estar dentro
del ±10% para textos en español/inglés, pero NO es la cifra exacta que
Anthropic te facturará.
"""

import os
from typing import Optional


class AnthropicTokenizer:
    """Cuenta tokens para modelos Claude vía la API oficial count_tokens.

    Args:
        model_id: ej. "claude-opus-4-7", "claude-sonnet-4-6", "claude-haiku-4-5".
        approx: si True, usa cl100k_base como proxy (no API, no exacto).

    Requiere ANTHROPIC_API_KEY si approx=False.
    """

    def __init__(self, model_id: str = "claude-sonnet-4-6", approx: bool = False):
        self.model_id = model_id
        self.approx = approx
        self._client = None
        self._tiktoken_enc = None

    def _lazy_load_api(self):
        if self._client is not None:
            return
        try:
            import anthropic
        except ImportError as e:
            raise ImportError(
                "anthropic SDK no está instalado. "
                "Instálalo con: pip install 'gemba-token-cost-calculator[anthropic]'"
            ) from e
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError(
                "ANTHROPIC_API_KEY no está configurada. "
                "Exporta tu clave (export ANTHROPIC_API_KEY=sk-ant-...) o "
                "usa el modo aproximado: AnthropicTokenizer(approx=True)."
            )
        self._client = anthropic.Anthropic()

    def _lazy_load_approx(self):
        if self._tiktoken_enc is not None:
            return
        try:
            import tiktoken
        except ImportError as e:
            raise ImportError(
                "tiktoken no está instalado (necesario para el modo aproximado). "
                "Instálalo con: pip install 'gemba-token-cost-calculator[openai]'"
            ) from e
        # cl100k_base es el encoding GPT-4. No es idéntico al de Claude
        # pero ambos son BPE con corpus principalmente en inglés, así que
        # la magnitud es razonablemente parecida (±10%).
        self._tiktoken_enc = tiktoken.get_encoding("cl100k_base")

    def count(self, text: str) -> int:
        if self.approx:
            self._lazy_load_approx()
            return len(self._tiktoken_enc.encode(text))
        self._lazy_load_api()
        response = self._client.messages.count_tokens(
            model=self.model_id,
            messages=[{"role": "user", "content": text}],
        )
        return response.input_tokens

    def encode_as_pieces(self, text: str, max_pieces: Optional[int] = None) -> list:
        """Anthropic NO expone piezas individuales. En modo approx devolvemos
        las de tiktoken. En modo API devolvemos lista de longitud N con un
        marcador genérico para que la salida sea consistente."""
        if self.approx:
            self._lazy_load_approx()
            ids = self._tiktoken_enc.encode(text)
            if max_pieces is not None:
                ids = ids[:max_pieces]
            return [self._tiktoken_enc.decode([i]) for i in ids]
        # Modo API: solo número, sin piezas reales
        n = self.count(text)
        if max_pieces is not None:
            n = min(n, max_pieces)
        return [f"<claude-token-{i}>" for i in range(n)]
