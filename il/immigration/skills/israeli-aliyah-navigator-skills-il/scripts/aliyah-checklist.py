#!/usr/bin/env python3
"""
Aliyah Checklist Generator

Generates a personalized checklist for new immigrants (olim) to Israel
based on their specific situation: current stage, family status,
country of origin, and profession.

Usage:
    python scripts/aliyah-checklist.py --stage pre-arrival --family single --country usa --profession tech
    python scripts/aliyah-checklist.py --stage first-week --family family --country france --profession medical
    python scripts/aliyah-checklist.py --help
"""

import argparse
import sys
from datetime import datetime


STAGES = ["pre-arrival", "first-week", "first-month", "first-year", "beyond"]
FAMILY_TYPES = ["single", "couple", "family"]
COUNTRIES = ["usa", "canada", "uk", "france", "russia", "ukraine", "south-africa",
             "ethiopia", "argentina", "brazil", "australia", "other"]
PROFESSIONS = ["medical", "engineering", "law", "accounting", "teaching",
               "tech", "trades", "academic", "other"]

# Countries with Nefesh B'Nefesh support
NBN_COUNTRIES = {"usa", "canada", "uk"}

# Driver's licence conversion does NOT depend on the country of issue. That
# system was replaced in August 2017 by an experience-based rule, so this script
# deliberately keeps no country list: an oleh from Ethiopia or Brazil with 8
# years' seniority has exactly the same entitlement as one from the USA.
#
# The rule (kolzchut "המרת רישיון נהיגה זר לרישיון נהיגה ישראלי"):
#   5+ years on the foreign licence AND target category 1/A/A1/A2/B
#       -> administrative conversion, no test
#   under 5 years, or any other category
#       -> full practical driving test (test). Theory only after failing twice.
#   under 2 years
#       -> also classified nahag chadash (new driver)
# The conversion window is 5 years in Israel. Separately, the foreign licence
# may be used to drive for 1 year from the date of entry. Two different clocks.
LICENSE_RULE = (
    "conversion depends on YEARS OF EXPERIENCE and licence category, not on "
    "country of issue; 5+ years and category 1/A/A1/A2/B = no test, "
    "otherwise a full practical test"
)


def get_pre_arrival_checklist(family: str, country: str, profession: str) -> list:
    """Generate pre-arrival tasks."""
    tasks = [
        ("HIGH", "Open file with Jewish Agency (Sochnut)"),
        ("HIGH", "Schedule appointment at Israeli consulate"),
        ("HIGH", "Gather proof of Jewish identity documents"),
        ("HIGH", "Ensure passport has at least 2 years of validity left"),
        ("HIGH", "Obtain police clearance from country of origin"),
        ("HIGH", "Get apostille on professional diplomas and transcripts"),
        ("MED", "Obtain certified translations of key documents (Hebrew or English)"),
        ("MED", "Research kupat cholim options (Clalit, Maccabi, Meuhedet, Leumit)"),
        ("MED", "Notify banks about upcoming international transfers"),
        ("MED", "Download Israeli banking apps and gov service apps"),
        ("LOW", "Research neighborhoods and housing options"),
        ("LOW", "Join olim Facebook groups for your destination city"),
    ]

    if country in NBN_COUNTRIES:
        tasks.insert(1, ("HIGH", "Register with Nefesh B'Nefesh (nbn.org.il) for free aliyah assistance"))
        tasks.append(("MED", "Apply for Nefesh B'Nefesh group flight"))
        tasks.append(("MED", "Attend NBN pre-aliyah employment webinar"))

    if family == "family":
        tasks.append(("HIGH", "Gather children's birth certificates"))
        tasks.append(("HIGH", "Get children's vaccination records"))
        tasks.append(("MED", "Research schools/ganim in destination area"))
        tasks.append(("MED", "Prepare children's academic transcripts for school enrollment"))

    if family in ("couple", "family"):
        tasks.append(("HIGH", "Gather marriage certificate"))
        tasks.append(("MED", "Plan shipping of household goods (tax-free container for olim)"))

    if profession == "medical":
        tasks.append(("HIGH", "Gather all medical diplomas and specialty certifications"))
        tasks.append(("MED", "Research Misrad HaBriut recognition process for your specialty"))
        tasks.append(("MED", "Begin Hebrew medical terminology study"))

    if profession == "law":
        tasks.append(("MED", "Research Israel Bar Association requirements"))
        tasks.append(("MED", "Note: foreign law degrees are NOT automatically recognized"))

    if profession == "accounting":
        tasks.append(("MED", "Research Israeli CPA exam requirements"))
        tasks.append(("MED", "Gather accounting qualifications for equivalency review"))

    if profession == "teaching":
        tasks.append(("MED", "Gather teaching credentials for Misrad HaChinuch evaluation"))
        tasks.append(("MED", "Note: Hebrew proficiency (Ulpan Bet+) will be required"))

    if profession == "engineering":
        tasks.append(("MED", "Gather engineering degree and professional certifications for MAHAT"))

    return tasks


