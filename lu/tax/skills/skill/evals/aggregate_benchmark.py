#!/usr/bin/env python3
"""
aggregate_benchmark.py — Agrège les results.json de toutes les itérations
et produit une table comparative + un Markdown utilisable dans le README.
"""

from __future__ import annotations

import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "evals-workspace"

console = Console()


def main() -> None:
    iters = sorted(p for p in WORKSPACE.glob("iteration-*") if p.is_dir() and not p.is_symlink())
    if not iters:
        console.print("[red]Aucune itération trouvée. Lancez d'abord run_evals.py[/red]")
        return

    latest = iters[-1]
    results = json.loads((latest / "results.json").read_text(encoding="utf-8"))

    table = Table(title=f"Benchmark Paperasse Lux ({results['iteration']})", show_lines=True)
    table.add_column("Skill", style="bold cyan")
    table.add_column("With Skill", justify="right", style="green")
    table.add_column("Without Skill", justify="right", style="red")
    table.add_column("Delta", justify="right", style="bold yellow")

    md = ["| Skill | With Skill | Without Skill | Delta |", "|-------|-----------|--------------|-------|"]
    totals_w, totals_wo, totals_n = 0.0, 0.0, 0

    for s in results["skills"]:
        if not s["cases"]:
            continue
        avg_w = sum(c["with"]["score"] for c in s["cases"]) / len(s["cases"])
        avg_wo = sum(c["without"]["score"] for c in s["cases"]) / len(s["cases"])
        delta = avg_w - avg_wo
        emph = "**" if delta >= 10 else ""
        table.add_row(s["skill"], f"{avg_w:.0f}%", f"{avg_wo:.0f}%", f"{delta:+.0f}%")
        md.append(f"| {s['skill']} | {avg_w:.0f}% | {avg_wo:.0f}% | {emph}{delta:+.0f}%{emph} |")
        totals_w += avg_w
        totals_wo += avg_wo
        totals_n += 1

    if totals_n:
        agg_w = totals_w / totals_n
        agg_wo = totals_wo / totals_n
        delta = agg_w - agg_wo
        table.add_row("Aggregate", f"{agg_w:.0f}%", f"{agg_wo:.0f}%", f"{delta:+.0f}%", style="bold")
        md.append(f"| **Aggregate** | **{agg_w:.0f}%** | **{agg_wo:.0f}%** | **{delta:+.0f}%** |")

    console.print(table)
    console.print("\n[bold]Markdown pour le README :[/bold]\n")
    console.print("\n".join(md))


if __name__ == "__main__":
    main()
