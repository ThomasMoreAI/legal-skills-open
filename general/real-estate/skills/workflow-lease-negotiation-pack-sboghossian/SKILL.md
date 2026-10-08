---
name: workflow-lease-negotiation-pack-sboghossian
title: Lease Negotiation Pack
description: Use when negotiating or reviewing a commercial or residential lease agreement — for tenant or landlord — across MENA jurisdictions. Covers pre-negotiation assessment, full deliverable set (lease, heads of terms, inventory, insurance, registration documents), negotiation axes (rent escalation, service charge, break clauses, use clause), and post-completion registration requirements (Ejari/Dubai, Tawtheeq/Abu Dhabi, Ejar/KSA, MOET/Lebanon) with VAT and RERA rent-cap compliance notes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-lease-negotiation-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Lease Negotiation Pack

## Purpose

This workflow delivers a complete lease negotiation for either party — tenant or landlord — including pre-negotiation assessment, document generation, negotiation strategy, and post-completion registration compliance. It covers commercial and residential leases across MENA jurisdictions with particular depth on UAE, KSA, and Lebanese market practice.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Side | Yes | Tenant or landlord — analysis is side-specific |
| Property type | Yes | Commercial (office, retail, warehouse, industrial) or residential |
| Property location + jurisdiction | Yes | Drives applicable law and registration requirements |
| Intended use | Yes | Drives use clause, zoning check, permitted activities |
| Counterparty details | Recommended | Landlord: tenant financial health; Tenant: title verification |
| Proposed rent and term | Yes | Starting point for negotiation |
| Required fit-out or modifications | If applicable | Triggers negotiation on landlord's fit-out contribution |
| Current market comparables | Recommended | Needed for rent benchmarking |

---

## Logic — Pre-Negotiation Phase

### Side-Specific Analysis

Load the appropriate review skill:
- Tenant perspective: [[review-lease-tenant-side]]
- Landlord perspective: [[review-lease-landlord-side]]

**Tenant due diligence on landlord:**
- Is the landlord the registered owner of the property? Verify via land registry or RERA records
- Is there a mortgage over the property? Mortgagee consent may be needed for a long lease
- Any disputes or litigation involving the property?
- Financial stability of the landlord entity (particularly important for landlords promising fit-out contributions or significant tenant incentives)

**Landlord due diligence on tenant:**
- Financial statements or bank statements (2–3 years for commercial tenants)
- References from previous landlords
- Credit check for individual tenants
- For SME tenants: consider requiring a personal guarantee from directors

### Market Assessment

- Review comparable rents in the same building, sub-market, and district
- In Dubai: RERA Rent Calculator — check the permissible rent range for the specific property against the existing tenant (for renewals)
- In Abu Dhabi: ADREC rental guidelines
- In KSA: Ejar platform for market reference rates

---

## Deliverables

| Document | Notes |
|----------|-------|
| Letter of intent / Heads of Terms | Non-binding summary of agreed commercial terms; provides negotiating framework |
| Lease agreement | [[draft-commercial-lease]] or [[draft-residential-lease]] — full form or abbreviated depending on term |
| Inventory and condition report | Schedule annexed to lease; documents pre-existing condition |
| Premises plan and drawings | Defines the exact space demised |
| Insurance certificates | Evidence of required insurance by each party at commencement |
| Security deposit / bank guarantee documentation | Amount, terms, return conditions |
| Registration documents | Ejari, Tawtheeq, Ejar, or MOET (see below) |

---

## Logic — Key Negotiation Axes

### 1. Rent and Escalation

| Mechanism | Description | MENA practice |
|-----------|-------------|--------------|
| Fixed rent | Same rent for full term | Simple; common for short terms |
| Fixed increases | Annual % increase agreed upfront (e.g., 5% per annum) | Landlord favors; common in UAE for 1–3 year terms |
| CPI-linked | Increases tied to published inflation index | Fair; used in international leases |
| Market-reviewed | Rent reviewed to prevailing market at review dates | Landlord favors; tenant wants cap on increase |
| RERA-capped | Dubai: RERA calculator caps increase for renewals based on comparable rents | Mandatory for Dubai residential; standard practice for commercial |

**Tenant negotiating position**: seek capped escalation (CPI capped at 5%) or fixed steps; avoid open market review without a cap.

**Landlord negotiating position**: seek upward-only review; aim for inflation-plus escalation.

### 2. Service Charge

- Commercial leases in MENA often add a service charge on top of base rent covering: building maintenance, security, cleaning, HVAC, common area utilities
- Tenant risks: unlimited service charge with no audit right creates exposure
- Tenant should negotiate: (a) the service charge budget is provided annually; (b) tenant has the right to audit actual expenditure; (c) service charge is capped at a % above the previous year's charge; (d) landlord must justify significant increases

### 3. Repair and Dilapidations

| Obligation | Tenant-favorable | Landlord-favorable |
|-----------|-----------------|-------------------|
| Structural repairs | Landlord's responsibility | Tenant responsible |
| Interior repairs | Fair wear and tear excluded | Full reinstatement |
| Dilapidations at expiry | Cap on dilapidations cost | Full schedule of condition |

