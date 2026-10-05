---
name: counsel-research-draft-pipeline-dmang69
title: Counsel Research & Draft Pipeline
description: Use when researching and drafting BC legal documents.
author: dmang69
author_url: https://github.com/dmang69/bc-legal-ai/tree/master/skills/counsel-research-draft-pipeline
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: litigation
language: en
sources:
- title: Counsel Framework
  path: references/counsel-framework.md
---

# Counsel Research & Draft Pipeline

## Overview

Mandatory production pipeline for elite BC superior-court / tribunal research and
drafting. Implements the operational half of the counsel mandate; full professional
framework lives in `references/counsel-framework.md` (synced from monorepo
`skills/supreme-court-civil-counsel/counsel-framework.md`).

**Trigger detail (full):** Research and summarize applicable authorities (verify
every citation) → Analyze facts against governing principles → Address
counterarguments and weaknesses → Draft in court-ready *format* → Pre-finalization
quality review (logic, chronology, citations, procedure, evidence, grammar,
formatting, cross-refs).

**Not legal advice.** Outputs are legal information and drafting support.
Default label every work product:

> **WORKING DRAFT — HUMAN VERIFICATION REQUIRED BEFORE FILING**

unless the human release gate in Step 5 has expressly passed.

## When to Use

- User asks for research + analysis + draft of any legal document
- Petitions, applications, responses, affidavits, briefs, submissions, BOAs
- Decision review memos, issue matrices, written argument
- Any task that would otherwise skip verification or counterargument work

**Don’t use for:** pure product-engineering on the monorepo (use `bc-legal-ai-product`);
casual Q&A that is not heading toward a citable work product.

**Companion loads (BC RTB → JR):**
`legal-document-preparation` + monorepo `bc-judicial-review-guide` +
`supreme-court-civil-counsel` (+ tenancy / `canlii-boa-builder` as needed).

## Absolute rules

1. Never invent facts.
2. Never present unverified authority as settled.
3. Do not claim certainty where the law is unsettled.
4. Identify assumptions, missing evidence, and issues requiring verification.
5. Every material FACT needs a record pinpoint or is labeled **ALLEGATION**.
6. Unverified citations = research leads only — never props for conclusions,
   deadlines, or “court-ready” claims.
7. Respect locked product corrections (below).

### Locked design corrections

| # | Rule |
|---|------|
| 1 | Consent ≠ privilege |
| 2 | Consent withdrawal ≠ unconditional deletion (PIPA; holds separate) |
| 3 | Forms: **66** petition · **67** response · **32** interlocutory · **33** app response · **109** affidavit |
| 4 | JR clock: **60 days from issuance** (ATA s.57 when incorporated); s.57(2); **alternatives** when uncertain |
| 5 | Honest encryption posture only |
| 6 | RTB published archive incomplete; absence ≠ non-existence |

### Mandatory analytical framework (strict separation — label everything)

| Category | Description |
|----------|-------------|
| **FACT** | Evidence-supported, verified, documented findings drawn directly from the record |
| **ALLEGATION** | Asserted but unproven claims requiring evidentiary substantiation before reliance |
| **LEGAL ARGUMENT** | Formal submissions grounded in statute, binding precedent, and common law |
| **INFERENCE** | Reasoned conclusions logically and defensibly drawn from established evidence |
| **ASSUMPTION** | Unverified propositions explicitly flagged as requiring investigation |
| **PROCEDURAL HISTORY** | Chronological record of all prior proceedings and interlocutory steps |
| **RECOMMENDATION** | Advisory positions identified as professional guidance subject to independent counsel review |

Prefix labels:

`[FACT]` · `[ALLEGATION]` · `[LAW]` · `[ARGUMENT]` · `[INFERENCE]` · `[ASSUMPTION]` ·
`[PROCEDURAL HISTORY]` · `[RECOMMENDATION]` · `[REMEDY]` · `[CITATION UNVERIFIED]` ·
`[LAW CURRENCY UNVERIFIED]` · `[INDEPENDENT COUNSEL RECOMMENDED]`

Also keep **FACT / LAW / ARGUMENT / ANALYSIS / REMEDY** visibly separated in structure.

**Boundary (always):** legal information and drafting support — not legal advice. SRL-primary use: flag independent counsel; never present unverified authority as settled. Full role/competencies: `references/counsel-framework.md`.

---

## Five-step pipeline (do not skip or reorder)

### Step 1 — Research and summarize applicable authorities (verify every citation)

**Do**

1. Confirm forum and jurisdiction before diving into merits.
2. Map governing statutes/regulations (BC Laws / Justice Canada), Rules/forms,
   practice directions, limitation / JR clock candidates.
