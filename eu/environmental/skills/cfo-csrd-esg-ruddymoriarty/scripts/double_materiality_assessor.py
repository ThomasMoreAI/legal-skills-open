#!/usr/bin/env python3
"""
double_materiality_assessor.py, construit la matrice de double matérialité.

Input : CSV avec colonnes sujet,standard_esrs,score_impact(1-5),score_financial(1-5)
Output : matrice + liste sujets matériels + sujets à reporter
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def evaluer_materialite(score_impact: int, score_financial: int, seuil: int = 3) -> dict:
    """Détermine si un sujet est matériel."""
    materiel_impact = score_impact >= seuil
    materiel_financial = score_financial >= seuil
    materiel = materiel_impact or materiel_financial

    if materiel_impact and materiel_financial:
        nature = "double matérialité"
        priority = "haute"
    elif materiel_impact:
        nature = "matériel sur impact uniquement"
        priority = "moyenne"
    elif materiel_financial:
        nature = "matériel sur financier uniquement"
        priority = "moyenne"
    else:
        nature = "non matériel"
        priority = "basse"

    return {
        "materiel": materiel,
        "materiel_impact": materiel_impact,
        "materiel_financial": materiel_financial,
        "nature": nature,
        "priority": priority,
        "score_total": score_impact + score_financial,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Matrice de double matérialité ESG")
    parser.add_argument("--sujets", type=Path, required=True,
                        help="CSV : sujet,standard_esrs,score_impact(1-5),score_financial(1-5)")
    parser.add_argument("--seuil", type=int, default=3, help="Seuil matérialité (défaut 3 sur 5)")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    sujets = []
    with args.sujets.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                score_impact = int(row.get("score_impact", 0))
                score_financial = int(row.get("score_financial", 0))
                if not (0 <= score_impact <= 5 and 0 <= score_financial <= 5):
                    continue
                eval_result = evaluer_materialite(score_impact, score_financial, args.seuil)
                sujets.append({
                    "sujet": row.get("sujet", ""),
                    "standard_esrs": row.get("standard_esrs", ""),
                    "score_impact": score_impact,
                    "score_financial": score_financial,
                    **eval_result,
                })
            except (ValueError, KeyError):
                continue

    sujets.sort(key=lambda s: s["score_total"], reverse=True)

    sujets_materiels = [s for s in sujets if s["materiel"]]
    sujets_non_materiels = [s for s in sujets if not s["materiel"]]

    standards_a_reporter = sorted(set(s["standard_esrs"] for s in sujets_materiels))

    result = {
        "_version": "0.1.0",
        "seuil_materialite": args.seuil,
        "nb_sujets_total": len(sujets),
        "nb_sujets_materiels": len(sujets_materiels),
        "nb_sujets_non_materiels": len(sujets_non_materiels),
        "standards_esrs_a_reporter": standards_a_reporter,
        "sujets_materiels": sujets_materiels,
        "sujets_non_materiels": sujets_non_materiels,
        "note": (
            "ESRS E1 (climat) bénéficie d'une présomption de matérialité, si non "
            "matériel, justifier explicitement. Pour les sujets matériels, reporter "
            "l'intégralité du standard ESRS correspondant."
        ),
    }

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"✓ Matrice double matérialité : {args.output}", file=sys.stderr)
        print(f"  → {len(sujets_materiels)}/{len(sujets)} sujets matériels", file=sys.stderr)
        print(f"  → Standards ESRS à reporter : {', '.join(standards_a_reporter)}", file=sys.stderr)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
