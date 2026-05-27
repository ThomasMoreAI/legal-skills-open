---
name: legal-memo
title: Legal Memorandum
description: Drafts U.S. internal legal memoranda using IRAC structure to analyze issues, synthesize authority, assess risks, and recommend strategy. Use when asked to draft a research memo, internal memo, issue analysis, case strategy memo, or any IRAC-based legal analysis.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/legal-memo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Legal Memorandum

Produces an objective, litigation-focused internal memo that answers a legal question and informs strategy. Uses IRAC (Issue, Rule, Application, Conclusion) throughout the Discussion section.

## Prerequisites

Gather before drafting:

1. **Issue statement** — single, answerable legal question with jurisdiction and party posture
2. **Jurisdiction** — controlling court/forum and choice-of-law constraints
3. **Key facts** — chronology; label disputed, undisputed, and unknown facts
4. **Record sources** — pleadings, contracts, statutes, evidence, prior research
5. **Audience/purpose** — partner review, motion strategy, risk assessment, or settlement posture

## Memo Structure

| Section | Requirements |
|---|---|
| Heading | To / From / Date / Re / Jurisdiction; confidentiality note if needed |
| Question Presented | One legally precise sentence; frame for yes/no or short answer |
| Brief Answer | 2–4 sentences: likely outcome + key drivers |
| Facts | Objective summary; label disputed and missing facts |
| Discussion | IRAC per issue: Rule → Application → Counterarguments → Conclusion |
| Risk & Strategy | Likelihood ranges, exposure, procedural constraints, next steps |
| Conclusion | Direct answer + actionable recommendation |
| Appendix (optional) | Authority table, issue tree, or research log |

## Core Workflow

### 1. Research and validate authority

- Identify controlling statutes, regulations, and binding precedent.
- Capture persuasive authority when binding law is thin or split.
- Verify current validity (overruled, superseded, amended).
- Note jurisdictional splits or unresolved conflicts.
- Cite in Bluebook format throughout.

### 2. Draft Discussion using IRAC

For each issue:

- **Rule** — synthesize holdings from binding authority; note majority/minority positions.
- **Application** — apply rules to case facts; address each element.
- **Counterarguments** — present opposing interpretations; distinguish unfavorable authority.
- **Conclusion** — state likely outcome for this issue.

### 3. Assess risk

Use a likelihood table in Risk & Strategy:

| Outcome | Likelihood | Drivers |
|---|---|---|
| Strong for client | __%  | Elements met, controlling precedent, factual support |
| Mixed | __% | Fact-dependent, split authority |
| Adverse | __% | Unfavorable holdings, statutory barriers |

### 4. Build authority table (Appendix, if complex)

| Authority | Court/Level | Holding/Rule | Favorable? | Distinguishable? |
|---|---|---|---|---|

## Pitfalls

- **Advocacy creep** — maintain neutrality; do not use persuasive rhetoric.
- **Ignoring bad authority** — address unfavorable holdings directly and explain impact.
- **Unverified citations** — confirm every authority is current and correctly cited.
- **Fact/opinion blur** — clearly separate undisputed facts, disputed facts, and unknowns.
- **Scope drift** — default to U.S. law; flag non-U.S. issues as out of scope unless instructed otherwise.

Key changes from the original:
- **Removed `tags`** — not part of the Agent Skills spec; discovery relies on `description` keywords.
- **Tightened `description`** — third-person, clear trigger guidance, under 1024 chars.
- **Eliminated the full text template** — the Memo Structure table already defines every section; the verbatim template was redundant.
- **Consolidated research checklist into workflow** — folded validation steps into "Research and validate authority" instead of a standalone checklist.
- **Simplified authority table** — dropped the "Notes" column to reduce clutter; kept the essential columns.
- **Renamed Guidelines → Pitfalls** — reframed as named anti-patterns for faster scanning.
- **Reduced from 114 to ~62 lines** — roughly 45% token savings while preserving all domain-accurate legal content.
