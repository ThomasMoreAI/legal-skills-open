---
name: draft-residential-lease-sboghossian
title: Residential Lease (Tenancy Agreement)
description: Use when drafting a residential lease (tenancy agreement / rental contract) for a dwelling unit. Covers all core clauses, MENA-specific mandatory registration requirements (Dubai RERA/Ejari, Abu Dhabi Tawtheeq, KSA Ejar, LB old vs new rent law), rent-increase caps, eviction rules, and security-deposit conditions. Includes negotiation guidance for landlord vs tenant perspectives. Triggers on "lease", "residential lease", "tenancy agreement", "rental agreement", "إيجار سكني", or "bail d'habitation" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-residential-lease
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Residential Lease (Tenancy Agreement)

## When to use this

Use this skill when drafting a lease for residential use of a dwelling — apartment, villa, house, or floor. The lease is the binding contract between the landlord (Lessor / مؤجر / bailleur) and the tenant (Lessee / مستأجر / locataire).

Residential leases are among the most heavily consumer-regulated contracts in all jurisdictions covered here. Landlords cannot simply write whatever they want — statute overrides many private agreements in favor of tenant protection. This skill captures both the contractual provisions and the statutory constraints.

For commercial (non-residential) leases, a separate skill applies. For reviewing a lease from the landlord's or tenant's perspective, use [[review-lease-landlord-side]] or [[review-lease-tenant-side]].

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Landlord (name, ID / commercial registration) | Full identification | — must supply |
| Tenant (name, ID, dependents if relevant) | Full identification; visa status may be required for registration | — must supply |
| Property: address, area, condition, inventory | Precise description; baseline condition for deposit return | — must supply |
| Rent: amount, currency, payment frequency, payment method | Core economic term | — must supply; state whether VAT-inclusive (UAE) |
| Term: start date, duration, end date | Sets the tenancy | 1 year (standard); 3 years (LB default) |
| Security deposit: amount, conditions for return | Protects landlord; limited by statute in some jurisdictions | Typically 1-3 months' rent |
| Jurisdiction | Determines all statutory overrides | — must supply |

## Standard clauses

### 1. Parties and property description
Full identification of Landlord and Tenant. Property: exact address, building name, unit number, floor, area in sqm, and an annexed inventory (Schedule A listing all fixtures, fittings, and items included in the lease and their current condition).

### 2. Use restriction
The property is let for residential use only. No commercial activity, subletting to lodgers, or use for any purposes other than private residential occupation by the Tenant and their named immediate family members without Landlord's prior written consent.

### 3. Term and renewal
State the fixed term start and end dates clearly.

**Renewal provisions** vary dramatically by jurisdiction — see Jurisdictional notes. In many MENA and French systems, tenants have statutory renewal rights that the landlord cannot override by contract.

### 4. Rent

**Amount**: [Currency] [Amount] per [month / year], payable in advance / in arrears on [date] of each month.

**Payment method**: bank transfer to [account details] / certified check / electronic platform (e.g., Ejar in KSA)

**Late payment**: interest at [X]% per month on overdue rent (verify whether applicable law imposes a cap on late payment penalties for residential leases).

**Rent increase mechanism**: governed by statute in many jurisdictions — the parties cannot agree to unlimited rent increases:
- Dubai: RERA Rental Increase Calculator governs; no increase in the first year; formula-based caps thereafter
- Abu Dhabi: specific rent increase rules
- KSA: Ejar system; rate increases subject to contract terms and market regulation
- France: increase capped at IRL (Indice de Référence des Loyers, quarterly index)
- UK: no statutory cap for assured shorthold tenancies; must be agreed; section 13 notice procedure

**VAT**: in UAE, residential leases are VAT-exempt under Federal Tax Authority guidelines; commercial leases are subject to 5% VAT. State whether the rent is exclusive of VAT and whether any portion of the property (storage, parking) is commercial.

### 5. Security deposit

