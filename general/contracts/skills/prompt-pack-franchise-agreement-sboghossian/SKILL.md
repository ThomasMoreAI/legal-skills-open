---
name: prompt-pack-franchise-agreement-sboghossian
title: Franchise Agreement
description: Use when drafting a franchise agreement granting a franchisee the right to operate a branded franchise at a specified location. Covers franchise fees, royalties, training requirements, operational standards, territory restrictions, term, renewal rights, and termination provisions. Applicable across MENA (UAE, KSA, LB, EG) and internationally. Critical in UAE and KSA where franchise arrangements can trigger mandatory commercial agency protection laws if not structured carefully. Trigger when a franchisor is entering a new market or when a franchisee needs its rights documented.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-franchise-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Franchise Agreement

## When to use this

Use this skill when drafting a franchise agreement — the core legal instrument by which a franchisor grants a franchisee the right to operate a business under the franchisor's brand, systems, and standards, in exchange for fees and royalties.

Franchise agreements must balance the franchisor's interest in protecting brand standards, IP, and business systems against the franchisee's interest in territorial protection, adequate support, and a fair commercial return. In MENA, an added layer of complexity arises from mandatory commercial agency and franchise-specific laws in certain jurisdictions.

Typical triggers:
- International franchisor entering UAE, KSA, or GCC markets
- Master franchise arrangement for a MENA region
- Domestic franchisor expanding its UAE or KSA concept
- Franchisee seeking to document its rights and protections

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Franchisor name and jurisdiction | Identity and IP owner | Ask |
| Franchisee name and jurisdiction | Identity; determines local law applicability | Ask |
| Brand / concept name | Subject of the franchise | Ask |
| Territory (single location, multiple units, or master franchise) | Scope of the right granted | Ask |
| Franchise fee structure | Initial fee + ongoing royalties + marketing fund contribution | Ask |
| Term | How long the agreement runs before renewal | Ask; typical is 5–10 years |

## Optional inputs

- Exclusivity of territory (exclusive vs. non-exclusive)
- Sub-franchising rights (for master franchisees)
- Transfer and assignment rights (can franchisee sell the franchise to a third party?)
- Right of first refusal on new units in the territory
- Development schedule (number of units to be opened and timeline — for multi-unit agreements)
- Franchisor approval process for new locations

## Document structure

### 1. Grant of franchise

- Grant of the right to operate under the franchisor's brand and system
- Territory: defined precisely (map reference, postal codes, or named area)
- Exclusivity: if exclusive, specify what "exclusive" means (no other franchisees; no company-owned units; no online sales in the territory?)
- Single-unit vs. multi-unit vs. master franchise: the type of rights granted

### 2. Franchise fee and royalties

**Initial franchise fee**:
- Amount (typically payable on signing or on commencement of training)
- Non-refundable (except in specific circumstances — state any refund conditions)

**Ongoing royalties**:
- Percentage of gross sales (typically 5–10% for food/retail; 2–6% for service businesses)
- Definition of "gross sales" (exclude taxes, refunds; confirm whether delivery platform fees are included)
- Payment frequency: weekly, monthly; method: direct debit, wire transfer
- Reporting obligation: franchisee to submit sales reports supporting each royalty payment

**Marketing fund contribution**:
- Percentage of gross sales to national/regional marketing fund (typically 1–4%)
- How the fund is administered; franchisor's obligation to use for marketing only
- Franchisee's right to audit marketing fund expenditure

**Technology fees**:
- POS system, loyalty program, digital ordering platform: monthly technology fees
- Franchisor's right to update technology and charge for updates

### 3. Term and renewal

**Initial term**: 5 or 10 years (aligned with investment payback period; negotiate based on upfront investment)

**Renewal rights**:
- Franchisee has the right to renew for one or more additional terms if: (a) not in material default; (b) signs the then-current form of franchise agreement; (c) completes any required refresher training
- Franchisor cannot refuse renewal except for cause
- Renewal fee: nil or nominal

### 4. Operations and brand standards

- Franchisee must operate the franchise in strict compliance with the Operations Manual (incorporated by reference)
- Franchisor's right to update the Operations Manual; reasonable notice required for material changes
- Quality and standards: franchisee must use approved suppliers; purchase approved products
- Inspection rights: franchisor can inspect premises on [X] hours' notice; conduct mystery shopping
- Right to take corrective action if standards are not met; escalation to termination for persistent failure

### 5. Training

- Initial training: franchisor provides [X] days of training for the franchisee's management team (at franchisor's training center); cost of travel and accommodation at franchisee's cost
- Ongoing training: annual refresher training; new product training
- Training for new staff: franchisee's obligation to ensure all customer-facing staff are trained to the franchisor's standards

### 6. Intellectual property

