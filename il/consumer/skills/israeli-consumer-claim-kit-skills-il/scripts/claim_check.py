#!/usr/bin/env python3
"""Offline checks for Israeli consumer claims. Not legal advice: the figures
assume the facts you enter are accurate and complete.

Two sub-commands:

  technician  Compensation under Consumer Protection Law s.18A(d) for a late
              or no-show technician, installer, delivery or gas inspection.
  cancel      Last day to cancel, and what may be deducted, under CPL s.14,
              s.14C, s.14C1, s.14E, s.13D and the 2010 Cancellation Regulations.

No network access. The rules are hard-coded from the statute text cited in
evidence.json; if the law changes, update the constants below and evidence.json together.

Examples:
  python3 claim_check.py technician --category warranty --coordinated 10:00 --arrived 14:20
  python3 claim_check.py technician --category delivery --coordinated 10:00 --no-show
  python3 claim_check.py cancel --type distance --received 2026-10-01 --price 1200
  python3 claim_check.py cancel --type distance --received 2026-10-01 --price 1200 \
      --status senior --conversation
  python3 claim_check.py cancel --type instore --goods listed --received 2026-10-01 --price 900
"""
import argparse
import calendar
from datetime import date, datetime, timedelta

FOOTER = ("Not legal advice. The result assumes the facts entered are accurate; "
          "check exclusions and exceptions before sending a demand.")

WAIT_WINDOW_H = 2          # s.18A(c)(2): waiting may not exceed 2 hours past the coordinated time
TIER_1_AFTER_WINDOW_H = 2  # s.18A(d)(1): NIS 300 once 2 hours passed beyond the waiting window
TIER_2_AFTER_WINDOW_H = 3  # s.18A(d)(1): NIS 600 once 3 hours passed beyond the waiting window
TIER_1_NIS = 300
TIER_2_NIS = 600
PHONE_RULE_NIS = 300       # s.18A(d)(2)
MAX_PLAUSIBLE_LATE_H = 12  # sanity guard against AM/PM and early-arrival typos

COVERED = {
    "warranty": "warranty or extended-warranty work",
    "equipment": "a service that depends on equipment at your home (converter, router)",
    "installation": "installing or removing goods the same dealer sold, rented or lent",
    "gas": "a periodic home gas-installation inspection",
    "delivery": "delivery of goods the dealer sold",
    "repair-contract": "a paid continuing repair contract",
}

STANDARD_DAYS = 14         # s.14(a)(1), s.14C(c)(1)
EXTENDED_MONTHS = 4        # s.14C1(b)-(c)
FEE_PCT = 0.05             # s.14E(b)(1), Cancellation Regs reg.5(a)
FEE_CAP_NIS = 100
INSTALL_CAP_NIS = 100      # s.14(b)(2), s.14E(b2)
INSTORE_MIN_PRICE = 50     # Cancellation Regs reg.1


def _hm(s: str) -> datetime:
    return datetime.strptime(s, "%H:%M")


