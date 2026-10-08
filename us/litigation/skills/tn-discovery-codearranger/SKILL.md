---
name: tn-discovery-codearranger
title: Tennessee Discovery
description: Use when drafting, responding to, or compelling discovery in a Tennessee civil case in Circuit or Chancery Court. Triggers include "Tennessee discovery", "Tenn. R. Civ. P. 26", "interrogatories under Rule 33", "how many interrogatories can I serve in Tennessee", "Request for Production under Rule 34", "Request for Admission under Rule 36", "deposition under Rule 30", "motion to compel Tennessee", "Rule 37 sanctions", "discovery response deadline Tennessee", "meet and confer Tennessee", "discovery dispute", "can I do discovery in General Sessions". Covers the Tenn. R. Civ. P. 26-37 framework, the 30-day response window (45 days for a defendant served before answering), the absence of a statewide numeric cap on interrogatories, the General Sessions "no formal discovery as of right" rule, meet-and-confer, and the motion-to-compel / sanctions workflow.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to
> discovery. Verify against the current Tenn. R. Civ. P. and the
> venue's local rules and standing orders before serving or filing.

Use this skill alongside `tn-statewide-format`, `tn-law-references`,
and (where applicable) `tn-first-30-days`. The Tennessee discovery
framework lives in **Tenn. R. Civ. P. 26-37** and applies in the
**Circuit** and **Chancery** Courts.

> **General Sessions has no formal discovery as of right.** Practice
> in General Sessions is informal and the Tenn. R. Civ. P. do not
> apply there except where specifically made applicable. If discovery
> is essential, the case may need to move to Circuit Court (including
> by the 10-day de novo appeal under Tenn. Code Ann. § 27-5-108 — see
> `tn-post-judgment`). See `tn-general-sessions`.

## Snapshot — Tennessee written-discovery clock

| Discovery device | Rule | Response due |
|---|---|---|
| Interrogatories | Tenn. R. Civ. P. 33 | **30 days** after service (**45 days** if the defendant was served before serving its answer) |
| Requests for Production | Tenn. R. Civ. P. 34 | **30 days** after service (same 45-day pre-answer rule) |
| Requests for Admission | Tenn. R. Civ. P. 36 | **30 days** after service (same 45-day pre-answer rule) |

Frame these as the **current** day counts; verify against Tenn. R.
Civ. P. 33/34/36 and add the Tenn. R. Civ. P. 6.05 **3-day mail
add-on** when service was by mail. Compute with `tn-deadlines`.

## Scope — Tenn. R. Civ. P. 26

Discovery scope is broad: a party may obtain discovery of any matter,
not privileged, that is **relevant** to the subject matter and
reasonably calculated to lead to admissible evidence, subject to the
proportionality and protective-order limits of Rule 26. Privileged
matter must be withheld with a **privilege log** describing the
withheld material so the requesting party can assess the claim.

## Interrogatories — Tenn. R. Civ. P. 33

Tennessee **allows written interrogatories**. There is **no statewide
numeric cap** on interrogatories under Tenn. R. Civ. P. 33.

> **Verify the venue.** Some counties' **local rules** impose a
> numeric cap (e.g., counting discrete subparts). Always check the
> filing court's local rules — indexed at tncourts.gov — before
> assuming you may serve an unlimited set. See `tn-law-references`.

- Service: after commencement of the action, subject to the venue's
  case-management order.
- Response due: **30 days** (45 days for a defendant served before
  answering).
- Form: each interrogatory answered separately and fully, in writing
  under oath; any objection stated with specificity.

```
INTERROGATORIES

Pursuant to Tenn. R. Civ. P. 33, [Defendant] requests that
[Plaintiff] answer the following Interrogatories separately and fully
in writing under oath, and serve the answers on the undersigned
within thirty (30) days of service.

INTERROGATORY NO. 1: State the name, address, and telephone number of
each person known to you to have knowledge of the facts alleged in the
Complaint, and describe the subject of that knowledge.

ANSWER:
[Response]

INTERROGATORY NO. 2: [...]
```

## Requests for Production — Tenn. R. Civ. P. 34

- Service: after commencement of the action.
- Response due: **30 days** (45 days for a defendant served before
  answering).
