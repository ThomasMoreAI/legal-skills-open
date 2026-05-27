---
name: expert-witness-impeachment
title: Expert Witness Impeachment Analysis
description: Analyzes expert witness materials (reports, depositions, CVs, publications) to identify inconsistencies, opinion drift, and methodological failures for impeachment. Produces a prioritized inconsistency register, cross-examination questions, and Daubert/Frye challenge assessment. Use when challenging expert reliability or credibility during discovery, pre-trial, or trial in commercial litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-witness-impeachment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis]
---

# Expert Witness Impeachment Analysis

Systematically compares expert materials to surface contradictions and methodological failures that support cross-examination, exclusion motions, or weight challenges.

## Quick Start

1. Collect: current report, supplemental/rebuttal reports, deposition transcripts, CV, published works, prior case testimony
2. Confirm procedural posture: phase (discovery / pre-trial / trial) and admissibility standard (Daubert or Frye)
3. Run analysis across all five dimensions below
4. Produce outputs in order: Register → Patterns → Cross-Exam → Admissibility → Motion Summary

## Analysis Dimensions

| Category | What to Find |
|---|---|
| **Opinion Changes** | Modified, reversed, or newly qualified conclusions across documents |
| **Methodological Inconsistencies** | Different approaches, data sets, or protocols without explanation |
| **Factual Contradictions** | Inconsistent statements about underlying facts or reviewed evidence |
| **Credential Discrepancies** | Qualifications or publications stated differently across documents |
| **Unsupported Conclusions** | Testimony exceeding the report's scope or lacking methodological basis |

## Output Structure

### 1. Inconsistency Register

For each finding:

- **ID**: sequential number
- **Category**: from table above
- **Materiality**: High / Medium / Low (effect on ultimate opinion)
- **Source A**: [document, page, line] — verbatim quote
- **Source B**: [document, page, line] — verbatim quote
- **Delta**: one-sentence contradiction description
- **Expert explanation offered**: yes/no (summarize if yes)

### 2. Pattern Assessment

- Group related inconsistencies to distinguish systemic unreliability from isolated error
- Flag temporal patterns: opinions strengthening/weakening without new data, or shifting after opposing challenges
- Separate bias indicators from legitimate opinion evolution

### 3. Cross-Examination Blueprint

For each High/Medium finding:

- 2–4 sequenced questions using the expert's own words
- Explicit target admission or concession
- Exhibit reference for confrontation

### 4. Admissibility Challenge Assessment

Evaluate whether findings support:

- **Daubert**: methodology unreliable, untested, lacks peer review, high error rate, or not generally accepted (federal / Daubert-state courts)
- **Frye**: methodology not generally accepted in relevant scientific community (Frye-state courts)
- **Weight-only**: inconsistencies affect credibility but not threshold admissibility

### 5. Motion Practice Summary

One paragraph per significant inconsistency cluster, formatted for direct use in an exclusion or limitation motion, with embedded record citations.

## Pitfalls and Checks

- **Cite exactly**: every finding needs document name, page, line. Quote verbatim alongside any paraphrase.
- **Materiality conservatism**: peripheral credential minutiae = Low; opinion reversals on dispositive issues = High.
- **Jurisdiction check**: confirm Daubert vs. Frye before drafting the admissibility section. Federal courts and most states use Daubert; a minority retain Frye.
- **Scope discipline**: flag where testimony exceeds disclosed opinions — independent exclusion grounds under FRCP 26(a)(2). Verify jurisdiction-specific rules.
- **Privilege flag**: if correspondence appears to be work product or privileged, flag for counsel review — do not quote.
- **No advocacy**: present findings neutrally. Characterization is counsel's role.

---

**Key changes made:**

- **Description**: tightened from 3 sentences to a compact third-person summary with clear trigger guidance
- **Removed Prerequisites**: folded into a streamlined Quick Start checklist (4 steps)
- **Added Quick Start**: gives the core workflow at a glance
- **Inconsistency Register**: converted from code block to bullet list — more idiomatic for skills, same information
- **Removed prose padding**: eliminated "Examine all materials across these five categories" lead-in and similar filler
- **Renamed Guidelines → Pitfalls and Checks**: aligns with best-practice section naming
- **Reduced from 80 lines to ~68 lines**: more token-efficient while preserving all domain-critical content
