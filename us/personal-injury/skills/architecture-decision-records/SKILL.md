---
name: architecture-decision-records
title: Architecture Decision Records
description: Record architectural decisions as ADRs in FirmVault/decisions/. Cherry-picked from stirps-ai/stirps-gov. Use when making significant design choices that affect the PHASE_DAG, workflow system, agent architecture, or data contracts. Each ADR cites wiki evidence and has testable failure criteria.
author: Whaleylaw
author_url: https://github.com/Whaleylaw/Roscoe-hermes/tree/main/roscoe-state/skills/domain/architecture-decision-records
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [adr, governance, architecture, firmvault, stirps, decisions]
---

# Architecture Decision Records

## When to Use

- Making any change to PHASE_DAG, DATA_CONTRACT, or DESIGN.md
- Resolving contradictions found in wiki audits
- Adding new parallel tracks, variant workflows, or phase transitions
- Choosing between architectural alternatives with real tradeoffs
- When you need to explain WHY a decision was made, not just WHAT

## Origin

Cherry-picked from [stirps-ai/stirps-gov](https://github.com/stirps-ai/stirps-gov):
- Took: ADR practice, immutable decision records, wiki-evidence citation
- Skipped: Full governance framework (4 cognitive modes, session model, map/territory split)
- Rationale: ADRs add accountability with minimal ceremony. The full Stirps
  framework is too much overhead for a solo builder with autonomous agents.

## ADR Template

Located at `/opt/data/FirmVault/decisions/_template.md`. Key sections:

1. **Status** — Proposed | Accepted | Superseded
2. **Context** — Why a decision is needed. Cite wiki evidence with article
   slugs and evidence counts.
3. **Decision** — Declarative statement of what was decided.
4. **Options Considered** — What alternatives existed and why they were rejected.
5. **Consequences** — What changes, what becomes possible, what constraints.
6. **Failure Criteria** — Specific, testable signals that the decision is wrong.
7. **Definition of Done** — Mechanically verifiable checklist.

## Rules

1. **ADRs are immutable.** Never edit a committed ADR. If a decision changes,
   create a new ADR that supersedes the original.
2. **Cite wiki evidence.** Every ADR should reference wiki articles with
   evidence counts: `[[slug]] (N cases, confidence)`. This connects decisions
   to observed reality, not assumptions.
3. **Include failure criteria.** If you can't name a testable condition under
   which the decision would be wrong, the decision isn't specific enough.
4. **Sequential numbering.** ADR-000, ADR-001, etc. Check existing files
   before creating to avoid collisions.
5. **Aaron approves.** All ADRs start as Proposed. Aaron marks Accepted.

## Existing ADRs (as of 2026-04-12)

| ADR | Title | Status | Key Evidence |
|-----|-------|--------|-------------|
| 000 | Record architectural decisions | Accepted | Meta — wiki audit found 6 undocumented contradictions |
| 001 | Parallel tracks replace linear phases | Proposed | lien-mgmt (122), pip (142), litigation-settles (74%) |
| 002 | Decline from any phase | Proposed | outcome-dist (51% decline), unreachable (49% MIA) |
| 003 | Records sufficient replaces all received | Proposed | records-gates-demand (45% conversion) |
| 004 | Client contactability system-wide track | Proposed | unreachable (49%), predicts-decline (55%) |
| 005 | Variant workflows for case types | Proposed | minor (29), WC (Form 110), KAC (26%), UIM |
| 006 | Closed is wind-down not terminal | Proposed | post-closing obligations, reopen cycles |

## Workflow: Wiki Audit → ADRs

This is the process that produced ADR-001 through ADR-006:

1. **Compile wiki** from case activity logs (see law-firm-wiki-compiler skill)
2. **Read PHASE_DAG.yaml** — the prescribed workflow
3. **Read all wiki articles** — the observed reality
4. **Write audit report** comparing prescribed vs observed:
   - Contradictions (DAG says X, wiki shows Y)
   - Gaps (real patterns not in DAG)
   - Redundancies (overlapping articles/concepts)
5. **Save to** `wiki/reports/workflow-vs-wiki-audit.md`
6. **Draft proposals** for each significant finding
7. **Write ADRs** for each decision, citing wiki evidence
8. **Save to** `FirmVault/decisions/ADR-NNN-slug.md`
9. **Get Aaron's approval** — Proposed → Accepted

## Files

- Template: `/opt/data/FirmVault/decisions/_template.md`
- Decisions: `/opt/data/FirmVault/decisions/ADR-*.md`
- Audit report: `/opt/data/FirmVault/wiki/reports/workflow-vs-wiki-audit.md`
- PHASE_DAG v2 proposal: `/opt/data/FirmVault/wiki/reports/PHASE_DAG_v2_proposal.md`
- Stirps reference: https://github.com/stirps-ai/stirps-gov

## Pitfalls

1. **Don't over-ADR.** Not every config change needs an ADR. Reserve for
   decisions that affect workflow structure, agent architecture, or data contracts.
2. **Don't fabricate alternatives.** If a retroactive ADR documents a decision
   already made, be honest that alternatives weren't formally evaluated.
3. **Evidence counts drift.** Wiki evidence counts change as more cases are
   compiled. Cite the count at time of writing — don't update old ADRs.
4. **ADRs are not specs.** They record WHY, not HOW. The PHASE_DAG yaml
   is the spec; the ADR explains why it looks that way.
