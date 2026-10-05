---
name: 27-ai-agent-regulator-overlap-mapping-peterbamuhigire
title: AI Agent Regulator Overlap Mapping Skill
description: Use when crosswalking AI-agent controls and evidence across two or more regulatory or assurance regimes while exposing divergent obligations. Use each regime's control pack for authoritative detail and evidence-pack-spec for handling requirements.
author: peterbamuhigire
author_url: https://github.com/peterbamuhigire/chwezi-sdlc-documentation/tree/main/09-governance-compliance/27-ai-agent-regulator-overlap-mapping
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
sources:
- title: Ai Agent Regulator Overlap Matrix
  path: references/ai-agent-regulator-overlap-matrix.md
---

# AI Agent Regulator Overlap Mapping Skill

<!-- dual-compat-start -->

## Use When

- Use when crosswalking AI-agent controls and evidence across two or more regulatory or assurance regimes while exposing divergent obligations. Use each regime's control pack for authoritative detail and evidence-pack-spec for handling requirements.

## Do Not Use When

- Do not use as the sole reference for any one regime — use it alongside the per-regime control pack. Do not treat the overlap as automatic; gaps shall be identified explicitly per row.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md, AI_Agent_HIPAA_Control_Pack.md, AI_Act_And_Regulatory_Compliance_Doc.md, NIST AI RMF mapping, AI_Data_Flow_And_DPIA.md, BAA/DPA addendum templates, regional regulator guidance documents (KE ODPC AI guidance 2024; NG NDPC advisory 2024; ZA POPIA s.71; UG DPPA 2019; RW DP Law 2021). | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Execute only non-mutating validation when authorised; editing remediation, publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Required evidence is missing or inaccessible | Mark the check not assessed, state impact, and stop any pass decision | False assurance from an incomplete review |
| Evidence supports the stated criterion | Record the finding and traceable rationale without mutating sources | Unrepeatable review conclusions |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Agent Regulator Overlap Mapping | Accountable reviewer, control owner, auditor, or release authority | Every control area shall map to every applicable regime. Shared-evidence cells shall name the evidence artefact. Divergent-evidence cells shall name the additional requirement. EU AI Act high-risk and prohibited classifications shall be cross-linked. Updates triggered by framework change shall be timestamped. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent Regulator Overlap Mapping evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every control area shall map to every applicable regime. Shared-evidence cells shall name the evidence artefact. Divergent-evidence cells shall name the additional requirement. EU AI Act high-risk and prohibited classifications shall be cross-linked. Updates triggered by framework change shall be timestamped.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent Regulator Overlap Mapping from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if required evidence is missing or inaccessible, mark the check not assessed, state impact, and stop any pass decision. Record the evidence and result in the validation record; this avoids false assurance from an incomplete review.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

A single audit-log retention configuration can satisfy SOC 2 CC7.2, ISO 27001 A.8.15, HIPAA §164.312(b), EU AI Act Art. 12, and NIST AI RMF MEASURE-3. The auditor wants to know which evidence is shared, which is unique, and where regimes diverge. This skill produces the crosswalk.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | SOC 2 / ISO / HIPAA control packs, AI Act doc, NIST AI RMF mapping, DPIA, BAA/DPA templates, regional regulator guidance |
| **Output** | `AI_Agent_Regulator_Overlap_Mapping.md` + `AI_Agent_Regulator_Overlap_Matrix.md` |
| **Standards** | All listed regimes |

## Core Instructions

### Step 1: Regimes in scope

- **SOC 2** (AICPA TSP 100; TSC 2017 / 2022 revisions).
- **ISO/IEC 27001:2022** + ISO/IEC 42001:2023 overlay.
- **HIPAA Security Rule** (45 CFR §164.302–§164.318) + Breach Notification (§164.400–§164.414).
- **EU AI Act** (Regulation 2024/1689).
- **NIST AI RMF 1.0** (2023) and updates.
- **Kenya DPA 2019** + ODPC AI guidance (2024).
- **Nigeria NDP Act 2023** + NDPC AI advisory (2024).
- **South Africa POPIA 2013** + Information Regulator guidance.
- **Uganda DPPA 2019**.
- **Rwanda DP Law 2021**.

