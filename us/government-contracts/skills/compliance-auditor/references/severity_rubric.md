# Severity Rubric — Detailed Examples

## Critical

Will cause Unacceptable rating or Compliance non-compliance:

- `shall` requirement with no satisfying `deliverable` or `performance_standard` (C3)
- Missing entire `evaluation_factor` coverage in the volumes (UCF Section M or equivalent)
- Cybersecurity cross-cut missing when CUI is in scope

## High

Likely to lower a technical score by ≥1 adjective:

- Orphan clauses (C1)
- Unresolved regulatory references (C2)
- Asymmetric proposal_instruction ↔ evaluation_factor coverage (C4 — UCF Section L↔M or non-UCF equivalent)
- Cybersecurity cross-cut partial (C6)

## Medium

Should fix during pink/red review:

- Missing compliance artifact references (C5)
- Loose amendments not linked to base (C7)
- Past performance not mapped to factor (C8)

## Low

Polish only:

- Typos in clause IDs that the coercion handled
- Empty `description` fields on entities
- Inconsistent capitalization of factor names

## Info

Observed pattern, no action:

- Multiple `RELATED_TO` fallbacks within a single document section (signal that future inference may help)
