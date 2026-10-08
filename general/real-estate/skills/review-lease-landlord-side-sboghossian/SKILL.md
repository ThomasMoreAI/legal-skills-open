---
name: review-lease-landlord-side-sboghossian
title: Lease Review — Landlord Side
description: Use when reviewing a commercial or residential lease from the landlord's perspective. Identifies weaknesses in the landlord's position across rent escalation, use restrictions, repair allocation, personal guarantees, forfeiture mechanics, reinstatement, and assignment control. Covers MENA jurisdictions (Lebanon, UAE Dubai, UAE Abu Dhabi, KSA) with statutory tenant protections that cannot be waived, plus general commercial-lease best practice.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-lease-landlord-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Lease Review — Landlord Side

## When to use this

Use when a landlord (or a lawyer acting for a landlord) needs to review a lease draft for adequacy of protection, balance of obligations, and compliance with local statutory requirements. The landlord's goal is to maximize security of income, preserve the asset, and maintain flexibility. This skill flags where a draft lease is insufficiently protective and recommends positions.

For the mirror tenant-side review, use [[review-lease-tenant-side]].

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Lease draft | The full document including schedules and plans | Required |
| Jurisdiction | Statutory protections and customary terms vary enormously | Required — ask if unclear |
| Property type | Commercial / office / retail / warehouse / residential — affects regime | Infer from draft; ask if unclear |
| Tenant identity | SME vs corporate; creditworthiness drives guarantee requirements | Ask if not in draft |
| Market context | Landlord vs tenant market affects negotiating baseline | Assume balanced unless told otherwise |

## Review Methodology

### Pass 1 — Rent and Escalation

**What to look for**:
- Is escalation tied to an objective index (CPI / HICP / RPI / a local equivalent) or to landlord's unilateral determination?
- Is there a floor (base rent cannot fall below initial level)?
- Is there a cap (limits upside for landlord — challenge if market-review mechanism exists separately)?
- Review frequency: annual reviews protect landlord better in inflationary environments; periodic market reviews (every 5 years) are customary in long commercial leases

**Strong landlord position**: CPI escalation + buffer (e.g., CPI + 1%) with a floor at the initial rent, plus a market review every 5 years with an upward-only ratchet.

**Statutory ceiling**: Dubai: RERA Rental Increase Calculator sets caps on annual rent increases (Dubai Decree 26/2013, amended by Decree 43/2013). Any escalation clause must be consistent with permissible RERA increments — a clause providing for escalation above RERA limits is void. Abu Dhabi has its own rent cap regime.

**Lebanon**: Under Law 160/1992 and subsequent legislation, commercial lease rents were historically frozen for old tenants. Post-2019 practice: new commercial leases are freely negotiated, but rent adjustment in USD requires careful drafting given lira/dollar exchange regime and Banque du Liban circulars affecting payment obligations.

### Pass 2 — Use Restriction

A well-drafted use clause:
- Specifies the permitted use precisely (e.g., "retail sale of consumer electronics and accessories only") — not "retail use generally"
- Prohibits change of use without landlord consent
- Prohibits subletting for a use outside the permitted description
- Specifies that no competing use within the building/complex is permitted (if applicable)

Flag: use clauses that are too broad ("any lawful commercial use") reduce the landlord's control and may limit the landlord's ability to enforce quiet enjoyment obligations to other tenants.

### Pass 3 — Fit-Out, Alterations, and Make-Good

**Fit-out approval**: tenant should be required to submit detailed plans and specifications for approval before commencing fit-out. Approval should not be unreasonably withheld, but landlord retains discretion on structural modifications.

**Insurance and permits**: tenant must maintain contractor's all-risk insurance during fit-out; must obtain all planning and building permits; any breach makes fit-out at tenant's risk.

**Make-good / reinstatement**: at lease expiry, tenant reinstates to delivery condition (shell-and-core or as-built) unless landlord elects to retain specific fit-out elements. Reinstatement obligation is worth money — ensure it is clearly drafted and the baseline delivery condition is documented (schedule of condition attached to lease at commencement).

Flag: leases without a schedule of condition attached — disputes on reinstatement are unavoidable without photographic/surveyor evidence of delivery condition.

### Pass 4 — Repair Obligations

**Standard allocation (commercial leases)**:
- Tenant: maintains and keeps in good repair and decoration the internal parts of the demised premises (including non-structural walls, floors, ceilings, fitted services, glazing)
- Landlord: maintains the structure, exterior, roof, and common parts; typically recovered through service charge

**Traps for landlord**:
- "Tenant-favored" repair clauses that limit tenant's obligation to "fair wear and tear" — in commercial leases this is unusual and weakens the landlord's position significantly
- Lease that makes landlord responsible for HVAC or specialist equipment installed by tenant
- No specific obligation on tenant to allow inspection and access for repair

**Recommendation**: include a specific obligation on the tenant to carry out repairs as required and not to allow the premises to fall into disrepair; landlord step-in right to execute repairs at tenant's cost if tenant fails to comply after notice.

### Pass 5 — Service Charge