def get_first_week_checklist(family: str, country: str, profession: str) -> list:
    """Generate first-week tasks."""
    tasks = [
        ("HIGH", "At Ben Gurion: Visit Misrad HaKlita desk, receive Teudat Oleh"),
        ("HIGH", "Collect the first sal klita payment at the airport (a prepaid card; the cash component is larger during strikes, chagim and emergencies)"),
        ("HIGH", "Get free SIM card at airport"),
        ("HIGH", "Register at Misrad HaPnim (Interior Ministry) for Teudat Zehut"),
        ("HIGH", "Open Israeli bank account (Leumi, Hapoalim, Discount, or Mizrahi)"),
        ("HIGH", "Register with a kupat cholim (HMO)"),
        ("HIGH", "Register at Bituach Leumi (National Insurance)"),
        ("MED", "Get Israeli phone number (if not received at airport)"),
        ("MED", "Register for Ulpan (via Misrad HaKlita or municipality)"),
        ("MED", "Set up online banking access"),
        ("MED", "Arrange temporary housing if not already secured"),
        ("LOW", "Learn basic Hebrew survival phrases for bureaucracy"),
    ]

    if family == "family":
        tasks.append(("HIGH", "Register children at local school or gan"))
        tasks.append(("MED", "Register children with kupat cholim"))
        tasks.append(("MED", "Apply for child allowances (kitzvat yeladim) at Bituach Leumi"))

    if country in NBN_COUNTRIES:
        tasks.insert(0, ("HIGH", "Meet Nefesh B'Nefesh representatives at airport"))

    return tasks


def get_first_month_checklist(family: str, country: str, profession: str) -> list:
    """Generate first-month tasks."""
    tasks = [
        ("HIGH", "Begin Ulpan classes"),
        ("HIGH", "Set up standing orders (horaot keva) for rent and utilities"),
        ("HIGH", "Apply for arnona discount at municipality (up to 90% on 100 sq m, for 12 of the first 24 months)"),
        ("MED", "Verify sal klita payments are arriving in bank account"),
        ("MED", "Explore employment options or register with Misrad HaKlita employment counseling"),
        ("MED", "Get familiar with public transportation (Rav-Kav card)"),
        ("MED", "Register for online government services (gov.il)"),
        ("LOW", "Set up utilities (electricity via IEC, water, internet)"),
        ("LOW", "Consider supplementary health insurance (bituach mashlim)"),
    ]

    if profession in ("medical", "engineering", "law", "accounting", "teaching"):
        tasks.append(("HIGH", "Submit professional license recognition application"))
        tasks.append(("MED", "Begin any required Israeli professional exams preparation"))

    # Driver's license tasks
    tasks.append(("MED", "Begin driver's licence conversion: with 5+ years on the "
                         "foreign licence AND category 1/A/A1/A2/B it is administrative, "
                         "otherwise book the full practical test"))
    tasks.append(("MED", "Get medical fitness certificate for licence conversion"))

    if family == "family":
        tasks.append(("MED", "Ensure children are settling into school/gan"))
        tasks.append(("MED", "Register for after-school activities (chugim)"))

    return tasks


def get_first_year_checklist(family: str, country: str, profession: str) -> list:
    """Generate first-year tasks."""
    tasks = [
        ("HIGH", "Complete Ulpan Aleph (420-450 funded hours)"),
        ("HIGH", "Convert the driving licence (window is 5 YEARS in Israel; the separate 1-year clock is how long you may keep DRIVING on the foreign licence, counted from date of entry)"),
        ("HIGH", "File annual tax return if income exceeds threshold"),
        ("MED", "Consider Ulpan Bet for continued Hebrew improvement"),
        ("MED", "Evaluate housing: renew lease or consider buying"),
        ("MED", "Build Israeli credit history through regular bill payments"),
        ("MED", "Verify all Bituach Leumi contributions are current"),
        ("MED", "Explore professional retraining programs via Misrad HaKlita"),
        ("LOW", "Renew arnona discount for second year (if eligible)"),
        ("LOW", "Consider pension planning (keren pensia / kupat gemel)"),
    ]

    if profession in ("medical", "law"):
        tasks.append(("HIGH", "Continue professional licensing process (exams, internship)"))

    if family == "family":
        tasks.append(("MED", "Review children's academic progress and Hebrew level"))

    return tasks


