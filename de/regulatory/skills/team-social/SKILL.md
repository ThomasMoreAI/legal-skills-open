---
name: team-social
title: Team Composition
description: Orchestrate the social benefits team for Bürgergeld, ALG I unemployment benefits, health insurance, Kindergeld, and Jobcenter interactions.
author: AliBassam
author_url: https://github.com/AliBassam/german-law-navigator/tree/main/.claude/skills/team-social
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: en
---

Orchestrate the social benefits team.

## Team Composition

- **intake-specialist** — gathers income/employment/family situation
- **social-benefits-specialist** — assesses eligibility and application process
- **administrative-specialist** — if appealing a Jobcenter/benefits Bescheid
- **document-drafter** — drafts Widerspruch or application cover letters

## Pipeline

### Phase 0: Freshness Check

Before intake begins, run a freshness check per `docs/law-freshness.md` (Social Benefits section).
Report findings to the user before proceeding.

### Phase 1: Intake

Key questions:
- Employment status (working / just lost job / never worked in Germany)?
- Nationality and residence status?
- Family situation (children, spouse, dependents)?
- What specific benefit? Or asking what they're eligible for?

### Phase 2: Eligibility Analysis

Delegate to **social-benefits-specialist** with case summary.

### Phase 3: Appeal (if Bescheid received)

If user received a Bescheid they want to challenge:
- Delegate to **administrative-specialist** for Widerspruch strategy
- Delegate to **document-drafter** for Widerspruch letter

### Phase 4: Final Output

```
## Benefits Summary

**Eligible for:** [list of benefits with amounts]
**How to apply:** [step-by-step, specific office]
**Documents needed:** [list]
**Appeal option:** [if Bescheid received]
```
