---
name: audit-gdpr-compliance-jeffreytse
title: Audit GDPR Compliance
description: Use when assessing an organization's compliance with the General Data Protection Regulation
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/privacy/skills/audit-gdpr-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
tags: [law, privacy, gdpr, compliance, ropa, dpa]
---

# Audit GDPR Compliance

Systematically assess an organization's GDPR compliance posture across data processing activities, documentation, and technical controls.

## Why This Is Best Practice

**Adopted by:** EDPB, national Data Protection Authorities (DPAs), CNIL (France), ICO (UK), BfDI (Germany); required for all organizations processing EU personal data
**Impact:** GDPR maximum fines reach €20M or 4% of global annual turnover, whichever is higher; in 2023, Meta received a €1.2B fine; Amazon received €746M in 2021. The majority of fines stem from auditable failures: no legal basis, no DPA, no ROPA.

**Why best:** GDPR compliance is an ongoing accountability obligation, not a one-time project. Organizations that invest in structured compliance programs (ROPA, DPIAs, vendor management) demonstrate accountability to DPAs, reducing both enforcement risk and fine quantum when incidents occur.

## Steps

1. **Map all personal data processing activities** — Identify every operation involving personal data: collection, storage, use, disclosure, transfer, deletion. For each: what data is collected, from whom, for what purpose, on what legal basis, stored where, retained how long, and who has access.
2. **Build and maintain the Article 30 ROPA** — Records of Processing Activities (ROPA) must be maintained by all organizations with > 250 employees or processing that poses risk; required fields: controller/processor name, purposes of processing, categories of data subjects and personal data, recipients, third-country transfers, retention periods, security measures.
3. **Establish legal basis for each processing activity** — Map each processing activity to one of six lawful bases (Article 6): consent, contract, legal obligation, vital interests, public task, legitimate interests; document the basis; reliance on legitimate interests requires a Legitimate Interests Assessment (LIA).
4. **Audit consent mechanisms** — Where consent is the legal basis: confirm it is freely given (no pre-ticked boxes), specific, informed, unambiguous (affirmative action), and easily withdrawable; document consent records including what was consented to and when.
5. **Review Data Subject Rights procedures** — Confirm operational processes exist for: Subject Access Requests (30-day response deadline), Right to Erasure, Right to Rectification, Right to Data Portability (machine-readable format), Right to Object; test each process end-to-end.
6. **Audit third-party data processors** — Identify all vendors processing personal data on your behalf; confirm a written Data Processing Agreement (DPA) exists with each (Article 28 requirement); DPA must include: processing subject matter, duration, nature, purpose, data categories, data subject categories, and controller obligations.
7. **Assess cross-border data transfers** — Identify any transfers of personal data to countries outside the EEA; confirm an adequate transfer mechanism for each: EU adequacy decision, Standard Contractual Clauses (SCCs), Binding Corporate Rules (BCRs), or derogations; update SCCs to 2021 version.
8. **Conduct Data Protection Impact Assessments (DPIAs)** — Required for high-risk processing: systematic profiling, processing sensitive data at scale, systematic monitoring, biometric data, automated decision-making with significant effects; conduct before starting high-risk processing, not after.

## Rules

- Never rely on consent as the legal basis for processing where there is a significant power imbalance between controller and data subject (e.g., employer-employee); use legitimate interests or contract instead.
- Always appoint a Data Protection Officer (DPO) if your organization is a public authority, or conducts large-scale systematic monitoring, or processes special category data at scale.
- Ensure privacy notices (Article 13/14) are provided at the time of collection; notices must be concise, transparent, intelligible, and in plain language.
- Data breach notification to the supervisory authority is required within 72 hours of becoming aware of a breach (Article 33); do not wait for full investigation before notifying.
- Implement data minimization: collect only the personal data that is adequate, relevant, and limited to what is necessary for the specified purpose.

## Examples

**ROPA entry for customer email marketing:** Controller: ACME Corp. Purpose: email marketing. Legal basis: consent (Article 6(1)(a)). Data categories: name, email address, purchase history. Data subjects: EU customers. Recipients: email service provider (Mailchimp — DPA executed). Retention: 2 years from last interaction or until consent withdrawn. Transfer mechanism: EU-US Data Privacy Framework. Security: TLS encryption in transit, AES-256 at rest.

## Common Mistakes

- **Treating GDPR as a one-time project** — GDPR compliance requires continuous maintenance: new processing activities need legal basis mapping; new vendors need DPAs; consent records must be maintained; ROPA must be kept current.
- **Relying on pre-ticked boxes for consent** — Pre-ticked checkboxes are explicitly invalid under GDPR; consent requires an affirmative opt-in action.
- **No documented process for Subject Access Requests** — The 30-day deadline is non-negotiable; organizations without a documented SAR process routinely breach it, a common source of DPA complaints.

---

> **Law disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Consult a licensed attorney before making legal decisions.
