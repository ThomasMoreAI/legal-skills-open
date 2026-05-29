#!/usr/bin/env python3
"""
ICS Calendar File Generator

Takes the computed deadlines JSON and generates an .ics file that can be
imported into Outlook, Google Calendar, Apple Calendar, etc.

Usage:
    python generate_ics.py --input computed.json --output deadlines.ics
    python generate_ics.py --input computed.json --output deadlines.ics --google

The .ics file will include:
- All-day, timed, and multi-day events
- Event descriptions with the rule basis
- Priority levels mapped to iCalendar priority values
- Attendee invitations (if email addresses are provided)
- Alarms/reminders: 7 days and 1 day before each deadline

Google Calendar mode (--google) adjusts output for better compatibility:
- Uses deterministic UIDs for idempotent reimport (deduplication)
- Omits VTIMEZONE blocks (Google uses its own IANA timezone database)
- Skips VALARM entries (Google ignores them and uses its own defaults)
- Uses LF line endings instead of CRLF (Google's import handles both,
  but LF avoids issues with some intermediate tools)
- Adds X-WR-TIMEZONE header for Google's timezone inference

Supported deadline fields:
- "date" (required): YYYY-MM-DD
- "time" (optional): HH:MM in 24-hour format — makes it a timed event
- "timezone" (optional): IANA timezone string, e.g. "America/Denver"
- "duration_days" (optional): integer — makes it a multi-day event
  If time is set without an explicit end time, the event ends at 17:00.
"""

import json
import sys
import argparse
import hashlib
import uuid
from datetime import date, datetime, timedelta


# ---------------------------------------------------------------------------
# ICS text helpers
# ---------------------------------------------------------------------------

def escape_ics_text(text):
    """Escape special characters for iCalendar text values."""
    text = text.replace("\\", "\\\\")
    text = text.replace(";", "\\;")
    text = text.replace(",", "\\,")
    text = text.replace("\n", "\\n")
    return text


def fold_line(line, max_octets=75):
    """Fold a content line per RFC 5545 §3.1.
    Lines longer than max_octets are split with a CRLF followed by a
    single space. We fold on UTF-8 byte boundaries to avoid splitting
    multi-byte characters."""
    encoded = line.encode("utf-8")
    if len(encoded) <= max_octets:
        return line

    chunks = []
    while len(encoded) > max_octets:
        # First chunk gets full width; continuations lose 1 byte to the
        # leading space.
        limit = max_octets if not chunks else max_octets - 1
        chunk = encoded[:limit]
        # Don't split in the middle of a multi-byte UTF-8 sequence.
        # Walk back if we landed on a continuation byte (10xxxxxx).
        while limit > 0 and (chunk[-1] & 0xC0) == 0x80:
            limit -= 1
            chunk = encoded[:limit]
        chunks.append(chunk.decode("utf-8"))
        encoded = encoded[limit:]

    if encoded:
        chunks.append(encoded.decode("utf-8"))

    # Join: first chunk bare, subsequent chunks prefixed with a space
    return ("\r\n ".join(chunks) if chunks else line)


def priority_to_ics(priority_str):
    """Map our priority levels to iCalendar priority values.
    iCal: 1-4 = high, 5 = normal, 6-9 = low."""
    return {"critical": 1, "high": 3, "medium": 5, "low": 7}.get(priority_str, 5)


def category_to_color(category):
    """Suggest calendar categories/colors based on deadline type.
    Note: actual color rendering depends on the calendar application."""
    mapping = {
        "trial": "Red Category",
        "discovery": "Blue Category",
        "experts": "Purple Category",
        "motions": "Orange Category",
        "pleadings": "Yellow Category",
        "adr": "Green Category",
        "hearing": "Red Category",
        "hearing_prep": "Orange Category",
        "award": "Red Category",
        "arbitration": "Blue Category",
        "custom": "Yellow Category",
    }
    return mapping.get(category, "Blue Category")


def deterministic_uid(matter, description, date_str):
    """Generate a stable UID from event content so that reimporting the
    same calendar deduplicates in Google Calendar (which keys on UID)."""
    raw = f"{matter}|{description}|{date_str}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]
    return f"{digest}@litigation-deadline-calendar"


