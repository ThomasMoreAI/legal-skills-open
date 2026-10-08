---
name: pa-workflow-inhouse-contract-intake-routing-sboghossian
title: In-House — Contract Intake Routing
description: Use when an in-house legal team needs to automatically triage and route incoming contracts to the appropriate reviewer — from automated low-risk processing to senior counsel or external counsel escalation. Covers the classification logic, routing rules, and automation criteria for an in-house contract intake workflow. Triggers when setting up or running a contract triage and routing system.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-inhouse-contract-intake-routing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# In-House — Contract Intake Routing

In-house legal teams are typically undersized relative to the volume of contracts they receive. Routing the right contract to the right reviewer — and auto-processing those that don't need a lawyer — is the highest-leverage capacity lever available. This skill provides the classification logic and routing rules for a contract intake workflow.

## Purpose

Classify incoming contracts by type and risk level, then route each to the appropriate handler:
- **Auto-process**: low-risk, standard-form contracts that can be accepted with no changes
- **AI-assisted review**: standard contracts that need clause-by-clause checking but not full legal counsel time
- **Junior counsel**: moderate complexity contracts needing review and limited negotiation
- **Senior counsel / GC**: high-value or high-risk contracts requiring strategic review
- **External counsel**: M&A, complex IP, cross-border regulatory, or matters requiring specialist expertise

## Inputs

| Input | Why it matters |
|---|---|
| Contract document | The incoming contract (PDF, DOCX, or text) |
| Contract type | What type of agreement is it? |
| Counterparty | Who is the other party — their size, sophistication, relationship |
| Deal value | Determines materiality and required review level |
| Jurisdiction | Affects applicable law and required expertise |
| Urgency | Signature deadline drives routing priority |

## Classification logic

### Step 1 — Identify contract type

| Contract type | Base routing |
|---|---|
| NDA (Mutual) — standard form | AI review → auto-sign if within approved playbook |
| NDA (One-way, us as disclosing party) | AI review → junior counsel if non-standard |
| NDA (One-way, us as receiving party) | AI review → junior counsel — receiving party NDAs have asymmetric risk |
| Vendor/SaaS contract (low value < USD 10K/yr) | AI review → auto-approve if within standard |
| Vendor/SaaS contract (medium value USD 10K–100K/yr) | Junior counsel |
| Master Service Agreement (MSA) | Senior counsel |
| Enterprise SaaS (> USD 100K/yr) | Senior counsel |
| Employment contract (standard) | AI review → HR sign-off → GC for exceptions |
| Employment contract (executive) | Senior counsel |
| IP Assignment / Work-for-hire | IP counsel or GC |
| Commercial agency / distribution | Senior counsel — agency law risk (see MENA notes below) |
| Joint venture | Senior counsel + external counsel |
| M&A (any form) | GC + external M&A counsel |
| Loan / facility agreement | GC + external finance counsel |
| Government contract | GC — public procurement rules may apply |
| Settlement agreement | GC — litigation strategy implications |

### Step 2 — Escalation triggers

Even within the base routing category, escalate to the next level if:

| Trigger | Escalation |
|---|---|
| Uncapped liability | One level up |
| Unusual termination for convenience (short notice) | One level up |
| Perpetual IP licence or IP ownership transfer | IP counsel |
| Cross-border with unfamiliar governing law | External counsel in that jurisdiction |
| Deal value > USD 500K | Senior counsel minimum |
| Counter-party is a government entity | GC + compliance review |
| Counter-party is a related party (affiliate, director) | GC + audit committee notification |
| Personal data processing (DPA/addendum) | Privacy counsel or DPO review |
| Security / InfoSec provisions | GC + CISO review |

### Step 3 — Automation criteria for auto-sign

A contract can be processed without any human legal review only if all of the following are true:
- Contract type is on the approved auto-sign list (typically: standard mutual NDA only)
- Contract uses an approved template or falls within the defined playbook tolerances
- Deal value is below the auto-sign threshold (set per company policy)
- No material deviation from the approved playbook
- No escalation triggers present (see Step 2)
- AI review has flagged no red flags

## Routing output

For each incoming contract, produce a routing ticket:

```
CONTRACT INTAKE TICKET
======================
Contract type:        [Type]
Counterparty:         [Name]
Deal value:           [Amount]
Jurisdiction:         [Governing law]
Urgency:              [Signature deadline if known]

AI classification:    [Auto-process / AI-review / Junior / Senior / External]
Escalation triggers:  [List, or "None"]
Assigned to:          [Name/role]
Priority:             [Routine / High / Urgent]

AI review summary:    [Key clause flags, if AI review performed]
Action required:      [What the assigned reviewer must do]
Deadline:             [Internal review deadline]
```

## MENA-specific routing notes

| Risk area | MENA-specific rule |
|---|---|
| UAE Commercial Agencies | Any distribution, exclusive agency, or authorised reseller contract with a UAE national counterparty may engage the UAE Commercial Agencies Law (Federal Law No. 18 of 1981, as amended). Registered agent termination rights are statutory and non-waivable. Escalate all distribution agreements to senior counsel for this analysis. |
| KSA Saudization | Service contracts with KSA counterparties: check for Nitaqat/Saudization obligations affecting staffing. |
| Employment — MENA generally | Employment contracts in UAE/KSA must comply with mandatory statutory provisions that cannot be waived. Any clause that purports to waive statutory rights needs GC sign-off. |
| Notarisation | Certain UAE and KSA transactions require notarised documents (real property, power of attorney, certain corporate acts). If in doubt, route to senior counsel. |
| Language | UAE courts use Arabic; KSA courts use Arabic. English-only contracts are enforceable but require translation in proceedings. Flag if the contract should be bilingual. |

## Performance metrics for the routing function

| Metric | Target |
|---|---|
| Average time from intake to routing assignment | < 2 hours |
| Auto-processed (no lawyer time) | 20–40% of volume |
| Contracts reviewed within SLA | > 90% |
| Escalation rate (proportion requiring external counsel) | < 10% |
| Rerouting rate (wrong initial classification) | < 5% |

## Related skills

- [[pa-workflow-inhouse-commercial-team-clause-explainer]]
- [[pa-workflow-inhouse-cross-functional-translation]]
- [[output-table-of-comparisons]]
- [[router-contract-type-classifier]]
