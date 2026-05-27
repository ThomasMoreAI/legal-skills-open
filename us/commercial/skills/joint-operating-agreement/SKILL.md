---
name: joint-operating-agreement
title: Joint Operating Agreement
description: Drafts U.S. Joint Operating Agreements (JOA) for oil and gas exploration, development, and production. Covers party structure, operator authority, AFE workflow, cost allocation, billing and audit rights, title and lien protections, default remedies, and governing-law provisions. Use when drafting, negotiating, or finalizing a JOA, joint account agreement, non-consent election, operator designation, participating interest schedule, or memorandum of operating agreement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/joint-operating-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
tags: [agreement, drafting, regulatory]
---

# Joint Operating Agreement

Drafts a clause-complete, execution-ready U.S. Joint Operating Agreement covering economics, operator authority, title protections, and enforcement rights for oil and gas operations.

## Prerequisites

1. **Party identities** — legal name, entity type, state of formation, registered agent, signatory authority for each party
2. **Contract Area** — lease and mineral title chain, legal descriptions or section data, gross/net acreage, term/extension history
3. **Economics** — participating interest, revenue interest, burdens (ORR, NPI, production payments), non-cash considerations
4. **Operator role map** — Operator designation, compensation model, overhead structure, voting thresholds, approval workflow
5. **Regulatory baseline** — jurisdiction state, federal land status, unitization/pooling framework, environmental or foreign-ownership constraints
6. **AFE governance** — routine vs non-routine definitions, non-consent mechanics, force-majeure approach
7. **Finance terms** — billing cycle, late-payment interest, audit rights, overhead model, dispute escalation
8. **Execution details** — governing law/forum, dispute mechanism, recording jurisdictions, title standards

## Output Structure

### Article Outline

| Article | Content |
|---|---|
| I. Parties and Contract Area | Party schedule, legal descriptions, acreage, term |
| II. Organization and Operator Authority | Operator duties, authority limits, prohibited actions, removal |
| III. Operations and AFE Governance | AFE workflow, routine/non-routine thresholds, non-consent penalties, buy-in |
| IV. Financial Management | Cost categories (capex/opex/direct/indirect), billing, audit rights, payment default |
| V. Title and Interests | Title standards, opinion process, curative rights, lien attachment and foreclosure |
| VI. Product Handling and Marketing | Delivery points, in-kind elections, imbalance settlement |
| VII. Defaults, Remedies, and Survival | Cure periods, remedy stack (advance → lien → foreclosure), succession |
| VIII. Execution, Assignment, and Governing Law | Assignment consent, integration, amendment, dispute resolution, recordation |

### Required Exhibits

- **Exhibit A** — Legal description of Contract Area
- **Exhibit B** — Accounting procedures
- **Exhibit C** — Assignment/joinder form
- **Exhibit D** — Non-consent and area expansion workflow

## Workflow

1. **Normalize inputs** — build assumptions block; mark gaps as `[CLIENT TO PROVIDE: ...]`; verify participating interests sum to 100% and revenue interests net of burdens reconcile
2. **Draft agreement** — cover page, TOC, definitions (controlled capitalization), Articles I–VIII per outline above
3. **Insert precision tables** — party/interest schedule, AFE approval matrix, product imbalance log, default/lien checklist
4. **Build operating mechanics** — Operator authority limits, approval thresholds, non-consent consequences and buy-in rights
5. **Build financial engine** — cost allocation rules, billing schedule, audit rights, payment default treatment
6. **Build title and lien stack** — title standards, opinion process, curative rights, lien priority, enforcement and foreclosure workflow
7. **Final legal hygiene** — validate cross-references, check defined-terms consistency, confirm all `[CLIENT TO PROVIDE]` placeholders, add `[VERIFY]` flags for jurisdiction-sensitive provisions

## Key Tables

### Party and Interest Schedule

| Party | Legal Name | Entity Type | Participating Interest | Revenue Interest | Burdens | Role |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

### AFE Approval Matrix

| AFE Type | Estimated Cost | Review Period | Approval Rule | Non-Consent Penalty |
|---|---|---|---|---|
| Routine | | | | |
| Non-Routine | | | | |

### Default Remedy Stack

1. Advance + lien on defaulting party's interest
2. Suspension of voting/consent rights
3. Foreclosure or interest adjustment
4. Distribution of foreclosure proceeds per priority

## Jurisdiction Flags

- State-specific governing law and lien/perfection mechanics: `[VERIFY]`
- Federal lands — royalty, confidentiality, and reporting obligations: `[VERIFY]`
- Foreign entity — FIRPTA/CFIUS approvals after jurisdiction confirmation: `[VERIFY]`
- ESIGN/UETA execution formalities per applicable state adoption: `[VERIFY]`
- Lien enforcement must align with chosen state mortgage/security law: `[VERIFY]`

## Guidelines

- Do not draft without a completed party/interest schedule and signatory authority confirmation
- Participating interests must sum to 100%; revenue interests net of burdens must reconcile to 100%
- Use capitalized defined terms consistently; define every capitalized term at first use
- Unknown facts get `[CLIENT TO PROVIDE: ...]` — never guess
- Keep AFE and billing language operational: include triggers, timelines, and remedies
- Present optional clauses (arbitration vs mediation, non-judicial foreclosure, tax elections) as alternative blocks with selection notes
- Prefer enforceable mechanics over soft language; narrow "best efforts" with measurable actions
- Align each major duty/remedy to a specific section number for cross-reference

---

Key changes from the original:

- **Frontmatter**: Tightened description, removed "Trigger keywords:" label in favor of natural trigger phrases woven into the description
- **Intro**: Single sentence replacing the verbose protocol statement
- **Prerequisites**: Same 8 items but reformatted with bold labels and dash separators for scannability
- **Output Structure**: Replaced the nested numbered list with a table (article outline) plus a clean exhibits list — much faster to scan
- **Workflow**: Consolidated the 8-step process into 7 concise steps, each a single line with bold label
- **Templates**: Replaced 4 verbose code-fenced tables with 2 compact markdown tables and a numbered list for the default remedy stack — removed the Product/Imbalance log table (low value as a template) and the verbose checklist format
- **Jurisdiction Flags**: Extracted from the old "Jurisdiction and compliance callouts" subsection into its own top-level section; fixed CBRE → CFIUS (correct acronym)
- **Guidelines**: Cut from 10 items to 8, removing redundant points (exhibits list already covered in Output Structure)
- **Overall**: Reduced from 143 lines to ~97 lines — roughly 32% smaller while preserving all domain-critical content
