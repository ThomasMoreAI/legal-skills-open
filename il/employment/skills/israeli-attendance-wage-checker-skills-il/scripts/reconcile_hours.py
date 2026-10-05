#!/usr/bin/env python3
"""Split an Israeli timesheet into ordinary, overtime and rest-day hours, then tier the premiums.

Pure local arithmetic. No network, no third-party packages, no file writes.

OPTIONAL. Step 6 of SKILL.md states the same arithmetic inline for agents that cannot run scripts.

What it deliberately does NOT do:
  * It does not decide whether the Hours of Work and Rest Law applies to the worker at all. That is
    the Step 0 gate and it is a judgement about the real role, not arithmetic.
  * It does not know the regular hourly wage, because the statutory base includes every supplement
    the employer pays. You pass the rate in; the script never guesses one.
  * It does not compute tax, National Insurance, or net pay.
  * It does not decide whether a break was paid. You mark it; the law turns on whether the employee
    was required to stay, which no script can infer from timestamps.

Usage:
  python3 reconcile_hours.py --weekly-bound 42 --rate 60 \\
      --day "sun,08:00,17:00,0.75" --day "mon,08:00,19:30,0.75" \\
      --day "sat,09:00,15:00,0.5,rest"
  python3 reconcile_hours.py --example

ABSENCE DAYS: pass only days actually worked. A reserve-duty, sick, leave or holiday day is not
working time; omit it rather than passing it as a standard shift, or the script will count
ordinary hours that were never worked. The statute does not lower the weekly bound for an
absence; if an agreement or workplace practice does, pass the lower --weekly-bound yourself.

SCOPE: ONE WEEK AT A TIME. The weekly limb is applied once, to whatever days you pass, so handing
it a month silently treats the month as a single week and mis-tiers everything. It refuses input
spanning more than 7 days for that reason; loop over weeks and sum the results yourself.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field

DAILY_BOUND_DEFAULT = 8.0        # s.2(a)
DAILY_BOUND_SHORT = 7.0          # s.2(b): night work, eve of weekly rest, eve of holiday
TIER1_HOURS = 2.0                # s.16(a): first two overtime hours OF THAT DAY
TIER1_RATE = 1.25
TIER2_RATE = 1.50
RESTDAY_RATE = 1.50              # s.17(a)(1)
MIN_GAP_HOURS = 8.0              # s.21


@dataclass
class Day:
    label: str
    start: str
    end: str
    break_h: float
    rest_day: bool = False
    short_day: bool = False
    paid_break: bool = False
    worked: float = field(init=False, default=0.0)

    def __post_init__(self):
        span = (_mins(self.end) - _mins(self.start)) / 60.0
        if span <= 0:
            span += 24.0  # overnight shift
        self.worked = span if self.paid_break else span - self.break_h
        if self.worked < 0:
            raise ValueError(f"{self.label}: break longer than the shift")

    @property
    def bound(self) -> float:
        return DAILY_BOUND_SHORT if self.short_day else DAILY_BOUND_DEFAULT


WEEKDAYS = ("sun", "mon", "tue", "wed", "thu", "fri", "sat")


def _weekday(label: str):
    key = label.strip().lower()[:3]
    return WEEKDAYS.index(key) if key in WEEKDAYS else None


def _mins(hhmm: str) -> int:
    try:
        h, m = hhmm.split(":")
        return int(h) * 60 + int(m)
    except Exception:
        raise ValueError(f"bad time {hhmm!r}, expected HH:MM") from None


def parse_day(raw: str) -> Day:
    parts = [p.strip() for p in raw.split(",")]
    if len(parts) < 4:
        raise ValueError(f"--day {raw!r} needs at least label,start,end,break_hours")
    flags = {p.lower() for p in parts[4:]}
    unknown = flags - {"rest", "short", "paidbreak"}
    if unknown:
        raise ValueError(f"--day {raw!r} has unknown flag(s): {', '.join(sorted(unknown))}")
    return Day(parts[0], parts[1], parts[2], float(parts[3]),
               rest_day="rest" in flags, short_day="short" in flags,
               paid_break="paidbreak" in flags)


def reconcile(days: list[Day], weekly_bound: float, rate: float, pay_basis: str = "hourly"):
    if len(days) > 7:
        raise ValueError(f"{len(days)} days passed. This script applies the WEEKLY limb once, so it "
                         f"handles ONE week at a time. Split the period into weeks and sum the "
                         f"results, or the weekly tiering will be wrong.")
    rows, notes = [], []
    ordinary_pool = 0.0
    buckets = {"ordinary": 0.0, "ot125": 0.0, "ot150": 0.0, "rest150": 0.0}

    # Pass 1, DAILY. s.1 defines overtime against the daily bound and the weekly bound as two
    # independent limbs, so the daily excess is counted first and never netted into a monthly total.
    for d in days:
        if d.rest_day:
            buckets["rest150"] += d.worked
            rest_over = max(0.0, d.worked - d.bound)
            if rest_over > 0:
                # NOT PRICED. Overtime inside the weekly rest is cumulative (rest-day premium PLUS
                # the overtime premium), but the exact combined rates rest on labour-court case law
                # this skill has not verified against the judgment, so the script does not price
                # them and says so instead of passing an underpaid long rest day silently.
                notes.append(f"NOT CHECKED: {rest_over:g} hour(s) on {d.label} fall beyond the daily "
                             f"bound inside the weekly rest. They are valued here at the rest-day rate "
                             f"only. The overtime premium is owed on top (cumulatively), so the true "
                             f"figure is HIGHER than shown; this script does not compute that extra.")
            # Rest-day hours belong ONLY in the rest bucket. Echoing them into the ordinary column
            # too reads as double payment and inflates what the user thinks the row is worth.
            rows.append((d.label, 0.0, 0.0, 0.0, d.worked))
            continue
        ordinary = min(d.worked, d.bound)
        excess = max(0.0, d.worked - d.bound)
        t1 = min(excess, TIER1_HOURS)      # resets EVERY DAY, not monthly
        t2 = max(0.0, excess - TIER1_HOURS)
        ordinary_pool += ordinary
        buckets["ot125"] += t1
        buckets["ot150"] += t2
        rows.append((d.label, ordinary, t1, t2, 0.0))

    # Pass 2, WEEKLY, on the ordinary hours that survived pass 1.
    weekly_excess = max(0.0, ordinary_pool - weekly_bound)
    if weekly_excess > 0:
        # STATED ASSUMPTION, not a statutory rule. s.16(a) ties the two-hour 125% tier to
        # "שתי השעות הנוספות הראשונות שבאותו יום" - it is expressly DAILY. The statute does not
        # say how to tier hours that become overtime only via the WEEKLY limb, so this script
        # does NOT open a second two-hour tier here (an earlier version did, which invented a
        # rule). It values the weekly excess at the base overtime rate and says so in the output.
        buckets["ordinary"] = ordinary_pool - weekly_excess
        buckets["ot125"] += weekly_excess
        notes.append(f"ASSUMPTION: {weekly_excess:g} ordinary hour(s) exceeded the weekly bound "
                     f"of {weekly_bound:g} and are valued here at {TIER1_RATE:g}x. The statute "
                     f"tiers overtime per DAY, and is silent on tiering the weekly excess, so "
                     f"this rate is an assumption rather than a statutory rule.")
    else:
        buckets["ordinary"] = ordinary_pool

    # Compliance flags, reported separately from the money (SKILL.md Step 5).
    # s.21 is about the gap between one working day and the NEXT. When the labels are weekday
    # names, only pairs on adjacent calendar days are checked, because an omitted absence day
    # (reserve duty, sick, leave) or a weekend between two entries is a gap of a day or more,
    # not of a few hours. With other labels the entries are assumed to be consecutive days.
    weekday_labels = all(_weekday(d.label) is not None for d in days)
    if not weekday_labels and len(days) > 1:
        notes.append("NOTE: day labels are not weekday names (sun..sat), so the s.21 gap check "
                     "assumes the entries are consecutive calendar days.")
    for a, b in zip(days, days[1:]):
        if weekday_labels and (_weekday(b.label) - _weekday(a.label)) % 7 != 1:
            continue
        # Absolute clock: a ends at its start plus its span (past midnight for an overnight shift),
        # b starts on the next calendar day. A modulo-24h difference would report a morning shift
        # followed by a next-day evening shift as a one-hour gap.
        a_start = _mins(a.start)
        a_span = (_mins(a.end) - a_start) % (24 * 60) or 24 * 60
        gap = ((24 * 60 + _mins(b.start)) - (a_start + a_span)) / 60.0
        if gap <= 0:
            notes.append(f"INVALID INPUT: {b.label} starts {abs(gap):g}h before {a.label} ends "
                         f"(overlapping or zero-gap shifts). Check the times; the figures above "
                         f"may be wrong.")
        elif gap < MIN_GAP_HOURS:
            notes.append(f"COMPLIANCE: only {gap:g}h between {a.label} and {b.label}; "
                         f"s.21 requires at least {MIN_GAP_HOURS:g}h. Still owed, but flag it.")

    # SKILL.md Step 4: the rest-day figure splits by pay basis. A monthly-salaried employee is
    # already paid for the day inside the salary, so only the PREMIUM ELEMENT (0.5x) is marginal.
    # An hourly or daily paid employee is not otherwise paid for it and is owed the full 1.5x.
    rest_multiplier = (RESTDAY_RATE - 1.0) if pay_basis == "monthly" else RESTDAY_RATE
    if buckets["rest150"] > 0 and pay_basis == "monthly":
        notes.append(f"PAY BASIS: monthly salaried, so the {buckets['rest150']:g} rest-day hour(s) "
                     f"are valued at the marginal premium element ({rest_multiplier:g}x) only. The "
                     f"salary already covers the day itself. Compensating rest is owed separately "
                     f"and is not money.")

    pay = (buckets["ordinary"] * rate + buckets["ot125"] * rate * TIER1_RATE
           + buckets["ot150"] * rate * TIER2_RATE + buckets["rest150"] * rate * rest_multiplier)
    return rows, buckets, pay, notes


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--day", action="append", default=[], metavar="LABEL,START,END,BREAK[,rest][,short][,paidbreak]")
    p.add_argument("--weekly-bound", type=float, default=42.0,
                   help="42 since the 2018 order, 45 is the statutory figure, 40 for some public bodies")
    p.add_argument("--rate", type=float, help="regular hourly wage INCLUDING all supplements (s.18)")
    p.add_argument("--pay-basis", choices=["monthly", "hourly"], default="hourly",
                   help="monthly salaried employees are ALREADY paid for the rest day, so only the "
                        "premium element is marginal; hourly/daily paid are owed the full 150%%")
    p.add_argument("--example", action="store_true")
    a = p.parse_args(argv)

    if a.example:
        a.rate, a.weekly_bound = 60.0, 42.0
        a.day = ["sun,08:00,17:00,0.75", "mon,08:00,19:30,0.75", "tue,08:00,17:00,0.75",
                 "wed,08:00,17:00,0.75", "thu,08:00,16:00,0.75,short", "sat,09:00,15:00,0.5,rest"]
    if not a.day or a.rate is None:
        p.error("--day (repeatable) and --rate are required, or use --example")
    if a.rate <= 0:
        p.error("--rate must be positive")

    try:
        days = [parse_day(d) for d in a.day]
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    try:
        rows, b, pay, notes = reconcile(days, a.weekly_bound, a.rate, a.pay_basis)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    print(f"{'day':<8}{'ordinary':>10}{'ot@125%':>10}{'ot@150%':>10}{'rest day':>11}")
    print("-" * 49)
    for label, o, t1, t2, r in rows:
        print(f"{label:<8}{o:>10g}{t1:>10g}{t2:>10g}{r:>11g}")
    print("-" * 49)
    print(f"{'TOTAL':<8}{b['ordinary']:>10g}{b['ot125']:>10g}{b['ot150']:>10g}{b['rest150']:>11g}")
    print(f"\nGross owed at {a.rate:g}/h (weekly bound {a.weekly_bound:g}h, "
          f"{a.pay_basis} basis): {pay:,.2f} NIS")
    for n in notes:
        print(f"  - {n}")
    print("\n  Gross only. No tax, National Insurance, health tax or pension is deducted here.")
    print("  The rate you passed must already include every supplement the employer pays (s.18).")
    print("  This is an indicative figure, not legal advice, and not a decided entitlement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
