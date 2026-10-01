#!/usr/bin/env python3
"""Compute the four Hotzaa LaPoal debtor clocks from the date the azhara was served.

The four azhara clocks run from service (hamtzaa), not from the date printed on the azhara and not
from the day the debtor noticed the file. Figures per references/verified-facts.md.

Usage:
  python3 deadlines.py 2026-08-01 --type shtar
  python3 deadlines.py 2026-08-01 --type katzuv
  python3 deadlines.py 2026-08-01 --type psak-din
"""
import argparse
from datetime import date, timedelta

TYPES = {
    "shtar":    ("Bill or check (shtar / hamchaa)", True,  20),
    "katzuv":   ("Fixed-sum claim (sechum katzuv)", True,  30),
    "psak-din": ("Money judgment (psak din kaspi)", False, 20),
    "mezonot":  ("Maintenance (mezonot)",           False, None),
}

def main():
    p = argparse.ArgumentParser(description="Hotzaa LaPoal debtor deadline calculator")
    p.add_argument("served", help="date the azhara was served, YYYY-MM-DD")
    p.add_argument("--type", required=True, choices=sorted(TYPES), help="file type")
    a = p.parse_args()

    y, m, d = (int(x) for x in a.served.split("-"))
    served = date(y, m, d)
    label, can_object, payorder_days = TYPES[a.type]

    print(f"File type   : {label}")
    print(f"Azhara served: {served.isoformat()}")
    print()

    rows = []
    if can_object:
        rows.append(("Objection (form 218)", served + timedelta(days=30),
                     "Timely = automatic stay + transfer to court. Late = no stay."))
    else:
        rows.append(("Objection", None,
                     "NOT AVAILABLE on this file type. Consider paraati (form 236) or setting aside the judgment."))
    if payorder_days:
        rows.append((f"Payment order (form 233)", served + timedelta(days=payorder_days),
                     "Later filing still possible, but interest and advocate fees may be added."))
    if a.type == "mezonot":
        rows.append(("Maintenance warning", None,
                     "No ordinary payment order (form 233). Arrest of up to 21 days is possible without an "
                     "ability examination, carried out only 7 days after an arrest warning is served."))
    else:
        rows.append(("Ability examination / paraati exemption", served + timedelta(days=21),
                     "A paraati claim filed inside this window exempts you from attending while pending."))

    for name, when, note in rows:
        when_s = when.isoformat() if when else "n/a"
        left = f"({(when - date.today()).days:+d} days from today)" if when else ""
        print(f"  {name}")
        print(f"    deadline: {when_s} {left}")
        print(f"    {note}")
        print()

    print("Paraati (form 236, relief 119) has NO deadline and stays open at any stage.")
    print("Reminder: a payment order does NOT lift existing restrictions or attachments.")
    print("A restriction takes effect only 30 days after its own warning is served: pay, or ask for an")
    print("ability examination on form 400 (code 159), inside that window. Count it from the warning, not the azhara.")
    print("If the restriction was imposed in your presence, no warning is sent and the 30 days run from imposition.")

if __name__ == "__main__":
    main()
