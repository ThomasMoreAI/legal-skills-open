---
name: draft-sublease-sboghossian
title: Sublease Agreement
description: Use when drafting a sublease agreement where an original tenant (Sublessor) sub-lets all or part of a premises to a Sublessee. Covers head-landlord consent requirements, sub-term limits, rent mechanics, use restrictions, head-lease compliance obligations, and the risk that a sublease without consent can terminate the head lease. Provides MENA-specific rules for Ejari (Dubai RERA) and Ejar (KSA) registration, and Lebanon's restrictive old-rent-law context.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-sublease
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Sublease Agreement

A sublease is a new tenancy granted by an existing tenant (the Sublessor) to a third party (the Sublessee) over all or part of the same premises, for a term not exceeding the remaining term of the head lease. The Sublessor retains its obligations to the head landlord and takes on new obligations to the Sublessee. The most critical step — often overlooked — is obtaining the head landlord's prior written consent.

## When to use this

- An existing tenant has excess space and wants to monetize it
- A company is downsizing and wants to offset rent during the remaining lease term
- A company's operations are relocating before the head lease expires
- A startup or small business wants to take a short flexible term in a larger tenant's space
- Back-to-back sublet to an affiliate entity as part of a group restructuring

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Sublessor (original tenant under head lease) | Must have legal authority to sublet; must be identified as the existing tenant | Must provide |
| Sublessee | Incoming tenant | Must provide |
| Premises description | Precise — full unit or partial (specific floor, area m²); must match or be a defined subset of the head-lease premises | Must provide |
| Sub-term | Duration; must end on or before the head lease expiry date | Must provide; build in a buffer before head-lease end |
| Sub-rent | Amount; often at or below market if related party; at market or above if monetizing | Must provide |
| Head landlord consent | Whether consent has been obtained or is a condition of the sublease | Always required; make sublease conditional on consent |

## Optional inputs

- Head landlord consent letter attached as a schedule
- Fit-out provisions (responsibility for tenant works in the sub-premises)
- Sub-deposit (security deposit held by Sublessor; calibrate to sub-rent period)
- Break clause aligned with head-lease break (prevents Sublessor being caught with a sublease when it wants to break)

## Critical: Head Landlord Consent

Most commercial leases prohibit sub-letting without the prior written consent of the landlord. The consequences of subletting without consent are severe:
- The head lease may contain an absolute prohibition on subletting; breach of this covenant entitles the head landlord to terminate the head lease (forfeiture in English-law systems; résiliation in civil-law)
- Even where consent is a "qualified" obligation (landlord cannot unreasonably withhold), the tenant cannot sublet until consent is given
- The Sublessee's occupation without consent may be unenforceable — the Sublessee cannot demand the Sublessor protect its possession if the head lease is terminated for breach

**Always make the sublease conditional on receipt of the head landlord's written consent, and attach the consent letter as Schedule 1 once obtained.**

Consent letter should include:
- Head landlord's acknowledgment of the Sublessor's right to sublet to the named Sublessee
- Any conditions imposed (use restrictions, Sublessee creditworthiness, direct obligation to landlord on default by Sublessor)
- Confirmation that the head lease is not in breach at the date of consent

## Document Structure

### 1. Recitals
- Reference to the head lease (full description: parties, date, premises)
- Statement that the head landlord has consented (or: "subject to the condition that head landlord consent is obtained by [date]")
- Brief background to the sublease arrangement

### 2. Sub-premises
Describe precisely:
- If the entire premises: "the Premises as defined in the Head Lease"
- If partial: "that part of the Premises comprising approximately [X] sq m on [floor/location], as shown hatched in red on the plan attached as Schedule 2"
- Shared areas (reception, common areas, bathrooms): specify access rights and any allocation of operating costs

