#!/usr/bin/env python3
"""Generate a dated bureaucratic timeline for settling an estate in Israel.

Anchors every milestone to the date of death and prints three horizons:
first 72 hours, first 30 days, and first year. Most dates are calendar offsets
to help a bereaved family plan. Rows marked [!] are hard statutory deadlines
(the 30-day firearms grace period and the 90-day enduring-power-of-attorney
residual authority) and are not slideable. Always confirm any real deadline
against the official source (btl.gov.il, gov.il, kolzchut.org.il).

Pure standard library. No network calls, no external services.

Usage:
    python3 generate_timeline.py --date-of-death 2026-07-01
    python3 generate_timeline.py --date-of-death 2026-07-01 --lang he
    python3 generate_timeline.py --example
"""

import argparse
import datetime as dt
import sys

# Each milestone: (day offset from death, English label, Hebrew label, horizon key, statutory)
#
# `statutory` is the important column. Most rows are PLANNING offsets a bereaved
# family can slide. Two rows are real clocks fixed by statute and must be printed
# as deadlines, not suggestions:
#   - 30 days: section 5(b)(5) of the Firearms Law, 5709-1949 exempts an heir or
#     estate administrator from the licence requirement for 30 days from the death.
#     Holding the weapon after that without a licence is an offence.
#   - 90 days: section 32kd(b) of the Legal Capacity and Guardianship Law,
#     5722-1962 gives the attorney under an enduring power of attorney a residual
#     authority for up to 90 days from the death. After that the authority is gone.
# Earlier versions of this script printed only soft offsets, so the only two hard
# clocks the skill knows about were invisible in its own headline deliverable.
MILESTONES = [
    (0, "Obtain the death notice (medical) from the doctor/hospital",
        "הוצאת הודעת פטירה (רפואית) מהרופא או בית החולים", "72h", False),
    (1, "Arrange burial with the Chevra Kadisha / religious council / civil burial society",
        "תיאום קבורה עם חברה קדישא / מועצה דתית / עמותת קבורה אזרחית", "72h", False),
    (7, "Confirm the death is registered at Misrad HaPnim and order the death certificate",
        "אימות רישום הפטירה במשרד הפנים והזמנת תעודת פטירה", "30d", False),
    (10, "Order several certified copies of the death certificate (free)",
        "הזמנת מספר עותקים מאושרים של תעודת הפטירה (חינם)", "30d", False),
    (14, "Notify banks; expect account freeze; request statements",
        "יידוע הבנקים; צפו להקפאת חשבון; בקשת פירוט", "30d", False),
    (14, "Notify pension funds, provident funds, and insurers",
        "יידוע קופות גמל, פנסיה וחברות ביטוח", "30d", False),
    (14, "Notify the employer; claim final salary, vacation redemption, and severance. Severance "
         "on death goes to the statutory sheirim under Severance Pay Law 5723-1963 s.5, who are "
         "not necessarily the heirs (for a death in the s.5(b1) determining period, heirs step in "
         "where there is no spouse or dependent child)",
        "יידוע המעסיק; דרישת שכר אחרון, פדיון חופשה ופיצויים. הפיצויים משולמים לשאירים לפי סעיף 5 "
        "לחוק פיצויי פיטורים, שאינם בהכרח היורשים (במות עובד בתקופה הקובעת של סעיף 5(ב1), "
        "היורשים באים במקום באין בן זוג או ילד תלוי)", "30d", False),
    (14, "If the deceased employed a caregiver or housekeeper: the death ends the employment; "
         "settle last salary, notice, recuperation, vacation, and severance as estate debts",
        "אם הנפטר העסיק מטפל או עוזרת בית: הפטירה מסיימת את ההעסקה; יש לסלק שכר אחרון, "
        "הודעה מוקדמת, הבראה, חופשה ופיצויים כחובות העיזבון", "30d", False),
    (21, "Cancel standing orders; notify utilities, HMO, municipality, subscriptions, card issuers",
        "ביטול הוראות קבע; יידוע תשתיות, קופת חולים, עירייה, מנויים, חברות אשראי", "30d", False),
    (30, "Confirm with Bituach Leumi and actively claim survivor benefits (separate skill)",
        "אימות מול ביטוח לאומי ותביעת קצבת שאירים באופן פעיל (סקיל נפרד)", "30d", False),
    (30, "DEADLINE: surrender the deceased's firearm to the police, or have it deactivated "
         "through the licensing bureau. Firearms Law 5709-1949 s.5(b)(5) exempts an heir from "
         "the licence requirement for 30 days from the death only",
        "מועד אחרון: מסירת כלי הירייה של הנפטר למשטרה, או השבתה דרך לשכת הרישוי. סעיף 5(ב)(5) "
        "לחוק כלי היריה פוטר יורש מחובת רישיון 30 יום מהפטירה בלבד", "30d", True),
    (90, "DEADLINE: the residual authority of an enduring power of attorney ends. Legal Capacity "
         "and Guardianship Law 5722-1962 s.32kd(b) allows the attorney for property to pay ongoing "
         "and burial costs and run a rented property or business for up to 90 days from the death",
        "מועד אחרון: פקיעת הסמכות השיורית של ייפוי כוח מתמשך. סעיף 32כד(ב) לחוק הכשרות המשפטית "
        "והאפוטרופסות מתיר למיופה הכוח לענייני רכוש לשלם תשלומים שוטפים והוצאות קבורה ולנהל נכס "
        "מושכר או עסק עד 90 יום מהפטירה", "1y", True),
    (60, "Obtain the succession order / probate order (separate skill, out of scope here)",
        "הוצאת צו ירושה / צו קיום צוואה (סקיל נפרד, מחוץ לתחום כאן)", "1y", False),
    (120, "After the order: release bank funds and securities",
        "אחרי הצו: שחרור כספים וניירות ערך בבנק", "1y", False),
    (150, "After the order: re-register real estate at the Land Registry (Tabu)",
        "אחרי הצו: רישום מקרקעין מחדש בלשכת רישום המקרקעין (טאבו)", "1y", False),
    (150, "After the order: transfer the vehicle at Misrad HaRishui",
        "אחרי הצו: העברת רכב במשרד הרישוי", "1y", False),
]

