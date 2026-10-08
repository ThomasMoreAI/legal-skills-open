---
name: draft-dpa-gdpr-sboghossian
title: Data Processing Agreement (GDPR — Article 28)
description: Use when drafting a Data Processing Agreement (DPA) compliant with GDPR Article 28. Covers all mandatory clauses, the three standard annexes (description of processing, technical/organizational measures, sub-processor list), international transfer mechanisms (SCCs, adequacy, BCRs), UK-GDPR adaptations (IDTA), sub-processor authorization models, audit rights, and liability allocation. P0 data-privacy skill applicable to any controller-processor relationship where EU/EEA personal data is processed.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-dpa-gdpr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# Data Processing Agreement (GDPR — Article 28)

## When to use this

A DPA is legally mandatory under GDPR Article 28(3) whenever a **controller** engages a **processor** to process personal data on its behalf. Common scenarios:

- A SaaS vendor (processor) processes customer data for a business (controller).
- A law firm (processor) handles client personal data under instructions from the client (controller).
- An HR software provider processes employee data for an employer.
- A cloud provider stores personal data from an EEA-based business.
- Any outsourcing arrangement touching EU personal data.

If the relationship involves DIFC or ADGM entities, pair with DIFC Law 5/2020 or ADGM Data Protection Regulations 2021 DPA variants — both are closely modeled on GDPR but have distinct enforcement authorities.

For processing in the UAE mainland or Saudi Arabia, use [[draft-dpa-uae-pdpl]] or [[draft-dpa-ksa-pdpl]] respectively as the primary instrument.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Controller (name, address, DPO if any) | Party giving processing instructions; bears primary liability | — |
| Processor (name, address, DPO if any) | Party processing on controller's behalf | — |
| Subject matter of processing | Core description for Annex I | — |
| Duration of processing | Period for Annex I; determines retention obligations | Coterminous with main services agreement |
| Nature and purpose of processing | Annex I: the "why" | — |
| Categories of data subjects | Annex I: employees, customers, users, etc. | — |
| Categories of personal data | Annex I: names, contact data, health data, financial data | — |
| Sub-processors (names, countries, services) | Annex III; authorization model | — |
| Technical and organizational measures (TOMs) | Annex II: encryption, access controls, backups | Processor provides on request |
| International transfer mechanism | If data flows outside EEA/UK | SCCs Module 2 default |

## Mandatory clauses (Article 28(3))

GDPR Article 28(3) specifies eight mandatory provisions. Every DPA must include all of them:

### 1. Processing on documented instructions only
> "The Processor shall process Personal Data only on documented instructions from the Controller, including with regard to transfers of Personal Data to a third country or an international organisation, unless required to do so by Union or Member State law to which the Processor is subject; in such a case, the Processor shall inform the Controller of that legal requirement before processing, unless that law prohibits such information on important grounds of public interest."

Include a mechanism for issuing instructions (written; email from designated contacts; ticketing system for SaaS).

### 2. Confidentiality obligations on Processor's personnel
All Processor staff with access to Personal Data must be bound by written confidentiality obligations or professional secrecy obligations.

### 3. Security measures (Article 32)
The Processor must implement appropriate technical and organizational measures (Annex II). The standard references Article 32 factors: nature, scope, context, and purposes of processing; risk to data subjects. Annex II must be specific — a reference to "industry-standard security" is insufficient.

### 4. Sub-processing — authorization and flow-down
Two models:
- **Specific authorization**: Controller approves each sub-processor individually in writing before engagement. High control, low flexibility.
- **General authorization**: Processor may add sub-processors with notice (typically 14–30 days) to Controller; Controller has a right to object. Standard for SaaS businesses with dynamic sub-processor ecosystems.

Regardless of model: flow-down obligation — Processor must impose the same data-protection obligations on each sub-processor by contract; Controller must be listed as a third-party beneficiary or Processor must audit and warrant compliance.

### 5. Assist Controller with data subject rights and impact assessments
Processor assists Controller in responding to data subject requests (access, rectification, erasure, restriction, portability, objection) within the response window (Controller has 30 days under GDPR for most requests; 72 hours for some).

Processor also assists Controller with:
- Privacy impact assessments (DPIAs) — Article 35.
- Prior consultation with supervisory authority — Article 36.
- Article 32 security obligations.

Define "assist" with specificity: who bears the cost of unusual or burdensome requests?

### 6. Personal data breach notification
> "The Processor shall notify the Controller **without undue delay** after becoming aware of a personal data breach."

In practice, this means within 24–48 hours to allow the Controller time to assess and file its notification with the supervisory authority within 72 hours (Article 33 GDPR).

Specify notification content: nature of breach, categories and approximate number of data subjects and records, likely consequences, measures taken or proposed. Reference the Article 33(3) notification template.

### 7. Return or deletion at end of services
At the Controller's election (not the Processor's default choice), the Processor must:
- Return all Personal Data to the Controller, or
- Delete all Personal Data (and confirm deletion in writing).

Address: format of returned data; deletion of backup copies; timing (typically 30–90 days post-termination).

### 8. Audit rights
The Processor must:
- Make available all information necessary to demonstrate compliance.
- Allow and contribute to audits and inspections conducted by the Controller or a mandated auditor.

Define audit scope (systems, records, personnel interviews), frequency (typically once per year unless a security incident occurs), notice period (30 days standard), cost allocation (Controller bears audit costs; Processor bears reasonable internal costs), and confidentiality of audit findings.

