#!/usr/bin/env python3
"""
is_simulator.py, calcule l'IS prévisionnel depuis résultat comptable + réintégrations.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def simulate_is(
    resultat_comptable: float,
    reintegrations: float,
    deductions: float,
    acomptes_verses: float,
    credits_impot: float,
    is_n_1: float,
    taux_reduit_pme: bool,
    report_deficit: float,
) -> dict:
    """Calcule l'IS dû."""
    resultat_fiscal = resultat_comptable + reintegrations - deductions

    # Report déficitaire (plafonné à 1M + 50% au-delà)
    if resultat_fiscal > 0 and report_deficit > 0:
        deficit_imputable = min(report_deficit, 1_000_000 + 0.5 * max(0, resultat_fiscal - 1_000_000))
        resultat_apres_report = resultat_fiscal - deficit_imputable
    else:
        deficit_imputable = 0
        resultat_apres_report = resultat_fiscal

    # Calcul IS
    if resultat_apres_report <= 0:
        is_brut = 0
    elif taux_reduit_pme:
        # 15% sur les 42 500 premiers €, 25% au-delà
        is_brut = min(resultat_apres_report, 42500) * 0.15 + max(0, resultat_apres_report - 42500) * 0.25
    else:
        is_brut = resultat_apres_report * 0.25

    # Solde
    is_net = is_brut - acomptes_verses - credits_impot
    solde = is_net if is_net > 0 else 0  # si crédit, pas de remboursement automatique en première application

    return {
        "_version": "0.1.0",
        "inputs": {
            "resultat_comptable": resultat_comptable,
            "reintegrations": reintegrations,
            "deductions": deductions,
            "acomptes_verses": acomptes_verses,
            "credits_impot": credits_impot,
            "taux_reduit_pme": taux_reduit_pme,
            "report_deficit_disponible": report_deficit,
        },
        "calcul": {
            "resultat_fiscal_avant_report": round(resultat_fiscal, 2),
            "deficit_impute": round(deficit_imputable, 2),
            "resultat_apres_report": round(resultat_apres_report, 2),
            "is_brut": round(is_brut, 2),
            "is_net_apres_credits": round(is_net, 2),
            "solde_a_payer": round(solde, 2),
        },
        "taux_effectif_pct": round(is_brut / resultat_comptable * 100, 2) if resultat_comptable > 0 else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulateur IS")
    parser.add_argument("--resultat-comptable", type=float, required=True)
    parser.add_argument("--reintegrations", type=float, default=0)
    parser.add_argument("--deductions", type=float, default=0)
    parser.add_argument("--acomptes-verses", type=float, default=0)
    parser.add_argument("--credits-impot", type=float, default=0, help="CIR + CII + autres")
    parser.add_argument("--is-n-1", type=float, default=0)
    parser.add_argument("--taux-reduit-pme", action="store_true",
                        help="Appliquer le taux réduit 15%% sur les 42 500 premiers €")
    parser.add_argument("--report-deficit", type=float, default=0, help="Déficit reportable disponible")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    result = simulate_is(
        args.resultat_comptable, args.reintegrations, args.deductions,
        args.acomptes_verses, args.credits_impot, args.is_n_1,
        args.taux_reduit_pme, args.report_deficit,
    )

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"✓ IS estimé : {result['calcul']['is_brut']:,.0f} € (solde à payer {result['calcul']['solde_a_payer']:,.0f} €)", file=sys.stderr)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
