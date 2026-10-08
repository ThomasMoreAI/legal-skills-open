---
name: id-discovery-codearranger
title: Idaho Discovery
description: 'Use when drafting, responding to, or compelling discovery in an Idaho civil case. Triggers include "Idaho discovery", "interrogatories Idaho Rule 33", "how many interrogatories can I serve in Idaho", "40 interrogatory limit Idaho", "request for production Idaho Rule 34", "request for admission Idaho Rule 36", "deemed admitted Idaho RFA", "deposition Idaho Rule 30", "30 days to respond to discovery Idaho", "meet and confer Idaho discovery", "motion to compel Idaho Rule 37", "discovery sanctions Idaho". Covers the I.R.C.P. 26-37 framework: interrogatories (cap of 40 including subparts, Rule 33), requests for production (Rule 34), requests for admission (Rule 36), depositions (Rule 30), the 30-day response window, meet-and-confer mechanics, and the motion-to-compel / sanctions workflow under Rule 37.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Deposition Notice
  path: references/deposition-notice.md
- title: Interrogatory Templates
  path: references/interrogatory-templates.md
- title: Meet And Confer Templates
  path: references/meet-and-confer-templates.md
- title: Motion To Compel
  path: references/motion-to-compel.md
- title: Rfa Templates
  path: references/rfa-templates.md
- title: Rfp Templates
  path: references/rfp-templates.md
---

# Idaho Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to discovery.
> Verify against the current Idaho Rules of Civil Procedure and the
> court's local rules and any scheduling order before serving or filing.

Use this skill alongside `id-statewide-format`, `id-law-references`, and
(where applicable) `id-first-30-days`. The Idaho civil discovery
framework lives in **I.R.C.P. 26-37** and applies in the **District
Court** and the **Magistrate Division**. Pull the verbatim rule text
from `../id-law-references/references/court-rules/` before serving or
responding.

## Idaho allows written interrogatories

Idaho permits the full toolkit of party discovery — written
interrogatories, requests for production, requests for admission, and
depositions — without leave of court. The four devices below are
available as of right; the response window for each is **30 days**.

## Interrogatories — I.R.C.P. 33

Written interrogatories to a party are governed by **I.R.C.P. 33**.

- **Numeric cap — 40, including subparts.** Under **I.R.C.P. 33(a)(1)** a
  party may serve **no more than 40 interrogatories, counting each
  discrete subpart as a separate interrogatory**, without leave of court
  or a written stipulation. To exceed the cap, obtain a stipulation or
  move for leave. Confirm the current count and the subpart-counting
  rule in the corpus before serving a large set.
- **Responses — 30 days.** Answers are served separately and fully, in
  writing under oath, within **30 days** (**I.R.C.P. 33(b)(2)**), with
  each objection stated specifically. Business records may be produced in
  lieu of a narrative answer on the rule's conditions (**Rule 33(d)**).

```
INTERROGATORIES

Pursuant to I.R.C.P. 33, [Defendant] requests that [Plaintiff] answer
the following Interrogatories separately and fully, in writing under
oath, within 30 days of service.

INTERROGATORY NO. 1: State the name, address, and telephone number of
each person known to you to have knowledge of the facts alleged in the
Complaint, and describe the subject of that knowledge.

ANSWER: [Response]
```

## Requests for Production — I.R.C.P. 34

**I.R.C.P. 34** requests documents, electronically stored information
(ESI), and tangible things, and may seek **entry onto land** for
inspection. The responding party produces documents as kept in the usual
course of business or organized to correspond to the request's
categories, and responds within **30 days** (**I.R.C.P. 34(b)(2)**).
**ESI** is produced in a reasonably usable form; address
form-of-production and metadata by stipulation, consistent with the
proportionality limits of Rule 26.

## Requests for Admission — I.R.C.P. 36

- **Critical — deemed admitted.** Under **I.R.C.P. 36(a)(3)** a matter is
  **deemed admitted** unless the party serves a written answer or
  objection within **30 days** of service. Calendar RFA deadlines
  carefully — a missed deadline can concede dispositive facts.
