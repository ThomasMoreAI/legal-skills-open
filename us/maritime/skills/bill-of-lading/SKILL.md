---
name: bill-of-lading
title: Bill of Lading
description: 'Drafts a U.S. ocean Bill of Lading (B/L) functioning as receipt, contract of carriage, and document of title under COGSA or Hague-Visby. Covers negotiable and straight B/Ls, cargo description, freight allocation, and core carriage clauses. Use when drafting or reviewing a bill of lading, master/house B/L, ocean shipment documentation, or title transfer. Trigger keywords: bill of lading, B/L, ocean carriage, COGSA, Hague-Visby, negotiable, straight, master bill, house bill.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bill-of-lading
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: maritime
language: en
tags: [agreement, drafting, regulatory]
---

# Bill of Lading

Produces a complete B/L that memorializes shipment, allocates risk, and complies with the governing carriage regime. Populate every field from source documents only — never invent data.

## Prerequisites

1. **Parties** — shipper, consignee, notify party legal names, addresses, contacts
2. **Booking & voyage** — booking confirmation, vessel/voyage, ports, delivery terms
3. **Cargo details** — packing list, commercial invoice, marks/numbers, weights, measurements
4. **Commercial terms** — Incoterms, freight payment (prepaid/collect), currency, charges
5. **Special requirements** — insurance/declared value instructions, special handling, hazmat data (UN number, IMDG class) if applicable

## Output Structure

### 1) Document Header

| Field | Req | Notes |
|---|---|---|
| B/L Number | Yes | Unique identifier |
| B/L Type | Yes | `Negotiable` or `Straight (Non-negotiable)` |
| Issue Place/Date | Yes | City, country, date |
| Carrier / Shipper / Consignee | Yes | Legal name and address each |
| Notify Party | Opt | If applicable |
| Vessel/Voyage / Booking No. | Opt | If known |
| Container/Seal Nos. | Opt | If applicable |

### 2) Shipment Routing

| Field | Req | Notes |
|---|---|---|
| Place of Receipt | Yes | Terminal or facility |
| Port of Loading / Discharge | Yes | Port code if available |
| Place of Delivery | Yes | Final destination |
| Transshipment | Opt | Intermediate ports |

### 3) Cargo Description

| Field | Req | Notes |
|---|---|---|
| Description of Goods | Yes | Trade description; do not speculate |
| Packages/Units | Yes | Count and unit type |
| Gross Weight | Yes | With unit |
| Marks/Numbers / HS Code | Opt | As on packages; shipper-provided |
| Measurement / Packaging | Opt | CBM; type and condition |
| Declared Value | Opt | If higher liability requested |
| Special Handling | Opt | Fragile, reefer, etc. |
| HazMat | Cond | IMDG class, UN number |

### 4) Freight and Charges

| Field | Req | Notes |
|---|---|---|
| Freight Term | Yes | Prepaid or Collect |
| Rate Basis | Yes | Per container/weight/measure |
| Currency | Yes | ISO code |
| Additional Charges | Opt | THC, docs, fuel, security |
| Payment Due | Opt | Date or upon release |

### 5) Core Clauses Checklist

- [ ] Receipt in apparent good order unless claused
- [ ] Carrier duty of due diligence — vessel seaworthiness
- [ ] Liability limitation: COGSA $500/package or customary freight unit unless higher value declared and paid [VERIFY]
- [ ] Notice of loss/damage timing (apparent vs. concealed) [VERIFY]
- [ ] Time bar: COGSA one year from delivery or due date [VERIFY]
- [ ] Exceptions: perils of the sea, act of God, inherent vice, shipper fault
- [ ] General average clause and GA contribution security
- [ ] Carrier lien for unpaid freight/charges
- [ ] Governing law, forum selection, or arbitration clause
- [ ] Himalaya clause extending defenses to agents/subcontractors
- [ ] Both-to-blame collision clause (if used by carrier)

### 6) Negotiability and Originals

- State number of originals issued; surrender of one renders others void
- Straight B/L: state non-negotiable, identify consignee
- Electronic B/L: specify system and rules governing eBL transfer

### 7) Signature Blocks

- Carrier or agent: signature, name, title, date
- Shipper signature if required by carrier practice
- Clausing space for exceptions to condition/quantity

## Guidelines

- Mirror packing list, booking, and shipper instructions exactly — never fabricate data
- If Hague-Visby or another regime governs, state it expressly and remove conflicting COGSA language [VERIFY]
- For L/C shipments, issue clean B/L only if no visible damage; otherwise clause accurately
- Align freight term with Incoterms and buyer/seller responsibilities
- Multimodal or door-to-door: clarify scope and liability regime for each leg
- Treat HS codes, weights, and counts as shipper-provided; avoid guarantees
- Flag jurisdiction-specific mandates or carrier standard terms that must attach
