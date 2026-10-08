---
name: tx-draft-note-codearranger
title: Draft a Texas Notice of Hearing
description: This skill should be used to scaffold a Texas Notice of Hearing — the document that sets a motion for an oral hearing or for submission and places it on the court's calendar. In Texas civil practice the scheduling document is the Notice of Hearing; the setting is obtained from the court coordinator (district and county courts) or the precinct clerk (justice courts), and the motion and notice are served on all parties under Tex. R. Civ. P. 21/21a. Triggers include "Texas notice of hearing", "set my motion for hearing Texas", "set my motion on submission Texas", "notice of submission Texas", "draft a notice of hearing for my motion", "TRCP 21 notice of hearing", "submission docket Texas", "get my Texas motion heard". Composes with `tx-statewide-format` for the caption, `tx-schedule-hearing` for obtaining the setting from the court coordinator, `tx-deadlines` for the notice count and service add-ons, and `tx-draft-motion` for the underlying motion.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Texas Notice of Hearing

> **NOT LEGAL ADVICE.** This skill scaffolds a notice document as a
> drafting aid. Verify the filing court's local rules and the
> assigned judge's practice — especially how a setting is obtained,
> the notice period, submission-vs-oral-hearing practice, and the
> certificate-of-service requirements — against current law before
> filing.

In Texas civil practice, a motion is placed on the court's calendar
by a **Notice of Hearing**. This is the document that **sets a
motion for hearing or for submission**. The filing and service of
the motion and its notice are governed by **Tex. R. Civ. P. 21** and
**21a**; the moving party files the notice with the clerk and serves
it on all parties.

## Submission vs. oral hearing — pick the setting

A Texas trial court may dispose of a motion in either of two ways,
and the **court's local rules and the assigned judge's practice
control**:

- **By submission** — the court rules on the papers, without oral
  argument. The Notice of Hearing states a **submission date**: the
  date by which responses are due and on or after which the court may
  rule. Most routine, non-evidentiary motions go on the **submission
  docket**.
- **By oral hearing** — the motion is set for argument on a date and
  time, in a courtroom or by remote appearance. Dispositive and
  evidentiary motions are commonly set this way.

Confirm which mode the assigned court uses for the motion type before
preparing the notice; some courts default everything to submission
unless oral argument is requested.

## Tex. R. Civ. P. 21(b) — the notice period

Under **Tex. R. Civ. P. 21(b)**, unless otherwise provided by these
rules or shortened by the court, a motion and notice of the hearing
on it must be **served at least three days before the time specified
for the hearing**. This is a **floor**, not a complete schedule:

- **Summary judgment is the exception.** A motion for summary
  judgment under **Tex. R. Civ. P. 166a** runs on a longer track —
  the motion and any supporting affidavits are served **at least 21
  days before** the hearing or submission date, and the response is
  due **7 days before** — so the Notice of Hearing for a Rule 166a
  motion must respect that 21-day track.
- Service by mail, commercial delivery, fax, or email adds **+3
  days** to a period that runs from service under **Tex. R. Civ. P.
  21a** — account for it when backing the setting out from the floor.

Do **not** hard-code response/reply day counts here. Confirm the
current notice-period and service-add-on figures in
`tx-law-references` and compute the actual dates with `tx-deadlines`.

## Who sets the setting — venue matters

How a setting is obtained varies by court level:

