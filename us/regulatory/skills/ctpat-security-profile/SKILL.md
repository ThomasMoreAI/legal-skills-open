---
name: ctpat-security-profile
title: C-TPAT Security Profile
description: 'Drafts a submission-ready C-TPAT Security Profile from verified company records for U.S. CBP enrollment, recertification, or validation prep. Use when preparing security profiles for importers, brokers, freight forwarders, or logistics participants. Trigger keywords: C-TPAT, CTPAT, CBP, security profile, customs compliance, validation visit, revalidation.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ctpat-security-profile
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, memo]
---

# C-TPAT Security Profile

Produces an evidence-based C-TPAT profile draft aligned to U.S. CBP minimum security criteria, mapped directly to company operations and source documents.

## Quick Start

1. Collect governing docs (policies, SOPs, audits, training records, partner questionnaires).
2. Confirm corporate identifiers (legal name, EIN, DUNS, C-TPAT account number, facility addresses).
3. Gather operations data (importer role, volumes, countries/lanes, supply chain map).
4. Gather security evidence per module (physical, personnel, cargo, conveyance, IT, business partner).
5. Set document version baseline and submission target date.

## Core Workflow

1. **Validate inputs** — verify each factual claim against source documents.
2. **Identify gaps** — emit a Gap Register before drafting if required facts are missing.
3. **Draft sections** — populate all 13 mandatory sections (see below).
4. **Crosswalk compliance** — map each company control → C-TPAT minimum → supporting evidence.
5. **Quality check** — scan for accuracy, contradictions, completeness, and CBP-appropriate tone.

## Intake Matrix

| Domain | Evidence Needed | Maps To |
|---|---|---|
| Eligibility | Import role, volume, facilities, prior tier | Intro + jurisdiction |
| Governance | Security leadership, reporting lines, budget | Org framework |
| Risk methodology | Assessment cadence, criteria, data sources | Risk assessment |
| Physical controls | Access, surveillance, lighting, alarms, patrols | Physical security |
| Personnel | Screening, onboarding, training, revocations | Personnel security |
| Procedural | Partner due diligence, custody chain, inspections | Business-partner security |
| Conveyance | Carrier vetting, 7-point inspections, seals, transit | Conveyance/cargo integrity |
| IT | MFA, segmentation, patching, incident response | IT security |
| Compliance | Self-assessments, corrective actions, validation prep | Continuous improvement |

## Mandatory Sections

1. Cover Page — company info, title, version, date, preparer
2. Profile Summary — tier objective, participation status, confidence level
3. Organizational Framework
4. Risk Assessment
5. Physical Security
6. Personnel Security
7. Procedural / Business-Partner Security
8. Conveyance and Cargo Integrity
9. Information Technology Security
10. Recordkeeping and Compliance Management
11. Self-Assessment and Corrective Action Register
12. Validation Readiness
13. Appendix Index and Signature Statement

## Section Template

Each security module section follows this structure:

- **Current Practice** — fact-based description
- **Controls in place** — specific measures
- **Evidence references** — document name + date
- **Gaps and residual risks**
- **Planned improvements** — owner assigned
- **Status**: Compliant / Partially Compliant / Non-Compliant

## Specialized Records

**Seven-Point Inspection Log** (per container/trailer): Unit ID, date/time, inspector, front wall, left side, right side, floor, ceiling/roof, doors inside/out, undercarriage, anomalies + photos + corrective actions.

**Seal Control Register**: Seal number, vendor/standard, issuance date, assigned shipment, installation point, receipt verification, discrepancy response, disposition.

**Corrective Action Plan**: Finding, control owner, corrective action, deadline, verification method, status.

## Pitfalls and Checks

- Use only verifiable facts from provided records — never invent documents, certifications, or findings.
- Every claim requires a source pointer (policy, SOP, log, audit report, contract, training record).
- Use exact terms from company records for titles, systems, equipment, and locations.
- Mark uncertain regulatory specifics with [VERIFY] for human confirmation.
- Enforce 7-point inspection checks and ISO 17712 high-security seal handling.
- Default to U.S.-only CBP scope unless user provides multinational authority requirements [VERIFY].
- Final output must be validator-ready: consistent cross-references, indexed exhibits, revision control.
