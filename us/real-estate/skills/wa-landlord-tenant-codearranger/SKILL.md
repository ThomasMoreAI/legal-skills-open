---
name: wa-landlord-tenant-codearranger
title: Washington Landlord-Tenant — Subject-Matter Bundle
description: 'Use when handling a Washington landlord-tenant matter — residential evictions, unlawful-detainer summary proceedings, mobile-home L&T, security-deposit recovery, warranty of habitability, retaliation, ERP referrals, and tenant Right to Counsel for eviction defense. Substantive framework: RCW 59.18 (RLTA), RCW 59.20 (mobile homes), RCW 59.12 (summary proceedings). Covers 2021 just-cause-eviction reform (SB 5160), 2019 pay-or-vacate reform (SB 5600), and statewide tenant Right to Counsel (HB 1815). Triggers include "Washington eviction", "tenant rights", "RCW 59.18", "unlawful detainer", "security deposit", "warranty of habitability", "just cause eviction", "right to counsel".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-landlord-tenant
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Washington Landlord-Tenant — Subject-Matter Bundle

> **NOT LEGAL ADVICE.** RLTA was extensively rewritten by
> SB 5600 (2019) and SB 5160 (2021), and there have been
> further amendments through 2024. This skill names the
> controlling chapters and describes the procedural
> framework; **current notice periods, deposit-return
> windows, damages caps, and section subsections live in
> the references corpus** at `wa-law-references/
> references/wa-rcw-debt/`. Pre-2021 precedent on no-cause
> 20-day terminations and the historic 3-day pay-or-vacate
> notice is NO LONGER ACCURATE for residential tenancies.

## At a glance

- **Substantive code**: **RCW 59.18 (Residential L&T Act,
  RLTA)** — comprehensively rewritten by SB 5160 (2021)
  for just-cause eviction; pay-or-vacate notice reformed
  by SB 5600 (2019)
- **Mobile homes**: RCW 59.20 (manufactured / mobile-home
  L&T)
- **Summary-proceedings procedure**: RCW 59.12 (forcible
  entry / detainer / unlawful detainer)
- **Right to Counsel**: HB 1815 (2021) made WA the first
  state to fund tenant counsel statewide for evictions

## Chapter pointers

| Topic | Chapter | Reference file |
|---|---|---|
| Residential L&T (RLTA) | RCW 59.18 | `RCW-59_18.md` |
| Unlawful-detainer procedure | RCW 59.12 | `RCW-59_12.md` |
| Mobile-home L&T | RCW 59.20 | `RCW-59_20.md` |

For notice periods, the just-cause grounds enumeration,
security-deposit-return window, repair-and-deduct cap,
retaliation presumption period, and writ-of-restitution
timing, **read the relevant chapter file**. Don't rely on
memory — these were materially changed in 2019 and 2021.

## Just-cause eviction — procedural framework

SB 5160 (2021) created statewide just-cause eviction at
RCW 59.18.650. A landlord may not terminate a periodic
tenancy or refuse to renew a fixed-term lease at
expiration without one of the enumerated grounds. The
grounds fall into categories:

- **Tenant-conduct grounds** — nonpayment, lease
  violation, waste / nuisance / criminal activity
- **Owner-side grounds** — owner move-in, sale to occupier
  buyer, substantial rehabilitation / demolition, change
  of use
- **Narrow-circumstance grounds** — additional categories
  listed in the statute

Each ground has its own notice form and notice period.
Some require relocation assistance or first-right-of-
refusal protections.

For the enumerated grounds, notice periods, and
displacement protections, see `RCW-59_18.md` (especially
the .650 section group). Pre-2021 "no-cause" 20-day
terminations are gone for covered tenancies.

### Coverage carve-outs

The just-cause requirement has narrow exemptions —
shared-housing with landlord, certain small-landlord
single-family rentals, some seasonal/transitional
housing. See `RCW-59_18.md` for the exception list.

## Notices — procedural framework

Washington uses several distinct notice types for
residential L&T terminations:

- **Pay-or-vacate** — for nonpayment; statutorily
  mandatory form (the form itself includes legal-aid
  contact info)
- **Comply-or-vacate** — for curable lease violations
- **No-cure / immediate** — for waste / nuisance /
  criminal activity
- **Just-cause termination** — for the owner-side and
  narrow-circumstance grounds

Each has its own notice period set by statute. See
`RCW-59_18.md` (for residential) and `RCW-59_20.md` (for
mobile home parks).

## Unlawful-detainer procedure — procedural framework

The WA eviction summary proceeding follows a fixed shape:

1. Landlord serves the appropriate notice
2. **Eviction Resolution Program (ERP) referral** in
   counties that require it — mandatory pre-filing
   mediation / rental-assistance matching
3. If ERP unsuccessful or not required, landlord files
   unlawful-detainer complaint + the abbreviated UD
   summons (NOT the standard CR 4 summons)
4. Tenant has a short window to respond (much shorter
   than the standard CR 12 answer)
5. Show-cause hearing — tenant raises affirmative
   defenses; court determines whether to issue writ of
   restitution immediately OR set the matter for trial
6. Writ of restitution → sheriff service → physical
   lockout

The exact response window, show-cause hearing window, and
post-writ vacate period are statutory. See `RCW-59_18.md`
and `RCW-59_12.md`.

## Right to Counsel

HB 1815 (2021) created statewide funded tenant counsel for
eviction defense. Key features:

- Income-eligibility threshold (set by the Office of
  Civil Legal Aid)
- Tenant must affirmatively request counsel
- Counsel appointed by the Office of Civil Legal Aid

Post-2021 measurement shows a strong majority of WA
eviction respondents appear with counsel, which has
materially changed the landscape — landlords now face
represented tenants raising the full RLTA defense
playbook.

## Security deposits — procedural framework

- Move-in checklist required at start of tenancy
- Landlord must return deposit + itemized statement
  within a statutory window after tenancy ends
- Failure to return + itemize timely creates a statutory
  damages remedy

For the move-in-checklist requirement, the return window,
itemization rules, and damages multiplier, see
`RCW-59_18.md`.

## Warranty of habitability + repair-and-deduct

Landlord must maintain premises fit for human habitation
(structural; common areas; reasonable security; heat /
hot water / electricity; building-code compliance).
Tenant remedies for breach include notice + reasonable
time to repair, then repair-and-deduct, diminution-of-rent
action, rent into court registry, or rescission. For the
notice rules, the repair-and-deduct cap, and the
remedy-procedure mechanics, see `RCW-59_18.md`.

## Retaliation

Landlord may not terminate / raise rent / decrease
services in retaliation for tenant's complaint to
landlord or government about habitability, demand for
repairs, tenant union activity, or filing an enforcement
action. A statutory presumption of retaliation operates
within a fixed window after protected activity. For the
presumption window and the retaliation defenses, see
`RCW-59_18.md`.

## Mobile-home L&T — procedural framework

A distinct rule set under RCW 59.20 governs landlord-
tenant relationships in mobile-home parks: limited
statutory grounds for termination; park-rule-change
notice and reasonableness; first-right-of-refusal on park
sale; relocation-assistance regime. See `RCW-59_20.md`.

## Composition with other wa- skills

- `wa-statewide-format` — caption + GR 14
- `wa-discovery` — discovery in eviction trials
- `wa-pro-se` — pro-se eviction defense
- `wa-first-30-days` — answer + affirmative defenses
- `wa-kcdc` / `wa-kcsc` / `wa-county-courts` — venue
  specifics
