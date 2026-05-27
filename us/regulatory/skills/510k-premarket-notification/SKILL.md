---
name: 510k-premarket-notification
title: FDA 510(k) Premarket Notification
description: Drafts FDA 510(k) Premarket Notification submissions demonstrating substantial equivalence under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated pathways. Use when preparing Class II medical device regulatory filings, substantial equivalence analyses, or FDA premarket submissions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/510k-premarket-notification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, letter]
---

# FDA 510(k) Premarket Notification

Drafts a complete 510(k) submission package demonstrating substantial equivalence to a predicate device under 21 CFR Part 807, Subpart E.

## Prerequisites

Gather before drafting:

1. **510(k) type** — Traditional, Special, or Abbreviated
2. **Predicate device** — trade name, manufacturer, K-number, clearance date
3. **Device classification** — product code, regulation number, panel, class
4. **Establishment registration** — FDA registration number; U.S. agent if foreign
5. **Technical file** — drawings, materials list, software architecture (if applicable)
6. **Performance data** — bench testing, biocompatibility (ISO 10993), clinical/literature evidence
7. **Proposed labeling** — IFU, package insert, patient materials, packaging artwork

## Submission Sections

### 1. Cover Letter

Address to appropriate CDRH division. Include device trade name + common name, 510(k) type, predicate (name, manufacturer, K-number), pathway justification (why 510(k) vs. PMA), submitter contact with establishment registration, and U.S. agent if foreign manufacturer.

### 2. FDA Form 3514

Complete all fields: applicant legal name and FDA registration number, trade name + common name, product code / regulation number / panel / class, submission type (original or resubmission with prior K-number), 510(k) type, disclosure election (Summary or Statement), contact info, and signature block with authorized representative.

### 3. Device Description

Enable reviewer comprehension without physical examination:

- Physical characteristics — size, weight, configuration
- Materials — flag patient-contacting materials with ISO 10993 status
- Operating principles and mechanism of action
- Software/firmware, cybersecurity, AI/ML components (if applicable)
- Energy source and safety controls (if applicable)
- Sterility method and SAL (if sterile)
- Novel features — each must be addressed in SE comparison

Reference engineering drawings, cross-sections, and annotated photos.

### 4. Intended Use & Indications for Use

- **Intended use** — general purpose, broad clinical condition
- **Indications** — patient population, specific conditions, anatomical site, selection criteria
- **Contraindications** — patients/conditions where device should not be used

Critical: IU language must be identical across labeling, submission, and Form 3514. Any divergence from predicate IU requires justification. Every indication must be supported by performance data.

### 5. Substantial Equivalence Comparison

Present as side-by-side table comparing subject vs. predicate across: intended use, technology, materials, energy source, software, performance specs, physical characteristics, and novel features.

For each parameter, state Same or Different with analysis. For every difference, explain why it raises no new safety or effectiveness questions, supported by data.

**Split predicate**: If using multiple predicates, justify. At least one must share the same intended use.

### 6. Performance Data

Present in order:

1. **Bench testing** — method, conditions, sample size, pre-specified acceptance criteria, results with statistics, predicate comparison
2. **Biocompatibility** (ISO 10993-1) — contact type/duration, tests, lab, criteria, results; document unexpected findings
3. **Animal studies** (if applicable) — GLP compliance, model justification, power analysis, endpoints, adverse events
4. **Clinical data** — study design, population, power analysis, endpoints, statistics, adverse events; OR literature review with synthesis
5. **Standards compliance** — applicable consensus standards (ASTM, ISO, IEC, AAMI) with test reports or declarations of conformity
6. **FDA guidance compliance** — cite device-specific guidance documents followed

Each data set must link to a specific SE comparison point or IFU claim.

### 7. Labeling Package

Required components (21 CFR Part 801):

- IFU — setup, technique, troubleshooting, maintenance
- Package insert — indications, contraindications, warnings
- Patient labeling (if applicable) — lay language
- Device/packaging labels — name, manufacturer, lot/serial, sterilization indicators, ISO 15223-1 symbols, storage, expiration
- Rx statement if prescription device
- Sterilization info if sterile — method, SAL, package integrity
- Symbol glossary

IFU indications must exactly match submission indications.

### 8. Truthful and Accurate Statement

Per 21 CFR 807.87(k). Signatory certifies all information is truthful and accurate, no material facts omitted, acknowledging 18 U.S.C. § 1001 penalties. Include printed name, title, signature, and date. Signatory must have direct knowledge of contents and binding authority.

### 9. 510(k) Summary or Statement

**Summary** (21 CFR 807.92) — public within 30 days of clearance: submitter contact, device names and classification, device description, IU (exact submission language), predicate comparison summary, performance data summary, SE conclusion.

**Statement** (21 CFR 807.93) — greater confidentiality: declaration to provide full 510(k) within 30 days of written request, contact info, fulfillment process must be in place.

## Pitfalls and Checks

- Cross-reference all sections for consistency in device description, IU language, and performance claims
- Verify predicate is currently legally marketed and not subject to Class III order
- Consider Pre-Submission (Q-Sub) for novel aspects or pathway uncertainty
- Electronic submissions must comply with 21 CFR Part 11 for signatures
- Flag proprietary/trade-secret content when choosing Summary vs. Statement
- Mark uncertain regulatory citations with [VERIFY]
- Do not draft clinical study protocols — flag data gaps for separate clinical planning

---

**Key changes made:**

- **Description** trimmed — removed enumeration of every section; kept trigger guidance
- **Renamed** "Output Structure" → "Submission Sections" for directness
- **Cover Letter & Form 3514** — collapsed tables/bullet lists into dense prose paragraphs, preserving all required fields
- **Intended Use** — replaced table with tight bullet list + inline critical rule
- **SE Comparison** — removed empty template table; described required parameters in prose with the same comparison dimensions
- **Labeling** — converted checkbox list to plain bullets (checkboxes are non-functional in skill context)
- **Truthful and Accurate Statement** — removed code-fenced template block; kept regulatory citation, required elements, and signatory rule in prose
- **Summary/Statement** — merged into single compact section
- **Renamed** "Guidelines" → "Pitfalls and Checks" per best practices
