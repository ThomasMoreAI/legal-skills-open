"""Deterministic period calculator for /pressuretest (method v2.8).

Stdlib only. Counts a contractual or procedural period so that no time
computation in a pressure test rests on impression. Invoke with quoted
paths (works from any directory):

    python "<skill root>/scripts/compute_period.py" --start 2026-06-19 \
        --days 15 --unit business --convention clear \
        [--holidays 2026-07-03,2026-08-31] [--weekend sat,sun] \
        [--direction forward|backward] \
        [--deadline 2026-07-10T17:00 --semantics not-before|due-by]

Conventions (state which one the documents fix; if none, say so):
    unit=calendar   every day counts.
    unit=business   weekend days and listed holidays do not count.
    convention=period  excludes start; uses the Nth counted day as the limit.
    convention=clear   excludes start and candidate event day; shifts the
                       limit one calendar day beyond the Nth counted day
                       in the counting direction, with no business-day roll.
    direction          chooses counting direction only, not the comparison.
    semantics=not-before  candidate date must be on or after the limit.
    semantics=due-by      candidate date must be on or before the limit.

Select unit and convention explicitly in the CLI. A date check also requires
explicit semantics: counting forward does not imply a minimum waiting period.
These are arithmetic options, not jurisdictional rules. Supply the governing
rule or label assumptions; no deemed service, cutoff time or timezone is checked.

Exit codes: 0 result on stdout as JSON; 2 usage or date error (stderr).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta

UNITS = {"calendar", "business"}
CONVENTIONS = {"period", "clear"}
DIRECTIONS = {"forward", "backward"}
SEMANTICS = {"not-before", "due-by"}
DAY_NAMES = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}
FULL_DAY_NAMES = {
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
}


def _weekend(names) -> frozenset[int]:
    out = set()
    for name in names:
        name = str(name).strip().lower()
        if name not in DAY_NAMES and name not in FULL_DAY_NAMES:
            raise ValueError(f"unknown weekday name: {name!r}")
        out.add(DAY_NAMES[name[:3]])
    if len(out) == 7:
        raise ValueError("weekend cannot exclude all seven days")
    return frozenset(out)


def _ordinal(n: int) -> str:
    suffix = (
        "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    )
    return f"{n}{suffix}"


def compute(
    start: date,
    days: int,
    unit: str = "calendar",
    convention: str = "period",
    holidays=(),
    weekend=("sat", "sun"),
    direction: str = "forward",
) -> dict:
    """Count `days` counted days from `start`; return boundary and permitted days."""
    if type(start) is not date:
        raise ValueError("start must be a date without a time")
    if type(days) is not int or days < 1:
        raise ValueError("days must be a positive integer")
    if unit not in UNITS:
        raise ValueError(f"unit must be one of {sorted(UNITS)}")
    if convention not in CONVENTIONS:
        raise ValueError(f"convention must be one of {sorted(CONVENTIONS)}")
    if direction not in DIRECTIONS:
        raise ValueError(f"direction must be one of {sorted(DIRECTIONS)}")
    holiday_set = set()
    for holiday in holidays:
        if isinstance(holiday, datetime):
            raise ValueError("holidays must be dates without times")
        holiday_set.add(
            holiday if isinstance(holiday, date) else date.fromisoformat(str(holiday))
        )
    weekend_set = _weekend(weekend)
    step = 1 if direction == "forward" else -1

    counted: list[date] = []
    cursor = start
    try:
        while len(counted) < days:
            cursor = cursor + timedelta(days=step)
            if unit == "business" and (
                cursor.weekday() in weekend_set or cursor in holiday_set
            ):
                continue
            counted.append(cursor)
        boundary = counted[-1]
        permitted = (
            boundary + timedelta(days=step) if convention == "clear" else boundary
        )
    except OverflowError as exc:
        raise ValueError("period exceeds the supported date range") from exc

    exclusions = ""
    if unit == "business":
        names = [k for k, v in DAY_NAMES.items() if v in weekend_set]
        exclusions = (
            f" ({'/'.join(names)} and {len(holiday_set)} listed holiday(s) excluded)"
        )
    relation = "after" if direction == "forward" else "before"
    tail = f"on the {convention} convention the limit date is {permitted.isoformat()}"
    statement = (
        f"Counting {days} {unit} day(s) {relation} {start.isoformat()}{exclusions}, "
        f"the {_ordinal(days)} counted day is {boundary.isoformat()}; {tail}."
    )
    return {
        "start": start.isoformat(),
        "days": days,
        "unit": unit,
        "convention": convention,
        "direction": direction,
        "weekend": sorted(k for k, v in DAY_NAMES.items() if v in weekend_set),
        "holidays": sorted(h.isoformat() for h in holiday_set),
        "counted": [d.isoformat() for d in counted],
        "boundary_day": boundary.isoformat(),
        "permitted_day": permitted.isoformat(),
        "statement": statement,
    }


def check_deadline(result: dict, deadline, semantics: str | None = None) -> dict:
    """Compare dates using an explicit relation; never certify clock compliance."""
    if semantics not in SEMANTICS:
        raise ValueError("date checks require semantics: not-before or due-by")
    if isinstance(deadline, datetime):
        if deadline.tzinfo is not None:
            raise ValueError(
                "timezone-aware checks are unsupported; supply a local date"
            )
        d_date, d_time = deadline.date(), deadline.time()
    elif isinstance(deadline, date):
        d_date, d_time = deadline, None
    else:
        raise ValueError("deadline must be a date or datetime")
    permitted = date.fromisoformat(result["permitted_day"])
    boundary = date.fromisoformat(result["boundary_day"])
    not_before = semantics == "not-before"
    ok = d_date >= permitted if not_before else d_date <= permitted
    shortfall = 0 if ok else abs((permitted - d_date).days)
    intra_day = d_time is not None and d_date == boundary
    time_text = f" at {d_time.isoformat()}" if d_time is not None else ""
    if ok:
        verdict = "satisfies the date-only comparison"
    else:
        verdict = (
            f"fails the date-only comparison by {shortfall} day(s): the "
            f"{'earliest' if not_before else 'latest'} permitted day is "
            f"{permitted.isoformat()}"
        )
    return {
        "deadline_date": d_date.isoformat(),
        "deadline_time": d_time.isoformat() if d_time is not None else None,
        "semantics": semantics,
        "time_checked": False,
        "deadline_ok": ok,
        "shortfall_days": shortfall,
        "intra_day_on_final_day": intra_day,
        "statement": (
            f"The stated date {d_date.isoformat()}{time_text} {verdict} "
            f"under {semantics} semantics and the {result['convention']} convention. "
            "Cutoff times, timezones and legal compliance are not checked."
        ),
    }


def _parse_date(text: str, name: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"{name}: {text!r} is not a valid ISO date") from exc


def _parse_deadline(text: str):
    if "T" in text:
        try:
            return datetime.fromisoformat(text)
        except ValueError as exc:
            raise ValueError(
                f"deadline: {text!r} is not a valid ISO date-time"
            ) from exc
    return _parse_date(text, "deadline")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--start", required=True, help="ISO date the period runs from")
    parser.add_argument("--days", required=True, type=int)
    parser.add_argument("--unit", required=True, choices=sorted(UNITS))
    parser.add_argument("--convention", required=True, choices=sorted(CONVENTIONS))
    parser.add_argument("--direction", default="forward", choices=sorted(DIRECTIONS))
    parser.add_argument("--holidays", default="", help="comma-separated ISO dates")
    parser.add_argument(
        "--weekend", default="sat,sun", help="comma-separated day names"
    )
    parser.add_argument(
        "--deadline", default=None, help="ISO date or date-time to test"
    )
    parser.add_argument(
        "--semantics",
        choices=sorted(SEMANTICS),
        help="required with --deadline: due-by (<= limit) or not-before (>= limit)",
    )
    args = parser.parse_args(argv)
    try:
        if bool(args.deadline) != bool(args.semantics):
            raise ValueError("--deadline and --semantics must be supplied together")
        start = _parse_date(args.start, "start")
        holidays = [
            _parse_date(h.strip(), "holidays")
            for h in args.holidays.split(",")
            if h.strip()
        ]
        weekend = [w for w in args.weekend.split(",") if w.strip()]
        result = compute(
            start,
            args.days,
            args.unit,
            args.convention,
            holidays,
            weekend,
            args.direction,
        )
        if args.deadline:
            result["check"] = check_deadline(
                result, _parse_deadline(args.deadline), args.semantics
            )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, indent=1)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
