#!/usr/bin/env python3
"""Estimate the Pikadon and discharge grant for a recently-discharged Israeli soldier.

Rates indexed to May 2026 values from hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5.
THE RATES CHANGE MONTHLY WITH CPI. Always verify the personalized amount against the
official calculator before any user makes financial plans.

Usage:
  python pikadon-calculator.py --service-type lochem --months 32 --gender male
  python pikadon-calculator.py --service-type tomech-lechima --months 30 --gender male
  python pikadon-calculator.py --service-type acher --months 24 --gender female
  python pikadon-calculator.py --service-type sle --months 18 --gender female
"""

import argparse
import sys

# Monthly rates published by the MoD, updated May 2026.
# Source: hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5 (pikadon) and .../Grant (grant).
PIKADON_RATES = {
    "lochem": 990.63,
    "tomech-lechima": 825.52,
    "acher": 660.42,
    "sle": 660.42,
    "ezrachi-beinayim": 495.38,   # מסלול אזרחי ביניים
    "ezrachi-mefutzal": 330.25,   # מסלול אזרחי מפוצל
}

GRANT_RATES = {
    "lochem": 684.99,
    "tomech-lechima": 570.42,
    "acher": 455.84,
    "sle": 455.84,
    "ezrachi-beinayim": 342.50,
    "ezrachi-mefutzal": 227.92,
}

# Basic training at the start of service is credited at a LOWER tier than the
# role actually served. The MoD states this explicitly: a combat soldier's first
# 4 training months count as combat support, and a combat-support soldier's
# first 2 training months count as "other". Ignoring this over-states a combat
# soldier's pikadon by roughly 660 NIS.
TRAINING_RECLASSIFICATION = {
    "lochem": (4, "tomech-lechima"),
    "tomech-lechima": (2, "acher"),
}

ACCRUAL_CAP = {"male": 32, "female": 24}

# A lochem or tomech lechima wounded during, or as a result of, training or
# operational activity who then moved to another role keeps the HIGHER rate for
# the whole service period. This script cannot detect that, so callers must pass
# the pre-injury service type for such a case; the printed note says so.
WOUNDED_KEEPS_HIGHER_RATE = True

NEKUDOT_ZIKUI_VALUE_PER_POINT_PER_MONTH_2026 = 242


def accrue(rates: dict, service_type: str, effective_months: int) -> tuple[float, list[str]]:
    """Sum an accrual over the service, applying the training reclassification."""
    breakdown: list[str] = []
    total = 0.0
    remaining = effective_months
    if service_type in TRAINING_RECLASSIFICATION:
        train_months, train_tier = TRAINING_RECLASSIFICATION[service_type]
        t = min(remaining, train_months)
        if t:
            total += t * rates[train_tier]
            breakdown.append(f"{t} training month(s) at the {train_tier} rate ({rates[train_tier]})")
            remaining -= t
    if remaining:
        total += remaining * rates[service_type]
        breakdown.append(f"{remaining} month(s) at the {service_type} rate ({rates[service_type]})")
    return round(total, 2), breakdown


