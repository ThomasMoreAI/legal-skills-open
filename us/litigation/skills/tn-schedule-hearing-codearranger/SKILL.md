---
name: tn-schedule-hearing-codearranger
title: Reserve a Hearing Date (Tennessee)
description: 'This skill should be used when the user needs to reserve a motion hearing date in a Tennessee court. Triggers include "schedule a hearing in Tennessee", "reserve a hearing date Tennessee", "set my motion for hearing in Tennessee", "Tennessee motion docket", "get a hearing date from the judge''s secretary", "Davidson Chancery hearing date", "Shelby Circuit motion setting", "Knox Chancery docket", "Hamilton County hearing date", "General Sessions return date", "do I file the Notice of Hearing before or after getting a date". In Tennessee civil practice, scheduling varies by county: many Circuit and Chancery courts require coordinating a date with the judge''s secretary / docket clerk before filing a Notice of Hearing, while General Sessions runs a periodic civil docket / return date. This skill drafts the contact email or call log and the Notice of Hearing, and gives per-flagship-county routing notes.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing Date (Tennessee)

> **NOT LEGAL ADVICE.** This skill helps draft scheduling
> correspondence and the Notice of Hearing. Hearing dates are
> ultimately the court's to assign, and the procedure varies by
> county — verify the filing court's local rules and the assigned
> judge's practices.

In Tennessee civil practice, **how a hearing gets set varies by
county and by individual judge.** There is no single statewide motion
calendar. Two broad patterns:

1. **Coordinate-then-notice.** In many Circuit and Chancery courts,
   the movant first **clears a date with the judge's secretary or the
   docket clerk** (by phone or email), then files and serves a
   **Notice of Hearing** stating that date. The court does not issue
   the setting; the parties do, after coordinating.
2. **General Sessions civil docket / return date.** General Sessions
   runs a periodic civil docket. The summons / civil warrant carries
   a **return date** — the date the matter first appears on the
   docket — rather than a separately-noticed motion hearing. Practice
   is informal and the formal civil rules generally do not apply.

Always confirm the venue's actual mechanism; some courts post motion
calendars, some require an agreed order setting the hearing, and some
self-set through a clerk's online system.

## When the parties initiate scheduling

| Situation | Action |
|---|---|
| Motion ready; need a hearing date in Circuit / Chancery | Call or email the judge's secretary / docket clerk to clear a date, then file and serve a Notice of Hearing |
| Rule 56 summary-judgment motion | Set the hearing **at least 30 days** after service of the motion (Tenn. R. Civ. P. 56.04); adverse party responds no later than 5 days before |
| Hearing already set; need to **continue** | File a Motion to Continue with proposed dates, or submit an agreed order resetting |
| Multi-hour evidentiary hearing | Coordinate the estimated length with chambers before noticing |
| General Sessions civil matter | The return date on the civil warrant governs; appear or seek a reset at the clerk's window |
| Emergency / ex parte relief | Contact chambers / the clerk immediately; follow the court's TRO procedure |

## Contact channels

Channels differ by county and by individual judge. **Do not cache or
guess email addresses or phone numbers** — they change at judicial
rotation. Fetch the current chambers / clerk contact from the court's
website or the AOC "Local Rules of Practice" page at tncourts.gov.

### Per-flagship-county routing notes

These are starting points only — each court's **local rules** and the
assigned judge's individual practices control. Verify before relying.

| County / District | Notes |
|---|---|
| **Davidson (Nashville), 20th JD** | Metro consolidated city-county government. Separate Circuit, Chancery (Chancery Court Clerk & Master), General Sessions, and Juvenile clerks. Chancery commonly coordinates motion dates through the Clerk & Master / chambers; confirm the part and the judge's practice. |
| **Shelby (Memphis), 30th JD** | Circuit and Chancery each run their own dockets; coordinate through the assigned division's clerk / secretary. (Shelby uses eFlex for e-filing; the Notice of Hearing is typically filed there once the date is cleared.) |
| **Knox (Knoxville), 6th JD** | Circuit, Chancery, and General Sessions divisions; coordinate motion dates per the assigned judge's docket practice and the local rules. |
| **Hamilton (Chattanooga), 11th JD** | Circuit, Chancery, and General Sessions; coordinate per the division clerk / chambers and the local rules. |
| **Other counties** | See `tn-county-courts`. Practice ranges from clerk-set dockets to chambers coordination. Always check the county's local rules. |

