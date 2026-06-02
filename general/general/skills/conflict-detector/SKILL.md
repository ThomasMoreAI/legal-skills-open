---
name: conflict-detector
title: Conflict Detector
description: Detect legal-source conflicts across definitions, scope, obligations, sanctions, and recency, then produce structured conflict reports.
author: kipeum86
author_url: https://github.com/kipeum86/game-legal-research/tree/main/.claude/skills/conflict-detector
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Conflict Detector

Use this skill during Step 6 when conflicts appear.

## Conflict Types

1. Definitional conflict
2. Scope conflict
3. Obligation conflict
4. Enforcement/sanction conflict
5. Recency conflict

## Output

Use `references/conflict-report-template.md`.

Resolution priority:
1. Legal hierarchy
2. Jurisdictional relevance
3. Recency
4. Original-text support

Before marking a conflict resolved or unresolved, apply the deterministic helper in
`citation_auditor.conflict_resolution`:

```python
from citation_auditor.conflict_resolution import resolve_conflict

resolution = resolve_conflict(claim_a, claim_b, sources, target_jurisdictions, profile="general")
```

- If `resolution.outcome == "resolved"`, use `preferred_source_id` in the conflict
  report and include the helper's top rationale in `provisional_resolution`.
- If `resolution.outcome == "unresolved"`, keep the conflict tagged
  `[Unresolved Conflict]` and record the score delta/rationale in
  `residual_uncertainty`.
- Do not override the helper with narrative intuition unless a jurisdiction-specific
  legal rule is cited from a primary source; if that happens, record the rule and
  source id in the conflict report.

Use a matter-specific `profile` when the conflict fits one of these patterns:

| Profile | Use When |
|---|---|
| `eu-member-state` | EU regulation/case law conflicts with member-state source, agency guidance, or implementation material |
| `us-federal-state` | US federal and state sources may conflict, especially where preemption is raised |
| `kr-delegated-regulation` | Korean statute, delegated regulation, ordinance, and agency guidance hierarchy matters |
| `agency-guidance` | Agency guidance or FAQ appears to conflict with statute, regulation, or case law |

If none fits cleanly, keep `profile="general"` and mark close-score results
`[Unresolved Conflict]`.

## Severity Handling

- High severity (obligation/sanction): attempt source expansion first.
- Low severity (definition/recency): mark `[Unresolved Conflict]` when unresolved.

## Persistence — `output/unresolved-conflicts.json`

When a conflict is marked `[Unresolved Conflict]` (i.e., it cannot be resolved after
applying the resolution-priority rules and any source-expansion attempt), write a record
to `output/unresolved-conflicts.json`.

### Entry Schema

```json
{
  "conflict_id": "CF-001",
  "first_detected": "2026-03-05",
  "last_seen": "2026-03-05",
  "times_encountered": 1,
  "type": "obligation",
  "severity": "high",
  "jurisdictions_involved": ["NL", "AU"],
  "domains_involved": [1],
  "description": "Conflicting obligations on loot-box disclosure between NL KSA ruling and AU ACCC guidance",
  "claim_a": {
    "summary": "NL: loot boxes are games of chance requiring full odds disclosure",
    "source_id": "NL-A1",
    "citation": "[A1] KSA, Decision 2024-07-01, p. 12",
    "grade": "A"
  },
  "claim_b": {
    "summary": "AU: loot boxes are not gambling under Qld Racing Act s. 4",
    "source_id": "AU-P2",
    "citation": "[P2] Queensland Racing Act 2002, s. 4",
    "grade": "A"
  },
  "resolution_attempted": true,
  "resolution_outcome": "unresolved",
  "residual_uncertainty": "Whether AU federal law may impose separate disclosure requirements",
  "next_steps": "Check Australian Consumer Law Schedule 2, Competition and Consumer Act 2010",
  "status": "open"
}
```

### Write Rules

1. Before writing, check if an entry with the same `jurisdictions_involved` + `domains_involved`
   + `type` already exists in the file.
   - **Duplicate found:** update `last_seen` and increment `times_encountered`. Do not
     create a new entry.
   - **No duplicate:** append a new entry.

2. Set `status` to `"open"` when first written. Change to `"resolved"` only when a
   subsequent research session provides a definitive primary-source resolution.

3. Update `output/unresolved-conflicts.json` immediately when the conflict is detected —
   do not wait until Step 9.

### Read Rules (at session start)

When the main agent loads this file at session start:
- Surface any `"open"` entries whose `jurisdictions_involved` and `domains_involved`
  overlap with the current query's scope.
- Prepend a brief note in the Step 6 analysis output:
  *"Note: {N} pre-existing unresolved conflict(s) from prior sessions are relevant to
  this query. See conflict IDs: {list}. These are included in the analysis below."*
