---
name: informed-consent-form-clinical-trial
title: Informed Consent Form — Clinical Trial
description: Drafts an IRB-ready Informed Consent Form (ICF) for FDA-regulated clinical trials compliant with 21 CFR 50.25, 50.27, and ICH-GCP. Use when drafting or revising consent documents for Phase I–IV trials, IND studies, or other FDA-regulated protocols requiring IRB submission.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/informed-consent-form-clinical-trial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [agreement, drafting, regulatory]
---

# Informed Consent Form — Clinical Trial

Produces a plain-language ICF (≤ 8th-grade reading level) covering all 21 CFR 50.25 required elements, HIPAA authorization, and ethics-compliant framing for research subjects.

## Prerequisites

Collect before drafting:

1. **Protocol details** — title, protocol number, phase, sponsor, IND number
2. **Investigational product** — name, mechanism, dosing, route, known risk profile
3. **Study design** — randomization, arms (incl. placebo), visit schedule, duration
4. **Site info** — PI name/title, institution, IRB name and contact
5. **Risk/benefit data** — preclinical and prior clinical risk frequencies/severities
6. **Injury/compensation policy** — sponsor coverage for research-related injury; participation payments

## Output Structure

### 1. Header Block

On every page: protocol title, protocol number, version/date, page X of Y.

### 2. Study Information

**Purpose**
- Plain-language disease/condition description
- What the study tests; trial phase; subject count (site and total)
- Include: *"This is a research study, not standard medical treatment."*

**Procedures** (chronological)
- Screening, randomization (arm probabilities incl. placebo), visit-by-visit table:

| Visit | Timing | Duration | Procedures |
|---|---|---|---|
| Screening | Week −2 | ~2 hrs | Labs, exam, eligibility |
| Baseline | Day 1 | ~3 hrs | IP administration, vitals, ECG |
| Follow-up | Wk 4, 8, 12 | ~1 hr | Labs, safety assessments |
| End of Study | Week 16 | ~2 hrs | Final assessments, unblinding |

- Flag research-only vs. standard-of-care procedures
- Note preparation requirements (fasting, hold meds)

**Risks and Discomforts**

Organize by category with frequency and severity:

| Category | Example | Frequency | Severity |
|---|---|---|---|
| Investigational product | Nausea, hepatotoxicity | Common/Rare | Mild/Serious |
| Study procedures | Venipuncture bruising | Common | Mild |
| Placebo exposure | Forgoing active therapy | N/A | Study-specific |
| Reproductive | Teratogenicity | Unknown | Potentially serious |
| Privacy/psychosocial | Time burden, incidental findings | Low | Mild |

- Include unknown-risks disclosure and new-information notification statement
- State injury care/compensation available and what is **not** covered

**Potential Benefits**
- Direct benefit: state honestly if possible, probable, or not expected; cite prior data; note not guaranteed
- Societal benefit: knowledge advancement
- Payments/free medication: list but clarify these are not medical benefits
- Include: *"Not participating will not affect your access to standard medical care."*

### 3. Subject Rights

**Confidentiality**
- Coded identifiers, encrypted storage, limited access
- Authorized accessors: research team, IRB, FDA, sponsor/monitors, DSMB
- Mandatory disclosure circumstances (reporting obligations, court order)
- Publication: no individual identification; data retention period stated
- **HIPAA Authorization** (if applicable): PHI use/disclosure scope; required for participation

**Voluntary Participation and Withdrawal**
- Voluntary; refusal/withdrawal does not affect care or benefits
- Withdraw any time without penalty; contact PI at listed number
- Pre-withdrawal data may be retained; investigator/sponsor may remove subject for safety, non-compliance, or study termination
- New findings affecting willingness will be communicated

**Contacts**

| Role | Name | Phone | Hours |
|---|---|---|---|
| PI (questions, injuries) | [Name, MD] | [###-###-####] | 24/7 emergencies |
| IRB (rights concerns) | [IRB Name] | [###-###-####] | M–F 9–5 |
| After-hours emergency | [On-call] | [###-###-####] | Evenings/weekends |

### 4. Consent Statement

First-person acknowledgment covering: form read/explained, questions answered, voluntary participation, right to withdraw, agreement to participate in [Study Title], Protocol [Number].

**Optional check-box consents** (if applicable):
- Future biospecimen research use
- Genetic testing
- Long-term follow-up contact
- HIPAA authorization

### 5. Signature Block (per 21 CFR 50.27)

| Signatory | Printed Name | Signature | Date |
|---|---|---|---|
| Research Subject | | | |
| Legally Authorized Representative | | | |
| Representative's relationship/authority | | N/A | N/A |
| Impartial Witness (if subject cannot read) | | | |
| Person Obtaining Consent (name + role) | | | |

- Subject receives signed, dated copy
- Add re-consent rows if protocol requires re-consent at defined intervals

## Drafting Rules

- **Reading level**: ≤ 8th grade; define technical terms on first use
- **No exculpatory language**: No waiver of legal rights or liability release (21 CFR 50.25(a)(8))
- **Therapeutic misconception**: Distinguish research from treatment; do not overstate direct benefit
- **Placebo disclosure**: Explain probability and risk of forgoing active therapy
- **Vulnerable populations**: Add protections per 21 CFR 50 Subparts C, D (pregnant women, children, prisoners, cognitively impaired)
- **Formatting**: ≥ 12pt font, section headings, page numbers, version/date footer; typical 8–15 pages

## Checklist Before Finalizing

- [ ] All 21 CFR 50.25(a) basic elements present
- [ ] All applicable 50.25(b) additional elements included
- [ ] No exculpatory language
- [ ] HIPAA authorization section included (if applicable)
- [ ] Vulnerable-population protections added (if applicable)
- [ ] Reading level verified ≤ 8th grade
- [ ] IRB approval required before use; retain IRB-stamped version as operative document
- [ ] **[VERIFY]**: Confirm ICH E6(R3) GCP requirements align with jurisdiction's adoption status
