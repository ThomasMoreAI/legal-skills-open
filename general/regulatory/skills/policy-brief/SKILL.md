---
name: policy-brief
title: Policy Brief
description: Generates structured public policy briefs analyzing legislation across economic, social, legal, and implementation dimensions. Use when drafting legislative impact analyses, policy summaries, regulatory briefs, or government affairs memoranda for lawmakers, lobbyists, or civic organizations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/policy-brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Policy Brief

Produces a balanced, structured policy brief that distills complex legislation into actionable impact analysis for diverse stakeholders.

## Prerequisites

1. **Legislation text** — full bill text, enrolled version, or enacted law
2. **Legislative history** (optional) — committee reports, fiscal notes, floor statements, amendment records
3. **Supplemental materials** (optional) — CBO/CRS analyses, agency impact statements, stakeholder comment letters

## Quick Start

1. Gather legislation text and any available history/analysis
2. Follow the output structure below section by section
3. Apply guidelines throughout — objectivity, plain language, fact vs. projection
4. Mark unverified statutory citations with `[VERIFY]`

## Output Structure

### 1. Executive Summary (2–3 paragraphs)

Cover: policy area, problem addressed, primary mechanism, and net expected impact (one-sentence takeaway).

### 2. Background & Context

- Policy problem and triggering events
- Prior legislative attempts or existing law being modified
- Political context: sponsors, coalitions, amendment history
- Comparable policies in other jurisdictions

### 3. Key Provisions

| Provision | Description | Effective Date | Mandatory/Discretionary | Sunset? |
|-----------|-------------|----------------|------------------------|---------|
| § ___ | ... | ... | ... | ... |

Flag phased implementation and delegated rulemaking authority.

### 4. Impact Analysis

Analyze across four dimensions:

- **Economic** — effects on businesses (by size/sector), government budgets, individuals; include quantitative projections from fiscal notes/CBO scores where available
- **Social** — affected populations, equity/distributional effects, public health/education/safety implications
- **Legal & Regulatory** — constitutional considerations, federalism implications, relationship to existing framework, new compliance/enforcement mechanisms
- **Implementation** — responsible agencies, resource requirements, timeline/phasing, administrative capacity concerns

### 5. Stakeholder Positions

| Stakeholder | Position | Rationale |
|-------------|----------|-----------|
| ... | Support/Oppose/Mixed | ... |

Present viewpoints without advocacy. Note coalition alignments.

### 6. Risks & Open Questions

- Unintended consequences and genuine uncertainty
- Implementation bottlenecks and litigation risk
- Questions dependent on future rulemaking or appropriations

### 7. Sources

List key sources consulted (legislation text, committee reports, agency analyses, academic studies).

## Pitfalls & Checks

- **Objectivity is paramount** — inform, do not persuade; acknowledge all sides of legitimate debate
- **Plain language** — define legal/technical terms on first use; use concrete examples for abstract mechanisms
- **Fact vs. projection** — label estimates, forecasts, and contested claims explicitly
- **Target length** — 3–6 pages; optimize for time-constrained readers
- **Jurisdiction** — default to U.S. federal; note state-level interactions where relevant
- **Citations** — mark any statutory citation not from provided materials with `[VERIFY]`
- **Audience** — write for policy professionals and informed non-specialists
