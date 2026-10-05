# Agent Tier Under EU AI Act Cross-Link

The AI Act compliance doc tiers each feature: prohibited / high-risk / limited-risk / minimal-risk. For agent features, the tier is **shifted upward** when the agent has irreversible side-effects or makes decisions that affect a person's legal or significant interests.

## Tier triggers for agent features

| Trigger | Tier |
|---------|------|
| Agent autonomously executes irreversible actions affecting a person's contract, employment, credit, healthcare, education, or housing | High-risk |
| Agent autonomously executes irreversible actions in regulated sectors (finance, healthcare, legal) with consumer-facing impact | High-risk |
| Agent autonomously executes any irreversible action against the user's data with no per-call human approval | High-risk if regulated context; Limited-risk otherwise |
| Agent acts only via compensable or idempotent tools | Limited-risk |
| Agent only proposes (L0) | Minimal-risk |

## High-risk classification implications

For high-risk classified agent features:

1. Article 14 (human oversight) — operationalised by the irreversibility-gating ADR (`ADR-AGT-002`) and the human-final-decision principle in the responsible-AI addendum.
2. Article 13 (transparency) — operationalised by the agent user disclosure pack.
3. Article 9 (risk management) — operationalised by the agent SLO doc and the agent rollout runbook.
4. Article 10 (data governance) — cross-link to `09-governance-compliance/16-ai-data-flow-and-dpia`.
5. Article 12 (logging) — operationalised by the audit-log retention in `ADR-AGT-005`.

## US sectoral overlay

- Colorado AI Act 2026 — applies to "consequential" agent actions; treat as equivalent to EU high-risk for compliance purposes.
- NYC AEDT — agents used for employment-related decisions trigger bias audit publication.

## African DPA overlay

- Uganda DPPA — special-category processing by agents triggers DPIA via `dpia-generator`.
- Ghana / Nigeria — equivalent rules; cross-check per project.
