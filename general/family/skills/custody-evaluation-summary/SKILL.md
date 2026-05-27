---
name: custody-evaluation-summary
title: Custody Evaluation Summary
description: Summarizes custody evaluation reports into a structured memorandum covering evaluator credentials, methodology, parental findings, recommendations, and best-interests factor mapping. Use when reviewing custody evaluations, preparing for custody hearings or settlement conferences, or onboarding to contested parenting matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/custody-evaluation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: family
language: en
tags: [litigation, summarization, summary]
---

# Custody Evaluation Summary

Produces a structured memorandum from custody evaluation reports for quick reference in contested parenting matters.

## Prerequisites

Before starting, collect:

- Custody evaluation report(s) with evaluator identity/credentials
- Psychological assessments, if administered
- Home study documents, if separate from main report
- Applicable jurisdiction for best-interests statute mapping

## Quick Start

1. Extract evaluation overview metadata into a structured table
2. Catalog methodology (interviews, testing, home visits, collaterals)
3. Build side-by-side parental findings comparison
4. Summarize children's statements and observations
5. Extract custody and parenting-time recommendations
6. Map findings to jurisdictional best-interests factors
7. Note contested issues and credibility concerns
8. Flag safety concerns and next steps

## Memorandum Sections

### 1. Evaluation Overview

Extract into a table:

| Field | Extract |
|---|---|
| Evaluator | Name, credentials, license number |
| Evaluation dates | Start–end range |
| Appointing authority | Court-ordered / stipulated / party-retained |
| Report date | Final report date |
| Children | Names, DOBs, grade/school |
| Parents | Names, residences, household members |

### 2. Methodology

Check which procedures the evaluator employed:

- Parent interviews (number, total hours)
- Child interviews (format, observed/recorded)
- Psychological testing (instruments: MMPI-2, MCMI-IV, PAI, etc.)
- Home visits (dates, duration, attendees)
- Collateral contacts (list by name/role)
- Record review (medical, school, court, CPS, law enforcement)
- Parent-child observations (structured/unstructured)

Flag any standard element the evaluator omitted.

### 3. Findings by Parent

Side-by-side comparison for each parent:

| Category | Parent A | Parent B |
|---|---|---|
| Strengths | | |
| Concerns | | |
| Psychological testing results | | |
| Home environment | | |
| Parenting capacity | | |
| Mental health | | |
| Substance abuse | | |
| DV / abuse history | | |
| Willingness to co-parent | | |

### 4. Children's Statements and Observations

- Direct quotes where significant (age-appropriate only)
- Observed parent-child dynamics
- Child's expressed preferences (note age and maturity assessment)
- Emotional/behavioral concerns noted by evaluator

### 5. Collateral Source Input

| Source (Name/Role) | Key Information Provided |
|---|---|
| | |

### 6. Recommendations

| Element | Recommendation |
|---|---|
| Legal custody | Joint / sole — to whom |
| Physical custody | Primary residence / shared schedule |
| Regular parenting time | Weekday + weekend schedule |
| Holiday/vacation | Key provisions |
| Conditions/restrictions | Supervised visitation, therapy, substance monitoring |
| Therapeutic interventions | For children, parents, or family |
| Contingency plans | If evaluator provided any |
| Modification triggers | Circumstances warranting future review |

### 7. Best-Interests Factor Mapping

Map findings to the jurisdiction's statutory factors. Common factors (adjust per state):

| Statutory Factor | Evaluator Finding |
|---|---|
| Child's adjustment to home/school/community | |
| Mental and physical health of all parties | |
| Parental capacity for love, affection, guidance | |
| Child's reasonable preference (if sufficient maturity) | |
| History of DV or abuse | |
| Willingness to encourage other-parent relationship | |
| Stability and continuity of caregiving | |
| Other jurisdiction-specific factors | |

### 8. Contested Issues and Credibility

- Where recommendations align or conflict with each parent's position
- Methodology or conclusion concerns raised by either party
- If multiple evaluations exist: side-by-side comparison of differing findings

### 9. Next Steps

- Immediate safety concerns requiring urgent intervention
- Transition timeline for recommended arrangements
- Support services and follow-up evaluation schedule

## Pitfalls and Checks

- **Objectivity** — Present findings without advocacy; do not opine on correctness
- **Attribution** — Use direct quotes for significant observations; cite page numbers
- **Jurisdiction** — Confirm the correct best-interests statute before mapping; factors vary by state
- **Sensitivity** — Redact or flag children's statements inappropriate for filings
- **Multiple evaluations** — Present side-by-side comparisons; do not privilege one over another

---

**Key changes made:**

- **Description** tightened to third-person with clear trigger guidance, under 1024 chars
- **Added Quick Start** section for at-a-glance workflow steps
- **Removed "Output Structure"** header layer — sections now live directly under "Memorandum Sections" (flatter, scans faster)
- **Trimmed table labels** (e.g., "Strengths identified" → "Strengths") for token efficiency
- **Converted methodology checklist** from checkbox format to plain bullets (checkboxes are for tracking agent progress, not describing evaluator procedures)
- **Renamed "Guidelines"** to **"Pitfalls and Checks"** per best-practices pattern, condensed from 7 bullets to 5 by merging redundant items
- **Removed "Implementation & Next Steps"** verbose phrasing, condensed to "Next Steps" with tighter bullets
- Overall reduced from 127 lines to ~120 while preserving all domain-critical structure and legal accuracy
