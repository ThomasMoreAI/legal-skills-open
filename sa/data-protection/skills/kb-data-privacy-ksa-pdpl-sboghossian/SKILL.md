---
name: kb-data-privacy-ksa-pdpl-sboghossian
title: Knowledge Pack — KSA Personal Data Protection Law (PDPL)
description: Use when a matter involves personal data processing, privacy obligations, or data-breach response in Saudi Arabia. Covers the KSA Personal Data Protection Law (Royal Decree M/19 2021, effective 2022–2023) and NDMO implementing regulations, lawful bases, sensitive data categories, cross-border transfer restrictions, data subject rights, and PDPL penalties up to SAR 5 million. Triggers on questions about PDPL KSA, Saudi data privacy, SDAIA, NDMO compliance, or data controller obligations in Saudi Arabia.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-data-privacy-ksa-pdpl
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: data-protection
language: en
---

# Knowledge Pack — KSA Personal Data Protection Law (PDPL)

## Scope

Saudi Arabia's **Personal Data Protection Law (PDPL)** was enacted by Royal Decree M/19 dated 9/2/1443H (September 2021) and became operative for most entities in **September 2023** following a phased rollout supervised by:

- **SDAIA** — Saudi Data and Artificial Intelligence Authority (policy and enforcement)
- **NDMO** — National Data Management Office (implementing regulations and technical guidance)

The PDPL applies to:
- Any entity (public or private) that processes personal data of **individuals located in Saudi Arabia** at the time of processing.
- Extra-territorial: foreign entities processing KSA residents' data to offer goods/services or to monitor behavior in KSA.
- Excluded: data processed for personal/family purposes; national security, crime, or judicial processing by competent authorities; deceased persons' data (except where linked to living persons).

## Key Definitions

| Term | PDPL Definition |
|---|---|
| Personal data | Any data that identifies or allows identification of a natural person |
| Sensitive data | Health and medical data; genetic and biometric data; credit/financial data; location data of a continuous or systematic nature; data revealing racial, ethnic, religious, or political views |
| Controller | Entity that determines purpose and means of processing |
| Processor | Entity processing on behalf of a controller |
| NDMO | National Data Management Office — technical regulation |
| SDAIA | Saudi Data and AI Authority — enforcement and policy |

## Lawful Bases for Processing

Unlike GDPR, the KSA PDPL uses a narrower set of lawful bases:

1. **Controller's legitimate interest** — processing that does not override data subject's interests; proportionality required.
2. **Public interest** — government and public sector tasks.
3. **Legal obligation** — required by applicable Saudi law.
4. **Contract** — necessary to perform a contract to which the data subject is a party.
5. **Vital interests** — protect life or health.
6. **Consent** — required specifically for sensitive data and for direct marketing; otherwise not the primary basis.

### Sensitive data processing
Requires **explicit consent** of the data subject **plus** one of the following additional grounds:
- Legal obligation or judicial procedure
- Legitimate public interest established by regulation
- Protection of vital interests when data subject is unable to consent

## Data Subject Rights

| Right | Mechanism |
|---|---|
| Access | Request copy of personal data held; no charge for first request annually |
| Rectification | Correct inaccurate or outdated data |
| Erasure | Delete when purpose fulfilled, consent withdrawn, or no longer legally required |
| Restriction / objection | Object to processing for direct marketing; request restriction during dispute |
| Portability | Receive data in portable format (limited to specific contexts under implementing regs) |
| Withdraw consent | At any time for consent-based processing |

- Response deadline: **30 days** (extendable once with notice).
- NDMO may issue further guidance on specific rights implementation.

## Consent Requirements

- Must be **written** (or electronic equivalent) when required.
- **Explicit** for sensitive data.
- **Specific** to the purpose — bundled/blanket consent does not satisfy the requirement.
- **Withdrawable** — controllers must maintain mechanisms for withdrawal.
- Consent from **minors** under 18 requires guardian consent.

## Cross-Border Data Transfers

Transfer of personal data outside Saudi Arabia is **prohibited** unless:

