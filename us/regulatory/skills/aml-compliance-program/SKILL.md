---
name: aml-compliance-program
title: AML Compliance Program
description: 'Drafts board-ready Anti-Money Laundering compliance programs for U.S. financial institutions under BSA/FinCEN requirements. Covers CIP, CDD, EDD, SAR/CTR reporting, OFAC screening, risk assessment, training, independent testing, and governance structures. Use when creating or updating AML policies, BSA compliance programs, or financial institution regulatory documentation. Trigger keywords: AML, BSA, FinCEN, Bank Secrecy Act, anti-money laundering, SAR, CTR, OFAC, CIP, CDD, KYC, compliance program.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/aml-compliance-program
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, memo, research]
---

# AML Compliance Program

Produces a comprehensive, board-ready AML compliance program tailored to a financial institution's risk profile, satisfying BSA, FinCEN, and federal/state requirements.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before drafting, collect from the user:

1. **Existing policies** — current AML program, risk assessments, exam reports, regulatory correspondence
2. **Institutional profile** — org chart, business lines, products, customer demographics, geographic footprint
3. **Risk data** — prior assessments, audit findings, enforcement actions, consent orders
4. **Applicable regulations** — confirm institution type (bank, MSB, broker-dealer) to determine which CFR parts, FinCEN guidance, and agency bulletins apply

Do not proceed until items 1–2 are addressed. Items 3–4 may be developed during drafting if unavailable.

## Quick Start

Draft a numbered policy document covering all sections below. Calibrate depth to the institution's size, complexity, and risk profile.

---

## Step 1: Program Foundation

| Element | Requirement |
|---|---|
| Board endorsement | Explicit board/senior management approval and oversight |
| Scope | All business lines, customer relationships, geographies, transaction types |
| Risk-based approach | Controls calibrated to risk assessment findings |
| Resource commitment | Adequate personnel, technology, budget |

## Step 2: AML Compliance Officer

| Element | Requirement |
|---|---|
| Qualifications | CAMS or equivalent; demonstrated BSA/AML expertise |
| Reporting line | Direct to senior management; regular board access |
| Independence | Evaluation tied to compliance effectiveness, not production |
| Authority | Unrestricted access to all records, systems, personnel |

**Core duties:** Regulatory contact (FinCEN, regulators, law enforcement) · SAR/CTR/BSA filing oversight · risk assessment coordination · training management · independent testing oversight · program design and updates.

## Step 3: Customer Identification Program (CIP)

Per 31 CFR § 1020.220:

| Data Point | Individual | Legal Entity |
|---|---|---|
| Full legal name | Required | Required |
| Date of birth | Required | N/A |
| Address | Residential/business street | Principal place of business |
| ID number | SSN/TIN or passport + country | EIN or equivalent |

**Verification:** Documentary (government ID / incorporation docs) · Non-documentary (consumer reporting, public databases) · Non-face-to-face (additional measures for remote channels).

**Retention:** 5 years after account closure.

## Step 4: Customer Due Diligence (CDD)

Per 31 CFR § 1010.230:

- Identify beneficial owners: each individual ≥25% equity + one with significant management control
- Collect via certification form; verify per CIP standards
- Update ownership on risk-based schedule and upon known changes
- Document relationship purpose, business activities, anticipated activity, source of funds
- Build expected transaction profiles (type, industry, geography, history)
- Ongoing monitoring: automated systems, periodic reviews, exception reporting

## Step 5: Enhanced Due Diligence (EDD)

**Mandatory EDD triggers:**

| Category | Examples |
|---|---|
| PEPs | Per FinCEN guidance |
| High-risk geographies | FATF high-risk/monitored jurisdictions |
| Complex ownership | Opaque structures obscuring beneficial ownership |
| High-risk businesses | MSBs, virtual currency exchanges, cash-intensive |
| Elevated risk rating | Multiple risk factors per internal methodology |

**Requirements:** Background investigation · senior management approval · enhanced monitoring (lower thresholds, more frequent reviews) · documented risk rating methodology (customer × geography × product × activity).

## Step 6: Suspicious Activity Reporting (SAR)

Per 31 CFR § 1020.320:

- **Threshold:** ≥ $5,000 where institution knows/suspects illegal activity, BSA evasion, no business purpose, or criminal facilitation
- **Deadlines:** 30 days (suspect identified) · 60 days (no suspect identified)
- **Key indicators:** Structuring · activity inconsistent with profile · large currency transactions · wire transfers lacking rationale or involving high-risk jurisdictions · recordkeeping/CIP avoidance · shell company transactions
- **Confidentiality:** Federal law prohibits disclosure to subjects; civil/criminal penalties for violation; records retained 5 years; need-to-know access only
- **Escalation:** Immediate report to Compliance Officer; good-faith reporters protected

