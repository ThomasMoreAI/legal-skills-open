---
name: or-draft-note-codearranger
title: Draft an Oregon Notice of Hearing
description: Use this skill when the user asks to draft a Notice of Hearing — the Oregon scheduling form that places a motion on the court's calendar (analogous to Washington's "Note for Motion Docket"). Triggers include "notice of hearing", "note for hearing", "schedule the motion", "draft the hearing notice", "draft a notice for the motion", "draft a note for motion docket" (the Washington-flavored phrase still triggers the skill — but the agent should redirect to "Notice of Hearing" terminology for Oregon practice). Scaffolds the Notice of Hearing to a single page; if the case is in Multnomah, detects the local SLR 5.015 conventions; if in Washington County (Oregon), applies SLR 5.045 (filed simultaneously with the motion). Composes with `or-statewide-format` (always) and the relevant court skill (`or-multcc`, `or-wccc`, or `or-county-courts`).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Oregon Notice of Hearing

Scaffold the scheduling form that places a motion on the
court's calendar. The Notice of Hearing is Oregon's analog to
Washington's "Note for Motion Docket".

> **NOT LEGAL ADVICE.** This skill scaffolds a scheduling form
> as a drafting aid. The user — not the skill — chooses the
> motion, the date requested, and the relief sought. Verify
> every rule, deadline, and local-rule requirement before
> filing. Pair with substantive review by counsel where stakes
> warrant.

> **Terminology**: Oregon practice calls this a **Notice of
> Hearing** (or "Notice of Hearing on Motion"). Some
> practitioners coming from Washington may say "note for
> motion docket" — this skill responds to both but produces
> the Oregon-correct form.

## When required

Most Oregon circuit courts require a Notice of Hearing to be
filed and served before a motion can be heard. Some judges
allow ex-parte requests to the judicial assistant in lieu of a
formal Notice — check the assigned judge's standing order.

Local-rule timing:

- **Multnomah SLR 5.015**: Notice filed within 3 business days
  of JA confirming the date
- **Washington Co (OR) SLR 5.045**: Notice filed
  **simultaneously** with the motion
- **Other counties**: per local SLR; usually filed
  simultaneously with or shortly after the motion

## What this skill produces

A single-page Notice of Hearing with:

1. **Caption** (court header, parties, case number, document
   title: "NOTICE OF HEARING ON [MOTION TITLE]")
2. **Hearing details panel** in the right column of the
   caption: date, time, courtroom or WebEx, mode, judge
3. **Notice text** identifying the motion, the date and time,
   the location, and the connection information for remote
   hearings
4. **Oral argument designation** (if requested)
5. **Signature block**
6. **Certificate of Service**

## Inputs to ask the user

- **Caption**: court / county / parties / case number
- **Motion title**: the title of the motion being noticed
- **Hearing date**: confirmed by the JA / Civil Division
- **Hearing time**: morning or afternoon block
- **Mode**: in-person, WebEx, telephone
- **Courtroom / connection info**: room number for in-person;
  WebEx URL / meeting ID for remote
- **Assigned judge**: Hon. [Name]
- **Estimated argument time**: e.g., 20 minutes

## Template

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH

VELOCITY INVESTMENTS, LLC,      │   Case No. 25CV12345
                                │
     Plaintiff,                 │   NOTICE OF HEARING ON
                                │   DEFENDANT'S MOTION TO
     v.                         │   COMPEL PRODUCTION OF
                                │   DOCUMENTS UNDER ORCP 46 A