- **District Courts and County Courts at Law** — the filer typically
  contacts the **court coordinator** (the judge's calendar staff) to
  reserve an oral-hearing date or to confirm the submission-docket
  procedure, then prepares the Notice of Hearing reflecting that
  setting. Some courts have an online or standing submission docket.
- **Justice Courts (JP courts)** — setting is handled through the
  **precinct clerk / Justice of the Peace's office**; justice-court
  procedure is simplified and the regular notice mechanics may differ.

Use `tx-schedule-hearing` to obtain or coordinate the setting before
the Notice of Hearing is prepared, and check the venue overlay
(`tx-hcdc`, `tx-dcdc`, `tx-county-courts`, `tx-family-court`) for the
local practice on who sets the date and how it is communicated.

## Certificate of service — Tex. R. Civ. P. 21a

Service of the motion and the Notice of Hearing on every other party
is governed by **Tex. R. Civ. P. 21a**, and a **certificate of
service** is required. The certificate must state the date and manner
of service and the recipients. For those who e-file, e-service
through eFileTexas is the default method; confirm the current service
manners in `tx-law-references` and see `tx-file-packet`.

## Standard Notice of Hearing scaffold

```
                    [Caption — see tx-statewide-format]

                       NOTICE OF HEARING
              [or: NOTICE OF SUBMISSION]

TO ALL PARTIES AND THEIR ATTORNEYS OF RECORD:

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed [date],
will be [heard / submitted to the Court for ruling] as follows:

  Date:       [Date — respecting the Rule 21(b) notice floor; 21
               days for a Rule 166a motion]
  Time:       [Time, if an oral hearing]
  Place:      [Courtroom / Judge, courthouse name, street address,
               city, Texas]
              [OR: submitted on the Court's submission docket
               without oral argument]
              [OR remote appearance — platform and connection
               details, as directed by the court]

Responses are due [per Rule 21(b) / Rule 166a / local rule].

                                        [Signature block —
                                         see tx-statewide-format]

                    CERTIFICATE OF SERVICE
[Date, manner, recipients — per tx-statewide-format and
Tex. R. Civ. P. 21a]
```

## Other party-filed notices

| Notice | Filer | Purpose | Authority |
|--------|-------|---------|-----------|
| Notice of Hearing / Notice of Submission | Movant | Sets a motion for oral hearing or submission | Tex. R. Civ. P. 21 |
| Notice of Filing | Filer | Cover notice accompanying a filed document or exhibit | local practice |
| Notice of Change of Address | Party / attorney | Updates the service address of record | Tex. R. Civ. P. 21a |
| Notice of Appearance | Party / attorney | Enters an appearance in the action | local practice |

## Filing checklist

- [ ] Setting obtained from / coordinated with the court coordinator
      (district/county) or precinct clerk (JP) (`tx-schedule-hearing`)
- [ ] Submission vs. oral hearing chosen per the court's local rules
- [ ] Notice and motion served respecting the Rule 21(b) notice floor —
      or the 21-day track for a Rule 166a motion; confirmed via
      `tx-law-references` and computed with `tx-deadlines`
- [ ] Service add-on (+3 days for mail/email/fax) accounted for
- [ ] Caption matches the assigned court and county (`tx-statewide-format`)
- [ ] Title `NOTICE OF HEARING` (or `NOTICE OF SUBMISSION`) in ALL
      CAPS, centered
- [ ] Date, time (if oral), place, and appearance method stated;
      response-due statement included
- [ ] Certificate of service complete (Tex. R. Civ. P. 21a)
- [ ] Footer carries the document title + "Page X of Y"

## Composition

- For format and caption: `tx-statewide-format`
- For obtaining or coordinating the setting: `tx-schedule-hearing`
- For the underlying motion: `tx-draft-motion`
- For a proposed order to bring to the hearing: `tx-draft-order`
- For the notice count and mail add-on computation: `tx-deadlines`
- For the venue overlay on who sets the date: `tx-hcdc`, `tx-dcdc`,
  `tx-county-courts`, `tx-family-court`
- For the current text of Tex. R. Civ. P. 21 / 21a and Rule 166a:
  `tx-law-references`

## References to author

- `references/notice-of-hearing-template.md` — annotated template
  (oral-hearing and submission variants)
- `references/notice-period.md` — Tex. R. Civ. P. 21(b) notice floor,
  the Rule 166a 21-day track, and the Rule 21a mail-add-on pointers
