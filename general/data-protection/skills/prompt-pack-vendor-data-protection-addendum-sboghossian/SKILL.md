---
name: prompt-pack-vendor-data-protection-addendum-sboghossian
title: Vendor Data Protection Addendum
description: Use when a company needs to attach a data protection addendum (DPA) to a vendor or supplier agreement where the vendor may access, process, or store personal data on behalf of the company. Covers processor obligations, security requirements, sub-processing restrictions, audit rights, cross-border transfer mechanisms, and breach notification. Especially important for MENA entities subject to UAE PDPL, KSA PDPL, Egypt PDPL, or GDPR, where a written data processing agreement is legally mandatory.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-vendor-data-protection-addendum
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Vendor Data Protection Addendum

## When to use this

Use this skill when a company (the "controller") engages a vendor (the "processor") who will have access to personal data — and the parties need a written data processing agreement to govern that processing relationship. A DPA is not optional under GDPR, UAE PDPL, KSA PDPL, or Egypt PDPL: each statute mandates a written contract between controller and processor setting out the processor's obligations.

Common triggers:
- Engaging a SaaS vendor whose platform will process employee or customer personal data
- Outsourcing HR, payroll, IT help-desk, or CRM functions to a third-party provider
- Using a cloud storage or analytics vendor that handles company-controlled personal data
- A vendor's own standard DPA needs to be counter-proposed with company-standard terms
- An existing vendor contract lacks a DPA and the company is conducting a data protection audit

This addendum supplements the master services agreement (MSA) or other main contract; it does not replace it.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Controller full name + registered address | Identifies the data controller | Prompt user |
| Processor / vendor full name + registered address | Identifies the data processor | Prompt user |
| Description of personal data processed | Defines the DPA's scope; triggers special-category obligations | Prompt user — be specific (categories of data subjects, data fields, volume) |
| Purposes of processing | Processor may only process on documented instructions | Prompt user |
| Duration of processing | When the DPA terminates | Coterminous with the main services contract |
| Governing law | Determines applicable data protection statute | Jurisdiction of the controller's establishment or where data subjects are located |

## Optional inputs

- **Sub-processor whitelist** — approved sub-processors identified upfront; general authorization vs. specific authorization
- **Security standards** — required certifications (ISO 27001, SOC 2, PCI-DSS)
- **Data residency** — requirement to store data within a specific country or region
- **Retention and deletion schedule** — how long processor may retain data; certified deletion obligations
- **DPIA cooperation** — processor's obligation to assist controller in conducting Data Protection Impact Assessments
- **Audit mechanism** — on-site audit vs. third-party certification; frequency; notice period

## Document structure

1. **Definitions** — "Personal Data," "Processing," "Data Subject," "Controller," "Processor," "Sub-processor," "Security Incident," "Applicable Data Protection Law" (list each statute: e.g., GDPR, UAE PDPL FDL 45/2021, KSA PDPL Royal Decree M/19, Egypt Law 151/2020, DIFC DP Law No. 5/2020)
2. **Nature, purpose, and scope of processing** — precise description of the processing operations; data subject categories; data categories; processing purposes; duration; instruction limitation (processor processes only as instructed by controller)
3. **Processor obligations**
   - Process only on documented instructions of controller
   - Confidentiality obligation on authorized personnel (including post-termination)
   - Implement appropriate technical and organizational security measures (Article 28(3)(c) GDPR equivalent)
   - Sub-processing restrictions (see §6)
   - Assist controller with data subject rights requests (response within applicable deadline)
   - Assist controller in meeting compliance obligations (security, breach notification, DPIA)
   - Return or delete personal data on termination
   - Provide information and audit cooperation
