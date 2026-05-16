"""Adaptador para tokenizadores de OpenAI vía tiktoken."""

from typing import Optional


class OpenAITokenizer:
    """Tokenizador para modelos de OpenAI usando tiktoken.

    Args:
        model_id: nombre del modelo según el catálogo de tiktoken.
                  Ej: "gpt-4", "gpt-4o", "gpt-3.5-turbo".

    Modelos soportados (ver tiktoken.encoding_for_model):
        - gpt-4o, gpt-4o-mini  -> encoding "o200k_base"
        - gpt-4, gpt-4-turbo   -> encoding "cl100k_base"
        - gpt-3.5-turbo        -> encoding "cl100k_base"
    """

    def __init__(self, model_id: str = "gpt-4o"):
        self.model_id = model_id
        self._tokenizer = None

    def _lazy_load(self):
        if self._tokenizer is not None:
            return
        try:
            import tiktoken
        except ImportError as e:
            raise ImportError(
                "tiktoken no está instalado. "
                "Instálalo con: pip install 'gemba-token-cost-calculator[openai]'"
            ) from e

        try:
            self._tokenizer = tiktoken.encoding_for_model(self.model_id)
        except KeyError:
            # Fallback: si el modelo es desconocido en tiktoken, usar cl100k_base
            # (típico para nuevos releases antes de actualizar tiktoken)
            self._tokenizer = tiktoken.get_encoding("cl100k_base")

    def count(self, text: str) -> int:
        """Devuelve el número de tokens del texto."""
        self._lazy_load()
        return len(self._tokenizer.encode(text))

    def encode_as_pieces(self, text: str, max_pieces: Optional[int] = None) -> list:
        """Devuelve la lista de piezas (strings) del texto.

        max_pieces: si se especifica, trunca la salida (útil para inspección rápida).
        """
        self._lazy_load()
        ids = self._tokenizer.encode(text)
        if max_pieces is not None:
            ids = ids[:max_pieces]
        return [self._tokenizer.decode([i]) for i in ids]
