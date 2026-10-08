---
name: draft-commercial-lease-sboghossian
title: Draft — Commercial Lease
description: Use when asked to draft a commercial lease for office, retail, or industrial premises. Covers the full clause set — premises, use, rent and service charge, VAT, rent review, fit-out and makegood, repair, insurance, alienation, forfeiture, and quiet enjoyment — with jurisdiction-specific notes for UAE onshore, DIFC/ADGM (FRI lease norms), KSA (15% VAT), Lebanon (commercial lease law and fonds de commerce protections), and Egypt. Required inputs include landlord, tenant, premises, rent, term, use, and jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-commercial-lease
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Draft — Commercial Lease

## When to use this

Use this skill to draft a commercial lease for:
- **Office space** (fitted or shell-and-core)
- **Retail premises** (shopping mall, high-street, standalone)
- **Industrial / warehousing** (logistics, manufacturing)
- **Free-zone premises** in UAE (DIFC, ADGM, JAFZA, DAFZA, etc.)

Commercial leases carry fewer mandatory tenant-protection rules than residential leases in most jurisdictions, giving parties more freedom of contract. However, certain MENA protections (notably in Lebanon) are mandatory and cannot be contracted out.

## Required inputs

| Input | Notes |
|---|---|
| Landlord | Full legal name; registration number; signatory authority |
| Tenant | Full legal name; registration number; signatory authority; trade license copy (for use clause alignment) |
| Premises | Precise description: floor, unit number, gross area (sqm), common areas defined, parking allocation |
| Permitted use | Must match Tenant's trade license and regulatory authorizations — critical |
| Rent | Base rent; currency; payment frequency (monthly/quarterly/annually in advance); first rent payment date |
| Service charge / CAM | Basis; cap (if negotiated); reconciliation mechanism |
| Term | Start date (or condition for start); end date; renewal option |
| Jurisdiction | Onshore UAE / DIFC / ADGM / KSA / LB / EG — governs mandatory requirements |

## Optional inputs

