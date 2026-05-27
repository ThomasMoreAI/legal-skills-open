---
name: regulatory-submission-summary
title: Regulatory Submission Summary
description: 'Produces structured summaries of regulatory submission packages (FDA NDAs, 510(k)s, BLAs, ANDAs, environmental permits, rate filings) for government approval processes. Distills clinical data, manufacturing information, compliance evidence, and supporting documentation into standardized overviews for regulatory reviewers, compliance teams, and executives. Use when summarizing submission packages, preparing regulatory filing overviews, or creating executive briefings on approval applications; trigger keywords: regulatory submission, NDA summary, 510(k) summary, BLA summary, filing overview, approval application, regulatory briefing, submission package.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/regulatory-submission-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [summarization, summary]
---

# Regulatory Submission Summary

Produces a structured summary of a regulatory submission package, enabling reviewers to quickly assess purpose, scope, supporting evidence, and compliance posture.

## Prerequisites

1. Primary submission documents — application form, cover letter, filing type identification.
2. Supporting technical data — clinical trials, safety/efficacy studies, engineering analyses, environmental or economic assessments.
3. Manufacturing/operational documentation — quality control, facility info, process descriptions.
4. Labeling or public-facing materials — proposed labels, consumer disclosures, service descriptions.
5. Agency correspondence — pre-submission meeting minutes, prior feedback, deficiency responses.
6. Regulatory pathway identification — NDA, 510(k), ANDA, BLA, environmental permit, rate case, etc.

## Output Structure / Process

### 1. Executive Overview

| Field | Content |
| --- | --- |
| Submitting Entity | Name, address, contact |
| Regulatory Body | FDA, EPA, FCC, state PUC, etc. |
| Submission Type | NDA, 510(k), BLA, ANDA, EIS, rate case, etc. |
| Submission Date | Date filed or to be filed |
| Requested Action | Approval, clearance, permit, authorization |
| Regulatory Framework | Statutory/regulatory basis with specific citations |
| Expedited Pathways | Breakthrough, fast track, priority review, waivers (if any) |

### 2. Subject Matter Description

- Product/device/substance/service identification (names, classifications, compositions).
- Intended use, target population, or scope of authorized operations.
- Key identifiers (NDC, device class, CAS number, facility ID as applicable).

### 3. Supporting Evidence Summary

Map each regulatory criterion to the evidence submitted:

| Approval Criterion | Evidence Submitted | Key Findings |
| --- | --- | --- |
| Safety | Study type, N= | Primary endpoints, results |
| Efficacy / Performance | Study type, N= | Primary endpoints, results |
| Manufacturing Quality | CMC data, GMP compliance | Key controls, validation status |
| Environmental / Public Impact | Assessment type | Conclusions, mitigation measures |

- Report statistical results with effect sizes, confidence intervals, and p-values.
- Flag novel aspects, first-in-class designations, or areas lacking established pathways.

### 4. Compliance Strategy

- Applicable statutes and regulations (cite specific sections).
- Guidance documents relied upon.
- Pre-submission interactions and how agency feedback was incorporated.
- Basis for any waiver, exemption, or special designation requests.

### 5. Review Timeline

| Milestone | Expected Date/Timeframe |
| --- | --- |
| Filing/acceptance review | |
| Substantive review period | |
| Information request window | |
| Advisory committee (if applicable) | |
| Public comment period (if applicable) | |
| Target action date | |

### 6. Submission Package Inventory

Number and briefly describe each major attachment/appendix:

1. **Module/Volume X** — Description
2. **Appendix A** — Description

### 7. Compliance Assessment

- [ ] Submission completeness relative to regulatory checklist
- [ ] Gaps or areas likely to trigger information requests
- [ ] Conditions or limitations that may attach to approval
- [ ] Post-approval commitments (REMS, Phase IV, monitoring, reporting)
- [ ] Ongoing compliance obligations

## Guidelines

- Use precise regulatory terminology; cite specific CFR sections, USC provisions, or agency guidance by name and number.
- Mark any citation that cannot be verified from source materials with `[VERIFY]`.
- Distinguish statistically significant from clinically meaningful results.
- Label interpretive conclusions vs. factual statements from the submission.
- Maintain jurisdiction awareness — FDA, EPA, FCC, and state agencies have distinct frameworks; do not conflate.
- For FDA submissions, follow the CTD (Common Technical Document) module structure where applicable.
- Flag regulatory risk areas transparently; do not minimize uncertainties.

## Troubleshooting

- **Missing pathway identification**: If the submission type is unclear, check the cover letter and application form first; flag ambiguity in the executive overview and mark `[VERIFY]`.
- **Incomplete evidence tables**: When study data is partial or not provided, note the gap explicitly rather than omitting the criterion row.
- **Multi-agency submissions**: If a product requires approval from multiple agencies (e.g., FDA + EPA), create separate executive overview and compliance strategy sections per agency.
- **Expedited pathway uncertainty**: If expedited designation status is claimed but not confirmed, note as "requested" vs. "granted" and mark `[VERIFY]`.

---

**Key changes from original:**

1. **Frontmatter**: Added `>-` multi-line description with explicit trigger keywords per spec; kept valid controlled-vocabulary tags.
2. **Section rename**: "Output Structure" → "Output Structure / Process" to match codebase convention (see `legal-research`, `client-advisory-summary`).
3. **Section rename**: "Review Process & Timeline" → "Review Timeline" (conciser).
4. **Added Troubleshooting section**: Required by the spec validation checklist but missing from the original.
5. **Trimmed prose**: Removed bracket placeholders from evidence table cells, tightened bullet formatting with terminal periods for consistency, removed the "Format for professional regulatory file inclusion" guideline (redundant with overall tone).
6. **Removed bold from prerequisite labels**: Aligns with the flat numbered-list style used in peer skills.
