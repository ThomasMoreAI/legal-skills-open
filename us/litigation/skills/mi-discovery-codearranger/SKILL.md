---
name: mi-discovery-codearranger
title: Michigan Discovery
description: 'Use when drafting, responding to, or compelling discovery in a Michigan civil case. Triggers include "Michigan discovery", "MCR 2.302", "interrogatories Michigan", "request for production Michigan", "request for admission Michigan", "deposition Michigan", "initial disclosures Michigan", "motion to compel MCR 2.313", "discovery sanctions Michigan", "meet and confer Michigan", "proportionality MCR 2.302(B)(1)", "discovery cutoff Michigan", "district court discovery Michigan". Covers the MCR 2.301-2.316 framework: the scheduling-order discovery period, mandatory initial disclosures, the proportionality scope, interrogatories, requests for production, requests for admission, depositions, meet-and-confer, and the motion-to-compel / sanctions workflow.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to
> discovery. Verify against the current Michigan Court Rules (MCR) and
> the venue's local rules and scheduling order before serving or
> filing.

Use this skill alongside `mi-statewide-format`, `mi-law-references`,
and (where applicable) `mi-first-30-days`. The Michigan civil
discovery framework lives in **MCR 2.301-2.316** and applies in the
**Circuit Court** (with a streamlined track in the **District Court** —
see below).

## Snapshot — Michigan written-discovery clock

| Discovery device | Rule | Response window |
|---|---|---|
| Interrogatories | MCR 2.309 | response due within the period set by the rule after service |
| Requests for Production / entry | MCR 2.310 | response due within the period set by the rule after service |
| Requests for Admission | MCR 2.312 | response due within the period set by the rule; **deemed admitted if not timely answered or objected to** |

Treat these as the **current** windows: pull the exact day counts from
the verbatim MCR text in the corpus (`mi-law-references`) rather than
relying on a memorized number, and add the MCR 2.107(C) **additional
time for service by mail** where it applies. Compute every date with
`mi-deadlines`.

## The discovery period — MCR 2.301

Discovery is governed by the court's **scheduling order** (MCR 2.401).
**MCR 2.301(A)** ties the discovery period to that order and ordinarily
closes it on the scheduling-order **discovery cutoff**. Confirm the
cutoff before serving requests whose responses would come due after it;
late-served discovery may be barred absent leave.

> **District Court — streamlined track.** Discovery in the District
> Court is **more limited** than in Circuit Court. **MCR 2.301(A)**
> restricts the scope/availability of District Court civil discovery
> (and discovery is generally unavailable in small claims). Check the
> current MCR 2.301(A) subrule before assuming Circuit-style discovery
> is available. See `mi-district-courts`.

## Mandatory initial disclosures — MCR 2.302(A)

Michigan adopted **mandatory initial disclosures** in the 2020
discovery amendments. **MCR 2.302(A)** requires parties to disclose
core case information (witnesses, documents, damages computations, and
applicable insurance, as the rule specifies) **without awaiting a
request**, on the timeline the rule sets relative to the pleadings /
scheduling order, and as a continuing duty under MCR 2.302(E).

- Calendar the initial-disclosure deadline as soon as the case is at
  issue — it runs independently of any request you serve.
- Verify the current MCR 2.302(A) categories and timing in the corpus;
  the subrules differ by track and case type.

## Scope and proportionality — MCR 2.302(B)(1)

The 2020 amendments rewrote discovery scope to a **proportionality**
standard, drawing on the lineage of the federal 2015 amendments to
FRCP 26(b)(1) (offered only as drafting history, not as controlling
law). Under **MCR 2.302(B)(1)**, parties may obtain discovery of any
non-privileged matter relevant to a claim or defense **and proportional
to the needs of the case**, weighing the factors the rule enumerates
(importance of the issues, amount in controversy, parties' relative
access to information, resources, importance of the discovery, and
burden-versus-benefit).

- Frame requests and objections in proportionality terms — a bare
  "overly broad / unduly burdensome" objection is weak under the
  amended rule.
- Privileged or trial-preparation material is withheld with a
  **privilege log** (MCR 2.302(B)(5)) describing the withheld matter so
  the requesting party can assess the claim.

## Interrogatories — MCR 2.309

Michigan **allows written interrogatories** to parties under MCR 2.309.
The rule **does not impose a statewide numeric cap** by its terms; a
**scheduling order or local rule may limit** the number — confirm any
cap (see `mi-law-references`) before serving a large set. Answers are
served separately and fully, in writing under oath, with each objection
stated specifically; business records may be produced in lieu of a
narrative answer on the rule's conditions.