# ---------------------------------------------------------------------------
# VTIMEZONE definitions
# ---------------------------------------------------------------------------

# Common US timezones. The key must match the IANA timezone ID.
VTIMEZONE_BLOCKS = {
    "America/Denver": """\
BEGIN:VTIMEZONE
TZID:America/Denver
BEGIN:STANDARD
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
TZOFFSETFROM:-0600
TZOFFSETTO:-0700
TZNAME:MST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
TZOFFSETFROM:-0700
TZOFFSETTO:-0600
TZNAME:MDT
END:DAYLIGHT
END:VTIMEZONE""",
    "America/New_York": """\
BEGIN:VTIMEZONE
TZID:America/New_York
BEGIN:STANDARD
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
TZOFFSETFROM:-0400
TZOFFSETTO:-0500
TZNAME:EST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
TZOFFSETFROM:-0500
TZOFFSETTO:-0400
TZNAME:EDT
END:DAYLIGHT
END:VTIMEZONE""",
    "America/Chicago": """\
BEGIN:VTIMEZONE
TZID:America/Chicago
BEGIN:STANDARD
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
TZOFFSETFROM:-0500
TZOFFSETTO:-0600
TZNAME:CST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
TZOFFSETFROM:-0600
TZOFFSETTO:-0500
TZNAME:CDT
END:DAYLIGHT
END:VTIMEZONE""",
    "America/Los_Angeles": """\
BEGIN:VTIMEZONE
TZID:America/Los_Angeles
BEGIN:STANDARD
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
END:DAYLIGHT
END:VTIMEZONE""",
}


# ---------------------------------------------------------------------------
# ICS generation
# ---------------------------------------------------------------------------

