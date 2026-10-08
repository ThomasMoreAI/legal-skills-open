---
name: draft-dpa-uae-pdpl-sboghossian
title: Data Processing Agreement — UAE Personal Data Protection (Federal + DIFC/ADGM)
description: Use when drafting a Data Processing Agreement (DPA) compliant with UAE Federal Decree-Law 45/2021 on Personal Data Protection (UAE PDPL). Covers UAE PDPL key requirements, the separate DIFC (Law 5/2020) and ADGM (Data Protection Regulations 2021) regimes that govern free-zone entities, cross-border transfer framework (Articles 22–23), bilingual Arabic/English requirement for federal filings, and the distinction between onshore UAE, DIFC, and ADGM entity obligations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-dpa-uae-pdpl
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: data-protection
language: en
---

# Data Processing Agreement — UAE Personal Data Protection (Federal + DIFC/ADGM)

## When to use this

The UAE data-protection landscape is **fragmented across three legal regimes**. Before drafting a DPA, identify which regime governs:

| Entity registration | Applicable law | Regulator |
|---|---|---|
| **UAE federal / onshore** (mainland + most free zones) | Federal Decree-Law 45/2021 (UAE PDPL) + implementing regulations | UAE Data Office (within UAE Digital Government Authority) |
| **DIFC** (Dubai International Financial Centre) | DIFC Data Protection Law (DIFC Law 5/2020) | DIFC Commissioner of Data Protection |
| **ADGM** (Abu Dhabi Global Market) | ADGM Data Protection Regulations 2021 | ADGM Registration Authority |

**Same entity, different regimes:** A multinational may have subsidiaries in all three. The applicable regime is determined by the entity's legal registration, not the data subject's location. A Dubai mainland company processing data about DIFC employees still uses the UAE PDPL; a DIFC-incorporated company uses DIFC Law 5/2020.

Use this skill for UAE federal / onshore entities. Use the DIFC/ADGM sections below for those regimes.

## Required inputs

Same as [[draft-dpa-gdpr]] — adapt for UAE PDPL specifics as set out below.

| Input | Why it matters |
|-------|----------------|
| Controller + Processor registration details | Determines which regime applies |
| Nature of data processed | UAE PDPL has enhanced requirements for sensitive/biometric data |
| Cross-border transfer countries | UAE PDPL Articles 22–23 govern; no adequacy list yet |
| Processor sub-contractor (sub-processor) list | Prior written consent required |
| Bilingual (Arabic/English) requirement confirmed | Arabic controls for federal filings |

## UAE PDPL key requirements

### Controller-processor relationship
- **Written contract required** — verbal or implied arrangements are non-compliant.
- Processor must process only on documented written instructions from the Controller.
- Controller bears primary compliance obligation; Processor carries secondary obligations.

### Security measures (Article 20)
Security measures must be "appropriate to the nature of the personal data and the risk of processing." No prescriptive list in the law itself; calibrate to the UAE Information Security Policy and NESA controls (for government/critical sector) or ISO 27001 / NIST CSF for private sector.

Minimum expected measures:
- Encryption in transit and at rest.
- Access controls with documented authorization procedures.
- Audit logging.
- Incident detection and response plan.
- Staff training.
- Vendor security assessments for sub-processors.

### Sub-processor consent (default: specific)
The UAE PDPL requires **prior written consent** of the Controller for each sub-processor engagement. Parties may negotiate a general authorization with notice, but this should be documented explicitly in the DPA — it is not the default.

Sub-processor obligations must flow down contractually (same-as-or-stricter obligations on sub-processor).

### Data subject rights (Article 14–17)
Data subjects in UAE have rights of: access, rectification, erasure, restriction, portability, and objection. The Processor must assist the Controller in responding to data subject requests within the Controller's statutory response window.

### Breach notification
- **To UAE Data Office**: "without undue delay" — implementing regulations expected to clarify; GDPR's 72-hour standard is a useful working benchmark until UAE regulations specify.
- **To affected data subjects**: if the breach is likely to result in high risk of harm.
- **Processor to Controller**: Processor should notify Controller within 24–48 hours to allow Controller to meet its regulatory notification obligations.

Notification content: nature of breach, categories and approximate number of data subjects and personal data records, contact details, likely consequences, measures taken and proposed.

### Data return / deletion
Controller's choice at end of services. Processor must return or permanently delete all Personal Data and certify deletion in writing within an agreed period (specify: typically 30–60 days post-termination).

## Cross-border transfers (Articles 22–23)

UAE PDPL permits international transfers in the following circumstances:

| Mechanism | Conditions |
|---|---|
| **Adequacy designation by UAE Data Office** | Country recognized as providing adequate protection (no official list published at time of writing; implementing regulations pending) |
| **Contractual safeguards** | Controller implements "appropriate contractual safeguards" — SCC-equivalent terms; binding corporate rules intra-group | 
| **Binding Corporate Rules** | For intra-group multinational transfers (BCRs) |
| **Specific derogations** | Explicit data subject consent; contractual necessity; legal claims; vital interests; public interest |

