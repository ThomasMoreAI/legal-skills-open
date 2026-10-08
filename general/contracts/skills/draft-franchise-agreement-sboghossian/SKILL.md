---
name: draft-franchise-agreement-sboghossian
title: Franchise Agreement
description: Use when drafting a franchise agreement granting a franchisee the right to operate a business under the franchisor's brand, systems, and standards in a defined territory. Covers the full clause structure (territory, fees, training, operations manual, brand use, renewal, termination, non-compete), MENA-specific considerations (commercial agency law traps, UAE Federal Franchise Law, KSA disclosure requirements, halal compliance), EU pre-contractual disclosure obligations, and common pitfalls including inadequate operations manual cross-references.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-franchise-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Franchise Agreement

## When to use this

A franchise agreement grants a franchisee the right to operate a business under the franchisor's brand name, systems, and operational standards in a defined territory. Unlike a distribution agreement (which is a buy-resell arrangement), a franchise involves:
- A license of the franchisor's brand and operational system.
- The franchisee operating in a branded manner that represents the franchisor to the public.
- Ongoing support, training, and quality control by the franchisor.
- Ongoing royalties paid to the franchisor.

Use this skill for:
- Single-unit franchise agreements (one location).
- Multi-unit development agreements (franchise for multiple locations in a territory).
- Master franchise agreements (franchisee has the right to sub-franchise in an entire country or region).

**The commercial agency trap in MENA:** a franchise agreement that gives the franchisee broad local exclusivity and makes them economically dependent on the franchisor risks being characterized as a protected commercial agency under UAE/KSA/Egypt commercial agency laws. Structure carefully — see Jurisdictional Notes.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Franchisor (full legal name + jurisdiction of IP ownership) | IP ownership must vest in the franchisor entity | — |
| Franchisee (full legal name + jurisdiction) | Local compliance obligations | — |
| Territory (exclusive or non-exclusive) | Defines franchisee's operating area | Non-exclusive by default |
| Franchise territory type (single unit / multi-unit / master) | Determines structure and sub-franchising rights | Single unit |
| Term (initial + renewal) | Commercial deal; renewal terms must be stated | 5 years + 5-year renewal |
| Franchise fee (initial) | One-time entry fee | — |
| Royalty rate (ongoing) | Ongoing percentage of gross revenue | 5–8% of gross sales |
| Marketing / advertising fund contribution | Separate from royalty; pooled for brand advertising | 1–2% of gross sales |
| Operations manual reference | The manual governs operational standards; must exist | Cross-reference by title |

## Optional inputs
- Area development agreement terms (for multi-unit)
- Sub-franchising rights and approval process (for master franchise)
- Technology and POS system requirements
- Supply chain restrictions (approved suppliers only)
- Real estate approval rights (franchisor approves site)

## Standard clause structure

### 1. Grant of franchise and territory
> "Subject to the terms of this Agreement, Franchisor hereby grants to Franchisee the [exclusive / non-exclusive] right and license to operate [one / X] [brand name] franchise location(s) within the Territory defined in Schedule A, during the Term."

Territory definition: for single-unit franchises, define by address or radius (e.g., 2 km radius from the premises). For master franchises, define by country or countries with sub-franchising rights.

Exclusivity carries the same MENA agency-law risks as in distribution agreements — see Jurisdictional Notes.

### 2. Franchise fees

**Initial franchise fee**
- One-time payment on signing; typically non-refundable.
- State amount; payment date; whether any portion is refundable (e.g., if premises cannot be secured).

**Ongoing royalties**
- Percentage of gross revenue (before VAT) payable [weekly / monthly].
- Definition of "gross revenue" is contested — be precise: include or exclude discounts, refunds, VAT, employee meals, catering orders, delivery partner fees.
- Payment mechanism: direct debit preferred; wire transfer alternative.

**Marketing / advertising fund contribution**
- Percentage of gross revenue paid into a pooled brand-advertising fund.
- Franchisor manages the fund; provides periodic reporting to franchisees on use.
- Franchisee's contribution does not guarantee local advertising spend.

**Technology and POS fees**
- Monthly license fee for franchisor's POS system, ordering platform, customer data system.
- Franchisee must use franchisor's approved technology; no alternative systems.

### 3. Training and support obligations (Franchisor)
- Initial training: [X] weeks at franchisor's training facility (and/or on-site); franchisor provides trainers; franchisee bears travel and accommodation.
- Opening support: [X] days of on-site support at launch.
- Ongoing training: access to franchisor's online training portal; annual training updates.
- Field support visits: [X] per year; unannounced inspections permitted under operations manual authority.
- Hotline / helpdesk access for operational support.

### 4. Operations standards (Franchisor controls)
- Franchisee must comply with the Operations Manual (the "Manual"), as amended from time to time.
- Manual governs: menu / product specification, service standards, store design and layout, hygiene and safety, staffing ratios, and customer-service procedures.
- Franchisor's right to update the Manual with reasonable notice.
- Franchisee's obligation to implement updates within [60 / 90] days of notification.

**Important:** the operations manual must exist and be provided to the franchisee at or before signing. A franchise agreement that cross-references a manual that doesn't exist yet is incomplete and creates disputes.

### 5. Brand and IP usage
- License to use Franchisor's trademarks, trade names, logos, and service marks solely in connection with the operation of the Franchised Business in the Territory.
- No sublicensing without written consent (except to sub-franchisees under a master franchise).
- Quality control right: Franchisor may inspect and require correction of non-compliant brand use.
- On termination: immediate cessation of all use; removal of signage; return of branded materials.
- No modification of marks; no use in domain names, social media handles, or email addresses without prior written approval.
- GCC trademark note: franchisee should not register the franchisor's marks in the Territory without authorization; any unauthorized registration creates a parallel-ownership problem.