- License: franchisor grants franchisee a non-exclusive license to use the brand trademarks, trade dress, and system within the territory for the term
- Restrictions: franchisee cannot use the IP outside the territory; cannot modify or adapt the IP; cannot sublicense (except to employees for use in the franchise)
- Ownership: all IP belongs to and remains with the franchisor; franchisee cannot challenge ownership
- Infringement: franchisee must notify franchisor of any third-party infringement; franchisor controls any enforcement action

### 7. Transfer and assignment

- Franchisee cannot transfer its rights without franchisor's prior written consent (not to be unreasonably withheld)
- Conditions for transfer: proposed transferee must meet franchisee approval criteria; complete training; pay transfer fee; sign new franchise agreement
- Right of first refusal: franchisor has [30]-day ROFR to purchase the franchise at the same terms offered by the third-party buyer
- Death or incapacity: special provisions allowing estate or family members to continue or transfer the franchise

### 8. Term and termination

**Termination by franchisor for cause**:
- Material breach of the franchise agreement (with [30]-day cure period for remediable breaches)
- Persistent breach (3 or more notices of breach in any 12-month period)
- Insolvency or bankruptcy
- Abandonment of the franchise
- Conviction of a criminal offense affecting the brand
- Fraud or misrepresentation

**Termination by franchisee for cause**:
- Franchisor material breach (with [30]-day cure period)
- Franchisor insolvency

**Consequences of termination**:
- Franchisee ceases using all IP immediately
- Return of Operations Manual and all confidential materials
- Franchisor option to purchase the business assets at a formula price (or market value)
- Post-termination non-compete: [1–2] year non-compete in the same territory in the same business type

### 9. Non-compete

- During the term: franchisee cannot operate a competing business
- Post-termination: [12–24] months within the territory or a defined radius of the franchise location
- Reasonableness of scope must comply with local enforceability rules (see jurisdictional notes)

## Jurisdictional notes

### MENA — Franchise and Commercial Agency Law Risk

| Jurisdiction | Franchise-specific law | Risk of commercial agency law applying |
|---|---|---|
| **UAE** | No specific franchise law; Commercial Agencies Law (Federal Law No. 18/1981, as amended) may apply | If the franchisee is registered as a commercial agent, the mandatory protections apply — including compensation on termination and the ability to block competing brand entry; NOT registering avoids this but reduces franchisee's protection |
| **KSA** | No specific franchise law; Commercial Agencies Regulation may apply | Similar risk; MISA registration required for foreign franchisors; agency protections can apply |
| **Kuwait / Qatar / Bahrain** | GCC commercial agency laws apply similarly | Termination without compensation is very difficult for registered agents/franchisees |
| **Lebanon** | Commercial Agency Law (Legislative Decree 34/1967) applies if the franchisee qualifies as an agent | Structure as a license rather than agency to reduce mandatory compensation risk |
| **Egypt** | Commercial Code and agency provisions | Courts look at substance over form; if the franchisee in practice acts as an agent, agent protections may apply |

**Practical approach for MENA franchises**: Structure the franchise arrangement explicitly as a license of IP and know-how with the franchisee acting as an independent principal (not as agent of the franchisor). Avoid granting the franchisee the right to enter contracts on behalf of the franchisor. Include explicit language that the franchisee is an independent contractor.

### EU Franchise Disclosure

The EU Franchising Code of Ethics requires pre-contractual disclosure of key commercial information to prospective franchisees. Several EU member states have statutory pre-contractual disclosure laws (France — Loi Doubin, requiring disclosure 20 days before signing).

### US

Under the FTC Franchise Rule, franchisors must provide a Franchise Disclosure Document (FDD) at least 14 days before signing. State franchise registration laws apply in 14 states. This agreement does not address the FDD but counsel should confirm FDD compliance for US deals.

## Common mistakes

- **Commercial agency law not considered**: The single most costly mistake for MENA franchisors — failing to assess whether the franchisee will trigger mandatory commercial agency protections, making termination practically impossible.
- **Vague territory definition**: "The UAE" as a territory is clear; "the greater Dubai area" is not — define with specificity.
- **No exclusivity carve-out for online sales**: A territorial exclusive that does not address e-commerce allows the franchisor to sell online in the franchisee's territory; specify whether online sales are carved out.
- **Training obligations without cost allocation**: If the franchisee must send employees to the franchisor's training center in another country, who pays travel and accommodation? This must be stated.
- **Termination without cause provision**: Many UAE and KSA franchise agreements allow termination without cause; while this is contractually permissible in the free zone context, it may not be commercially reasonable for a franchisee with a significant upfront investment.

## Related skills

- [[prompt-pack-distribution-agreement]]
- [[prompt-pack-full-contract-risk-review]]
- [[prompt-pack-due-diligence-report]]