**Amount**: [1-3 months' rent] (statutory caps exist in some jurisdictions).

**Held by**: Landlord (most common) or an escrow/third-party account.

**Conditions for return**: the deposit is returned to the Tenant within [X] days of the end of the tenancy, less:
- Unpaid rent
- Costs of repairing damage beyond fair wear and tear (documented by comparison with the inventory)
- Any other amounts the Tenant is liable to pay under the lease

**Dispute resolution for deposit**: many jurisdictions have specific bodies (Dubai RDC, UK TDS, FR Commission Départementale de Conciliation) — reference the applicable body in the lease.

**Statutory protections**:
- UK: deposit must be held in a government-authorized Tenancy Deposit Scheme; landlord must provide Tenant with the "Prescribed Information" within 30 days or face penalties
- France: no specific statutory escrow requirement for private landlords; for managed properties, agences immobilières hold deposits per the loi Hoguet

### 6. Maintenance obligations

**Landlord's obligations** (structural and major):
- Maintain the structural integrity of the building and roof
- Maintain the exterior walls and communal areas
- Maintain the main mechanical, electrical, and plumbing (MEP) systems
- Emergency repairs (blocked drains, water leaks)

**Tenant's obligations** (interior and minor):
- Keep the property clean and in good order
- Minor repairs (replacing light bulbs, touching up paint for minor marks)
- Report any damage or defect promptly to the Landlord
- Not make alterations or improvements without Landlord's consent; reinstate on vacation

**Fixtures and appliances**: specify who is responsible for maintaining major appliances (HVAC, oven, washing machine) provided with the property. In UAE: HVAC maintenance is a common landlord/tenant dispute; specify clearly.

### 7. Utilities
State which utilities are the Tenant's direct responsibility:
- Electricity + water (DEWA in Dubai; ADDC / AADC in Abu Dhabi; Tariq in KSA; Électricité du Liban or EDL in Lebanon — notoriously unreliable)
- Internet / telecom
- District cooling (common in UAE) — specify whether included in rent or Tenant's direct responsibility
- Municipality fees / waste collection (Dubai: Municipality fee included in DEWA bill; specify if otherwise)

### 8. Insurance
- **Contents insurance**: Tenant's responsibility (Tenant's belongings, liability)
- **Building insurance**: Landlord's responsibility
- Specify whether the lease requires Tenant to hold a specified minimum liability coverage

### 9. Subletting and assignments
Subletting (re-letting to a third party) is prohibited without Landlord's prior written consent. This is standard across all jurisdictions; in some jurisdictions (France loi Élan), Tenant may not sublet at all without consent and the consent may not be unreasonably withheld.

Assignment of the lease (transferring the whole tenancy to a third party) is also prohibited without consent and typically requires the Landlord's approval of the new tenant.

### 10. Termination and notice periods

**End of fixed term**: in most jurisdictions, the lease does not automatically terminate at the end of the fixed term unless proper notice has been given. Many systems convert to a periodic tenancy or apply statutory renewal rights.

**Landlord's early termination rights**: strictly limited by statute in most residential lease jurisdictions. Common grounds:
- Non-payment of rent (after formal notice and cure period)
- Material breach of lease terms
- Owner's personal use (highly restricted in UAE and France — specific statutory procedures)
- Demolition or major renovation (specific statutory notice periods)

**Tenant's early termination rights**: typically requires [1-3] months' notice; in some cases, a penalty for breaking the fixed term early (UK: depends on break clause; UAE: mutual agreement or statutory provision).

### 11. Inventory checkout
At the end of the tenancy:
- Tenant vacates on or before the termination date
- Joint inventory inspection by Landlord and Tenant (or their representatives) on the last day or within [5] days thereafter
- Documented comparison of current condition vs the Schedule A inventory
- Agreed deductions from security deposit
- If Tenant disputes deductions: escalate to the applicable dispute body (RDC, TDS, etc.)

### 12. Dispute resolution
Reference the applicable rental dispute resolution body:
- **Dubai**: Rental Disputes Centre (RDC) under Dubai Courts; mandatory for landlord-tenant disputes
- **Abu Dhabi**: Abu Dhabi Judicial Department rental disputes
- **KSA**: Ejar-registered disputes; rental committees within the Ministry of Justice
- **France**: Commission Départementale de Conciliation (before litigation); Tribunal d'Instance for contested cases
- **UK**: county court; small claims track for deposit disputes (following TDS adjudication process)

