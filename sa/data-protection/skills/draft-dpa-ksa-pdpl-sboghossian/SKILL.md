---
name: draft-dpa-ksa-pdpl-sboghossian
title: Data Processing Agreement — KSA Personal Data Protection Law (PDPL)
description: Use when drafting a Data Processing Agreement (DPA) compliant with the KSA Personal Data Protection Law (PDPL — Royal Decree M/19 2021, amended 2023). Covers PDPL Articles 27–32 mandatory requirements, bilingual Arabic/English requirement for SDAIA filings, cross-border transfer framework (SDAIA adequacy, SCC-equivalent safeguards, data localization), breach notification (72 hours to SDAIA), and penalty exposure up to SAR 5,000,000.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-dpa-ksa-pdpl
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: data-protection
language: en
---

# Data Processing Agreement — KSA Personal Data Protection Law (PDPL)

## When to use this

Use this skill when a Saudi-nexus data processing relationship requires a written DPA under the KSA Personal Data Protection Law (PDPL). The PDPL applies when:

- Personal data of Saudi residents or nationals is processed.
- A controller or processor is established in Saudi Arabia.
- Processing activities are directed at individuals in Saudi Arabia, regardless of the processor's location.

The instrument must be **bilingual Arabic/English** for SDAIA filings; Arabic controls.

For parallel GDPR requirements (e.g., a Saudi processor handling data on behalf of a European controller), use this skill alongside [[draft-dpa-gdpr]].

## Regulatory framework

| Item | Detail |
|------|--------|
| Primary law | Personal Data Protection Law (PDPL) — Royal Decree M/19, 9/2/1443H (16 Sept 2021) |
| Amendments | Amended by Royal Decree M/148 of 1444H (2023) — transitional period adjustments |
| Implementing regulations | PDPL Implementing Regulations issued by SDAIA (Saudi Data & AI Authority) |
| Regulator | SDAIA — Saudi Data & AI Authority |
| Effective date | September 14, 2023 (after extended transitional period) |
| Penalty exposure | Up to SAR 5,000,000 per violation (+ potential suspension orders + criminal referral for willful violations) |

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Controller (name, KSA CR number if applicable, address, DPO if any) | Primary compliance obligation bearer | — |
| Processor (name, address, nature of services) | Party processing on instructions | — |
| Subject matter of processing | For Annex I | — |
| Duration | Processing period + retention | Coterminous with services |
| Nature and purpose of processing | Annex I; governs permissible activities | — |
| Categories of data subjects | Saudi nationals, residents, or individuals in KSA | — |
| Categories of personal data | Standard vs. sensitive (health, financial, biometric, beliefs) | — |
| Sub-processors with locations | SDAIA requires documented controller approval mechanism | — |
| Technical and organizational measures | Mapped to SDAIA Cybersecurity Controls | SDAIA NCA framework |
| Cross-border transfer mechanism | Required for any transfer outside KSA | — |

## PDPL mandatory DPA provisions (Articles 27–32)

### 1. Written contract requirement (Article 27)
The PDPL requires a written contract between the controller and processor. A verbal or implied arrangement is non-compliant. Include an effective date and clearly state both parties' legal names and registration details.

### 2. Processing on documented instructions only (Article 27)
The processor may only process personal data strictly in accordance with the controller's written instructions. If the processor receives a lawful governmental request for data disclosure, it must notify the controller before complying unless prohibited from doing so by law.

### 3. Confidentiality obligations (Article 28)
All processor personnel with access to personal data must be bound by written confidentiality undertakings. The processor must document its data-access authorization procedures.

### 4. Appropriate technical and organizational measures (Article 28)
Security measures must be appropriate to the nature and sensitivity of the data and the risk of processing. SDAIA's implementing regulations and the National Cybersecurity Authority (NCA) Essential Cybersecurity Controls (ECC) provide the reference framework.

Required measures at minimum:
- Encryption at rest and in transit.
- Access controls with documented authorization matrix.
- Audit logging for data access and modifications.
- Incident detection and response procedures.
- Staff training on data protection.
- Physical access controls to processing facilities.

### 5. Sub-processing requires controller consent (Article 29)
- **Specific consent model** is the PDPL default: processor may not engage a sub-processor without the controller's prior written approval.
- Where the parties negotiate a **general authorization model** (pre-approved list with notification for additions), this must be explicitly agreed and the controller retains a time-limited right to object.
- Processor must flow down all PDPL obligations to each sub-processor.

### 6. Breach notification (Article 30)
- **To SDAIA**: within **72 hours** of the processor becoming aware of a personal data breach that is likely to pose a risk to data subjects.
- **To affected data subjects**: "without undue delay" if the breach is likely to result in high risk of harm.
- Processor must notify controller promptly (market standard: within 24 hours) to enable the controller to meet its SDAIA notification deadline.
- Notification content: nature of breach, categories and approximate number of data subjects affected, contact details of data protection officer, likely consequences, measures taken.