### 6. Reporting and audit rights
- Weekly or monthly sales reporting (format specified).
- Annual audited financial statements (for master franchisees).
- Franchisor's right to audit franchisee's books and records with [X] days' notice; no limitation on frequency if non-compliance is suspected.
- Franchisee bears audit costs if shortfall in reported royalties exceeds [X]%.

### 7. Approved suppliers
Franchisee must source products/ingredients/materials from Franchisor's approved supplier list. Franchisor may add/remove suppliers with reasonable notice. Franchisee may propose new suppliers; approval process must be transparent.

Note: EU competition law (Vertical Agreements BER 2022/720) restricts exclusive sourcing obligations beyond what is genuinely necessary for quality control. For EU markets, the "approved supplier" mechanism must not amount to exclusive purchasing above the block-exemption thresholds.

### 8. Renewal
- Franchisee has the right to renew for [X] years by giving [X] months' written notice before expiry.
- Conditions: (a) franchisee is not in breach; (b) franchisee has met minimum performance standards; (c) franchisee signs the then-current form of franchise agreement (which may differ from this Agreement); (d) franchisee has paid a renewal fee of [amount].
- No automatic renewal; positive election required.

### 9. Termination
**Immediate termination (no cure):**
- Abandonment of the franchise.
- Unauthorized use of IP post-warning.
- Criminal conviction of franchisee or its principals.
- Insolvency.
- Material misrepresentation in the franchise disclosure document or application.

**Termination with cure period (typically 30 days):**
- Non-payment of royalties.
- Breach of the Operations Manual.
- Failure to meet minimum performance standards after written warning.

**Convenience termination:**
- Neither party should have an unqualified right of convenience termination. Franchise relationships require investment by both sides; build in a long notice period (6–12 months) if convenience termination is permitted at all after the initial term.

### 10. Non-compete post-termination
- Franchisee and its principals shall not operate a directly competing business in the Territory for [12–24] months post-termination.
- Scope: the same or closely similar business activity.
- Territory: the Territory plus a reasonable buffer zone.
- Enforceability varies widely by jurisdiction — see Jurisdictional Notes.

## Jurisdictional notes

### UAE — Franchise and Agency Law interface

UAE Federal Law 18/1981 on Commercial Agency can capture franchise relationships if the franchisee is exclusively promoting the franchisor's brand in a defined territory. The risk markers are: exclusivity + dependence + long-term relationship.

Mitigation: non-exclusive franchise territory where commercially feasible; explicit acknowledgment that relationship is not a commercial agency; franchisee operates independently on its own account (not for and on behalf of franchisor).

UAE also enacted Federal Law No. 9/2022 on commercial concession (franchise); this law requires pre-contractual disclosure and governs franchisee protections. Confirm the latest implementing regulations before finalizing a UAE franchise agreement.

### KSA — Commercial Agency Law

Same agency-law risk as UAE. Additionally:
- KSA Commercial Agencies Law may require registration.
- Halal compliance: specify whether the franchise's product/service has halal certification; include ongoing compliance obligation.
- MISA investment license may be required for foreign franchisors operating directly in KSA.

### France — Pre-contractual disclosure (DIP)
French Loi Doubin (Law of 31 December 1989, codified in Code de Commerce) requires franchisors to provide a **Document d'Information Précontractuelle (DIP)** at least **20 days before** the signing of the franchise agreement or any pre-contract payment. The DIP must include:
- 5 years' financial history of the franchisor.
- List of franchisees and their turnover.
- Number of franchisees who joined and left in the past year.
- Pending litigation.
- Description of the network and local market.

Failure to provide the DIP entitles the franchisee to rescind the agreement within 5 years.

### EU
- Block Exemption Regulation 2022/720 covers franchise agreements as vertical agreements.
- Exclusive territory grants, passive-sales restrictions, and RPM are the primary competition-law risks.
- Online sales restrictions have become harder to justify post-2022.

### US
- Federal Trade Commission (FTC) Franchise Rule requires pre-sale disclosure via a Franchise Disclosure Document (FDD); 14-day pre-contract disclosure period.
- Many states have additional franchise registration and disclosure requirements.

## Common mistakes

1. **Operations manual not delivered** — cross-referencing a manual that doesn't exist at signing leaves standards undefined and unenforceable.
2. **Royalty base not defined** — "gross revenue" without exclusion of VAT, refunds, and inter-company transactions leads to royalty disputes.
3. **No minimum performance standards** — franchisor has no right to terminate underperforming franchisees without MSPs; include annual minimum sales targets.
4. **Trademark registered by franchisee** — the franchise agreement should prohibit unauthorized trademark registration; include a provision requiring franchisee to cooperate in trademark recordal/deregistration.
5. **Pre-contractual disclosure missed** — in France (DIP), the US (FDD), and UAE (new franchise law), missing disclosure is a basis for rescission.
6. **Non-compete wider than necessary** — post-termination non-competes in EU and common-law jurisdictions must be reasonable in scope, time, and territory; excessive clauses are void.

## Related skills

- [[draft-distribution-agreement]] — reseller structure where no brand/system license is involved
- [[draft-distribution-agreement-mena-extension]] — MENA agency-law risk analysis applicable to both distribution and franchise
- [[draft-license-agreement]] — standalone brand or IP license without the full franchise structure
- [[kb-commercial-agency-mena]] — commercial agency law reference for UAE, KSA, Egypt, Lebanon
