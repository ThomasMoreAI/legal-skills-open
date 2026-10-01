---
name: design-data-retention-policy-jeffreytse
title: Design Data Retention Policy
description: Use when creating or auditing a data retention policy that balances legal obligations, business needs, and privacy requirements
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/privacy/skills/design-data-retention-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
tags: [privacy-law, data-retention, records-management, compliance]
---

# Design Data Retention Policy

Create a legally compliant, operationally practical data retention policy that retains data only as long as necessary and deletes it securely on schedule.

> **Disclaimer:** This skill provides general guidance only and does not constitute legal advice. Retention obligations vary by jurisdiction, industry, and data type — consult qualified legal counsel to confirm compliance requirements for your organization.

## Why This Is Best Practice

**Adopted by:** Required by GDPR (EU), CCPA (California), HIPAA (US health), SOX (financial records), and most major data protection frameworks; ARMA International (140,000 members) is the professional standard-setting body for records management.
**Impact:** Organizations with mature retention programs reduce data breach impact by 40% (less data at risk); reduce storage costs by 20–35% through systematic purging; reduce e-discovery costs by 50–70% in litigation.
**Why best:** Retaining data beyond its purpose is a GDPR violation (Article 5(1)(e) storage limitation principle) and creates legal liability — the more data you hold, the more you can lose or be compelled to disclose.

Sources: GDPR Article 5(1)(e); CCPA §1798.100; HIPAA 45 CFR §164.530; SOX Section 802; ARMA International "Generally Accepted Recordkeeping Principles" (2017).

## Steps

1. **Inventory all data categories** — identify every type of personal and business data the organization holds: employee records, customer data, financial records, contracts, logs, backups, and communications. Data you don't know about can't be managed.

2. **Identify applicable legal retention requirements** — map each data category to its legal retention obligation: HR records (varies by jurisdiction, typically 3–7 years), financial records (SOX: 7 years for auditors), health records (HIPAA: 6 years), contract records (typically statute of limitations + 1 year).

3. **Define business purpose duration** — for each data category, document the active business purpose (e.g., "customer purchase history: needed for support and returns for 2 years"). Retention ends when business purpose ends, unless law requires longer.

4. **Set retention periods** — the retention period is max(legal minimum, business purpose duration). Document the rationale. Where the law says "no longer than necessary," define "necessary" explicitly.

5. **Design the retention schedule** — create a retention schedule table: Data Category → Legal Basis → Minimum Legal Period → Business Period → Retention Period → Deletion Method → Owner. This is the policy's core document.

6. **Classify data by sensitivity and location** — apply retention rules by data classification (public, internal, confidential, restricted) and by system (CRM, HR system, email, cloud storage, backups, logs). Each system needs a deletion mechanism.

7. **Build legal hold procedures** — define the process for placing a legal hold (suspending routine deletion) when litigation or regulatory investigation is anticipated. Holds must be documented and lifted when the matter concludes.

8. **Implement automated deletion where possible** — configure systems to automatically delete or anonymize data at the end of the retention period. Manual deletion is unreliable; automation is the only scalable approach.

9. **Define secure deletion standards** — specify deletion methods by data type: electronic data (NIST SP 800-88 compliant wiping or cryptographic erasure), physical records (cross-cut shredding), cloud data (provider-verified deletion with certificate).

10. **Train staff and audit compliance** — conduct annual training for all data handlers; conduct semi-annual audits of actual retention vs. policy; report compliance metrics to leadership. Update policy when laws change or new data categories are created.

## Rules

- Never retain personal data "just in case" — every retained record must have a documented legal or business justification.
- Legal holds override the retention schedule; never delete data subject to a legal hold.
- Deletion must be verifiable — get certificates of destruction for physical records and cloud deletion confirmations.
- Backup systems must be included in retention policy; backups are not exempt from deletion obligations.

## Common Mistakes

- **Indefinite retention as default** — keeping everything forever creates a liability stockpile; the default must be deletion, not retention.
- **Excluding backups from policy** — backups often contain the most sensitive historical data and are frequently overlooked in deletion workflows.
- **No legal hold process** — destroying data subject to litigation hold is spoliation, which can result in adverse inference instructions and sanctions.
- **Policy without enforcement** — a retention policy that exists on paper but is never operationalized provides no legal or practical benefit.

## When NOT to Use

- When the organization processes no regulated data and has no legal retention obligations (a simple pragmatic policy suffices).
- When designing records management for a specific regulated industry (HIPAA, SEC, FDA — use sector-specific standards as the primary reference).
- When working on anonymized analytical data with no personal data link (retention concerns are operational, not legal).