def compute_pikadon(service_type: str, months: int, gender: str,
                    medical_discharge: bool = False,
                    hesder_total_months: int | None = None) -> dict:
    if service_type not in PIKADON_RATES:
        raise ValueError(f"Unknown service-type {service_type!r}. Valid: {list(PIKADON_RATES)}")
    if gender not in ACCRUAL_CAP:
        raise ValueError(f"Unknown gender {gender!r}. Valid: male, female")
    if months < 0:
        raise ValueError("months must be non-negative")

    # The 32/24 caps in s.11(a) are caps on SHERUT SADIR. They do not govern the
    # national-service and civilian tracks, so don't silently truncate those.
    civilian_track = service_type in ("sle", "ezrachi-beinayim", "ezrachi-mefutzal")
    cap = None if civilian_track else ACCRUAL_CAP[gender]
    effective_months = months if cap is None else min(months, cap)
    rate = PIKADON_RATES[service_type]
    pikadon, pikadon_breakdown = accrue(PIKADON_RATES, service_type, effective_months)
    grant, grant_breakdown = accrue(GRANT_RATES, service_type, effective_months)

    # Nekudot zikui thresholds differ by service population:
    #   Male IDF/MAGAV/Police/SHABAS: ≥23 months => 2 points
    #   Female IDF/MAGAV/Police/SHABAS: ≥22 months => 2 points
    #   SLE (any gender): ≥24 months => 2 points
    # Credit-point months are NOT the same quantity as Pikadon months:
    #  - an early discharge on medical grounds is deemed to have completed 12
    #  - hesder/SHLAT counts total service from enlistment, not paid months only
    # Both are caller-declared because the script cannot infer either.
    counted = 12 if (medical_discharge and months < 12) else months
    if hesder_total_months is not None:
        counted = hesder_total_months
    if service_type == "sle":
        points_per_year = 2 if counted >= 24 else (1 if counted >= 12 else 0)
    elif gender == "male":
        points_per_year = 2 if counted >= 23 else (1 if counted >= 12 else 0)
    else:
        points_per_year = 2 if counted >= 22 else (1 if counted >= 12 else 0)

    monthly_credit = NEKUDOT_ZIKUI_VALUE_PER_POINT_PER_MONTH_2026 * points_per_year
    total_36_months = monthly_credit * 36

    return {
        "service_type": service_type,
        "months_input": months,
        "months_effective": effective_months,
        "cap_applied": cap is not None and months > cap,
        "rate_per_month_nis": rate,
        "pikadon_estimate_nis": pikadon,
        "pikadon_breakdown": pikadon_breakdown,
        "grant_estimate_nis": grant,
        "grant_breakdown": grant_breakdown,
        "nekudot_zikui_points_per_year": points_per_year,
        "nekudot_zikui_monthly_credit_nis": monthly_credit,
        "nekudot_zikui_total_over_36_months_nis": total_36_months,
        "note": "MoD rates as published May 2026, with the training reclassification applied. A soldier wounded in training or operational activity who moved to another role keeps the higher pre-injury rate for the whole service, so pass the pre-injury service type in that case. Verify on the hachvana.mod.gov.il official calculator before any financial decision.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--service-type", required=True, choices=list(PIKADON_RATES.keys()))
    parser.add_argument("--months", required=True, type=int, help="Months of paid service")
    parser.add_argument("--gender", required=True, choices=["male", "female"])
    parser.add_argument("--medical-discharge", action="store_true",
                        help="Early discharge on health grounds: deemed to have completed 12 "
                             "months for the credit-point threshold (does NOT change the Pikadon, "
                             "which stays pro-rata on months actually served)")
    parser.add_argument("--hesder-total-months", type=int, default=None,
                        help="Hesder/SHLAT: total service months from enlistment to discharge. "
                             "Unpaid service does not accrue Pikadon but DOES count toward the "
                             "credit-point threshold, so pass paid months in --months and the "
                             "total here")
    args = parser.parse_args()

    try:
        result = compute_pikadon(args.service_type, args.months, args.gender,
                                 medical_discharge=args.medical_discharge,
                                 hesder_total_months=args.hesder_total_months)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    print("Pikadon and discharge-grant estimate (MoD rates, May 2026):")
    print(f"  Service type:                       {result['service_type']}")
    cap_note = (f"cap {ACCRUAL_CAP[args.gender]} for {args.gender}"
                if args.service_type not in ("sle", "ezrachi-beinayim", "ezrachi-mefutzal")
                else "no sherut-sadir cap on this track")
    print(f"  Months input / effective:           {result['months_input']} / {result['months_effective']} ({cap_note})")
    if result["cap_applied"]:
        print(f"  NOTE: Months exceeded cap; extra service does not accrue Pikadon")
    print(f"  Rate per month (served role):       {result['rate_per_month_nis']} NIS")
    print(f"  Pikadon estimate:                   {result['pikadon_estimate_nis']:,.2f} NIS")
    for line in result["pikadon_breakdown"]:
        print(f"      {line}")
    print(f"  Discharge grant estimate:           {result['grant_estimate_nis']:,.2f} NIS")
    for line in result["grant_breakdown"]:
        print(f"      {line}")
    print()
    print("Nekudot zikui (Section 39a) over 36 months from month after discharge:")
    print(f"  Points per year:                    {result['nekudot_zikui_points_per_year']}")
    print(f"  Monthly tax credit:                 {result['nekudot_zikui_monthly_credit_nis']} NIS")
    print(f"  Total over 36 months:               {result['nekudot_zikui_total_over_36_months_nis']:,} NIS")
    print()
    print("REMINDER:")
    print("  - Pikadon rates are indexed monthly to CPI. Verify on the official calculator")
    print("    at https://www.hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5/Pages/default.aspx")
    print("  - Nekudot zikui reduce tax owed but cannot exceed liability and do not refund as cash.")
    print("  - Submit Tofes 101 to employer + Teudat Shichrur to start receiving the credit.")
    print("  - If employer never applied: file Tofes 135 retroactive (up to 6 years back).")


if __name__ == "__main__":
    main()