### 7. Data return and deletion (Article 31)
At end of the processing relationship, the processor must:
- Return all personal data to the controller, **or**
- Permanently delete all personal data — with written certification of deletion provided to the controller.
- Timing: within 30 days of termination (specify in the agreement; PDPL does not specify a number of days).
- Address: deletion of backup copies, test/staging environments.

### 8. Information and audit rights (Article 32)
The processor must:
- Provide all information the controller needs to demonstrate PDPL compliance on request.
- Permit and facilitate audits and inspections by the controller or its mandated auditor.
- Assist the controller in conducting data protection impact assessments.

## Annexes

### Annex I — Description of processing (Arabic + English)
| Field | Arabic term | Content |
|-------|-------------|---------|
| Subject matter | موضوع المعالجة | Description of services |
| Duration | مدة المعالجة | Processing period |
| Nature | طبيعة المعالجة | Activities: storage, analysis, transfer, etc. |
| Purpose | الغرض من المعالجة | Business purpose |
| Categories of data subjects | فئات أصحاب البيانات | Saudi nationals, residents, etc. |
| Categories of personal data | فئات البيانات الشخصية | List of data types |
| Sensitive personal data | البيانات الحساسة | Health, financial, biometric, beliefs, criminal records |

### Annex II — Technical and organizational security measures
Map measures to the SDAIA Implementing Regulations and NCA Essential Cybersecurity Controls (ECC-1:2018). Include:
- Network security controls.
- Identity and access management (IAM).
- Asset management and classification.
- Vulnerability management and patch cycles.
- Business continuity and disaster recovery (BCDR).
- Security incident management procedure.
- Cloud security (if applicable — cloud service providers in KSA must meet CST cloud regulations).

### Annex III — Sub-processor register
| Sub-processor | Legal entity | Country | Services | Approval status |
|---|---|---|---|---|
| [Name] | [Entity] | [Country] | [Services] | Pre-approved / pending controller approval |

## Cross-border data transfers

The PDPL adopts a **data localization preference** for sensitive personal data; standard personal data may be transferred internationally subject to conditions:

| Transfer mechanism | Description | Practical use |
|---|---|---|
| **SDAIA adequacy decision** | SDAIA may designate countries/regions with adequate protection (no list published at time of writing) | Limited applicability pending SDAIA adequacy list |
| **Contractual safeguards** | SCC-equivalent contractual terms approved by SDAIA; or binding corporate rules for intra-group transfers | Standard approach for international B2B transfers |
| **Explicit consent** | Data subject's explicit, specific consent to transfer | Narrow use case; not appropriate for employment data or ongoing SaaS processing |
| **Necessity derogations** | Performance of a contract to which the data subject is party; legal claims; protection of vital interests | Limited; not for routine transfers |

**Sensitive personal data** (health, financial, biometric, religious beliefs, criminal records) requires additional safeguards for cross-border transfer. Controller must maintain documentation of transfer justification.

Data sovereignty: some KSA government and regulated-sector contracts require data to be stored entirely within the Kingdom. Confirm whether government or regulated-sector requirements apply.

## Bilingual requirement

The DPA must be executed in **Arabic** for SDAIA filings and regulatory proceedings. An English version may be provided for working purposes, but:
- Arabic text controls in the event of any inconsistency.
- Ensure the Arabic translation is accurate and is reviewed by a native Arabic legal translator (not machine-translated).
- In the event of enforcement action by SDAIA, the Arabic version will be the operative document.

## Penalty exposure — inform commercial negotiations

When negotiating liability caps in the DPA, surface the following to the client:

| Violation | Maximum penalty |
|-----------|----------------|
| Non-compliance with PDPL data-processing requirements | SAR 1,000,000 |
| Cross-border transfer without proper safeguards | SAR 3,000,000 |
| Breach of sensitive personal data provisions | SAR 5,000,000 |
| Repeat violation | Fine doubled; suspension of data-processing activities |

These penalties inform the appropriate scale of indemnification caps in the DPA — a cap below the maximum penalty exposure may be challenged as unconscionable in SDAIA proceedings.

## Common mistakes

1. **Treating PDPL as identical to GDPR** — the PDPL has material differences, especially on cross-border transfers, sensitive data requirements, and the lack of an established adequacy list.
2. **English-only DPA** — unenforceable before SDAIA; must have Arabic version.
3. **Missing breach notification timeline to controller** — the PDPL's 72-hour SDAIA notification deadline means the processor must notify the controller within 24 hours, not 72.
4. **No data localization analysis** — for sensitive data or government/regulated-sector processing, localization may be mandatory.
5. **Blanket sub-processor pre-approval** — PDPL default is specific consent; blanket pre-approval without notification mechanism may be non-compliant.
6. **Annex II mapped to ISO 27001 only** — SDAIA and NCA expect mapping to KSA-specific frameworks (NCA ECC); reference both.

## Related skills

- [[draft-dpa-gdpr]] — GDPR DPA; use alongside this skill for dual-regulation situations
- [[draft-dpa-uae-pdpl]] — UAE Federal Decree-Law 45/2021 DPA
- [[draft-privacy-policy]] — Arabic/English privacy notice required under PDPL
- [[kb-data-privacy-mena]] — reference pack on data privacy law across MENA including PDPL
