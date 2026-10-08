---
name: review-lease-tenant-side-sboghossian
title: Lease Review — Tenant Side
description: Use when reviewing a commercial or residential lease from the tenant's perspective. Identifies risks and missing protections across rent escalation caps, service charge transparency, quiet enjoyment, repair allocation, make-good obligations, renewal rights, and personal guarantees. Covers MENA jurisdictions (Lebanon, UAE, KSA) and general commercial-lease best practice, with statutory tenant protections that vary by jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-lease-tenant-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Lease Review — Tenant Side

## When to use this

Use when a tenant (or a lawyer acting for a tenant) needs a protective review of a lease draft. The tenant's primary concerns are: cost certainty over the lease term, protection from arbitrary landlord action, operational flexibility, and exit rights. This skill flags where a draft lease is insufficiently protective and recommends pushback positions.

For the mirror landlord-side review, use [[review-lease-landlord-side]].

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Lease draft | The full document including schedules | Required |
| Jurisdiction | Statutory tenant protections vary substantially | Required — ask if unclear |
| Property type | Commercial / office / retail / warehouse / residential | Infer from draft |
| Intended use | Confirms whether permitted use clause is wide enough | Ask if not obvious |
| Lease term | Affects which protections matter most (short vs long-term) | From draft |
| Personal guarantee request | Whether the landlord is asking for a director/individual guarantee | From draft; flag if absent in context |

## Review Methodology

### Pass 1 — Rent and Escalation (Cost Certainty)

**What the tenant needs**:
- Escalation tied to an objective index — CPI, HICP, or a published government index — not landlord's determination
- A cap on annual escalation (e.g., no more than 5% per year regardless of CPI movements)
- No rent review clause that allows market resets without a floor protection

**Statutory caps to know**:
- **Dubai**: RERA Rental Increase Calculator caps annual increases; even if the lease permits higher increases, the RERA ceiling applies. Verify current RERA cap percentages — they vary based on current rent vs market rent relationship
- **Abu Dhabi**: Abu Dhabi Municipality rent cap regime (separate from Dubai)
- **KSA**: No statutory rent cap for commercial leases; purely contractual — ensure escalation is defined and capped
- **Lebanon**: New commercial leases (post-1992) are freely negotiated; however, given currency instability, USD vs LBP denomination is critical. Recommend: rent denominated in USD with a floor and an explicit Banque du Liban regulation acknowledgment; include a force majeure provision addressing banking restrictions
- **UK**: Most commercial leases have upward-only rent reviews — tenant should push for upward-downward or CPI-linked

**Red flags**:
- "Rent shall be reviewed annually at the landlord's discretion" — no objective standard
- Escalation compounding without a cap
- Market review upward-only ratchet with no downward correction on falling markets

### Pass 2 — Service Charge Transparency

Service charges can be a major hidden cost. Tenant needs:

- **Actual cost basis**: service charge reflects actual costs incurred; no profit element for landlord
- **Year-over-year cap**: increases in the service charge budget capped at a percentage (e.g., CPI + 2%), except in extraordinary circumstances
- **Audit right**: tenant can audit the service charge accounts within 12 months of receipt of the reconciliation statement; any overcharge refunded with interest
- **Exclusion of capex**: major capital works (roof replacement, structural repairs) should not be included in the service charge unless over a defined threshold and with tenant's advance notice and consent
- **Sinking fund**: if a sinking fund exists, tenant should understand the contribution basis and how accumulated funds are held

Flag: service charge provisions with no audit right; no exclusion of capex; no YoY cap on increase; management fee exceeding 15%.

### Pass 3 — Quiet Enjoyment

A quiet enjoyment covenant is a landlord's positive obligation that the tenant shall have peaceful and undisturbed possession of the premises for the duration of the lease.

This covenant must be:
- Express (not just implied) — in many civil-law jurisdictions it must be written
- Not subject to conditions that effectively undermine it (e.g., "quiet enjoyment subject to payment of rent" is circular)
- Covering both the landlord and anyone claiming through the landlord (including mortgagees who might take possession)

**MENA context**: In UAE and KSA, landlord interference with the tenant's possession (e.g., padlocking premises for rent arrears without a court order) is generally not permitted under civil codes and real estate regulations; the quiet enjoyment covenant codifies this right contractually.

### Pass 4 — Repair and Maintenance Allocation

**Tenant's target position** (commercial):
- Structural repairs, exterior walls, roof, building envelope: landlord's obligation
- Common parts, building services (lifts, HVAC serving the whole building): landlord via service charge
- Internal non-structural items, tenant's own fit-out, glazing within demise: tenant
- HVAC serving only tenant's demise: negotiate; can be shared obligation with maintenance records

Flag: any clause that assigns structural or exterior repairs to the tenant — unusual in commercial leases and should be resisted. If forced to accept, negotiate a substantial rent reduction to reflect the additional obligation.

**Fair wear and tear**: ensure repair obligations exclude fair wear and tear — this is standard in residential leases and should be negotiated in commercial leases; prevents tenant being liable for normal aging of the premises.

### Pass 5 — Make-Good / Reinstatement

The make-good obligation requires the tenant to restore the premises to a defined condition at the end of the lease. This can be expensive.

