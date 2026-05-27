---
name: triple-net-lease-agreement
title: Commercial Triple Net Lease Agreement
description: Drafts U.S. commercial triple-net (NNN) lease agreements from deal materials. Triggers on term sheets, LOIs, or due-diligence packets where rent, taxes, insurance, and maintenance allocate to the tenant. Produces an execution-ready lease covering expense pass-throughs, use controls, default/remedy architecture, transfer gates, indemnity/insurance, SNDA, and exhibits.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/triple-net-lease-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Commercial Triple Net Lease Agreement

Converts transaction facts into a complete, execution-ready NNN lease with full expense-allocation mechanics.

## Quick Start

Collect before drafting:

1. **Deal terms** — term sheet/LOI, rent schedule, concessions, TI allowance, pre-close conditions.
2. **Parties** — legal names, entity type, state of formation, signing authority, guarantor details.
3. **Property** — legal description, parcel ID, site map, title evidence, zoning, occupancy status.
4. **Risk** — insurance binders/baselines, coverage levels, indemnity expectations.
5. **Operations** — permitted use, hours, signage/parking/access needs.
6. **Jurisdiction** — governing-state landlord-tenant statute, fee-shifting rules, anti-indemnity limits, assignment restrictions, enforcement caps.

## Workflow

### Step 1 — Intake Validation

Confirm data across eight categories before drafting:

`PARTIES | PREMISES | RENT/TERM | EXPENSES | USE/COMPLIANCE | DEFAULTS | MORTGAGE | EXECUTION`

Flag gaps. Do not draft around missing material inputs.

### Step 2 — Draft Modules

| Module | Key Content | Output |
|---|---|---|
| Definitions | Consistent defined terms | Cross-reference-safe definitions block |
| Premises & Title | Legal description, use areas, common-area rights | Scope + boundaries + access rights |
| Term | Start trigger, possession milestones, renewal | Option windows, notice format, rent formula |
| Base Rent | Rent, due dates, proration, late charges | Payment timetable + method |
| NNN Expenses | Taxes, insurance, CAM, utilities, reserves | Pass-through formula + audit rights + billing timing |
| Insurance | CGL, property, excess, WC, umbrella | Additional insured, primary/non-contributory, lapse cure |
| Maintenance | Structural vs. non-structural split | Repair obligations + capital replacement treatment |
| Use & Compliance | Permitted/prohibited use, ADA, environmental | Zoning alignment + change-of-use triggers |
| Alterations | Consent standards, ownership at expiry | Buildout obligations + surrender handling |
| Transfers | Assignment/subletting/change-of-control | Consent gate + criteria + continued liability |
| Defaults | Monetary + non-monetary triggers | Notice/cure windows + cure exceptions |
| Remedies | Reentry, reletting, acceleration, damages | Jurisdiction-compliant remedy ladder |
| Risk Allocation | Indemnity, subrogation waiver, liability split | Negligence carve-outs + public policy guardrails |
| Mortgage Relations | SNDA/attornment, mortgage priority | Sale/foreclosure continuity language |
| Final Provisions | Notice, force majeure, estoppel, integration | State-compliant boilerplate + severability |
| Execution Kit | Signature blocks, exhibits, checklist | Execution-ready blanks marked `[____]` |

### Step 3 — Populate Clause Summary

Complete for each lease:

- Lease Name / Property / Parties
- Initial Term / Renewal Terms
- Base Rent / Escalation (CPI/FMV/step-up)
- Security Deposit
- Insurance (limits + forms)
- CAM Methodology / Tax Reconciliation
- Default Cure Periods
- Attorney Fees / Dispute Venue
- Governing Law / Notice Addresses

### Step 4 — Compliance Controls

Apply before finalizing:

1. Validate all defined terms are used consistently throughout.
2. Confirm every variable rate (rent, escalation, CAM, taxes) references a computable source.
3. Insert required exhibits; mark unresolved items `[____]`.
4. Tag uncertain legal rules `[VERIFY]`.
5. Attach closing checklist: insurance binders, estoppel, deposits, corporate authority, first payment proration.

## Jurisdiction Checks

| Check | Risk | Action |
|---|---|---|
| Anti-indemnity limits | Many states ban indemnity for own negligence | Add carve-outs and caps |
| Holdover/penalty rent | May be deemed punitive | Set defensible escalation standard |
| Guaranty enforceability | Varies by authority and drafting | Confirm guarantor language + notice terms |
| Notice service validity | State-specific form/receipt rules | Use state-appropriate service matrix |
| Attorney-fee symmetry | Mutuality often required | Mirror or justify unilateral recovery |

## Pitfalls

- **Never** assume statutory defaults — localize assignment, cure, acceleration, and indemnity clauses to governing state.
- **Never** leave unresolved blanks unmarked — use `[____]` for missing data, `[VERIFY]` for uncertain law.
- **Always** preserve full NNN economics: taxes, insurance, CAM, utilities, common-area methodology.
- **Always** separate structural repair from ordinary maintenance with unambiguous allocation.
- **Always** include measurable consent standards for transfers to prevent unconstrained waiver.
- **Always** include SNDA/attornment where financing or foreclosure risk exists.
