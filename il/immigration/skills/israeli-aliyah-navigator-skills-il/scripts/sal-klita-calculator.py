#!/usr/bin/env python3
"""
Sal Klita (absorption basket) calculator, 2026 rates.

Source of every number below: Ministry of Aliyah and Integration, "סל קליטה"
(https://www.gov.il/he/pages/absorption_basket), page updated 27.07.2026,
tables "לוח סיוע כספי בסל הקליטה" (three tracks) and "לוח תוספות לסל קליטה".
The tables are transcribed verbatim. Do NOT interpolate, index, or "estimate"
these amounts: if the year changes, re-read the page and replace the table.

Structure of the basket (identical in all three tracks):
  1. Ben Gurion payment, loaded onto a prepaid card on arrival (olim who change
     status inside Israel get it as a bank deposit instead).
  2. A one-time "bank top-up" (השלמה לחשבון בנק), paid into the Israeli bank
     account. It is a separate line, not part of the monthly instalments.
  3. Six monthly instalments. There is NO seventh payment: after month 6 the
     oleh is checked for income support (havtachat hachnasa), not another
     basket payment.

Tracks:
  standard    -- working-age oleh
  pre-pension -- reaches the statutory retirement age within 5 years of aliyah
  pensioner   -- already at the statutory retirement age set by law
Note the tracks key off the STATUTORY retirement age (67 for men; 62-65 for
women by birth year), not off age 65.

Usage:
    python scripts/sal-klita-calculator.py --status single
    python scripts/sal-klita-calculator.py --status couple --child-ages 3,9,17
    python scripts/sal-klita-calculator.py --status single --track pensioner
    python scripts/sal-klita-calculator.py --example
"""

import argparse
import sys

YEAR = 2026
SOURCE = "https://www.gov.il/he/pages/absorption_basket (updated 27.07.2026)"

# track -> status -> (airport, bank_top_up, monthly, published_total)
BASKET = {
    "standard": {
        "single": (1250, 1544, 3150, 21694),
        "single-parent": (2300, 1631, 5190, 35071),
        "couple": (2500, 4023, 5806, 41359),
    },
    "pre-pension": {
        "single": (1250, 1583, 3992, 26785),
        "single-parent": (2300, 1690, 6201, 41196),
        "couple": (2500, 3904, 7414, 50888),
    },
    "pensioner": {
        "single": (1250, 2305, 3204, 22779),
        "single-parent": (2300, 1606, 4030, 28086),
        "couple": (2500, 3785, 4663, 34263),
    },
}

# Child supplements (added to the family's basket; a minor never has a basket
# of their own). key -> (airport, bank_top_up, monthly, published_total)
CHILD_SUPPLEMENT = {
    "0-4": (250, 3095, 1581, 12831),
    "4-18": (250, 3051, 870, 8521),
    "18-21": (250, 3106, 1324, 11039),
}

# Supplement for a household of 6 or more people. No airport / bank line.
LARGE_FAMILY_SUPPLEMENT = (0, 0, 986, 5918)

MONTHS = 6


def child_band(age: int) -> str:
    if age < 4:
        return "0-4"
    if age < 18:
        return "4-18"
    if age <= 21:
        return "18-21"
    return ""


def line_total(row) -> int:
    airport, top_up, monthly, published = row
    computed = airport + top_up + monthly * MONTHS
    if computed != published:
        # The ministry's own published total wins. Two of its rows are a few
        # shekels off their component sum (rounding inside the ministry table):
        # the 18-21 child row and the large-family row. Report the gap instead
        # of silently choosing one of the two numbers.
        print(
            f"Note: ministry rounding: {airport} + {top_up} + 6 x {monthly} = {computed}, "
            f"but the published total for this row is {published}. Using the published total.",
            file=sys.stderr,
        )
    return published


def calculate(status: str, track: str, child_ages, household_size: int) -> dict:
    row = BASKET[track][status]
    adults = 1 if status in ("single", "single-parent") else 2
    if household_size is None:
        household_size = adults + len(child_ages)

    parts = [(f"Base basket ({status}, {track})", row)]
    for age in child_ages:
        band = child_band(age)
        if not band:
            print(
                f"Note: a child aged {age} is outside the supplement bands (0-21) "
                "and adds nothing to the basket.",
                file=sys.stderr,
            )
            continue
        parts.append((f"Child aged {age} (band {band})", CHILD_SUPPLEMENT[band]))

    if household_size >= 6:
        parts.append(("Household of 6 or more", LARGE_FAMILY_SUPPLEMENT))

    total = sum(line_total(p[1]) for p in parts)
    airport = sum(p[1][0] for p in parts)
    top_up = sum(p[1][1] for p in parts)
    monthly = sum(p[1][2] for p in parts)
    return {
        "parts": parts,
        "airport": airport,
        "bank_top_up": top_up,
        "monthly": monthly,
        "months": MONTHS,
        "total": total,
        "household_size": household_size,
    }


