#!/usr/bin/env python3
"""GDPR / RODO deadline calculator - deterministic, offline, zero dependencies.

Computes the two time limits that matter operationally, the way EU law actually counts them:

- **Breach notification (Art. 33)** - 72 hours from AWARENESS (the moment the controller
  became aware), not from the event. Hour-based.
- **Data subject request / DSAR (Art. 12(3))** - one month from RECEIPT, extendable by two
  further months. Month-based, counted per Regulation (EEC, Euratom) No 1182/71 art. 3(2)(c):
  a period in months ends on the day of the last month bearing the same number as the start
  day; if that month has no such day, it ends on the last day of that month
  (e.g. receipt 31 Jan -> one month -> 28/29 Feb).

Usage:
    python gdpr_deadlines.py breach  --from "2026-06-30T14:30"
    python gdpr_deadlines.py dsar    --from 2026-01-31 [--extend]

Output is JSON. Dates are naive local-time ISO 8601; the caller supplies the timezone context.
This is a clerical aid - the legal decision (whether a deadline applies, whether to extend)
stays with the controller / DPO.
"""

from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import datetime, timedelta


def add_months(d: datetime, months: int) -> datetime:
    """Add whole months per Reg. 1182/71 art. 3(2)(c): same day-number, clamped to month end."""
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    last_day = calendar.monthrange(year, month)[1]
    day = min(d.day, last_day)
    return d.replace(year=year, month=month, day=day)


def breach_deadline(awareness: datetime) -> dict:
    deadline = awareness + timedelta(hours=72)
    return {
        "regime": "breach_notification",
        "basis": "RODO/GDPR art. 33(1) - 72h od stwierdzenia / from awareness",
        "awareness": awareness.isoformat(),
        "deadline_72h": deadline.isoformat(),
        "note": "PL: zegar startuje od STWIERDZENIA naruszenia, nie od zdarzenia; po terminie "
                "zglos z wyjasnieniem opoznienia (art. 33 ust. 1 zd. 2). "
                "EN: the clock starts on AWARENESS, not the event; if late, notify with reasons "
                "for the delay (art. 33(1) sent. 2).",
    }


def dsar_deadline(receipt: datetime, extend: bool) -> dict:
    base = add_months(receipt, 1)
    out = {
        "regime": "data_subject_request",
        "basis": "RODO/GDPR art. 12(3) - 1 miesiac od otrzymania / from receipt",
        "receipt": receipt.isoformat(),
        "deadline_1_month": base.isoformat(),
    }
    if extend:
        out["deadline_extended_3_months"] = add_months(receipt, 3).isoformat()
        out["note"] = ("PL: przedluzenie o max 2 miesiace przy zlozonosci - poinformuj osobe w "
                       "ciagu PIERWSZEGO miesiaca z przyczyna (art. 12 ust. 3). "
                       "EN: extension of up to 2 months for complexity - inform the person within "
                       "the FIRST month with the reason (art. 12(3)).")
    return out


def _parse(s: str) -> datetime:
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise SystemExit(f"error: nieczytelna data {s!r}; uzyj ISO 8601 (YYYY-MM-DD lub YYYY-MM-DDTHH:MM)")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="GDPR/RODO deadline calculator")
    sub = p.add_subparsers(dest="regime", required=True)
    b = sub.add_parser("breach", help="72h breach notification (art. 33)")
    b.add_argument("--from", dest="frm", required=True, help="awareness time, ISO 8601")
    d = sub.add_parser("dsar", help="data subject request (art. 12(3))")
    d.add_argument("--from", dest="frm", required=True, help="receipt date, ISO 8601")
    d.add_argument("--extend", action="store_true", help="apply the +2 month extension")
    args = p.parse_args(argv)

    when = _parse(args.frm)
    if args.regime == "breach":
        result = breach_deadline(when)
    else:
        result = dsar_deadline(when, args.extend)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
