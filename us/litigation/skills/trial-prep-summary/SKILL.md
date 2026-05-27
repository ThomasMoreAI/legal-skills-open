---
name: trial-prep-summary
title: Trial Preparation Summary
description: Generates a structured courtroom-ready trial preparation summary synthesizing procedural history, facts, legal issues, evidence, witnesses, and strategy into a quick-reference document. Trigger when preparing trial binders, pre-trial review documents, courtroom reference materials, or trial strategy memos in commercial litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/trial-prep-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [summarization, summary]
---

# Trial Preparation Summary

Synthesizes case materials into a single courtroom-ready reference organized for rapid access during examination, argument, and tactical decisions.

## Required Inputs

1. **Pleadings** — complaint, answer, counterclaims, amended pleadings
2. **Discovery** — interrogatory responses, RFP productions, RFA responses
3. **Depositions** — transcripts with page:line citations
4. **Expert reports** — opinions, methodology, bases
5. **Motions & orders** — dispositive motions, MILs, rulings
6. **Exhibit list** — pre-marked exhibits with Bates ranges
7. **Witness list** — anticipated witnesses for both sides

## Quick Start

1. Collect all inputs above
2. Build sections 1–9 below in order
3. Cite every assertion to exhibit #, depo page:line, or Bates range
4. Mark uncertain legal citations `[VERIFY]`
5. Use tables over prose throughout

## Output Sections

### 1. Case Overview

| Field | Content |
|-------|---------|
| Caption | Full case caption |
| Court / Judge | Court, department, judge |
| Trial date | Date(s), estimated duration |
| Causes of action | Claims/counterclaims with statutory or common-law basis |
| Burden of proof | Party bearing burden per claim/defense |
| Relief sought | Damages figures, equitable relief, fees |

### 2. Procedural History

Reverse-chronological table of significant docket entries:

| Date | Event | Order/Ruling | Impact on Trial |
|------|-------|--------------|-----------------|

Flag pending motions, unresolved discovery disputes, deferred evidentiary rulings, and approaching deadlines (pretrial conference, exhibit exchange, witness disclosure).

### 3. Factual Narrative

- **Chronology table** — date, event, source (exhibit #, depo cite), disputed/undisputed
- **Undisputed facts** — stipulated or established by RFA admissions
- **Disputed facts** — competing versions with supporting evidence for each side

### 4. Element Mapping

One table per claim/defense (repeat for multi-count cases):

| Element | Governing Law | Our Evidence | Their Evidence | Strength (1–5) |
|---------|--------------|--------------|----------------|-----------------|

Per claim, also note: jury instruction references, standard of proof, key distinguishing case law.

### 5. Evidence Inventory

| Exhibit # | Description | Auth. Witness | Foundation Issues | Anticipated Objections | MIL Status |
|-----------|-------------|---------------|-------------------|----------------------|------------|

Flag exhibits needing business-records foundation (FRE 803(6)), expert authentication, or chain-of-custody proof.

### 6. Witness Summaries

Per witness:

| Field | Content |
|-------|---------|
| Name / Role | |
| Calling party | Plaintiff / Defendant / Both |
| Key topics | |
| Favorable depo cites | Page:line |
| Impeachment material | Prior inconsistent statements, bias, interest |
| Availability | Voluntary / subpoenaed / issues |

Separate fact witnesses from experts. For experts add: opinions offered, methodology, Daubert challenge status.

### 7. Motions in Limine Tracker

| Motion | Filed By | Subject | Status | Impact if Granted | Impact if Denied |
|--------|----------|---------|--------|-------------------|-----------------|

### 8. Damages / Relief Analysis

- **Damages model** — methodology, supporting docs, expert basis
- **Damages table** — category, amount claimed, evidence, vulnerabilities
- **Equitable relief** — terms sought, legal standard, factual predicates
- **Fees/costs** — contractual or statutory basis, documented amounts

### 9. Strategic Assessment

- **Case theory** — one-paragraph narrative for the fact-finder
- **Strongest arguments** — ranked with supporting evidence
- **Key vulnerabilities** — candid weaknesses with mitigation strategies
- **Anticipated opposing themes** — their narrative and rebuttal points
- **Trial flow** — suggested witness order, examination priorities
- **Contingencies** — if-then scenarios for adverse rulings or unexpected testimony

## Pitfalls

- **Unsourced assertions** — every fact must cite exhibit #, depo page:line, or Bates range
- **Stale citations** — mark all legal citations `[VERIFY]` unless confirmed current and jurisdictionally on-point
- **Advocacy creep** — maintain neutral analytical tone; flag weaknesses candidly
- **General legal summaries** — skip principles the attorney already knows; focus on case-specific application
- **Missing Daubert flags** — always note whether a reliability challenge is pending or viable for expert testimony