1. The destination country provides **adequate protection** — per NDMO adequacy list (currently being developed; GDPR-equivalent jurisdictions used as benchmark).
2. **Contractual safeguards** approved by NDMO (model clauses or binding corporate rules).
3. **Explicit consent** of the data subject for the specific transfer and its risks.
4. Transfer necessary for contract performance, judicial proceedings, or legal claims.
5. Transfer necessary to protect vital interests when data subject is unable to consent.
6. The transfer is in the **public interest** established by law.

Controllers must document transfer basis and obtain NDMO approval for certain categories.

## Data Breach Obligations

- Notify **NDMO within 72 hours** of becoming aware of a breach likely to harm data subjects.
- Notify **affected data subjects without undue delay** when the breach may directly affect their rights or interests.
- Maintain internal incident register.
- Implement preventive technical and organizational security measures.

## Security Requirements

- Implement **technical and organizational security measures** proportionate to the nature and risk of processing.
- Physical, administrative, and technical safeguards required.
- **Data Processing Agreements (DPAs)** with processors mandatory; processors must provide equivalent security guarantees.
- Retention limitation: data must be deleted once the purpose is achieved unless retention is required by law.

## Penalties

| Violation | Administrative Penalty |
|---|---|
| Transfer of personal data outside KSA without authorization | SAR 3,000,000 (up to SAR 5,000,000 for repeat) |
| Processing sensitive data without required consent/grounds | SAR 3,000,000 |
| Violating data subject rights | SAR 1,000,000 |
| Failure to implement security measures / breach notification | SAR 2,000,000 |
| General PDPL violation | SAR 1,000,000 (up to SAR 2,000,000 for repeat) |

- Criminal penalties possible for intentional violations causing harm.
- SDAIA may publish violator names publicly (naming and shaming).
- Repeat violations trigger doubled fines.

## Sector-Specific Overlays

| Sector | Additional regulator |
|---|---|
| Financial / banking | SAMA (Saudi Central Bank) — data and cybersecurity guidance |
| Fintech / crypto | CMA + SAMA data governance requirements |
| Health data | Ministry of Health data governance standards |
| Telecom / cloud | CITC data localization and cybersecurity requirements |
| Government data | NCA (National Cybersecurity Authority) cloud and data policies |

Health data and financial data are **sensitive data** under PDPL and require heightened protections.

## Data Localization

- KSA does not impose a blanket data-localization requirement under PDPL.
- However, **sector-specific regulations** (particularly SAMA, MOH, and CITC) impose localization requirements for certain categories of regulated data (financial records, health records, telecom data).
- Cloud computing and SaaS agreements must address localization obligations per sector.

## Compliance Checklist

- [ ] Data mapping: inventory all personal data flows in KSA operations
- [ ] Identify and document lawful basis for each processing activity
- [ ] Obtain explicit consent for sensitive-data processing
- [ ] Review and update privacy notices (Arabic mandatory; bilingual recommended)
- [ ] Establish consent-withdrawal mechanisms
- [ ] Put Data Processing Agreements in place with all processors
- [ ] Assess cross-border transfer mechanisms for data leaving KSA
- [ ] Implement 72-hour breach notification procedure
- [ ] Establish data subject rights request-handling process
- [ ] Check sector-specific data localization obligations

## Comparison with GDPR

| Feature | KSA PDPL | GDPR |
|---|---|---|
| Primary regulator | SDAIA / NDMO | National DPA (country-specific) |
| Consent model | Required for sensitive data / marketing; legitimate interest basis available | Six bases; consent one of six |
| DPO | Not specifically mandated (NDMO guidance may specify) | Mandatory in certain cases |
| Max fine | SAR 5M | €20M / 4% global turnover |
| Breach notification | 72 hours to NDMO | 72 hours to national DPA |
| Extra-territorial | Yes | Yes |

## Caveats & Currency

The PDPL's implementing regulations and NDMO guidance have been issued in phases. The adequacy list, approved model clauses, and sector-specific guidance are still developing as of 2025. Consult current NDMO publications before advising. SAMA, CITC, and MOH layered obligations require separate verification per sector.

## Related Skills

- [[kb-data-privacy-gdpr]]
- [[kb-data-privacy-egypt]]
- [[kb-data-privacy-uae-pdpl]]
- [[kb-fintech-licensing-cma-ksa]]
- [[kb-healthcare-regulation-mena]]
- [[draft-data-processing-agreement]]
- [[draft-privacy-policy]]
