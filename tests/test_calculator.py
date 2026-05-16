"""Tests de la calculadora.

Estos tests no requieren tokenizadores reales: usan un MockTokenizer que
cuenta caracteres dividido por 4 (aproximación grosera pero suficiente para
verificar la matemática del coste).
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.calculator import calculate, load_prices, ModelCost


class MockTokenizer:
    """Tokenizer falso: tokens = ceil(len(text) / 4)."""

    def __init__(self, model_id):
        self.model_id = model_id

    def count(self, text):
        return max(1, len(text) // 4)

    def encode_as_pieces(self, text, max_pieces=None):
        return [text[i:i+4] for i in range(0, len(text), 4)]


def _mock_get_tokenizer(provider, tokenizer_id, anthropic_approx=False):
    return MockTokenizer(tokenizer_id)


class TestCalculatorMath(unittest.TestCase):
    """Verifica que el coste se calcula correctamente dada N tokens."""

    @classmethod
    def setUpClass(cls):
        cls.prices = load_prices()

    @patch("src.calculator.get_tokenizer", side_effect=_mock_get_tokenizer)
    def test_input_cost_gpt4o(self, _mock):
        # "Hola mundo" -> 10 chars -> 10//4 = 2 tokens
        results = calculate("Hola mundo", ["gpt-4o"], role="input",
                            prices_data=self.prices)
        self.assertEqual(len(results), 1)
        r = results[0]
        self.assertEqual(r.n_tokens, 2)
        # gpt-4o input: $2.50 / 1M tokens
        # 2 tokens * 2.50 / 1_000_000 = 0.000005 USD
        self.assertAlmostEqual(r.cost_usd, 2 * 2.50 / 1_000_000, places=10)

    @patch("src.calculator.get_tokenizer", side_effect=_mock_get_tokenizer)
    def test_output_cost_uses_output_rate(self, _mock):
        results = calculate("x" * 100, ["claude-opus-4-7"], role="output",
                            prices_data=self.prices)
        r = results[0]
        # 100 chars / 4 = 25 tokens
        # opus output: $75 / 1M
        self.assertEqual(r.n_tokens, 25)
        self.assertAlmostEqual(r.cost_usd, 25 * 75.0 / 1_000_000, places=10)

    @patch("src.calculator.get_tokenizer", side_effect=_mock_get_tokenizer)
    def test_eur_conversion(self, _mock):
        results = calculate("x" * 1000, ["gpt-4o"], role="input",
                            prices_data=self.prices)
        r = results[0]
        # cost_eur = cost_usd * 0.92 (del prices.yaml)
        self.assertAlmostEqual(r.cost_eur,
                               r.cost_usd * self.prices["exchange"]["usd_to_eur"])

    @patch("src.calculator.get_tokenizer", side_effect=_mock_get_tokenizer)
    def test_multiple_models(self, _mock):
        results = calculate("x" * 400, ["gpt-4o", "claude-haiku-4-5", "llama-3-8b"],
                            prices_data=self.prices)
        self.assertEqual(len(results), 3)
        # Todos los modelos tienen N tokens iguales (mock), pero costes distintos
        n_tokens_set = {r.n_tokens for r in results}
        self.assertEqual(len(n_tokens_set), 1)
        cost_set = {round(r.cost_usd, 8) for r in results}
        self.assertEqual(len(cost_set), 3)

    @patch("src.calculator.get_tokenizer", side_effect=_mock_get_tokenizer)
    def test_unknown_model_raises(self, _mock):
        with self.assertRaises(ValueError):
            calculate("x", ["modelo-inexistente-xyz"], prices_data=self.prices)


class TestPricesYaml(unittest.TestCase):
    def setUp(self):
        self.prices = load_prices()

    def test_has_exchange_rate(self):
        self.assertIn("exchange", self.prices)
        self.assertIn("usd_to_eur", self.prices["exchange"])
        self.assertGreater(self.prices["exchange"]["usd_to_eur"], 0)

    def test_models_have_required_fields(self):
        required = ["provider", "tokenizer_id", "input_per_million_usd",
                    "output_per_million_usd"]
        for model_id, spec in self.prices["models"].items():
            for field in required:
                self.assertIn(field, spec,
                              f"Modelo {model_id} no tiene campo {field}")

    def test_providers_are_known(self):
        valid = {"openai", "anthropic", "hf"}
        for model_id, spec in self.prices["models"].items():
            self.assertIn(spec["provider"], valid,
                          f"Provider desconocido en {model_id}: {spec['provider']}")


if __name__ == "__main__":
    unittest.main()
