---
name: whistleblower-protection-policy
title: Whistleblower Protection Policy
description: Drafts a U.S. whistleblower-protection policy for corporate and nonprofit organizations. Triggers when the user needs a whistleblower policy, retaliation-prohibition clause, hotline-reporting framework, compliance-ethics policy, or governance document addressing SOX, Dodd-Frank, OSHA, or state whistleblower statutes.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/whistleblower-protection-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [corporate, drafting, memo]
---

# Whistleblower Protection Policy

Produces a board-adoptable whistleblower policy with fill-in placeholders and U.S. compliance guardrails for public, private, and nonprofit entities.

## Quick Start

Gather before drafting:

1. **Org profile** — legal name, entity type (public/private/nonprofit), governing state, reporting contacts.
2. **Statute applicability** — SOX, Dodd-Frank, OSHA, False Claims Act, state statutes.
3. **Governance stack** — existing code of conduct, handbook, grievance/investigation policies.
4. **Administration model** — who receives reports, investigates, and oversees outcomes.
5. **Channel preferences** — email, portal, hotline, written/verbal; tone and length targets.
6. **Adoption mechanics** — signatory roles, effective-date process, review cadence.

If any input is missing, emit a short clarifying checklist before drafting.

## Policy Sections (fixed order)

| # | Section | Required Content |
|---|---------|-----------------|
| 0 | Title block & version | Org name, version, effective date, scope entities |
| 1 | Introduction & commitment | Scope statement, non-retaliation promise, protected intent |
| 2 | Covered concerns | Serious-misconduct taxonomy, explicit non-coverage examples |
| 3 | Reporting procedures | Normal path, override path, anonymous option, channel placeholders |
| 4 | Investigation & resolution | Triage, assignment, timeline expectations, reporter updates |
| 5 | Anti-retaliation | Strict prohibition, protected-conduct examples, sanctions |
| 6 | Confidentiality & limits | Need-to-know bounds, legal exceptions, expectation management |
| 7 | Good-faith reporting | Reasonable-belief standard (no certainty burden), bad-faith consequences |
| 8 | Administration & governance | Board/committee roles, secure records, training, periodic review |
| 9 | External legal rights | Supplement-not-replace, no internal-prerequisite condition |
| 10 | Adoption & effective date | Board resolution, signature block, supersession language |

## Required Placeholders

Use exactly these tokens:

- `[Organization Name]`, `[State of Formation]`, `[Board Chair]`, `[Executive Director/CEO]`
- `[Primary Contact]`, `[Alternative Contact]`, `[Hotline URL/Number]`
- `[Adoption Date]`, `[Effective Date]`, `[Review Cycle]`

## Citation Discipline

- Reference statutes only when clearly supported by entity type and jurisdiction.
- Tag uncertain scope with `[VERIFY]` and request jurisdictional confirmation.
- Always verify: SOX §806 applicability, Dodd-Frank retaliation channels, OSHA/state overlap.

## Output Format

- Numbered sections with clear headings.
- Prose-first; bullets only where needed (max 5 per section).
- End each section with implementation-ready fill-ins, not drafting notes.
- Close with signature block for Board Chair and CEO/Executive Director.

## Pitfalls & Checks

- **Never** state that internal reporting is a legal prerequisite for external agency filing.
- Branch public-company vs. nonprofit/private language where statute relevance differs.
- Distinguish anti-frivolous-reporting language from negligent or honest mistakes.
- Protect good-faith reporters regardless of substantiation outcome.
- Set explicit confidentiality limits: need-to-know, lawful disclosure, legal process, audit/defense.
- Require annual or semiannual review, training completion, and board reporting metrics.
- End with disclaimer: "This policy is internal guidance and does not replace legal counsel for specific rights."