- Rent-free period / fit-out period
- Turnover rent (retail)
- Tenant's fit-out specification and landlord approval process
- Break clause (either party's right to terminate early)
- Security deposit amount and release conditions
- Personal guarantee from tenant's parent or principals

## Document structure

### 1. Parties
Full legal names, addresses, registration numbers, authorized signatories. Include tenant's trade license number and licensing authority — the use clause will reference it.

### 2. Premises
- Precise address, floor, unit number.
- Floor plan attached as Schedule.
- Measurement standard (net internal area vs gross internal area vs gross external area — specify; this affects rent calculations).
- Common areas: lobby, lifts, toilets, loading bay — defined and allocated.
- Parking: number of spaces, location, whether dedicated or shared.

### 3. Use clause
**Critical**: the permitted use must align with the tenant's regulatory licenses.
- Too narrow: tenant cannot adapt the business or sublease.
- Too broad: landlord loses control over the tenant mix (important for retail centers).

Standard language:
> "The Tenant shall use the Premises solely for the purpose of [specific use — aligned to trade license] and shall not, without the Landlord's prior written consent (not to be unreasonably withheld), use or permit the use of the Premises for any other purpose."

Use clause change: require landlord consent; landlord may condition consent on conformity with a retail center's concept.

### 4. Term
- Commencement date (or condition: "the date the Tenant receives its trade license" — specify fallback).
- Expiry date.
- Renewal option: mechanism (notice period, negotiated vs automatic, any rent cap on renewal).
- Holdover: what happens if tenant remains after expiry — "holding over" rent (often 1.5–2× monthly rent as deterrent).

### 5. Rent and payment mechanics
- **Base rent**: annual amount ÷ payment frequency; specify in words and figures.
- **Payment method**: bank transfer to specified account; advance by cheques (UAE practice: post-dated cheques for the full year is common).
- **Late payment interest**: commercial rate; specify clearly; for KSA use "delay compensation" language.
- **Rent review**: mechanism and frequency (every 3–5 years). Options:
  - Fixed step-up (e.g., 5% per annum — simple, landlord-friendly).
  - CPI-linked (tracks inflation — balanced).
  - Open market review (full renegotiation — tenant risk in strong markets).
- **Turnover rent** (retail): percentage of tenant's gross sales above a threshold; requires tenant to provide audited turnover figures.

### 6. Service charge and common area maintenance (CAM)
- What is included: management, maintenance, cleaning, security, utilities for common areas, insurance of building, reserve fund.
- **Fixed service charge** vs **variable** (actual cost basis).
- **Cap**: tenant should negotiate a cap on service charge increases.
- **Audit right**: tenant's right to inspect service charge accounts.
- **Exclusions**: capital expenditure items, sinking fund contributions (or define clearly).

### 7. VAT and taxes
- **UAE**: 5% VAT applies to commercial rent (Federal Decree-Law 8/2017).
- **KSA**: 15% VAT applies to commercial rent (standard rate post-2020).
- State whether rent is quoted inclusive or exclusive of VAT; exclusive is standard in commercial leases.
- Tenant responsible for any stamp duty, registration fees, or transaction taxes.

### 8. Fit-out and tenant works
- **Landlord's works**: what condition is the premises delivered in (shell-and-core vs ready-fit; specify MEP connections, air-conditioning status).
- **Tenant's fit-out**: obligation to carry out fit-out within a specified period; landlord approval required for design and structural changes.
- **Fit-out period / rent-free**: common in negotiated commercial leases; specify exact period during which no base rent or reduced rent is payable.
- **Landlord's fit-out contribution** (in competitive markets): landlord may contribute a per-sqm allowance; specify conditions for payment.
- **Makegood obligations**: at lease end, tenant must return premises in agreed condition (typically: as delivered / shell-and-core, or fitted condition per schedule).

### 9. Repair and maintenance
- **Landlord's obligations**: structure, exterior, roof, common areas, building services.
- **Tenant's obligations**: interior; fit-out; fixtures and fittings.
- **FRI lease** (Full Repairing and Insuring — common in DIFC/ADGM/UK): all repair and insurance responsibility passes to tenant; tenant may be required to repair the entire building.
- Repair standard: "good and substantial repair and condition, fair wear and tear excepted."
- Schedule of condition: attach a photographic schedule at lease commencement; limits tenant's repair liability to the condition shown.

### 10. Insurance
- **Landlord insures**: building (reinstatement cost basis), public liability for common areas.
- **Tenant insures**: contents, fit-out, plate glass, public liability for the premises, workers' compensation.
- Both parties name each other as additional insured where appropriate.
- Tenant must provide landlord with evidence of insurance annually.

### 11. Alienation — assignment, subletting, change of control
- **Assignment**: tenant's right to assign the lease (transfer to a third party), subject to landlord consent. Landlord may condition consent on: creditworthiness of assignee, assignee assuming all obligations.
- **Subletting**: sublet of whole or part; landlord consent.
- **Change of control**: a change of majority ownership of the tenant entity — treated as an assignment for consent purposes (important for private equity-owned tenants).
- **Permitted transfers to affiliates**: usually permitted without consent (with notice).

### 12. Landlord's consent standard
The standard "not to be unreasonably withheld, conditioned, or delayed" gives the tenant recourse if the landlord is obstructive. Specify this in assignment and use-change clauses.

### 13. Forfeiture / termination for breach
- **Right of re-entry**: landlord may terminate and re-enter if tenant breaches (especially non-payment of rent).
- **Notice and cure period**: tenant must receive notice and have an opportunity to remedy (typically: 30 days for rent arrears; 14 days for other breaches with immediate cure for repeated breaches).
- **Insolvency**: landlord may terminate immediately on tenant's insolvency or appointment of receiver.
- **Relief from forfeiture**: in common-law jurisdictions (DIFC, ADGM, UK), courts have equitable jurisdiction to relieve a tenant from forfeiture if the breach is remedied.

### 14. Quiet enjoyment
> "The Landlord covenants with the Tenant that, so long as the Tenant performs its obligations under this Lease, the Tenant shall have quiet enjoyment of the Premises without any interruption or disturbance by the Landlord or any person claiming under or through the Landlord."

This is a fundamental landlord obligation; include it in every commercial lease.

### 15. Boilerplate
Standard governing law, dispute resolution (see [[draft-boilerplate-clauses]]), notices, entire agreement, and counterparts.

## Jurisdictional notes

### UAE onshore
- **RERA (Real Estate Regulatory Authority, Dubai)**: commercial leases must be registered on Ejari system.
- **DIFC**: leases with DIFC-registered tenants are typically governed by DIFC law; FRI norms common.
- **Abu Dhabi**: Tawtheeq registration system for commercial leases.
- **VAT**: 5%; standard commercial practice is rent exclusive of VAT.
- **Post-dated cheques**: standard payment mechanism; bounce of a security cheque is a criminal offense — serious leverage for landlords.

### KSA
- **Municipal authority registration**: commercial leases to be registered.
- **VAT**: 15%; state clearly in lease.
- **Foreign tenants**: require valid commercial registration and MISA license.
- **Interest / late payment**: use delay compensation language.

### Lebanon — commercial lease law and fonds de commerce
- Lebanon's Law on Commercial Leases provides **mandatory tenant protections** that cannot be contracted out:
  - **Renewal rights**: a long-standing commercial tenant has a right to lease renewal.
  - **Fonds de commerce / goodwill** (pas de porte): on non-renewal by the landlord, the tenant is entitled to compensation for the goodwill (valeur locative / valeur commerciale) developed in the premises.
  - This compensation can be substantial in prime commercial locations.
- **Practical implication**: landlords negotiating commercial leases in Lebanon must understand they may not be able to remove a tenant without significant compensation; this affects lease structuring and rent levels.
- **Ejection**: requires court proceedings; protracted.
- Leases in Arabic or French; Arabic preferred for official purposes.

### Egypt
- **Civil Code**: general lease principles apply to commercial leases; less specific commercial lease legislation than Lebanon.
- Registration with Real Estate Publicity Authority recommended.
- VAT: 14% standard rate applies to commercial rent.

### DIFC / ADGM
- English common law and FRI lease norms apply.
- Arbitration: DIFC-LCIA or ADGM Arbitration Centre.
- No stamp duty; lease registration with DIFC/ADGM authority.

## Common mistakes

- **Premises not precisely defined**: disputes about what area is leased (and the rent payable per sqm) are common; always attach a floor plan.
- **Use clause wider than trade license**: tenant cannot legally operate a use not covered by its trade license; misalignment causes regulatory enforcement risk.
- **No schedule of condition**: without it, the tenant is liable to return the premises in a standard better than they received them; attach a photographic schedule at handover.
- **Post-dated cheques for full rent without security deposit clause**: if cheques bounce, landlord has recourse but must pursue the criminal route; a separate security deposit provides parallel protection.
- **Lebanese lease without goodwill clause assessment**: drafters unfamiliar with the fonds de commerce regime may inadvertently create a lease that entitles the tenant to very large compensation on non-renewal.
- **Makegood obligations ambiguous**: "original condition" is ambiguous — define clearly whether this means shell-and-core, as delivered, or as fitted.

## Related skills

- [[draft-boilerplate-clauses]]
- [[draft-board-resolution]]
- [[review-contract-general]]
- [[draft-bilingual-ar-en-side-by-side]]
