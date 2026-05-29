---
name: litigation-deadline-calendar-dave-marcus
title: Litigation Deadline Calendar
description: 'Calendar litigation and arbitration deadlines from a scheduling order. Parses a PDF scheduling order, identifies key dates, computes backward deadlines using the applicable rules (Colorado CRCP, Federal FRCP, or arbitration forum rules for AAA/JAMS), and generates an .ics calendar file for Outlook or Google Calendar import.

  Use this skill whenever the user mentions: litigation deadlines, scheduling order, case management order, deadline calendaring, discovery deadlines, trial preparation deadlines, arbitration scheduling, or anything related to computing or tracking court or arbitration deadlines. Also trigger when the user uploads a PDF that appears to be a court scheduling order or arbitration scheduling order.'
author: Dave Marcus
author_url: https://lawve.ai/en/skills/litigation-deadline-calendar-dave-marcus
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Arbitration Rules
  path: references/arbitration-rules.md
- title: Colorado Crcp
  path: references/colorado-crcp.md
- title: Federal Frcp
  path: references/federal-frcp.md
---

# Litigation Deadline Calendar

This skill takes a scheduling order (PDF upload), determines the applicable
procedural rules, extracts key dates, computes all backward deadlines, and
generates an .ics calendar file the user can import into Outlook or Google
Calendar.

## Quick Start Workflow

1. **Gather information** from the user
2. **Parse the scheduling order** PDF
3. **Verify the rules** are current
4. **Compute deadlines** using the scripts
5. **Generate .ics file** and deliver to user

---

## Step 1: Gather Information

Ask the user for the following. They may provide some of this upfront; fill
in what you have and ask for the rest.

**Required:**
- The scheduling order PDF (uploaded file)
- Matter name (how the user wants it displayed on calendar entries, e.g., "Smith v. Jones Co.")
- Proceeding type: **litigation** or **arbitration**

**If litigation:**
- Jurisdiction: **Try to determine from the scheduling order first.** Look for
  the court name, case number format, or header to identify the jurisdiction.
  Common patterns:
  - "District Court, ___ County, Colorado" → Colorado
  - "United States District Court" → Federal
  - "Superior Court of California" → California
  - State name in the court caption → that state
  If the scheduling order clearly identifies the jurisdiction, confirm it with
  the user: "This appears to be a [State] case based on the court name. Can you
  confirm?"
  If you **cannot determine the jurisdiction from the PDF**, always ask the user
  explicitly. **Never guess or default.** The tool will raise an error if no
  jurisdiction is provided.
- Service method: **electronic** (default), **mail**, **hand**, or **fax**.
  Service method affects deadline computation differently per jurisdiction:
  - Colorado: e-service adds 0 days, mail adds 3 days
  - Federal: e-service adds 0 days, mail adds 3 days
  - California: e-service adds 2 court days, mail adds 5 days (10 out-of-state)
  - New York: e-service adds 5 days, mail adds 5 days (6 out-of-state)
  - Florida: e-service adds 0 days, mail adds 5 days
  - Georgia/Massachusetts/New Jersey: e-service adds 3 days, mail adds 3 days
  - Texas/Illinois/Pennsylvania/Ohio: e-service adds 0 days, mail adds 3 days
  For California and New York mail service, also ask whether service is
  in-state or out-of-state (use "mail" for in-state, "mail_out_of_state" for
  out-of-state).

**If arbitration:**
- Forum: AAA Commercial, AAA Employment, JAMS Comprehensive, or JAMS Streamlined

**Optional (but check saved preferences first):**
- Calendar application: **Outlook** (default) or **Google Calendar**. This
  controls the .ics output format. Google Calendar mode uses deterministic
  UIDs (so reimporting deduplicates), omits VTIMEZONE and VALARM blocks
  (Google ignores them), and uses LF line endings.
  **Persistence:** Before asking, check CLAUDE.md for a saved
  `calendar_app` preference (e.g., `calendar_app: google` or
  `calendar_app: outlook`). If found, use it silently — do not re-ask.
  If not found, ask the user which calendar app they use and save
  their choice to CLAUDE.md so it carries forward to future sessions.
  Example CLAUDE.md entry: `calendar_app: google`