def technician(a: argparse.Namespace) -> None:
    if a.category == "other":
        print("Not covered by s.18A: the technician rule applies only to:")
        for v in COVERED.values():
            print(f"  - {v}")
        print("A one-off paid call-out (plumber, electrician) is not on this list, so no "
              "fixed 300/600 applies. Describe the lateness in an ordinary demand instead.")
        print(FOOTER)
        return

    print(f"Category: {COVERED[a.category]} (covered by s.18A(c)(1)).")
    if a.phone_alternative:
        print("You were offered 'wait for our call' instead of a coordinated hour. If you were not "
              "told you may refuse it, or the wait at home exceeded two hours, the compensation "
              f"is NIS {PHONE_RULE_NIS} (s.18A(d)(2)). The 300/600 time tiers apply only when an "
              "hour was coordinated.")
        print(FOOTER)
        return

    coord = _hm(a.coordinated)
    if a.no_show:
        print(f"Coordinated time: {a.coordinated}. Nobody came.")
        print(f"Once five hours passed after the coordinated time with no visit (two-hour window "
              f"plus three), the statutory compensation is NIS {TIER_2_NIS}. Keep evidence that "
              "nobody came (you were home, the company's record, a call log); if you left early, "
              "check whether they came after you left.")
        amount = TIER_2_NIS
    else:
        arr = _hm(a.arrived)
        if a.next_day:
            arr += timedelta(days=1)
        if arr < coord:
            print("Arrival is earlier than the coordinated time. If the technician came early, there "
                  "is no lateness. If the visit ran past midnight, re-run with --next-day. "
                  "Use 24-hour times (13:00, not 1:00).")
            print(FOOTER)
            return
        late_h = (arr - coord).total_seconds() / 3600
        if late_h > MAX_PLAUSIBLE_LATE_H:
            print(f"Warning: {late_h:.1f} hours late is unusual. Check the times are 24-hour and on "
                  "the right day before relying on this.")
        beyond = late_h - WAIT_WINDOW_H
        print(f"Coordinated: {a.coordinated}. Arrived: {arr.strftime('%H:%M')}. "
              f"{late_h:.2f} h after the coordinated time, {max(beyond, 0):.2f} h beyond the window.")
        if beyond >= TIER_2_AFTER_WINDOW_H:
            amount = TIER_2_NIS
        elif beyond >= TIER_1_AFTER_WINDOW_H:
            amount = TIER_1_NIS
        else:
            amount = 0
        if not amount:
            if late_h > WAIT_WINDOW_H:
                print("Late beyond the two-hour window but not yet two hours beyond it: no fixed "
                      "compensation under s.18A(d)(1). The lateness can still go in a complaint.")
            else:
                print("Within the two-hour waiting window: no breach of s.18A.")
    if amount:
        print(f"Statutory compensation (s.18A(d)(1)): NIS {amount}, no proof of damage needed.")
    print("If the provider postponed by notice no later than 20:00 the evening before, with a new "
          "agreed time and without pushing the service past its legal deadline (s.18A(c)(3)), "
          "count from the NEW time instead; a later notice leaves the original time standing. Not owed if the delay came from circumstances the "
          "provider did not and should not have known of when the time was set, or could not "
          "foresee, and could not prevent (s.18A(f)).")
    print(FOOTER)


def _add_months(d: date, months: int) -> date:
    m = d.month - 1 + months
    y = d.year + m // 12
    m = m % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def _distance_notes() -> None:
    print("No right to cancel a distance sale (s.14C(d)) for: perishable goods; lodging, travel, "
          "vacation or leisure if cancelling within seven non-rest days before the service; "
          "computer information; goods made specially for you; recordable goods once the original "
          "packaging was opened.")
    print("A one-off service bought at a distance must be cancelled at least two non-rest days "
          "before it is due (s.14C(c)(2)).")