HORIZON_TITLES = {
    "72h": ("First 72 hours: burial and first documents",
            "72 שעות ראשונות: קבורה ומסמכים ראשונים"),
    "30d": ("First 30 days: registration, certificate, notification cascade",
            "30 ימים ראשונים: רישום, תעודה, שרשרת יידוע"),
    "1y": ("First year: orders, asset transfer, benefits",
           "שנה ראשונה: צווים, העברת נכסים, קצבאות"),
}

ORDER = ["72h", "30d", "1y"]


def parse_date(text):
    try:
        return dt.date.fromisoformat(text)
    except ValueError:
        sys.exit("error: --date-of-death must be YYYY-MM-DD, e.g. 2026-07-01")


def build_timeline(dod, lang):
    lines = []
    for key in ORDER:
        en_title, he_title = HORIZON_TITLES[key]
        lines.append("")
        lines.append("=== " + (he_title if lang == "he" else en_title) + " ===")
        for offset, en, he, hkey, statutory in sorted(MILESTONES, key=lambda m: m[0]):
            if hkey != key:
                continue
            when = dod + dt.timedelta(days=offset)
            label = he if lang == "he" else en
            day_word = "יום" if lang == "he" else "day"
            mark = "[!] " if statutory else "    "
            lines.append(f"  {mark}{when.isoformat()} (+{offset} {day_word})  {label}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Dated estate-settlement timeline for Israel.")
    p.add_argument("--date-of-death", help="Date of death, format YYYY-MM-DD")
    p.add_argument("--lang", choices=["en", "he"], default="en", help="Output language")
    p.add_argument("--example", action="store_true", help="Run with a sample date")
    args = p.parse_args()

    if args.example:
        dod = dt.date(2026, 7, 1)
        print("Example: date of death 2026-07-01")
    elif args.date_of_death:
        dod = parse_date(args.date_of_death)
    else:
        p.print_help()
        sys.exit(0)

    print(build_timeline(dod, args.lang))
    note = ("\nRows marked [!] are HARD deadlines fixed by statute: the 30-day firearms "
            "grace period (Firearms Law 5709-1949 s.5(b)(5)) and the 90-day residual authority "
            "of an enduring power of attorney (Legal Capacity and Guardianship Law 5722-1962 "
            "s.32kd(b)). Every other row is a planning offset you can slide, not a legal "
            "deadline. Confirm anything time-critical at btl.gov.il, gov.il, and kolzchut.org.il.")
    print(note)


if __name__ == "__main__":
    main()