```
INTERROGATORIES

Pursuant to MCR 2.309, [Defendant] requests that [Plaintiff] answer the
following Interrogatories separately and fully, in writing under oath,
within the time allowed by the rule.

INTERROGATORY NO. 1: State the name, address, and telephone number of
each person known to you to have knowledge of the facts alleged in the
Complaint, and describe the subject of that knowledge.

ANSWER: [Response]
```

## Requests for Production — MCR 2.310

Requests documents, ESI, and tangible things, and may seek entry onto
land for inspection. The responding party produces documents as kept in
the usual course of business or organized to correspond to the request's
categories. **ESI** is produced in a reasonably usable form; address
form-of-production and metadata by stipulation, consistent with the
proportionality limits of MCR 2.302(B).

## Requests for Admission — MCR 2.312

- **Critical**: a matter is **deemed admitted** unless the party timely
  serves a written answer or objection within the period MCR 2.312
  allows. Calendar RFA deadlines carefully — a missed deadline can
  concede dispositive facts.
- A party may move to **amend or withdraw** an admission on the
  conditions the rule states (merits served; no prejudice to the
  requesting party).

## Depositions — MCR 2.303-2.308

- **MCR 2.306** oral depositions; **MCR 2.307** depositions on written
  questions; **MCR 2.303** deposition procedure; **MCR 2.308** use at
  trial.
- Serve **reasonable** written notice of time, place, and deponent; for
  an entity deposition, describe the matters for examination so the
  entity can designate a witness.
- A deposition notice may be paired with a **subpoena** under MCR 2.305
  / MCR 2.506. Remote / video depositions are permitted by stipulation
  or order — confirm the recording method on the notice.

## Meet-and-confer

Before filing a discovery motion, **confer** with opposing counsel and
**document** the attempt. MCR 2.313 conditions relief on a good-faith
effort to obtain the discovery without court action; many scheduling
orders and local rules require a conferral certificate as a
precondition to a motion to compel — verify the venue's requirement.

```
Subject: Conferral re: Discovery Responses — [Case Short Title],
         Case No. [Number]

[Counsel Name], this email is my good-faith effort to confer under MCR
2.313 before I file a Motion to Compel. Your responses to my client's
First Set of Interrogatories and Requests for Production, served on
[DATE], are deficient as follows:

  1. Interrogatory No. 3 — Boilerplate objection without specifying
     vague terms or quantifying the burden, contrary to MCR 2.302(B)(1).
  2. Request for Production No. 7 — No documents produced though the
     Complaint references documents within this request.

Please supplement by [date]. If I do not hear from you, I will proceed
with a Motion to Compel and seek expenses under MCR 2.313. [Name]
```

## Motion to compel and sanctions — MCR 2.313

If conferral fails, move to compel under **MCR 2.313**. The motion
should:

1. **Identify the specific deficiencies** (which interrogatory / RFP /
   RFA, and why the response is inadequate).
2. **Attach** the requests and responses as exhibits.
3. **Document the conferral attempt** (good-faith certificate, where
   required).
4. **Address each objection** on the merits, in proportionality terms.
5. **Request specific relief**: an order compelling responses by a date
   certain, and an award of expenses.

### Sanctions ladder

- On a granted motion to compel, **MCR 2.313** authorizes an award of
  the reasonable **expenses, including attorney fees**, caused by the
  failure, unless the opposing position was substantially justified.
- For **disobedience of a discovery order**, MCR 2.313 escalates to
  stronger sanctions — up to striking pleadings, dismissal, or
  default judgment.
- The rule also addresses the consequences of failing to disclose, to
  admit, or to supplement.

Verify the current subrule lettering against the verbatim MCR 2.313
text in `mi-law-references`.

## Composition

- For drafting the motion to compel: `mi-draft-motion`
- For the supporting affidavit / declaration: `mi-draft-declaration`
- For the notice of hearing: `mi-draft-note`
- For statewide format: `mi-statewide-format`
- For deadline arithmetic and the scheduling-order cutoff:
  `mi-deadlines`
- For the District Court streamlined track: `mi-district-courts`
- For consumer-debt RFP / RFA banks and debt-buyer discovery strategy:
  `mi-consumer-debt`

## References

- `references/interrogatory-templates.md` — MCR 2.309 templates
- `references/rfp-templates.md` — MCR 2.310 templates
- `references/rfa-templates.md` — MCR 2.312 templates
- `references/initial-disclosures.md` — MCR 2.302(A) disclosure checklist
- `references/motion-to-compel.md` — MCR 2.313 scaffold
- `references/conferral-templates.md` — meet-and-confer email templates
- `references/privilege-log.md` — MCR 2.302(B)(5) privilege-log format