- Attendee email addresses (people to invite to the calendar entries)
- Any deadlines they already know are unusual or modified by the court

**Built-in jurisdictions** (full rules database including state-specific holidays,
service day additions, short-period computation thresholds, and discovery response
periods): Colorado, Federal, California, New York, Texas, Florida, Illinois,
Pennsylvania, Ohio, Georgia, New Jersey, Massachusetts.

**Other jurisdictions**: The tool will use conservative federal-style defaults
and the skill should perform a web search to verify the specific state's rules
before computing. Always warn the user that non-built-in jurisdiction deadlines
should be independently verified.

Present this as a simple conversation, not a form. For example:
"What's the matter name as you'd like it to appear on calendar entries?"
"Is this litigation or arbitration?"
"This looks like it's from the District Court of Denver County — is this a
Colorado state case?"

---

## Step 2: Parse the Scheduling Order

Read the uploaded PDF using the Read tool. Extract every date mentioned in the
order along with what it represents. Common dates to look for:

**Litigation scheduling orders typically include:**
- Trial date
- Discovery cutoff / completion date
- Dispositive motion deadline
- Pretrial / trial preparation conference date
- Deadline to amend pleadings
- Deadline to join parties
- Plaintiff expert disclosure deadline
- Defendant expert disclosure deadline
- Rebuttal expert disclosure deadline
- Mediation deadline
- Motions in limine deadline
- Proposed jury instructions deadline
- Witness and exhibit list deadline

**Arbitration scheduling orders typically include:**
- Hearing date(s)
- Discovery / information exchange cutoff
- Expert disclosure deadlines
- Pre-hearing brief deadline
- Exhibit exchange deadline
- Witness list deadline
- Dispositive motion deadline (if permitted)
- Mediation deadline

After parsing, **show the user what you found** and ask them to confirm before
proceeding. Format it as a clean list:

"Here's what I extracted from the scheduling order:
- Trial Date: September 15, 2026
- Discovery Cutoff: July 28, 2026
- Dispositive Motion Deadline: June 15, 2026
[etc.]

Does this look right? Anything I missed or got wrong?"

This confirmation step is important because PDF parsing can miss dates or
misinterpret them, and an error here cascades through every computed deadline.

---

## Step 3: Verify Rules Are Current

Before computing deadlines, verify the rules and provide sources.

**Verification procedure:**
1. Search the web for the current text of the applicable rules AND any recent
   amendments:
   - For Colorado: search "Colorado Rules of Civil Procedure amendments [current year]"
     and "CRCP rule changes [current year]" on coloradojudicial.gov
   - For Federal: search "Federal Rules of Civil Procedure amendments [current year]"
   - For other states: search "[State] rules of civil procedure [current year]"
   - For AAA: search "AAA arbitration rules update [current year]"
   - For JAMS: search "JAMS arbitration rules update [current year]"

2. **Verify state holidays.** The tool has built-in holiday functions for 12
   states, but holidays can and do change (states may add, rename, or remove
   holidays). Search for:
   - "[State] legal holidays [current year]"
   - "[State] court holidays [current year]"
   - "[State] court closures [current year]"
   Compare what you find against the holidays the script will compute. If a
   state has added, renamed, or removed a holiday, tell the user and adjust
   the computation. Getting a holiday wrong can silently shift deadlines by
   a day.

3. For built-in jurisdictions, compare what you find against the reference files
   and the `STATE_RULES` dictionary in `scripts/compute_deadlines.py`:
   - Colorado: `references/colorado-crcp.md`
   - Federal: `references/federal-frcp.md`
   - Arbitration: `references/arbitration-rules.md`
   - Other built-in states: check the `STATE_RULES` entry in the script

4. If you find a discrepancy (in rules OR holidays):
   - Tell the user: "I found that [rule/holiday X] was changed on [date]. The
     built-in version says [old]; the current version says [new]. I'll use the
     updated version for this calculation."
   - Use the corrected rule or holiday for computation.

