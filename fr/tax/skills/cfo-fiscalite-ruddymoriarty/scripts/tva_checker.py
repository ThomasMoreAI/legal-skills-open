#!/usr/bin/env python3
"""
tva_checker.py, vérifie la cohérence entre la balance comptable et la CA3 déclarée.

Input : balance (CSV) + CA3 déclarée (JSON) + taux appliqués
Output : écarts détectés + suggestions de régularisation
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def load_balance(path: Path) -> dict[str, float]:
    balance = {}
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                compte = row.get("compte") or row.get("CompteNum")
                debit = float((row.get("debit") or "0").replace(",", "."))
                credit = float((row.get("credit") or "0").replace(",", "."))
                balance[compte] = balance.get(compte, 0) + debit - credit
            except (ValueError, KeyError):
                continue
    return balance


def check_tva_coherence(balance: dict, ca3_declaree: dict, tolerance_pct: float = 1.0) -> dict:
    """Compare les soldes TVA en balance vs la CA3."""
    # Soldes TVA (en crédit pour collectée, débit pour déductible)
    tva_collectee_balance = -balance.get("44571", 0)  # crédit = solde positif
    tva_deductible_balance = balance.get("44566", 0) + balance.get("44562", 0)  # débit = solde positif
    tva_solde_net_balance = tva_collectee_balance - tva_deductible_balance

    # Valeurs CA3
    tva_collectee_ca3 = ca3_declaree.get("tva_collectee", 0)
    tva_deductible_ca3 = ca3_declaree.get("tva_deductible", 0)
    tva_solde_net_ca3 = tva_collectee_ca3 - tva_deductible_ca3

    # Écarts
    ecart_collectee = tva_collectee_balance - tva_collectee_ca3
    ecart_deductible = tva_deductible_balance - tva_deductible_ca3
    ecart_net = tva_solde_net_balance - tva_solde_net_ca3

    # Tolérance
    def is_within_tolerance(val, ref):
        if ref == 0:
            return abs(val) < 100  # 100€ de tolérance si ref = 0
        return abs(val / ref) * 100 < tolerance_pct

    alerts = []
    if not is_within_tolerance(ecart_collectee, tva_collectee_ca3):
        alerts.append(f"⚠️ Écart TVA collectée : balance {tva_collectee_balance:,.2f} € vs CA3 {tva_collectee_ca3:,.2f} € (écart {ecart_collectee:,.2f})")
    if not is_within_tolerance(ecart_deductible, tva_deductible_ca3):
        alerts.append(f"⚠️ Écart TVA déductible : balance {tva_deductible_balance:,.2f} € vs CA3 {tva_deductible_ca3:,.2f} € (écart {ecart_deductible:,.2f})")
    if not is_within_tolerance(ecart_net, tva_solde_net_ca3):
        alerts.append(f"🔴 Écart TVA NET : balance {tva_solde_net_balance:,.2f} € vs CA3 {tva_solde_net_ca3:,.2f} € (écart {ecart_net:,.2f})")

    return {
        "_version": "0.1.0",
        "balance": {
            "tva_collectee": round(tva_collectee_balance, 2),
            "tva_deductible": round(tva_deductible_balance, 2),
            "tva_net_a_payer": round(tva_solde_net_balance, 2),
        },
        "ca3_declaree": {
            "tva_collectee": tva_collectee_ca3,
            "tva_deductible": tva_deductible_ca3,
            "tva_net_a_payer": round(tva_solde_net_ca3, 2),
        },
        "ecarts": {
            "collectee": round(ecart_collectee, 2),
            "deductible": round(ecart_deductible, 2),
            "net": round(ecart_net, 2),
        },
        "tolerance_pct": tolerance_pct,
        "coherent": len(alerts) == 0,
        "alerts": alerts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Vérification cohérence TVA")
    parser.add_argument("--balance", type=Path, required=True)
    parser.add_argument("--ca3", type=Path, required=True,
                        help="JSON : {tva_collectee, tva_deductible}")
    parser.add_argument("--tolerance-pct", type=float, default=1.0)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    if not args.balance.exists():
        print(f"❌ Fichier balance introuvable : {args.balance}", file=sys.stderr)
        return 1
    if not args.ca3.exists():
        print(f"❌ Fichier CA3 introuvable : {args.ca3}", file=sys.stderr)
        return 1

    try:
        balance = load_balance(args.balance)
        ca3 = json.loads(args.ca3.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"❌ Erreur de lecture : {e}", file=sys.stderr)
        return 1

    result = check_tva_coherence(balance, ca3, args.tolerance_pct)

    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        status = "✓ cohérent" if result["coherent"] else "⚠️ incohérence"
        print(f"{status}, {len(result['alerts'])} alerte(s)", file=sys.stderr)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
