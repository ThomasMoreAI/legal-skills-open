#!/usr/bin/env python3
"""
Litigation Deadline Calculator

Computes backward deadlines from scheduling order dates based on the applicable
rules of civil procedure (Colorado CRCP, Federal FRCP, state-specific rules)
or arbitration rules (AAA, JAMS).

Usage:
    python compute_deadlines.py --input deadlines.json --output computed.json

Input JSON format:
{
    "matter_name": "Smith v. Jones Co.",
    "proceeding_type": "litigation" | "arbitration",
    "jurisdiction": "colorado" | "federal" | "california" | "new_york" | etc.,
    "forum": "aaa_commercial" | "aaa_employment" | "jams_comprehensive" | "jams_streamlined",
    "service_method": "electronic" | "mail" | "hand" | "fax",
    "scheduling_order_dates": { ... },
    "attendees": ["jane@company.com"]
}

Jurisdiction is REQUIRED for litigation matters. The script will raise an error
if no jurisdiction is provided — it never defaults or guesses.

Output JSON: list of deadline objects with description, date, rule_basis, category, priority
"""

import json
import sys
import argparse
from datetime import date, timedelta, datetime


# ---------------------------------------------------------------------------
# Shared date helpers
# ---------------------------------------------------------------------------

def parse_date(s):
    """Parse a YYYY-MM-DD string into a date object. Returns None if falsy."""
    if s:
        return datetime.strptime(s, "%Y-%m-%d").date()
    return None


def observe_holiday(d):
    """Adjust a holiday to its observed date.
    Saturday holidays are observed on Friday; Sunday on Monday."""
    if d.weekday() == 5:  # Saturday
        return d - timedelta(days=1)
    elif d.weekday() == 6:  # Sunday
        return d + timedelta(days=1)
    return d


# ---------------------------------------------------------------------------
# Jurisdiction rules database
#
# IMPORTANT: Both the procedural rules AND the holiday functions in this
# database serve as a BASELINE, not a source of truth. The skill's
# verification step (Step 3 in SKILL.md) must search for recent changes
# to both rules and holidays before every computation. Holidays can and
# do change — states add, rename, or remove them. Procedural rules change
# even more frequently. Never treat these values as authoritative without
# verification.
#
# Each jurisdiction entry contains:
#   short_period_threshold: periods shorter than this (in days) exclude
#       weekends/holidays from the count. Set to 0 for "count all days always."
#   service_days: dict mapping service method -> extra days added to response
#       periods. Keys: "electronic", "mail", "hand", "fax"
#   discovery_response_days: default days to respond to interrogatories/RFPs/RFAs
#   expert_plaintiff_days: days before trial for plaintiff expert disclosure
#   expert_defendant_days: days before trial for defendant expert disclosure
#   expert_rebuttal_days: days before trial (or after opposing disclosure) for rebuttal
#   expert_rebuttal_relative: if True, rebuttal is measured from opposing disclosure
#       date rather than backward from trial
#   disco_cutoff_default: default discovery cutoff in days before trial (0 = set by order)
#   summary_j_response: days to respond to a dispositive motion
#   summary_j_reply: days to reply
#   rule_prefix: short label for citations (e.g., "CRCP", "FRCP")
#   extra_holidays: function(year) -> set of additional state-specific holidays
#       beyond the federal holiday list. Returns empty set if none.
#   notes: list of strings with important jurisdiction-specific caveats
# ---------------------------------------------------------------------------

def _no_extra_holidays(year):
    """No state-specific holidays beyond federal."""
    return set()


def _california_extra_holidays(year):
    """California: Cesar Chavez Day (March 31)."""
    return {observe_holiday(date(year, 3, 31))}


def _texas_extra_holidays(year):
    """Texas: Texas Independence Day (March 2), day after Thanksgiving."""
    return {
        observe_holiday(date(year, 3, 2)),
        nth_weekday(year, 11, 3, 4) + timedelta(days=1),  # day after Thanksgiving
    }


