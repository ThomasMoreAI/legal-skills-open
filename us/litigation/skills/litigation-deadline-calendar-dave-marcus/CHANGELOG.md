# Changelog

## 0.3.1 — 2026-04-23

### Added
- **Google Calendar compatibility mode**: `generate_ics.py --google` produces output optimized for Google Calendar import: deterministic UIDs for dedup on reimport, `X-WR-TIMEZONE` header, no VTIMEZONE blocks (Google uses its own IANA database), no VALARM entries (Google ignores them), and LF line endings to avoid mangling by intermediate tools.
- **RFC 5545 line folding**: Long content lines are now folded at 75 octets per the iCalendar spec, with proper handling of multi-byte UTF-8 characters.
- **Dynamic VTIMEZONE selection**: VTIMEZONE blocks are now emitted only for timezones actually referenced by timed events (supports America/Denver, America/New_York, America/Chicago, America/Los_Angeles). Previously hardcoded to America/Denver only.
- **Deterministic UIDs** (Google mode): Event UIDs are derived from matter name + description + date via SHA-256, so reimporting the same calendar deduplicates instead of creating duplicates.
- **Calendar app choice in SKILL.md**: Step 1 now asks the user which calendar app they use (Outlook or Google Calendar). Step 5 passes the `--google` flag accordingly. The preference is saved to CLAUDE.md so the user is only asked once.

### Changed
- **Holiday caching**: `get_holidays()` results are now cached by `(year, jurisdiction)` to avoid redundant recomputation in loops, batch runs, or tests.

## 0.3.0 — 2026-04-06

### Added
- **Jurisdiction-specific rules database**: Built-in rules for 12 jurisdictions (Colorado, Federal, California, New York, Texas, Florida, Illinois, Pennsylvania, Ohio, Georgia, New Jersey, Massachusetts) covering holidays, service day additions, short-period computation thresholds, and discovery response periods.
- **State-specific holidays**: Each built-in jurisdiction now computes its own holiday calendar (e.g., Patriots' Day in Massachusetts, Cesar Chavez Day in California, Texas Independence Day, Lincoln's Birthday in Illinois/Ohio, Flag Day in Pennsylvania).
- **Full service method matrix**: Support for electronic, mail, hand delivery, and fax service with jurisdiction-specific day additions. California and New York support separate in-state and out-of-state mail calculations.
- **Jurisdiction auto-detection**: The skill now attempts to identify the jurisdiction from the scheduling order PDF (court name, case number format, caption) before asking the user. If it can't determine, it asks explicitly.
- **Jurisdiction notes**: Computed output includes jurisdiction-specific caveats and reminders (e.g., "New York discovery responses due in 20 days, shorter than most states").

### Changed
- Jurisdiction is now **required** for litigation matters. The script raises an error if none is provided — it never defaults or guesses.
- `compute_deadline()` now uses a unified `compute_deadline_with_threshold()` function that handles all short-period exclusion rules (Colorado <11 days, Florida/MA/GA <7 days, Texas/IL/OH <5 days, California/Federal/PA/NY count all days).
- `compute_backward_date()` simplified — no longer takes a jurisdiction parameter (backward dates always subtract calendar days and roll to preceding business day).
- `service_days()` now reads from the jurisdiction rules table instead of hardcoded if/else logic.
- Service method documentation in SKILL.md now shows the per-jurisdiction impact.

### Refactored
- Extracted `observe_holiday()` helper to eliminate repeated Saturday→Friday / Sunday→Monday logic across all holiday functions.
- Moved `parse_date()` to module level (was duplicated inside two functions).
- Jurisdiction rules dict is now passed through the call chain instead of being re-looked-up by `service_days()` and `compute_deadline()`.
- Scheduling order direct entries are now driven by a data table instead of seven near-identical if/append blocks.
- Expert disclosure blocks (plaintiff/defendant) combined into a loop.
- Arbitration custom-date detection now checks dict keys explicitly instead of converting the whole dict to a string.
- Eliminated `compute_deadline_calendar()` (was identical to `compute_deadline_with_threshold()` with threshold=0).
- Fixed ICS event count to exclude `is_note` entries that don't produce calendar events.

### Important design note
- All built-in rules AND holidays are treated as a **baseline, not a source of truth**. The verification step (Step 3) now explicitly checks for changes to state holidays in addition to procedural rules. Holidays can change (states add, rename, or remove them), and a missed holiday change can silently shift deadlines by a day.

### For non-built-in jurisdictions
- The script uses conservative federal-style defaults with a prominent warning.
- The skill should perform a web search to verify the specific state's rules before computing.

## 0.2.0 — 2026-02-27

### Changed
- Jurisdiction is now always asked explicitly. The skill no longer defaults to Colorado; it prompts for jurisdiction every time.
- Written discovery deadlines (Interrogatories, RFPs, RFAs) are now combined into a single calendar entry instead of three separate entries with identical dates.
- Disclaimer removed from computed output and calendar event descriptions.

### Added
- Source citation requirement: the skill now provides URLs to the official rule texts used in each calculation, both during verification and in the final output.
- Timed event support: deadline entries can include a `time` field (HH:MM) and `timezone` field (IANA string) to create timed calendar events instead of all-day events. Events without an explicit end time default to 17:00.
- Multi-day event support: deadline entries can include a `duration_days` field to span multiple days (e.g., a 5-day trial). Works with both timed and all-day events.
- VTIMEZONE block (America/Denver) is automatically included in the .ics file when any timed events are present.

## 0.1.0 — 2026-02-27

Initial release.

- Colorado CRCP rules built in (Rule 6 time computation, Rules 26/33/34/36 discovery, Rule 56 summary judgment, expert disclosures)
- Federal FRCP rules built in
- AAA Commercial and Employment arbitration rules
- JAMS Comprehensive and Streamlined arbitration rules
- PDF scheduling order parsing
- Backward deadline computation from scheduling order dates
- .ics calendar file generation with Outlook import support
- Calendar entry format: Matter Name — Deadline Description
- Attendee/invite support via .ics ATTENDEE fields
- Automatic reminders at 7 days and 1 day before each deadline
- Rule verification step that checks for recent amendments before computing
- Holiday calendar computation with observed-date logic
