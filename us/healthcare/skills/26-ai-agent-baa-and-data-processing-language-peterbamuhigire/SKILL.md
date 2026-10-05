---
name: 26-ai-agent-baa-and-data-processing-language-peterbamuhigire
title: AI Agent BAA and Data-Processing Language Skill
description: Use when drafting legal-review-ready AI-agent BAA or DPA addendum clauses for service-principal access, audit logs, kill switch, memory, subprocessors, training exclusion, breach, and transfers. Use HIPAA control pack for controls and privacy-doc-set for the parent set.
author: peterbamuhigire
author_url: https://github.com/peterbamuhigire/chwezi-sdlc-documentation/tree/main/09-governance-compliance/26-ai-agent-baa-and-data-processing-language
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
sources:
- title: Ai Agent Baa Template
  path: references/ai-agent-baa-template.md
- title: Ai Agent Dpa Template
  path: references/ai-agent-dpa-template.md
---

# AI Agent BAA and Data-Processing Language Skill

<!-- dual-compat-start -->

## Use When

- Use when drafting legal-review-ready AI-agent BAA or DPA addendum clauses for service-principal access, audit logs, kill switch, memory, subprocessors, training exclusion, breach, and transfers. Use HIPAA control pack for controls and privacy-doc-set for the parent set.

## Do Not Use When

- Do not use as a substitute for legal review — these are drop-in templates that the parent BAA / DPA owner adapts. Do not use unedited; the legal team shall review.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: Parent BAA template, parent DPA template, AI Agent Architecture Spec, Action Catalogue Spec, AI Agent Responsible-AI Addendum, AI Agent Compliance Policy Pack, AI Agent SLO Doc, AI Agent Runbook, AI Data Flow + DPIA, AI HIPAA Control Pack (if PHI in scope), sub-processor list. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Lawful basis, jurisdiction, data flow, or legal owner is unverified | Stop publication or signature and request legal/privacy review | Invalid privacy or contract claim |
| Residual high risk remains after controls | Escalate to the accountable authority; do not self-certify | Unauthorised risk acceptance |

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
| AI Agent BAA and Data-Processing Language | Accountable reviewer, control owner, auditor, or release authority | Every drop-in clause shall be self-contained, referenced to a control in the relevant control pack, and signable as an addendum. Cross-jurisdiction language shall name the transfer mechanism. Breach notification clauses shall name the timeline and the recipient. Sub-processor change clauses shall name the notice period. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent BAA and Data-Processing Language evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every drop-in clause shall be self-contained, referenced to a control in the relevant control pack, and signable as an addendum. Cross-jurisdiction language shall name the transfer mechanism. Breach notification clauses shall name the timeline and the recipient. Sub-processor change clauses shall name the notice period.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent BAA and Data-Processing Language from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if lawful basis, jurisdiction, data flow, or legal owner is unverified, stop publication or signature and request legal/privacy review. Record the evidence and result in the validation record; this avoids invalid privacy or contract claim.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

Two drop-in contract addenda for agent processing:

- **BAA Addendum** — extends the parent Business Associate Agreement with agent-specific obligations under HIPAA §164.504(e).
- **DPA Addendum** — extends the parent Data Processing Agreement with agent-specific obligations under GDPR Art. 28 and the African DPA regimes (Kenya DPA s.40; Nigeria NDP Act 2023 Art. 29; South Africa POPIA s.21; Uganda DPPA 2019 s.24; Rwanda DP Law 2021 Art. 25).

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Parent BAA, parent DPA, Agent Architecture, Action Catalogue, Responsible-AI Addendum, Policy Pack, SLO, Runbook, DPIA, HIPAA control pack (if applicable), sub-processor list |
| **Output** | `AI_Agent_BAA_Addendum.md`, `AI_Agent_DPA_Addendum.md`, per-region annexes |
| **Standards** | HIPAA §164.504(e); GDPR Art. 28; KE DPA 2019 s.40; NDP Act 2023 Art. 29; POPIA s.21; UG DPPA 2019 s.24; RW DP Law 2021 Art. 25 |

## Core Instructions

### Step 1: Identify the regulatory regime

For each tenant determine: HIPAA (covered entity in US healthcare); GDPR (EU/EEA/UK data subjects); KE DPA; NG NDPR / NDP Act; ZA POPIA; UG DPPA; RW DP Law; combinations.

### Step 2: Common agent-distinctive obligations

Across all regimes, the addenda shall cover:

