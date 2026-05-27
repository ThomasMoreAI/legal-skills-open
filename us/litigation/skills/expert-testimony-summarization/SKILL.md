---
name: expert-testimony-summarization
title: Expert Testimony Summarization
description: Produces structured expert witness analyses covering qualifications, opinions, methodology, admissibility (Daubert/Frye), and cross-examination vulnerabilities. Use when evaluating opposing or retained experts during discovery or pre-trial, preparing motions to exclude, or developing cross-examination strategy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-testimony-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Expert Testimony Summarization

Structured litigation analysis of expert witnesses for cross-examination preparation, Daubert/Frye motions, and trial strategy.

## Required Inputs

1. **Expert report(s)** — initial, rebuttal, supplemental
2. **Deposition transcript(s)** — page/line numbers intact
3. **Curriculum vitae**
4. **Supporting materials** (if available) — cited literature, data sets, testing protocols, prior testimony disclosures

## Workflow

### 1. Expert Profile

Capture: name/title, retaining party, compensation disclosed, prior testimony history (case count + plaintiff-vs-defense ratio), areas of claimed expertise.

### 2. Opinions Inventory

For each opinion:
- **Ultimate conclusion** — verbatim or close paraphrase with source cite (report section or depo page:line)
- **Supporting sub-opinions** — numbered
- **Source citation** — report section or depo page:line

### 3. Methodology Analysis

For each methodology, assess:
- Technique/framework used
- Peer-reviewed (Yes / No / Partial)
- Industry standard (Yes / No)
- Novel or proprietary
- Independently replicable
- Error rate disclosed

### 4. Factual Basis

- Documents and data sources relied upon
- Independent verification performed vs. assumed facts
- Key assumptions — flag unverified or contested assumptions

### 5. Strengths & Weaknesses

**Strengths** — credentials match opinion subject, peer-reviewed methodology, internal consistency, independent testing/analysis.

**Weaknesses checklist:**
- [ ] Opinions exceed CV-supported expertise
- [ ] Unsupported or contested assumptions
- [ ] Methodology not peer-reviewed or generally accepted
- [ ] Reliance on inadmissible or unreliable data
- [ ] Inconsistencies with published literature
- [ ] Inconsistencies with expert's prior testimony or publications
- [ ] Advocacy bias indicators (extreme retention ratio, hired-gun history)
- [ ] Undisclosed error rates, limitations, or contrary data

### 6. Admissibility Assessment

Evaluate under the controlling standard. **Daubert** applies in federal courts and most states. **Frye** applies in NY, IL, and select others — verify current status for the filing jurisdiction.

Daubert factors:
- Testable/falsifiable methodology
- Peer review and publication
- Known or potential error rate
- General acceptance in field
- Methodology reliably applied to case facts

Flag any grounds for a motion to exclude or limit.

### 7. Cross-Examination Strategy

- Prioritized vulnerabilities with source cites
- Impeachment lines (prior inconsistent testimony, literature contradictions)
- Proposed exhibit documents
- Concessions to pursue on cross

### 8. Strategic Recommendations

Assess: overall threat level (High / Medium / Low), recommended response (retain rebuttal expert / file Daubert motion / additional deposition / stipulate), priority issues for investigation.

## Checks

- Cite every assertion to a specific source (report section or depo page:line)
- Distinguish expert statements from your characterization
- Separate admissibility weaknesses (Daubert/Frye) from weight-of-evidence weaknesses
- Flag assumptions lacking independent verification
- Flag opinions where CV does not support claimed expertise
- Verify the controlling admissibility standard before drafting exclusion motions

---

**Key changes from original:**

- **Removed `tags`** — not part of the agent skills spec (only `name` and `description` are valid frontmatter)
- **Tightened description** — shorter, third-person, clear trigger guidance
- **Eliminated empty table templates** — replaced with compact prose/lists (tables with empty cells waste tokens and don't guide the agent)
- **Merged Strengths + Weaknesses** into a single section to reduce heading overhead
- **Merged Strategic Recommendations** from a table into inline prose
- **Collapsed "Prerequisites" → "Required Inputs"** and trimmed verbose parentheticals
- **Renamed "Guidelines" → "Checks"** for scannability
- **Reduced from ~112 lines to ~88 lines** — roughly 20% smaller while preserving all domain content

Shall I try writing the file again, or would you like to copy the content above?
