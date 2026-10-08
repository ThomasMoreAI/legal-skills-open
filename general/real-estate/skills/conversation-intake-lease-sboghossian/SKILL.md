---
name: conversation-intake-lease-sboghossian
title: Intake — Lease
description: Use when a user wants to draft or review a lease agreement and Claude must collect the minimum viable inputs before generating the document. Triggers on requests to prepare a tenancy agreement, lease contract, or rental arrangement for residential, commercial, or industrial premises. Covers MENA registration regimes (Dubai Ejari, Abu Dhabi Tawtheeq, KSA Ejar, Lebanon) and common-law equivalents (DIFC, ADGM, UK).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-lease
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Intake — Lease

## When this applies

Activate when a user requests help drafting, reviewing, or registering a lease or tenancy agreement for any type of premises. This skill gathers the mandatory fields before routing to the appropriate drafting skill. The lease type and jurisdiction together control which statutory framework governs rent-increase caps, eviction procedure, registration mandates, and security deposit rules.

## Behavior

Single-turn intake (or two-turn maximum). Extract any information already given and ask only for what is missing. Offer to identify sensible defaults for less commercially sophisticated users.

## Required fields

### 1. Lease type

The statutory framework differs by use category. Confirm one of:

| Type | Notes |
|---|---|
| Residential | Typically highest statutory protection for tenant; rent-increase caps, eviction grounds restricted |
| Commercial | Less tenant-protective; parties have more freedom of contract in many MENA jurisdictions |
| Industrial / warehouse | Often treated as commercial; zoning compliance is key |
| Retail / high-street shop | May have sector-specific regulations (mall leases in UAE have bespoke terms) |
| Mixed-use | Bifurcated analysis — residential portions governed by residential rules |

### 2. Jurisdiction

This determines the registration authority, mandatory form, and substantive rights:

| Jurisdiction | Registration body | Key statutory instrument |
|---|---|---|
| Dubai | RERA (Real Estate Regulatory Agency); registration via Ejari portal | Dubai Law No. 26/2007 on Regulating the Relationship between Lessors and Lessees; Dubai Decree No. 43/2013 (rent-increase index, RERA calculator) |
| Abu Dhabi | Tawtheeq (Department of Municipalities and Transport) | Abu Dhabi Law No. 20/2006 on the Regulation of Tenancy Relationships |
| KSA | Ejar platform (Ministry of Housing / REGA) | Saudi Real Estate Law; Ejar electronic lease mandatory for regulated premises |
| Lebanon | No mandatory national registry for private leases | Old Rent Law (pre-1992 tenants: heavily protected, near-irremovable) vs New Rent Law (post-1992: market-rate); Law No. 160/1992 defining the split |
| Egypt | No Ejari equivalent; notarization sometimes required | Egyptian Civil Code Arts. 558–642 (lease provisions) |
| DIFC | DIFC Leasing Office; DIFC Real Estate Law | Common law; English-language leases; service-charge reconciliation standard |
| UK (England & Wales) | Land Registry; EPC required | Landlord and Tenant Act 1954 (commercial); Housing Act 1988 (residential AST) |

### 3. Premises details

- Full address (street, building, unit number, floor).
- Area in square meters (m²) or square feet — used for rent-per-sqm analysis and for Ejari / Tawtheeq forms.
- Condition at handover: furnished / unfurnished / shell-and-core for commercial. Recommend attaching a handover inspection inventory as an annex (material for security deposit return disputes).
- Parking: spaces allocated, included in rent or separately charged?

### 4. Term