5. If you cannot verify (e.g., search fails):
   - Tell the user: "I wasn't able to verify whether the [jurisdiction] rules
     have been updated recently. The built-in rules are current as of early 2026.
     You may want to independently confirm the key time periods."

**For non-built-in jurisdictions** (any state other than Colorado):
Search for the specific state's rules of civil procedure, focusing on:
- Time computation rules (equivalent of Rule 6)
- Discovery response deadlines
- Expert disclosure deadlines
- Summary judgment timelines
- Legal holidays

Present what you find to the user for confirmation before computing.

**Source citation requirement — this is mandatory:**
After verifying the rules, always provide the user with a "Sources" section
listing the specific URLs where they can independently check the rules being
applied. This is critical because the user manages outside counsel and needs
to be able to verify the rules independently. Format:

"**Sources for [Jurisdiction] rules used in this calculation:**
- [Rule description]: [URL to official source or authoritative reference]
- [Rule description]: [URL]"

Preferred official sources by jurisdiction:
- Colorado: coloradojudicial.gov or courts.state.co.us
- Federal: law.cornell.edu/rules/frcp or uscourts.gov
- AAA: adr.org
- JAMS: jamsadr.com
- Other states: the state judiciary's official website

If you cannot find an official source for a rule, say so explicitly rather
than omitting the citation.

---

## Step 4: Compute Deadlines

Create the input JSON file for the computation script. The format is:

```json
{
    "matter_name": "Smith v. Jones Co.",
    "proceeding_type": "litigation",
    "jurisdiction": "colorado",
    "forum": "",
    "service_method": "electronic",
    "scheduling_order_dates": {
        "trial_date": "2026-09-15",
        "discovery_cutoff": "2026-07-28",
        "dispositive_motion_deadline": "2026-06-15",
        "pretrial_conference": "2026-08-15",
        "plaintiff_expert_disclosure": null,
        "defendant_expert_disclosure": null,
        "rebuttal_expert_disclosure": null,
        "amend_pleadings_deadline": "2026-03-15",
        "join_parties_deadline": "2026-03-15",
        "mediation_deadline": "2026-05-01",
        "hearing_date": null,
        "custom_dates": {
            "Motions in Limine": "2026-08-01",
            "Proposed Jury Instructions": "2026-08-01"
        }
    },
    "attendees": ["jane@company.com", "bob@lawfirm.com"]
}
```

Use `null` for any dates not present in the scheduling order. The script will
compute them from the rules where applicable (e.g., expert deadlines computed
backward from trial date).

Add any dates from the scheduling order that don't fit standard fields into
`custom_dates` with a descriptive label.

### Optional Fields on Any Deadline Entry

The computed deadlines JSON (output of `compute_deadlines.py`) supports three
optional fields on individual deadline entries that control how they appear
in the .ics calendar:

- **`time`** (string, HH:MM in 24-hour format): Makes the event a timed event
  instead of all-day. Example: `"time": "08:30"`. If no explicit end time is
  provided, the event is assumed to end at 17:00 on the last day.
- **`timezone`** (string, IANA timezone): The timezone for timed events.
  Example: `"timezone": "America/Denver"`. Defaults to `America/Denver` if
  omitted.
- **`duration_days`** (integer): Makes the event span multiple days.
  Example: `"duration_days": 5` for a 5-day trial starting on the event date.
  If combined with `time`, the event starts at the specified time on day 1 and
  ends at 17:00 on the last day. If used without `time`, it creates a multi-day
  all-day event.

These fields are useful for events like multi-day trials or hearings, or when
the scheduling order specifies a particular time for a conference or deadline.

Run the computation:
```bash
python scripts/compute_deadlines.py --input /tmp/input.json --output /tmp/computed.json
```

Review the output and sanity-check the computed dates:
- Do all dates fall on business days?
- Are the backward-computed dates BEFORE their anchor deadlines?
- Do expert disclosure deadlines fall in a reasonable sequence?
- For arbitration: are you using arbitration rules, not litigation rules?

