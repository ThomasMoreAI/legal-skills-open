---
name: easement-dispute-complaint
title: Easement Dispute Complaint
description: Drafts a plaintiff-side U.S. complaint for easement disputes covering interference, trespass, declaratory judgment, and injunctive relief. Triggers when user needs to initiate litigation to enforce, clarify, or establish easement rights against interference, blockage, or encroachment on real property.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/easement-dispute-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, litigation, pleading]
---

# Easement Dispute Complaint

Drafts a court-ready complaint for easement interference in U.S. real property litigation. Structures element-driven allegations, jurisdictional pleading, and comprehensive prayer for relief.

## Prerequisites

Collect before drafting:

1. **Easement instrument** — recorded grant, deed reservation, or basis for implied/prescriptive claim (book/page or document number)
2. **Legal descriptions** — dominant and servient estates, surveys or plats
3. **Interference evidence** — dated photos, correspondence, obstruction descriptions
4. **Party information** — full legal names, addresses, ownership/interest roles
5. **Jurisdiction/venue** — county, court, local formatting rules
6. **Damages** — alternative access costs, property value impact, repair/removal expenses

## Quick Start

1. Gather prerequisites and identify easement type (express, implied, necessity, prescriptive)
2. Determine jurisdiction (state vs. federal diversity) and venue
3. Draft complaint following the output structure below
4. Attach exhibits: recorded instrument, chain-of-title excerpts, survey, photos, demand letters
5. Run the checklist in Pitfalls before finalizing

## Output Structure

### 1. Caption & Introduction

- Court name with county/district/division
- Full legal names for all parties (include entity type for non-individuals)
- Document title (e.g., *Complaint for Interference with Easement Rights, Trespass, and Injunctive Relief*)
- One-paragraph roadmap: easement type, interference, relief sought

### 2. Party Allegations

| Party | Required Allegations |
|---|---|
| Plaintiff | Name, address, interest in dominant estate, standing basis |
| Defendant | Name, address, relationship to servient estate, role in interference |

### 3. Jurisdiction & Venue

- **State court**: claim affecting title/possession of real property; amount in controversy if threshold applies
- **Federal diversity**: citizenship of each party, complete diversity, AIC > $75,000
- **Venue**: property location statute; cite venue code; personal jurisdiction if out-of-state defendant

### 4. Factual Narrative (Chronological)

**Easement creation — allege by type:**

| Type | Required Facts |
|---|---|
| Express grant | Instrument date, parties, recording info; quote scope/location language; chain of title |
| Reservation | Conveyance history, reservation language, recording info |
| Implication | Apparent + continuous use at severance; reasonable necessity; intent to continue |
| Necessity | Common ownership, severance date, landlocked/no public access at severance |
| Prescriptive | Open & notorious; continuous; adverse; claim of right; statutory period with specific dates |

**Physical description:**
- Dimensions, boundaries, location per survey/plat
- Improvements (road, driveway, utilities) and who maintains them
- Historical use pattern with duration

**Defendant's interference — allege with specificity:**
- Each act: date, time, location, description (barrier, parked vehicles, debris, threats)
- Obstruction dimensions relative to easement boundary
- Demand letters sent, responses, failed negotiations
- Defendant's stated position (abandonment, scope dispute) — address preemptively

**Damages:**
- Alternative access costs
- Obstruction removal expenses
- Diminution in dominant estate value
- Lost use and enjoyment

### 5. Causes of Action

**Count I — Interference with Easement Rights**
1. Valid easement exists [incorporate creation facts]
2. Defendant interfered through specific acts
3. Interference is substantial and wrongful
4. No legal justification
5. Ongoing harm to plaintiff
6. Cite applicable state property law

**Count II — Trespass** *(if applicable)*
1. Plaintiff holds possessory interest in easement area
2. Defendant intentionally placed objects/structures without permission
3. Unlawful interference with possessory rights
4. Allege continuing vs. temporary trespass as facts support

**Count III — Declaratory Judgment**
1. Actual, justiciable controversy exists
2. Questions for determination: location, scope, maintenance obligations, validity
3. Harm from uncertainty OR defendant has taken adverse position
4. Cite state declaratory judgment act [VERIFY statute]

**Count IV — Injunctive Relief**
1. No adequate remedy at law (access loss not fully compensable; interference ongoing)
2. Irreparable harm — describe specifically
3. Balance of hardships favors plaintiff
4. Public interest supports enforcement
5. Seek temporary, preliminary, and permanent relief

**Additional counts to consider:**
- **Nuisance** — interference beyond easement area
- **Breach of covenant** — if easement created by agreement with express promises
- **Slander of title** — if defendant made false statements challenging validity

### 6. Prayer for Relief

1. **Declaratory judgment** — existence, validity, location, scope; defendant's obligation to cease interference
2. **Injunction** (preliminary + permanent) — cease interference; remove obstructions; court retains jurisdiction
3. **Compensatory damages** — alternative access costs, removal expenses, property value diminution
4. **Consequential damages** — foreseeable harm per state law
5. **Attorney's fees** — if available by statute, contract, or equity [VERIFY fee-shifting authority]
6. **Pre/post-judgment interest** at statutory rate
7. **Costs of suit**
8. **Further relief as the court deems just**

## Pitfalls & Checks

- **Pleading specificity**: each interference act needs date, description, and location — conclusory "interference" allegations are insufficient
- **Exhibits**: reference each exhibit (instrument, survey, photos, demand letters) in the body text
- **Verification**: include if required by local rules or if seeking TRO/preliminary injunction
- **Paragraph structure**: one allegation per numbered paragraph; consecutive numbering throughout
- **Anticipate defenses**: preemptively rebut abandonment, scope excess, and location disputes in factual narrative
- **Jurisdiction-specific [VERIFY]**: prescriptive easement statutory periods vary by state; injunction standards vary by circuit/state
- **Citation format**: Bluebook or local rules; verify all statutory citations
- **Internal consistency**: every cause of action must be supported by factual allegations; every prayer item must correspond to an asserted claim
