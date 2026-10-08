---
name: ga-schedule-hearing-codearranger
title: Set a Hearing (Georgia)
description: This skill should be used when the user needs to get a motion heard in a Georgia court. Triggers include "set a hearing in Georgia", "rule nisi", "notice of hearing Georgia", "get my motion on the calendar", "schedule a hearing in Georgia", "reserve a hearing date Georgia". In Georgia, a party requests oral argument under USCR 6.3 and the court sets the hearing by signing a Rule Nisi (a proposed order setting the date and time) under USCR 6.4. This skill drafts the Rule Nisi and the Notice of Hearing, explains coordinating with the assigned judge's staff attorney or calendar clerk, covers service and e-filing of the rule nisi through PeachCourt or Odyssey eFileGA, and addresses family-case calendaring through the assigned division.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Set a Hearing (Georgia)

> **NOT LEGAL ADVICE.** This skill is a procedural and
> drafting aid, not legal advice. Verify current rules,
> deadlines, and venue-specific practices before filing.
> Pair with substantive review by counsel where stakes
> warrant.

In Georgia civil practice, a hearing on a motion is obtained through
the **Rule Nisi** mechanism. A party requests oral argument under
**USCR 6.3**, and the court sets the hearing by signing a **Rule
Nisi** under **USCR 6.4** — a proposed order, prepared by the movant
and presented to chambers, that fixes the date and time the judge
will hear the matter. This skill drafts that Rule Nisi and the
accompanying **Notice of Hearing**.

## The Rule Nisi — Georgia's hearing-setting device

A **Rule Nisi** ("rule unless") is a short proposed order. The movant
drafts it with a blank date/time, sends it to the assigned judge's
chambers, and the judge signs it with the date the court is available.
The signed Rule Nisi is then served on all parties and tells everyone
when and where to appear.

| Step | What happens |
|---|---|
| 1. File the motion | Stated with particularity under USCR 6.1 |
| 2. Request oral argument | Under USCR 6.3 (for summary judgment, a timely request makes oral argument a matter of right) |
| 3. Draft the Rule Nisi | Proposed order setting hearing date/time/place; leave date/time blank or propose dates |
| 4. Coordinate with chambers | Get an available date from the judge's staff attorney / calendar clerk |
| 5. Judge signs the Rule Nisi | Under USCR 6.4 the court sets the hearing |
| 6. Serve and file | Serve the signed Rule Nisi + Notice of Hearing on all parties; e-file |

## Coordinating with chambers

Hearing dates come from the **assigned judge's** chambers, not from a
self-service docket. Contact the judge's **staff attorney** or
**calendar clerk** to obtain an available date before finalizing the
Rule Nisi. Practice varies by judge and county:

- Some chambers want the proposed Rule Nisi emailed in Word so the
  staff attorney can insert the date and route it for signature.
- Some divisions publish a standing motions calendar and assign you a
  slot.
- In Fulton, check the assigned judge's **Civil Standing Case
  Management Order** for the chambers contact and the preferred
  method of requesting a setting.

**Agent behavior**: when drafting the request, fetch the assigned
judge's current chambers contact (staff attorney / calendar clerk)
from the county Superior or State Court website. **Do not cache or
guess chambers contacts** — they change at judicial rotation.

## Rule Nisi template

```
                          [Caption]

                          RULE NISI

The above-styled matter coming before the Court on [Movant]'s
[Motion Title], filed [date],

IT IS HEREBY ORDERED that a hearing on said Motion shall be held
before the Honorable [Judge Name] on the ____ day of __________,
20__, at ____ __.m., in Courtroom ____, [Courthouse Name and
Address], [City], Georgia.

All parties shall appear and show cause why the relief requested
should not be granted.

SO ORDERED, this ____ day of __________, 20__.

                                   ___________________________
                                   Judge, [Superior / State] Court
                                   [Circuit] Judicial Circuit
```

## Notice of Hearing template

After the judge signs the Rule Nisi, serve a **Notice of Hearing**
(Georgia terminology) on all parties:

```
                          [Caption]

                       NOTICE OF HEARING

TO: [All parties / counsel of record]

PLEASE TAKE NOTICE that [Movant]'s [Motion Title] is scheduled for
hearing before the Honorable [Judge Name] on [date] at [time] in
Courtroom [###], [Courthouse Name and Address], pursuant to the
Rule Nisi entered by the Court on [date].

This ____ day of __________, 20__.

                                   [Signature block]
                                   [Name]
                                   [Georgia Bar No. or "Pro Se"]
                                   [Address / Phone / Email]

                  [Certificate of Service]
```

## Service of the Rule Nisi and Notice

The signed Rule Nisi and the Notice of Hearing are subsequent papers
served under **O.C.G.A. § 9-11-5** with a **certificate of service**
at the foot. Registered e-filers are served through the e-filing
system; any party not on the e-filing system must be served by the
method the rules allow (mail, hand delivery). Confirm every party
receives actual notice of the date.

## E-filing the Rule Nisi

Georgia civil e-filing is mandatory in the flagship counties (SB407
mandate). The e-filing system is county-dependent:

- **Fulton** and **Cobb** — **PeachCourt** (eFileGA).
- **Gwinnett** — **Odyssey eFileGA** (Tyler).

Confirm the county's system on the assigned court's site. Upload the
proposed Rule Nisi for chambers' signature per local practice, then
file the signed Rule Nisi and the Notice of Hearing under the case.

## Family-case calendaring

In divorce and other domestic matters (heard exclusively in Superior
Court), the case is assigned to a division and calendaring runs
through that **assigned division**. In Fulton, that is the dedicated
Family Division. Before the hearing, confirm the pre-hearing filings
required by the domestic standing order are on file — the Domestic
Relations Financial Affidavit (USCR 24.2) and the Child Support
Worksheet — or the court may decline to reach the merits. Temporary
hearings in family cases are commonly set by Rule Nisi the same way.

## Hearing-length estimation guidance

| Motion type | Typical length |
|---|---|
| Motion to dismiss (O.C.G.A. § 9-11-12(b)(6)) | 30-60 min |
| Motion for summary judgment (O.C.G.A. § 9-11-56) | 60-90 min |
| Motion to compel (O.C.G.A. § 9-11-37) | 30 min |
| Motion to open default (O.C.G.A. § 9-11-55) | 30-60 min |
| Temporary hearing (family) | 30-90 min |
| Final hearing — uncontested divorce | 5-15 min |
| Permanent/final hearing — contested family | Half-day to full day |

## Composition

- For drafting the underlying motion: `ga-draft-motion`
- For the Rule Nisi and the Notice of Hearing as orders/notices:
  `ga-draft-order`, `ga-draft-note`
- For hearing-day prep and protocol: `ga-hearings`
- For court-specific scheduling channels and e-filing system:
  `ga-fulton`, `ga-cobb`, `ga-gwinnett`
- For deadlines and timing: `ga-deadlines`
- For format: `ga-statewide-format`
- For assembling and filing the packet: `ga-file-packet`

## References

- `references/rule-nisi-template.md`
- `references/notice-of-hearing-template.md`
- `references/chambers-coordination.md` — staff-attorney / calendar-
  clerk contact and per-county e-filing
