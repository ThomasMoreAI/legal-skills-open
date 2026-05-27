---
name: witness-summary
title: Witness Statement Summary
description: Generates structured summaries of witness statements for litigation, extracting chronological narratives, key facts, credibility indicators, and evidentiary value. Use when summarizing depositions, declarations, affidavits, or witness testimony during discovery, pre-trial, or trial preparation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/witness-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Witness Statement Summary

Produces a structured, reference-ready summary of witness statements for case preparation, deposition planning, and trial strategy.

## Inputs

1. **Witness statement(s)** — transcripts, declarations, affidavits, or deposition excerpts
2. **Case context** (if available) — claims at issue, parties, key disputed facts
3. **Related exhibits** (if available) — documents referenced in the statement

## Quick Start

For each witness statement, produce sections 1–7 below in order. Preserve factual specificity throughout — never generalize away dates, amounts, or names. Quote significant language verbatim with transcript/paragraph citations.

## Output Sections

### 1. Executive Summary

| Field | Content |
|---|---|
| Witness name | Full name, role (party / fact witness / expert) |
| Relationship to case | Connection to parties and events |
| Statement type | Declaration, deposition, interview, affidavit |
| Date of statement | When given; date(s) of events described |
| Bottom line | 2–3 sentences: what this witness establishes and strategic significance |

### 2. Witness Background

- Biographical details relevant to credibility or weight
- Relationship to parties
- Basis of knowledge (percipient, expert, custodian)
- Prior involvement in related proceedings

### 3. Chronological Fact Narrative

| Date/Time | Location | Event/Observation | Certainty | Corroboration |
|---|---|---|---|---|
| Specific date | Where | What witness describes | High / Hedged / Uncertain | Supporting or conflicting evidence |

- Flag hedging language verbatim ("I believe," "to the best of my recollection")
- Note temporal gaps the witness cannot account for

### 4. Key Evidentiary Points

- **Admissions** — statements against interest or acknowledging opposing elements
- **Corroborations** — alignment with other witnesses or documents
- **Contradictions** — conflicts with other accounts, documents, or this witness's prior statements
- **Unique facts** — information only this witness provides

### 5. Admissibility Concerns

Flag each issue with the governing rule:

| Issue | Detail | Rule |
|---|---|---|
| Hearsay | Quote the statement-within-a-statement | FRE 801–807 |
| Opinion/speculation | Lay opinion exceeding scope | FRE 701–702 |
| Authentication gaps | Referenced docs not yet authenticated | FRE 901 |
| Privilege risk | Attorney-client or work product implications | — |
| Character/propensity | Testimony triggering propensity issues | FRE 404 |

### 6. Credibility Assessment

| Factor | Observation |
|---|---|
| Internal consistency | Contradictions within the statement |
| External consistency | Alignment with documentary/physical evidence |
| Bias/motive | Financial interest, party relationship, litigation motivation |
| Demeanor indicators | Certainty, qualifications, volunteered vs. elicited |
| Impeachment material | Prior inconsistent statements, convictions (FRE 609), bias |

### 7. Strategic Assessment

- **Strengths** — what testimony establishes favorably
- **Vulnerabilities** — cross-examination and rebuttal lines
- **Recommended follow-up** — additional discovery, corroborating evidence, deposition topics

## Multi-Witness Sets

When summarizing multiple witnesses, add a **Conflict Matrix** cross-referencing disputed facts across witnesses. Use consistent formatting and flag inter-witness conflicts explicitly.

## Pitfalls

- **Generalizing facts** — preserve all dates, amounts, names, and sequences exactly
- **Missing hedging language** — always quote qualifiers verbatim; they affect evidentiary weight
- **Unreferenced exhibits** — mark documents referenced but not provided as **[NOT REVIEWED]**
- **Editorializing** — keep factual sections neutral; reserve opinion for credibility and strategic sections
- **Jurisdiction assumptions** — default to U.S. federal rules; adapt when jurisdiction is specified

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not in the spec), tightened `description` with clearer trigger guidance
- **Structure**: Reorganized into Quick Start → Output Sections → Pitfalls pattern per best practices
- **Conciseness**: Removed the separate "Guidelines" prose section; distilled rules into a "Pitfalls" checklist and embedded key instructions in Quick Start
- **Multi-witness**: Extracted from Guidelines into its own short section for discoverability
- **Token savings**: Trimmed redundant wording across tables and bullet points while preserving all domain-accurate legal content (FRE rules, credibility factors, evidentiary categories)