4. **Controller obligations** — controller's representations that it has a lawful basis for the processing; controller's obligation to provide timely instructions; controller's obligation to inform processor of any legal requirements that affect processing
5. **Technical and organizational measures (TOM)** — Annex/Schedule setting out minimum security measures: encryption at rest (AES-256) and in transit (TLS 1.2+), access control (role-based, MFA), pseudonymization, regular security testing, physical security; processor may maintain equivalent measures as certified under ISO 27001 or SOC 2 Type II in lieu of a bespoke TOM schedule
6. **Sub-processing** — general or specific authorization required; processor must notify controller before engaging a new sub-processor; controller may object within [14 days]; sub-processors must be bound by equivalent DPA obligations; processor remains liable for sub-processor acts
7. **Data subject rights** — processor to notify controller of any data subject request within [3 business days]; processor must assist controller in fulfilling requests within the statutory deadline (30 days under GDPR; UAE PDPL and KSA PDPL require "prompt" response); no independent right of processor to respond to data subjects
8. **Security incident notification** — processor must notify controller of any Security Incident without undue delay and in any event within [24–48 hours] of discovery; initial notification may be preliminary; follow-up with full details within [72 hours]; GDPR: controller must notify supervisory authority within 72 hours; UAE PDPL: "without undue delay" to TDRA and affected individuals; KSA PDPL: within 72 hours to SDAIA; Egypt PDPL: notification to Personal Data Protection Center
9. **Audit and inspection** — controller right to audit processor's compliance with the DPA on [30-day] prior notice; audit at controller's cost; processor may satisfy audit right by providing third-party certification (ISO 27001, SOC 2); controller may conduct an ad hoc audit if a Security Incident occurs
10. **Data transfer mechanisms** — processor identifies sub-processors and data flows outside the controller's jurisdiction; applicable transfer mechanisms: EU SCCs (Module 2: controller-to-processor), UK IDTA, UAE SCCs (TDRA-approved), SDAIA-approved mechanisms for KSA; data residency requirements if applicable
11. **Retention and deletion** — on termination of the main contract, processor must return or securely delete all personal data within [30 days]; certify deletion in writing; processor may retain data for legal hold requirements but must notify controller
12. **Liability and indemnification** — each party liable for its own non-compliance; processor indemnifies controller for regulatory fines and third-party claims caused by processor's breach; processor liability cap (typically fees paid in the [12 months] preceding the claim)
13. **Term** — DPA is effective upon execution and terminates on expiry of the main contract (or earlier deletion of all personal data)
14. **Schedules** — A: Description of processing (data subjects, data categories, purpose, duration, special categories); B: Approved sub-processors; C: Technical and organizational measures; D: Transfer mechanisms (SCCs or equivalents)

## Jurisdictional notes

| Jurisdiction | Mandatory DPA requirement | Special notes |
|---|---|---|
| EU / GDPR | Art. 28 GDPR — mandatory written contract | Standard clauses (Art. 28(7) model) issued by European Commission; specific mandatory content |
| DIFC | DIFC DP Law 2020 Art. 23 — mandatory written contract | Common-law framework; DIFC DP Commissioner may inspect; SCCs for transfers out of DIFC |
| ADGM | ADGM DPR 2021 — mandatory written contract | Similar to DIFC; ADGM Registration Authority oversight |
| UAE (onshore) | UAE PDPL FDL 45/2021 — Art. 19 mandates data processing contract | TDRA oversight; approved transfer mechanisms; Arabic version required for government data |
| KSA | KSA PDPL Art. 29 — written contract required for outsourcing | SDAIA oversight; 72-hour breach notification; Saudi data residency for government and health data |
| Lebanon | No enacted comprehensive PDPL yet; sector-specific rules apply | Banking secrecy (Law 3/1956) constrains DPAs for financial sector; medical records rules apply |
| Egypt | Egypt PDPL Law 151/2020 Art. 22 — written data processing contract required | Personal Data Protection Center oversight; cross-border transfers require PDP Center approval |
| UK | UK GDPR Art. 28 + DPA 2018 | UK IDTA for transfers out of UK; ICO template DPA clauses available |

**Cross-border transfer trap:** Processors commonly sub-contract to cloud providers (AWS, Azure, GCP) hosted outside the controller's jurisdiction. The DPA must identify this transfer chain and specify the applicable transfer mechanism (SCCs, adequacy decision, TDRA approval). In KSA, health and government data may not leave the Kingdom at all.

**Arabic language requirement (UAE / KSA):** DPAs relating to UAE or KSA data subjects may need to be executed in Arabic or accompanied by an Arabic translation. For government contracts, Arabic is typically the official language.

## Drafting standards

- **Article 28 GDPR mandatory content must be replicated** even in non-EU DPAs — it represents the global baseline and will satisfy most non-EU regulators as a minimum
- **Sub-processor list** should be an Annex with periodic update mechanism; "general authorization" is only permissible if controller is given notice and objection right
- **Security annex must be specific** — "industry standard security" without specification is insufficient; reference certifications or enumerate concrete measures
- **Breach notification** — set 24–48 hours as processor obligation to give controller time to meet the 72-hour regulatory clock
- **No carve-outs for anonymized / aggregated data** without defining both terms precisely — vendors often claim broad analytics rights under vague "anonymization" language

## Common mistakes

- **DPA missing entirely** — the single most common gap discovered in privacy audits
- **Using a processor's standard DPA without review** — large cloud vendors' standard DPAs heavily favor the processor; counter-propose or negotiate key terms
- **Sub-processor list too vague** — "affiliates and subcontractors" without names fails the statutory specificity requirement
- **No data return / deletion obligation** — processor retains data indefinitely unless deletion is contractually required
- **Security annex by reference only** — "SOC 2 certification" alone does not describe what security measures are actually in place; attach the certification summary
- **Breach notification timeline inconsistent** — processor's 24-hour obligation to controller must be specified separately from controller's 72-hour obligation to the regulator

## Related skills

- [[prompt-pack-third-party-data-sharing-agreement]]
- [[prompt-pack-vendor-agreement-red-flag-scan]]
- [[prompt-pack-vendor-risk-assessment-questionnaire]]
- [[kb-mena-data-protection]]
- [[heuristic-always-state-jurisdiction-first]]
