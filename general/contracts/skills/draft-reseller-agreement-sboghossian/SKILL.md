---
name: draft-reseller-agreement-sboghossian
title: Reseller Agreement
description: Use when drafting a reseller agreement for B2B SaaS, digital products, or technology goods — governing the relationship between a product vendor and a reseller who sells to end customers. Distinct from a distribution agreement (physical goods) and a commercial agency (agent acts on behalf of the vendor). Covers margin/commission structures, territory and marketing restrictions, branding (co-branded vs vendor-branded), customer relationship ownership, IP protection, and termination/transition provisions. Triggers on "reseller agreement", "reseller contract", "value-added reseller", "VAR agreement", or "channel partner agreement" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-reseller-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Reseller Agreement

## When to use this

A reseller agreement governs a commercial channel relationship where:
- The **Vendor** (also called Supplier or Principal) owns the product or service
- The **Reseller** (also called Channel Partner or VAR — Value-Added Reseller) purchases or licenses the product and resells it to end customers in their own name

Key distinction from related instruments:
- **vs. Distribution Agreement**: a distribution agreement typically involves physical goods and local stocking; a reseller agreement is more commonly used for SaaS, digital products, and technology licenses
- **vs. Commercial Agency**: a commercial agent acts on behalf of the vendor and binds the vendor in contracts with customers; a reseller buys and resells in its own name and bears its own commercial risk
- **vs. MSA**: a reseller agreement defines the ongoing channel relationship; it does not govern custom professional services delivery

**MENA caution**: in UAE, KSA, and Qatar, a channel arrangement that involves exclusive territory rights and a reseller "promoting" the vendor's products may be characterized as a commercial agency under local commercial agency laws, which provide strong statutory protection to the local party (automatic renewal, compensation on termination). Structure the agreement carefully to avoid this — see Jurisdictional notes.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Vendor (principal) | Full identification | — must supply |
| Reseller | Full identification | — must supply |
| Products / services being resold | Specific product catalog or list | — must supply |
| Territory | Where the Reseller may resell | Named countries / regions |
| Exclusivity | Exclusive / non-exclusive / sole | Non-exclusive |
| Pricing and margin | Reseller purchase price or commission rate | Per negotiated price list |
| Term | Duration of the agreement | 1 year, auto-renewing |
| Governing law | | Vendor's home jurisdiction |

## Document structure

### 1. Parties and recitals
Full identification. Recitals: Vendor's product and business; Reseller's market access and capability; mutual intent to establish a reseller relationship.

