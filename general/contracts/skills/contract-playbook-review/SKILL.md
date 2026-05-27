---
name: contract-playbook-review
title: Contract Playbook Review
description: 'Reviews contracts clause-by-clause against a defined negotiation playbook, grading each clause as acceptable, needs review, or unacceptable and generating specific redline suggestions with winning language. Supports playbook creation from existing contracts, precedent language, or policy documents. Use when reviewing incoming contracts against firm standards, running playbook-based contract reviews, creating or maintaining negotiation playbooks, standardizing contract language across teams, or conducting high-volume contract review with consistent quality. Trigger keywords: playbook, contract review, clause grading, redline, winning language, contract compliance, clause-by-clause, contract standards, playbook review.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/contract-playbook-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [transactional, corporate, agreement, analysis, drafting]
---

# Contract Playbook Review

Reviews contracts systematically against a negotiation playbook — a structured set of rules defining acceptable, negotiable, and unacceptable positions for each clause type. Produces clause-level compliance grades and specific redline suggestions using preferred language.

## Prerequisites

1. **Contract under review** — the agreement to analyze (draft, counterparty paper, or executed)
2. **Playbook** — one of:
   - An existing playbook document (any format: PDF, Word, markdown, spreadsheet)
   - A set of precedent contracts with "winning language" to extract rules from
   - A firm policy or standards document describing acceptable positions
   - Verbal description of key positions (minimum viable — will generate a partial playbook)
3. **Client role** — which party the reviewer represents (buyer/seller, licensor/licensee, landlord/tenant, etc.)
4. **Jurisdiction** — governing law, if known
5. **Priority areas** — any clauses or risk areas requiring heightened scrutiny

If no playbook is provided, offer to create one from precedent contracts or firm standards before proceeding.

## Workflow

### Phase 1: Playbook Preparation

If the playbook is not already structured, convert it into a clause rule set.

For each clause type, extract or define:

| Field | Description |
|---|---|
| **Clause category** | E.g., Limitation of Liability, Indemnification, Term & Termination |
| **Acceptable position** | Language or terms the firm will accept without negotiation |
| **Fallback position** | Compromise language the firm can live with after negotiation |
| **Unacceptable position** | Terms that must be rejected or substantially revised |
| **Winning language** | Preferred draft language to propose when redlining |
| **Rationale** | Why this position matters (business risk, legal exposure, precedent) |
| **Escalation trigger** | Conditions requiring partner or client approval |

**Creating a playbook from precedent contracts:**
1. Analyze 3–5 executed contracts where the firm achieved favorable terms
2. For each clause type, extract the language that was ultimately agreed
3. Identify patterns — which provisions were consistently negotiated and how
4. Synthesize into the rule structure above
5. Flag any clauses where precedent contracts are inconsistent with each other

### Phase 2: Clause-by-Clause Review

Analyze every material provision in the contract against the playbook rules.

For each clause, produce:

| Field | Content |
|---|---|
| **Section reference** | Exact section number and title from the contract |
| **Clause category** | Mapped playbook category |
| **Grade** | Acceptable / Needs Review / Unacceptable |
| **Current language** | Verbatim quote of the key provision |
| **Issue** | What deviates from the playbook position and why it matters |
| **Suggested redline** | Specific replacement language from the playbook's winning language, adapted to the contract's defined terms and structure |
| **Escalation** | Whether this triggers partner/client approval per playbook rules |

**Grading criteria:**

- **Acceptable** — Clause materially conforms to the playbook's acceptable or fallback position. No changes needed.
- **Needs Review** — Clause is between the fallback and unacceptable positions, or contains ambiguity that could be read unfavorably. Redline suggested but attorney judgment required.
- **Unacceptable** — Clause matches an unacceptable position or is absent when required. Must be revised before execution.

### Phase 3: Review Summary

#### 3a. Compliance Dashboard

| Category | Total Clauses | Acceptable | Needs Review | Unacceptable |
|---|---|---|---|---|
| Liability & Risk | | | | |
| Commercial Terms | | | | |
| IP & Confidentiality | | | | |
| Term & Termination | | | | |
| Governance & Disputes | | | | |
| **Totals** | | | | |

#### 3b. Critical Issues (Unacceptable)

List every unacceptable clause with:
- Section reference
- Issue summary (one sentence)
- Required action (redline, delete, or add missing provision)
- Escalation status

#### 3c. Negotiation Priority List

Rank all flagged items by:
1. **Business impact** — financial exposure, operational risk
2. **Likelihood of counterparty concession** — based on market norms
3. **Interdependencies** — clauses that affect other provisions if changed

#### 3d. Missing Provisions

Clauses the playbook requires but the contract omits entirely. For each:
- Playbook requirement
- Risk of omission
- Proposed insertion language

### Phase 4: Redline Output

Produce a consolidated redline draft showing all suggested changes:
- Deletions in strikethrough
- Additions in bold
- Each change annotated with the playbook rule and grade that triggered it
- Preserve original section numbering and defined terms

## Clause Categories — Standard Coverage

Review at minimum these categories (expand based on contract type):

**Liability & Risk Allocation**
- Limitation of liability (cap, consequential damages exclusion, carve-outs)
- Indemnification (scope, mutual vs. one-sided, survival, procedures)
- Insurance requirements (types, minimums, additional insured)
- Warranty / disclaimer (express, implied, remedy limits)
- Force majeure (definition, notice, extended-event termination)

**Commercial Terms**
- Payment terms (timing, late fees, set-off, price escalation)
- Scope of work / deliverables (change orders, acceptance criteria)
- Service levels / SLAs (metrics, measurement, remedies, credits)
- Volume commitments / minimum purchase obligations
- Audit rights

**IP & Confidentiality**
- IP ownership (work product, background IP, license-back)
- Confidentiality (term, carve-outs, residuals, return/destruction)
- Data protection / privacy (DPA, sub-processors, breach notification)
- Non-compete / non-solicit (scope, duration, enforceability)

**Term & Termination**
- Initial term and renewal (auto-renewal, opt-out window, notice period)
- Termination for convenience (notice, wind-down, fees)
- Termination for cause (cure period, material breach definition)
- Post-termination obligations (transition, survival clauses)

**Governance & Disputes**
- Governing law and venue
- Dispute resolution (arbitration vs. litigation, institution, seat)
- Assignment / change of control (consent requirements, exceptions)
- Entire agreement / amendment (written modification requirements)
- Notices (method, addresses, effectiveness)

## Guidelines

- Quote exact section numbers and key language verbatim — never paraphrase when grading
- Apply playbook rules consistently across all clauses — do not selectively enforce
- When the contract uses defined terms, adapt suggested redlines to match (e.g., use "Company" not "Vendor" if that is the contract's defined term)
- Flag any clause that could be read two ways and grade based on the less favorable interpretation
- If the playbook is silent on a clause type, note it as "Outside playbook scope" — do not grade
- Mark [VERIFY] on any enforceability assessment under specific jurisdiction law
- Do not assume counterparty will accept suggested language — present alternatives at fallback positions where relevant
- For high-volume review (multiple contracts against same playbook), maintain consistency — identical clauses get identical grades
- Separate factual analysis from negotiation strategy recommendations
- Note when a clause interacts with other provisions (e.g., liability cap affects indemnity, termination affects payment obligations)