### 3. Term
- Start date (must be on or after Sublessor's possession date under head lease)
- End date (must be before or on the head lease termination date — add a buffer of at least one month to allow for handback without overlap)
- If the head lease has a break option that Sublessor intends to exercise, the sublease should contain a corresponding break clause (otherwise, Sublessor is trapped between head-lease termination and sublease obligations)

### 4. Sub-rent
- Amount (per month / per year, stated in figures and words)
- Currency
- Payment mechanism (bank transfer; standing order)
- Payment date (e.g., first business day of each month)
- Late payment interest
- Review mechanism (if the sub-term is longer than one year): CPI, fixed percentage, or linked to head-lease rent review

### 5. Use Clause
The Sublessee's permitted use must be equal to or narrower than the permitted use in the head lease. If the head lease permits "office use," the sublease may permit "office use for [specific purpose]" but not a use that would breach the head lease (e.g., retail, food service, workshop).

### 6. Sublessee Obligations Under Head Lease
The Sublessee must be bound to comply with all Sublessor's obligations under the head lease insofar as they relate to the sub-premises. Key obligations to pass through:
- Maintaining the sub-premises in good repair
- Not making alterations without consent
- Complying with building regulations and applicable law
- Not causing nuisance or disturbance
- Allowing the head landlord access on the same terms as in the head lease
Include a direct statement: "The Sublessee shall not do or omit to do any act or thing in respect of the Sub-premises that would constitute a breach of the Head Lease."

### 7. Insurance
- Specify who insures the sub-premises (typically Sublessor maintains the policy it held under the head lease; Sublessee takes out contents and liability cover)
- Waiver of subrogation between Sublessor and Sublessee

### 8. Default and Remedies
- Events of default by Sublessee: non-payment for [5–10] business days; breach of material obligation not cured within [20] days of notice
- Sublessor's remedies: terminate the sublease, re-enter the sub-premises, claim arrears
- Note: in common-law systems, forfeiture must follow the prescribed process (serve section 146 notice in UK; equivalent in DIFC); in civil-law, judicial termination may be required

### 9. End of Sub-Term and Return of Premises
- Sublessee vacates on the last day of the sub-term
- Condition: sub-premises returned in the condition they were delivered (subject to fair wear and tear)
- Handback procedure: inspection with both parties present; schedule of condition vs current state; deposit return within [X] days less any deductions

### 10. Governing Law
Same as the head lease in most cases; consistency avoids conflict between the two instruments.

## Jurisdictional Notes

### UAE — Dubai (RERA / Ejari)
- Subletting without head landlord consent is prohibited under Dubai Law 26/2007 (as amended by Law 33/2008)
- The sublease must be registered with RERA's Ejari system; an unregistered sublease is not effective against third parties
- The head landlord's NOC (No Objection Certificate) must be obtained before Ejari registration; Ejari requires the NOC as part of the registration package
- If the head-lease Ejari registration is not current, the sublease cannot be registered

### KSA — Ejar
- Subletting requires head landlord consent; the sublease arrangement must be reflected in the Ejar registration system
- Ejar is the Ministry of Housing platform for registering residential and commercial leases in KSA; registration is mandatory
- Without Ejar registration, the sublease is valid between parties but cannot be enforced against third parties and will not be recognized by courts

### Lebanon — Old Rent Law
- Commercial and residential properties subject to the Lebanese old rent law (pre-1992 leases and regulated leases) have strong tenant protections but very restricted subletting rights
- Subletting under an old-rent-law lease typically requires explicit contractual permission; without it, the head landlord has grounds for termination
- New-regime leases (post-1992) are governed by the 2001 Law on Rental of Real Property; subletting restrictions depend on the lease terms

### UK — Landlord and Tenant Act 1954
- Commercial leases in England and Wales may have statutory protection under the Landlord and Tenant Act 1954; sublease must be structured consistently with the head lease's protected status (or contracted-out status)
- Landlord's consent: in qualified covenants, landlord cannot unreasonably withhold consent but may impose reasonable conditions
- Direct covenant: head landlord may insist that the Sublessee enters into a direct covenant with the head landlord to comply with head-lease terms (creating direct privity)

## Common Mistakes

- **Sublease term longer than head lease** — if the head lease expires before the sublease term, the sublease ends automatically; this leaves the Sublessee without possession and with a damages claim; always check the head-lease expiry date and align sub-term accordingly
- **No break clause aligned with head-lease break** — if the Sublessor has a break right in the head lease and exercises it, the sublease is terminated by operation of law; but the Sublessor may have damages liability to the Sublessee; include a corresponding break clause
- **Sub-rent exceeding head-rent without justification** — in some MENA jurisdictions, subletting at a profit above the head rent without the landlord's consent is a breach of the head lease even if subletting in principle is permitted
- **Use clause not checked against head lease** — Sublessee's actual business not permitted under the head-lease use clause; landlord can terminate
- **No consent = no sublease** — if the parties proceed to occupy without consent and the head lease is terminated, the Sublessee's claim is against the Sublessor (breach of quiet enjoyment and covenant) but the Sublessee has no right to remain on the premises

## Related skills

- [[draft-lease-agreement]]
- [[draft-assignment-of-lease]]
- [[review-lease-tenant-side]]
