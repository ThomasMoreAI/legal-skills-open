#!/usr/bin/env python3
"""Deterministic candidate-deadline computation from evidence-gated tables.

The model never performs date arithmetic. This script is the only source of
computed dates in the australian-litigation-deadlines plugin. It reads a
computation-rule table and, where needed, a holiday table from the plugin's
references directory, and refuses to compute (returning ``identify_only``)
whenever the rule, a provision it relies on, or the holiday data is not in
the ``verified`` evidence state, or the computation would leave verified
holiday coverage or cross an uncertain window. A refusal is a result, not an
error. Every computed date is a candidate that the responsible lawyer must
confirm before reliance.

Usage:
    python compute_deadline.py --input request.json
    echo '{...}' | python compute_deadline.py

Request JSON:
    {
      "table_id": "nsw-courts",
      "period_rule_id": "ucpr-defence-after-service",
      "trigger_date": "2026-08-14",
      "tables_dir": "optional override of the references directory"
    }
"""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import json
import sys
from pathlib import Path

DISCLAIMER = (
    "Candidate date only. The responsible lawyer must confirm every date "
    "before reliance. This tool is not a diary, court-list or "
    "practice-management system."
)

DEFAULT_TABLES_DIR = Path(__file__).resolve().parents[3] / "references"

SUPPORTED_UNITS = ("calendar_days", "clear_days", "business_days", "months", "years")


class Refusal(Exception):
    """Computation is refused; the rule is identified but no date is given."""


def load_json(path: Path, label: str) -> dict:
    if not path.is_file():
        raise ValueError(f"{label} not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} is not valid JSON: {path}: {exc}") from exc


