---
name: co-schedule-hearing
title: Reserve a Hearing Date (Colorado)
description: This skill should be used when the user needs to reserve a motion hearing date in a Colorado court. Triggers include "schedule a hearing in Colorado", "reserve a hearing date Colorado", "set a motion for hearing Colorado", "Colorado law-and-motion calendar", "Denver division 12 chambers hearing", "Arapahoe County hearing date". In Colorado civil practice, the court typically issues a Notice of Setting after a motion is fully briefed — parties do not self-schedule. This skill therefore drafts the contact email or call log appropriate to the assigned judge's practice (chambers email, JA scheduling email, division clerk call), and explains the court-driven scheduling rhythm.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing Date (Colorado)

> **NOT LEGAL ADVICE.** This skill helps draft scheduling
> correspondence. Hearing dates are ultimately the court's to
> assign.

In Colorado civil practice, **the court** issues a Notice of Setting
to schedule a hearing on a fully-briefed motion. The parties **do
not self-schedule** the way they do in Washington (Note for Motion
Docket) or some other states. This skill handles the situations where
the parties **do** need to engage chambers about scheduling.

## When the parties initiate scheduling

| Situation | Action |
|---|---|
| Motion is fully briefed and you want the court to set a hearing | Email chambers / JA requesting setting |
| Hearing already set; need to **continue** | File a Motion to Continue (C.R.C.P. 121 § 1-11) with proposed dates |
| Multi-day evidentiary hearing needed (Rule 56 oral argument, contempt) | Joint motion with proposed dates and estimated length |
| Trial date setting (after at-issue) | Per the CMO entered after the C.R.C.P. 16(b) conference |
| Default judgment hearing (C.R.C.P. 55(b)(2)) | Motion for entry of default judgment with proposed hearing time |
| Emergency hearing (TRO, ex parte) | C.R.C.P. 65 motion for TRO; contact chambers immediately |

## Contact channels

Different JDs use different channels for chambers contact:

| JD | Channel | Notes |
|---|---|---|
| 2nd (Denver) | Email to division clerk; some chambers use a "judicial assistant" alias | Address listed on the judge's practice standards |
| 18th (Arapahoe / Douglas / Elbert / Lincoln) | JA email per division | Listed on https://www.coloradojudicial.gov/courts/judicial-districts/18th-judicial-district |
| 4th (El Paso / Teller) | Email or call division clerk | Listed on the 4th JD page |
| Smaller JDs | Phone call to clerk; some allow email | Verify with clerk |

**Agent behavior**: when drafting a scheduling email, fetch the
assigned judge's current practice standards or the JD's chambers
roster. **Do not cache or guess email addresses** — they change at
judicial rotation.

## Standard scheduling email template

```
To:      [Chambers / JA email address per judge's practice standards]
CC:      [Opposing counsel — usually required, see below]
Subject: Setting Request — [Motion title and date filed], Case
         No. [Case Number]

Dear [Division ## Judicial Assistant / Chambers / Clerk]:

I am [counsel for / pro se / self-represented] [party name] in the
above-captioned matter assigned to the Honorable [Judge Name],
Division ##.

[Movant party] filed [Motion Title] on [date]. The Response was
filed on [date] [or due to be filed on date], and the Reply was
filed on [date] [or due to be filed on date]. Briefing is now
[complete / will be complete on (date)].

I respectfully request that the Court set this matter for hearing
in accordance with the Judge's practice standards. I estimate the
hearing will require [length] minutes. I have conferred with
opposing [counsel / party], and [we are jointly available on the
following dates and times / opposing counsel has identified the
following dates as unavailable: ...].

Joint availability (or my available dates, if I have not yet
received opposing counsel's response):
  - [Date 1] [Time]
  - [Date 2] [Time]
  - [Date 3] [Time]

Thank you for your assistance.

Respectfully,
[Name]
[Reg. No. if attorney / "Self-Represented" if pro se]
[Phone]
[Email]
```

**Always CC opposing counsel** on chambers scheduling emails —
ex-parte contact with the court on substantive matters is prohibited
under Colo. R. Prof. Conduct 3.5(b). Scheduling discussions are
borderline but the safe practice is to include opposing counsel /
party.

## Joint Motion to Continue template (when already scheduled)

When a set hearing needs to be moved:

```
                [Caption]

        JOINT MOTION TO CONTINUE HEARING
            (UNDER C.R.C.P. 121 § 1-11)

The parties, by and through [counsel], jointly move the Court to
continue the hearing currently set for [date] at [time] on
Defendant's Motion to [Title], and in support state:

1. The hearing is currently set for [date and time] in Division ##.

2. [Reason for continuance — counsel conflict, witness availability,
   newly developed need for additional briefing, family-law
   mediation pending, etc.].

3. The parties have conferred and jointly request that the hearing
   be reset to one of the following dates (in order of preference):
     a. [Date 1] [Time]
     b. [Date 2] [Time]
     c. [Date 3] [Time]

4. No party will be prejudiced by this continuance.

WHEREFORE, the parties jointly request that the Court vacate the
hearing currently set for [date] and reset the hearing to a mutually
available date.

[Signature blocks for both parties' counsel / both pro se parties]
```

## Hearing-length estimation guidance

| Motion type | Typical length |
|---|---|
| C.R.C.P. 12(b)(5) Motion to Dismiss | 30-60 min |
| C.R.C.P. 56 Motion for Summary Judgment | 60-90 min |
| Motion to Compel | 30 min |
| Discovery sanctions (Rule 37(b)) | 30-60 min |
| Default judgment (C.R.C.P. 55(b)(2)) | 15-30 min |
| Set-aside default (C.R.C.P. 60(b)) | 30-60 min |
| TRO (Rule 65) | 30-60 min |
| Preliminary injunction | 90-180 min (often evidentiary) |
| Contempt | Variable; can run hours |
| Decree of dissolution (uncontested) | 5-15 min |
| Permanent orders hearing (contested family) | Full day |

## Composition

- For drafting the underlying motion: `co-draft-motion`
- For the notice that goes out after the court sets the hearing:
  `co-draft-note`
- For hearing-day prep and protocol: `co-hearings`
- For court-specific scheduling channels: `co-denver`,
  `co-arapahoe`, `co-county-courts`
- For deadlines and timing: `co-deadlines`

## References

- `references/scheduling-email-template.md`
- `references/joint-motion-to-continue-template.md`
- `references/chambers-contacts.md` — JD-by-JD scheduling contact
  channels
- `references/judge-practice-standards-index.md`