### Step 2: Canonical control areas

| Area | Description |
|------|-------------|
| Action governance | What actions an agent may perform; authorisation model |
| Audit logging | Record-keeping for tool calls and approval events |
| Audit-log integrity | Tamper-evidence (hash-chain, WORM) |
| Access control | Identity, scope, least privilege |
| Approval and supervision | Human-in-the-loop placement |
| Kill-switch and containment | Emergency stop; force-pause |
| Incident management | Detection, response, postmortem |
| Breach notification | Timeline, recipient, content |
| Sub-processor management | Disclosure, change notice |
| Data subject rights | Access, erasure, objection, explanation |
| Transparency and disclosure | User/tenant disclosure of agent involvement |
| Cross-border transfer | Mechanism per direction |
| DPIA / impact assessment | When required; assistance |
| Bias and protected-class outcomes | Review cadence; remediation |
| Training-data exclusion | Provider commitment; evidence |
| Memory and erasure | Tiered memory; erasure SLA |
| Red-team and adversarial testing | Cadence; severity |
| Change management | CAB; ADR; gate |
| Monitoring and SLI | Burn-rate alerts; intervention |
| Documentation retention | Years per regime |

### Step 3: For each area, map to each regime

For each (area × regime) cell:

- The specific clause / criterion / standard ID.
- The shared evidence artefact (if any) — name and frequency.
- Divergent evidence required — name and rationale.
- Risk if the area is treated as fully overlapping without divergent evidence.

Produce the matrix in `references/ai-agent-regulator-overlap-matrix.md`.

### Step 4: Identify EU AI Act tier per feature

Cross-link the EU AI Act classification from `ai-act-and-regulatory-compliance-doc`:

- Prohibited (Art. 5) — block.
- High-risk (Annex III) — full Annex IV technical documentation, conformity assessment, post-market monitoring, registration.
- Limited-risk (Art. 50) — transparency obligations.
- Minimal-risk — voluntary codes.

Per area declare additional AI Act obligations.

### Step 5: One-evidence-multiple-regimes reuse table

Produce a concrete reuse table:

| Evidence artefact | SOC 2 | ISO | HIPAA | EU AI Act | NIST | KE | NG | ZA | UG | RW |
|---------------------|--------|-----|--------|------------|------|-----|-----|-----|-----|-----|
| Hash-chain integrity report | CC7.2, PI1.4 | A.8.15, A.8.24 | 164.312.b, .c | Art. 12 | MEASURE-3 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Kill-switch drill report | CC7.4, A1.3 | A.5.30 | 164.308.a.7 | n/a (operational) | MANAGE | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Approval event sample | CC5.1, PI1.4 | A.5.15, A.8.2 | 164.312.d | Art. 14 | MEASURE | s.40 | Art. 29 | s.71 | s.24 | Art. 26 |
| DPIA addendum | P3 | A.5.34 | 164.502 | Art. 27 | MAP | s.31 | Art. 28 | s.71 | s.21 | Art. 22 |
| Sub-processor list + change log | CC9.1, P6 | A.5.19, A.5.20 | 164.308.b.1 | (provider chain) | GOVERN | s.40 | Art. 29 | s.20 | s.24 | Art. 26 |

### Step 6: Write the mapping doc

`AI_Agent_Regulator_Overlap_Mapping.md` sections: 1) Regimes in Scope, 2) Canonical Control Areas, 3) Per-area Regime Crosswalk, 4) EU AI Act Tier per Feature, 5) Evidence Reuse Table, 6) Divergent Evidence Required per Regime, 7) Update Triggers, 8) Sign-off.

## Standards

- All regimes listed in Step 1.

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-regulator-overlap-matrix.md`.