**Practical implication**: Until the UAE Data Office publishes an adequacy list, international transfers to most countries (including EU, US, KSA) require contractual safeguards. Where GDPR also applies, combine UAE PDPL contractual safeguards with GDPR SCCs in a single instrument.

MENA cross-transfer note: transfers between UAE onshore entities and UAE free zones (DIFC, ADGM) may require additional consideration because DIFC and ADGM are separate legal jurisdictions — treat as international transfers for compliance purposes.

## DIFC — Law 5/2020

### Regime overview
DIFC Law 5/2020 is closely modeled on GDPR and applies to any entity incorporated, licensed, or operating within the DIFC that processes personal data. The DIFC Commissioner of Data Protection (CDP) is the enforcement authority.

### DPA requirements under DIFC Law 5/2020
The DIFC DPA requirements are materially equivalent to GDPR Article 28 obligations:
- Written contract between Controller and Processor required.
- All eight Article 28(3) GDPR-equivalent obligations apply.
- Standard contractual clauses: DIFC CDP has published standard DPA template language; compliance is simplified by using it.
- International transfers: DIFC has mutual adequacy recognition with UK ICO and EU — transfers between DIFC and EU/UK do not require additional SCC/IDTA.

### DIFC vs. UAE federal — the interface
- A DIFC entity contracting with a UAE mainland entity for data processing: DIFC entity (if processor) is subject to DIFC Law 5/2020; UAE mainland entity (if controller) may be subject to UAE PDPL. Dual DPA provisions or a combined instrument is needed.
- Consider which law governs the DPA and include explicit governing-law clause.

## ADGM — Data Protection Regulations 2021

### Regime overview
ADGM Data Protection Regulations 2021 are also closely modeled on GDPR and apply to entities registered in ADGM. The ADGM Registration Authority (RA) oversees enforcement.

### DPA requirements
Materially equivalent to GDPR:
- Written contract required between Controller and Processor.
- Processor processes only on Controller's documented instructions.
- Security measures proportionate to risk.
- Sub-processor: prior Controller consent.
- Breach notification: without undue delay to Controller and RA.
- Data return/deletion at end of services.
- Audit rights.

International transfers from ADGM: ADGM RA has published a list of adequate jurisdictions; EU/UK are recognized; most MENA jurisdictions are not.

## Bilingual requirement

For UAE federal / onshore DPAs:
- **Arabic version is mandatory** for any filing with the UAE Data Office, federal courts, or onshore regulatory proceedings.
- English version is acceptable as the working language; Arabic controls in the event of inconsistency.
- DIFC and ADGM proceedings are conducted in English; Arabic translation not required for those jurisdictions.

## Document structure

Adopt the same structure as [[draft-dpa-gdpr]] with the following UAE PDPL-specific modifications:

1. **Governing law clause**: UAE Federal law for onshore; DIFC Law 5/2020 for DIFC entities; ADGM DP Regulations 2021 for ADGM entities.
2. **Dispute resolution**: UAE federal courts (onshore); DIFC Courts (DIFC entities); ADGM Courts (ADGM entities). International arbitration (DIAC, LCIA) is a common alternative.
3. **Bilingual execution block**: dual-language signature blocks with Arabic names/entities.
4. **Annex II (Security Measures)**: map to UAE cybersecurity frameworks (NESA for government/critical sector; UAE NCA for national critical infrastructure; ISO 27001 for private sector).
5. **Cross-border transfer annex**: include the contractual safeguard provisions and list destination countries with applicable transfer mechanism.

## Common mistakes

1. **Treating DIFC/ADGM as UAE federal** — these are separate legal jurisdictions with their own data-protection laws; a UAE PDPL DPA does not comply with DIFC Law 5/2020 and vice versa.
2. **No cross-border transfer mechanism for MENA transfers** — UAE PDPL requires contractual safeguards for transfers to KSA, LB, EG (none of which are on an adequacy list); a clause stating "transfers are permitted" without the mechanism is non-compliant.
3. **English-only DPA for federal entities** — unenforceable before UAE federal courts or the UAE Data Office.
4. **Penalty tables not consulted** — UAE PDPL penalty regulations are pending final publication; use UAE PDPL enforcement guidance as a proxy for negotiating liability caps.
5. **DIFC-UAE interface not addressed** — dual-jurisdiction entities need dual DPA provisions or a carefully drafted governing-law clause that addresses both regimes.

## Related skills

- [[draft-dpa-gdpr]] — GDPR DPA; use where EU data subjects are involved or Processor is EU-based
- [[draft-dpa-ksa-pdpl]] — KSA PDPL DPA for Saudi-nexus processing
- [[draft-privacy-policy]] — Arabic/English privacy notice required under UAE PDPL
- [[kb-data-privacy-mena]] — reference pack on UAE PDPL, DIFC DP Law, ADGM DP Regs, and KSA PDPL
