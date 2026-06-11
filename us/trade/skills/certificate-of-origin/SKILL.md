---
name: certificate-of-origin
title: USMCA/NAFTA Certificate of Origin
description: Drafts USMCA/NAFTA Certificates of Origin for preferential tariff treatment on US-Mexico-Canada goods. Verifies origin criteria, HS classifications, and regional value content. Use when preparing trade certificates, customs origin documentation, duty preference claims, or cross-border shipment certifications.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/certificate-of-origin
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trade
language: en
tags: [drafting, letter, research]
---

# USMCA/NAFTA Certificate of Origin

Generates legally compliant Certificates of Origin certifying goods qualify for preferential tariff treatment under USMCA (effective July 1, 2020) or legacy NAFTA.

## Prerequisites

- Commercial invoices and bills of materials for goods being certified
- Production records (material sourcing, manufacturing location, supplier docs)
- Party information: legal names, addresses, tax IDs for exporter, producer, importer
- HS tariff classification (minimum 6-digit; 8- or 10-digit if importing country requires)
- Any prior origin determinations or tariff rulings for same goods

## Quick Start

1. Confirm agreement: USMCA for shipments on/after July 1, 2020; NAFTA for earlier
2. Collect exporter, producer, and importer details
3. Describe goods with HS codes and determine origin criterion (A/B/C/D)
4. Draft certification statement with legal declarations
5. Generate certificate with signature block

## Core Workflow

### 1. Determine Agreement and Coverage Type

| Shipment Date | Agreement |
|---|---|
| Before July 1, 2020 | NAFTA (Ch. 4-5) |
| On or after July 1, 2020 | USMCA (Ch. 4-5) |

Confirm **single shipment** or **blanket** (max 12 months from signature, USMCA Art. 5.2).

### 2. Collect Party Information

For exporter, producer, and importer: full legal business name, complete physical address, and tax ID / business registration number.

**Special cases:**

| Scenario | Handling |
|---|---|
| Exporter = Producer | State "Same" in producer field |
| Producer confidential | "Available to Customs upon request" (Art. 5.2); note verification risk |
| Importer unknown | "Unknown" / "Various"; may need updating before preference claim |

### 3. Describe Goods

Each good requires: commercial name, technical specs (model/part numbers), material composition, HS classification (6+ digits matching entry docs), and intended use. Never use vague descriptions ("parts," "merchandise").

### 4. Determine Origin Criterion

| Criterion | Meaning |
|---|---|
| **A** | Wholly obtained/produced entirely in US/MX/CA — zero third-country content |
| **B** | Produced entirely in US/MX/CA using only originating materials |
| **C** | Produced using non-originating materials satisfying product-specific rules (tariff shift, RVC) |
| **D** | Automotive goods meeting enhanced USMCA auto rules |

**Regional Value Content** (when required) — calculate via either method:
- Transaction value: RVC = ((TV − VNM) / TV) × 100
- Net cost: RVC = ((NC − VNM) / NC) × 100

Retain calculation worksheets. For tariff shift analysis, confirm non-originating materials classify in a different heading/subheading than the finished good. Flag sector-specific rules for automotive, textiles/apparel, and agricultural goods.

### 5. Draft Certification Statement

Must include:

- Affirmation goods qualify as originating under USMCA Ch. 4-5 (or NAFTA Ch. 4-5)
- Basis of certifier's knowledge (direct examination, production records, company role)
- Acknowledgment of verification rights (written requests, questionnaires, facility visits)
- Record retention: **5 years** from signature (USMCA) or importation (NAFTA)
- 30-day response obligation for verification requests
- Penalties awareness: civil penalties, criminal prosecution (18 U.S.C. § 1001 [VERIFY] or MX/CA equivalents), MFN duty liability plus interest, customs privilege suspension

### 6. Signature Block

Include: signatory name, title/position (must have binding authority), full legal company name, date (unambiguous format), phone (with country code), and email.

If exporter certifies based on producer-supplied information, obtain and retain written origin statement from producer.

## Output Structure

Generate certificate sections in order:

1. **Header** — Agreement identifier, blanket vs. single shipment, coverage period
2. **Exporter block** — Name, address, tax ID
3. **Producer block** — Name, address, tax ID (or confidentiality notation)
4. **Importer block** — Name, address, tax ID (or "Unknown")
5. **Goods table** — Description, HS number, origin criterion, country of origin per line item
6. **Certification statement** — Full legal declaration
7. **Signature block**

Append a **compliance memo**: basis for origin determination, supporting docs to maintain, risk flags (marginal RVC, ambiguous tariff shifts, sourcing changes), and monitoring recommendations.

## Pitfalls and Checks

- Never mix NAFTA/USMCA frameworks — verify by shipment date
- Flag RVC within 5% of minimum threshold as high-risk
- Mark uncertain HS classifications for client review before submission
- Blanket certificates must not exceed 12-month coverage
- Cross-check consistency across certificate, commercial invoice, and entry docs
- Use "N/A" or "Unknown" only where legitimately unavailable
- Do not provide final legal sign-off — flag for attorney review where origin qualification is marginal