def _massachusetts_extra_holidays(year):
    """Massachusetts: Patriots' Day (3rd Monday in April)."""
    return {nth_weekday(year, 4, 0, 3)}


def _illinois_extra_holidays(year):
    """Illinois: Lincoln's Birthday (Feb 12), General Election Day (Nov, even years)."""
    holidays = {observe_holiday(date(year, 2, 12))}
    if year % 2 == 0:
        # First Tuesday after the first Monday in November
        first_monday = nth_weekday(year, 11, 0, 1)
        holidays.add(first_monday + timedelta(days=1))
    return holidays


def _pennsylvania_extra_holidays(year):
    """Pennsylvania: Flag Day (June 14), day after Thanksgiving."""
    return {
        observe_holiday(date(year, 6, 14)),
        nth_weekday(year, 11, 3, 4) + timedelta(days=1),
    }


def _day_after_thanksgiving(year):
    """Helper: day after Thanksgiving for states that observe it."""
    return {nth_weekday(year, 11, 3, 4) + timedelta(days=1)}


def _ohio_extra_holidays(year):
    """Ohio: Lincoln's Birthday (Feb 12)."""
    return {observe_holiday(date(year, 2, 12))}


# The master jurisdiction rules table. Keys are lowercase jurisdiction names.
STATE_RULES = {
    "colorado": {
        "short_period_threshold": 11,
        "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 35,
        "expert_plaintiff_days": 126,
        "expert_defendant_days": 98,
        "expert_rebuttal_days": 63,
        "expert_rebuttal_relative": False,
        "disco_cutoff_default": 49,
        "summary_j_response": 35,
        "summary_j_reply": 14,
        "rule_prefix": "CRCP",
        "extra_holidays": _no_extra_holidays,
        "notes": [
            "CRCP Rule 6: periods < 11 days exclude intermediate weekends/holidays.",
            "E-service adds 0 days (CRCP amendment removed the 3-day extension).",
            "RFA non-response = deemed admitted under CRCP Rule 36.",
        ],
    },
    "federal": {
        "short_period_threshold": 0,
        "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 21,
        "summary_j_reply": 14,
        "rule_prefix": "FRCP",
        "extra_holidays": _no_extra_holidays,
        "notes": [
            "FRCP Rule 6: counts all calendar days for all periods.",
            "E-service adds 0 days (amended Dec 1, 2016).",
            "Local rules may significantly alter deadlines — always check.",
            "RFA non-response = deemed admitted under FRCP Rule 36.",
        ],
    },
    "california": {
        "short_period_threshold": 0,
        "service_days": {
            "electronic": 2, "mail": 5, "mail_out_of_state": 10,
            "hand": 0, "fax": 2,
        },
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 30,
        "summary_j_reply": 14,
        "rule_prefix": "CCP",
        "extra_holidays": _california_extra_holidays,
        "notes": [
            "California counts all calendar days regardless of period length.",
            "Mail adds 5 days in-state, 10 days out-of-state (CCP § 1013).",
            "E-service and fax each add 2 court days (not calendar days).",
            "Cesar Chavez Day (March 31) is a state holiday.",
        ],
    },
    "new_york": {
        "short_period_threshold": 0,
        "service_days": {
            "electronic": 5, "mail": 5, "mail_out_of_state": 6,
            "hand": 0, "fax": 0,
        },
        "discovery_response_days": 20,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 21,
        "summary_j_reply": 14,
        "rule_prefix": "CPLR",
        "extra_holidays": _no_extra_holidays,
        "notes": [
            "New York discovery responses due in 20 days (shorter than most states).",
            "Mail and e-service both add 5 days (CPLR § 2103).",
            "Mail from outside NY adds 6 days.",
        ],
    },
    "texas": {
        "short_period_threshold": 5,
        "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 21,
        "summary_j_reply": 14,
        "rule_prefix": "TRCP",
        "extra_holidays": _texas_extra_holidays,
        "notes": [
            "TRCP: periods <= 5 days exclude intermediate weekends/holidays.",
            "Mail adds 3 days only for periods <= 5 days.",
            "Texas Independence Day (March 2) is a state holiday.",
            "Day after Thanksgiving is a state holiday.",
        ],
    },
    "florida": {
        "short_period_threshold": 7,
        "service_days": {"electronic": 0, "mail": 5, "hand": 0, "fax": 0},
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 20,
        "summary_j_reply": 14,
        "rule_prefix": "Fla. R. Civ. P.",
        "extra_holidays": _day_after_thanksgiving,
        "notes": [
            "Florida: periods < 7 days exclude intermediate weekends/holidays.",
            "Mail adds 5 days (Fla. R. Civ. P. 1.080).",
            "Discovery responses: 30 days (45 if served with process).",
            "Day after Thanksgiving is a state holiday.",
        ],
    },
    "illinois": {
        "short_period_threshold": 5,
        "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 28,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 21,
        "summary_j_reply": 14,
        "rule_prefix": "Ill. Sup. Ct. R.",
        "extra_holidays": _illinois_extra_holidays,
        "notes": [
            "Illinois: periods <= 5 days exclude intermediate weekends/holidays.",
            "Discovery responses due in 28 days (Ill. Sup. Ct. R. 213).",
            "Lincoln's Birthday (Feb 12) is a state holiday.",
            "General Election Day (even years) is a state holiday.",
        ],
    },
    "pennsylvania": {
        "short_period_threshold": 0,
        "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 30,
        "summary_j_reply": 14,
        "rule_prefix": "Pa. R. Civ. P.",
        "extra_holidays": _pennsylvania_extra_holidays,
        "notes": [
            "Pennsylvania counts all calendar days regardless of period length.",
            "Flag Day (June 14) is a state holiday.",
            "Day after Thanksgiving is a state holiday.",
        ],
    },
    "ohio": {
        "short_period_threshold": 5,
        "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 28,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 28,
        "summary_j_reply": 14,
        "rule_prefix": "Ohio R. Civ. P.",
        "extra_holidays": _ohio_extra_holidays,
        "notes": [
            "Ohio: periods <= 5 days exclude intermediate weekends/holidays.",
            "Discovery and motion responses due in 28 days.",
            "Lincoln's Birthday (Feb 12) is a state holiday.",
        ],
    },
    "georgia": {
        "short_period_threshold": 7,
        "service_days": {"electronic": 3, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 30,
        "summary_j_reply": 14,
        "rule_prefix": "Ga. R. Civ. P.",
        "extra_holidays": _day_after_thanksgiving,
        "notes": [
            "Georgia: periods < 7 days exclude intermediate weekends/holidays.",
            "Both mail and e-service add 3 days.",
            "Day after Thanksgiving is a state holiday.",
        ],
    },
    "new_jersey": {
        "short_period_threshold": 5,
        "service_days": {"electronic": 3, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 60,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 28,
        "summary_j_reply": 14,
        "rule_prefix": "N.J. R. Civ. P.",
        "extra_holidays": _no_extra_holidays,
        "notes": [
            "New Jersey discovery responses due in 60 days (much longer than most states).",
            "Both mail and e-service add 3 days.",
        ],
    },
    "massachusetts": {
        "short_period_threshold": 7,
        "service_days": {"electronic": 3, "mail": 3, "hand": 0, "fax": 0},
        "discovery_response_days": 30,
        "expert_plaintiff_days": 90,
        "expert_defendant_days": 90,
        "expert_rebuttal_days": 30,
        "expert_rebuttal_relative": True,
        "disco_cutoff_default": 0,
        "summary_j_response": 21,
        "summary_j_reply": 14,
        "rule_prefix": "Mass. R. Civ. P.",
        "extra_holidays": _massachusetts_extra_holidays,
        "notes": [
            "Massachusetts: periods < 7 days exclude intermediate weekends/holidays.",
            "Both mail and e-service add 3 days.",
            "Patriots' Day (3rd Monday in April) is a state holiday.",
        ],
    },
}

# Default rules for jurisdictions not in the built-in database
_FALLBACK_RULES = {
    "short_period_threshold": 0,
    "service_days": {"electronic": 0, "mail": 3, "hand": 0, "fax": 0},
    "discovery_response_days": 30,
    "expert_plaintiff_days": 90,
    "expert_defendant_days": 90,
    "expert_rebuttal_days": 30,
    "expert_rebuttal_relative": True,
    "disco_cutoff_default": 0,
    "summary_j_response": 21,
    "summary_j_reply": 14,
    "rule_prefix": "Rules of Civil Procedure",
    "extra_holidays": _no_extra_holidays,
    "notes": [],  # Populated dynamically with a warning
}


def _normalize_jurisdiction(jurisdiction):
    """Normalize a jurisdiction string to a lookup key."""
    return jurisdiction.lower().replace(" ", "_").replace("-", "_")


def get_jurisdiction_rules(jurisdiction):
    """Look up rules for a jurisdiction. Returns the rules dict or None if not
    found in the built-in database."""
    return STATE_RULES.get(_normalize_jurisdiction(jurisdiction))


def get_supported_jurisdictions():
    """Return list of jurisdiction keys that have built-in rules."""
    return sorted(STATE_RULES.keys())


# ---------------------------------------------------------------------------
# Holiday computation
# ---------------------------------------------------------------------------

def nth_weekday(year, month, weekday, n):
    """Return the nth occurrence of a weekday in a given month.
    weekday: 0=Monday, 6=Sunday. n: 1-based."""
    first_day = date(year, month, 1)
    first_weekday = first_day.weekday()
    diff = (weekday - first_weekday) % 7
    return first_day + timedelta(days=diff + 7 * (n - 1))


def last_weekday(year, month, weekday):
    """Return the last occurrence of a weekday in a given month."""
    if month == 12:
        last_day = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)
    diff = (last_day.weekday() - weekday) % 7
    return last_day - timedelta(days=diff)


def get_federal_holidays(year):
    """Return a set of observed federal holiday dates for a given year."""
    raw = [
        date(year, 1, 1),                          # New Year's Day
        nth_weekday(year, 1, 0, 3),                 # MLK Day
        nth_weekday(year, 2, 0, 3),                 # Presidents' Day
        last_weekday(year, 5, 0),                   # Memorial Day
        date(year, 6, 19),                          # Juneteenth
        date(year, 7, 4),                           # Independence Day
        nth_weekday(year, 9, 0, 1),                 # Labor Day
        nth_weekday(year, 10, 0, 2),                # Columbus Day
        date(year, 11, 11),                         # Veterans Day
        nth_weekday(year, 11, 3, 4),                # Thanksgiving
        date(year, 12, 25),                         # Christmas
    ]
    return {observe_holiday(h) for h in raw}


# Cache: (year, jurisdiction_key) -> frozenset of holidays.
# Avoids recomputing the same holiday set when called in loops or tests.
_holiday_cache = {}


def get_holidays(year, jurisdiction):
    """Get the full holiday set for a jurisdiction and year.
    Combines federal holidays with any state-specific holidays.
    Results are cached by (year, jurisdiction)."""
    key = (year, _normalize_jurisdiction(jurisdiction) if jurisdiction else "")
    if key not in _holiday_cache:
        holidays = get_federal_holidays(year)
        rules = get_jurisdiction_rules(jurisdiction)
        if rules and rules.get("extra_holidays"):
            holidays.update(rules["extra_holidays"](year))
        _holiday_cache[key] = frozenset(holidays)
    return _holiday_cache[key]


def collect_holidays_for_dates(date_strings, jurisdiction):
    """Build a holiday set covering all years referenced in a list of date
    strings, plus the current year and next year."""
    years = {date.today().year, date.today().year + 1}
    for d in date_strings:
        try:
            years.add(datetime.strptime(d, "%Y-%m-%d").year)
        except (ValueError, TypeError):
            pass
    holidays = set()
    for y in years:
        holidays.update(get_holidays(y, jurisdiction))
    return holidays


# ---------------------------------------------------------------------------
# Time computation
# ---------------------------------------------------------------------------

def is_business_day(d, holidays):
    """Check if a date is a business day (not weekend, not holiday)."""
    return d.weekday() < 5 and d not in holidays


def next_business_day(d, holidays):
    """If d is not a business day, advance to the next one."""
    while not is_business_day(d, holidays):
        d += timedelta(days=1)
    return d


def compute_deadline_with_threshold(start_date, days, threshold, holidays):
    """Compute a deadline using a short-period threshold.

    - Exclude the trigger day.
    - If period < threshold days: exclude intermediate Sat/Sun/holidays.
    - If period >= threshold (or threshold is 0): count every day.
    - If last day is Sat/Sun/holiday: extend to next business day.

    threshold=0 means always count all days (federal-style).
    threshold=11 means Colorado-style (< 11 days excludes weekends).
    threshold=7 means Florida/Massachusetts/Georgia-style.
    threshold=5 means Texas/Illinois/Ohio-style.
    """
    if threshold > 0 and days < threshold:
        # Exclude intermediate weekends and holidays
        current = start_date
        counted = 0
        while counted < days:
            current += timedelta(days=1)
            if is_business_day(current, holidays):
                counted += 1
        return current
    else:
        # Count every day, then roll to next business day if needed
        return next_business_day(start_date + timedelta(days=days), holidays)


def compute_backward_date(anchor_date, days, holidays):
    """Compute a date that is 'days' before the anchor date.

    For backward computation (e.g., 'serve interrogatories at least X days
    before discovery cutoff'), we subtract days and then adjust if the
    resulting date is not a business day (move EARLIER, not later).
    """
    target = anchor_date - timedelta(days=days)
    while not is_business_day(target, holidays):
        target -= timedelta(days=1)
    return target


# ---------------------------------------------------------------------------
# Service method adjustment
# ---------------------------------------------------------------------------

def get_service_extra(rules, method):
    """Return additional days to add based on rules dict and service method."""
    svc_table = rules["service_days"]
    if method == "mail_out_of_state" and "mail_out_of_state" in svc_table:
        return svc_table["mail_out_of_state"]
    return svc_table.get(method, 0)


# ---------------------------------------------------------------------------
# Deadline entry helpers
# ---------------------------------------------------------------------------

def _make_entry(matter, label, dt, rule_basis, category, priority, **extra):
    """Build a single deadline dict."""
    entry = {
        "description": f"{matter} — {label}",
        "date": dt.isoformat() if isinstance(dt, date) else dt,
        "rule_basis": rule_basis,
        "category": category,
        "priority": priority,
    }
    entry.update(extra)
    return entry


# Scheduling order fields: (json_key, display_label, category, priority)
_SCHEDULING_ORDER_FIELDS = [
    ("trial_date",                  "Trial Date",                       "trial",     "critical"),
    ("discovery_cutoff",            "Discovery Cutoff",                 "discovery", "critical"),
    ("dispositive_motion_deadline", "Dispositive Motion Filing Deadline","motions",   "critical"),
    ("pretrial_conference",         "Pretrial Conference",              "trial",     "high"),
    ("amend_pleadings_deadline",    "Deadline to Amend Pleadings",      "pleadings", "high"),
    ("join_parties_deadline",       "Deadline to Join Parties",         "pleadings", "high"),
    ("mediation_deadline",          "Mediation Deadline",               "adr",       "high"),
]


# ---------------------------------------------------------------------------
# Litigation deadline generation
# ---------------------------------------------------------------------------

def generate_litigation_deadlines(data):
    """Generate all computed deadlines for a litigation matter."""
    jurisdiction = data.get("jurisdiction", "")
    if not jurisdiction:
        raise ValueError(
            "Jurisdiction is required for litigation matters. "
            "The tool cannot compute deadlines without knowing which "
            "jurisdiction's rules to apply. Please specify a jurisdiction."
        )

    jurisdiction = _normalize_jurisdiction(jurisdiction)
    svc_method = data.get("service_method", "electronic")
    dates = data["scheduling_order_dates"]
    matter = data["matter_name"]

    # Look up jurisdiction rules (or use fallback with warning)
    rules = get_jurisdiction_rules(jurisdiction)
    if not rules:
        rules = dict(_FALLBACK_RULES)
        rules["notes"] = [
            f"WARNING: {jurisdiction} is not in the built-in rules database. "
            "These deadlines use conservative federal-style defaults. "
            "The skill should have verified the actual rules via web search. "
            "Please independently verify all computed deadlines."
        ]

    # Unpack rule parameters
    response_days = rules["discovery_response_days"]
    expert_p = rules["expert_plaintiff_days"]
    expert_d = rules["expert_defendant_days"]
    expert_r = rules["expert_rebuttal_days"]
    expert_rebuttal_relative = rules["expert_rebuttal_relative"]
    disco_cutoff_default = rules["disco_cutoff_default"]
    summary_j_response = rules["summary_j_response"]
    summary_j_reply = rules["summary_j_reply"]
    rule_prefix = rules["rule_prefix"]
    threshold = rules["short_period_threshold"]
    svc_extra = get_service_extra(rules, svc_method)

    # Build holiday set covering all relevant years
    all_date_strings = [v for v in dates.values() if isinstance(v, str)]
    if dates.get("custom_dates"):
        all_date_strings.extend(dates["custom_dates"].values())
    holidays = collect_holidays_for_dates(all_date_strings, jurisdiction)

    deadlines = []

    # --- Scheduling order dates (direct entries) ---
    parsed = {}
    for field, label, category, priority in _SCHEDULING_ORDER_FIELDS:
        dt = parse_date(dates.get(field))
        parsed[field] = dt
        if dt:
            deadlines.append(_make_entry(matter, label, dt, "Scheduling Order", category, priority))

    # Custom dates from the scheduling order
    for label, dt_str in dates.get("custom_dates", {}).items():
        dt = parse_date(dt_str)
        if dt:
            deadlines.append(_make_entry(matter, label, dt, "Scheduling Order", "custom", "high"))

    # Convenience aliases
    trial_date = parsed["trial_date"]
    discovery_cutoff = parsed["discovery_cutoff"]
    disp_motion_deadline = parsed["dispositive_motion_deadline"]

    # Parse expert dates (not in the standard fields table)
    plaintiff_expert = parse_date(dates.get("plaintiff_expert_disclosure"))
    defendant_expert = parse_date(dates.get("defendant_expert_disclosure"))
    rebuttal_expert = parse_date(dates.get("rebuttal_expert_disclosure"))

    # --- Expert disclosure deadlines ---
    if trial_date:
        # Plaintiff and defendant expert disclosures (same pattern)
        for label, so_date, days_before in [
            ("Plaintiff Expert Disclosure Deadline", plaintiff_expert, expert_p),
            ("Defendant Expert Disclosure Deadline", defendant_expert, expert_d),
        ]:
            if so_date:
                deadlines.append(_make_entry(
                    matter, label, so_date, "Scheduling Order", "experts", "critical"))
            else:
                computed = compute_backward_date(trial_date, days_before, holidays)
                deadlines.append(_make_entry(
                    matter, label, computed,
                    f"{rule_prefix} Rule 26(a)(2) ({days_before} days before trial)",
                    "experts", "critical"))

        # Rebuttal expert disclosure
        if rebuttal_expert:
            deadlines.append(_make_entry(
                matter, "Rebuttal Expert Disclosure Deadline",
                rebuttal_expert, "Scheduling Order", "experts", "high"))
        else:
            if expert_rebuttal_relative and defendant_expert:
                re_date = compute_deadline_with_threshold(
                    defendant_expert, expert_r, threshold, holidays)
                rule_note = f"{rule_prefix} Rule 26(a)(2) ({expert_r} days after opposing disclosure)"
            else:
                re_date = compute_backward_date(trial_date, expert_r, holidays)
                rule_note = f"{rule_prefix} Rule 26(a)(2) ({expert_r} days before trial)"
            deadlines.append(_make_entry(
                matter, "Rebuttal Expert Disclosure Deadline",
                re_date, rule_note, "experts", "high"))

    # --- Discovery backward deadlines ---
    effective_response_days = response_days + svc_extra
    disco_anchor = discovery_cutoff
    if not disco_anchor and trial_date and disco_cutoff_default > 0:
        disco_anchor = compute_backward_date(trial_date, disco_cutoff_default, holidays)
        deadlines.append(_make_entry(
            matter, "Discovery Cutoff (Computed)", disco_anchor,
            f"{rule_prefix} Rule 16(b)(11) ({disco_cutoff_default} days before trial)",
            "discovery", "critical"))

    if disco_anchor:
        last_disco = compute_backward_date(disco_anchor, effective_response_days, holidays)
        deadlines.append(_make_entry(
            matter, "Last Day to Serve Written Discovery (Interrogatories, RFPs, RFAs)",
            last_disco,
            f"{rule_prefix} Rules 33/34/36 ({response_days}-day response period + "
            f"{svc_extra}-day service addition, must complete before discovery cutoff; "
            "RFA non-response = deemed admitted)",
            "discovery", "critical"))

        last_depo = compute_backward_date(disco_anchor, 14, holidays)
        deadlines.append(_make_entry(
            matter, "Last Day to Notice Depositions", last_depo,
            f"{rule_prefix} Rule 30 (14-day reasonable notice, must complete before discovery cutoff)",
            "discovery", "high"))

    # --- Dispositive motion response/reply ---
    if disp_motion_deadline:
        response_date = compute_deadline_with_threshold(
            disp_motion_deadline, summary_j_response + svc_extra, threshold, holidays)
        deadlines.append(_make_entry(
            matter, "Dispositive Motion Response Due (if filed on deadline)",
            response_date,
            f"{rule_prefix} Rule 56 ({summary_j_response}-day response period + "
            f"{svc_extra}-day service addition)",
            "motions", "high"))

        reply_date = compute_deadline_with_threshold(
            response_date, summary_j_reply + svc_extra, threshold, holidays)
        deadlines.append(_make_entry(
            matter, "Dispositive Motion Reply Due (if response filed on deadline)",
            reply_date,
            f"{rule_prefix} Rule 56 ({summary_j_reply}-day reply period)",
            "motions", "medium"))

    # --- Jurisdiction notes ---
    if rules.get("notes"):
        deadlines.append(_make_entry(
            matter, f"Jurisdiction Notes ({rule_prefix})",
            date.today(), " | ".join(rules["notes"]),
            "info", "low", is_note=True))

    deadlines.sort(key=lambda x: x["date"])
    return deadlines


# ---------------------------------------------------------------------------
# Arbitration deadline generation
# ---------------------------------------------------------------------------

# Arbitration scheduling order fields: (json_key, display_label)
_ARBITRATION_FIELDS = [
    ("dispositive_motion_deadline",  "Dispositive Motion Deadline"),
    ("pretrial_conference",          "Pre-Hearing Conference"),
    ("plaintiff_expert_disclosure",  "Claimant Expert Disclosure"),
    ("defendant_expert_disclosure",  "Respondent Expert Disclosure"),
    ("rebuttal_expert_disclosure",   "Rebuttal Expert Disclosure"),
    ("amend_pleadings_deadline",     "Deadline to Amend Claims"),
    ("mediation_deadline",           "Mediation Deadline"),
]


def generate_arbitration_deadlines(data):
    """Generate deadlines for an arbitration matter.
    For arbitration, we primarily extract the scheduling order dates and
    add forum-specific procedural deadlines."""
    forum = data.get("forum", "aaa_commercial")
    dates = data["scheduling_order_dates"]
    matter = data["matter_name"]

    holidays = set()
    for y in range(date.today().year, date.today().year + 2):
        holidays.update(get_federal_holidays(y))

    deadlines = []
    custom_dates = dates.get("custom_dates", {})
    custom_keys_lower = {k.lower() for k in custom_dates}

    hearing_date = parse_date(dates.get("hearing_date")) or parse_date(dates.get("trial_date"))
    discovery_cutoff = parse_date(dates.get("discovery_cutoff"))

    # Scheduling order dates (extract as-is)
    if hearing_date:
        deadlines.append(_make_entry(
            matter, "Arbitration Hearing", hearing_date,
            "Scheduling Order", "hearing", "critical"))

    if discovery_cutoff:
        deadlines.append(_make_entry(
            matter, "Discovery/Information Exchange Cutoff", discovery_cutoff,
            "Scheduling Order", "discovery", "critical"))

    # Custom dates
    for label, dt_str in custom_dates.items():
        dt = parse_date(dt_str)
        if dt:
            deadlines.append(_make_entry(
                matter, label, dt,
                "Arbitrator's Scheduling Order", "custom", "high"))

    # Other explicitly listed dates
    for field, label in _ARBITRATION_FIELDS:
        dt = parse_date(dates.get(field))
        if dt:
            deadlines.append(_make_entry(
                matter, label, dt,
                "Arbitrator's Scheduling Order", "arbitration", "high"))

    # Forum-specific procedural deadlines
    if hearing_date:
        if "aaa" in forum:
            award_deadline = next_business_day(
                hearing_date + timedelta(days=30), holidays)
            deadlines.append(_make_entry(
                matter, "Arbitration Award Deadline", award_deadline,
                "AAA Rule R-43 (30 days after hearing close)", "award", "high"))

            if not any("exhibit" in k for k in custom_keys_lower):
                deadlines.append(_make_entry(
                    matter, "Pre-Hearing Exhibit Exchange (suggested)",
                    compute_backward_date(hearing_date, 14, holidays),
                    "AAA common practice (14 days before hearing)",
                    "hearing_prep", "medium"))

        elif "jams" in forum:
            award_deadline = next_business_day(
                hearing_date + timedelta(days=30), holidays)
            deadlines.append(_make_entry(
                matter, "Arbitration Award Deadline", award_deadline,
                "JAMS Rule 24 (30 days after hearing close)", "award", "high"))

            if not any("brief" in k for k in custom_keys_lower):
                deadlines.append(_make_entry(
                    matter, "Pre-Hearing Briefs Due (suggested)",
                    compute_backward_date(hearing_date, 14, holidays),
                    "JAMS common practice (14 days before hearing)",
                    "hearing_prep", "medium"))

            if not any("witness" in k for k in custom_keys_lower):
                deadlines.append(_make_entry(
                    matter, "Witness List Due (suggested)",
                    compute_backward_date(hearing_date, 14, holidays),
                    "JAMS common practice (14 days before hearing)",
                    "hearing_prep", "medium"))

    deadlines.sort(key=lambda x: x["date"])
    return deadlines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Compute litigation/arbitration deadlines")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    proceeding_type = data.get("proceeding_type", "litigation")

    if proceeding_type == "arbitration":
        deadlines = generate_arbitration_deadlines(data)
    else:
        deadlines = generate_litigation_deadlines(data)

    result = {
        "matter_name": data["matter_name"],
        "proceeding_type": proceeding_type,
        "jurisdiction": data.get("jurisdiction", ""),
        "forum": data.get("forum", ""),
        "service_method": data.get("service_method", "electronic"),
        "generated_date": date.today().isoformat(),
        "deadlines": deadlines,
        "attendees": data.get("attendees", []),
        "disclaimer": ""
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    event_count = sum(1 for d in deadlines if not d.get("is_note"))
    print(f"Computed {event_count} deadlines for '{data['matter_name']}'")
    print(f"Output written to: {args.output}")

    for dl in deadlines:
        if dl.get("is_note"):
            continue
        priority_marker = "!!!" if dl["priority"] == "critical" else "! " if dl["priority"] == "high" else "  "
        print(f"  {priority_marker} {dl['date']}  {dl['description']}")


if __name__ == "__main__":
    main()
