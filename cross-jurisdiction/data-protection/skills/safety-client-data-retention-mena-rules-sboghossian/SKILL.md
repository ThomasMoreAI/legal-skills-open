---
name: safety-client-data-retention-mena-rules-sboghossian
title: Client Data Retention — MENA Jurisdiction Rules
description: Use when configuring or reviewing data retention periods for client matter files, communications, and AML records across MENA jurisdictions. Covers mandatory minimum retention periods for KSA (Saudi Bar + PDPL), UAE (Federal Law on Legal Profession + DFSA AML), Lebanon (Beirut/Tripoli Bar), Egypt, DIFC (DFSA), and ADGM (FSRA). Also covers anonymization vs hard-delete obligations, legal-hold overrides, and tax-record retention minimums.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-client-data-retention-mena-rules
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Client Data Retention — MENA Jurisdiction Rules

## When to use this

Apply when:
- Configuring automatic data-deletion or anonymization schedules for an eFirm tenant in a MENA jurisdiction.
- A lawyer asks how long they must keep client files.
- Responding to a client request to delete their data — does a legal-hold override apply?
- Auditing compliance with AML record-keeping obligations.
- Advising an in-house legal team on their document-retention policy for a MENA operation.

## Minimum retention periods by jurisdiction

### Saudi Arabia (KSA)

| Record type | Minimum period | Authority |
|-------------|---------------|-----------|
| Client matter files (general) | 5 years post-matter close | Saudi Bar Association rules; Code of Law Practice (Royal Decree M/38) |
| AML records (client due diligence, transaction records) | 10 years | Saudi AML Law; FATF 40 Recommendations implementation |
| Tax records | 10 years | Zakat, Tax and Customs Authority (ZATCA) requirements |

**Practical note**: the 5-year matter-file period is a professional minimum; some contracts or regulatory contexts require longer periods. CDD (Customer Due Diligence) records under AML rules must be kept for 10 years from the end of the business relationship.

### United Arab Emirates (UAE — Federal / Onshore)

| Record type | Minimum period | Authority |
|-------------|---------------|-----------|
| Client matter files (general) | 5 years post-matter close | Federal Decree-Law No. 23 of 1991 on the Legal Profession |
| AML records | 5 years minimum | UAE AML Law (Federal Decree-Law No. 20 of 2018); FATF implementation |
| DFSA-regulated entity records | 6 years | DFSA Rulebook (GEN Module) |
| Tax/VAT records | 5 years | UAE Federal Tax Authority |

**DIFC note**: for DFSA-regulated firms within DIFC, AML records must be retained for 6 years. Client files should be retained per the engagement letter, but minimum 5 years is the safe standard.

### ADGM

| Record type | Minimum period | Authority |
|-------------|---------------|-----------|
| AML records (FSRA-regulated) | 6 years | FSRA AML Rules |
| Client files | Per engagement letter; minimum 5 years recommended | ADGM Court and FSRA guidance |

### Lebanon

| Record type | Minimum period | Authority |
|-------------|---------------|-----------|
| Client matter files | 10 years (typical practice) | Beirut Bar / Tripoli Bar internal rules |
| AML records | 5 years minimum; 7–10 years for higher-risk matters | Lebanese AML Law (Law 44 of 2015) |

**Practical note**: Lebanon does not have a comprehensive personal-data-protection law as of May 2026. The retention obligations derive from bar rules and sector-specific AML legislation. Law 44 of 2015 (AML) and the associated Circular of the Banking Control Commission set the AML record standard.

### Egypt

| Record type | Minimum period | Authority |
|-------------|---------------|-----------|
| Client matter files | 10 years (typical practice) | Egyptian Bar regulations |
| AML records | 5 years post-transaction | Egypt AML Law (Law 80 of 2002, as amended) |
| Tax records | 5 years | Egyptian Tax Authority |

### Bahrain

| Record type | Minimum period | Authority |
|-------------|---------------|-----------|
| AML records | 5 years post-transaction | Bahrain AML Law; CBB Rulebook |
| Client files | 5 years (professional practice standard) | Bahrain Bar rules |

## End-of-retention procedures

When the retention period has elapsed:

1. **Anonymize, then delete (preferred over hard-delete)**: anonymize the data (remove all direct and indirect identifiers) rather than immediately hard-deleting. This preserves aggregate matter data for conflict-checking history and statistical use while removing personal exposure.
2. **Confirm no legal hold**: before any deletion or anonymization, check whether the matter or client is subject to a legal-hold order (litigation hold, regulatory investigation, tax authority inquiry). If yes, the hold overrides the standard retention clock.
3. **Client request for early deletion**: honor where permitted by law; document the request and the action. Note that professional obligations (AML, bar rules) may prevent full early deletion even when requested.
4. **Tax records**: retain for the jurisdictionally required period (typically 5–10 years) regardless of other matter closure.

## Legal-hold override

A **legal-hold flag** in the matter management system overrides all automatic deletion and anonymization schedules. Legal holds are triggered by:
- Notice of litigation or regulatory investigation involving the matter.
- Court order or regulatory request to preserve records.
- Internal assessment that the matter may become contentious.

The hold remains in force until explicitly released by the matter's supervising lawyer. Release of a legal hold should be documented.

## Platform behavior

The platform provides:
- **Configurable retention period per matter**: set at tenant onboarding or per-matter by the supervising lawyer.
- **Automatic anonymization trigger**: at the retention threshold, the system flags the matter for review and anonymizes upon confirmation.
- **Legal-hold flag**: set per matter; prevents auto-deletion; surfaced in matter dashboard.
- **Client deletion request workflow**: generates a deletion/anonymization confirmation with legal-hold check.

## Common mistakes

- **Treating the matter-close date as the retention start**: the retention period typically runs from the **end of the client relationship** or **last transaction**, not from when the file was opened.
- **Forgetting AML retention is longer**: AML/CDD records in most MENA jurisdictions have a 10-year (KSA) or minimum-5-year (UAE, LB, EG) obligation — longer than general matter-file periods.
- **Hard-deleting too early**: early hard-deletion that violates professional retention rules could expose the firm to regulatory sanctions; anonymization is safer and usually sufficient.
- **Ignoring tax records**: tax records have their own retention clocks and may extend beyond both matter-file and AML periods.

## Related skills

- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation and data segregation
- [[safety-cross-border-data-transfer-gcc-eu]] — cross-border transfer requirements for retained data
- [[safety-bar-rule-1-6-confidentiality-ai]] — confidentiality obligations for AI tool use
- [[safety-pii-redaction-before-rag]] — PII handling before external processing
- [[review-compliance-gap-analysis]] — gap-analysis workflow for compliance reviews
