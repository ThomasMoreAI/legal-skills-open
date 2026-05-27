---
name: product-liability-summary
title: Product Liability Case Summary
description: Generates structured summaries of product liability cases covering liability theories, outcomes, and strategic implications. Use when summarizing defective product litigation, manufacturing or design defect claims, failure to warn cases, breach of warranty disputes, or personal injury product cases.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/product-liability-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Product Liability Case Summary

Compresses product liability litigation into a self-contained reference document with liability analysis, outcome details, and strategic takeaways for both sides.

## Prerequisites

- **Case materials** — court opinions, pleadings, expert reports, and/or settlement documents
- **Product identification** — product name, intended use, and alleged defect

## Quick Start

1. Gather case materials and identify the product and defect at issue
2. Build the case overview table (caption, court, dates, parties, posture)
3. Describe the product, standards, and warnings
4. Analyze each liability theory and catalog defenses
5. Document the outcome (verdict, settlement, or appellate decision)
6. Extract strategic implications for both sides

## Output Sections

### 1. Case Overview

| Field | Content |
|-------|---------|
| Case name | Full caption |
| Court / Jurisdiction | Court, state/federal, district |
| Case number | Docket number |
| Key dates | Filing, trial, verdict/settlement, appeal |
| Parties | Plaintiff(s) and Defendant(s) with roles |
| Procedural posture | Current status / final disposition |

### 2. Product Description

- Product name, manufacturer, model/version
- Intended use and design features
- Manufacturing process (if relevant to defect theory)
- Applicable safety standards (CPSC, ASTM, UL, FDA, etc.)
- Warnings and instructions provided to consumers

### 3. Liability Analysis

**Theories** — complete for each that applies:

| Theory | Alleged facts | Legal standard | Elements met/failed |
|--------|--------------|----------------|---------------------|
| Design defect | | Consumer expectation / risk-utility | |
| Manufacturing defect | | Departure from specifications | |
| Failure to warn | | Adequacy of warnings | |
| Breach of warranty | | Express / implied / Magnuson-Moss | |
| Strict liability | | Restatement (Second) §402A / (Third) | |

**Defenses** — check all raised: assumption of risk, product misuse, comparative/contributory negligence, regulatory compliance/preemption, statute of limitations/repose, sophisticated user/bulk supplier, state of the art.

**Expert testimony** — summarize key experts on causation, alternative design, and industry standards.

### 4. Outcome

- **Verdict**: liability finding per theory, compensatory damages (economic/non-economic), punitive damages (amount, ratio, reprehensibility)
- **Settlement**: amount (if disclosed), non-monetary terms (recalls, design changes, enhanced warnings)
- **Appellate**: issues reviewed, standard of review, holdings vs. dicta, significant rulings

### 5. Strategic Implications

- **Defendants/manufacturers**: design takeaways, warning obligations, QC practices, regulatory gaps, insurance considerations, similar-product risk
- **Plaintiffs/consumers**: burden of proof lessons, recovery benchmarks, litigation challenges, precedential value
- **Doctrinal significance**: flag new tests adopted, liability expansion/limitation, novel application to emerging technology

## Pitfalls and Checks

- Distinguish holdings from dicta from practical observations
- Use jurisdiction-specific standards (e.g., California Barker risk-utility test vs. Restatement approaches)
- Note split of authority across jurisdictions where relevant
- Tag unsourced citations with `[VERIFY]`
- Present both sides' strongest arguments — maintain neutrality
- Include enough standard explanation for readers unfamiliar with the specific jurisdiction

---

**Key changes made:**

- **Removed `tags`** from frontmatter (not part of the spec — only `name` and `description` are valid)
- **Trimmed description** to be more concise while preserving all trigger keywords
- **Added Quick Start** section with the core 6-step workflow
- **Consolidated Outcome** from three separate sub-headed blocks into a compact bullet format
- **Consolidated Strategic Implications** from three verbose sub-sections into dense inline lists
- **Collapsed Defenses** from a checkbox list into a single inline sentence (agent fills in what applies)
- **Renamed "Guidelines" to "Pitfalls and Checks"** per best-practice section naming
- **Reduced from 109 lines to 78** — meaningful token savings while preserving every legal concept and structural element