---

## Step 5: Generate the .ics File

Run the calendar generation. If the user specified Google Calendar, add the
`--google` flag:

```bash
# Outlook / Apple Calendar (default):
python scripts/generate_ics.py --input /tmp/computed.json --output /path/to/output/[matter_name]_deadlines.ics

# Google Calendar:
python scripts/generate_ics.py --input /tmp/computed.json --output /path/to/output/[matter_name]_deadlines.ics --google
```

Google Calendar mode produces a file optimized for Google's import behavior:
deterministic UIDs (reimporting updates instead of duplicating), no VTIMEZONE
blocks (Google uses its own timezone database), no VALARM entries (Google
ignores them and applies its own default reminders), and LF line endings.

The output file should go to the user's workspace folder with a descriptive
filename based on the matter name.

**Before delivering the file, show the user a summary:**

"Here are the deadlines I've computed for [Matter Name]:

[List each deadline with date, description, and rule basis]

**Critical deadlines** (marked with !!!) need special attention.

The .ics file includes reminders at 7 days and 1 day before each deadline.
[If Google Calendar mode:] Note: Google Calendar uses its own default
reminders and will not import the custom reminder settings.
[If attendees were specified:] Calendar invitations will be sent to [names]
when you import the file.

**Important:** These deadlines are computed from the scheduling order and
applicable rules. They should be independently verified by counsel, especially
regarding local rules and any subsequent orders that may modify deadlines.

**Sources for the rules applied:**
[List each source URL used — same sources provided in Step 3]"

Then provide the .ics file link. The sources should always appear in the final
output so the user has them right alongside the deadlines, not just earlier in
the conversation where they might scroll past them.

---

## Reference Files

Read these reference files for the detailed rules used in computation:

- **Colorado CRCP rules**: `references/colorado-crcp.md`
  - Read when jurisdiction is Colorado
  - Covers Rule 6 (time computation), Rules 26/33/34/36 (discovery), Rule 56 (summary judgment)

- **Federal FRCP rules**: `references/federal-frcp.md`
  - Read when jurisdiction is Federal
  - Key difference: FRCP counts all days for all periods; adds 3 days for e-service

- **Arbitration rules**: `references/arbitration-rules.md`
  - Read when proceeding type is arbitration
  - Covers AAA Commercial, AAA Employment, JAMS Comprehensive, JAMS Streamlined
  - Critical: Do NOT apply litigation time-computation rules to arbitration

---

## Calendar Entry Format

All calendar entries follow this format:
**[Matter Name] — [Deadline Description]**

Examples:
- Smith v. Jones Co. — Trial Date
- Smith v. Jones Co. — Last Day to Serve Interrogatories
- Smith v. Jones Co. — Plaintiff Expert Disclosure Deadline
- Smith v. Jones Co. — Arbitration Hearing

The matter name always comes first so that entries from different cases are
visually distinguishable in a crowded calendar.

---

## Edge Cases and Warnings

**Scheduling order supersedes default rules:**
If the scheduling order sets a deadline that differs from what the rules would
produce (e.g., a shorter discovery period), always use the scheduling order date.
Only use rule-based computation for deadlines NOT specified in the order.

**Arbitration is not litigation:**
If the user says "arbitration," never apply CRCP or FRCP time-computation rules.
Arbitration deadlines come from the arbitrator's order and the forum rules. If
the arbitrator's order incorporates any litigation rules by reference, note that
to the user but still apply them as the arbitrator specified.

**Local rules:**
For federal cases, local rules can significantly alter deadlines (especially
for summary judgment responses and pretrial procedures). Flag this to the user:
"Federal courts often have local rules that modify these default deadlines.
Check the local rules for [district] to verify."

**Amended scheduling orders:**
If the user mentions that the scheduling order has been amended, ask for the
most recent version. Earlier versions may have superseded dates.

**Already-passed deadlines:**
If any computed deadline falls before today's date, flag it prominently:
"WARNING: [Deadline] computed as [date], which has already passed. Verify
this is correct or whether an extension was granted."
