---
name: draft-eviction-notice-sboghossian
title: Eviction Notice / Notice to Vacate
description: 'Use when drafting an eviction notice or notice to vacate. Jurisdiction-sensitive: UAE-Dubai (12-month notice via notary/registered post under Decree 26/2013), UAE-Abu Dhabi (12-month, Tawtheeq), KSA (Ejar-registered leases), Lebanon (strong tenant protection under Old Rent Law; standard 3-year terms under New Rent Law), France (6-month residential unfurnished), UK (Section 21 / Section 8). Covers grounds, cure periods, service formalities, and the self-help prohibition applicable in all jurisdictions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-eviction-notice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Eviction Notice / Notice to Vacate

## When to use this

An eviction notice (notice to vacate) is the formal written notice from a landlord to a tenant demanding that the tenant vacate a property. It is:
- A legal prerequisite to commencing eviction proceedings in most jurisdictions.
- A record that the landlord complied with the required notice period.
- The starting point for calculating the date the tenant must vacate.

The notice **must comply with applicable law** in the jurisdiction where the property is located. The most common reasons eviction proceedings fail are: wrong notice period, wrong service method, or wrong grounds. Confirm all three before serving.

Use this skill for both residential and commercial property evictions, with the understanding that commercial and residential regimes differ significantly in most jurisdictions.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Landlord (full name / entity name) | Must be the registered owner or authorized agent | — |
| Tenant (full name / entity name) | Exact legal name as in the lease | — |
| Property (address, floor, reference number) | Precise identification matches lease; essential for court filing | — |
| Grounds for eviction | Determines the applicable notice period and statutory route | — |
| Lease details (start date, expiry date, rent amount) | Required for the notice and for any subsequent court application | — |
| Applicable notice period | Jurisdiction + grounds specific | — |
| Cure period (if applicable) | Many jurisdictions require a cure opportunity for breach | — |
| Service method | Jurisdiction-specific; wrong method invalidates | — |

## Jurisdictional notice periods and rules

### UAE — Dubai (Law No. 26/2007 as amended by Decree 26/2013)

The Dubai eviction regime is one of the most landlord-protective in MENA for end-of-term scenarios, but has strict procedural requirements:

| Ground | Notice period | Service requirement |
|---|---|---|
| Non-renewal at end of term (owner occupation) | **12 months** prior to lease expiry | Via Dubai Notary Public or registered post with acknowledgment |
| Non-renewal (renovation/demolition) | 12 months | Same |
| Non-payment of rent | 30 days (notice to pay or vacate) | Notary Public or registered post |
| Breach of lease conditions | 30 days cure notice | Notary Public or registered post |

Key rules:
- The 12-month notice for non-renewal **must be served before the lease expiry date** — service after expiry is invalid.
- If the 12-month notice is not served, the tenancy automatically renews on the same terms.
- Eviction proceedings for non-compliance with the notice go before the **Dubai Rental Dispute Settlement Committee (RDSC)**, not the regular courts.
- Dubai Law 26/2013 Art. 25 limits the grounds for eviction; ensure the ground used is one recognized by the law.
- RERA rent calculator governs rent increase limits (not covered here but relevant context).

### UAE — Abu Dhabi

- Similar 12-month notice requirement for non-renewal at term end.
- **Tawtheeq** (Abu Dhabi Tenancy System) registration of the lease is mandatory; eviction proceedings require a Tawtheeq-registered lease.
- Notice served via Abu Dhabi Notary Public or registered post.
- Disputes before the **Abu Dhabi Rental Disputes Committee**.

### KSA — Ejar platform

- KSA lease evictions are governed by the Saudi Lease Law and the **Ejar** platform (mandatory for registered leases).
- Residential: 3-month notice for non-renewal at lease end.
- Commercial: 6-month notice (conventional; confirm in the lease terms).
- Non-payment: demand notice → 15 days to pay → eviction filing with Ejar / courts.
- Legal notice must be served via notary or official channel to trigger formal proceedings.

### Lebanon — dual regime

Lebanon has two overlapping lease regimes:

**Old Rent Law (Law of 2001 transition for pre-1992 leases)**
- Properties under the Old Rent regime: extremely strong tenant protection; rent is capped at very low levels (indexed from pre-civil-war levels); eviction is practically impossible except for very limited grounds (owner personal occupation, structural demolition, serious breach).
- Tenants can pass rights to heirs. Landlords must seek court orders; eviction through administrative channels is blocked.

**New Rent Law (Law No. 160/1992, current framework for post-1992 leases)**
- Standard 3-year lease with renewal rights.
- Landlord may evict at end of term with sufficient notice (typically 3 months written notice for residential; longer for commercial).
- Eviction for non-payment: demand for payment → 15-day cure → court application.

**General:** Lebanese courts interpret in favor of tenants; obtaining an eviction order for non-payment typically takes 12–24 months in practice.