**Tenant protections needed**:
- **Schedule of condition**: a photographic and written record of the premises at lease commencement, annexed to the lease. Tenant's obligation is to return to the condition shown in the schedule, not to a better condition
- **Fair wear and tear exclusion**: tenant is not responsible for deterioration from normal use
- **Make-good cap**: if tenant has invested in fit-out, negotiate a cap on make-good liability (e.g., not to exceed the original fit-out cost; or a fixed monetary cap)
- **Landlord's option not to require reinstatement**: many landlords prefer to retain quality fit-out; include a mechanism for landlord to elect to keep the fit-out at the end of the term in lieu of reinstatement

Flag: blanket reinstatement obligations to "original delivery condition" without a schedule of condition — creates unlimited liability for the tenant.

### Pass 6 — Termination Rights and Break Options

A tenant's termination rights matter most in long leases:

- **Tenant break option**: unilateral tenant right to terminate on notice (typically 6–12 months) at specified dates. Should have minimal conditions — at most: no arrears of rent at the break date; premises returned in reinstatement condition (avoid requiring "full compliance" with all covenants — this standard is nearly impossible to achieve in practice)
- **Termination for landlord breach**: tenant should have the right to terminate if the landlord commits a material breach and fails to remedy it within 30–60 days of written notice
- **Force majeure**: consider whether force majeure relief from rent obligations is appropriate — useful for events that make the premises unfit for use (fire, flood, natural disaster, government closure orders)

**Jurisdictional note**: UK Landlord and Tenant Act 1954 gives commercial tenants security of tenure — right to renew at the end of the term unless the landlord successfully objects on specific statutory grounds. If tenant wants this protection, ensure the lease is not contracted out of the Act. If the landlord insists on contracting out, tenant should seek compensation.

**LB / FR**: Commercial tenants have a droit au bail (right to the lease), including compensation on non-renewal — pas de porte / indemnité d'éviction. These rights are statutory and cannot be waived contractually.

### Pass 7 — Insurance

**Allocation**:
- **Building insurance**: landlord's obligation; tenant should check that the cover includes loss of rent and full rebuilding value; tenant has an interest in ensuring the building is fully insured (otherwise an uninsured loss could result in no replacement premises)
- **Contents and tenant's own property**: tenant's obligation
- **Cross-waiver of subrogation**: both parties' insurers should waive their subrogation rights against the other party — prevents landlord's insurer suing tenant for a claim landlord's own insurance covered

### Pass 8 — Renewal Options

**Tenant's target**:
- Option to renew for one or more further terms at the tenant's election
- Renewal rent: either at market rent (with an arbitration mechanism for disputes) or CPI-linked from the expiring rent
- Notice period for exercise: typically 6–12 months before lease expiry
- Automatic expiry if option not exercised (prevents landlord from claiming holdover)

**Statutory renewal rights** (where applicable — cannot be waived by contract):
- **Lebanon**: commercial tenants have renewal rights under the Commercial Code; failure to renew may trigger indemnité d'éviction
- **France**: 3-year tripod renewal rights under Statute Pinel
- **UK**: LTA 1954 Part II (unless contracted out)
- **UAE/KSA**: no equivalent statutory right; purely contractual

### Pass 9 — Assignment and Subletting

**Tenant's target position**:
- Right to assign with landlord consent, consent not to be unreasonably withheld or delayed
- Right to sublet the whole or part, subject to conditions (assignee creditworthy; no change of use)
- Right to share occupation with group companies without triggering assignment restrictions

Flag: absolute prohibition on assignment — standard for short-term leases but unusual and commercially problematic for leases over 5 years. Push for a consent-not-unreasonably-withheld standard with clear criteria.

### Pass 10 — Personal Guarantee

If the landlord requests a personal guarantee from the tenant's directors or shareholders:

- **Scope**: resist guaranteeing obligations beyond rent and service charge; resist guaranteeing make-good and reinstatement at their full uncapped cost
- **Cap**: cap the guarantee at 12 months' rent and service charge
- **Duration**: guarantee should expire if the lease is assigned to a creditworthy assignee and the landlord has consented
- **Release triggers**: negotiate automatic release on: (a) specified years of performance without default; (b) achievement of certain financial metrics by the tenant entity

## Red Flags — Critical Issues

| Issue | Severity | Action |
|---|---|---|
| Open-ended landlord discretion on rent escalation | Critical | Insist on objective index or fixed percentage |
| No cure period before forfeiture for non-payment | Critical | Minimum 14-day notice before right of re-entry |
| Absolute prohibition on assignment | High | Negotiate consent-not-unreasonably-withheld |
| Service charge: no cap, no audit, includes capex | High | Negotiate YoY cap + audit right + capex exclusion |
| Broad tenant indemnity for landlord's third-party claims | High | Limit to claims caused by tenant's acts or omissions |
| Reinstatement: no schedule of condition | High | Refuse to sign without schedule attached |
| Personal guarantee: uncapped | Medium | Cap at 12–24 months rent |
| No quiet enjoyment covenant | Medium | Insert express covenant |
| Force majeure: no rent relief | Low–Medium | Negotiate for loss of access scenarios |

## Output Format

Produce a structured lease review report:

1. **Tenant risk score** (1–5; 1 = severe tenant risk, 5 = well-protected tenant)
2. **Critical issues table** with clause reference, issue, severity, and recommended position
3. **Statutory rights checklist** confirming which tenant rights apply by jurisdiction
4. **Negotiation priority ranking** — what to fight for first, what to concede last

## Related Skills

- [[review-lease-landlord-side]]
- [[review-missing-clauses]]
- [[review-risk-flagging]]
- [[draft-commercial-lease]]
- [[draft-residential-lease]]
- [[review-unusual-terms-detector]]
