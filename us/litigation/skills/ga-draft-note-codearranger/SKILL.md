---
name: ga-draft-note-codearranger
title: Draft a Georgia Notice of Hearing / Rule Nisi
description: This skill should be used to scaffold a Georgia scheduling document — a Notice of Hearing or the Rule Nisi presented for the judge's signature. Triggers include "notice of hearing Georgia", "rule nisi", "draft a rule nisi Georgia", "draft a notice of hearing for my motion", "set my motion for hearing Georgia", "Georgia hearing notice for a motion to compel". Produces the Notice of Hearing / Rule Nisi that identifies the underlying motion, the date, time, and place set by the court, and the certificate of service, and explains how the Notice of Hearing pairs with the Rule Nisi the judge signs under USCR 6.3 / 6.4.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Georgia Notice of Hearing / Rule Nisi

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — chooses the
> motion type, theory of relief, and strategy. Verify every
> rule, deadline, and citation against current law before
> filing. Pair with substantive review by counsel where stakes
> warrant.

Use this skill in addition to `ga-statewide-format` when a motion
requires a hearing date to be placed on the court's calendar. In
Georgia, a party requesting oral argument requests it within the
response period (USCR 6.3); the hearing date is then set by the court.
Two paired documents do the work:

| Document | Who prepares / signs | Purpose | Authority |
|---|---|---|---|
| **Notice of Hearing** | Filer prepares and serves | Notifies all parties of the date, time, and place of a hearing on a pending motion | USCR 6.3 / 6.4 |
| **Rule Nisi** | Filer drafts; **judge signs** | The court's order setting the matter down and directing the parties to appear and show cause | USCR 6.3 / 6.4 |

The filer commonly prepares the **Rule Nisi** in proposed form and
submits it with the motion; the judge signs it, fixing the date. The
**Notice of Hearing** then transmits that date to the parties with a
certificate of service. (When the matter calls for the judge's signed
ruling rather than a scheduling order, see `ga-draft-order`.)

## Standard Notice of Hearing scaffold

```
                [Caption — see ga-statewide-format,
                 per O.C.G.A. § 9-11-10(a)]

                       NOTICE OF HEARING

TO ALL PARTIES AND THEIR COUNSEL OF RECORD:

PLEASE TAKE NOTICE that [Movant]'s [Motion Title], filed [date], is
set for hearing before the above-styled Court as follows:

  Date:       [Date]
  Time:       [Time]
  Place:      [Courtroom number, courthouse name, county, address]
              [OR remote — platform, meeting ID, and password]
  Before:     The Honorable [Judge Name]
  Length:     [Estimated minutes]

Counsel and parties shall appear [in person / by videoconference] as
directed by the Court.

Respectfully submitted, this ___ day of __________, 20__.

                                        _____________________________
                                        [Name]
                                        [Address]
                                        [City, GA ZIP]
                                        [Phone]
                                        [Email]
                                        Pro Se
                                        [OR: Georgia Bar No. ______]

                       CERTIFICATE OF SERVICE
[Date, method, recipients — per O.C.G.A. § 9-11-5 and
ga-statewide-format]
```

## Proposed Rule Nisi scaffold (for the judge's signature)

```
                [Caption — see ga-statewide-format]

                          RULE NISI

The foregoing [Motion Title] having been filed and presented to the
Court, it is hereby ORDERED that the [opposing party] appear before
the undersigned on the ___ day of __________, 20__, at ____ __.m.,
in [Courtroom ___, courthouse name, county, address], to show cause,
if any there be, why the relief requested in the Motion should not be
granted.

SO ORDERED, this ___ day of __________, 20__.

                                        _____________________________
                                        Judge, [Superior / State] Court
                                        of [County] County
```

> The blanks in the Rule Nisi are filled and the order is signed **by
> the judge or chambers**, not by the filer. The filer submits it in
> proposed form.

## Filing checklist

- [ ] Caption matches the assigned court and county
- [ ] Notice of Hearing identifies the motion by title and filing date
- [ ] Date, time, and place fields present (or marked "to be set by the Court")
- [ ] Proposed Rule Nisi attached for the judge's signature
- [ ] Certificate of Service complete (O.C.G.A. § 9-11-5)
- [ ] Oral argument timely requested if required (USCR 6.3)
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format: `ga-statewide-format`
- For the underlying motion: `ga-draft-motion`
- For the judge's substantive ruling: `ga-draft-order`
- For the scheduling protocol: `ga-schedule-hearing`
- For hearing preparation: `ga-hearings`
- For the venue overlay: `ga-fulton`, `ga-cobb`, `ga-gwinnett`,
  `ga-state-court`, `ga-magistrate`, `ga-county-courts`,
  `ga-family-court`
- For pre-filing QC: `ga-quality-check`, `ga-fact-check`
- For pro se conventions: `ga-pro-se`

## References

- `references/notice-of-hearing-template.md` — annotated template
- `references/rule-nisi-template.md` — proposed Rule Nisi for signature