- The responding party must produce documents as they are kept in the
  usual course of business or organized to correspond to the
  categories in the request.
- ESI: produce in a reasonably usable form; preserve metadata unless
  the form is agreed otherwise.

## Requests for Admission — Tenn. R. Civ. P. 36

- Service: after commencement of the action.
- Response due: **30 days** (45 days for a defendant served before
  answering).
- **Critical**: a matter is **deemed admitted** unless the party
  timely serves a written answer or objection (Tenn. R. Civ. P. 36.01).
  Calendar RFA deadlines carefully — a missed deadline can concede
  dispositive facts.
- A party may move to **withdraw or amend** an admission under Tenn.
  R. Civ. P. 36.02 when the merits would be served and the requesting
  party is not prejudiced.

## Depositions — Tenn. R. Civ. P. 30 / 31

- **Rule 30** — oral depositions; **Rule 31** — depositions on written
  questions.
- Notice: serve **reasonable** written notice stating time, place, and
  the deponent; for an entity deposition, describe the matters for
  examination so the entity can designate a witness.
- Non-party documents: a deposition notice may be accompanied by a
  subpoena under Tenn. R. Civ. P. 45.
- Remote / video depositions are permitted by stipulation or court
  order; confirm the recording method.

## Meet-and-confer

Before filing a discovery motion, **confer** with opposing counsel to
attempt informal resolution, and **document** the attempt. Many
Tennessee local rules and standing orders require a good-faith
conferral certificate as a precondition to a motion to compel —
verify the venue's local rule.

```
Subject: Conferral re: Discovery Responses — [Case Short Title],
         Docket No. [Number]

[Counsel Name],

This email is my good-faith effort to confer before I file a Motion to
Compel under Tenn. R. Civ. P. 37.

Your responses to my client's First Set of Interrogatories and
Requests for Production, served on [DATE], are deficient as follows:

  1. Interrogatory No. 3 — Boilerplate objection ("vague, overly
     broad, unduly burdensome") without specifying which terms are
     vague or quantifying the burden.

  2. RFP No. 7 — No documents produced; the response states none
     exist, yet the Complaint references documents within this request.

  [...]

Please supplement by [date 7-10 days out]. If I do not hear from you, I
will proceed with a Motion to Compel and seek expenses under Tenn. R.
Civ. P. 37.01.

[Name]
```

## Motion to compel — Tenn. R. Civ. P. 37

If conferral fails, move to compel under **Tenn. R. Civ. P. 37.01**.
The motion should:

1. **Identify the specific deficiencies** (which interrogatory / RFP /
   RFA and why the response is inadequate).
2. **Attach** the requests and responses as exhibits.
3. **Document the conferral attempt** (certificate of good-faith
   conferral, if the venue requires one).
4. **Address each objection** with specificity.
5. **Request specific relief**: an order compelling responses by a date
   certain, and an award of expenses.

### Sanctions

- **Tenn. R. Civ. P. 37.01** — on a successful motion to compel, the
  court may award the reasonable expenses, including attorney's fees,
  caused by the failure, unless the opposing position was
  substantially justified.
- **Tenn. R. Civ. P. 37.02** — for disobedience of a discovery order:
  stronger sanctions, up to striking pleadings, dismissal, or default
  judgment.
- **Tenn. R. Civ. P. 37.03** — consequences of failing to admit or to
  supplement.

Verify the current subpart lettering in the verbatim rule text.

## Composition

- For drafting the motion to compel: `tn-draft-motion`
- For the supporting declaration / affidavit: `tn-draft-declaration`
- For statewide format: `tn-statewide-format`
- For consumer-debt RFP / RFA banks and debt-buyer discovery strategy:
  `tn-consumer-debt`
- For deadline arithmetic: `tn-deadlines`
- For the informal General Sessions track: `tn-general-sessions`

## References

- `references/interrogatory-templates.md` — Rule 33 templates
- `references/rfp-templates.md` — Rule 34 templates
- `references/rfa-templates.md` — Rule 36 templates
- `references/motion-to-compel.md` — Tenn. R. Civ. P. 37 scaffold
- `references/conferral-templates.md` — meet-and-confer email templates
- `references/privilege-log.md` — privilege-log format and content