JOHN DOE,                       │
                                │   HEARING: [Date] at [Time]
     Defendant.                 │   PLACE: Courtroom [#] /
                                │   WebEx (link below)
                                │   BEFORE: Hon. [Judge]
                                │   MODE: [In person / WebEx]
                                │   ORAL ARGUMENT: [time
                                │   estimate]
────────────────────────────────────────────────────────────

TO:  Plaintiff Velocity Investments, LLC and its counsel of
     record [Name, OSB #, Address, Email]

PLEASE TAKE NOTICE that Defendant's Motion to Compel
Production of Documents Under ORCP 46 A, filed [date], will
be heard before the Honorable [Judge Name], Department /
Courtroom [#] of the Circuit Court of the State of Oregon
for the County of Multnomah, on:

       [DAY OF WEEK], [MONTH DAY], 20[YY] at [TIME] [AM/PM]
       Hearing mode: [In person / WebEx]
       WebEx information: [URL or meeting ID and password]
       Estimated argument: [20 minutes]

The hearing was reserved with the Judicial Assistant to the
Hon. [Judge Name] on [date]; confirmation is attached as
Exhibit 1.

Defendant respectfully requests oral argument under UTCR
5.050.

DATED this ____ day of __________, 20__.

______________________________________
JOHN DOE
Defendant, pro se
[Address]
[Phone]
[Email]


                  CERTIFICATE OF SERVICE
[Per UTCR 1.090, served on Plaintiff and counsel via
File and Serve eService and by email to [opposing email]]
```

## County-specific variations

### Multnomah

Notice filed within 3 business days of JA confirmation.
Filing through File and Serve, document code "Notice of
Hearing".

The Multnomah courthouse is the Central Courthouse, 1200 SW
1st Avenue. Identify "Multnomah County Central Courthouse"
in the Place line if helpful.

### Washington Co (Oregon)

Notice filed **simultaneously** with the motion under WCCC
SLR 5.045. The motion and Notice are uploaded together in
File and Serve.

The courthouse is at 145 NE 2nd Avenue, Hillsboro.

### Other counties

Per local SLR. The Notice typically:

- Is filed simultaneously with or shortly after the motion
- Identifies the assigned judge if one has been assigned
- Reflects the mode confirmed by the court coordinator or
  Civil Division

## Multiple motions noticed for the same hearing

If several motions are being argued together (e.g., a Motion
to Compel and a Motion for Protective Order arising from the
same discovery dispute), the Notice may list both. Format:

```
NOTICE OF HEARING ON DEFENDANT'S MOTION TO COMPEL UNDER
ORCP 46 A AND PLAINTIFF'S CROSS-MOTION FOR PROTECTIVE ORDER
UNDER ORCP 36 C
```

## Stricken or continued hearings

If a previously noticed hearing is stricken or continued, file
an amended Notice. Reference the prior Notice and explain the
change:

```
NOTICE OF HEARING (AMENDED) ON DEFENDANT'S MOTION TO COMPEL

[Notice 1 of [date] is hereby AMENDED. The hearing
previously set for [old date] at [old time] is RESET as
follows:]
```

The same caption / signature / Certificate of Service apply.

## Pro se notes

- A pro se filer must use the same Notice format as counseled
  parties
- The OSB# field is omitted on the signature block (pro se
  filers don't have an OSB#)
- Email is acceptable for the contact email; use a stable
  email account that won't change during the litigation

## Companion documents

A complete motion packet includes:

1. Motion + Memorandum
2. Supporting Declaration with exhibits
3. Proposed Order ("[PROPOSED]" in title)
4. **Notice of Hearing** (this skill)
5. Certificate of Service

The Notice is the LAST document filed in time-sequence (after
the JA has confirmed the date), unless the local SLR requires
simultaneous filing.

## Quality checks

Before filing the Notice:

- **`or-fact-check`** — verify the hearing date, time,
  mode, courtroom, and connection info match the JA's
  confirmation
- **`or-quality-check`** — UTCR 2.010 format pass

A Notice with the wrong date or wrong WebEx link is the most
common pro se filing error and the most likely reason a
hearing falls off the calendar.

## Cross-references

- `or-statewide-format/references/templates/notice-of-hearing.md`
  — full template
- `or-schedule-hearing` — the email or call to reserve the
  date (precedes the Notice)
- `or-multcc/references/civil-motion-scheduling.md` —
  Multnomah-specific
- `or-wccc/references/civil-motion-practice.md` —
  Washington Co-specific
- `or-county-courts` — other counties