Processor may satisfy audit right by providing third-party audit reports (ISO 27001, SOC 2 Type II) in lieu of on-site audit.

## Annexes

### Annex I — Description of processing
| Field | Content |
|-------|---------|
| Subject matter | Brief description of the services (e.g., "hosting of customer data management platform") |
| Duration | Period of data processing (e.g., "for the duration of the Services Agreement and [X] months thereafter") |
| Nature of processing | Activities performed: storage, transmission, analysis, deletion |
| Purpose of processing | The business purpose on behalf of the Controller |
| Categories of data subjects | Employees, customers, end-users, prospects, etc. |
| Categories of personal data | Names, email addresses, IP addresses, financial data, health data (flag if special-category data) |
| Sensitive / special-category data | Yes/No; if yes, enhanced measures and explicit Controller instruction required |

### Annex II — Technical and organizational measures
Must be specific and verifiable. At minimum include:

| Measure | Description |
|---------|-------------|
| Encryption | At rest (AES-256 or equivalent); in transit (TLS 1.2+ or equivalent) |
| Access controls | Role-based access; principle of least privilege; MFA for privileged accounts |
| Physical security | Data center certifications (ISO 27001, SOC 2, Tier III/IV) |
| Backup and recovery | Frequency, retention, tested recovery procedures |
| Incident response | Detection, containment, notification procedures |
| Pseudonymisation | If applicable |
| Data minimisation | Processes to ensure only required data is processed |
| Vendor management | Sub-processor security assessments |
| Personnel training | Annual data-protection and security awareness |

### Annex III — Sub-processor list
| Sub-processor | Entity/Address | Services | Data transferred | Country |
|---------------|----------------|----------|-----------------|---------|
| [Name] | [Legal entity + address] | [e.g., cloud hosting] | [categories] | [country] |

## International transfers

### EEA to third countries
If Personal Data will be transferred outside the EEA:

| Mechanism | When to use | Notes |
|-----------|-------------|-------|
| **Adequacy decision** | Country on EU Commission adequacy list (UK, Switzerland, Japan, South Korea, Israel, etc.) | No additional safeguards required |
| **Standard Contractual Clauses (SCCs)** | Most common for B2B transfers | Use Module 2 (Controller → Processor) or Module 3 (Processor → Processor). Incorporate the Annex III TIA (Transfer Impact Assessment) |
| **Binding Corporate Rules (BCRs)** | Intra-group transfers within a multinational group | Requires supervisory authority approval; lengthy process |
| **Article 49 derogations** | Limited use cases (explicit consent, contractual necessity, vital interests, public interest) | Cannot be used as a substitute for ongoing transfers |

MENA note: at the time of writing, no MENA jurisdiction has EU adequacy status. Transfers to UAE (mainland, KSA, LB, EG) require SCCs or BCRs. Transfers to DIFC (which has its own DIFC Law 5/2020) may use adequacy recognition between DIFC and EU.

### UK-GDPR adaptations
For transfers from the UK (post-Brexit):
- Use the **UK International Data Transfer Agreement (IDTA)** (IDTA October 2022) — replaces EU SCCs for transfers from UK.
- Alternatively, use the **UK Addendum to EU SCCs**.
- If the entity operates in both EU and UK, consider a combined EU-SCC + UK Addendum structure.

## Key negotiation points

### Sub-processor authorization
- SaaS vendors uniformly insist on general authorization with notice; enterprise clients often push for specific authorization or veto rights.
- Acceptable compromise: general authorization with a materiality threshold (Controller can object to new sub-processors processing sensitive data or core data).

### Audit rights
- Processors resist open-ended on-site audit rights.
- Acceptable compromise: annual right, 30 days' notice, limited to relevant systems, Controller pays costs above Processor's reasonable internal costs; third-party audit reports accepted in lieu.

### Liability allocation
- GDPR does not cap DPA liability between controller and processor — this is a commercial negotiation.
- Common approach: DPA liability follows the main services agreement cap; carve-out for regulatory fines attributable to the other party's fault.
- Note: GDPR Article 82 establishes joint and several liability of controller and processor toward data subjects; internal allocation between them is the purpose of the DPA indemnification clause.

### Breach notification timing
- 24 hours is tight but increasingly market standard for notification to Controller.
- Processor should not investigate the incident before notifying Controller — early notification with incomplete information is better than delayed notification with full facts.

## Common mistakes

1. **Annex II left blank** — "appropriate security measures" without specifics is not GDPR-compliant; supervisory authorities expect concrete measures.
2. **Sub-processor list not maintained** — processors must keep Annex III current and notify on changes.
3. **No SCCs for MENA transfers** — UAE and KSA data processors are not in any adequacy country; SCCs are required.
4. **Breach notification threshold miscalibrated** — "significant" breach triggers are too high; the threshold is awareness of any personal data breach, not just significant ones.
5. **Audit right not scoped** — unlimited audit rights with no notice requirement are commercially impractical and will be resisted.
6. **Deletion deadline not specified** — "delete at end of services" without a specific period leads to disputes.

## Related skills

- [[draft-dpa-uae-pdpl]] — DPA adapted for UAE Federal Decree-Law 45/2021
- [[draft-dpa-ksa-pdpl]] — DPA adapted for KSA PDPL (Royal Decree M/19 2021)
- [[draft-privacy-policy]] — public-facing privacy notice that GDPR Article 13/14 requires
- [[review-data-privacy]] — reviewing an existing DPA or data-processing arrangement for compliance gaps
- [[kb-gdpr]] — GDPR reference knowledge pack
