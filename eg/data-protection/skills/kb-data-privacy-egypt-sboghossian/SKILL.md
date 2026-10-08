---
name: kb-data-privacy-egypt-sboghossian
title: Knowledge Pack — Egypt Personal Data Protection Law (Law 151/2020)
description: Use when a matter involves personal data processing, privacy obligations, or data-breach response in Egypt. Covers Egypt's Personal Data Protection Law (Law 151/2020) and its executive regulations, the role of the Personal Data Protection Centre (PDPC), consent requirements, data subject rights, cross-border transfer restrictions, and penalties. Triggers on questions about Egyptian data privacy compliance, PDPL Egypt, data controller obligations, or sensitive-data handling in Egyptian jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-data-privacy-egypt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eg
practice: data-protection
language: en
---

# Knowledge Pack — Egypt Personal Data Protection Law (Law 151/2020)

## Scope

Egypt's Personal Data Protection Law (Law No. 151 of 2020) and its Executive Regulations (Prime Ministerial Decree 1074/2022) constitute the country's first comprehensive data-protection framework. The law applies to:

- **Any entity** (natural or legal, public or private) that collects, stores, processes, or transmits personal data of individuals who are:
  - Located in Egypt at the time of processing, **or**
  - Egyptian nationals (regardless of location)
- **Extra-territorial reach**: foreign entities processing Egyptian residents' or nationals' data are covered.
- Exempted: purely personal/household use; national security and public order data processed by competent authorities; statistical research using anonymized data.

## Key Definitions

| Term | Egyptian Law Definition |
|---|---|
| Personal data | Any data that identifies or could identify a natural person |
| Sensitive data | Health, genetic, biometric, religious belief, political opinion, criminal records, financial data |
| Controller | Entity that determines purposes and means of processing |
| Processor | Entity that processes data on behalf of a controller |
| Processing | Any operation performed on personal data (collection, storage, use, transfer, erasure, etc.) |
| PDPC | Personal Data Protection Centre — supervisory authority |

## Lawful Bases for Processing

1. **Express consent** — written, explicit, and informed; may be withdrawn at any time.
2. **Contractual necessity** — processing necessary to perform a contract to which the data subject is a party.
3. **Legal obligation** — required by Egyptian law.
4. **Vital interests** — necessary to protect the life or health of the data subject or a third party.
5. **Public task** — processing by a public authority for a task in the public interest.
6. **Legitimate interests** — balance-of-interests test; **not available for sensitive data**.

### Sensitive data requires **explicit written consent** plus additional safeguards — no legitimate-interests basis.

## Data Subject Rights

| Right | Details |
|---|---|
| Access | Request a copy of personal data held |
| Rectification | Correct inaccurate or incomplete data |
| Erasure | Request deletion when legal basis ceases or consent withdrawn |
| Restriction | Suspend processing while dispute is resolved |
| Objection | Object to processing (especially direct marketing) |
| Portability | Receive data in a machine-readable format |
| Withdraw consent | At any time; withdrawal does not affect prior lawful processing |

- Controllers must respond to requests within **30 days** (extendable to 60 days with notice).

## Registration & Notification Obligations

- Controllers and processors that process **sensitive data** or that process **on a large scale** must **register with the PDPC** before commencing processing.
- Registration fee + periodic renewal.
- Prior notification to PDPC required for:
  - High-risk processing activities (DPIA-equivalent assessment required)
  - Automated decision-making affecting individuals
  - Large-scale processing of sensitive categories

## Cross-Border Data Transfers

- Transfer outside Egypt is **prohibited unless**:
  1. The destination country provides **adequate protection** (PDPC adequacy list — not yet published as of 2025; EU SCCs used as reference practice).
  2. **Contractual safeguards** approved by PDPC (standard contractual clauses or binding corporate rules).
  3. **Express consent** of the data subject for the specific transfer.
  4. Transfer is necessary for contract performance, legal claims, vital interests, or public interest.
- Controllers must document the transfer basis and retain records.

## Data Breach Obligations

- Notify **PDPC within 72 hours** of becoming aware of a breach that is likely to risk data subjects' rights or freedoms.
- Notify **affected data subjects without undue delay** if the breach is likely to cause high risk.
- Maintain internal breach register.

## Data Protection Officer (DPO)

- Required for:
  - Public authorities
  - Entities whose core activities involve **large-scale processing of sensitive data**
  - Entities whose core activities involve **large-scale systematic monitoring**
- DPO must have expertise in data-protection law; may be internal or external.

## Security Requirements

- Implement **technical and organizational measures** appropriate to the risk level.
- Measures include: encryption, pseudonymization, access controls, regular testing.
- Third-party processors must provide sufficient security guarantees; documented by a **Data Processing Agreement (DPA)**.

## Penalties

| Violation | Penalty |
|---|---|
| Processing without lawful basis or without consent | EGP 100,000 – 1,000,000 |
| Transfer outside Egypt without authorization | EGP 500,000 – 5,000,000 |
| Processing sensitive data without explicit consent | EGP 500,000 – 5,000,000 |
| Failure to notify breach | EGP 50,000 – 500,000 |
| General non-compliance | EGP 10,000 – 1,000,000 |
| Repeated violations | Doubled fines + criminal liability for responsible individuals |

## Supervisory Authority: PDPC

- **Personal Data Protection Centre (PDPC)** — under the Ministry of Communications.
- Powers: registration, inspection, investigation, issuing guidance, imposing fines.
- Complaint mechanism: data subjects may file complaints with PDPC.
- PDPC may issue binding guidance and codes of practice.

## Practical Compliance Checklist

- [ ] Map all personal data flows (data mapping / inventory)
- [ ] Identify and document lawful basis for each processing activity
- [ ] Update privacy notices / privacy policy (Arabic and English)
- [ ] Ensure consent mechanisms meet "explicit, informed, withdrawable" standard
- [ ] Register with PDPC if required (sensitive data / large-scale processing)
- [ ] Put **Data Processing Agreements** in place with all processors
- [ ] Establish cross-border transfer mechanisms for international data flows
- [ ] Implement breach detection and notification procedures
- [ ] Appoint DPO if triggered
- [ ] Conduct Data Protection Impact Assessments (DPIAs) for high-risk activities

## Comparison with GDPR and Regional PDPLs

| Feature | Egypt 151/2020 | GDPR (EU) | KSA PDPL | UAE PDPL |
|---|---|---|---|---|
| Adequacy mechanism | Yes (PDPC list) | Yes (EC list) | Yes (NDMO list) | Yes (DIFC/ADGM separate) |
| DPO mandatory | Large-scale/sensitive | Public/core activities | Not specified | Certain controllers |
| Max fine | EGP 5M | €20M / 4% global | SAR 5M | AED 20M |
| Breach notification | 72 hours to PDPC | 72 hours to DPA | 72 hours to SDAIA | 72 hours to TDRA |
| Extra-territorial | Yes | Yes | Yes | Yes |

## Caveats & Currency

Egypt's PDPC is newly established and enforcement practice is still developing. Executive Regulations were issued in 2022; implementing guidance continues to be published. Verify current PDPC adequacy lists, registration fees, and specific thresholds before advising. The penalty amounts above reflect the law as enacted; assess any amendments post-2023 with current sources.

## Related Skills

- [[kb-data-privacy-gdpr]]
- [[kb-data-privacy-ksa-pdpl]]
- [[kb-data-privacy-uae-pdpl]]
- [[kb-healthcare-regulation-mena]]
- [[draft-privacy-policy]]
- [[draft-data-processing-agreement]]