- A party may move to **amend or withdraw** an admission on the rule's
  conditions (the merits are subserved and no prejudice to the requesting
  party).

## Depositions — I.R.C.P. 30

- **I.R.C.P. 30** governs oral depositions; serve **reasonable** written
  notice of the time, place, and deponent.
- A party may take up to **30 depositions** without leave of court; to
  exceed that number, obtain a stipulation or move for leave. Confirm the
  current limit in the corpus.
- For an **entity deposition**, describe the matters for examination with
  reasonable particularity so the entity can designate a witness.
- Remote / video depositions are permitted by stipulation or order; state
  the recording method on the notice.

## Scope and proportionality — I.R.C.P. 26

Discovery is limited to matter that is **relevant to a claim or defense
and proportional to the needs of the case** (**I.R.C.P. 26(b)(1)**).
Privileged matter and attorney work product are protected; assert a
privilege expressly and log withheld material.

## Meet-and-confer

Before filing any discovery motion, **confer in good faith** with the
opposing party and **document** the attempt. Idaho conditions discovery
relief on a good-faith effort to resolve the dispute without court
action, and the motion must include a **certification** that the effort
was made. Confirm the venue's specific conferral requirement in
`../id-law-references/references/court-rules/`.

```
Subject: Meet-and-Confer re: Discovery Responses —
         [Case Short Title], Case No. [Number]

[Name], this is my good-faith effort to confer under I.R.C.P. 37 before
I file a Motion to Compel. Your responses to my First Set of
Interrogatories and Requests for Production, served on [DATE], are
deficient as follows:

  1. Interrogatory No. 3 — Boilerplate objection without specifying the
     vague term or quantifying the burden.
  2. Request for Production No. 7 — No documents produced though the
     Complaint references documents within this request.
  3. Request for Admission No. 2 — Evasive non-answer.

Please supplement by [date]. If I do not hear from you, I will proceed
with a Motion to Compel and seek expenses under Rule 37. [Name]
```

## Motion to compel and sanctions — I.R.C.P. 37

If conferral fails, move to compel under **I.R.C.P. 37**. The motion
should:

1. **Identify the specific deficiencies** (which interrogatory / RFP /
   RFA, and why the response is inadequate).
2. **Attach** the requests and responses as exhibits.
3. **Certify the good-faith conferral** (and attach the correspondence).
4. **Address each objection** on the merits.
5. **Request specific relief**: an order compelling responses by a date
   certain, plus an award of reasonable expenses.

A motion to compel is noticed for hearing under **I.R.C.P. 7(b)** — see
`id-hearings` and `id-schedule-hearing`.

### Sanctions ladder

- On a granted motion to compel, **Rule 37** authorizes an award of the
  reasonable **expenses, including attorney fees**, caused by the
  failure, unless the opposing position was substantially justified.
- For **disobedience of a discovery order**, Rule 37 escalates to
  stronger sanctions — up to striking pleadings, dismissal, or default
  judgment.
- Rule 37 also addresses the consequences of **failing to admit** under
  Rule 36.

Verify the current subpart lettering against the verbatim Rule 37 text in
`../id-law-references/references/court-rules/`.

## Composition

- For drafting the motion to compel: `id-draft-motion`
- For the supporting affidavit / declaration: `id-draft-declaration`
- For the notice of hearing on the motion: `id-draft-note`,
  `id-schedule-hearing`
- For statewide format: `id-statewide-format`
- For deadline arithmetic (the 30-day response window and the
  scheduling-order cutoff): `id-deadlines`
- For venue: `id-ada`, `id-bonneville`, `id-county-courts`
- For consumer-debt RFP / RFA banks and debt-buyer chain-of-title
  discovery strategy: `id-consumer-debt`

## References

- `references/interrogatory-templates.md` — Rule 33 templates (40-cap)
- `references/rfp-templates.md` — Rule 34 templates
- `references/rfa-templates.md` — Rule 36 templates
- `references/deposition-notice.md` — Rule 30 notice scaffold
- `references/motion-to-compel.md` — Rule 37 scaffold
- `references/meet-and-confer-templates.md` — conferral templates
