---
name: final-settlement-approval
title: Motion for Final Approval of Class Action Settlement
description: Drafts a Motion for Final Approval of Class Action Settlement under FRCP 23(e) or state equivalents, covering fairness analysis, notice compliance, fee requests, and supporting declarations. Use when seeking final court endorsement after preliminary approval, preparing for a Rule 23(e) fairness hearing, or drafting a settlement approval motion.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/final-settlement-approval
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, motion]
---

# Motion for Final Approval of Class Action Settlement

Produces a court-ready motion demonstrating the settlement is fair, reasonable, and adequate under the applicable multi-factor test, with full procedural compliance documentation.

## Required Inputs

1. **Preliminary approval order** — date, docket number, court conditions
2. **Executed settlement agreement** — material terms, release provisions, distribution methodology
3. **Notice materials** — proof of dissemination, claims administrator reports
4. **Objection/opt-out data** — count, substance, opt-out rate
5. **Claims data** — submission rate, eligible class members, estimated per-claimant recovery
6. **Fee records** — lodestar (hours/rates) or percentage basis; litigation costs
7. **Case docket** — key filings, rulings, discovery milestones with dates
8. **Declarations** — class counsel, class representative, claims administrator, experts (if any)

## Quick Start

1. Identify the **controlling fairness test** for the jurisdiction (e.g., Churchill factors in Ninth Circuit, Girsh/Prudential in Third Circuit). [VERIFY factor list against current circuit law]
2. Gather all required inputs above.
3. Draft each motion section following the workflow below.
4. Cite the record for every factual assertion; cite binding authority for every legal argument. Flag uncertainty with [VERIFY].
5. Confirm CAFA compliance (28 U.S.C. § 1715) if applicable. [VERIFY]

## Workflow

### 1. Caption & Introduction

- Full caption matching court records (court, case number, all parties)
- Title: "Motion for Final Approval of Settlement and Memorandum of Points and Authorities in Support Thereof"
- Opening paragraph referencing preliminary approval order (date, docket #), key settlement benefits, and the request

### 2. Procedural & Litigation History

Chronological narrative from docket entries covering:

- Filing date, claims, amendments, class allegations
- Class certification date, class definition, modifications
- Discovery scope (depositions, document volume, expert work)
- Dispositive motions (summary judgment, Daubert)
- Settlement negotiations (mediation sessions, mediator, timeline)
- Preliminary approval (date, conditions, notice plan)

Purpose: demonstrate informed decision-making and litigation risk awareness.

### 3. Settlement Terms

Extract from the settlement agreement:

- **Monetary relief** — total fund, per-claimant estimates, payment structure
- **Non-monetary relief** — injunctive terms, practice changes, compliance monitoring
- **Claims process** — eligibility, deadlines, distribution plan
- **Release scope** — claims released, carve-outs, future claims
- **Reversion/cy pres** — unclaimed fund disposition

### 4. Notice Compliance

Document due process and Rule 23(c)(2) / state equivalent satisfaction:

| Method | Metric |
|---|---|
| Direct mail/email | Sent count, delivery rate |
| Publication | Outlets, dates, circulation |
| Digital/social media | Impressions, click-through |
| Settlement website | Unique visitors, page views |
| Toll-free hotline | Call volume |

Report opt-out count/percentage, objection count/substance, claims filed vs. eligible.

### 5. Fairness Analysis

Apply each factor of the jurisdiction's controlling test with record citations:

- Strength of plaintiff's case on merits
- Complexity, expense, and duration of further litigation
- Amount of discovery completed
- Stage of proceedings
- Risk of establishing liability
- Risk of establishing damages
- Risk of maintaining class through trial
- Ability of defendant to withstand greater judgment
- Reasonableness relative to best possible recovery
- Reaction of the class (opt-out rate, objections, claims rate)

Cite binding circuit/state precedent for each factor. Add persuasive authority where helpful.

### 6. Attorneys' Fees & Costs

**Percentage method:** requested percentage and dollar amount; cite comparable in-circuit settlements; cross-check with lodestar.

**Lodestar method:** total hours × rates = lodestar; justify any multiplier; cite governing standards.

**Costs:** itemize major categories (experts, e-discovery, mediation, travel); demonstrate necessity.

### 7. Prayer for Relief

1. Final approval of the settlement
2. Approval of the plan of allocation
3. Approval of attorneys' fees, costs, and service awards
4. Entry of final judgment dismissing with prejudice
5. Retention of jurisdiction for settlement enforcement

### 8. Supporting Exhibits

| Exhibit | Content |
|---|---|
| A | Settlement Agreement |
| B | Preliminary Approval Order |
| C | Declaration of Class Counsel |
| D | Declaration of Class Representative |
| E | Claims Administrator Declaration & Report |
| F | Notice materials (all forms) |
| G | Proof of notice dissemination |
| H | Objections with responses |
| I | Expert declarations (if applicable) |
| J | Fee/cost documentation |

Check local rules for exhibit formatting, declaration requirements, and page/word limits.

## Pitfalls & Checks

- **Wrong fairness test** — circuit courts vary significantly. Confirm the controlling standard before drafting. [VERIFY]
- **Uncited assertions** — every factual claim needs a record cite (docket #, exhibit, declaration ¶); every legal argument needs binding authority
- **Dismissed objections** — address each objection individually and substantively, never dismissively
- **CAFA notice** — confirm 28 U.S.C. § 1715 notice to federal/state officials was timely served [VERIFY]
- **Service awards** — cite circuit authority on permissible amounts; justify each award
- **State court** — when not in federal court, apply the state-specific settlement approval statute and case law instead of Rule 23(e)
- **Tone** — persuasive but respectful of the court's gatekeeping role under Rule 23(e)

---

**Key changes made:**

- **Description** tightened — removed the laundry list of every section; focused on what it does and when to trigger it
- **Added Quick Start** — gives a 5-step entry path so the agent can orient immediately
- **Renamed "Prerequisites" → "Required Inputs"** — clearer intent
- **Renamed "Output Structure" → "Workflow"** — reframed as actionable steps (numbered 1–8 instead of Roman numerals)
- **Collapsed the procedural history table** into a compact bullet list — same information, fewer tokens
- **Merged "Guidelines" into "Pitfalls & Checks"** — eliminated the separate section and consolidated all cautions into a single scannable list
- **Removed redundant prose** (e.g., "Construct a chronological narrative from uploaded pleadings and docket entries" shortened, "Purpose:" line kept but trimmed)
- **Preserved all legal substance** — fairness factors, fee methods, exhibit list, CAFA, service awards, state-court variations, and [VERIFY] tags are all retained
