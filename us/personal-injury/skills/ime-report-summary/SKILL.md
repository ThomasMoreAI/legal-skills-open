---
name: ime-report-summary
title: IME Report Critical Analysis
description: Critically analyzes defense IME reports by auditing record completeness, comparing findings against treating physician records, and surfacing bias indicators and cross-examination vulnerabilities. Triggers when reviewing an IME report, preparing for defense expert deposition, or building a rebuttal strategy in personal injury litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ime-report-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [analysis, litigation, summarization, summary]
---

# IME Report Critical Analysis

Produce a plaintiff-side critical analysis memorandum of a defense IME report. The output is usable for cross-examination outlines, expert witness preparation, and admissibility motions.

## Prerequisites

1. **IME report** — complete defense medical expert report
2. **Treating physician records** — notes, diagnoses, treatment plans
3. **Diagnostic imaging** — MRI, CT, X-ray results
4. **Therapy records** — PT, OT, pain management documentation
5. **Prior medical exams** — pre-incident or subsequent examinations (if any)

## Workflow

### Step 1 — Examination Overview

Populate this table from the IME report:

| Field | Detail |
|-------|--------|
| Examiner | Name, credentials, specialty |
| Referral source | Defense counsel / insurance carrier |
| Date & location | When and where conducted |
| Questions posed | Specific issues examiner addressed |
| Scope limitations | Records not reviewed, tests not performed |

### Step 2 — Examinee Profile

Summarize: demographics, injury mechanism, current symptoms, treatment timeline, legal context.

### Step 3 — Records Review Audit

- List every document the IME examiner claims to have reviewed.
- Compare against the complete medical file.
- **Flag all omitted records** — missing records ground a challenge for incomplete analysis.

### Step 4 — History Discrepancy Analysis

Compare the IME's recitation of patient history against treating records:

| Issue | IME States | Treating Records Show | Significance |
|-------|-----------|----------------------|--------------|
| Symptom onset | | | |
| Complaint severity | | | |
| Functional limitations | | | |
| Treatment response | | | |

Flag symptoms minimized or absent from the IME that appear in treating notes, and physical exam findings conflicting with contemporaneous treating exams.

### Step 5 — Comparative Medical Analysis

Side-by-side comparison on each contested issue:

| Issue | IME Opinion | Treating Physician Opinion | Supporting Authority |
|-------|-------------|---------------------------|---------------------|
| Causation | | | |
| MMI status | | | |
| Permanent impairment rating | | | |
| Future care needs | | | |
| Work restrictions / disability | | | |

Cite AMA Guides, specialty clinical guidelines, and peer-reviewed literature. Mark uncertain citations with [VERIFY].

### Step 6 — Bias & Impeachment Indicators

Check each that applies:

- [ ] Minimizes subjective complaints without objective basis
- [ ] Selectively cites records favoring defense; ignores contrary evidence
- [ ] Uses outdated or non-standard diagnostic criteria
- [ ] Offers causation opinions outside examiner's specialty
- [ ] Conclusions not supported by exam findings
- [ ] Cursory examination relative to injury complexity
- [ ] Litigation history skews heavily defense-side
- [ ] Substantial income from IME work vs. patient care
- [ ] Financial relationship with referring party or insurer
- [ ] Disciplinary history or criticized methodology

### Step 7 — Strategic Recommendations

**Top 3–5 cross-examination vulnerabilities**, each with:
- The specific weakness
- Contradicting documentary evidence or medical authority
- Suggested deposition/trial questions

**Next steps:**
- Supplemental expert consultation needed
- Additional medical evidence to obtain
- Rebuttal report strategy

**Case impact:** Note settlement leverage if IME undermines defense, or rehabilitation steps if IME presents challenges.

## Pitfalls & Checks

- Use **direct quotes** from both IME and treating records to demonstrate contradictions.
- Every factual assertion must cite a specific document and page/section.
- Do not editorialize — let discrepancies speak; frame analysis for attorney use.
- Note jurisdiction-specific IME admissibility rules and Daubert/Frye challenge opportunities.
- Maintain professional tone suitable for attorney work product.