3. Pull case law via CanLII hierarchy: binding → persuasive → guidance.
4. For **every** authority you will rely on:
   - Verify **existence** and citation format
   - Record: jurisdiction, court/tribunal, date, neutral citation, URL, **access date**, pinpoint, treatment/history
   - State the legal principle in one tight sentence
   - Mark `[AUTHORITY VERIFIED — source, access date, pinpoint, treatment]` **or**
     `[CITATION UNVERIFIED — do not rely on or file]`
5. Produce an **Authorities Summary** table before drafting prose:

| Authority | Citation | Pinpoint | Principle | Application lean | Status |
|-----------|----------|----------|-----------|------------------|--------|

**Statutes:** operative text only from **BC Laws** (BC) or Justice Canada (federal).
CanLII statute mirrors are research aids only.
**Cases:** CanLII/official reporters. Automated CanLII case PDF fetch is blocked
(DataDome) — mark download/verification path; never fabricate the text.

**Done when:** every authority that will appear in the draft is either VERIFIED with
pinpoint or explicitly UNVERIFIED and quarantined from reliance; JR/limitation
candidates listed if posture engages them.

### Step 2 — Analyze the facts against the governing legal principles

**Do**

1. Extract facts **only** from the record with pinpoints (transcript timestamps,
   affidavit paras, exhibit tabs, decision paragraphs).
2. Build chronology + PROCEDURAL HISTORY; list missing record pieces.
3. State issues, burden/standard of proof, and standard of review **if** JR/appeal:
   - RTB / ATA s.58 path: **patent unreasonableness** for typical expertise-bound
     fact/law; **correctness** for procedural fairness — do **not** default-label
     RTB as “Vavilov reasonableness.”
4. For each issue: principle (from Step 1) → elements → map FACT/INFERENCE to each
   element → gaps (ASSUMPTION/ALLEGATION).
5. Separate analysis block from advocacy: reader must see what is established vs
   what is argued.

**Done when:** every live issue has a principle → facts/record → gap map; no orphan
factual claims without source or ALLEGATION tag.

### Step 3 — Address potential counterarguments and weaknesses

**Do**

1. Steelman the strongest opposing positions (respondent / tribunal / landlord /
   Crown / adverse party).
2. For each: concede what must be conceded; distinguish adverse authority; identify
   evidentiary soft spots (hearsay, attribution, credibility-only attacks, new
   evidence on JR).
3. Rate risk honestly (especially RTB JR high bar).
4. Note costs, mootness, adequate alternative remedy, delay, record-bound limits.
5. Flag `[INDEPENDENT COUNSEL RECOMMENDED]` when triggers fire (possession, money,
   opposing counsel, stay urgency, appeal clocks, Charter, privilege, multi-party).

**Done when:** draft will not rely on a proposition that collapses under the best
   available counter without the counter having been named and handled.

### Step 4 — Draft the requested document in court-ready *format*

**Format** means structure, style of cause, forms, and professional organization —
**not** a unilateral claim that the product is filing-ready.

**Standard spine (adapt to form):**

Title → Jurisdiction → Style of Cause → Issues → Facts → Chronology →
Applicable Law → Analysis → Supporting Authorities → Counterarguments →
Remedy Requested → Conclusion → Assumptions & Gaps → Recommendations → Disclaimer

**Form locks (BCSC):** petition **66** · response **67** · interlocutory **32** ·
application response **33** · affidavit **109**. Never commence a petition as 67.

**Deliverable types:** notices of application, petitions, responses, replies,
affidavits, briefs, memoranda, factums, written submissions, oral scripts, BOAs
(user prefers **12-field** authorities tables for complex JR), BODs, chronologies,
issue matrices, filing checklists.

**Docx on this Windows host:** build with `python-docx` via system Python 3.14
(not Hermes venv); Windows paths (`G:\My Drive\...`); never `write_file` a fake `.docx`.
See `legal-document-preparation` for path details.

Every draft header/footer or closing band includes WORKING DRAFT (or human-gate
language if Step 5 passed) plus the standard disclaimer.

**Done when:** requested instrument exists in the correct form/shape with labels,
pins, authorities summary, counters, remedy, and disclaimer — still WORKING DRAFT
until Step 5 human gate.

### Step 5 — Pre-finalization quality review

Before delivering as complete (and **before any court-ready claim**), run **all** checks:

| Gate | Check |
|------|--------|
| Logic | Internal consistency; no contradictory positions without explanation |
| Chronology | Dates ordered; no impossible sequences; gaps listed |
| Citations | Existence, format, pinpoints; VERIFIED vs UNVERIFIED quarantine held |
| Procedure | Correct form; forum; service theory; fees/registry notes; JR clock / alternatives |
| Evidence | Every material factual assertion has record support **or** ALLEGATION tag |
| Grammar | Plain professional English; SRL-clear where user is SRL |
| Formatting | Style of cause, tabs/exhibits, numbering, court-acceptable layout |
| Cross-refs | Internal paragraph/tab/exhibit references resolve |
| Locks | Corrections #1–#6 respected; no consent/privilege conflation; no archive-completeness myth |
| Counsel flag | Independent counsel marker present when warranted |
| Disclaimer | Standard not-advice band present |

### Court-ready / filing-ready human release gate

Do **not** strip WORKING DRAFT or call a product court-/filing-ready unless a
**qualified human** confirms:

- record support + pinpoints for every material factual assertion
- current or point-in-time enactments from official sources
- case existence, pinpoints, hierarchy, treatment
- current Rules, practice directions, forms, fees, registry practice, service, deadlines
- privilege, confidentiality, redaction, conflict review
- relief, jurisdiction, evidence foundation, formatting, internal cross-references

Otherwise retain: **WORKING DRAFT — HUMAN VERIFICATION REQUIRED BEFORE FILING**.

**Done when:** checklist above is completed item-by-item in the delivery note
(pass / fail / N/A with reason); failed items block any filing-ready language.

---

## Mandatory considerations (every matter)

Run or explicitly N/A:

1. **Jurisdictional analysis** — governing court/tribunal; territorial and subject-matter jurisdiction; privative clauses; statutory grants; forum selection. **Resolve before merits.**
2. **Applicable legislation** — all relevant statutes, regulations, subordinate legislation, Rules of Court, limitation periods, transitional provisions
3. Rules of Court / tribunal rules + **correct forms**
4. Case law hierarchy (binding vs persuasive)
5. Procedural fairness / natural justice
6. Standard of review (if engaged) — RTB: ATA s.58 map
7. Burden / standard of proof; admissibility
8. Remedies / enforcement / costs
9. Public interest (if engaged)
10. Limitation periods + JR s.57 candidates/alternatives

## Decision-review spot list

When the task is reviewing a decision, scan for each applicable defect:

procedural unfairness · jurisdictional error · error of law · error of fact ·
mixed fact and law · bias (actual / RAP) · patent unreasonableness or reasonableness
(as standard requires) · adequacy of reasons · failure to consider material evidence ·
ignoring binding precedent · misapplication of legislation · improper burden shift ·
procedural irregularity · natural justice · fettering / abuse of discretion

## Delivery note (append to every completed pipeline run)

```
PIPELINE STATUS
1 Research/authorities: complete | gaps: …
2 Fact–law analysis: complete | gaps: …
3 Counterarguments: complete | residual risks: …
4 Draft: [document type + path] | label: WORKING DRAFT | form: …
5 Quality review: [pass/fail per gate]
Court-ready human gate: NOT PASSED | PASSED by [human] on [date]
[INDEPENDENT COUNSEL RECOMMENDED]: yes/no — reason
Disclaimer: included
```

### Standard disclaimer

> AI-assisted legal information and drafting support only — **not legal advice**.
> No solicitor–client relationship. Verify statutes on BC Laws, Rules/forms on
> official court sites, and cases on CanLII before filing. Seek licensed counsel
> when marked `[INDEPENDENT COUNSEL RECOMMENDED]`.

## Reference

Full professional mandate, competencies, and analytical framework detail:
**`references/counsel-framework.md`**

Monorepo operational skill (product chat runtime):
`D:\AI legal\bc-legal-ai\skills\supreme-court-civil-counsel\`
JR doctrine lock: `...\skills\bc-judicial-review-guide\`

## Common pitfalls

1. Jumping to draft before verified authorities table exists.
2. Analysis that restates facts without applying elements of the legal test.
3. No steelman counter — one-sided briefs get destroyed in chambers.
4. Calling format polish “court-ready” without the human release gate.
5. Form 67 as originating petition; Vavilov-default on RTB; single JR date when finality unclear.
6. Invented pinpoints or CanLII-only statute text for filing.
7. Skipping the delivery note so the user cannot see what failed review.

## Verification checklist

- [ ] Steps 1→5 executed in order
- [ ] Authorities summary present; each relied cite VERIFIED or quarantined
- [ ] Facts pinned or labeled ALLEGATION
- [ ] Counterarguments section present
- [ ] Correct form / document spine
- [ ] Pre-finalization gates all checked
- [ ] WORKING DRAFT retained unless human gate documented
- [ ] Disclaimer + counsel flag as required
- [ ] Locks #1–#6 respected
- [ ] Pointer to counsel-framework honored for depth questions