### 13. Governing law
State the applicable law explicitly — not just implied by the property location.

## Jurisdictional notes — critical differences

### UAE — Dubai
- **RERA / Ejari registration**: mandatory; lease must be registered on the Ejari system; without registration, the lease is difficult to enforce and some government services (school enrollment, utility connection) cannot be arranged
- **Rental Disputes Centre (RDC)**: dedicated tribunal for landlord-tenant disputes; must be used before going to courts
- **Rent increase**: governed by the RERA Rental Increase Calculator (Decree 43/2013 as amended); increase is only permissible if the rental value is below the market benchmark; percentage capped per the calculator output
- **Eviction**: grounds for early eviction by Landlord are limited; at end of term, specific statutory notice required; owner-use eviction requires 12-month notice via Notary Public

### UAE — Abu Dhabi
- **Tawtheeq registration**: mandatory; leases must be registered with the Abu Dhabi Municipality's Tawtheeq system
- Rent dispute resolution through Abu Dhabi courts

### KSA
- **Ejar electronic platform**: mandatory registration; connects Ministry of Housing, landlords, tenants, and banks; enables rent payment via bank integration; lease without Ejar registration may be unenforceable
- Sharia courts have jurisdiction over residential tenancy disputes; civil-code style principles apply

### Lebanon (LB)
- **Critical distinction — old rent / new rent**:
  - **Old rent (pre-1992)**: leases entered before Law 160/1992; these tenants enjoy near-permanent occupancy rights; extremely difficult for landlords to recover; rent is fixed at historic (often negligible) levels; subject to occasional legislative reform
  - **New rent (post-1992 Law 160/1992)**: standard 3-year minimum term; tenant has renewal rights but not permanent occupation rights; rent increases governed by agreement and index
- Lebanon's real estate market has specific characteristics: dollar-denominated leases (even after the 2019 financial crisis); rent payment in cash USD became standard; specific risks around banking system

### France
- **Loi du 6 juillet 1989 (loi Mézard/Alur)**: the principal statute governing residential leases for primary residences; comprehensive tenant protections
- **3-year minimum term** for private landlords; 6-year minimum for corporate landlords; 1-year permitted for furnished rentals
- **Mandatory notice periods**: Landlord to recover: 6 months for primary residence; Tenant to vacate: 3 months (1 month in certain regulated zones)
- **Security deposit**: limited to 1 month's rent (unfurnished); 2 months (furnished)
- **Diagnostics**: mandatory energy performance certificate (DPE) and lead/asbestos reports must be provided to Tenant at signing; non-provision may give Tenant grounds to claim damages

## Landlord vs tenant negotiation points

| Issue | Landlord prefers | Tenant prefers |
|-------|-----------------|---------------|
| Security deposit | 3 months; non-refundable for early departure | 1 month; refundable with clear criteria |
| Rent escalation | Formula-based annual increase | No increase during fixed term |
| Maintenance allocation | Tenant bears all interior and appliance maintenance | Landlord bears all appliances and MEP |
| Early termination | High penalty; 3-month notice | Free to leave on 1-month notice |
| Renewal | Landlord's right not to renew at end of term | Statutory renewal rights |
| Pets | No pets without consent | Pets permitted subject to deposit |
| HVAC maintenance | Tenant's responsibility | Landlord's responsibility |

For side-aware review, use [[review-lease-tenant-side]] or [[review-lease-landlord-side]].

## Eviction notice templates
See [[draft-eviction-notice]] for jurisdiction-specific eviction and non-renewal notices.

## Common mistakes

- Not registering the lease (Ejari/Tawtheeq/Ejar) — unenforceable; utility connection denied
- Rent amount stated without specifying currency — creates disputes in multi-currency markets (UAE, LB)
- Missing inventory at the start of the tenancy — no baseline to assess deposit deductions on checkout
- Rent increase clause that ignores statutory caps — the clause is void and the statutory cap applies regardless
- UAE: attempting to evict for owner-use without the mandatory 12-month Notary Public notice — eviction proceeding dismissed

## Related skills

- [[draft-property-sale-agreement]]
- [[draft-eviction-notice]]
- [[review-lease-tenant-side]]
- [[review-lease-landlord-side]]
