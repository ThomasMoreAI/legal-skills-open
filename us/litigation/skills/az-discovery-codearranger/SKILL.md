---
name: az-discovery-codearranger
title: Arizona Discovery
description: 'Use when drafting, responding to, or compelling discovery in an Arizona civil case. Triggers include "Arizona discovery", "Rule 26.1 disclosure Arizona", "mandatory initial disclosure Arizona", "tiered case Arizona Rule 26.2", "Tier 1 Tier 2 Tier 3 Arizona", "interrogatories Arizona Rule 33", "request for production Arizona", "Rule 34 Arizona", "request for admission Arizona Rule 36", "deposition Arizona Rule 30", "subpoena Arizona Rule 45", "motion to compel Rule 37 Arizona", "good-faith consultation Arizona discovery", "discovery sanctions Arizona". Covers the Ariz. R. Civ. P. 26-37 framework: the broad mandatory initial disclosure under Rule 26.1, the tiered-case discovery limits under Rule 26.2, interrogatories, requests for production, requests for admission, depositions, subpoenas, and the motion-to-compel / sanctions workflow.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to
> discovery. Verify against the current Arizona Rules of Civil Procedure
> and the venue's local rules and scheduling order before serving or
> filing.

Use this skill alongside `az-statewide-format`, `az-law-references`, and
(where applicable) `az-first-30-days`. The Arizona civil discovery
framework lives in **Ariz. R. Civ. P. 26-37** and applies in the
**Superior Court**. The **Justice Court** runs a limited, streamlined
discovery track — see `az-justice-courts`.

Two features make Arizona discovery distinctive, and they drive
everything else below. Read these first.

## ★ Distinctive #1 — Mandatory initial disclosure (Rule 26.1)

Arizona does **not** wait for a discovery request to put the core of a
case on the table. **Ariz. R. Civ. P. 26.1** imposes a **broad,
automatic, and continuing duty** to disclose — far more than notice
pleading. Each party must disclose, **without awaiting a request**:

- the **factual basis** and **legal theory** of each claim and defense;
- the **names, addresses, and phone numbers** of witnesses / persons with
  relevant knowledge, and the subject of that knowledge;
- the names of **expert witnesses** and the substance of their opinions;
- a **computation and measure of damages** and supporting documents;
- the existence and location of **relevant documents, ESI, and tangible
  things** (and the party must produce or make them available);
- the existence of **insurance** that may satisfy a judgment.

Key practice points:

- **Calendar the Rule 26.1 deadline the moment the case is at issue.**
  The timeline runs relative to the pleadings / scheduling order —
  independent of any request you serve. Confirm the current day counts
  in the corpus (`az-law-references`) and compute dates with
  `az-deadlines`.
- The duty is **continuing**: a party must **seasonably supplement**.
- **Disclosure is enforced with teeth.** A witness or information not
  timely disclosed may be **excluded** absent good cause / harmless
  error — the exclusion sanction is the backbone of the regime, so treat
  Rule 26.1 as the centerpiece, not a formality.

## ★ Distinctive #2 — The tiered-case system (Rule 26.2)

Arizona assigns every Superior Court case to **Tier 1, Tier 2, or Tier
3** based principally on the **amount in controversy** (and certain
case types). The tier sets **presumptive discovery limits** — deposition
hours / count, interrogatory count, RFA count, and similar caps — scaled
to the stakes of the case.

- **Tier 1** — lowest amount in controversy; the **tightest** limits.
- **Tier 2** — mid-range; intermediate limits.
- **Tier 3** — highest amount in controversy (and complex / specified
  case types); the **most generous** limits.

How tier is set:

- A party states the tier (or its basis) in an **early pleading /
  certificate**, and the court assigns the tier in the scheduling order.
  The tier can be **changed by stipulation or by motion** for good cause.
- The **dollar thresholds** separating the tiers and the **specific
  numeric limits** each tier imposes are **rule-set and subject to
  amendment** — **do not memorize them**. Pull the current Tier 1 / 2 /
  3 thresholds and per-tier limits from the verbatim Rule 26.2 text in
  the corpus (`az-law-references`) before serving discovery.

> **Confirm the tier before you serve anything.** Every numeric
> discovery limit below is a function of the assigned tier. Serving
> discovery that exceeds the tier's presumptive limit without a
> stipulation or court order risks objection and exclusion.

## Interrogatories — Rule 33

Arizona allows written interrogatories to parties under **Ariz. R. Civ.
P. 33**, which distinguishes **uniform interrogatories** (the
court-approved standard sets) from **non-uniform interrogatories**.

- The **number of interrogatories is set by the Rule 26.2 tier**, not by
  a flat statewide cap: Rule 33(a)(2) provides that interrogatories are
  "subject to the numeric limits in Rule 26.2(f)." Each subpart counts as
  one interrogatory, except that a uniform interrogatory and its subparts
  count as one. **Confirm the current per-tier count and the
  subpart-counting rule in the corpus** before serving a large set.
- Answers are served separately and fully, in writing under oath, with
  each objection stated specifically. Business records may be produced
  in lieu of a narrative answer on the rule's conditions (Rule 33(d)).

