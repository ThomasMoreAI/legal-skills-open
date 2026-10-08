---
name: mi-draft-note-codearranger
title: Draft a Michigan Notice of Hearing
description: This skill should be used to scaffold a Michigan Notice of Hearing — the document that places a motion on the court's calendar — and the related party-filed notices in Michigan civil practice. Triggers include "Michigan notice of hearing", "notice a motion for hearing Michigan", "MCR 2.119(C) notice", "schedule motion hearing notice", "draft a notice of hearing for my motion", "set my motion for hearing in Michigan". The scheduling document in Michigan is a Notice of Hearing (NOT a "Note for Motion Docket" or a "Notice of Motion"). Under MCR 2.119(C) a written motion and a notice of the time and place of hearing must be served, and the proof of service follows MCR 2.107. Composes with `mi-statewide-format` for the caption, `mi-schedule-hearing` for obtaining the hearing date, and `mi-draft-motion` for the underlying motion.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Michigan Notice of Hearing

> **NOT LEGAL ADVICE.** This skill scaffolds a notice document as a
> drafting aid. Verify the filing court's local rules and the assigned
> judge's practice — especially how hearing dates are obtained and the
> minimum notice period — against current law before filing.

In Michigan civil practice the document that places a motion on the
court's calendar is the **Notice of Hearing**. It tells all parties
when and where the court will hear a previously filed motion. Michigan
does **not** use a "Note for Motion Docket" or a freestanding "Notice
of Motion" — the motion and the notice of hearing travel together.

## MCR 2.119(C) — the motion-and-notice requirement

Under **MCR 2.119(C)**, a written motion (other than one that may be
heard ex parte), the notice of the time and place of the hearing, and
any supporting brief or affidavits must be **served** on the other
parties. The rule sets a **minimum notice period** before the hearing,
with a longer period when service is by mail.

- Do **not** hard-code the day count here. Confirm the exact minimum
  notice period (and the mail add-on) in the current text of MCR
  2.119(C) via `mi-law-references`, and compute the date with
  `mi-deadlines`.
- The notice period runs **backward** from the hearing date: the
  motion + notice must be served at least the rule's minimum number of
  days before the hearing. Building in the mail-service add-on and any
  longer local-rule period is the filer's responsibility.
- Some motions may be **heard ex parte** or decided **without oral
  argument** under MCR 2.119(E) (the court may dispense with oral
  argument). Confirm whether the motion at hand requires a noticed
  hearing at all before scheduling one.

## Get the hearing date first

Michigan trial courts vary in how a motion hearing date is obtained.
Many circuit and district courts require the filer to **secure a
motion date** from the assigned judge's clerk or the court's motion
calendar before the Notice of Hearing can state a date; some run a
standing motion day. Practice differs by court and by judge.

- **Use `mi-schedule-hearing`** for the mechanics of obtaining or
  coordinating the date with the court before noticing the motion.
- **Check the local rules** of the filing court and the assigned
  judge's practice guidelines.
- Confirm the appearance method (in person vs. remote) — many Michigan
  courts hold motion hearings by videoconference under MCR 2.407 and
  the Michigan Trial Court Standards for the use of video technology.

## Proof of service — MCR 2.107

Service of the motion and Notice of Hearing on every other party is
governed by **MCR 2.107** (manner of service; service on the attorney
of record where a party is represented). The filing must include a
**proof of service** stating the date, manner, and recipients. The
notice period under MCR 2.119(C) is measured from the date of service,
so the proof-of-service date is what fixes whether the minimum notice
was satisfied.

## Standard Notice of Hearing scaffold

```
                    [Caption — see mi-statewide-format]

                       NOTICE OF HEARING

TO ALL PARTIES AND THEIR ATTORNEYS OF RECORD:

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed [date], will
be brought on for hearing before the Honorable [Judge Name] as
follows:

  Date:       [Date]
  Time:       [Time]
  Place:      [Courtroom / Judge, courthouse name, street address,
               city, Michigan]
              [OR remote appearance — platform and connection
               details, if the court hears motions by video under
               MCR 2.407]

The motion and this notice are served on all parties pursuant to
MCR 2.119(C) and MCR 2.107.

                                        [Signature block —
                                         see mi-statewide-format]

                       PROOF OF SERVICE
[Date, manner, recipients — per mi-statewide-format and MCR 2.107]
```

## Other party-filed notices

| Notice | Filer | Purpose | Authority |
|--------|-------|---------|-----------|
| Notice of Hearing | Movant | Sets a filed motion for hearing | MCR 2.119(C) + local rules |
| Notice of Filing | Filer | Cover notice accompanying a filed document or exhibit | local practice |
| Notice of Dismissal | Plaintiff | Voluntary dismissal | MCR 2.504(A) |
| Notice of Change of Address | Party / attorney | Updates the service address of record | MCR 2.107 |

## Filing checklist

- [ ] Hearing date obtained / coordinated per the court's procedure
      (`mi-schedule-hearing`)
- [ ] Caption matches the assigned court and county
      (`mi-statewide-format`)
- [ ] Title `NOTICE OF HEARING` in ALL CAPS, centered
- [ ] Date, time, place, and appearance method stated
- [ ] MCR 2.119(C) minimum notice period satisfied (with mail add-on
      where applicable) — verified via `mi-law-references` and
      computed with `mi-deadlines`
- [ ] Motion + supporting brief/affidavits served with the notice
      under MCR 2.119(C)
- [ ] Proof of service complete (MCR 2.107)

## Composition

- For format and caption: `mi-statewide-format`
- For obtaining the hearing date: `mi-schedule-hearing`
- For the underlying motion: `mi-draft-motion`
- For the proposed order to bring to the hearing: `mi-draft-order`
- For the minimum-notice computation and any mail add-on:
  `mi-deadlines`
- For the venue overlay: `mi-wayne`, `mi-oakland`, `mi-36th-district`,
  `mi-circuit-courts`, `mi-district-courts`
- For the current text of MCR 2.119 and MCR 2.107:
  `mi-law-references`

## References

- `references/notice-of-hearing-template.md` — annotated template
- `references/mcr-2119C-notice-period.md` — MCR 2.119(C) notice-period
  pointer + MCR 2.107 service notes
