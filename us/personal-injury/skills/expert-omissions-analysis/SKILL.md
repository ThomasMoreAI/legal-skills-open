---
name: expert-omissions-analysis
title: Expert Omissions Analysis
description: Analyzes expert witness reports against complete medical record sets to identify omissions, bias patterns, and methodology gaps. Generates impeachment-ready reports with pin-cited findings and strategic recommendations. Triggers when the user needs to review opposing expert reports, prepare cross-examination, support Daubert/Frye motions, or retain rebuttal experts in personal injury or medical malpractice litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-omissions-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [analysis, litigation]
---

# Expert Omissions Analysis

Cross-references expert materials against the full medical record set to surface omitted records, classify their impact, and produce a structured impeachment report.

## Prerequisites

- **Complete medical record set** — Bates-stamped or indexed, all discovery-produced records
- **Expert materials** — report(s), deposition transcript(s), CV, supplemental declarations
- **Expert's materials-reviewed list** — extracted from report or deposition
- **Case chronology** — treatment timeline, injuries, key medical events

## Workflow

### 1. Inventory and Cross-Reference

Build a comparison matrix with columns: Record ID/Bates range, date of service, provider/facility, record type, cited by expert (Yes/No/Partial), and expert cite location (report page or depo page:line).

Flag every record where cited = No or Partial.

### 2. Classify Omissions

Assign priority to each flagged record:

| Priority | Criteria |
|---|---|
| **Critical** | Contradicts opinion, shows alternative causation, or reveals undisclosed pre-existing condition |
| **High** | Fills chronology gap or documents unaddressed treatment decisions |
| **Moderate** | Qualifies or weakens conclusions |
| **Low** | Cumulative or unlikely to affect opinion foundation |

### 3. Evaluate Methodology

Assess the expert's review process:

- Did the expert provide a complete materials-reviewed list?
- Does the expert's chronology match the actual medical timeline?
- Are factual assertions contradicted by records the expert claims to have reviewed?
- Did the expert acknowledge and explain gaps?
- Does the methodology satisfy Daubert/Frye reliability factors?

### 4. Identify Bias Patterns

Flag systematic omission patterns:

- Omissions cluster around records supporting opposing theory
- Pre-existing conditions consistently excluded
- Unfavorable imaging/labs ignored while favorable ones cited
- Selective quotation (partial citation)
- Temporal gaps obscuring intervening causes

### 5. Generate Report

Structure output as:

**I. Executive Summary** — total records, count not cited, critical/high omission count, key finding (1–2 sentences)

**II. Omissions Table** — matrix from Step 1 filtered to omitted records, sorted by priority

**III. Critical Omissions Detail** — for each Critical/High item: omitted record ID, content summary, expert's statement (quote + cite), impact on opinion foundation

**IV. Methodology Deficiencies** — Step 3 findings with supporting citations

**V. Bias Pattern Analysis** — Step 4 patterns with statistical support where available

**VI. Strategic Recommendations** — cross-examination questions (numbered, pin-cited), Daubert/Frye challenge points, rebuttal expert focus areas, deposition follow-up topics if discovery is ongoing

## Pitfalls and Checks

- **Pin-cite everything** — every assertion references a Bates number, depo page:line, or report page
- **Do not overstate minor gaps** — flag low-priority items but distinguish them from genuine impeachment material
- **Note defensible omissions** — record may be cumulative or irrelevant to the specific opinion rendered
- **Daubert factors**: testability, peer review, error rate, general acceptance, fit to facts [VERIFY: *Daubert v. Merrell Dow Pharmaceuticals*, 509 U.S. 579 (1993)]
- **Frye jurisdictions**: standard is general acceptance only; flag when applicable [VERIFY: *Frye v. United States*, 293 F. 1013 (D.C. Cir. 1923)]
- **Adapt for either side** — plaintiff (challenging defense IME expert) or defense (challenging treating physician or plaintiff's retained expert)
- **Do not render medical opinions** — identify what records say and what the expert missed, not whether the medical conclusion is correct