```
NON-UNIFORM INTERROGATORIES

Pursuant to Ariz. R. Civ. P. 33, [Defendant] requests that [Plaintiff]
answer the following Interrogatories separately and fully, in writing
under oath, within the time allowed by the rule.

INTERROGATORY NO. 1: State the name, address, and telephone number of
each person known to you to have knowledge of the facts alleged in the
Complaint, and describe the subject of that knowledge.

ANSWER: [Response]
```

## Requests for Production — Rule 34

**Ariz. R. Civ. P. 34** requests documents, ESI, and tangible things,
and may seek **entry onto land** for inspection. The responding party
produces documents as kept in the usual course of business or organized
to correspond to the request's categories. **ESI** is produced in a
reasonably usable form; address form-of-production and metadata by
stipulation, consistent with the proportionality / tier limits.

## Requests for Admission — Rule 36

- **Critical**: under **Ariz. R. Civ. P. 36**, a matter is **deemed
  admitted** unless the party timely serves a written answer or
  objection within the period the rule allows. Calendar RFA deadlines
  carefully — a missed deadline can concede dispositive facts.
- A party may move to **amend or withdraw** an admission on the rule's
  conditions (merits served; no prejudice to the requesting party).

## Depositions — Rule 30

- **Ariz. R. Civ. P. 30** governs oral depositions; serve **reasonable**
  written notice of time, place, and deponent.
- For an **entity deposition**, describe the matters for examination so
  the entity can designate a witness.
- **Deposition hours and the number of depositions are tier-limited
  under Rule 26.2** — confirm the tier's presumptive deposition limits
  before noticing. Remote / video depositions are permitted by
  stipulation or order; state the recording method on the notice.

## Subpoenas — Rule 45

**Ariz. R. Civ. P. 45** compels a non-party to produce documents or
appear for deposition / at trial. Observe the rule's service, notice-to-
parties, and **protection-from-undue-burden** provisions; a non-party
may object or move to quash on the rule's grounds.

## Good-faith consultation and meet-and-confer

Before filing any discovery motion, **personally consult** with opposing
counsel and **document** the attempt. Arizona conditions discovery
relief on a **good-faith consultation** (and the motion must include a
**certification** that it occurred). Many scheduling orders require the
conferral certificate as a precondition — verify the venue's
requirement in `az-law-references`.

```
Subject: Good-Faith Consultation re: Discovery Responses —
         [Case Short Title], Case No. [Number]

[Counsel Name], this is my good-faith effort to confer under Ariz. R.
Civ. P. 37 before I file a Motion to Compel. Your responses to my
client's First Set of Non-Uniform Interrogatories and Requests for
Production, served on [DATE], are deficient as follows:

  1. Interrogatory No. 3 — Boilerplate objection without specifying the
     vague term or quantifying the burden.
  2. Request for Production No. 7 — No documents produced though the
     Complaint references documents within this request.
  3. Rule 26.1 disclosure — No computation of damages provided.

Please supplement by [date]. If I do not hear from you, I will proceed
with a Motion to Compel and seek expenses under Rule 37. [Name]
```

## Motion to compel and sanctions — Rule 37

If consultation fails, move to compel under **Ariz. R. Civ. P. 37**. The
motion should:

1. **Identify the specific deficiencies** (which interrogatory / RFP /
   RFA / Rule 26.1 disclosure category, and why the response is
   inadequate).
2. **Attach** the requests and responses as exhibits.
3. **Certify the good-faith consultation** (and attach the conferral
   correspondence).
4. **Address each objection** on the merits.
5. **Request specific relief**: an order compelling responses by a date
   certain, plus an award of reasonable expenses.

### Sanctions ladder

- On a granted motion to compel, **Rule 37** authorizes an award of the
  reasonable **expenses, including attorney fees**, caused by the
  failure, unless the opposing position was substantially justified.
- For **disobedience of a discovery order**, Rule 37 escalates to
  stronger sanctions — up to striking pleadings, dismissal, or default
  judgment.
- Rule 37 also addresses the consequences of **failing to disclose under
  Rule 26.1** (exclusion of the undisclosed matter) and of failing to
  admit.

Verify the current subpart lettering against the verbatim Rule 37 text
in `az-law-references`.

## Composition

- For drafting the motion to compel: `az-draft-motion`
- For the supporting affidavit / declaration: `az-draft-declaration`
- For the notice / lodging of the motion: `az-draft-note`
- For statewide format: `az-statewide-format`
- For deadline arithmetic, the Rule 26.1 disclosure clock, and the
  scheduling-order cutoff: `az-deadlines`
- For the Justice Court streamlined discovery track: `az-justice-courts`
- For consumer-debt RFP / RFA banks and debt-buyer chain-of-title
  discovery strategy: `az-consumer-debt`

## References

- `references/interrogatory-templates.md` — Rule 33 uniform / non-uniform templates
- `references/rfp-templates.md` — Rule 34 templates
- `references/rfa-templates.md` — Rule 36 templates
- `references/initial-disclosure.md` — Rule 26.1 disclosure checklist
- `references/tier-limits.md` — Rule 26.2 Tier 1/2/3 thresholds and per-tier discovery limits
- `references/motion-to-compel.md` — Rule 37 scaffold
- `references/consultation-templates.md` — good-faith consultation / meet-and-confer templates