### France (residential)

- **Unfurnished residential**: landlord must give **6 months' notice** prior to lease expiry, by registered letter or bailiff (huissier) service, for non-renewal (own occupation, sale, or serious breach).
- **Furnished residential**: 3-month notice period.
- **Non-payment**: mise en demeure → 2-month cure period → court order through commissioner for protection against illegal eviction.
- **Repossession moratorium (trêve hivernale)**: evictions are suspended between 1 November and 31 March (winter truce); court orders obtained during this period are not executable until after 31 March.

### UK (England and Wales)

| Ground | Notice | Form | Notes |
|---|---|---|---|
| **Section 21** (no-fault; assured shorthold tenancy) | **2 months'** written notice | Form 6A | Cannot be used in first 4 months; cannot be used if landlord has not complied with prescribed information / deposit protection requirements |
| **Section 8** (fault-based; specific statutory grounds) | 2 weeks to 2 months depending on ground | Form 3 | Ground 8 (rent arrears): 2 months' arrears; court proceedings if tenant does not vacate |

Post-Renters Reform Bill changes are in progress as of 2024-2025; Section 21 may be abolished — verify current law at drafting.

## Notice structure

### 1. Notice header
Date. Landlord's name and address. Tenant's name and address. Property address and lease reference.

### 2. Service of notice
Mark the method: "This notice is served by [UAE Notary Public / registered post with acknowledgment / bailiff / personal delivery]."

### 3. Reference to lease
"This notice is given in relation to the lease agreement dated [date] between [Landlord] and [Tenant] for the premises at [address] (the 'Lease')."

### 4. Grounds for notice
State the specific ground(s) clearly:
- "The Landlord does not wish to renew the Lease upon its expiry on [date] due to the Landlord's requirement of the premises for personal/family occupation." (UAE)
- "The Tenant has failed to pay rent due under the Lease in the amount of [currency + amount] for the period [from] to [to] in breach of Clause [X] of the Lease." (breach-based)

### 5. Cure period (if applicable)
"You are hereby required to pay the outstanding rent of [amount] within [30] days of service of this notice. If payment is not received within this period, the Landlord will commence eviction proceedings without further notice."

### 6. Vacating date
"You are hereby required to vacate and deliver up possession of the Premises by [specific date — not less than the applicable statutory minimum notice period]."

### 7. Consequences of non-compliance
"If you fail to vacate the Premises by the required date, the Landlord will apply to the [competent court / RDSC / Committee] for an eviction order and may seek recovery of all costs incurred, including legal fees."

### 8. Reservation of rights
"This notice is without prejudice to any and all rights of the Landlord, including the right to recover outstanding rent, damages, and costs."

### 9. Signature and service record
Landlord's signature, date, name. Record the method of service and date of service.

## Critical service rules

| Jurisdiction | Required service method | Effect of wrong method |
|---|---|---|
| UAE (Dubai) | Notary Public or registered post with acknowledgment | Notice is void; 12-month period does not start running |
| UAE (Abu Dhabi) | Notary Public or registered post | Same |
| KSA | Notary or official Ejar platform notice | Notice is void |
| Lebanon | Registered post (at minimum); bailiff for critical notices | Statute of limitations may not begin |
| France | Registered letter (LRAR) or bailiff (huissier) | Notice invalid; tenant cannot be required to leave |
| UK Section 21 | Any written form; but first-tier tribunal must confirm compliance | If prescribed information not provided, Section 21 is invalid |

## Common mistakes

1. **Notice period miscalculation** — the most frequent reason landlords lose; calculate from the date of service (not the date of preparation) and add at minimum the statutory period.
2. **Service method non-compliance** — sending by WhatsApp or email when a notarized notice is required; the notice period does not start running.
3. **Missing ground or wrong ground** — in UAE, eviction grounds are limited by Decree 26/2013 Art. 25; a ground not in that list (e.g., wanting to sell to a third party rather than occupy) is invalid.
4. **Pre-cure application** — filing court proceedings before the cure period has expired renders the application premature; courts dismiss or adjourn.
5. **Self-help eviction** — changing locks, cutting utilities, removing tenant's belongings: **illegal in every jurisdiction covered** and exposes the landlord to criminal and civil liability. Always use formal court process.
6. **Notice after lease expiry** — in Dubai, the 12-month non-renewal notice must be served before expiry; serving it after the lease has expired converts the lease to a renewed tenancy.

## Related skills

- [[draft-lease-agreement]] — the underlying lease the notice is terminating
- [[draft-demand-letter]] — for combined rent-demand and eviction notices
- [[review-lease]] — reviewing the lease before drafting the notice to confirm grounds and notice requirements
- [[kb-real-estate-mena]] — real estate law reference pack for UAE, KSA, and LB