Best practice: annex a schedule of condition photographed at lease commencement; limits tenant's reinstatement obligations to the condition documented.

### 4. Use Clause

- Narrow use clause: protects landlord but restricts tenant
- Wide use clause: gives tenant flexibility for business changes
- **Tenant should seek**: broadly drafted use clause covering the current business and reasonably foreseeable expansions; e.g., "for use as an office and ancillary uses"
- **Landlord should seek**: defined permitted use with a tenant covenant to comply with statutory requirements for that use

### 5. Break Clauses

A break clause allows one or both parties to terminate the lease before expiry on defined notice:
- **Tenant break**: gives tenant flexibility; most valuable for growing or uncertain businesses; target: tenant option to break at year 3 of a 5-year lease on 6 months' notice
- **Landlord break**: allows landlord to redevelop; tenant should resist or require compensation
- Break conditions: often require payment of all arrears, vacation of the premises, and compliance with repairing obligations — conditions must be strictly satisfied or break fails

### 6. Subletting and Assignment

- **Tenant perspective**: right to sublet or assign provides flexibility; resist blanket prohibition
- Standard position: subletting and assignment permitted with landlord's prior written consent, not to be unreasonably withheld or delayed
- **Landlord perspective**: control over sub-tenants is reasonable; require information about sub-tenant; no sub-letting at a premium (rack rent)

### 7. Renewal Rights

- **Tenant option to renew**: the most valuable tenant right; ensure option is clear: notice period (typically 6–12 months before expiry), exercise mechanism, rent at renewal (at market or pre-agreed)
- **Landlord discretion**: if no renewal option, tenant has no right to stay at expiry (subject to statutory protections in some jurisdictions)

---

## Pre-Completion Checklist

Before lease execution and occupation:

- [ ] Final lease text agreed and signed by both parties
- [ ] Inventory and condition report signed by both parties
- [ ] Insurance certificates exchanged (confirm each party has required coverage)
- [ ] Security deposit / bank guarantee received and confirmed
- [ ] Bank guarantee in place (if required instead of cash deposit)
- [ ] Utility transfers arranged (electricity, water, internet service account transfers)
- [ ] Move-in date confirmed
- [ ] Key and access handover schedule agreed

---

## Post-Completion — Registration and Compliance

Registration with the relevant authority is mandatory within the statutory window:

| Jurisdiction | System | Deadline | Consequence of non-registration |
|-------------|--------|---------|-------------------------------|
| Dubai (commercial and residential) | Ejari — Dubai Land Department | Before move-in; typically within 30 days | Unregistered lease not enforceable in RERA disputes; utility connection may be refused |
| Abu Dhabi (residential) | Tawtheeq — Abu Dhabi Municipality | Before move-in | Similar enforcement risk |
| Abu Dhabi (commercial) | ADREC registration system | Within registration period | Enforcement limitation |
| KSA (commercial and residential) | Ejar — Ministry of Human Resources | Within 30 days of execution | Significant enforcement limitation; access to government Ejar dispute resolution unavailable |
| Lebanon | MOET — Ministry of Economy and Trade registration for commercial leases | Within 15 days | Affects tax registration; may affect enforcement |
| DIFC | DIFC leases do not use UAE mainland registration systems; governed by DIFC lease terms and DIFC Courts | N/A for Ejari | DIFC Courts jurisdiction |

**VAT treatment (UAE):**
- Commercial leases: subject to 5% VAT; landlord must issue a VAT invoice
- Residential leases: generally exempt from UAE VAT; confirm current rules with VAT adviser

**RERA rent caps (Dubai):**
- Law No. 26 of 2007 (as amended) regulates landlord-tenant relations in Dubai
- RERA Rent Increase Calculator determines the maximum permissible increase on renewal based on comparable properties
- Landlord cannot increase rent beyond the RERA calculator output; dispute route: RERA Committee

---

## Jurisdictional Notes

### UAE (General)

- Federal Law No. 6 of 2007 (Consumer Protection in Real Estate) and emirate-level laws govern
- Dubai: Landlord-Tenant Law; RERA is the regulator; Rental Dispute Settlement Centre handles disputes
- Abu Dhabi: Law No. 20 of 2006 and ADREC regulations
- Free zones (DIFC, JAFZA, etc.): their own leasing rules apply; not subject to main UAE landlord-tenant laws

### KSA

- Ejar system: digital contract; protects both parties; mandatory for all real estate lease contracts
- Anti-eviction protections during Ramadan: eviction enforcement typically paused during Ramadan
- Commercial lease disputes: Real Estate courts / arbitration

### Lebanon

- Civil Code provisions on leases; several special laws for commercial tenants (older law provides significant tenant protections including automatic renewal rights for commercial tenants in some circumstances)
- Currency: specify explicitly whether rent is in USD or LBP; USD denomination strongly recommended for any new commercial lease given LBP instability

---

## Related Skills

- [[draft-commercial-lease]]
- [[draft-residential-lease]]
- [[review-lease-tenant-side]]
- [[review-lease-landlord-side]]
- [[workflow-startup-incorporation-pack]]
- [[wiki-research]]