def cancel(a: argparse.Namespace) -> None:
    if a.type == "continuing":
        print("Continuing transaction: the deal ends within 3 business days of the notice, "
              "or 6 business days if sent by registered mail (s.13D(c)). No deadline to cancel.")
        print(FOOTER)
        return

    start = date.fromisoformat(a.received)
    vulnerable = a.status in ("senior", "oleh", "disability")
    breach = a.reason == "defect"

    if a.type == "instore":
        if a.price is not None and a.price <= INSTORE_MIN_PRICE:
            print(f"The in-store regulations apply only to goods priced above NIS {INSTORE_MIN_PRICE}.")
            print(FOOTER)
            return
        if a.goods == "listed":
            last = start + timedelta(days=STANDARD_DAYS)
            print(f"Furniture, home and garden equipment, electrical devices, unopened goods, ordered "
                  f"goods not yet supplied, water purifiers, watches: cancel by {last.isoformat()} "
                  "(14 days from receipt, reg.2(1)).")
        elif a.goods == "clothing":
            print("Clothing and footwear: until two non-rest days after purchase, price tag not "
                  "removed (reg.2(2)). Count the days yourself, skipping Shabbat and holidays.")
        elif a.goods == "jewelry":
            print("Jewelry up to NIS 3,000: until two non-rest days after purchase (reg.2(7)).")
        else:
            print("This item is not on the regulations' schedule, so there is no statutory in-store "
                  "right to cancel. Check the shop's posted return-policy sign (s.4C): if none is "
                  "posted, returns are presumed allowed, provided the goods did not deteriorate.")
            print(FOOTER)
            return
        print("Conditions: the goods must be returned undamaged and unused (reg.2). Connecting to "
              "electricity, gas or water counts as use. Bring the invoice or till slip (reg.3(a)). "
              "A franchisee with a posted notice may refuse refunds at other branches (reg.3(e)).")
        print("Not covered (reg.6): furniture assembled in your home, made-to-measure goods, food, "
              "underwear and swimwear, jewelry above NIS 3,000, and more.")
        if vulnerable:
            print("There is no extended 4-month right for in-store purchases (s.14C1 covers "
                  "door-to-door and distance sales only).")
        print("Refund: no later than 7 business days, same payment method (reg.4(a)).")
        if breach:
            print("For a defect, these regulations are not the route: use the warranty or the "
                  "shop's obligations for defective goods.")
        elif a.price is not None:
            fee = min(a.price * FEE_PCT, FEE_CAP_NIS)
            print(f"Maximum cancellation fee: NIS {fee:.2f} (5% or NIS 100, whichever is lower, "
                  "reg.5(a)), plus a card-clearing charge only if the shop proves it paid one.")
        print(FOOTER)
        return

    rule = "s.14C(c)(1)" if a.type == "distance" else "s.14(a)(1)"
    last = start + timedelta(days=STANDARD_DAYS)
    print(f"Standard right: cancel by {last.isoformat()} (14 days, {rule}). "
          "Send it a day early to be safe.")
    if vulnerable:
        if a.type == "doortodoor" or a.conversation:
            ext = _add_months(start, EXTENDED_MONTHS)
            sub = "s.14C1(b)" if a.type == "doortodoor" else "s.14C1(c)"
            print(f"Extended right for {a.status}: cancel by {ext.isoformat()} (4 months, {sub}). "
                  "Attach one status certificate (s.14C1(d)).")
        else:
            print("No extended right: a distance sale gets 4 months only if the deal included a "
                  "conversation with the dealer, electronic included (s.14C1(c)).")
    print("Count from the LATER of the deal date, receipt of the goods, or receipt of the "
          "disclosure document. If the disclosure document never arrived, the clock may not "
          "have started.")

    if a.type == "doortodoor":
        print("Door-to-door cancellation (s.14(b)): the dealer returns the full price paid, with "
              f"no cancellation fee. Only an installation charge of up to NIS {INSTALL_CAP_NIS} is "
              "allowed. Perishable goods are excluded (s.14(c)).")
    else:
        _distance_notes()
        print("Refund within 14 days of the notice, with a copy of the charge-cancellation notice (s.14E).")
        if breach:
            print("Cancelling for a defect, non-conformity, late delivery or other dealer breach: "
                  "NO cancellation fee (s.14E(a)(1)).")
        elif a.price is not None:
            fee = min(a.price * FEE_PCT, FEE_CAP_NIS)
            print(f"Maximum cancellation fee: NIS {fee:.2f} (5% or NIS 100, whichever is lower, "
                  "s.14E(b)(1)). Shipping and packaging count inside this cap.")
    print(FOOTER)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("technician", help="technician / delivery lateness compensation")
    t.add_argument("--category", required=True, choices=list(COVERED) + ["other"],
                   help="what the visit was for; 'other' = one-off paid call-out")
    t.add_argument("--coordinated", help="coordinated time HH:MM (24-hour)")
    g = t.add_mutually_exclusive_group()
    g.add_argument("--arrived", help="actual arrival time HH:MM (24-hour)")
    g.add_argument("--no-show", action="store_true", help="nobody came at all")
    t.add_argument("--next-day", action="store_true", help="arrival was after midnight")
    t.add_argument("--phone-alternative", action="store_true",
                   help="you were told to wait for a call instead of a coordinated hour")

    c = sub.add_parser("cancel", help="cancellation deadline and fee")
    c.add_argument("--type", required=True, choices=["distance", "doortodoor", "instore", "continuing"])
    c.add_argument("--received", help="YYYY-MM-DD, the later of deal / delivery / disclosure document")
    c.add_argument("--price", type=float)
    c.add_argument("--status", choices=["none", "senior", "oleh", "disability"], default="none")
    c.add_argument("--conversation", action="store_true", help="distance deal included a call or chat with the dealer")
    c.add_argument("--reason", choices=["no-reason", "defect"], default="no-reason")
    c.add_argument("--goods", choices=["listed", "clothing", "jewelry", "other"], default="other",
                   help="in-store only: which schedule item the goods fall under")

    a = p.parse_args()
    if a.cmd == "technician":
        if a.category != "other" and not a.phone_alternative:
            if not a.coordinated or not (a.arrived or a.no_show):
                p.error("give --coordinated and either --arrived or --no-show")
        technician(a)
    else:
        if a.type != "continuing" and not a.received:
            p.error("--received is required")
        cancel(a)


if __name__ == "__main__":
    main()
