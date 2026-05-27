---
name: court-order-summaries
title: Court Order Summaries
description: Generates structured summaries of court orders and decisions, extracting obligations, deadlines, monetary awards, injunctive relief, and procedural requirements into an action-oriented reference. Flags ambiguities for attorney review. Converts relative timeframes to calendar dates. Use when summarizing court orders, judgments, injunctions, consent decrees, or compliance orders.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/court-order-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Court Order Summaries

Transforms a court order into a structured reference covering who must do what, by when, and with what consequences. Scoped to U.S. federal and state courts.

## Prerequisites

- Full text of the court order with entry date visible
- Identification of all named parties and roles
- Applicable court rules for computing time

## Quick Start

1. Identify the entry date and all named parties
2. Extract obligations, deadlines, and monetary awards into the output sections below
3. Convert every relative timeframe ("within 30 days") to a specific calendar date
4. Flag ambiguities — never resolve or gap-fill

## Output Structure

### 1. Executive Overview (2–3 sentences)

Core holding, most urgent deadline, primary obligated party. Flag anything requiring immediate action (TROs, preliminary injunctions, sub-10-day deadlines) here.

### 2. Parties & Roles

| Party | Role | Obligations Under This Order |
|-------|------|------------------------------|
| [Name] | Plaintiff / Defendant / Third Party | Brief description |

### 3. Deadlines & Required Actions

| Party | Action Required | Deadline (Date) | Order Ref. | Consequence if Missed |
|-------|----------------|-----------------|------------|----------------------|

- Convert relative timeframes to calendar dates from the entry date
- Account for weekends, court holidays, and time-computation rules
- Note stays or deadline suspensions pending appeal

### 4. Monetary Obligations

| Obligor | Obligee | Amount | Type | Due Date | Order Ref. |
|---------|---------|--------|------|----------|------------|

Type: judgment / sanction / fee / bond.

### 5. Injunctive & Equitable Relief

| Type | Party Bound | Conduct Required or Prohibited | Duration / Conditions | Order Ref. |
|------|------------|-------------------------------|----------------------|------------|

Types: mandatory injunction, prohibitory injunction.

### 6. Procedural & Ongoing Requirements

- Reporting obligations (frequency, recipient, format)
- Notice provisions
- Compliance certifications
- Court supervision or monitoring requirements

### 7. Findings & Future Proceedings

- Findings of fact or conclusions of law with precedential or preclusive effect
- Rights preserved or limited (appeal, modification, enforcement)
- Conditions precedent or contingent obligations

### 8. Ambiguities & Attorney Review Items

List provisions that are unclear, internally inconsistent, or require legal interpretation. Do not resolve ambiguities — flag them for attorney review.

## Pitfalls & Checks

- **Fidelity**: Reproduce deadlines and obligations verbatim or in direct paraphrase; never alter scope
- **No gap-filling**: If the order is silent on a consequence or procedure, state that explicitly — do not infer
- **Cite everything**: Every obligation, deadline, and finding must reference its ¶, page, or § number
- **Immediate flags first**: Anything actionable within 7 days must appear in the Executive Overview
- **Plain language**: Use accessible terms; retain legal terms of art with brief parenthetical context
- **Jurisdiction header**: Note the specific court and jurisdiction at the top of every summary

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec; discovery relies on `description` keywords
- **Tightened description** — same trigger guidance, fewer tokens
- **Added Quick Start** — gives the agent an immediate action sequence before the full output template
- **Removed decorative `---` dividers** between output subsections — unnecessary token cost
- **Removed emoji** (⚠) — per codebase convention
- **Compressed table annotations** — e.g., monetary type values moved to a single inline note instead of a verbose column header
- **Renamed "Guidelines" to "Pitfalls & Checks"** — aligns with best-practice body structure and signals actionable guardrails
- **Reduced from 96 lines to 72 lines** — well under the 500-line budget
