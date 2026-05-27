---
name: med-mal-summary
title: Medical Malpractice Summary
description: Produces structured medical malpractice case summaries from medical records for personal injury litigation. Extracts chronological care narratives, identifies potential standard-of-care breaches, traces causation, assesses damages, and flags expert needs and statute of limitations issues. Use when evaluating medical negligence claims, onboarding med-mal matters, or assessing case merits during pre-filing or discovery.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/med-mal-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [analysis, litigation, summary]
---

# Medical Malpractice Summary

Produces a structured med-mal case summary from medical records for attorney case evaluation and litigation planning.

## Prerequisites

1. **Medical records** — hospital charts, physician notes, nursing notes, discharge summaries
2. **Diagnostic materials** — lab results, imaging/radiology reports, pathology reports
3. **Procedure documentation** — operative reports, anesthesia records, consent forms
4. **Pharmacy records** — medication administration records, prescription history
5. **Patient intake** — chief complaint, date of incident, treating providers, patient demographics

## Output Structure

### 1. Case Overview Table

| Field | Content |
|---|---|
| Patient | Name, DOB, relevant medical history |
| Date(s) of alleged negligence | Specific dates |
| Facility/Provider(s) | Names, specialties, roles |
| Chief complaint / Presenting condition | Initial presentation |
| Alleged injury/outcome | Summary of harm |
| SOL flag | Statute date + discovery rule considerations |

### 2. Chronological Care Narrative

For each treatment episode:

| Date | Provider (Specialty) | Clinical Findings | Diagnosis | Treatment/Orders | Outcome/Notes |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Flag entries with `⚠` where potential standard-of-care issues exist.

### 3. Standard of Care Analysis

For each identified deviation:

- **Provider**: Name and specialty
- **Action/Omission**: What was done or not done
- **Expected standard**: What a reasonably competent provider in that specialty would have done
- **Supporting basis**: Clinical guidelines, protocols, or accepted practice (cite where identifiable)
- **Severity**: Critical / Significant / Minor

Breach categories to evaluate:

- [ ] Diagnostic errors — missed, delayed, or wrong diagnosis
- [ ] Failure to order appropriate tests
- [ ] Misinterpretation of test results
- [ ] Treatment selection errors
- [ ] Surgical/procedural errors
- [ ] Medication errors (wrong drug, dose, interaction)
- [ ] Failure to obtain informed consent
- [ ] Monitoring failures (post-op, medication, vitals)
- [ ] Premature discharge
- [ ] Failure to refer to specialist
- [ ] Communication failures between providers
- [ ] Documentation gaps or alterations

### 4. Causation Analysis

For each breach, trace: **Breach → Mechanism of Harm → Injury/Outcome**

Classify each harm:

| Category | Description |
|---|---|
| Attributable to negligence | Would not have occurred but for the breach |
| Underlying condition | Natural disease progression |
| Unavoidable complication | Known risk of necessary treatment |
| Concurrent/intervening cause | Other contributing factors |

### 5. Damages Assessment

| Category | Details | Documentation Source |
|---|---|---|
| Additional medical treatment | Surgeries, hospitalizations, rehab, future care | Page/record refs |
| Physical impairment | Permanent injury, disability, functional limitations | Page/record refs |
| Pain and suffering | Duration, severity, ongoing nature | Page/record refs |
| Lost wages / Earning capacity | Work restrictions, vocational impact | Page/record refs |
| Life expectancy impact | If applicable | Page/record refs |

### 6. Legal & Evidentiary Flags

- **Expert specialties needed** — list by specialty based on providers and issues involved
- **Statute of limitations** — calculate from treatment dates; note discovery rule triggers
- **Record red flags** — gaps, late entries, alterations, inconsistencies between providers
- **Provider admissions** — documented apologies, acknowledgments of error, incident reports
- **Applicable guidelines** — cite specific clinical practice guidelines or hospital protocols implicated
- **Strengths** — strongest facts supporting liability and damages
- **Weaknesses** — defenses, contributory factors, documentation gaps undermining the claim

## Guidelines

- Cite every factual assertion to specific page numbers, dates, and document sources
- Use medical terminology with parenthetical plain-language explanations on first use
- Present balanced analysis — identify both strengths and weaknesses of the claim
- Do not render legal conclusions on ultimate liability; frame as "potential" breaches for attorney evaluation
- Flag any records that appear incomplete or were not provided
- If standard-of-care analysis requires subspecialty knowledge beyond the records, note that expert consultation is needed
- Mark any cited clinical guidelines or statistics with `[VERIFY]` unless directly quoted from provided records
