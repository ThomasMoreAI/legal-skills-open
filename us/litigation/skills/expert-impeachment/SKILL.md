---
name: expert-impeachment
title: Expert Witness Impeachment
description: Surfaces inconsistencies, opinion shifts, methodological flaws, and credential discrepancies across expert reports, transcripts, CVs, and publications for impeachment, cross-examination, and exclusion motions. Trigger when the user references expert impeachment, expert report analysis, Daubert or Frye challenges, deposition prep against an expert, or credibility attacks on opposing expert witnesses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-impeachment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis]
---

# Expert Witness Impeachment

Builds a citation-ready inconsistency map to challenge expert credibility, reliability, and admissibility.

## Quick Start

1. Collect all expert materials: reports, supplements, rebuttals, deposition/trial transcripts, declarations, CV, publications, prior testimony, data/appendices.
2. Confirm page/line or Bates-citable versions of each source.
3. Identify the case theory, key disputed issues, and governing admissibility standard (Daubert, Frye, or local rule).
4. Proceed through the workflow steps below in order.

## Workflow

### 1. Source Inventory

Build a table of every source document with columns: Source, Date, Type, Citation Format, Notes.

### 2. Opinion Chronology

Map the expert's opinions over time with columns: Date, Document/Testimony, Key Opinion Statement, Cite. Track how positions evolved across filings.

### 3. Inconsistency Log

For each inconsistency found, log:
- **ID** — unique identifier
- **Category** — one of: `Opinion Change`, `Methodology`, `Facts/Assumptions`, `Credentials`, `Scope Creep`, `Prior Testimony Conflict`, `Publication Conflict`, `Math/Calculation Error`
- **Statement A** and **Statement B** — exact quotes with pinpoint cites
- **Delta** — nature of the conflict
- **Materiality** — H/M/L
- **Admissibility Impact** — Reliability, Fit, Qualifications, or combination
- **Explanation Offered** — any justification on record
- **Cross-Exam Hook** — suggested line of questioning

### 4. Methodology Audit

- Identify each dataset, test, model, or protocol relied upon.
- Confirm consistent application across reports and testimony.
- Flag changes in assumptions, variables, or inputs without explanation.
- Flag conclusions not supported by stated method.
- Note departures from the expert's own published standards or prior testimony.
- Record concessions on limitations, error rates, or missing data.

### 5. Credentials & Bias Check

Verify each claimed credential. Log: Claim, Source, Verification Status, Conflict, Materiality. Flag financial bias, repeat retention patterns, and advocacy history.

### 6. Materiality & Strategy Ranking

Rank each inconsistency ID by: relevance to core issues, expected defense, backfire risk, and recommended use (Motion / Cross / Both). Prioritize contradictions tied to disputed issues or damages.

### 7. Cross-Examination Questions

For each high-priority ID, draft 3–6 tight questions following this pattern:
- Lock in Statement A (cite)
- Confirm Statement B (cite)
- Force the inconsistency
- Tie to reliability/fit
- Obtain concession on impact to opinion

### 8. Admissibility Analysis

- Map high-priority inconsistencies to governing standard elements (reliability, relevance/fit, qualifications).
- Note curative explanations and whether the record supports them.
- Draft a motion-ready paragraph per high-priority ID.

## Pitfalls

- Always use exact quotes with pinpoint citations; paraphrasing undermines impeachment value.
- Treat evolving opinions as impeachment only when unsupported by new data or analysis.
- Do not assume Daubert applies — verify the governing standard and local rules.
- Separate peripheral inconsistencies from motion-worthy defects; over-inclusion dilutes impact.
- Flag any legal citations or standards with `[VERIFY]` if uncertain.
- Avoid character attacks; focus strictly on record-supported reliability and fit.