1. **Agent service-principal access** — the agent is a named service principal scoped to the tenant; least privilege; quarterly access review.
2. **Reversibility and approval** — irreversible-class tool calls require human approval; signed event.
3. **Audit-log retention** — per the retention table; hash-chain integrity; tenant audit export on request.
4. **Kill-switch SLA** — propagation ≤ 5 s; per-tenant kill-switch available to tenant admin and processor on-call.
5. **Memory erasure** — tenant-controlled memory tier opt-in; erasure on request within 30 days; certificate of erasure.
6. **Sub-processor change** — 30-day notice for material change to model provider or other sub-processor; right to object.
7. **Training-data exclusion** — provider commitment that tenant data does not train provider models; evidence available on request.
8. **Breach notification** — timeline per regime (HIPAA ≤ 60 days; GDPR ≤ 72 hours to controller).
9. **Cross-jurisdiction transfers** — named transfer mechanism (DPF / SCCs + TIA / adequacy / data-residency).
10. **In-product disclosure** — tenant-admin and end-user agent disclosure shown in product.

### Step 3: HIPAA BAA addendum

Map obligations 1-10 onto §164.504(e) language. Key HIPAA-specific clauses:

- **Limit on use and disclosure** — agent shall not use or disclose PHI other than as permitted or required for the engagement or required by law.
- **Safeguards** — agent service-principal least privilege; audit controls per §164.312(b); integrity per §164.312(c)(1).
- **Reporting** — breach notification ≤ 60 days; immediate to covered entity for ≥ 500 individuals; cooperation with HHS investigation.
- **Subcontractors** — model provider executes BAA or PHI is de-identified before model call; sub-processor change notice.
- **Access by individual** — DSAR-equivalent process; agent memory and action history included.
- **Amendment** — covered entity right to amend; agent compliance with amendments.
- **Accounting of disclosures** — agent action audit log supports accounting per §164.528.
- **Return or destruction at termination** — agent memory tier returned or destroyed; certificate of destruction.

### Step 4: GDPR DPA addendum

Map obligations 1-10 onto Art. 28 language. Key GDPR-specific clauses:

- **Documented instructions** — agent processing limited to documented instructions in the parent DPA plus this addendum.
- **Confidentiality** — agent operators and supervisors subject to confidentiality obligations.
- **Security** — Art. 32 measures including encryption, integrity, availability, regular testing.
- **Sub-processors** — Art. 28(2) general written authorisation plus 30-day notice for new sub-processors; right to object.
- **Data subject rights** — controller assistance under Arts. 12-22 including erasure of agent memory.
- **Breach notification** — ≤ 72 hours to controller per Art. 33.
- **DPIA assistance** — Art. 35 assistance; cross-link to AI Data Flow + DPIA.
- **Audit rights** — controller right to audit; processor right to provide SOC 2 / ISO certifications in lieu of audit (with caveat).
- **International transfers** — DPF where applicable; SCCs + TIA + supplementary measures otherwise.
- **Deletion at termination** — agent memory and action history deletion or return.

### Step 5: African DPA annexes

| Regime | Specifics |
|--------|-----------|
| Kenya DPA 2019 | Data Commissioner notification per s.43; data residency expectation; ODPC AI guidance overlay (2024); cross-border transfer per s.49 |
| Nigeria NDP Act 2023 | NDPC notification; lawful basis under Art. 25; cross-border under Schedule; NDPC AI advisory overlay |
| South Africa POPIA | Information Regulator notification; s.71 automated decision-making protections (right to object, right to explanation); cross-border under s.72 |
| Uganda DPPA 2019 | PDPO notification per s.23; immediate breach notification standard; data residency considerations |
| Rwanda DP Law 2021 | NCSA notification; cross-border under Art. 48 |

### Step 6: Cross-jurisdiction transfer mechanisms

Declare per direction:

- EU → US: DPF certified; SCCs Module 2 with TIA and supplementary measures fallback.
- EU → KE / NG / ZA: SCCs + adequacy assessment.
- US → EU: GDPR-compliant processor language.
- Intra-Africa: per bilateral adequacy where present; SCCs + adequacy assessment otherwise.

### Step 7: Signature blocks

Per addendum: tenant authorised signatory + processor authorised signatory + effective date + version. Counter-signature on amendments.

### Step 8: Write the addenda

`AI_Agent_BAA_Addendum.md`: sections 1-10 plus signature block.
`AI_Agent_DPA_Addendum.md`: sections 1-10 plus signature block.
`annexes/<region>.md`: per-region annex with the specifics from Step 5.

## Standards

- HIPAA §164.504(e); §164.314
- GDPR Art. 28; Art. 32-36
- Kenya DPA 2019 s.40, s.43, s.49
- Nigeria NDP Act 2023 Art. 28-29; Schedule
- South Africa POPIA s.21, s.71, s.72
- Uganda DPPA 2019 s.23, s.24
- Rwanda DP Law 2021 Art. 25, Art. 48
- EU SCCs (Commission Implementing Decision 2021/914)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-baa-template.md`, `references/ai-agent-dpa-template.md`.
