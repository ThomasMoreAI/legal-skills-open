---
name: interconnection-agreement
title: Interconnection Agreement
description: Drafts U.S. telecommunications Interconnection Agreements (ICAs) under 47 U.S.C. §§ 251-252 and FCC Part 51, covering POIs, traffic classification, reciprocal compensation, access charges, LNP, E911, signaling, and dispute resolution. Use when drafting or revising an ICA, negotiating Section 251/252 terms, defining POI/transport arrangements, structuring ILEC/CLEC or VoIP interconnection, or preparing state PUC filings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/interconnection-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Interconnection Agreement

Drafts a complete ICA suitable for execution and state PUC filing under the Communications Act framework.

## Quick Start

Gather before drafting:

1. **Parties** — Legal names, entity types, FCC FRNs, carrier classification (ILEC/CLEC/CMRS/VoIP)
2. **Scope** — Geographic area, traffic types, desired POIs, interconnection method (direct/indirect), anticipated volumes
3. **Technical** — Switch locations, interface standards, signaling (SS7/SIP), LNP/CNAM/E911 needs
4. **Commercial** — Rate elements, billing format, payment terms, existing tariffs/commission orders
5. **Regulatory** — Section 252 status, filing jurisdiction(s), prior ICA or arbitration history

## Agreement Structure

| Section | Content |
|---|---|
| Title + Effective Date | Agreement name; execution/approval effective date clause |
| Parties + Recitals | Legal names, carrier types, FRNs, statutory basis (47 U.S.C. § 251/252) [VERIFY] |
| Definitions | See Key Definitions below |
| Interconnection | POI details, transport/trunking, technical specs, signaling, testing |
| Traffic Classification | Local, intraLATA, interLATA, wireless, VoIP — definitions and billing treatment |
| Numbering + Databases | LNP procedures, CNAM, routing, NPAC access |
| E911 | PSAP routing, ANI/ALI responsibilities, priority handling |
| Performance | KPIs (ASR/NER/PND), thresholds, remediation |
| Rates + Billing | Rate tables, invoices, records, audits, disputes |
| Term + Termination | Initial term, renewal, termination for cause/convenience, transition |
| Dispute Resolution | Tiered process — regulatory vs commercial paths |
| Regulatory Compliance | FCC/state law, filing/approval mechanics, change-in-law |
| Standard Terms | Confidentiality, indemnity, liability limits, force majeure, notices, assignment |
| Signatures | Authorized signatories, optional notary, e-signatures |

## Key Definitions

Define each term precisely:

| Term | Requirements |
|---|---|
| Point of Interconnection (POI) | Physical address, logical demarcation, meet-point vs end office vs tandem, interface standard (DS-1/DS-3/OC-x/Ethernet) |
| Local Traffic | Origination/termination within local calling area; cite tariff/PUC designation |
| IntraLATA Toll / InterLATA | Within-LATA outside local area / crosses LATA boundary |
| Wireless Traffic | CMRS-originated/terminated; classification method |
| VoIP Traffic | IP-enabled voice; jurisdictional treatment and interim compensation |
| UNEs / Interconnection Facilities | Distinguish § 251(c)(3) vs § 251(c)(2) [VERIFY] |
| Transport / Tandem / End Office | Technical definitions tied to network topology |
| Busy Hour / CCS / MOU / PIU / PLU | Measurement and apportionment terms |
| Reciprocal Compensation | § 251(b)(5) obligation [VERIFY] |

## Technical Specs Checklist

- [ ] POI inventory: address, floor/bay/cage, equipment IDs
- [ ] Trunking: one-way/two-way, initial capacity, augmentation thresholds
- [ ] Signaling: SS7 point codes or SIP profile + headers
- [ ] Testing: ATIS/TIA protocols, acceptance criteria
- [ ] Forecasts: cadence and format for traffic projections
- [ ] Performance reporting: ASR/NER/PND metrics and remedies

## Rate and Billing Tables

Populate three rate schedules:

**A. Reciprocal Compensation** — Traffic type, rate, symmetric/asymmetric, jurisdictional basis

**B. Transport / Tandem / Entrance Facilities** — Element, NRC, MRC, order interval

**C. Access Charges** — Traffic type, tariff/rate reference, conditions

Billing workflow: specify invoice timing/format (EMR/EDI/CSV), records retention and audit rights, dispute window, and undisputed-amount payment terms.

## Dispute Resolution Ladder

| Stage | Timeframe | Scope |
|---|---|---|
| Operational Negotiation | X business days | Technical/billing issues |
| Executive Escalation | X days | Unresolved operational disputes |
| Mediation | X days | Non-binding commercial disputes |
| Regulatory Complaint | As needed | § 251/252 compliance, rates, traffic classification |
| Arbitration | Final step | Purely commercial contract disputes |

## Regulatory Filing

- Filing deadline after execution: [VERIFY]
- Effective date: execution vs PUC approval vs filing
- PUC rejection: amendment process and interim performance obligations

## Pitfalls and Checks

- Never invent rates, POIs, FRNs, or regulatory approvals — use placeholders if missing
- Tie traffic classification to specific jurisdictional rules and tariffs; flag VoIP treatment uncertainty
- Cite federal framework: Communications Act §§ 251-252 and 47 C.F.R. Part 51 [VERIFY]
- Include "continue to perform" during disputes to prevent service disruption
- Add jurisdiction addendum for known state PUC rules; otherwise include a state-law non-preemption clause
- Use defined terms consistently; verify all internal cross-references
- Move POIs, technical specs, and rate tables to exhibits when the agreement exceeds 10 pages