def report(r: dict) -> None:
    print(f"Sal Klita estimate, {YEAR} rates")
    print(f"Household size: {r['household_size']}")
    print()
    print("Components:")
    for label, (a, t, m, tot) in r["parts"]:
        print(f"  {label}: airport {a:,} + bank top-up {t:,} + 6 x {m:,} = {tot:,} NIS")
    print()
    print(f"  Ben Gurion prepaid card (on arrival): {r['airport']:,} NIS")
    print(f"  One-time bank top-up:                 {r['bank_top_up']:,} NIS")
    print(f"  Monthly instalment (x6):              {r['monthly']:,} NIS")
    print(f"  TOTAL over the 6-month basket:        {r['total']:,} NIS")
    print()
    print("Notes:")
    print("  * There is NO 7th payment for anyone. Month 7 is where the post-basket")
    print("    entitlements begin (rent assistance, havtachat kiyum), not another")
    print("    instalment.")
    print("  * The bank top-up requires an Israeli account (a JOINT account for a couple);")
    print("    give the account details to Misrad HaAliyah VeHaKlita.")
    print("  * The basket is NOT income-tested.")
    print("  * Register within one year of receiving oleh status.")
    print("  * This covers the SIX-MONTH basket only. Rent assistance (from month 7),")
    print("    havtachat kiyum, the special old-age pension and the daycare subsidy")
    print("    are separate and are NOT in this total. See")
    print("    references/post-basket-entitlements.md.")
    print("  * A child crossing a band (4 or 18) during the six months is not")
    print("    modelled here; check the month the band changes.")
    print("  * Aliyah BeNifrad (family arriving at different times within a year) is")
    print("    not modelled: the basket is per FAMILY unit and later arrivals receive")
    print("    only the remainder.")
    print("  * Leaving Israel STOPS the payments; they resume only if you return within")
    print("    the first aliyah year.")
    print("  * The track is set by the STATUTORY retirement age, not by age 65.")
    print(f"  * Source: {SOURCE}")


def main() -> int:
    p = argparse.ArgumentParser(
        description="Calculate the 2026 sal klita (absorption basket) for a new oleh.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--status", choices=["single", "single-parent", "couple"], default="single")
    p.add_argument(
        "--track",
        choices=["standard", "pre-pension", "pensioner"],
        default="standard",
        help="pre-pension = reaches statutory retirement age within 5 years of aliyah; "
        "pensioner = already at the statutory retirement age",
    )
    p.add_argument(
        "--child-ages",
        default="",
        help="comma-separated ages of children, e.g. 2,7,19 (bands: 0-4, 4-18, 18-21)",
    )
    p.add_argument(
        "--household-size",
        type=int,
        default=None,
        help="total people in the household; 6 or more adds the large-family supplement",
    )
    p.add_argument("--example", action="store_true", help="run a worked example")
    a = p.parse_args()

    if a.example:
        print("Example: couple with children aged 3 and 9, standard track\n")
        report(calculate("couple", "standard", [3, 9], None))
        return 0

    ages = []
    for raw in a.child_ages.split(","):
        raw = raw.strip()
        if not raw:
            continue
        try:
            age = int(raw)
        except ValueError:
            p.error(
                f"--child-ages expects whole years separated by commas; got {raw!r}. "
                "Use digits only (for example: 3,9,17)."
            )
        if age < 0:
            p.error(f"--child-ages got a negative age ({age}). Ages start at 0.")
        ages.append(age)

    if ages and a.status == "single":
        p.error(
            "--status single with --child-ages: a lone adult with a child is a "
            "single-parent household (הורה עצמאי) and belongs on the "
            "'single-parent' track, which pays a different and substantially "
            "larger basket. Re-run with --status single-parent, or drop "
            "--child-ages if the children are not in the household."
        )
    report(calculate(a.status, a.track, ages, a.household_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
