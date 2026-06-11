---
name: commercial-invoice-for-export
title: Commercial Invoice for Export
description: Drafts a compliant Commercial Invoice for Export satisfying customs, banking (L/C), logistics, and insurance requirements. Enforces Incoterms 2020, HS tariff classification, country-of-origin determination, export control referencing, and certification language. Use when preparing export invoices for customs authorities, freight forwarders, banks, or insurance underwriters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commercial-invoice-for-export
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: trade
language: en
tags: [agreement, drafting, regulatory]
---

# Commercial Invoice for Export

Drafts a legally precise export commercial invoice for customs clearance, letter of credit payment, and multi-jurisdictional regulatory compliance.

## Prerequisites

Gather before drafting:

- **Purchase order / proforma invoice** — pricing, quantity, product specs
- **Sales contract or L/C** — payment terms, special notations, latest shipment date
- **Export license** (if controlled goods) — license number, expiration, ECCN or USML category
- **Shipping instructions** — Incoterm, named place/port, carrier details
- **Origin documentation** — country of manufacture, FTA qualification basis if claiming preference

## Invoice Sections

### 1. Header & Invoice Reference

| Field | Requirement |
|---|---|
| Invoice Number | Sequential, non-duplicative; traceable in compliance/accounting systems |
| Invoice Date | DD/MM/YYYY internationally; MM/DD/YYYY if US-only |
| Cross-references | Bill of lading / AWB number, packing list ref, certificate of origin number |

### 2. Party Identification

**Exporter / Shipper:**
- Full legal registered name (not trade name / DBA)
- Complete registered address with postal code and country
- Tax ID / EIN / VAT / export registration number
- International phone and customs/shipping email

**Consignee / Importer:**
- Full legal name as registered in destination country
- Delivery or customs clearance address (include FTZ, bonded warehouse, or SEZ codes if applicable)
- Importer tax ID in destination-country format (EU VAT, CA BN, US EIN, etc.)
- Import license number or customs broker reference if required
- Authorized contact: name, title, phone, email

> All party details must match PO, L/C, import permits, and AES/EEI filings character-for-character.

### 3. Commercial & Shipping Terms

| Field | Format |
|---|---|
| Incoterms 2020 | Three-letter code + full named place (e.g., `FOB Shanghai Port, China`) |
| Currency | Transaction currency; unit prices reflect all costs included under the Incoterm |
| Payment Terms | Net days, L/C reference, D/P, D/A, etc. |

### 4. Goods Description & Valuation

Each line item requires:

| Column | Requirement |
|---|---|
| Description | Specific technical detail — commercial name, dimensions, material/composition, model/part number, brand, intended use. No vague terms ("machine parts," "electronics") |
| HS / HTS Code | 6-digit HS minimum; extend to 8–10 digits per destination schedule. Flag classification risk for high-duty or controlled items |
| Country of Origin | Legal determination (substantial transformation / tariff shift / RVC) — not simply exporter's location |
| Quantity & UOM | Metric preferred (kg, MT, L, m², m³); include shipping units and item count |
| Unit Price | Must match proforma / PO / L/C exactly |
| Line Total | Quantity × Unit Price; verify arithmetic |

**Totals block:** subtotals by category (if multiple), total merchandise value, freight/insurance (itemized or included per Incoterm — state clearly), net weight (goods only, kg), gross weight (goods + packaging, kg).

### 5. FTA / Preferential Origin (if applicable)

- Identify the FTA (USMCA, CPTPP, EU agreement, ASEAN, bilateral)
- State the rule of origin satisfied (tariff shift, RVC threshold, specific process)
- Reference certificate of origin number, issuing authority, date
- Exporter must hold approved-exporter status if required by the FTA

### 6. Export Control Notation (if applicable)

For EAR- or ITAR-controlled goods, include:

- **ECCN** and license number + expiration, OR license exception (e.g., EAR99 / NLR)
- **USML Category** (for ITAR items)

### 7. Certification & Signature Block

Include verbatim or substantively equivalent declaration:

> "I hereby certify that the information contained in this invoice is true, correct, and complete; that the goods are of the country of origin stated; that the prices shown are the actual transaction value with no undisclosed considerations; and that this shipment is in full compliance with applicable export control regulations, trade laws, economic sanctions, and anti-boycott requirements of the exporting country. I understand that civil and criminal penalties may be imposed for false or fraudulent statements."

Signature block: handwritten signature line, printed name, title, date (jurisdiction-appropriate format), company seal / chamber stamp / notarization space (if required by destination country or L/C).

## Pitfalls & Checks

- **L/C compliance** — Verify every element against L/C field-by-field (description, quantity, value, Incoterm, shipment date, special notations). Any discrepancy risks payment refusal.
- **No generic descriptions** — Customs undervaluation or misclassification penalties apply to vague language. Use HS-aligned terminology.
- **Tariff code verification** — HS codes and duty rates change. For high-value or controlled goods, recommend a binding tariff ruling or licensed customs broker review.
- **Origin ≠ exporter location** — Multi-country production requires documented substantial transformation, tariff shift, or RVC analysis.
- **Weights** — Always provide both net and gross weight; required by most customs authorities.
- **Recordkeeping** — Retain invoice and supporting documents 5 years (US EAR); 5–10 years in other jurisdictions.
- **Missing information** — If any required field cannot be determined, identify the gap, explain the compliance risk, and request the information before issuing.
