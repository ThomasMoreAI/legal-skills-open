#!/usr/bin/env python3
"""Emit the document-collection checklist for settling an estate in Israel.

Prints the core documents every family reuses, plus asset-specific documents
when you pass one or more asset types. Pure standard library, no network calls.

Usage:
    python3 checklist.py
    python3 checklist.py --assets bank real_estate vehicle
    python3 checklist.py --lang he --assets pension
    python3 checklist.py --example
"""

import argparse
import sys

CORE = [
    ("Death certificate (several certified copies)",
     "תעודת פטירה (כמה עותקים מאושרים)"),
    ("Deceased's national ID",
     "תעודת זהות של הנפטר"),
    ("Heirs' national IDs",
     "תעודות זהות של היורשים"),
    ("Succession order / probate order (obtained separately: israeli-wills-inheritance)",
     "צו ירושה / צו קיום צוואה (מתקבל בנפרד: israeli-wills-inheritance)"),
]

BY_ASSET = {
    "bank": [
        ("Bank account numbers and latest statements",
         "מספרי חשבונות בנק ודפי חשבון אחרונים"),
        ("List of active standing orders to cancel",
         "רשימת הוראות קבע פעילות לביטול"),
    ],
    "pension": [
        ("Pension / provident fund / managers' insurance policy numbers",
         "מספרי קופות גמל / פנסיה / ביטוח מנהלים"),
        ("Clearing-house (mislaka) account locator report",
         "דוח איתור חשבונות מהמסלקה"),
    ],
    "real_estate": [
        ("Land Registry extract (nesach tabu)",
         "נסח טאבו"),
        ("Mortgage / loan agreements on the property",
         "הסכמי משכנתה / הלוואה על הנכס"),
    ],
    "vehicle": [
        ("Vehicle registration (rishayon rechev)",
         "רישיון רכב"),
        ("Death certificate for Misrad HaRishui transfer",
         "תעודת פטירה להעברה במשרד הרישוי"),
    ],
    "business": [
        ("Business registration and accountant contact",
         "רישום העסק ופרטי רואה החשבון"),
        ("Outstanding invoices, debts, and standing orders",
         "חשבוניות פתוחות, חובות והוראות קבע"),
    ],
    "caregiver": [
        ("Caregiver's employment contract, payslips, and pension-fund severance deposits",
         "חוזה ההעסקה של המטפל, תלושי שכר והפקדות הפיצויים לקרן הפנסיה"),
        ("Foreign-worker permit details (if a foreign caregiver)",
         "פרטי היתר העסקת עובד זר (אם מדובר במטפל זר)"),
    ],
    "credit_card": [
        ("Each card issuer and the recurring charges on each card",
         "כל חברת אשראי והחיובים החוזרים בכל כרטיס"),
    ],
    "digital": [
        ("Phone, email, and cloud accounts; keep the phone line until two-factor codes are moved",
         "טלפון, דואר אלקטרוני וחשבונות ענן; להשאיר את הקו עד שקודי האימות הדו-שלבי הועברו"),
    ],
    "employer": [
        ("Employer payroll / HR contact",
         "פרטי שכר / משאבי אנוש אצל המעסיק"),
        ("Last payslip and employment contract",
         "תלוש שכר אחרון וחוזה העסקה"),
    ],
}

VALID_ASSETS = sorted(BY_ASSET.keys())


def emit(assets, lang):
    def pick(pair):
        return pair[1] if lang == "he" else pair[0]

    header = "רשימת מסמכים לאיסוף" if lang == "he" else "Document-collection checklist"
    print("=== " + header + " ===")
    core_title = "מסמכי ליבה" if lang == "he" else "Core documents"
    print("\n[" + core_title + "]")
    for pair in CORE:
        print("  [ ] " + pick(pair))

    for asset in assets:
        if asset not in BY_ASSET:
            print(f"  (skipped unknown asset: {asset})", file=sys.stderr)
            continue
        print(f"\n[{asset}]")
        for pair in BY_ASSET[asset]:
            print("  [ ] " + pick(pair))


def main():
    p = argparse.ArgumentParser(description="Estate document checklist for Israel.")
    p.add_argument("--assets", nargs="*", default=[],
                   help="Asset types: " + ", ".join(VALID_ASSETS))
    p.add_argument("--lang", choices=["en", "he"], default="en", help="Output language")
    p.add_argument("--example", action="store_true",
                   help="Run with a sample set of assets")
    args = p.parse_args()

    assets = args.assets
    if args.example:
        assets = ["bank", "real_estate", "vehicle"]
        print("Example assets: bank, real_estate, vehicle\n")

    emit(assets, args.lang)


if __name__ == "__main__":
    main()
