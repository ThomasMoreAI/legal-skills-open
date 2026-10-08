---
name: id-draft-note-codearranger
title: Draft an Idaho Notice of Hearing
description: This skill should be used to scaffold an Idaho Notice of Hearing — the document that places a motion on the court's calendar for hearing — and the related party-filed notices in Idaho civil practice. In Idaho the scheduling document is the Notice of Hearing under I.R.C.P. 7(b)(3); the moving party serves and files it at least 14 days before the hearing. Triggers include "Idaho notice of hearing", "set a motion for hearing Idaho", "I.R.C.P. 7(b)(3) notice", "notice a hearing Idaho", "draft a notice of hearing for my motion", "14-day notice Idaho motion", "schedule my Idaho motion for hearing". Composes with `id-statewide-format` for the caption, `id-schedule-hearing` for obtaining or coordinating the date, `id-deadlines` for the 14-day count and service add-ons, and `id-draft-motion` for the underlying motion.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Notice Of Hearing Template
  path: references/notice-of-hearing-template.md
- title: Notice Period
  path: references/notice-period.md
---

# Draft an Idaho Notice of Hearing

> **NOT LEGAL ADVICE.** This skill scaffolds a notice document as
> a drafting aid. Verify the filing court's local rules and the
> assigned judge's practice — especially how a hearing date is
> obtained, the notice period, and the certificate-of-service
> requirements — against current law before filing.

In Idaho civil practice, a motion is set for hearing by a **Notice
of Hearing**. The scheduling mechanism is governed by **I.R.C.P.
7(b)(3)**: the moving party files and serves the Notice of Hearing,
and the **notice and motion must be served and filed at least 14
days before the hearing**. Idaho's scheduling document is the
Notice of Hearing — not a "Note for Motion Docket" or a
freestanding "Notice of Motion".

## I.R.C.P. 7(b)(3) — the 14-day notice rule

Under **I.R.C.P. 7(b)(3)**, the moving party serves and files the
**Notice of Hearing** that sets the motion for hearing:

- The **notice and motion must be served and filed at least 14
  days before the hearing**. Confirm the current day count in
  `id-law-references` and compute the actual date with
  `id-deadlines`, which applies **I.R.C.P. 2.2** time computation
  (Rule 6 is reserved) and the **+3 days for service by mail**.
- **Summary judgment is the exception.** A motion for summary
  judgment under **I.R.C.P. 56** runs on a longer track — the
  motion is served at least **28 days** before the hearing and the
  answering brief at least **14 days** before — so the Notice of
  Hearing for a Rule 56 motion must respect that track. Confirm the
  current figures in `id-law-references`.

Do **not** hard-code response/reply day counts here. Confirm the
briefing schedule and any notice-period figures in the current text
of the rule via `id-law-references`, and compute dates with
`id-deadlines`.

## Who sets the date — venue matters

How a motion hearing date is obtained varies across Idaho courts
and judicial assignments. In many courts the filer **contacts the
judge's clerk or the trial-court administrator** to obtain an
available date before preparing the Notice of Hearing; some courts
run standing motion calendars. Whether a matter is heard in the
**Magistrate Division** or the **District Court** also affects the
calendaring channel.

- **Use `id-schedule-hearing`** for obtaining or coordinating the
  date with the court before the Notice of Hearing is prepared.
- **Check the venue overlay** — `id-ada`, `id-bonneville`,
  `id-county-courts`, `id-family-court` — for the local practice on
  who sets the date and how it is communicated.
- Appearance method (in person vs. remote/telephonic) is set by the
  court and the assigned judge's practice.

## Certificate of service — I.R.C.P. 5

Service of the motion and the Notice of Hearing on every other
party is governed by **I.R.C.P. 5**, and a **certificate of
service** is required for papers served after the complaint. The
filing must state the date, manner, and recipients. E-filing
through iCourt (I.R.E.F.S.) constitutes consent to e-service;
confirm the current service manners (including electronic service)
in **I.R.C.P. 5** and the I.R.E.F.S. rules via `id-law-references`.

## Standard Notice of Hearing scaffold

```
                    [Caption — see id-statewide-format]

                       NOTICE OF HEARING

TO ALL PARTIES AND THEIR ATTORNEYS OF RECORD:

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed [date],
will be brought on for hearing before the Honorable [Judge Name]
as follows:

  Date:       [Date — at least 14 days after service/filing per
               I.R.C.P. 7(b)(3); 28 days for a Rule 56 motion]
  Time:       [Time]
  Place:      [Courtroom / Judge, courthouse name, street address,
               city, Idaho]
              [OR remote appearance — platform and connection
               details, as directed by the court]

                                        [Signature block —
                                         see id-statewide-format]

                    CERTIFICATE OF SERVICE
[Date, manner, recipients — per id-statewide-format and I.R.C.P. 5]
```

## Other party-filed notices

| Notice | Filer | Purpose | Authority |
|--------|-------|---------|-----------|
| Notice of Hearing | Movant | Sets a motion for hearing; the scheduling document | I.R.C.P. 7(b)(3) |
| Notice of Filing | Filer | Cover notice accompanying a filed document or exhibit | local practice |
| Notice of Change of Address | Party / attorney | Updates the service address of record | I.R.C.P. 5 |
| Notice of Appearance | Party / attorney | Enters an appearance in the action | I.R.C.P. 5 / local practice |

## Filing checklist

- [ ] Hearing date obtained from / coordinated with the court per its
      procedure (`id-schedule-hearing`)
- [ ] Notice and motion served/filed **at least 14 days** before the
      hearing (Rule 7(b)(3)) — or the 28-day track for a Rule 56
      motion; confirmed via `id-law-references` and computed with
      `id-deadlines`
- [ ] Service add-on (+3 days for mail) accounted for in the count
- [ ] Caption matches the assigned court (District Court / Magistrate
      Division) and county (`id-statewide-format`)
- [ ] Title `NOTICE OF HEARING` in ALL CAPS, centered
- [ ] Date, time, place, and appearance method stated
- [ ] Certificate of service complete (I.R.C.P. 5)
- [ ] Footer carries the document title + "Page X of Y"

## Composition

- For format and caption: `id-statewide-format`
- For obtaining or coordinating the hearing date: `id-schedule-hearing`
- For the underlying motion: `id-draft-motion`
- For a proposed order to bring to the hearing: `id-draft-order`
- For the 14-day / 28-day computation and mail add-ons: `id-deadlines`
- For the venue overlay on who sets the date: `id-ada`,
  `id-bonneville`, `id-county-courts`, `id-family-court`
- For the current text of I.R.C.P. 7(b)(3) and Rule 5:
  `id-law-references`

## References to author

- `references/notice-of-hearing-template.md` — annotated template
- `references/notice-period.md` — I.R.C.P. 7(b)(3) 14-day rule, the
  Rule 56 28-day exception, and the I.R.C.P. 2.2 + mail-add-on
  pointers
