---
name: shippers-letter-of-instruction
title: Shipper's Letter of Instruction (SLI)
description: Drafts a U.S.-focused Shipper's Letter of Instruction (SLI) authorizing a freight forwarder, capturing EEI/AES filing intent, and documenting export-control classifications. Use when drafting SLIs, authorizing forwarders, preparing EEI/AES filings, or documenting ECCN/ITAR/EAR99 classifications for international exports.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/shippers-letter-of-instruction
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Shipper's Letter of Instruction (SLI)

Produces a compliance-ready SLI that authorizes the forwarder and aligns export data across commercial invoices and government filings.

## Prerequisites

Collect before drafting:

- **Parties** — legal names, addresses, contacts for shipper (USPPI), consignee, forwarder, intermediate consignee
- **Shipment** — Incoterms, routing, ports, carrier, dates, insurance
- **Commodities** — descriptions, part/model numbers, qty, UoM, weights, packaging
- **Classification** — Schedule B/HS codes, ECCN/ITAR/EAR99 status, license or exemption basis
- **Valuation** — invoice value, currency, valuation basis
- **Screening** — restricted party/end-use results, red-flag findings

## Quick Start

Draft the SLI in nine sections. Each section maps to a block in the output.

```
- [ ] Header
- [ ] Party table
- [ ] Shipment details
- [ ] Commodity table
- [ ] Export control classification
- [ ] EEI/AES filing
- [ ] Authorizations
- [ ] Certifications
- [ ] Signature block
```

## Output Sections

### 1. Header

- Document title, internal reference number, preparation date
- Cross-reference to invoice/PO/packing list

### 2. Party Table

| Role | Fields |
|---|---|
| Shipper (USPPI) | Legal name, address, contact, EIN/DUNS |
| Consignee | Legal name, address, contact, importer ID |
| Forwarder | Legal name, address, contact |
| Intermediate Consignee | Legal name, address, contact (if any) |

### 3. Shipment Details

Incoterms (year), routing, port of export/destination, carrier/mode, ship date, insurance (Y/N + coverage), special handling/hazardous.

### 4. Commodity Table

Per line item: description (commercial + technical), part/model, HS/Schedule B, qty/UoM, net weight, gross weight, value.

### 5. Export Control Classification

Per line item: ECCN, license required (Y/N), license number, ITAR/USML category (if any), EAR99 (Y/N).

### 6. EEI/AES Filing

- **Filing responsibility**: `Forwarder` or `Shipper`
- **Authorization statement** (verbatim when forwarder files): "The shipper hereby designates and authorizes the freight forwarder named herein to act as our forwarding agent for export control and customs purposes, including preparation and filing of EEI in AES using our USPPI information and the shipment details provided."
- **Filing exemption** (if any): cite regulatory basis `[VERIFY]` (e.g., 15 CFR 30.36)

### 7. Authorizations

- Forwarder authorized to prepare/submit export documents, book transport, coordinate delivery
- State scope limitations or prohibited actions if any

### 8. Certifications

- Information accuracy and completeness
- Compliance with EAR, ITAR, OFAC sanctions, anti-boycott rules
- Restricted party screening completed; no known prohibited end-use/end-user
- No knowledge of diversion or prohibited destination

### 9. Signature Block

Authorized signatory: name, title, company, signature, date.

## Pitfalls

- **Name mismatch** — party names/addresses must match official registrations and invoice data exactly.
- **Vague descriptions** — commodity descriptions must support customs classification; never use generic labels.
- **Unverified "no license required"** — always tie to destination/end-user/end-use analysis. Mark uncertain items `[VERIFY]`.
- **Cross-document drift** — values, quantities, and HS/Schedule B codes must align with the commercial invoice.
- **Missing hazmat** — include hazardous material declarations and handling instructions when applicable.
- **Inconsistency** — any discrepancy between SLI and other export documents risks customs holds.

---

Key changes from the original:

- **Removed `tags`** — not part of the spec's frontmatter schema
- **Tightened description** — still third-person with clear triggers, cut keyword stuffing
- **Added Quick Start** — checklist workflow for fast orientation
- **Compressed tables** — party table uses Role/Fields format instead of 7 empty columns; shipment details and commodity table are inline prose instead of sparse tables
- **Renamed "Guidelines" → "Pitfalls"** — matches the best-practices pattern and is more scannable
- **Cut ~30% tokens** — removed redundant prose while preserving every domain-critical detail