### 2. Definitions
Key terms: Products, Territory, End Customer, End Customer Agreement, Reseller Price, MSRP (Manufacturer's Suggested Retail Price), Confidential Information, Intellectual Property, Term, Renewal Term.

### 3. Appointment and scope

**Appointment**: Vendor appoints Reseller as a [non-exclusive / exclusive] reseller of the Products in the Territory during the Term.

**Non-exclusive** (most common): Vendor retains the right to appoint other resellers in the same Territory and to sell directly to end customers. The Reseller bears market competition risk.

**Exclusive**: Vendor appoints only this Reseller in the Territory; Vendor may not sell directly or appoint other resellers in the Territory during the Term. Requires higher commitment obligations from the Reseller (minimum purchase volumes, marketing spend).

**Products**: attach a product catalog as Schedule 1; specify whether new products are automatically included or require a Schedule amendment.

### 4. Reseller obligations

Core obligations:
- Use commercially reasonable efforts to promote and sell the Products in the Territory
- Achieve the minimum purchase/revenue commitment (if any) — see below
- Market the Products in accordance with Vendor's brand guidelines
- Not make representations about the Products that are inconsistent with Vendor's official documentation
- Promptly notify Vendor of any customer complaints, defects, or regulatory issues relating to the Products
- Maintain required certifications, training, or technical qualifications (Vendor may require technical certifications)
- Comply with applicable laws in the Territory (export controls, data privacy, sector regulations)
- Report sales activity to Vendor: monthly summary of orders placed and pipeline

### 5. Pricing and margin

**Reseller pricing model — two main approaches**:

**Option A (Reseller buys at Reseller Price)**:
- Vendor publishes a Reseller Price (MSRP less an agreed discount, e.g., 20-40% off MSRP)
- Reseller pays Vendor the Reseller Price; Reseller determines the price it charges end customers (floor: Reseller Price; ceiling: up to MSRP or market-based)
- Vendor may set a minimum price (MAP — Minimum Advertised Price) to protect brand value; but cannot in most jurisdictions fix the actual resale price (resale price maintenance = competition law violation in EU/UK)

**Option B (Commission on sales)**:
- Reseller brings customers and signs contracts in Vendor's name (or generates orders for Vendor)
- Vendor pays Reseller a commission on sales
- This structure is closer to a commercial agency — be careful with commercial agency law in MENA

**Most-favored-reseller clause**: if Vendor offers better terms (lower Reseller Price) to any other reseller in the Territory, it must offer those same terms to this Reseller. Include if the Reseller has bargaining leverage.

### 6. Minimum purchase / revenue commitment

If exclusivity is granted or Vendor is making a significant commitment:
- Reseller commits to minimum annual purchase orders or revenue (e.g., USD 500,000 per year)
- If Reseller fails to meet the minimum: Vendor may convert the arrangement to non-exclusive (preferred over termination for commercial continuity); or Vendor may terminate
- Quarterly review points: Reseller provides progress report; Vendor may adjust the minimum on renewal

### 7. Co-branded vs Vendor-branded sales

**Vendor-branded sales** (most common for SaaS and digital products):
- Reseller sells under Vendor's brand name
- Customers know they are purchasing Vendor's product
- Reseller's brand appears as a "reselling partner" or "powered by" disclosure
- Vendor's brand guidelines control marketing materials

**Co-branded sales** (common for bundled solutions):
- Reseller sells under a combined brand (Reseller's brand + Vendor's product)
- Vendor's product is an embedded component of Reseller's solution
- Requires specific brand licensing provisions in the agreement

**White-label / OEM** (separate agreement needed):
- Reseller sells the product under Reseller's own brand with no reference to Vendor
- Vendor's brand is completely suppressed
- Different commercial model; typically higher volume; different IP and support obligations

### 8. Customer relationship ownership

This is the most commercially sensitive provision:

**Standard (Vendor retains relationship)**:
- Reseller introduces and manages the relationship; but the End Customer Agreement is between the customer and the Vendor (or includes Vendor as a party)
- Vendor has direct visibility into customer use, support tickets, and renewal
- Vendor retains the right to communicate directly with customers

**Reseller-owns-the-customer**:
- The End Customer Agreement is between the Reseller and the end customer only; Vendor's name may not even appear
- Vendor has no direct relationship with the customer
- Higher risk for Vendor: if Reseller fails, customers cannot be moved; Vendor has no leverage on renewal
- Only appropriate for Vendor if Reseller is much larger, or for strategic distribution market penetration

**Best practice for Vendor**: Vendor-owns-the-customer, with Reseller as the sales and implementation layer. Reseller gets commission or margin, but the contract of record is between Vendor and the customer.

### 9. End customer agreement
- Reseller must ensure each end customer accepts Vendor's standard End Customer Agreement (EULA / subscription terms) before use
- Reseller is not authorized to modify the End Customer Agreement without Vendor's prior written consent
- Reseller's liabilities to end customers are Reseller's own; Vendor is not responsible for Reseller's representations

### 10. Intellectual property
- Vendor retains all ownership of the Products, brand, trademarks, and technology
- Vendor grants Reseller a limited, non-exclusive license to use the Vendor's trademarks and marketing materials solely to promote and sell the Products in the Territory
- Reseller may not modify the Products, decompile the software, or create derivative works
- Reseller's customer relationships and customer data generated through the Reseller channel remain Reseller's property (subject to Vendor's rights under the End Customer Agreement)

### 11. Support and training
- Who provides first-line support to end customers — Reseller or Vendor?
- Escalation: if Reseller provides first-line support, specify the escalation path to Vendor for second-line and third-line support
- Training: Vendor provides initial certification training; Reseller must maintain current certification; Reseller's staff must pass Vendor's technical exam

### 12. Term and termination

**Term**: [1] year; auto-renewing unless [60]-day prior notice.

**Termination for cause**:
- Either party may terminate for material breach with a [30]-day cure period
- Vendor may terminate immediately if Reseller: violates export controls; misrepresents the Products; becomes insolvent

**Termination for convenience**: [90]-day notice (Vendor); [30]-day notice (Reseller). Longer notice for Vendor protects Reseller's pipeline.

**Consequences of termination**:
- Reseller ceases all sales activities immediately on termination
- Reseller must notify affected end customers
- Existing customer contracts: Vendor may assume directly or appoint a replacement reseller to take over support
- **Transition assistance**: Reseller cooperates to transfer open deals and customer relationships
- **No compensation**: unless the agreement expressly provides for it, there is no automatic goodwill payment or compensation on termination — but see Jurisdictional notes (commercial agency laws)

### 13. Governing law and dispute resolution

## Jurisdictional notes — MENA commercial agency risk

In UAE, KSA, Qatar, Bahrain, and Kuwait, a reseller arrangement with exclusive territory and significant promotional activity may be characterized as a commercial agency:
- **UAE Commercial Agency Law (Federal Law 3/1987 as amended)**: if the arrangement involves an "agent" registered with the Ministry of Economy, the agent has statutory protection including automatic renewal and compensation on termination
- **KSA Commercial Agency Law**: similar strong protection for the local agent
- **Risk**: if the reseller is characterized as a commercial agent and registers as such, the Vendor cannot simply terminate the arrangement; termination may require significant compensation

**Avoidance measures**:
1. State expressly: "This agreement is not a commercial agency; Reseller acts as principal in its own right"
2. Do not use "agent" or "representative" language anywhere in the agreement
3. Ensure the Reseller contracts in its own name with customers, not in Vendor's name
4. Consider appointing multiple non-exclusive resellers rather than one exclusive reseller
5. Take local counsel advice in each GCC state before appointing exclusive channel partners

## Common mistakes

- Granting exclusivity without minimum purchase commitments — Vendor is locked out of the territory with no revenue guarantee
- Reseller-owns-customer model for SaaS — Vendor has no visibility or direct relationship; customer data and renewals at risk
- No brand guidelines or minimum quality standards — Reseller damages Vendor's brand in the Territory
- Forgetting the commercial agency characterization risk in MENA exclusive arrangements
- No transition/handover obligations on termination — customers are stranded mid-contract

## Related skills

- [[draft-distribution-agreement]]
- [[draft-msa]]
- [[draft-licensing-agreement-software]]
- [[draft-ip-licensing]]
