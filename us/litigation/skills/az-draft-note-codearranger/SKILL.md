---
name: az-draft-note-codearranger
title: Draft an Arizona Notice of Hearing
description: 'This skill should be used to scaffold an Arizona Notice of Hearing — the document that asks the court to place a motion on its calendar for oral argument — and the related party-filed notices in Arizona civil practice. Triggers include "Arizona notice of hearing", "request oral argument Arizona Rule 7.1", "set a motion for hearing Arizona", "notice a hearing Arizona", "draft a notice of hearing for my motion", "ask for oral argument on my Arizona motion". In Arizona the request for oral argument is governed by Ariz. R. Civ. P. 7.1: a party may request oral argument, but the court decides whether to hold it or rule on the briefs, and in many Superior Courts the court — not the party — sets the hearing date after a request. Composes with `az-statewide-format` for the caption, `az-schedule-hearing` for obtaining or coordinating the date, and `az-draft-motion` for the underlying motion.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Arizona Notice of Hearing

> **NOT LEGAL ADVICE.** This skill scaffolds a notice document as a
> drafting aid. Verify the filing court's local rules and the assigned
> judge's practice — especially how a hearing date is obtained, whether
> oral argument will be granted at all, and the certificate-of-service
> requirements — against current law before filing.

In Arizona civil practice, a motion is decided on the briefs unless the
court holds **oral argument**. The mechanism for asking the court to hear
a motion is a **request for oral argument** under Ariz. R. Civ. P. 7.1,
and the party-filed scheduling document is typically a **Notice of
Hearing** once a date exists. Arizona terminology and mechanics differ
from a "Note for Motion Docket" or a freestanding "Notice of Motion" —
the request and the noticing of a date travel with the motion and the
court's order.

## Ariz. R. Civ. P. 7.1 — requesting oral argument

Under **Ariz. R. Civ. P. 7.1**, a party may **request oral argument** on
a motion, but the **court decides** whether to hear argument or rule on
the written submissions. Two consequences flow from this:

- The request for oral argument is normally made **in the motion or
  response itself** (or in a separate request as the rule allows), not by
  a freestanding self-scheduled notice. Confirm the current text and the
  manner of making the request in **Ariz. R. Civ. P. 7.1** via
  `az-law-references`.
- Because the court controls whether argument is held, a party often
  cannot unilaterally place a motion on the calendar. In many Superior
  Courts the **court sets the date** after a request and issues a Notice
  of Hearing or minute entry; the party's Notice of Hearing then
  memorializes that court-assigned date for service on all parties.

Do **not** hard-code response/reply day counts or any minimum notice
period here. Confirm the briefing schedule and any notice-period figures
in the current text of the rule via `az-law-references`, and compute
dates with `az-deadlines`.

## Who sets the date — venue matters

How a motion hearing date is obtained varies sharply across Arizona
courts and judicial assignments:

- In many **Superior Courts**, the assigned division issues the hearing
  date by minute entry after a Rule 7.1 request — the party does **not**
  self-schedule. A party-filed Notice of Hearing then restates that date
  for service.
- Some divisions and the **limited-jurisdiction courts** run standing
  motion calendars or expect the filer to coordinate a date with the
  division clerk before noticing.
- Appearance method (in person vs. remote/telephonic) is set by the
  court and the assigned judge's practice.

Point to the venue skills before noticing, and use the scheduling skill
for the mechanics:

- **Use `az-schedule-hearing`** for obtaining or coordinating the date
  with the court before the Notice of Hearing is prepared.
- **Check the venue overlay** — `az-maricopa`, `az-pima`,
  `az-superior-courts`, `az-justice-courts` — for the local practice on
  who sets the date and how it is communicated.

## Certificate / proof of service — Rule 5

Service of the motion, the request for oral argument, and any Notice of
Hearing on every other party is governed by **Ariz. R. Civ. P. 5**. The
filing must include a **certificate of service** stating the date,
manner, and recipients. Confirm the current service manners (including
electronic service through the court's e-filing system) in
**Ariz. R. Civ. P. 5** via `az-law-references`.

## Standard Notice of Hearing scaffold

```
                    [Caption — see az-statewide-format]

                       NOTICE OF HEARING

TO ALL PARTIES AND THEIR ATTORNEYS OF RECORD:

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed [date], is set
for [oral argument / hearing] before the Honorable [Judge Name] as
follows:

  Date:       [Date set by the court]
  Time:       [Time]
  Place:      [Division / Judge, courthouse name, street address,
               city, Arizona]
              [OR remote appearance — platform and connection
               details, as directed by the court]

[Where the court sets the date by minute entry, recite: "Pursuant to the
court's [minute entry / order] dated [date] setting oral argument under
Ariz. R. Civ. P. 7.1, ..."]

                                        [Signature block —
                                         see az-statewide-format]

                    CERTIFICATE OF SERVICE
[Date, manner, recipients — per az-statewide-format and Ariz. R. Civ. P. 5]
```

## Other party-filed notices

| Notice | Filer | Purpose | Authority |
|--------|-------|---------|-----------|
| Notice of Hearing | Movant | Memorializes a court-set hearing/argument date | Ariz. R. Civ. P. 7.1 + local practice |
| Request for Oral Argument | Movant / respondent | Asks the court to hear argument on a motion | Ariz. R. Civ. P. 7.1 |
| Notice of Filing | Filer | Cover notice accompanying a filed document or exhibit | local practice |
| Notice of Change of Address | Party / attorney | Updates the service address of record | Ariz. R. Civ. P. 5 |

## Filing checklist

- [ ] Oral argument requested in the motion/response (or as the rule
      allows) under Ariz. R. Civ. P. 7.1
- [ ] Hearing date obtained from / coordinated with the court per its
      procedure (`az-schedule-hearing`); confirm whether the court or the
      party sets it (`az-maricopa` / `az-pima` / `az-superior-courts` /
      `az-justice-courts`)
- [ ] Caption matches the assigned court and county
      (`az-statewide-format`)
- [ ] Title `NOTICE OF HEARING` in ALL CAPS, centered
- [ ] Date, time, place, and appearance method stated
- [ ] Any minimum notice period confirmed via `az-law-references` and
      computed with `az-deadlines`
- [ ] Certificate of service complete (Ariz. R. Civ. P. 5)

## Composition

- For format and caption: `az-statewide-format`
- For obtaining or coordinating the hearing date: `az-schedule-hearing`
- For the underlying motion (and where the Rule 7.1 request is made):
  `az-draft-motion`
- For a proposed order to bring to the hearing: `az-draft-order`
- For any minimum-notice computation and mail/electronic add-ons:
  `az-deadlines`
- For the venue overlay on who sets the date: `az-maricopa`, `az-pima`,
  `az-superior-courts`, `az-justice-courts`
- For the current text of Ariz. R. Civ. P. 7.1 and Rule 5:
  `az-law-references`

## References

- `references/notice-of-hearing-template.md` — annotated template
- `references/rule-7-1-oral-argument.md` — Ariz. R. Civ. P. 7.1
  request-for-oral-argument pointer + Rule 5 service notes
