---
name: ind-application
title: IND Application
description: Drafts FDA Investigational New Drug (IND) applications under 21 CFR Part 312, including Form 1571, Investigator's Brochure, clinical protocols, CMC sections, and nonclinical data packages. Use when preparing IND submissions, pre-IND packages, IND amendments, or clinical trial authorization documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ind-application
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: life-sciences
language: en
tags: [drafting, memo]
---

# IND Application

Drafts a complete IND application under 21 CFR Part 312 for FDA authorization to begin human clinical trials.

## Prerequisites

Collect before drafting:

1. **Drug substance/product info** — chemical name, code designation, structural formula, mechanism of action
2. **Nonclinical reports** — pharmacology, toxicology, PK/PD data
3. **CMC data** — manufacturing process, specifications, stability, certificates of analysis
4. **Clinical protocol(s)** — design, objectives, endpoints, statistical analysis plan
5. **Investigator info** — CVs, Form FDA 1572, clinical site details
6. **Prior human experience** (if any) — foreign trials, literature, compassionate use
7. **IRB documentation** — approval letters or submission plans, informed consent forms

## Quick Start

1. Confirm trial phase (I/II/III) — this drives CMC depth and nonclinical requirements
2. Complete Form 1571 cover sheet
3. Draft sections in 21 CFR 312.23(a) order (see below)
4. Cross-reference all nonclinical citations to specific IND sections
5. Run checklists for Form 1571, IB, protocol, and environmental assessment

## IND Section Order (21 CFR 312.23(a))

| # | Section | Reference |
|---|---------|-----------|
| 1 | Cover Sheet — FDA Form 1571 | 312.23(a)(1) |
| 2 | Table of Contents — mirror regulatory numbering | 312.23(a)(2) |
| 3 | Introductory Statement — rationale, therapeutic purpose, investigational plan | 312.23(a)(3) |
| 4 | Investigator's Brochure — safety, efficacy, pharmacology, known risks | 312.23(a)(5) |
| 5 | Clinical Protocol(s) — design, dosing, safety monitoring, statistical plan | 312.23(a)(6) |
| 6 | CMC: Drug Substance — synthesis, specs, stability | 312.23(a)(7) |
| 7 | CMC: Drug Product — formulation, controls, container/closure, stability | 312.23(a)(7) |
| 8 | Pharmacology/Toxicology — PK, acute/chronic tox, repro tox, genotox | 312.23(a)(8) |
| 9 | Previous Human Experience — prior clinical data, foreign trials, literature | 312.23(a)(9) |
| 10 | Additional Information — IRB approvals, consent, investigator qualifications | 312.23(a)(10) |

## Key Checklists

### Form 1571

- [ ] Sponsor name, address, contact
- [ ] Drug name and code designations
- [ ] Trial phase (I, II, III)
- [ ] IND number (amendment) or "Initial"
- [ ] Serial number
- [ ] Indication(s) under investigation
- [ ] List of enclosed sections
- [ ] Authorized signature with date

### Investigator's Brochure

- [ ] Physical/chemical/pharmaceutical properties
- [ ] Nonclinical pharmacology summary
- [ ] Nonclinical PK and metabolism
- [ ] Nonclinical toxicology (tabulate: species, route, duration, NOAEL, findings)
- [ ] Clinical experience summary (if applicable)
- [ ] Known/anticipated adverse effects and precautions

### Clinical Protocol

- [ ] Title, protocol number, version/date
- [ ] Primary and secondary objectives
- [ ] Study design and phase
- [ ] Inclusion/exclusion criteria
- [ ] Dosing regimen with rationale
- [ ] Efficacy and safety endpoints
- [ ] Stopping rules and dose-limiting toxicity definitions
- [ ] Safety monitoring plan (AE reporting, DSMB if applicable)
- [ ] Statistical analysis plan with sample size justification

## Phase-Appropriate CMC Depth

| Phase | Drug Substance | Drug Product | Stability |
|-------|---------------|-------------|-----------|
| I | Synthetic route, preliminary specs, structure confirmation | Formulation description, basic controls | Abbreviated (cover trial duration) |
| II | Refined process, tightened specs, impurity profiles | Validation initiated, expanded controls | 6+ months accelerated + long-term |
| III | Full process validation, complete characterization | Full cGMP, container/closure validation | ICH-compliant program |

## Nonclinical Study Table Format

For each study, tabulate: study type, test facility (with GLP status), species/strain, route, dose levels, duration, NOAEL/NOEL, key findings, relevance to clinical dose.

## Environmental Assessment

- Most INDs qualify for categorical exclusion under 21 CFR 25.31(e)
- If claiming exclusion: cite the specific 21 CFR 25 provision with basis statement
- If exclusion does not apply: prepare assessment per 21 CFR Part 25 Subpart B

## Pitfalls and Checks

- **Verify FDA forms** — retrieve current Form 1571/1572 from fda.gov; versions update periodically
- **Phase-appropriate CMC** — do not over-document Phase I or under-document Phase III
- **Cross-reference internally** — protocol references to nonclinical data must cite specific IND section/page
- **GLP compliance** — pivotal safety studies require 21 CFR Part 58; flag and justify any non-GLP studies
- **No promotional language** — avoid unsupported efficacy claims; this is a scientific/regulatory document
- **Safety-first framing** — every section must demonstrate adequate basis for protecting human subjects
- **Confidential info** — mark trade secrets per 21 CFR 312.130 if sponsor requests
- **eCTD format** — for electronic submissions, organize per FDA eCTD Module 1–5 structure
- **Pre-IND feedback** — if a Type B pre-IND meeting occurred, address each FDA comment explicitly