def generate_ics(data, output_path, google_mode=False):
    """Generate an .ics file from computed deadlines data.

    Args:
        data: dict with matter_name, deadlines, attendees
        output_path: path to write the .ics file
        google_mode: if True, output is optimized for Google Calendar
    """
    matter = data["matter_name"]
    deadlines = data["deadlines"]
    attendees = data.get("attendees", [])

    # Collect all timezones referenced by timed events
    timezones_used = set()
    for dl in deadlines:
        if dl.get("time") and not dl.get("is_note"):
            timezones_used.add(dl.get("timezone", "America/Denver"))

    lines = []
    lines.append("BEGIN:VCALENDAR")
    lines.append("VERSION:2.0")
    lines.append("PRODID:-//Litigation Deadline Calendar//EN")
    lines.append("CALSCALE:GREGORIAN")
    lines.append("METHOD:PUBLISH")
    lines.append(f"X-WR-CALNAME:{escape_ics_text(matter)} - Deadlines")

    if google_mode:
        # Google Calendar uses X-WR-TIMEZONE to infer the default timezone
        # for events that don't specify one. Pick the most-used timezone,
        # falling back to America/Denver.
        default_tz = "America/Denver"
        if timezones_used:
            default_tz = max(timezones_used, key=lambda tz:
                sum(1 for dl in deadlines if dl.get("timezone", "America/Denver") == tz))
        lines.append(f"X-WR-TIMEZONE:{default_tz}")
    else:
        # Non-Google: embed VTIMEZONE blocks for all referenced timezones
        for tz in sorted(timezones_used):
            block = VTIMEZONE_BLOCKS.get(tz)
            if block:
                for tz_line in block.strip().split("\n"):
                    lines.append(tz_line)

    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    for dl in deadlines:
        if dl.get("is_note"):
            continue

        # Deterministic UIDs let Google Calendar deduplicate on reimport.
        # Random UUIDs are better for Outlook (avoids accidental overwrites).
        if google_mode:
            uid = deterministic_uid(matter, dl["description"], dl["date"])
        else:
            uid = str(uuid.uuid4())

        dl_date = datetime.strptime(dl["date"], "%Y-%m-%d").date()

        event_time = dl.get("time")
        timezone = dl.get("timezone", "America/Denver")
        duration_days = dl.get("duration_days")

        description_parts = [
            f"Rule Basis: {dl['rule_basis']}",
            f"Category: {dl['category'].replace('_', ' ').title()}",
            f"Priority: {dl['priority'].upper()}"
        ]
        description = "\\n".join(description_parts)

        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{uid}")
        lines.append(f"DTSTAMP:{now}")

        if event_time:
            hour, minute = event_time.split(":")
            start_str = dl_date.strftime("%Y%m%d") + f"T{hour}{minute}00"
            lines.append(f"DTSTART;TZID={timezone}:{start_str}")

            if duration_days and duration_days > 1:
                end_date = dl_date + timedelta(days=duration_days - 1)
                end_str = end_date.strftime("%Y%m%d") + "T170000"
            else:
                end_str = dl_date.strftime("%Y%m%d") + "T170000"
            lines.append(f"DTEND;TZID={timezone}:{end_str}")

        elif duration_days and duration_days > 1:
            dtstart = dl_date.strftime("%Y%m%d")
            dtend = (dl_date + timedelta(days=duration_days)).strftime("%Y%m%d")
            lines.append(f"DTSTART;VALUE=DATE:{dtstart}")
            lines.append(f"DTEND;VALUE=DATE:{dtend}")

        else:
            dtstart = dl_date.strftime("%Y%m%d")
            dtend = (dl_date + timedelta(days=1)).strftime("%Y%m%d")
            lines.append(f"DTSTART;VALUE=DATE:{dtstart}")
            lines.append(f"DTEND;VALUE=DATE:{dtend}")

        lines.append(f"SUMMARY:{escape_ics_text(dl['description'])}")
        lines.append(f"DESCRIPTION:{escape_ics_text(description)}")
        lines.append(f"PRIORITY:{priority_to_ics(dl['priority'])}")
        lines.append(f"CATEGORIES:{category_to_color(dl['category'])}")
        lines.append("TRANSP:TRANSPARENT")

        for email in attendees:
            lines.append(
                f"ATTENDEE;RSVP=TRUE;PARTSTAT=NEEDS-ACTION;CN={email}:mailto:{email}")

        # Google Calendar ignores VALARM on import and uses its own default
        # reminders, so we skip them in Google mode to keep the file clean.
        if not google_mode:
            lines.append("BEGIN:VALARM")
            lines.append("TRIGGER:-P7D")
            lines.append("ACTION:DISPLAY")
            lines.append(f"DESCRIPTION:7 days until: {escape_ics_text(dl['description'])}")
            lines.append("END:VALARM")

            lines.append("BEGIN:VALARM")
            lines.append("TRIGGER:-P1D")
            lines.append("ACTION:DISPLAY")
            lines.append(f"DESCRIPTION:TOMORROW: {escape_ics_text(dl['description'])}")
            lines.append("END:VALARM")

        lines.append("END:VEVENT")

    lines.append("END:VCALENDAR")

    # Apply RFC 5545 line folding to any lines exceeding 75 octets
    folded = [fold_line(line) for line in lines]

    # Google import handles both CRLF and LF, but some tools between the
    # user and Google (email clients, cloud storage previews) can mangle
    # CRLF. LF-only is safer for that path. Outlook requires CRLF per spec.
    line_ending = "\n" if google_mode else "\r\n"
    with open(output_path, "w", newline="") as f:
        f.write(line_ending.join(folded) + line_ending)

    event_count = sum(1 for dl in deadlines if not dl.get("is_note"))
    mode_label = " (Google Calendar mode)" if google_mode else ""
    print(f"Generated .ics file with {event_count} events{mode_label}: {output_path}")
    print(f"Matter: {matter}")
    if attendees:
        print(f"Attendees: {', '.join(attendees)}")
    print(f"\nTo use: Import this file into Outlook, Google Calendar, or Apple Calendar.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate .ics calendar file from computed deadlines")
    parser.add_argument("--input", required=True,
                        help="Path to computed deadlines JSON file")
    parser.add_argument("--output", required=True,
                        help="Path for output .ics file")
    parser.add_argument("--google", action="store_true",
                        help="Optimize output for Google Calendar compatibility")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    generate_ics(data, args.output, google_mode=args.google)


if __name__ == "__main__":
    main()
