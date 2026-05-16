---
name: token-cost-calculator
description: >
  Esta skill se activa cuando el usuario quiere calcular el coste real (en
  USD o EUR) de tokenizar un texto en varios modelos de IA. Útil para
  comparar coste entre proveedores (OpenAI, Anthropic, HuggingFace) y para
  evaluar el impacto del idioma en la factura.

  Triggers: "cuánto cuesta este prompt en GPT-4o", "compara el coste de mi
  prompt en Claude y Qwen", "¿cuántos tokens tiene este texto?",
  "calcúlame el coste por mes asumiendo 10k usuarios", "¿es más caro en
  español o en inglés?".
version: 0.1.0
---

# Skill: Token Cost Calculator

## Cuándo usar

Cuando el usuario quiera **calcular o comparar coste real** en tokens y dinero entre modelos de IA. Esta skill usa los tokenizadores reales (no aproximaciones pedagógicas).

Casos típicos:

- *"¿Cuántos tokens es este prompt en GPT-4o?"*
- *"Compara el coste de este prompt en GPT-4o, Claude Opus y Qwen 7B."*
- *"Si tengo 10.000 usuarios al día con 5 mensajes cada uno, ¿cuánto me cuesta al mes en cada modelo?"*
- *"¿Es más caro tokenizar este prompt en español o en inglés?"*

## Mapeo a comandos

| Acción del usuario | Comando / Función |
|--------------------|-------------------|
| Calcular coste de un texto | `gemba-tokens --text "..." --models gpt-4o,claude-opus-4-7,...` |
| Listar modelos disponibles | `gemba-tokens --list-models` |
| Calcular desde fichero | `gemba-tokens --file path.txt --models ...` |
| Modo aproximado Claude (sin API) | añadir `--anthropic-approx` |
| Cambiar moneda | `--currency USD` o `--currency EUR` |

## Cómo proceder

1. **Identifica qué quiere el usuario**: número de tokens (simple) o coste comparado (más interesante).
2. **Si compara modelos**: ofrece al menos 3 modelos cubriendo distintos rangos de precio (un frontier, un mid-tier y un open source).
3. **Si el usuario pasa un volumen estimado** (usuarios/día, mensajes/usuario), multiplica por la cifra base y devuelve un coste mensual estimado.
4. **Si el texto es muy corto**: avisa al usuario que las diferencias entre modelos son más significativas con prompts más largos y representativos.

## Comportamiento por defecto

- **Modelos por defecto si no se especifican**: `gpt-4o,claude-sonnet-4-6,qwen-2-5-7b` (un OpenAI, un Anthropic, un open source).
- **Moneda por defecto**: EUR.
- **Si falla autenticación**: explica al usuario qué necesita exportar (`HF_TOKEN`, `ANTHROPIC_API_KEY`) o sugiere `--anthropic-approx`.

## Para el cálculo mensual

Si el usuario pasa contexto como *"tengo 10k usuarios al día, 5 mensajes cada uno"*:

1. Multiplica n_tokens × 5 mensajes × 10.000 usuarios × 30 días.
2. Asume también una respuesta del LLM proporcional al input (típicamente 1.5–3× el input).
3. Calcula coste total mensual sumando input + output.
4. Presenta la cifra agregada por modelo.

## Cosas que NO hace esta skill

- No optimiza prompts ni sugiere cambios de redacción para gastar menos tokens (eso es trabajo aparte).
- No detecta automáticamente el idioma del texto (responsabilidad del usuario).
- No actualiza los precios automáticamente. Si el usuario reporta un cambio, sugerir editar `prices.yaml`.

## Comandos disponibles

- `/calcular-tokens` — Calcula coste de un texto en varios modelos. Ver `commands/calcular-tokens.md`.

---

*Material complementario del artículo de Gemba [«¿Qué es un token?»](https://www.gemba.es/p/que-es-un-token) — 18 de mayo de 2026.*