- Start date and end date (or duration in months/years).
- Renewal mechanism: automatic renewal unless notice given? Break clause? Option to renew with rent fixed or at market?
- Notice periods for termination — confirm statutory minimum where applicable (e.g., Dubai Law 26/2007: landlord must give 12 months' notice to recover premises for own use; KSA Ejar: notice governed by Ejar platform defaults).

### 5. Rent

- Annual rent (total) or monthly rent — state which.
- Currency: AED, SAR, USD, LBP, EGP. Flag LBP/USD duality risk for Lebanon leases (specify which USD clearly — "fresh dollars" vs Lebanese bank dollars remain a live issue).
- Payment frequency: monthly, quarterly, semi-annual, annual (Dubai: annual/semi-annual cheques remain common practice even post-digital-payment reforms).
- Number of post-dated cheques (Dubai/Abu Dhabi practice: often 1–4 cheques for the year).
- Rent-increase mechanism: CPI-linked? RERA calculator cap (Dubai: increases capped by Decree 43/2013 schedule relative to market average)? Free-market escalation?
- Service charge / maintenance charge: separate line or inclusive?

### 6. Security deposit

- Amount (Dubai custom: 5% of annual rent for residential; 10% for commercial — not statutory, but market standard).
- Conditions for return (deductions for damage beyond fair wear and tear; timeframe for return after vacation — Dubai: within 30 days standard).
- Held by: landlord directly or escrow agent?

### 7. Permitted use

The permitted use clause must precisely match the tenant's trade license category (commercial) or residential occupancy intent. A commercial tenant operating outside their licensed activity in the leased premises is in breach of both the lease and the trade license; landlords can seek forfeiture.

### 8. Side

Drafting for landlord or tenant changes clause emphasis materially:
- **Landlord perspective**: tighter dilapidations language, shorter cure periods, landlord's right to inspect, forfeiture triggers, subletting prohibition.
- **Tenant perspective**: longer cure periods, subletting/assignment rights, break clauses, fit-out rights and reinstatement carve-outs, landlord covenant to maintain structure.

## Optional inputs

- **Fit-out / alteration rights**: commercial / retail tenants often need to fit out premises; confirm what work is permitted and whether reinstatement at end of term is required.
- **Assignment and subletting**: is the tenant permitted to assign the lease or sublet? Any landlord consent requirements?
- **Force majeure / COVID-style clauses**: post-2020 commercial lease practice increasingly includes rent-suspension or abatement triggers for government-mandated closure.
- **Guarantor**: personal or corporate guarantee from a parent entity or director.

## Critical jurisdictional traps

- **Lebanon Old Rent Law**: never draft a Lebanon residential lease without confirming whether the premises fall under the pre-1992 rent regime. Old-rent tenants have statutory occupation rights that effectively make eviction impossible on economic grounds — this is a live issue for landlords seeking to redevelop.
- **Dubai RERA rent-increase cap**: the maximum permissible rent increase is set by the RERA rental index; increases above the permitted threshold are void and the tenant can seek recovery. Verify the current year's index percentage before agreeing any escalation clause.
- **Ejari / Ejar mandatory registration**: leases not registered in Dubai's Ejari or KSA's Ejar system may be unenforceable against third parties and will not be recognized in eviction proceedings. Registration is the client's (usually landlord's) responsibility.
- **KSA Ejar platform requirement**: since 2021, residential and commercial leases in KSA must be registered on the Ejar platform. Electronic issuance is mandatory; paper-only leases are non-compliant.

## Output

1. A structured intake summary confirming all eight fields and any outstanding items.
2. A routing instruction to [[draft-residential-lease]] or [[draft-commercial-lease]] with the completed intake data.
3. A flag if mandatory registration is required (jurisdiction-specific).

## Do not

- Draft the lease before confirming jurisdiction and lease type.
- Assume Dubai rules apply to all UAE leases — Abu Dhabi has a separate regime (Tawtheeq, separate rental increase rules).
- Omit the RERA calculator warning for Dubai leases — many landlords attempt increases that exceed the statutory cap.

## Related skills

- [[draft-residential-lease]]
- [[draft-commercial-lease]]
- [[kb-real-estate-mena]]
- [[heuristic-statute-of-limitations-flag]]
- [[conversation-intake-employment-contract]]
