---
name: expert-witness-omissions
title: Expert Witness Medical Records Omissions Analysis
description: Identifies medical records an expert witness failed to review, cite, or address by cross-referencing the expert's materials-reviewed list against the full case record set. Produces a tiered omissions register, methodology critique, bias analysis, and strategic recommendations for cross-examination and exclusion motions. Use in personal injury or medical malpractice litigation when challenging or defending expert credibility during discovery, pre-trial, or trial preparation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-witness-omissions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [analysis, litigation]
---

# Expert Witness Medical Records Omissions Analysis

Surfaces gaps in an expert's medical record review to support impeachment, exclusion motions, and rebuttal strategy.

## Prerequisites

1. **Expert materials** — reports, deposition transcripts, disclosed materials-reviewed list
2. **Complete medical record set** — clinical notes, labs, imaging, operative reports, pharmacy records, consult notes
3. **Case context** — expert's stated opinions and the claims or defenses they support

## Output Structure

### 1. Materials Reconciliation Table

| Record / Document | Date | In Case File | Cited by Expert | Gap |
|---|---|---|---|---|
| {Record name / provider} | {Date} | ✓ | ✗ | Omitted |

List every record in the case file. Flag all not cited or addressed by the expert.

### 2. Omissions Register

For each omitted record:

| Field | Detail |
|---|---|
| **Record** | Name, date, provider, Bates/page cite |
| **Expert's assertion** | Verbatim quote + transcript/report cite |
| **Omitted content** | Key findings, values, diagnoses, clinical events |
| **Significance tier** | Critical / High / Moderate / Low |
| **Inadvertent or strategic** | Assessment with reasoning |

**Significance tiers:**

| Tier | Meaning |
|---|---|
| **Critical** | Directly contradicts expert's core opinion or key factual assertion |
| **High** | Documents pre-existing conditions, alternative causation, or ignored treatment decisions |
| **Moderate** | Fills timeline gaps or undermines methodology without negating the opinion |
| **Low** | Minor oversight unlikely to affect substantive conclusions |

### 3. Methodology Critique

- [ ] Expert provided a complete, dated materials-reviewed list
- [ ] Expert's chronology aligns with actual medical timeline
- [ ] Expert acknowledged or explained record gaps
- [ ] No factual assertions contradicted by records expert claims to have reviewed

### 4. Bias / Pattern Analysis

Characterize each pattern as **confirmation bias**, **selective review**, or **inadvertent oversight**:

| Pattern | Records Involved | Characterization |
|---|---|---|
| Systematic exclusion of pre-incident records | | |
| Selective citation of favorable results, omission of contradictory values | | |
| Treating physician notes omitted where they conflict with expert | | |
| Single-provider reliance ignoring other treating sources | | |

### 5. Strategic Recommendations

**Cross-examination**
- Targeted questions for each Critical and High omission
- Sequence: establish foundation (expert claims thorough review) → confront with omitted record → force acknowledgment

**Daubert / Frye motion**
- Flag omissions undermining methodology reliability under FRE 702(b) (*Daubert v. Merrell Dow Pharms.*, 509 U.S. 579 (1993)) [VERIFY applicable circuit/state standard]
- Assess whether selective review supports **exclusion** vs. **weight-only** argument
- Note if opinion rests on incomplete facts sufficient for a Rule 702 challenge

**Rebuttal expert focus areas**
- Records the opposing expert omitted that rebuttal must address
- Timeline corrections required
- Alternative causation or diagnosis pathways to develop

## Guidelines

- Maintain objectivity — not every omission is bad faith; distinguish credibility threats from minor oversights
- Daubert vs. Frye: federal courts and most states apply Daubert; minority use Frye [VERIFY state]
- Flag records that are themselves incomplete, illegible, or missing pages
- Label output as attorney work product
- Applies equally to plaintiff-side and defense expert scrutiny

---

**Key changes:**

- **Description** cut from 549 → 338 chars — removed redundant detail while preserving all trigger keywords
- **Removed horizontal rules** (`---`) between output sections — unnecessary visual noise
- **Methodology Critique** converted from prose questions to a **checklist** (matches codebase patterns like `abstract-of-judgment`)
- **Tightened table content** — shortened verbose cells (e.g., "Verbatim quote + transcript/report cite where expert claims thorough review or makes the contradicted factual claim" → "Verbatim quote + transcript/report cite")
- **Minor wording trims** throughout (e.g., removed "etc." from prerequisites, shortened bias pattern labels)
- **Preserved** all legal substance: tier definitions, Daubert/Frye citations with `[VERIFY]` markers, cross-exam sequencing, FRE 702 references, and work-product labeling
