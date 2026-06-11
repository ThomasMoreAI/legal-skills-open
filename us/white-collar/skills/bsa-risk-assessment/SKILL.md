---
name: bsa-risk-assessment
title: BSA/AML Risk Assessment
description: Drafts a BSA/AML Risk Assessment for U.S. financial institutions per FinCEN, FFIEC, and OCC standards. Evaluates inherent risks (customer, product, geographic, transaction, third-party), control adequacy, and residual risk. Use when preparing annual BSA compliance assessments, post-acquisition integration reviews, or when business changes trigger reassessment under 31 U.S.C. § 5318(h).
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bsa-risk-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: white-collar
language: en
---

# BSA/AML Risk Assessment

Produces examination-ready BSA Risk Assessments evaluating inherent AML/CFT risks against mitigating controls per FFIEC BSA/AML Examination Manual methodology.

## Prerequisites

Gather before drafting:

1. **Institution profile** — entity type, charter/regulator, total assets, branch footprint, international relationships
2. **Products & services** — inventory with volumes for high-risk products (wires, monetary instruments, prepaid, trade finance, crypto on/off ramps)
3. **Customer data** — segments with counts of high-risk categories (cash-intensive businesses, PEPs, NRAs, MSBs, foreign correspondents)
4. **BSA/AML program docs** — policies, CIP/CDD/EDD procedures, monitoring system specs, training records
5. **Filing history** — annual CTR/SAR counts by category
6. **Independent testing** — most recent scope, findings, remediation status
7. **Regulatory history** — outstanding MRAs, MOUs, enforcement actions

## Document Sections

### 1. Executive Summary

Overall risk rating (Low/Moderate/High), key concentrations, control gaps, priority recommendations with owners and target dates.

### 2. Introduction

- Regulatory basis: 31 U.S.C. § 5318(h); 31 C.F.R. § 1020.210
- Scope: all business lines, products, customers, geographies
- Assessment period and update frequency (typically annual)
- FFIEC risk-based methodology alignment

### 3. Institution Overview

Table covering: entity type, charter/regulator, total assets, branch count, high-risk products offered, customer segments, annual CTR/SAR filing counts.

### 4. Inherent Risk Identification

Five risk dimensions, each rated High/Moderate/Low:

- **Customer** — cash-intensive businesses, MSBs, NBFIs, PEPs, NRAs, nonprofits, foreign correspondents, FATF-listed jurisdiction customers
- **Product & Service** — flag products enabling anonymity, rapid movement, or cross-border activity (wires, prepaid, private banking, trade finance, digital channels, crypto)
- **Geographic** — HIDTA/HIFCA areas, FATF grey/black list jurisdictions, FinCEN GTO zones, OFAC sanctioned countries
- **Transaction** — high-volume cash, structuring patterns, funnel accounts, rapid cycling, shell companies, trade-based ML
- **Third-Party** — independent agents, outsourced onboarding/processing, fintech partnerships

### 5. Risk Assessment Matrix

Per risk category:

| Risk | Inherent | Likelihood | Impact | Mitigating Controls | Residual |
|---|---|---|---|---|---|
| [Category] | H/M/L | H/M/L | H/M/L | [Description] | H/M/L |

Reference FATF typology reports and FinCEN advisories for current typologies (ransomware, elder exploitation, human trafficking, real estate, virtual assets).

### 6. Controls & Mitigation

Evaluate each BSA program component against its regulatory basis:

| Component | Citation |
|---|---|
| CIP | 31 C.F.R. § 1020.220 |
| CDD / Beneficial Ownership | 31 C.F.R. § 1010.230 |
| EDD | FFIEC Manual |
| Transaction Monitoring | FFIEC Manual |
| OFAC Screening | 31 C.F.R. Part 501 |
| CTR Filing | 31 U.S.C. § 5313 |
| SAR Filing | 31 U.S.C. § 5318(g) |
| BSA Officer / Governance | 31 C.F.R. § 1020.210 |
| Training | 31 C.F.R. § 1020.210 |
| Independent Testing | 31 C.F.R. § 1020.210 |

For each: document current status and adequacy rating.

### 7. Conclusions & Recommendations

- Overall risk determination with narrative justification
- Residual risks where controls are insufficient
- Prioritized remediation table (recommendation, priority, owner, target date)

## Verification Requirements

These items change over time — confirm before finalizing:

- [ ] FATF grey/black list countries — verify at fatf-gafi.org
- [ ] Active FinCEN GTOs — jurisdiction-specific and time-limited
- [ ] Beneficial ownership threshold (currently 25%) — check for subsequent FinCEN rulemaking
- [ ] FinCEN advisory numbers — verify FIN numbers and dates before citing

## Pitfalls

- **Quantitative support required** — risk ratings must cite transaction volumes, SAR counts, or alert rates; qualitative assertions alone are insufficient
- **Board presentation** — document must be board-approved or presented to senior management with evidence of review
- **Version retention** — keep prior assessments; regulators compare year-over-year
- **Privilege risk** — do not include attorney-client privileged material if document will be produced to examiners
- **FFIEC citations** — reference specific Examination Manual sections when evaluating control adequacy