## Standard scheduling email / call-log template

```
To:      [Judge's secretary / docket clerk per the court's current roster]
CC:      [Opposing counsel / party — include them; see below]
Subject: Hearing-Date Request — [Motion title and date filed],
         Docket No. [Number], [County] [Circuit/Chancery] Court

Dear [Judge ___'s Secretary / [County] [Court] Docket Clerk]:

I am [counsel for / pro se / self-represented] [party name] in the
above-captioned matter, [Docket No. ____], assigned to [Judge Name /
Division ___].

[Movant] has filed (or is prepared to file) [Motion Title]. I
respectfully request a hearing date in accordance with the Court's
docket and the Judge's practice. I estimate the hearing will require
[length] minutes.

[For a Rule 56 motion: Because this is a motion for summary judgment,
the hearing must be set at least 30 days after service of the motion
under Tenn. R. Civ. P. 56.04.]

I have conferred with opposing [counsel / party], and [we are jointly
available on the dates below / opposing counsel has noted the
following conflicts: ...]:
  - [Date 1] [Time]
  - [Date 2] [Time]
  - [Date 3] [Time]

Once the Court confirms a date, I will file and serve a Notice of
Hearing.

Thank you for your assistance.

Respectfully,
[Name]
[BPR # if attorney / "Pro Se" if self-represented]
[Phone]
[Email]
```

**Call-log alternative.** If the court schedules by phone, log the
call: date / time of call, person spoken to, date offered, any
conditions, and the date you will state in the Notice of Hearing.

**Include opposing counsel / party.** Coordinate availability before
contacting the court, and avoid ex-parte communication with the court
on anything beyond pure scheduling logistics.

## Notice of Hearing template

Once the date is cleared, file and serve the Notice of Hearing:

```
                [Caption — Tenn. R. Civ. P. 10.01]

                    NOTICE OF HEARING

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed on [date],
will be heard before [the Honorable [Judge Name] / Division ___] of
the [County] [Circuit / Chancery] Court at [courthouse address],
on [date] at [time], or as soon thereafter as counsel may be heard.

[For a Rule 56 motion: This Notice is served at least thirty (30)
days before the hearing in compliance with Tenn. R. Civ. P. 56.04.]

                              Respectfully submitted,
                              [Signature block — Rule 11; BPR # or Pro Se]

                    CERTIFICATE OF SERVICE
[Tenn. R. Civ. P. 5 — date, method, recipients]
```

## Hearing-length estimation guidance

| Motion type | Typical length |
|---|---|
| Tenn. R. Civ. P. 12.02(6) motion to dismiss | 30-60 min |
| Tenn. R. Civ. P. 56 summary judgment | 60-90 min |
| Motion to compel (Rule 37) | 30 min |
| Motion to set aside default | 30-60 min |
| Rule 59 motion to alter or amend | 30-60 min |
| Default-judgment hearing | 15-30 min |
| Temporary restraining order / injunction | 30-180 min (often evidentiary) |
| Uncontested divorce (irreconcilable differences) | 5-15 min |
| Contested family-law hearing | Variable; can run a full day |

(For an irreconcilable-differences divorce, also confirm the waiting
period under Tenn. Code Ann. § 36-4-103(a) — at least 60 days on file
with no minor child, 90 days with a minor child — before requesting
the hearing date. See `tn-family-law`.)

## Composition

- For drafting the underlying motion: `tn-draft-motion`
- For the Notice of Hearing as a standalone document: `tn-draft-note`
- For hearing-day prep and protocol: `tn-hearings`
- For court-specific scheduling channels: `tn-davidson`, `tn-shelby`,
  `tn-knox`, `tn-hamilton`, `tn-county-courts`,
  `tn-general-sessions`
- For deadlines and timing (Rule 6.01 / 6.05; § 15-1-101 holidays):
  `tn-deadlines`
- For family-law hearing timing: `tn-family-law`, `tn-family-court`

## References

- `tn-law-references` for Tenn. R. Civ. P. 56.04 and Rule 5 / 6 text
- The AOC "Local Rules of Practice" index at tncourts.gov for the
  filing court's current scheduling procedure
- Confirm the assigned judge's individual practices and the county's
  local rules before relying on any routing note above.
