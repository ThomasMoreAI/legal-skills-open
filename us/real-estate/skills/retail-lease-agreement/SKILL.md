---
name: retail-lease-agreement
title: Retail Lease Agreement
description: 'Drafts a U.S. retail lease agreement for shopping center or commercial property tenancies, covering base rent, percentage rent with gross sales definitions, CAM charges, continuous operation obligations, tenant improvement allowances, exclusive use clauses, radius restrictions, and default/remedies provisions. Use when drafting or negotiating retail leases, shopping center leases, or commercial storefront tenancy agreements. Trigger keywords: retail lease, shopping center lease, percentage rent, CAM charges, gross sales, exclusive use, radius restriction, tenant improvement allowance, triple net.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/retail-lease-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Retail Lease Agreement

Drafts a balanced retail lease for shopping center or commercial property tenancies covering financial, operational, and protective provisions for both landlord and tenant.

## Prerequisites

1. **Party information** — legal names, entity types, notice addresses for Landlord and Tenant
2. **Premises description** — unit number, address, center name, square footage (usable vs. GLA)
3. **Lease term** — commencement trigger (execution / delivery / opening), expiration, free-rent periods
4. **Rent structure** — base rent, escalation type, percentage rent rate and breakpoint
5. **Tenant improvements** — delivery condition, TI allowance amount, construction timeline
6. **Negotiated deal points** — exclusive use scope, radius restriction distance, CAM cap, merchants' association

## Output Structure

Draft sections in order. Populate from deal terms only — do not invent figures.

### 1. Parties & Premises

- Legal names, entity type, notice addresses
- Premises: unit, address, center name, SF basis (usable / GLA), included common areas

### 2. Lease Term & Commencement

- Start trigger, expiration date
- Rent abatement (within term or extends term — specify)
- Landlord delivery deadline; Tenant opening deadline

### 3. Base Rent & Escalations

| Period | Annual Rent | Monthly Rent | Escalation Basis |
|--------|-------------|--------------|------------------|
| Year 1 | [_] | [_] | Fixed |
| Year 2+ | [_] | [_] | Fixed % / CPI / FMV reset |

Payment: due 1st of month; remittance address/account; late fee and grace period.

### 4. Percentage Rent

- Rate: __% of Gross Sales
- Natural breakpoint = Base Rent ÷ Rate (or negotiated fixed breakpoint — specify which)
- Calculation period: monthly / quarterly / annual
- Reporting: within __ days after each period; annual certified statement
- Landlord audit rights: __ days notice; Tenant maintains records __ years

**Gross Sales — Include:** all revenues from business in/on/from Premises (cash, credit, layaway, online orders fulfilled from Premises, gift card redemptions, vending/kiosk)

**Gross Sales — Exclude:** returns/refunds, sales tax remitted, employee discounts (cap __%), insurance proceeds for damaged/stolen goods, fixture/equipment sales not in ordinary course

### 5. Additional Rent (Triple-Net Pass-Throughs)

| Charge | Share Basis | Cap / Exclusions |
|--------|-------------|------------------|
| CAM | Pro-rata (Premises SF ÷ total GLA) | Annual increase cap: __%; exclude capital items with useful life >1 yr |
| Real Estate Taxes | Pro-rata | Include special assessments? [Y/N] |
| Property Insurance | Pro-rata | Landlord maintains building/CA policy; Tenant pays share |

Reconciliation: annual statement within __ days of year-end; Tenant audit right on __ days notice.

**Tenant's Own Insurance (Tenant's sole cost):**
- CGL: $__M per occurrence / $__M aggregate
- Property/contents: replacement value
- Business interruption: __ months

### 6. Permitted Use & Continuous Operation

- **Permitted Use:** exact description of products/services and trade name — no broad categories
- **Continuous Operation:** operate during all hours center is open to public
- **Dark store remedy:** percentage rent adjustment / termination right / liquidated damages — specify
- **Permitted closures:** casualty restoration, force majeure, remodeling with Landlord approval (max __ days)

### 7. Premises Delivery & Tenant Improvements

**Delivery Condition:** As-is / Broom clean / Vanilla box (HVAC, electrical, plumbing stubbed)

**TI Allowance:**

| Element | Value |
|---------|-------|
| Amount | $__ PSF / $__ total |
| Eligible costs | Hard construction; architectural fees / permits / PM (specify) |
| Disbursement | Paid invoices + unconditional lien waivers; Landlord pays within __ days |
| Expiration | Forfeited if not drawn by __ |

**Construction:** Licensed/insured contractors; Landlord-approved plans; all permits and ADA compliance; completion __ days after delivery; open for business __ days after delivery. Delay carve-outs: force majeure and Landlord-caused delays (excusable); all others unexcused.

### 8. Signage

- Exterior, window, and illuminated signage requires prior written Landlord approval
- Comply with center signage criteria, local zoning, and design guidelines
- Tenant bears all fabrication, installation, maintenance, and removal costs

### 9. Exclusive Use & Radius Restriction

**Exclusive Use (if negotiated):**

| Element | Value |
|---------|-------|
| Protected category | [specific products/services] |
| Scope | Entire center / Inline only (excludes anchors/pads) |
| Carve-outs | Existing tenants as of Lease Date; de minimis (<__% of sales) |

**Radius Restriction (if negotiated):**

| Element | Value |
|---------|-------|
| Radius | __ miles from Premises |
| Duration | Coterminous with Lease (+ __ months post-expiration if negotiated) |
| Scope | All locations / Same trade name or ownership only |

### 10. Default & Remedies

| Default Type | Notice | Cure Period |
|-------------|--------|-------------|
| Monetary | Written | __ days (typically 5–10) |
| Non-monetary (curable) | Written | 30 days; extended if cure diligently pursued |
| Non-monetary (incurable) | Written | None |

**Landlord remedies:** termination; re-entry/repossession; reletting on Tenant's account; damages = unpaid rent + reletting costs + unamortized TI + PV of remaining rent less reletting proceeds.

Verify remedies comply with applicable state landlord-tenant law. Do not include unenforceable penalty provisions. `[VERIFY]`

### 11. Standard Commercial Provisions

- Assignment/subletting: Landlord consent required; reasonable criteria
- Maintenance: Tenant → interior; Landlord → structure, roof, common areas
- Indemnification: mutual, based on respective negligence/willful misconduct
- Casualty/condemnation: restoration obligations and termination thresholds
- SNDA (subordination, non-disturbance, attornment)
- Estoppel certificates: deliver within __ days of request
- Merchants' association: dues $__ initial; adjustment mechanism __
- Dispute resolution: Litigation / Arbitration (AAA Commercial Rules)
- Governing law: State of __

### 12. Signature Blocks

- Authorized signatories with title and date for each party
- Corporate authority recitals for entity parties
- Notarization / witness lines if required by state law or for recording

## Guidelines

- **Gross Sales definition** is the most heavily negotiated provision — flag online/omnichannel sales attribution ambiguities for client review
- **CAM exclusions**: confirm whether management fees are capped (commonly 10–15% of CAM) and whether capital replacements are excluded or amortized
- **Continuous operation** may be unenforceable as specific performance in some jurisdictions — consider liquidated damages alternative `[VERIFY]`
- **ADA compliance** responsibility must be allocated explicitly (common area vs. Premises interior)
- **TI disbursements**: confirm lien waiver requirements comply with state mechanics' lien statutes `[VERIFY]`
- **Percentage rent breakpoints**: distinguish natural (Base Rent ÷ Rate) from artificial (negotiated fixed) — document which applies
- Tag jurisdiction-specific citations with `[VERIFY]` when accuracy is uncertain
