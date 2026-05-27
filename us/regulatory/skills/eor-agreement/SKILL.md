---
name: eor-agreement
title: Exporter of Record (EOR) Agreement
description: Drafts a U.S.-compliant Exporter of Record (EOR) Agreement appointing a third party as USPPI for international export transactions. Allocates compliance obligations under EAR, ITAR, OFAC, and CBP with denied-party screening, AES/EEI filing, indemnification, and record retention. Use when drafting EOR appointments, export compliance service agreements, or logistics outsourcing for cross-border shipments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/eor-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [agreement, drafting]
---

# Exporter of Record (EOR) Agreement

Drafts an enforceable EOR Agreement appointing a qualified third party as USPPI, allocating export compliance obligations, and managing liability under U.S. export control law.

## Prerequisites

1. **Party details** — legal names, entity types, jurisdictions, EIN numbers, CBP exporter-of-record numbers
2. **Goods/technology** — technical specs, ECCN classifications, USML categories if defense articles, commodity jurisdiction determinations
3. **Destinations and end-users** — countries, consignees, end-use certifications
4. **Scope** — compliance-only vs. combined logistics; exclusive vs. non-exclusive
5. **Existing authorizations** — BIS/DDTC licenses, license exceptions, OFAC authorizations
6. **Business terms** — fees, term length, insurance minimums, governing law/venue

## Output Structure

### 1. Parties & Recitals
- Full party identification with CBP registration numbers
- Recitals: principal's export need → regulatory complexity → EOR expertise
- Acknowledgment of penalty exposure under EAR, ITAR, OFAC, CBP

### 2. Definitions

| Term | Definition |
|---|---|
| **EOR / USPPI** | Party on export documentation legally responsible for the transaction |
| **Export Controls** | EAR (15 C.F.R. §§ 730–774), ITAR (22 C.F.R. §§ 120–130), OFAC sanctions, anti-boycott regs (15 C.F.R. Part 760) |
| **EEI/AES Filing** | Electronic Export Information via Automated Export System per 15 C.F.R. Part 30 |
| **Controlled Items** | Goods, software, or technology subject to EAR, ITAR, or OFAC |
| **Denied Parties Screening** | Pre-shipment check against DPL, Entity List, Unverified List, SDN List, FSE List, ITAR Debarred List |
| **Export Documentation** | Commercial invoice, packing list, BOL/AWB, license/exception, EEI, certificate of origin, DCS |

### 3. Appointment & Scope
- Exclusive/non-exclusive; product categories, destinations, carve-outs
- Authority limits: regulatory acts only vs. authority to bind commercially
- Escalation for novel classifications, sensitive end-users, denied-party hits

### 4. EOR Obligations

- [ ] Classify items under EAR (ECCN) or ITAR (USML); document rationale
- [ ] Determine licensing; apply exceptions or obtain BIS/DDTC licenses
- [ ] Submit EEI via AES for shipments meeting thresholds (15 C.F.R. Part 30)
- [ ] Place Destination Control Statements on invoices and BOLs
- [ ] Screen all participants against denied-party lists **before each shipment**; document results
- [ ] Prepare complete export documentation per transaction
- [ ] Retain records **5 years** from export, license expiration, or enforcement action (15 C.F.R. § 762.2)
- [ ] Notify Principal within **[X] business days** of compliance issues, license denials, government inquiries
- [ ] Maintain E&O insurance ($[X]M min.), customs bond, general liability ($[X]M min.)

### 5. Principal Obligations

- [ ] Provide accurate technical specs and end-use/end-user info before each shipment
- [ ] Disclose prior commodity jurisdiction determinations and classification requests
- [ ] Notify EOR of product changes, new destinations/end-users, ownership changes
- [ ] Warrant IP rights and manufacturing authorizations; no export-restricting liens
- [ ] Bear all costs: EOR fees, filing fees, duties, taxes, license fees
- [ ] Cooperate with government audits and enforcement actions
- [ ] Comply with FCPA (15 U.S.C. § 78dd-1 et seq.) and anti-boycott regs (15 C.F.R. Part 760)

### 6. Representations & Warranties
- Both: not on any restricted party list; no disqualifying investigations; authority to execute
- **EOR**: holds required licenses/registrations; maintains compliance systems and trained personnel
- **Principal**: information accurate and complete; no undisclosed item restrictions
- Ongoing covenant: immediate notice of restricted-party status change or material compliance issue

### 7. Indemnification

| Party | Covers |
|---|---|
| **Principal indemnifies** | Inaccurate/incomplete info; undisclosed classifications; principal-caused violations; unauthorized changes; breach of warranties |
| **EOR indemnifies** | EOR negligence or willful misconduct; filing/documentation errors; unauthorized acts beyond scope |

- Procedure: written notice → indemnifying party controls defense → indemnified party cooperates
- Unlimited liability carve-outs: gross negligence, willful misconduct, fraud, intentional export violations

### 8. Limitation of Liability
- Cap: lesser of $[X] or [X] months fees paid
- No consequential/punitive damages (except third-party awards or willful misconduct)

### 9. Term & Termination

| Event | Notice |
|---|---|
| Convenience | [30–90] days written |
| Material breach | [15–30] days + cure period |
| Immediate (no cure) | Bankruptcy; restricted-party listing; license revocation; imminent violation risk |

Post-termination: complete in-process shipments; transfer/assign licenses per agency rules; return documents within [X] days; refund unearned fees. Surviving: indemnification, confidentiality, records, payment.

### 10. Governing Law & Disputes
- [State] law; federal export law supersedes on regulatory matters
- Tiered: executive negotiation [30d] → mediation [60d] → arbitration/litigation
- Injunctive relief carve-out for confidentiality breaches and imminent violations
- Jury trial waiver if litigating

### 11. General Provisions
- Integration; written amendments; counterparts; e-signatures
- Schedules: product/ECCN list, fee schedule, approved destinations, compliance procedures

## Guidelines

- **ITAR trigger**: Defense articles (USML I–XXI) require ITAR-specific reps, DDTC license/TAA references, registration (22 C.F.R. § 122); consider standalone addendum
- **AES threshold**: EEI required for shipments >$2,500 or requiring license (15 C.F.R. § 30.2) [VERIFY]
- **OFAC**: Screen SDN and sectoral sanctions even absent EAR/ITAR license requirements (50 U.S.C. § 1701 et seq.)
- **Anti-boycott**: Required for goods destined for/transiting Arab League countries; both parties covenant compliance (15 C.F.R. Part 760)
- **Insurance**: Confirm E&O, bond, and GL minimums against industry standards and export risk profile
- **State law**: Indemnification and liability caps may face state-specific enforceability limits
- **License transfers**: Export licenses generally non-transferable to successor EOR without BIS/DDTC approval; flag in transition planning
