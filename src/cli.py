"""CLI para la calculadora de coste por token."""

from pathlib import Path
import sys

import click

from .calculator import calculate, load_prices, ModelCost


def _format_money(value, currency="EUR", decimals=6):
    """Formatea un importe con N decimales y el símbolo correcto."""
    if currency == "EUR":
        return f"{value:.{decimals}f} €"
    return f"${value:.{decimals}f}"


def _print_table(results, currency="EUR"):
    """Imprime resultados en una tabla legible."""
    cols = ["Modelo", "Proveedor", "#Tokens", f"Coste ({currency})", "Notas"]
    widths = [22, 10, 10, 18, 30]
    sep = "  "

    header = sep.join(c.ljust(w) for c, w in zip(cols, widths))
    print(header)
    print("-" * (sum(widths) + len(sep) * (len(cols) - 1)))

    for r in results:
        money = r.cost_eur if currency == "EUR" else r.cost_usd
        tokens_str = str(r.n_tokens) if r.n_tokens >= 0 else "ERR"
        money_str = _format_money(money, currency) if r.n_tokens >= 0 else "—"
        notes = (r.notes[:27] + "...") if len(r.notes) > 30 else r.notes
        row = [
            r.model.ljust(widths[0]),
            r.provider.ljust(widths[1]),
            tokens_str.rjust(widths[2]),
            money_str.rjust(widths[3]),
            notes.ljust(widths[4]),
        ]
        print(sep.join(row))


@click.command()
@click.option("--text", "-t", default=None, help="Texto a tokenizar (entre comillas).")
@click.option("--file", "-f", "input_file", type=click.Path(exists=True),
              help="Fichero de texto a tokenizar.")
@click.option("--models", "-m", default="gpt-4o,claude-sonnet-4-6,llama-3-8b",
              help="Modelos separados por coma. Ver --list-models.")
@click.option("--role", type=click.Choice(["input", "output"]), default="input",
              help="Si los tokens son input (prompt) o output (respuesta).")
@click.option("--currency", type=click.Choice(["USD", "EUR"]), default="EUR")
@click.option("--anthropic-approx", is_flag=True, default=False,
              help="Usa cl100k_base como proxy para Claude (sin ANTHROPIC_API_KEY).")
@click.option("--list-models", is_flag=True, default=False,
              help="Lista todos los modelos disponibles en prices.yaml y termina.")
@click.option("--prices", "prices_file", type=click.Path(exists=True), default=None,
              help="Fichero alternativo de precios.")
def main(text, input_file, models, role, currency, anthropic_approx,
         list_models, prices_file):
    """Calcula el coste de tokenizar un texto en varios modelos."""

    prices_data = load_prices(Path(prices_file)) if prices_file else load_prices()

    if list_models:
        click.echo("Modelos disponibles en prices.yaml:\n")
        for mid, spec in prices_data["models"].items():
            click.echo(
                f"  {mid:<25} ({spec['provider']:<10}) "
                f"in=${spec['input_per_million_usd']:.2f} "
                f"out=${spec['output_per_million_usd']:.2f}/1M"
            )
        return

    if not text and not input_file:
        click.echo(
            "Tienes que pasar --text 'tu texto' o --file ruta/al/fichero.txt",
            err=True
        )
        sys.exit(1)

    if input_file:
        text = Path(input_file).read_text(encoding="utf-8")

    model_list = [m.strip() for m in models.split(",") if m.strip()]

    click.echo(f"Texto: {len(text)} caracteres ({len(text.split())} palabras)")
    click.echo(f"Rol: {role}\n")

    results = calculate(
        text=text,
        models=model_list,
        role=role,
        prices_data=prices_data,
        anthropic_approx=anthropic_approx,
    )

    _print_table(results, currency=currency)

    # Resumen rápido al final
    valid = [r for r in results if r.n_tokens > 0]
    if valid:
        cheapest = min(valid, key=lambda r: r.cost_usd)
        most_expensive = max(valid, key=lambda r: r.cost_usd)
        if cheapest.model != most_expensive.model:
            ratio = most_expensive.cost_usd / cheapest.cost_usd if cheapest.cost_usd > 0 else float("inf")
            click.echo()
            click.echo(
                f"→ Más caro: {most_expensive.model} "
                f"({_format_money(most_expensive.cost_eur if currency == 'EUR' else most_expensive.cost_usd, currency)})"
            )
            click.echo(
                f"→ Más barato: {cheapest.model} "
                f"({_format_money(cheapest.cost_eur if currency == 'EUR' else cheapest.cost_usd, currency)})"
            )
            if ratio != float("inf"):
                click.echo(f"→ Diferencia: {ratio:.1f}x")


if __name__ == "__main__":
    main()
