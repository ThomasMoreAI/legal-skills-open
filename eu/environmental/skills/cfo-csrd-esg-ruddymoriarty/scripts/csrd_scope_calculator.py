#!/usr/bin/env python3
"""
csrd_scope_calculator.py, détermine la wave CSRD applicable.

Input : critères société (effectif, CA, bilan, coté, PIE, hors-UE)
Output : wave (1, 2, 3, 4, hors_scope) + premier exercice à reporter
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def determiner_wave(effectif: int, ca_eur: float, bilan_eur: float, coté: bool, pie: bool, hors_ue_groupe: bool, ca_ue_eur: float = 0) -> dict:
    """Détermine la wave CSRD applicable."""

    # Wave 1 : grandes entités cotées et PIE
    if pie and effectif >= 500 and (ca_eur >= 50_000_000 or bilan_eur >= 25_000_000):
        return {
            "wave": "wave_1",
            "label": "Wave 1 - Grandes entités cotées et PIE",
            "premier_exercice_reporté": 2024,
            "premier_rapport_publié": 2025,
            "statut": "déjà obligatoire",
            "note": "Si pas encore reporté, urgence absolue.",
        }

    # Wave 2 : grandes entités non cotées
    critères_wave2 = [effectif >= 250, ca_eur >= 50_000_000, bilan_eur >= 25_000_000]
    if sum(critères_wave2) >= 2:
        return {
            "wave": "wave_2",
            "label": "Wave 2 - Grandes entités non cotées + mid-caps",
            "premier_exercice_reporté": 2028,
            "premier_rapport_publié": 2029,
            "statut": "préparation 2026-2027 recommandée",
            "note": "Reportée à 2028 par directive (UE) 2025/794 Stop-the-Clock du 14/04/2025.",
        }

    # Wave 3 : PME cotées
    critères_wave3 = [ca_eur >= 900_000, bilan_eur >= 450_000]
    if coté and 10 <= effectif <= 250 and sum(critères_wave3) >= 2:
        return {
            "wave": "wave_3",
            "label": "Wave 3 - PME cotées (ESRS-LSME standard simplifié)",
            "premier_exercice_reporté": 2028,
            "premier_rapport_publié": 2029,
            "statut": "préparation 2026-2027 recommandée",
            "note": "Standard simplifié ESRS-LSME applicable.",
        }

    # Wave 4 : groupes hors UE
    if hors_ue_groupe and ca_ue_eur >= 150_000_000:
        return {
            "wave": "wave_4",
            "label": "Wave 4 - Groupes hors UE avec CA UE > 150 M€",
            "premier_exercice_reporté": 2028,
            "premier_rapport_publié": 2029,
            "statut": "préparation requise",
            "note": "Filiale UE significative ou succursale.",
        }

    # Hors scope
    return {
        "wave": "hors_scope",
        "label": "Hors scope CSRD",
        "premier_exercice_reporté": None,
        "premier_rapport_publié": None,
        "statut": "non obligatoire",
        "note": (
            "Démarche volontaire recommandée si vos clients sont in-scope "
            "(ils vous demanderont les données Scope 3) ou si vous visez des "
            "financements green/impact. Aides publiques disponibles (ADEME, BPI Climat, "
            "France 2030), voir cfo-financement-croissance pour la passerelle Moriarty."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Détermine la wave CSRD")
    parser.add_argument("--effectif", type=int, required=True)
    parser.add_argument("--ca-eur", type=float, required=True)
    parser.add_argument("--bilan-eur", type=float, required=True)
    parser.add_argument("--coté", action="store_true", help="Société cotée")
    parser.add_argument("--pie", action="store_true",
                        help="Public Interest Entity (cotée OU banque/assurance/établissement paiement)")
    parser.add_argument("--hors-ue-groupe", action="store_true",
                        help="Groupe hors UE avec activité significative en UE")
    parser.add_argument("--ca-ue-eur", type=float, default=0,
                        help="CA UE pour groupes hors UE")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    result = determiner_wave(
        args.effectif, args.ca_eur, args.bilan_eur,
        args.coté, args.pie, args.hors_ue_groupe, args.ca_ue_eur,
    )

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"✓ Wave CSRD : {result['wave']}", file=sys.stderr)
        print(f"  → {result['label']}", file=sys.stderr)
        if result["premier_exercice_reporté"]:
            print(f"  → Premier rapport publié en : {result['premier_rapport_publié']}", file=sys.stderr)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
