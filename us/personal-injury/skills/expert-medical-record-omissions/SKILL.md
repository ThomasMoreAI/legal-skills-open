---
name: expert-medical-record-omissions
title: Expert Medical Record Omissions
description: Analyzes expert witness reports, depositions, and testimony to identify gaps in medical record review, map conflicts to the full record set, and produce impeachment and admissibility analysis with pinpoint citations. Use when reviewing expert reports for missing medical records, selective review patterns, Daubert/Frye challenges, cross-examination prep, motions to exclude or limit, or rebuttal expert focus in personal injury or medical malpractice litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-medical-record-omissions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Expert Medical Record Omissions

Identify material omissions in expert medical record review and translate them into litigation-ready challenges with pinpoint citations.

## Prerequisites

1. Complete medical record set with Bates labels and index
2. Expert materials: report(s), disclosure, materials-reviewed list, CV, deposition/testimony transcripts, exhibits
3. Case theory summary (claims, defenses, causation or standard-of-care theory)
4. Jurisdiction admissibility standard (Daubert, Frye, or hybrid)
5. Medical chronology or timeline (if available)

## Workflow

1. Build record inventory and expert review map
2. Detect omissions and contradictions
3. Rate materiality and litigation impact
4. Flag patterns suggesting selective review or bias
5. Deliver structured report with pinpoint citations

## Record Inventory

For each medical record, capture:

| Field | Entry |
|---|---|
| Record date | Encounter or service date |
| Provider/facility | Name and specialty |
| Record type | Note, imaging, lab, operative, billing, etc. |
| Bates range | Start–end |
| Key facts | Diagnosis, findings, causation cues |
| Causation relevance | Supports / Contradicts / Alternative / Neutral |

## Expert Review Map

Extract from the expert's own materials:

| Item | Source | Citation |
|---|---|---|
| Materials-reviewed list | Report or disclosure | Page/paragraph |
| Records cited in opinions | Report | Page/paragraph |
| Deposition admissions about records | Transcript | Page/line |
| Stated limitations or exclusions | Report or deposition | Page/line |

## Omission Matrix

One row per omitted record:

| Omitted record | Date | Provider | Bates | Expert statement that should have addressed it | Conflict or gap | Significance |
|---|---|---|---|---|---|---|
| _Record name_ | _Date_ | _Provider_ | _Bates_ | _Report/Depo cite_ | Contradiction / Alternative / Context | High / Med / Low |

**Significance scale:**
- **High** — Directly undermines key opinion or reliability. Use for admissibility challenges, motion practice.
- **Medium** — Alters weight but not core opinion. Use for cross-examination, rebuttal focus.
- **Low** — Peripheral or cumulative. Use for background impeachment.

## Inconsistency Log

| Expert assertion | Claimed source | Contradicting record | Citation (Bates + page/line) | Impact |
|---|---|---|---|---|
| _Assertion_ | _Cite_ | _Record_ | _Bates + page/line_ | Material / Moderate / Minor |

## Pattern Flags

Check for these indicators of selective review or bias:

- [ ] Repeated omission of pre-existing conditions
- [ ] Omission of alternative causation records
- [ ] Omission of treating provider notes conflicting with opinion
- [ ] Omission of diagnostic imaging or labs central to timeline
- [ ] Chronology inconsistencies versus record dates
- [ ] Mischaracterization of records listed as reviewed
- [ ] Selective inclusion of favorable records only

## Strategic Outputs

### Cross-Examination Seeds

| Theme | Anchor omission | Objective |
|---|---|---|
| Record completeness | _Record_ | Establish incomplete review |
| Methodology | _Omitted category_ | Show unreliable process |
| Alternative causation | _Record_ | Expose unaddressed cause |
| Timeline accuracy | _Record_ | Undermine chronology |

### Motion Triggers

Flag for Daubert/Frye challenge or motion to exclude when:
- Expert failed to consider key facts relevant to causation or standard of care
- Methodology not reliably applied to the full record set
- Opinions based on inaccurate timeline or mischaracterized records
- Expert did not review materials they claim to have reviewed

## Report Structure

Organize final output as:

1. **Scope and Materials** — Record set scope, expert materials reviewed, admissibility standard
2. **Omission Summary** — Count and list by significance (High / Medium / Low)
3. **Omission Matrix** — Full table
4. **Inconsistency Log** — Full table
5. **Pattern Analysis** — Indicators observed, alternative explanations for omissions
6. **Strategic Recommendations** — Cross-examination themes, motion practice targets, rebuttal expert focus areas

## Pitfalls

- **Omission vs. disagreement**: Only flag omissions where the record exists and was not addressed. Disagreement with a reviewed record is not an omission.
- **Record completeness**: Confirm the record set is complete before concluding a gap is material. Flag missing record categories that could change the analysis.
- **Citation rigor**: Every omission and contradiction requires a pinpoint citation (Bates + page/line).
- **Weight vs. admissibility**: Separate weight attacks from admissibility challenges. Note the jurisdiction's standard.
- **Neutrality**: Avoid advocacy language in the analysis itself.
- **PHI**: Protect PHI and comply with applicable confidentiality rules.
