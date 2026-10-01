#!/usr/bin/env python3
"""
cir_estimator.py, estime le CIR éligible pour un projet R&D.

Input : dépenses R&D ventilées (salaires chercheurs, sous-traitance, amortissements, brevets)
Output : CIR estimé + avertissements sur les points à risque
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def estimate_cir(
    salaires_chercheurs: float,
    frais_fonctionnement_pct: float,
    sous_traitance_agreee: float,
    amortissements_rd: float,
    frais_brevets: float,
    veille_technologique: float,
) -> dict:
    """Calcul CIR selon art. 244 quater B CGI."""
    # Frais de fonctionnement = % forfaitaire sur salaires (typiquement 43% ou 75% pour PME récent)
    frais_fonctionnement = salaires_chercheurs * frais_fonctionnement_pct / 100

    # Plafonds
    veille_plafonnee = min(veille_technologique, 60000)

    depenses_eligibles = (
        salaires_chercheurs
        + frais_fonctionnement
        + sous_traitance_agreee
        + amortissements_rd
        + frais_brevets
        + veille_plafonnee
    )

    # Taux : 30% jusqu'à 100M€, 5% au-delà
    if depenses_eligibles <= 100_000_000:
        cir = depenses_eligibles * 0.30
    else:
        cir = 100_000_000 * 0.30 + (depenses_eligibles - 100_000_000) * 0.05

    warnings = []
    if salaires_chercheurs == 0:
        warnings.append("⚠️ Sans salaires chercheurs, le CIR est très faible, vérifiez l'éligibilité de l'activité comme R&D")
    if sous_traitance_agreee > salaires_chercheurs * 2:
        warnings.append("⚠️ Sous-traitance > 2× salaires internes : vérifier plafond (limité à 2× dépenses internes)")
    if veille_technologique > 60000:
        warnings.append(f"ℹ️ Veille technologique plafonnée à 60 000 € (dépense {veille_technologique:,.0f} € → retenue {veille_plafonnee:,.0f} €)")
    if not frais_brevets and depenses_eligibles > 100000:
        warnings.append("💡 Pas de frais de brevets déclarés : si vous innovez, envisagez de déposer un brevet (déductible + preuve de nouveauté)")

    return {
        "depenses_eligibles_detail": {
            "salaires_chercheurs": salaires_chercheurs,
            "frais_fonctionnement_forfait": round(frais_fonctionnement, 2),
            "sous_traitance_agreee": sous_traitance_agreee,
            "amortissements_rd": amortissements_rd,
            "frais_brevets": frais_brevets,
            "veille_technologique_retenue": round(veille_plafonnee, 2),
        },
        "total_depenses_eligibles": round(depenses_eligibles, 2),
        "taux_applique": "30% (< 100M€)" if depenses_eligibles <= 100_000_000 else "30% < 100M€ + 5% au-delà",
        "cir_estime": round(cir, 2),
        "warnings": warnings,
        "articulation_cii_avis": "Si vous avez aussi des phases prototype / pilote pré-commercial, envisagez le CII (20% additionnel sur ces phases, plafond 400k€ de dépenses).",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimation CIR")
    parser.add_argument("--salaires-chercheurs", type=float, required=True)
    parser.add_argument("--frais-fonctionnement-pct", type=float, default=43.0,
                        help="Forfait frais fonctionnement (défaut 43%%, PME récent 75%%)")
    parser.add_argument("--sous-traitance-agreee", type=float, default=0)
    parser.add_argument("--amortissements-rd", type=float, default=0)
    parser.add_argument("--frais-brevets", type=float, default=0)
    parser.add_argument("--veille-technologique", type=float, default=0)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    result = estimate_cir(
        args.salaires_chercheurs,
        args.frais_fonctionnement_pct,
        args.sous_traitance_agreee,
        args.amortissements_rd,
        args.frais_brevets,
        args.veille_technologique,
    )

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"✓ CIR estimé : {result['cir_estime']:,.0f} € sur {result['total_depenses_eligibles']:,.0f} € de dépenses", file=sys.stderr)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