def parse_date(value: str, label: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be an ISO date (YYYY-MM-DD): {value!r}") from exc


def require_verified(evidence: dict | None, what: str) -> None:
    state = (evidence or {}).get("state")
    if state != "verified":
        raise Refusal(
            f"{what} is in evidence state {state!r}, not 'verified'; verify it "
            "against the official publisher with verify-deadline-basis first"
        )


def add_months(date: dt.date, months: int) -> dt.date:
    """Corresponding-date rule: same day in the target month, else its last day."""
    month_index = date.month - 1 + months
    year = date.year + month_index // 12
    month = month_index % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return dt.date(year, month, day)


def parse_month_day(value: str) -> tuple[int, int]:
    try:
        month, day = map(int, value.split("-"))
        dt.date(2000, month, day)
    except (AttributeError, TypeError, ValueError) as exc:
        raise Refusal(f"invalid excluded-range date {value!r}; expected MM-DD") from exc
    return month, day


def in_excluded_ranges(date: dt.date, ranges: list[dict]) -> bool:
    """Recurring month-day ranges (e.g. 12-24 to 01-14) whose days are not counted."""
    month_day = (date.month, date.day)
    for entry in ranges:
        start = parse_month_day(entry["from"])
        end = parse_month_day(entry["to"])
        if start <= end:
            if start <= month_day <= end:
                return True
        elif month_day >= start or month_day <= end:
            return True
    return False


class HolidayTable:
    def __init__(self, data: dict) -> None:
        require_verified(data.get("evidence"), f"holiday table {data.get('table_id')}")
        self.table_id = data["table_id"]
        self.holidays = {parse_date(day, "holiday") for day in data["holidays"]}
        coverage = data["coverage"]
        self.cover_from = parse_date(coverage["from"], "coverage.from")
        self.cover_to = parse_date(coverage["to"], "coverage.to")
        self.windows = [
            (
                parse_date(window["from"], "uncertain window from"),
                parse_date(window["to"], "uncertain window to"),
                window.get("reason", "uncertain window"),
            )
            for window in data.get("uncertain_windows", [])
        ]
        self.caveats = list(data.get("caveats", []))

    def check_usable(self, date: dt.date) -> None:
        if not self.cover_from <= date <= self.cover_to:
            raise Refusal(
                f"holiday table {self.table_id} covers {self.cover_from} to "
                f"{self.cover_to} and does not cover {date}; refresh the table "
                "before computing dates in that range"
            )
        for start, end, reason in self.windows:
            if start <= date <= end:
                raise Refusal(f"{date} falls in an uncertain holiday window ({start} to {end}): {reason}")

    def is_business_day(self, date: dt.date) -> bool:
        self.check_usable(date)
        return date.weekday() < 5 and date not in self.holidays


def next_business_day_on_or_after(date: dt.date, table: HolidayTable, excluded_ranges: list[dict]) -> dt.date:
    while True:
        if excluded_ranges and in_excluded_ranges(date, excluded_ranges):
            raise Refusal(
                f"rolling the last day would enter an excluded range at {date}; "
                "the interaction of the next-business-day rule with the "
                "excluded-days provision is not settled by the tables and needs "
                "the responsible lawyer"
            )
        if table.is_business_day(date):
            return date
        date += dt.timedelta(days=1)


def raw_deadline(trigger: dt.date, length: int, unit: str) -> dt.date:
    if unit == "calendar_days":
        return trigger + dt.timedelta(days=length)
    if unit == "clear_days":
        return trigger + dt.timedelta(days=length + 1)
    if unit == "months":
        return add_months(trigger, length)
    if unit == "years":
        return add_months(trigger, length * 12)
    raise Refusal(f"unsupported period unit {unit!r}; the period fails closed")


def counted_day_deadline(
    trigger: dt.date,
    length: int,
    excluded_ranges: list[dict],
    table: HolidayTable | None,
) -> dt.date:
    """Step forward counting only days outside the excluded ranges; when a
    holiday table is given, count only business days as well."""
    date = trigger
    counted = 0
    while counted < length:
        date += dt.timedelta(days=1)
        if in_excluded_ranges(date, excluded_ranges):
            continue
        if table is not None and not table.is_business_day(date):
            continue
        counted += 1
    return date


def compute(request: dict, tables_dir: Path) -> dict:
    for key in ("table_id", "period_rule_id", "trigger_date"):
        if not request.get(key):
            raise ValueError(f"request is missing required field {key!r}")

    table_path = tables_dir / "computation-rules" / f"{request['table_id']}.json"
    table = load_json(table_path, "computation-rule table")
    trigger = parse_date(request["trigger_date"], "trigger_date")

    rules = {rule["id"]: rule for rule in table.get("period_rules", [])}
    rule = rules.get(request["period_rule_id"])
    if rule is None:
        raise ValueError(
            f"period rule {request['period_rule_id']!r} is not in table "
            f"{request['table_id']!r}; known rules: {sorted(rules)}"
        )

    identity = {
        "table_id": table["table_id"],
        "period_rule_id": rule["id"],
        "label": rule.get("label"),
        "citation": rule.get("citation"),
        "trigger": rule.get("trigger"),
        "trigger_date": trigger.isoformat(),
        "disclaimer": DISCLAIMER,
    }

    warnings = list(rule.get("warnings", []))
    try:
        require_verified(rule.get("evidence"), f"period rule {rule['id']}")
        provisions = {prov["id"]: prov for prov in table.get("computation_provisions", [])}
        applied = []
        excluded_ranges: list[dict] = []
        short_threshold = 0
        for prov_id in rule.get("applies_provisions", []):
            provision = provisions.get(prov_id)
            if provision is None:
                raise Refusal(f"provision {prov_id!r} referenced by rule {rule['id']} is not in the table")
            require_verified(provision.get("evidence"), f"provision {prov_id}")
            applied.append(provision["citation"])
            effects = provision.get("time_computation_effects") or {}
            excluded_ranges.extend(effects.get("excluded_ranges", []))
            short_threshold = max(short_threshold, effects.get("short_period_threshold_days", 0))

        unit = rule["period"]["unit"]
        length = rule["period"]["length"]
        rollover = rule.get("rollover", "none")
        if unit not in SUPPORTED_UNITS:
            raise Refusal(f"unsupported period unit {unit!r}; the period fails closed")
        if rollover not in ("none", "next_business_day"):
            raise Refusal(f"unsupported rollover {rollover!r}; the period fails closed")
        if not isinstance(length, int) or length < 1:
            raise Refusal(f"period length must be a positive integer, got {length!r}")
        if excluded_ranges and unit not in ("calendar_days", "business_days"):
            raise Refusal(
                f"an applied provision declares excluded ranges, which the tables "
                f"express only for calendar_days and business_days periods, not "
                f"{unit!r}; the period fails closed"
            )
        if short_threshold and unit == "calendar_days" and length <= short_threshold:
            raise Refusal(
                f"an applied provision counts only business days in periods of "
                f"{short_threshold} days or less, which a calendar_days rule "
                "cannot express; the period fails closed"
            )

        needs_holidays = unit == "business_days" or rollover == "next_business_day"
        holiday_table = None
        if needs_holidays:
            holiday_path = tables_dir / "holidays" / f"{table['holiday_table']}.json"
            holiday_table = HolidayTable(load_json(holiday_path, "holiday table"))
            warnings.extend(holiday_table.caveats)

        if unit == "business_days":
            if holiday_table is None:
                raise Refusal("business-day computation requires a verified holiday table")
            deadline = counted_day_deadline(trigger, length, excluded_ranges, holiday_table)
        elif excluded_ranges:
            deadline = counted_day_deadline(trigger, length, excluded_ranges, None)
            if rollover == "next_business_day":
                if holiday_table is None:
                    raise Refusal("business-day rollover requires a verified holiday table")
                deadline = next_business_day_on_or_after(deadline, holiday_table, excluded_ranges)
        else:
            deadline = raw_deadline(trigger, length, unit)
            if rollover == "next_business_day":
                if holiday_table is None:
                    raise Refusal("business-day rollover requires a verified holiday table")
                deadline = next_business_day_on_or_after(deadline, holiday_table, [])

        return {
            "status": "computed",
            **identity,
            "candidate_date": deadline.isoformat(),
            "candidate_day": deadline.strftime("%A"),
            "provisions_applied": [rule.get("citation"), *applied],
            "holiday_table": holiday_table.table_id if holiday_table else None,
            "warnings": warnings,
        }
    except Refusal as refusal:
        return {
            "status": "identify_only",
            **identity,
            "reason": str(refusal),
            "warnings": warnings,
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="request JSON file (default: stdin)")
    parser.add_argument(
        "--tables-dir",
        type=Path,
        default=DEFAULT_TABLES_DIR,
        help="references directory holding computation-rules/ and holidays/",
    )
    args = parser.parse_args(argv)

    try:
        if args.input:
            request = load_json(args.input, "request")
        else:
            request = json.loads(sys.stdin.read())
        result = compute(request, args.tables_dir)
    except (ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, indent=2))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
