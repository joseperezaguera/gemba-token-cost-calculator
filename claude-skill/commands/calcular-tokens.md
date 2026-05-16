---
description: Calcula coste real por token de un texto en varios modelos de IA (OpenAI, Anthropic, HuggingFace)
allowed-tools: Bash, Read
argument-hint: <texto o fichero> [--models lista] [opciones]
---

# /calcular-tokens

Calcula el número de tokens y el coste estimado de un texto en uno o varios modelos comerciales y open source.

## Argumentos

- `<texto>` — el texto a evaluar (entre comillas) **o** `--file <ruta>` para leerlo de fichero.
- `--models <lista>` — modelos separados por coma (default: `gpt-4o,claude-sonnet-4-6,qwen-2-5-7b`).
- `--role input|output` — si los tokens son de prompt o de respuesta (default: input).
- `--currency EUR|USD` — moneda de salida (default: EUR).
- `--anthropic-approx` — si no tienes `ANTHROPIC_API_KEY`, usa `cl100k_base` como proxy para Claude.

## Comportamiento

1. Ejecuta `gemba-tokens` con los argumentos pasados.
2. Si Anthropic falla porque no hay `ANTHROPIC_API_KEY`, sugiere reintentar con `--anthropic-approx`.
3. Si HuggingFace falla por gating, indica qué token necesita el usuario.
4. Presenta los resultados al usuario interpretando:
   - Cuál es el más barato y el más caro.
   - Qué ratio hay entre ellos.
   - Si el modelo más caro está justificado por el número de tokens (a veces un modelo "premium" usa más tokens, no menos).

## Ejemplos

```
/calcular-tokens "Cuánto cuesta esta consulta tipo de mi producto"
```

```
/calcular-tokens --file ./mi_prompt_sistema.txt --models gpt-4o,claude-opus-4-7,llama-3-8b
```

```
/calcular-tokens "Hola, ¿cómo puedo devolver un pedido?" --models gpt-4o,claude-sonnet-4-6 --anthropic-approx
```

## Si el usuario pasa volumen estimado

Cuando aporte contexto como *"con 10k usuarios y 5 mensajes/día"*, multiplica:

```
coste_mensual = n_tokens × n_mensajes × n_usuarios × 30 días × precio_por_token
```

Y suma input + estimación de output (típicamente 1.5–3× el input). Presenta el total mensual estimado por modelo.

## Recordatorio

Estas cifras son **el coste estimado** con los tokenizadores reales y el catálogo de precios del repo. Los precios reales pueden cambiar: edita `src/prices.yaml` si detectas una discrepancia.
