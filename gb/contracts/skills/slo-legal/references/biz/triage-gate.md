---
name: triage-gate
created: 2026-04-25
status: stable-interface
audience: every advisor skill in the biz pack (`/slo-legal`, `/slo-accounting`, `/slo-equity`, `/slo-fundraise`)
purpose: |
  Single source of truth for the four hard-block predicates that every advisor skill cites.
  Adding a fifth predicate is a `/slo-architect` decision, not a per-milestone option.
  Predicate IDs are stable interface — renaming or removing one breaks the cross-skill citation contract enforced by `crates/sldo-install/tests/e2e_biz_a_m2.rs`.
---

# Triage gate — hard-block predicates for advisor skills

Every advisor skill (`/slo-legal`, `/slo-accounting`, `/slo-equity`, `/slo-fundraise`) reads this file and applies the four predicates BEFORE entering `draft` mode. If any predicate is true, the skill MUST refuse to draft and route to `triage` with the appropriate professional (lawyer / accountant / DPO / accountant + lawyer).

Predicate evaluation is the LLM's responsibility — these are natural-language tests that the skill applies to the founder's stated situation. The fingerprint of "did the gate fire?" goes into every drafted artifact's `triage_gate_passed: bool` frontmatter; firing routes to the `triage` mode output instead.

## The four predicates

| id | name | predicate | if_true | route_to | rationale_doc |
|---|---|---|---|---|---|
| `gate-1-regulated` | Regulated domain | Is the matter touching FCA, MHRA, ICO, healthcare, financial services, or any other regulator with statutory enforcement powers over the founder or their counterparty? | `route_to_triage` | `lawyer` | `references/biz/jurisdiction-uk.md` (M2 — list of UK regulators in scope) |
| `gate-2-deal-value-over-5k` | Deal value above threshold | Is the deal value, contract value, or annual value of the engagement greater than £5,000 (GBP, exclusive of VAT)? | `route_to_triage` | `lawyer` | `references/biz/cost-baseline-jpp-law-2026.md` (the threshold tracks roughly half the cost of the cheapest fixed-fee solicitor engagement; see provenance) |
| `gate-3-counterparty-has-lawyer-or-their-paper` | Counterparty has a lawyer OR founder is signing their paper | Is the counterparty represented by a lawyer in this matter, OR is the founder being asked to sign a contract drafted by the counterparty (rather than send their own)? | `route_to_triage` | `lawyer` | none (operational principle: defending interests is harder than asserting them) |
| `gate-4-gdpr-document` | GDPR-related document | Does the requested artifact relate to GDPR / UK GDPR — privacy notice, ROPA (record of processing activities), DPA (data processing agreement), internal data-protection policy, lawful-basis statement, DPIA (data protection impact assessment), DSAR (data subject access request) procedure, breach-notification template, or any other document the ICO would expect to see in a controller's accountability file? | `route_to_triage` | `dpo` (or `lawyer + dpo` if no DPO) | `references/biz/ico-duaa-index.md` (M2 — DUAA 2025 commencement + lawful-basis examples), `references/biz/ico-enforcement-reality.md` (M2 — descriptive provenance for the broad block) |

## Locked decisions (referenced by the predicates above)

- **GDPR broad hard-block on `draft` (locked 2026-04-25).** `gate-4-gdpr-document` is unconditional refusal of `draft` mode for ANY GDPR-related document. Translate and triage are permitted. Defensible on professional-negligence + upside-asymmetry grounds; the £17.5M PECR ceiling under DUAA 2025 (Stage 3 commenced 5 February 2026) makes the tail unbounded even though sub-£1M-turnover-private-company enforcement clusters at PECR direct marketing rather than Article 13. Reversal requires a fresh `/slo-architect` pass with new ICO enforcement evidence.
- **Deal-value threshold £5,000 (locked 2026-04-25).** Deliberately conservative for a UK seed-stage founder. The threshold is a single number, not a complexity score — borderline cases (£4,800 + complex IP scope, £6,200 + simple month-to-month NDA) should be evaluated alongside the other three predicates. If gate-2 passes (under £5,000) but gate-1 or gate-3 fires, the skill still routes to `triage`.

## Predicate firing — what the artifact looks like

When a predicate fires, the skill MUST:

1. Refuse to enter `draft` mode for the requested artifact.
2. Produce a `triage`-mode artifact instead at `docs/biz-public/<area>/triage-<slug>-<date>.md`.
3. Frontmatter MUST carry `triage_gate_passed: false` and a `gates_fired:` list naming every predicate that fired (e.g., `gates_fired: [gate-2-deal-value-over-5k, gate-3-counterparty-has-lawyer-or-their-paper]`).
4. Body MUST cite each fired predicate by ID and quote the predicate text.
5. Body MUST include a "what to bring to your [lawyer / accountant / DPO]" briefing checklist tailored to the founder's situation.
6. Body MUST cite `cost_baseline_ref: references/biz/cost-baseline-jpp-law-2026.md@<retrieval-date>` in the frontmatter even though no draft was produced (so the founder sees the cost-of-this-being-a-real-engagement number).

## What this file is NOT

- This file is NOT executable code. The predicate-id strings are read by `/slo-critique` and structural-contract tests as Markdown prose, never spliced into shell, never invoked as subprocess names.
- This file is NOT a complete decision tree for whether to engage a professional. It is the floor: every advisor skill applies AT LEAST these four predicates. Skills MAY add domain-specific additional checks in their own SKILL.md prose (e.g., `/slo-fundraise` adds an SEIS/EIS Advance Assurance check; that is skill-specific, not a fifth predicate here).
- This file is NOT authorization to relax any predicate. Advisor SKILL.md prose may make a predicate's wording more concrete for that domain, but cannot override the routing or refuse-to-draft semantics.
- This file is NOT a substitute for `SECURITY.md` (root) or the threat model. It is the operational source-of-truth for the gates; `SECURITY.md` documents project-wide rules and the threat model documents abuse cases.

## Change-control discipline

Adding a fifth predicate, removing a predicate, or renaming a predicate ID requires:

1. A fresh `/slo-architect` pass against new evidence (typically a research dossier or an incident retrospective).
2. Update of `docs/slo/design/biz-skill-pack-{overview,interfaces,threat-model}.md`.
3. Update of every advisor skill's SKILL.md to cite the new / renamed predicate.
4. Update of `crates/sldo-install/tests/e2e_biz_a_m2.rs` (cross-skill citation test) to expect the new predicate-id set.
5. Migration entry in `docs/slo/completed/RUNBOOK-BIZ-SKILL-PACK-A.md` (or the runbook performing the change).
6. `/slo-critique` security persona review of the change before it merges.

The structural-contract test `triage_gate_predicate_set_unchanged_from_m1` in `e2e_biz_a_m2.rs` is the immutability enforcement mechanism. It asserts the predicate-id set is exactly `{gate-1-regulated, gate-2-deal-value-over-5k, gate-3-counterparty-has-lawyer-or-their-paper, gate-4-gdpr-document}`.