## Step 7: Currency Transaction Reporting (CTR)

Per 31 CFR §§ 1010.310, 1020.310:

| Element | Requirement |
|---|---|
| Threshold | Currency transactions > $10,000 per person per business day |
| Aggregation | Multiple transactions by/on behalf of same person in one day |
| Filing deadline | 15 calendar days via BSA E-Filing |
| Currency | Coin and paper money only (excludes cashier's checks, money orders) |

**Exemptions (31 CFR § 1020.315):** Banks, government entities, listed public companies, qualifying businesses. Require documentation, approval, biennial renewal, annual review.

## Step 8: OFAC Compliance

| Trigger | Timing |
|---|---|
| Account opening | Before relationship established |
| Existing customers | Minimum annually; risk-based frequency |
| Transactions (wires, ACH) | Real-time or near real-time |

**Lists:** SDN, Consolidated Sanctions, country-based programs.

**Actions:**
- **Blocking** — mandatory for sanctioned persons' property; interest-bearing account; report to OFAC within 10 business days
- **Rejection** — prohibited transactions not requiring blocking; notify originator; document decision

**Retention:** All screening records ≥ 5 years.

## Step 9: Risk Assessment

| Dimension | Factors |
|---|---|
| Products/services | Velocity, geographic reach, anonymity, abuse susceptibility |
| Customers | Type, occupation, geography, relationship characteristics |
| Entities | Ownership structure, business purpose, formation jurisdiction |
| Geography | Physical presence, customer concentrations, FATF/State Dept. flags |

Assess **inherent** (pre-controls) and **residual** (post-controls) risk. Conduct annually minimum or upon significant changes. Findings drive CDD intensity, monitoring sensitivity, and resource allocation.

## Step 10: Training

| Audience | Timing |
|---|---|
| All employees/officers/directors | Annual minimum |
| New hires | Within 30 days or before customer-facing duties |
| High-risk positions | Role-specific schedule with specialized content |

**Core curriculum:** Institution AML policies · BSA/PATRIOT Act/FinCEN/OFAC · ML/TF typologies · red flags · CIP/CDD procedures · reporting obligations.

**Documentation:** Attendance records, completion certificates, comprehension assessments.

## Step 11: Independent Testing

| Element | Standard |
|---|---|
| Independence | Personnel independent of AML function |
| Frequency | 12–18 months; higher-risk more frequent |
| Reporting | Findings to Compliance Officer, management, board |

**Scope:** Regulatory compliance · policy adequacy · risk assessment methodology · transaction monitoring effectiveness · training adequacy · SAR/CTR timeliness · CIP/CDD compliance · OFAC procedures.

**Remediation:** Management response required; action plans with timelines; follow-up verification.

## Step 12: Governance

**Board duties:** Approve program and updates · review risk assessment · receive quarterly compliance reports · review testing results · allocate resources.

**Quarterly metrics:** SAR/CTR activity, OFAC screening, CDD/EDD activities, training completion, testing findings, regulatory developments.

**Change management:** Document rationale → compliance + legal review → management/board approval → communicate to personnel → maintain version history.

## Step 13: Recordkeeping

| Record Type | Retention |
|---|---|
| SARs + supporting docs | 5 years from filing |
| CTRs + supporting docs | 5 years from filing |
| CIP/CDD/beneficial ownership | 5 years after account closure |
| OFAC screening/blocking | 5 years minimum |
| Risk assessments, testing, training | 5 years minimum |

Organized for prompt retrieval upon regulatory request. Security controls and audit trails for SAR-related records.

---

## Checkpoint B: Post-Draft Review (Mandatory)

After delivering the draft, ask the user:

1. Does the program scope match your institution's business lines and risk profile?
2. Are the CIP/CDD/EDD thresholds appropriate for your customer base?
3. Do the governance and reporting structures align with your board/committee framework?
4. Any enforcement history, consent orders, or MRAs that require specific program provisions?

## Quality Checks

- [ ] All 13 sections addressed with institution-specific detail
- [ ] CFR citations verified — uncertain citations marked [VERIFY]
- [ ] Risk-based approach: controls scaled to institution size and complexity
- [ ] SAR confidentiality protections embedded in relevant sections
- [ ] OFAC strict-liability posture reflected throughout
- [ ] Retention periods consistent across sections
- [ ] Disclaimer included: framework requires qualified legal counsel review and institution-specific tailoring

## Guidelines

- Mark uncertain CFR citations with [VERIFY] — regulations change; confirm at drafting date
- OFAC obligations are strict liability — err on the side of caution in all screening procedures
- SAR confidentiality violations carry serious penalties — embed protections in every relevant procedure and training module
- Program must be reviewed regularly for regulatory changes, emerging risks, and implementation lessons
- Consult legal counsel for interpretation questions
