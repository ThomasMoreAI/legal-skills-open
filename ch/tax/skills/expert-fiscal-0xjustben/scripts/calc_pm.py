#!/usr/bin/env python3
"""calc_pm.py — Personal income tax calculator (Python parallel of scripts/calc.js).

Computes Swiss personal income tax: ICC (impôt cantonal et communal) + IFD (impôt fédéral direct).
Legal reference:
  - IFD : Loi sur l'impôt fédéral direct (LIFD, RS 642.11), barème art. 36 LIFD.
  - ICC : harmonisation par LHID (RS 642.14); barèmes cantonaux propres.

This is a SIMPLIFIED illustrative model. Real cantonal scales are piecewise and updated yearly.
External deps: stdlib only.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Literal, TypedDict

Marital = Literal["single", "married"]

# IFD 2024 simplified marginal brackets (CHF, art. 36 LIFD) — single taxpayer
IFD_BRACKETS_SINGLE = [
    (14_500, 0.00),
    (31_600, 0.0077),
    (41_400, 0.0088),
    (55_200, 0.0264),
    (72_500, 0.0297),
    (78_100, 0.0594),
    (103_600, 0.0660),
    (134_600, 0.0880),
    (176_000, 0.1100),
    (755_200, 0.1320),
    (float("inf"), 0.1150),  # flat above ceiling
]
IFD_BRACKETS_MARRIED = [
    (28_300, 0.00),
    (50_900, 0.01),
    (58_400, 0.02),
    (75_300, 0.03),
    (90_300, 0.04),
    (103_400, 0.05),
    (114_700, 0.06),
    (124_200, 0.07),
    (131_700, 0.08),
    (137_300, 0.09),
    (141_200, 0.10),
    (143_100, 0.11),
    (145_000, 0.12),
    (895_900, 0.13),
    (float("inf"), 0.1150),
]

# Very rough cantonal multipliers (coefficient cantonal + communal, ~%). Illustrative only.
CANTON_MULTIPLIER = {
    "GE": 1.55, "VD": 1.55, "ZH": 1.19, "BE": 1.54, "VS": 1.50,
    "FR": 1.50, "NE": 1.65, "JU": 1.95, "TI": 1.00, "BS": 1.00,
}


class CalcInput(TypedDict):
    canton: str
    marital: Marital
    income: float
    deductions: float


class CalcOutput(TypedDict):
    ICC: float
    IFD: float
    total: float
    taxableIncome: float


def _piecewise(brackets: list[tuple[float, float]], income: float) -> float:
    tax = 0.0
    prev = 0.0
    for ceiling, rate in brackets:
        if income <= ceiling:
            tax += (income - prev) * rate
            return max(tax, 0.0)
        tax += (ceiling - prev) * rate
        prev = ceiling
    return tax


def calc_pm(inp: CalcInput) -> CalcOutput:
    taxable = max(0.0, inp["income"] - inp["deductions"])
    brackets = IFD_BRACKETS_MARRIED if inp["marital"] == "married" else IFD_BRACKETS_SINGLE
    ifd = _piecewise(brackets, taxable)
    # ICC: approximate cantonal base tax = IFD * (canton multiplier * ratio). Illustrative.
    mult = CANTON_MULTIPLIER.get(inp["canton"].upper(), 1.40)
    icc_base = _piecewise(brackets, taxable) * 3.0  # cantonal "impôt de base" usually higher
    icc = icc_base * mult
    return {
        "ICC": round(icc, 2),
        "IFD": round(ifd, 2),
        "total": round(icc + ifd, 2),
        "taxableIncome": round(taxable, 2),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Compute Swiss personal income tax (ICC + IFD).")
    p.add_argument("--canton", required=True)
    p.add_argument("--marital", choices=["single", "married"], default="single")
    p.add_argument("--income", type=float, required=True)
    p.add_argument("--deductions", type=float, default=0.0)
    args = p.parse_args()
    out = calc_pm({"canton": args.canton, "marital": args.marital,
                   "income": args.income, "deductions": args.deductions})
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
