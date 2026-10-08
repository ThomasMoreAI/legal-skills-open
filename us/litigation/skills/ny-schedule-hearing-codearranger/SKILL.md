---
name: ny-schedule-hearing-codearranger
title: Reserve a Motion Return Date in New York
description: Use when the user needs to reserve a motion return date in a New York court. Triggers include 'reserve a return date', 'NY motion return date', 'NY Part calendar', 'IAS Part calendar', 'next available motion date NY County', 'how do I schedule a hearing in NY Supreme Court', 'NY motion scheduling', 'Justice [name] Part Rules return date', 'Commercial Division motion date', 'reservations for oral argument', 'schedule an OSC return date'. Drafts the chambers email or NYSCEF self-scheduling per the assigned IAS Part's protocol and the relevant Justice's Part Rules. In New York, Justices' Part Rules govern motion scheduling — there is no central motion calendar after IAS assignment.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Motion Return Date in New York

> **NOT LEGAL ADVICE.** Verify the assigned Justice's Part
> Rules before selecting a return date.

## NY scheduling model

Once a case is assigned to an IAS Part (after RJI filing),
**all motion scheduling is done through that Justice's
Part**. New York has no central motion calendar after
assignment.

Each Part has its own scheduling protocol:

- **Self-select from a calendar**: many Justices publish a
  motion calendar on their Part Rules page; the moving party
  picks any open date
- **Email request**: moving party emails the Part clerk
  requesting a return date; clerk responds with a date
- **Phone request**: some Justices' Parts still use phone
  scheduling
- **Calendar reservation system**: some Comm Div Parts and
  high-volume Parts use an online reservation system

## How to find the protocol

1. **Find the assigned Justice's Part Rules**:
   - NY County: https://ww2.nycourts.gov/courts/1jd/supctmanh/Part%20Rules.shtml
   - Kings County: https://ww2.nycourts.gov/courts/2jd/kings/civil/Civil_Part_Rules.shtml
   - Bronx County: https://ww2.nycourts.gov/courts/12jd/supreme/civil/PartRules.shtml
   - Nassau County: https://ww2.nycourts.gov/courts/10jd/nassau/civil/
   - Queens County: https://ww2.nycourts.gov/courts/11jd/supreme/civilterm/queens_partrules.shtml
2. **Scroll to "Motion Practice" or "Scheduling"** sections
3. **Note the Part email address** — typically
   "Part##chambers@nycourts.gov" or similar
4. **Note any pre-motion-letter requirement** — some
   Justices require a 2-page letter before any formal
   motion

## Calendar selection

A safe return date is:

- **At least 13 days** out (8-day minimum + 5-day mail
  add-on if serving by mail; CPLR 2214(b) + 2103(b)(2))
- **At least 16 days** out if expecting a cross-motion under
  CPLR 2215
- **On a Part-published motion day** (e.g., "Motions heard
  on Wednesdays at 9:30 AM")
- **Not on a court holiday** (`ny-deadlines` for the
  holiday calendar)

## Chambers email template

```
Subject: Request for Return Date — Index No. [#####/YYYY] — [Caption]

Honorable [Justice Name],

I am writing on behalf of Defendant [NAME], who appears
in the above-captioned action pro se. I respectfully
request a return date for a motion to [BRIEF DESCRIPTION,
e.g., "dismiss the complaint pursuant to CPLR 3211(a)(5)"].

Per the Court's Part Rules, the earliest available motion
date is [DATE]. The motion papers will be served by
[METHOD] on or before [DATE], satisfying the CPLR 2214(b)
8-day minimum service period plus any applicable mail
add-on under CPLR 2103(b)(2).

If a different return date is preferred or required, I will
adjust accordingly. Please confirm the date and any other
Part-Rule requirements (e.g., courtesy copy, oral-argument
request, etc.).

Thank you for your consideration.

Respectfully submitted,

[Print Name]
Self-Represented Defendant
[Phone, email]
Index No. [#####/YYYY]
```

## OSC scheduling

For an Order to Show Cause, the moving party brings the
unsigned OSC + supporting papers to chambers ex parte:

1. **NY County**: 60 Centre Street, Room 130 — Ex Parte
   Office (also accepts emergency electronic submission via
   designated email)
2. **Kings County**: 360 Adams Street, Room 296 — Ex Parte
3. **Other counties**: chambers email or Part-Rule procedure
4. The Justice signs the OSC and sets the return date and
   any TRO terms
5. The signed OSC is then served on opposing parties per
   the directions in the OSC

## Commercial Division specific

Comm Div Parts often:

- Use online reservation systems
- Require pre-motion letters
- Permit only one motion per pre-motion-letter exchange
- Schedule a "discovery conference" before motion practice

Check 22 NYCRR § 202.70(g) Rules and the specific Justice's
supplemental rules.

## Composition with other ny- skills

- `ny-draft-note` — drafting the Notice of Motion / OSC with
  the return date
- `ny-deadlines` — minimum-notice computation
- `ny-nyco` / `ny-kings` / `ny-bronx` / `ny-nassau` /
  `ny-queens` / `ny-county-courts` — court-specific Part
  protocols
- `ny-file-packet` — assembling the packet for filing once
  the date is reserved
