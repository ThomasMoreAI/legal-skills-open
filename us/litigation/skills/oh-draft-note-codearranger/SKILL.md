---
name: oh-draft-note-codearranger
title: Draft an Ohio Notice of Hearing
description: Use to draft an Ohio Notice of Hearing. Triggers include 'Ohio notice of hearing', 'Ohio Civ. R. 7 notice', 'Ohio Civ. R. 56(C) summary judgment notice', 'Ohio motion hearing notice'. **Skill name is 'note' for filename consistency across the marketplace; the output is an Ohio 'Notice of Hearing'.**
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Ohio Notice of Hearing

> **NOT LEGAL ADVICE.** Ohio uses "Notice of Hearing" — not
> NY's "Notice of Motion" or WA's "Note for Motion Docket."

## When you need a Notice of Hearing

After filing a motion, most Ohio Common Pleas courts
require the movant to **schedule the hearing with chambers
or the assigned magistrate** and then file a Notice of
Hearing. Procedure varies by court:

- **Cuyahoga County** — court issues the hearing notice via
  case-management order; movant rarely files a separate
  notice
- **Franklin County** — movant calls chambers, gets a
  date, and files Notice of Hearing
- **Hamilton County** — court schedules ex parte; movant
  files a request via the court's website
- **Summit County** — varies by department

Always verify per-court Loc. R. and chambers practice.

## Standard Notice of Hearing form

```
IN THE COURT OF COMMON PLEAS OF [COUNTY], OHIO

[Plaintiff Name],                Case No. [CV-NNNNN]
                                  Judge: [Name]
        vs.
                                  NOTICE OF HEARING
[Defendant Name],

PLEASE TAKE NOTICE that [Movant's] Motion to [Relief]
will be heard before [Judge / Magistrate Name] on
[Day, Date], at [Time], in Courtroom [Number].

                                  Respectfully submitted,

                                  __________________________
                                  [Counsel / Pro Se name]
                                  [Address / Phone / Email]
                                  [Atty. Reg. # if counsel]

CERTIFICATE OF SERVICE
[Service text]
```

## Service requirements

- File the Notice with the court
- Serve copy on every party in the case (Civ. R. 5)
- File certificate of service

## Summary-judgment-specific notice

Civ. R. 56(C) requires **14 days' advance notice** of the
hearing on a motion for summary judgment. The notice
period runs from service of the motion + notice to the
hearing date. Civ. R. 6(D) adds 3 days for mail service.

## Order to Show Cause variant

Where the movant needs **expedited relief** (e.g.,
emergency protective order, TRO), Civ. R. 65 allows an
Order to Show Cause / Notice of Hearing combined. The
court signs the order; movant serves it; the responding
party must appear to show cause why the relief should not
be granted.

## Composition with other oh- skills

- `oh-schedule-hearing` — chambers scheduling protocols
- `oh-draft-motion` — the underlying motion
- `oh-deadlines` — 14-day Civ. R. 56(C) notice math
- `oh-statewide-format` — caption + signature
