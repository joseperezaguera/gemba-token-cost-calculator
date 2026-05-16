# Demo: el mismo texto en español vs inglés

Este ejemplo muestra en directo el hecho que el artículo de Gemba destaca: **el mismo contenido cuesta más tokens en español que en inglés**, porque los corpus de entrenamiento de los modelos dominantes están sesgados hacia el inglés.

## El experimento

Tomamos la misma idea expresada en los dos idiomas:

| Idioma | Texto |
|--------|-------|
| Español | *Los tokens son la moneda en la que pagamos la era de la inteligencia artificial.* |
| Inglés  | *Tokens are the currency in which we pay for the age of artificial intelligence.* |

Y los pasamos por la calculadora en cuatro modelos:

```bash
gemba-tokens --text "Los tokens son la moneda en la que pagamos la era de la inteligencia artificial." \
  --models gpt-4o,claude-sonnet-4-6,qwen-2-5-7b,llama-3-8b

gemba-tokens --text "Tokens are the currency in which we pay for the age of artificial intelligence." \
  --models gpt-4o,claude-sonnet-4-6,qwen-2-5-7b,llama-3-8b
```

## Qué esperar ver

- **GPT-4o y Claude Sonnet** (entrenados con corpus dominantemente inglés) suelen necesitar entre un **30% y un 80% más tokens** para la versión en español que para la versión en inglés.
- **Qwen** (entrenado con mucho más texto en chino y multilingüe) suele tener una penalización menor para el español.
- **Llama 3** queda en medio según versión.

## Lo que esto significa para tu factura

Si tu producto sirve a usuarios hispanohablantes y eliges un modelo con tokenizer orientado al inglés, no solo pagas más caro por token: pagas también más tokens por mensaje. Es el **multiplicador oculto** que el artículo describe en §5: ratio de coste = (precio_por_token × tokens_por_mensaje), y el segundo factor depende fuertemente del idioma.

Para una decisión informada:

1. Mete un texto **representativo** de los prompts reales de tu producto (no una frase corta).
2. Compara los cuatro modelos.
3. Multiplica por tu volumen estimado (usuarios × mensajes/día × días/mes).
4. La diferencia mensual entre modelos suele ser **mucho mayor** de lo que parece a partir del precio por millón.
