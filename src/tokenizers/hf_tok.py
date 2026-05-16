"""Adaptador para tokenizadores de HuggingFace vía transformers.

Soporta Llama 3, Qwen, Mistral, T5, mBART, BERT y cualquier otro modelo
disponible en el Hub. Algunos requieren autenticación (login HF + aceptar
licencia): meta-llama/Meta-Llama-3-8B, Qwen/Qwen2.5-7B-Instruct, etc.
"""

import os
from typing import Optional


class HFTokenizer:
    """Wrapper sobre transformers.AutoTokenizer.

    Args:
        model_id: identificador en el Hub, ej. "meta-llama/Meta-Llama-3-8B",
                  "Qwen/Qwen2.5-7B-Instruct", "google-bert/bert-base-multilingual-cased",
                  "google/mt5-base", "mistralai/Mistral-7B-v0.3".

    Si el modelo es gated y no hay HF_TOKEN configurado, lanza un error
    explicativo con instrucciones.
    """

    def __init__(self, model_id: str):
        self.model_id = model_id
        self._tokenizer = None

    def _lazy_load(self):
        if self._tokenizer is not None:
            return
        try:
            from transformers import AutoTokenizer
        except ImportError as e:
            raise ImportError(
                "transformers no está instalado. "
                "Instálalo con: pip install 'gemba-token-cost-calculator[hf]'"
            ) from e

        kwargs = {}
        token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
        if token:
            kwargs["token"] = token

        try:
            self._tokenizer = AutoTokenizer.from_pretrained(self.model_id, **kwargs)
        except Exception as e:
            msg = str(e)
            if "gated" in msg.lower() or "401" in msg or "access" in msg.lower():
                raise RuntimeError(
                    f"El modelo {self.model_id} requiere autenticación. "
                    f"Pasos:\n"
                    f"  1. Acepta la licencia en https://huggingface.co/{self.model_id}\n"
                    f"  2. Genera un token en https://huggingface.co/settings/tokens\n"
                    f"  3. Exporta: export HF_TOKEN=hf_xxx"
                ) from e
            raise

    def count(self, text: str) -> int:
        self._lazy_load()
        # add_special_tokens=False para contar solo el texto, no el BOS/EOS
        return len(self._tokenizer.encode(text, add_special_tokens=False))

    def encode_as_pieces(self, text: str, max_pieces: Optional[int] = None) -> list:
        self._lazy_load()
        ids = self._tokenizer.encode(text, add_special_tokens=False)
        if max_pieces is not None:
            ids = ids[:max_pieces]
        return [self._tokenizer.decode([i]) for i in ids]