def get_beyond_checklist(family: str, country: str, profession: str) -> list:
    """Generate beyond-first-year tasks."""
    tasks = [
        ("MED", "Track remaining years of 10-year foreign income tax exemption"),
        ("MED", "Review and optimize tax situation with professional advisor"),
        ("MED", "Consider Israeli citizenship benefits (voting, passport renewal)"),
        ("MED", "Continue professional development in Israeli context"),
        ("LOW", "Explore buying property (mas rechisha discount for olim)"),
        ("LOW", "Review Bituach Leumi pension entitlements"),
        ("LOW", "Consider army service obligations (if applicable by age)"),
    ]

    return tasks


STAGE_FUNCTIONS = {
    "pre-arrival": get_pre_arrival_checklist,
    "first-week": get_first_week_checklist,
    "first-month": get_first_month_checklist,
    "first-year": get_first_year_checklist,
    "beyond": get_beyond_checklist,
}


def print_checklist(stage: str, tasks: list):
    """Print a formatted checklist."""
    stage_labels = {
        "pre-arrival": "Pre-Arrival Preparation",
        "first-week": "First Week in Israel",
        "first-month": "First Month",
        "first-year": "First Year",
        "beyond": "Beyond First Year",
    }

    priority_symbols = {
        "HIGH": "[!!!]",
        "MED": "[ ! ]",
        "LOW": "[   ]",
    }

    print()
    print("=" * 60)
    print(f"  ALIYAH CHECKLIST: {stage_labels.get(stage, stage)}")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 60)
    print()

    # Group by priority
    for priority in ["HIGH", "MED", "LOW"]:
        priority_tasks = [(p, t) for p, t in tasks if p == priority]
        if not priority_tasks:
            continue

        priority_labels = {
            "HIGH": "HIGH PRIORITY (do immediately)",
            "MED": "MEDIUM PRIORITY (do soon)",
            "LOW": "LOW PRIORITY (when time allows)",
        }

        print(f"  {priority_labels[priority]}")
        print(f"  {'-' * 50}")
        for _, task in priority_tasks:
            print(f"  {priority_symbols[priority]} {task}")
        print()

    print(f"  Total tasks: {len(tasks)}")
    high_count = len([t for t in tasks if t[0] == "HIGH"])
    med_count = len([t for t in tasks if t[0] == "MED"])
    low_count = len([t for t in tasks if t[0] == "LOW"])
    print(f"  High: {high_count} | Medium: {med_count} | Low: {low_count}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate a personalized aliyah checklist based on your situation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --stage pre-arrival --family single --country usa --profession tech
  %(prog)s --stage first-week --family family --country france --profession medical
  %(prog)s --stage first-month --family couple --country russia --profession engineering

Stages: pre-arrival, first-week, first-month, first-year, beyond
Family: single, couple, family
Countries: usa, canada, uk, france, russia, ukraine, south-africa, ethiopia,
           argentina, brazil, australia, other
Professions: medical, engineering, law, accounting, teaching, tech, trades,
             academic, other
        """
    )

    parser.add_argument(
        "--stage",
        required=True,
        choices=STAGES,
        help="Current aliyah stage"
    )
    parser.add_argument(
        "--family",
        required=True,
        choices=FAMILY_TYPES,
        help="Family status (single, couple, or family)"
    )
    parser.add_argument(
        "--country",
        required=True,
        choices=COUNTRIES,
        help="Country of origin"
    )
    parser.add_argument(
        "--profession",
        required=True,
        choices=PROFESSIONS,
        help="Professional field"
    )
    parser.add_argument(
        "--all-stages",
        action="store_true",
        help="Show checklists for all stages (not just the specified one)"
    )

    args = parser.parse_args()

    print()
    print(f"  Oleh Profile:")
    print(f"  Stage: {args.stage}")
    print(f"  Family: {args.family}")
    print(f"  Country: {args.country}")
    print(f"  Profession: {args.profession}")

    if args.country in NBN_COUNTRIES:
        print(f"  Note: Nefesh B'Nefesh support available for {args.country.upper()} olim")

    print(f"  Licence: {LICENSE_RULE}")

    if args.all_stages:
        for stage in STAGES:
            func = STAGE_FUNCTIONS[stage]
            tasks = func(args.family, args.country, args.profession)
            print_checklist(stage, tasks)
    else:
        func = STAGE_FUNCTIONS[args.stage]
        tasks = func(args.family, args.country, args.profession)
        print_checklist(args.stage, tasks)


if __name__ == "__main__":
    main()
