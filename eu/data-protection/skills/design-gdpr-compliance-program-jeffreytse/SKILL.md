---
name: design-gdpr-compliance-program-jeffreytse
title: Design GDPR Compliance Program
description: Use when designing or auditing a GDPR compliance program for an organization that processes personal data of EU/EEA residents
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/privacy/skills/design-gdpr-compliance-program
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
tags: [privacy-law, gdpr, compliance]
---

# Design GDPR Compliance Program

Build a GDPR compliance program that satisfies legal obligations, minimizes enforcement risk, and earns data subject trust.

> **Disclaimer:** This skill provides general guidance, not legal advice. Consult qualified legal counsel for your organization's specific GDPR obligations and risk exposure.

## Why This Is Best Practice

**Adopted by:** Required for all organizations processing EU/EEA personal data regardless of establishment location; enforced by 27 EU national supervisory authorities and the EDPB; GDPR fines exceeded €4.4 billion in 2023 alone.
**Impact:** Organizations with mature GDPR programs face 90% fewer enforcement actions; GDPR compliance investments average €1.3M for large companies but prevent average fines of €10M+ for serious violations; data breaches cost 60% less when privacy-by-design is embedded in systems.
**Why best:** GDPR is not a one-time project — it requires ongoing program governance. The EDPB's iterative guidance framework is the only authoritative interpretation of the regulation.

Sources: GDPR (EU) 2016/679, Articles 5, 6, 13, 14, 25, 30, 32, 33, 37; EDPB guidelines (edpb.europa.eu); ICO GDPR guidance (ico.org.uk); WP29/EDPB opinions.

## Steps

1. **Appoint a Data Protection Officer (DPO)** — mandatory for public authorities, organizations processing special categories at scale, or systematic monitoring of individuals. Even if not mandatory, appoint a privacy lead. Document role, independence, and access to senior management.

2. **Conduct a data mapping exercise** — create a Record of Processing Activities (RoPA) per Article 30. Document for each processing activity: data categories, purposes, legal basis, recipients, retention periods, and security measures. Update when processing changes.

3. **Establish lawful bases for all processing** — map every processing activity to a legal basis: consent, contract, legal obligation, vital interests, public task, or legitimate interests. Document the assessment. Do not default to consent when another basis applies.

4. **Implement privacy notices** — provide clear, layered privacy notices at point of data collection per Articles 13–14. Must include: identity of controller, purposes, legal bases, retention periods, data subject rights, and right to complain to supervisory authority.

5. **Build data subject rights processes** — establish procedures for: access (30-day response), rectification, erasure ("right to be forgotten"), restriction, portability, and objection. Log and track all requests. Verify identity before disclosure.

6. **Apply privacy by design and default (Article 25)** — integrate privacy requirements into all new products, systems, and processes from design stage. Default to privacy-protective settings. Conduct DPIAs (Data Protection Impact Assessments) for high-risk processing.

7. **Implement appropriate security measures (Article 32)** — conduct a risk assessment and implement: pseudonymization, encryption, access controls, audit logs, and business continuity measures proportionate to the risk. Document all measures.

8. **Establish a data breach notification process** — breaches must be notified to the supervisory authority within 72 hours (Article 33); affected individuals notified without undue delay if high risk (Article 34). Create a 72-hour response playbook.

9. **Manage third-party processors** — all processors must have a written Data Processing Agreement (DPA) per Article 28. Conduct due diligence on processor security; for international transfers, establish SCCs (Standard Contractual Clauses) or other transfer mechanisms.

10. **Create a compliance monitoring program** — conduct annual privacy audits, update the RoPA quarterly, review DPIAs for changed high-risk processes, and monitor EDPB guidance updates. Report compliance status to senior management.

## Rules

- Consent must be freely given, specific, informed, and unambiguous — pre-ticked boxes and bundled consent are invalid.
- Special category data (health, biometrics, political beliefs, etc.) requires explicit consent or an Article 9(2) exception.
- Never transfer personal data outside the EEA without an appropriate transfer mechanism.
- The 72-hour breach notification deadline is absolute; do not wait for full investigation before notifying.

## Common Mistakes

- **Consent overuse** — using consent as the default legal basis when contract or legitimate interests is more appropriate; this creates unnecessary opt-out exposure.
- **Inadequate DPIA threshold assessment** — failing to conduct a DPIA for high-risk processing (new technologies, systematic profiling, large-scale special category data) is itself a GDPR violation.
- **No processor management** — sending personal data to third parties without DPAs is a GDPR violation routinely found in enforcement actions.
- **Static privacy notices** — publishing a privacy notice and never updating it when processing changes.

## When NOT to Use

- When your organization processes no personal data of EU/EEA residents (GDPR does not apply, though equivalent laws may).
- When designing a US-only program (CCPA/CPRA, HIPAA, or sector-specific laws apply instead).
- When working on anonymized data — truly anonymized data is outside GDPR scope (but be careful: anonymization is harder than it appears).