A landlord-protective service charge clause:
- Defines service charge broadly: estate management, common-area utilities, insurance, security, lift maintenance, landscaping, waste removal
- Provides for full pass-through of actual costs with reasonable management fee (typically 10–15%)
- Sets out allocation methodology (e.g., pro rata on floor area)
- Includes a provision for estimated service charge payable in advance with annual reconciliation

Flag: service charge caps (beneficial to tenant) that limit the landlord's ability to recover actual costs; definitions that exclude major items; no mechanism for advance payment (creates cash-flow risk for landlord).

### Pass 6 — Personal Guarantee

For SME or newly-incorporated tenants:
- Personal guarantee from individual director(s)/owner(s)
- Capped at 12–24 months' rent (or total rent and service charge for the guarantee period)
- Guarantee must be an unconditional, on-demand guarantee — not a "see-to-it" guarantee which requires landlord to first pursue the tenant
- Guarantee should survive assignment unless landlord releases in writing

Jurisdictional note: in UAE, guarantees by company directors/shareholders require the guarantor to have been given independent legal advice or the guarantee may be challenged. Ensure the guarantee deed recites this. In Lebanon, a personal guarantee (kafala) executed before a notary is stronger than a private document.

### Pass 7 — Forfeiture / Termination for Non-Payment

**Landlord's right of forfeiture** (re-entry):
- Non-payment: right should arise after a short grace period (7–14 days after due date)
- Other breaches: right should arise after a cure period (typically 30 days for remediable breaches; immediate for irremediable breaches)
- Statutory minimum cure periods in many jurisdictions limit how quickly a landlord can act

**MENA statutory floors**:
- **UAE/Dubai**: Decree 26/2013 and RERA rules require a formal eviction notice through the Rental Disputes Center; self-help repossession is not permitted
- **Lebanon**: Law 160/1992 and the Law of Summary Procedures regulate eviction; courts have discretion to grant time-to-cure; commercial tenants have renewal rights under the Commercial Code
- **KSA**: Summary eviction before the commercial court is possible but procedurally protracted; landlord should include clear termination provisions consistent with SCCA arbitration for faster resolution

Flag: a lease that provides for termination/re-entry without adequate notice provisions — may be unenforceable in the relevant jurisdiction.

### Pass 8 — Assignment and Subletting

**Strong landlord position**: absolute prohibition on assignment and subletting without prior written consent; consent can be withheld or conditioned at landlord's absolute discretion.

**Practical compromise**: prohibition without consent, consent not to be unreasonably withheld, but landlord can require: (a) original tenant remains as guarantor; (b) incoming assignee is of equivalent or better financial standing; (c) no change in permitted use.

Flag: "reasonableness" standard on consent without clear criteria — creates risk of disputes. Define unreasonable refusal explicitly.

### Pass 9 — Renewal Rights

**Landlord preference**: lease expires at the end of the term without statutory renewal rights (where local law permits).

**Statutory renewal rights that cannot be waived**:
- **Lebanon**: Commercial Code Article 524 and Law 160/1992 grant commercial tenants a right to renew (droit au bail); on non-renewal by landlord, tenant may be entitled to goodwill compensation (indemnité d'éviction). This applies regardless of contract terms.
- **France**: Statute equivalent — Loi Pinel 2014 rules on commercial leases; tenant entitled to renewal or indemnité d'éviction after 3 years (première période triennale)
- **UK**: Landlord and Tenant Act 1954, Part II — commercial tenant has right to lease renewal unless landlord establishes grounds under Section 30. Must be contracted out if landlord does not want renewal rights.
- **UAE/Dubai**: No equivalent statutory renewal right for commercial leases; renewal terms are contractual

Recommend: expressly state in the lease whether renewal rights exist and, where permitted by local law, exclude statutory renewal obligations.

## Red Flags — Tenant Asks to Resist

| Tenant Ask | Why Landlord Should Push Back |
|---|---|
| Cure periods longer than 30 days for rent arrears | Extends period of non-payment before landlord can act |
| "Reasonable consent" standard on all alterations | Limits landlord control over physical condition of asset |
| Force majeure relief from rent obligation | Landlord's mortgage and service obligations do not pause |
| Option to renew at current rent (no market review) | Locks landlord into below-market rent on renewal |
| Break option at tenant's election | Undermines income security; if agreed, require conditions (no arrears; reinstatement) |
| Service charge cap | May leave landlord unrecovered for actual costs |
| Absolute assignment prohibition as "too onerous" | Counter: consent not to be unreasonably withheld is the compromise |

## Output Format

Produce a structured report with:

1. **Landlord protection score** (1–5; 1 = very weak, 5 = strong landlord position)
2. **Critical gaps** (items that leave the landlord materially exposed)
3. **Statutory compliance issues** (items that may be void or unenforceable under local law)
4. **Recommended positions** for each key clause (ideal / acceptable / walk-away)
5. **Negotiation priority order** (most important items for landlord to hold)

## Related Skills

- [[review-lease-tenant-side]]
- [[review-missing-clauses]]
- [[review-risk-flagging]]
- [[draft-commercial-lease]]
- [[review-unusual-terms-detector]]
