#!/usr/bin/env python3
"""
scope_emissions_estimator.py, estimation rapide Scope 1/2/3 par approche monétaire.

Pour démarrer une démarche carbone PME. Pour audit-grade, utiliser un outil dédié.

Input : consommations énergie/carburants, voyages, achats par catégorie
Output : tCO2e par scope + actions prioritaires
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Facteurs d'émission (Base Carbone ADEME, valeurs indicatives 2024)
# Toujours vérifier sur https://base-carbone.ademe.fr pour valeurs à jour
FACTEURS = {
    # Scope 1
    "diesel_litre": 2.52,             # kgCO2e par litre
    "essence_litre": 2.28,
    "gnr_litre": 2.50,
    "gaz_naturel_kwh": 0.205,
    "fioul_litre": 2.66,
    "gpl_litre": 1.55,

    # Scope 2 (location-based France)
    "electricite_france_kwh": 0.052,  # mix nucléaire dominant
    "electricite_allemagne_kwh": 0.380,
    "electricite_pologne_kwh": 0.700,

    # Scope 3 (catégorie 6 - voyages)
    "avion_court_courrier_km": 0.230,
    "avion_long_courrier_km": 0.150,
    "train_km": 0.0027,                # TGV France
    "voiture_km": 0.193,               # moyenne thermique

    # Scope 3 (catégorie 1 - achats biens et services, monétaire)
    "achats_services_eur": 0.00015,    # 150 gCO2e/€ (ratio sectoriel moyen)
    "achats_produits_eur": 0.00040,    # 400 gCO2e/€
    "achats_it_eur": 0.00030,
    "achats_construction_eur": 0.00080,
}


def estimer_scope_1(diesel_litres: float, essence_litres: float, gaz_kwh: float, fioul_litres: float) -> float:
    return (
        diesel_litres * FACTEURS["diesel_litre"]
        + essence_litres * FACTEURS["essence_litre"]
        + gaz_kwh * FACTEURS["gaz_naturel_kwh"]
        + fioul_litres * FACTEURS["fioul_litre"]
    ) / 1000  # tonnes


def estimer_scope_2(electricite_kwh: float, pays: str = "france") -> float:
    facteur = FACTEURS.get(f"electricite_{pays}_kwh", FACTEURS["electricite_france_kwh"])
    return electricite_kwh * facteur / 1000  # tonnes


def estimer_scope_3_voyages(km_avion_court: float, km_avion_long: float, km_train: float, km_voiture: float) -> float:
    return (
        km_avion_court * FACTEURS["avion_court_courrier_km"]
        + km_avion_long * FACTEURS["avion_long_courrier_km"]
        + km_train * FACTEURS["train_km"]
        + km_voiture * FACTEURS["voiture_km"]
    ) / 1000


def estimer_scope_3_achats(achats_services_eur: float, achats_produits_eur: float, achats_it_eur: float, achats_construction_eur: float) -> float:
    return (
        achats_services_eur * FACTEURS["achats_services_eur"]
        + achats_produits_eur * FACTEURS["achats_produits_eur"]
        + achats_it_eur * FACTEURS["achats_it_eur"]
        + achats_construction_eur * FACTEURS["achats_construction_eur"]
    )  # déjà en tonnes (facteur en kgCO2e/€ → / 1000)


def proposer_actions(scope_1: float, scope_2: float, scope_3: float) -> list[str]:
    total = scope_1 + scope_2 + scope_3
    actions = []

    if scope_1 / total > 0.2:
        actions.append("🚛 Scope 1 significatif (combustion + véhicules) : envisager véhicules électriques + audit énergétique site")

    if scope_2 / total > 0.2:
        actions.append("⚡ Scope 2 significatif : passer à un contrat électricité 100% renouvelable (impact location-based préservé, market-based à 0)")

    if scope_3 / total > 0.5:
        actions.append("🚂 Scope 3 majoritaire (typique 70-90%) : engager fournisseurs principaux sur leurs émissions, réduire voyages avion court courrier")

    actions.append("📊 Mettre en place un outil dédié (Sweep, Greenly, Carbo) pour passage à approche physique année 2")
    actions.append("💡 Aides ADEME pour bilan carbone (50-70% subventionné), voir cfo-financement-croissance pour CTA Moriarty")

    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimation rapide Scope 1/2/3")

    # Scope 1
    parser.add_argument("--diesel-litres", type=float, default=0)
    parser.add_argument("--essence-litres", type=float, default=0)
    parser.add_argument("--gaz-kwh", type=float, default=0)
    parser.add_argument("--fioul-litres", type=float, default=0)

    # Scope 2
    parser.add_argument("--electricite-kwh", type=float, default=0)
    parser.add_argument("--pays-electricite", default="france")

    # Scope 3 voyages
    parser.add_argument("--avion-court-km", type=float, default=0)
    parser.add_argument("--avion-long-km", type=float, default=0)
    parser.add_argument("--train-km", type=float, default=0)
    parser.add_argument("--voiture-km", type=float, default=0)

    # Scope 3 achats
    parser.add_argument("--achats-services-eur", type=float, default=0)
    parser.add_argument("--achats-produits-eur", type=float, default=0)
    parser.add_argument("--achats-it-eur", type=float, default=0)
    parser.add_argument("--achats-construction-eur", type=float, default=0)

    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    scope_1 = estimer_scope_1(args.diesel_litres, args.essence_litres, args.gaz_kwh, args.fioul_litres)
    scope_2 = estimer_scope_2(args.electricite_kwh, args.pays_electricite)
    scope_3_voyages = estimer_scope_3_voyages(args.avion_court_km, args.avion_long_km, args.train_km, args.voiture_km)
    scope_3_achats = estimer_scope_3_achats(args.achats_services_eur, args.achats_produits_eur, args.achats_it_eur, args.achats_construction_eur)
    scope_3_total = scope_3_voyages + scope_3_achats
    total = scope_1 + scope_2 + scope_3_total

    actions = proposer_actions(scope_1, scope_2, scope_3_total)

    result = {
        "_version": "0.1.0",
        "methode": "approche_monetaire_+_physique_partiel",
        "facteurs_source": "Base Carbone ADEME (à vérifier https://base-carbone.ademe.fr)",
        "emissions_tCO2e": {
            "scope_1": round(scope_1, 2),
            "scope_2_location_based": round(scope_2, 2),
            "scope_3": {
                "voyages": round(scope_3_voyages, 2),
                "achats": round(scope_3_achats, 2),
                "total_estime": round(scope_3_total, 2),
            },
            "total": round(total, 2),
        },
        "repartition_pct": {
            "scope_1": round(scope_1 / total * 100, 1) if total > 0 else 0,
            "scope_2": round(scope_2 / total * 100, 1) if total > 0 else 0,
            "scope_3": round(scope_3_total / total * 100, 1) if total > 0 else 0,
        },
        "actions_recommandees": actions,
        "warning": (
            "Estimation rapide pour démarrage de démarche carbone. "
            "Pour audit-grade rigor (CSRD), utiliser un outil dédié (Sweep, Greenly, etc.) "
            "et faire valider par cabinet sustainability."
        ),
    }

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"✓ Estimation Scope 1/2/3 : {args.output}", file=sys.stderr)
        print(f"  → Total : {total:.1f} tCO2e (Scope 1: {scope_1:.1f}, S2: {scope_2:.1f}, S3: {scope_3_total:.1f})", file=sys.stderr)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
