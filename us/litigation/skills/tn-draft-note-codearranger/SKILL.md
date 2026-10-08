---
name: tn-draft-note-codearranger
title: Draft a Tennessee Notice of Hearing
description: This skill should be used to scaffold a Tennessee Notice of Hearing — the document that places a motion on the court's calendar — and the related party-filed notices in Tennessee civil practice. Triggers include "draft a Tennessee notice of hearing", "set my motion for hearing in Tennessee", "Notice of Hearing for a Chancery motion", "draft a notice to set a motion on the docket", "draft a notice of filing Tennessee", "notice of voluntary dismissal Tennessee", "notice of change of address". The scheduling document in Tennessee is a Notice of Hearing (NOT a Note for Motion Docket or Notice of Motion). Note that many Circuit and Chancery courts require the filer to obtain or coordinate a hearing date with the judge's office or docket clerk before noticing the motion — this varies by county. Composes with `tn-statewide-format` for the caption, `tn-schedule-hearing` for obtaining the date, and `tn-draft-motion` for the underlying motion.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Tennessee Notice of Hearing

> **NOT LEGAL ADVICE.** This skill scaffolds a notice document. Verify
> the filing court's local rules and the assigned judge's standing
> orders — especially how hearing dates are obtained — before filing.

In Tennessee civil practice the scheduling document that places a
motion on the court's calendar is the **Notice of Hearing**. It tells
all parties when and where the court will hear a previously filed
motion. The Notice of Hearing serves the motion's hearing date under
**Tenn. R. Civ. P. 5** and is filed in the underlying Circuit or
Chancery case.

> **General Sessions is different.** General Sessions practice is
> informal and the Tennessee Rules of Civil Procedure generally do not
> apply there. A General Sessions matter is set by a return date / court
> date assigned when the civil warrant issues, not by a party-filed
> Notice of Hearing. See `tn-general-sessions`.

## Coordinate the date first — this varies by county

Many Tennessee Circuit and Chancery courts require the filer to
**obtain or coordinate a hearing date** from the judge's office, the
docket clerk, or the Clerk & Master (in Chancery) **before** serving a
Notice of Hearing — you cannot simply pick a date and notice it. Other
courts run a standing motion docket on set days where motions are heard
without an individually assigned time. Practice differs by county and
by judge.

- **Check the local rules** of the filing court (indexed on the AOC
  "Local Rules of Practice" page at tncourts.gov) and the assigned
  judge's standing orders.
- **Use `tn-schedule-hearing`** for the mechanics of contacting the
  judge's office / docket clerk to secure a date.
- Confirm any **minimum-notice** requirement — for a summary-judgment
  motion under Tenn. R. Civ. P. 56.04, the motion must be served **at
  least 30 days before the hearing**; other motions may carry a
  shorter local-rule notice period. Use `tn-deadlines` to compute the
  date and any Rule 6.05 mail add-on.

## Standard Notice of Hearing scaffold

```
                    [Caption — see tn-statewide-format]

                       NOTICE OF HEARING

TO ALL PARTIES AND THEIR COUNSEL OF RECORD:

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed [date], will
be brought on for hearing before the Honorable [Judge / Chancellor
Name] as follows:

  Date:       [Date]
  Time:       [Time]
  Place:      [Courtroom / Part, courthouse name, street address,
               city, Tennessee]
              [OR remote appearance — platform and connection
               details, if permitted by the court]
  Division:   [Circuit / Chancery Part or Division number]

This matter has been [set / assigned a hearing date] by [the Court /
the judge's office / the docket clerk] in accordance with the local
rules of [County] County. Counsel and self-represented parties should
confirm the appearance method (in person / remote) with the court
before the hearing date.

                                        [Signature block —
                                         see tn-statewide-format]

                       CERTIFICATE OF SERVICE
[Date, method, recipients — per tn-statewide-format and Rule 5]
```

## Other party-filed notices

| Notice | Filer | Purpose | Authority |
|--------|-------|---------|-----------|
| Notice of Hearing | Movant | Sets a filed motion for hearing | Tenn. R. Civ. P. 5 + local rules |
| Notice of Filing | Filer | Cover notice accompanying a filed document or exhibit | local practice |
| Notice of Voluntary Dismissal | Plaintiff | Voluntary dismissal under Tenn. R. Civ. P. 41.01 | Tenn. R. Civ. P. 41.01 |
| Notice of Appeal (Sessions → Circuit) | Appealing party | Triggers de novo appeal within 10 days | Tenn. Code Ann. § 27-5-108 |
| Notice of Change of Address | Party / counsel | Updates the service address of record | Tenn. R. Civ. P. 5 |

### Notice of Voluntary Dismissal — Tenn. R. Civ. P. 41.01

A plaintiff generally may take a **voluntary nonsuit** (dismissal
without prejudice) by filing a written notice of dismissal, subject to
the limits in Rule 41.01 (e.g., once a motion for summary judgment is
pending, or where a counterclaim has been pleaded that cannot remain
pending for independent adjudication). A **second** voluntary dismissal
of a claim based on or including the same claim may operate as an
adjudication on the merits. Verify the current rule text and track any
prior dismissals before filing.

```
                [Caption — see tn-statewide-format]

              NOTICE OF VOLUNTARY DISMISSAL
                 (TENN. R. CIV. P. 41.01)

PLEASE TAKE NOTICE that Plaintiff hereby voluntarily dismisses this
action [without prejudice], pursuant to Tenn. R. Civ. P. 41.01.

                                        [Plaintiff signature block]
```

### General Sessions de novo appeal notice

To appeal a General Sessions judgment to Circuit Court for trial **de
novo**, the appealing party must perfect the appeal within **10 days**
of entry of the judgment under Tenn. Code Ann. § 27-5-108 (uniform
statewide 10-day period; perfecting also involves the appeal
bond/cost requirements with the Sessions clerk — confirm the clerk's
exact procedure). See `tn-post-judgment` and `tn-general-sessions`.

## Filing checklist

- [ ] Hearing date obtained / coordinated per the court's procedure
      (`tn-schedule-hearing`)
- [ ] Caption matches the assigned court (Circuit / Chancery) and
      county (`tn-statewide-format`)
- [ ] Title `NOTICE OF HEARING` in ALL CAPS, centered
- [ ] Date, time, place, division, and appearance method stated
- [ ] Minimum-notice / 30-day Rule 56.04 requirement satisfied
      (`tn-deadlines`)
- [ ] Certificate of Service complete (Rule 5)

## Composition

- For format and caption: `tn-statewide-format`
- For obtaining the hearing date: `tn-schedule-hearing`
- For the underlying motion: `tn-draft-motion`
- For the proposed order to bring to the hearing: `tn-draft-order`
- For deadline math (30-day Rule 56.04, Rule 6.05 mail add-on):
  `tn-deadlines`
- For the General Sessions forum: `tn-general-sessions`
- For the venue overlay: `tn-davidson`, `tn-shelby`, `tn-knox`,
  `tn-hamilton`, `tn-county-courts`

## References

- `references/notice-of-hearing-template.md` — annotated template
- `references/notice-of-dismissal-template.md` — Rule 41.01 nonsuit
- `references/coordinating-hearing-dates.md` — county-by-county
  date-setting practice notes
