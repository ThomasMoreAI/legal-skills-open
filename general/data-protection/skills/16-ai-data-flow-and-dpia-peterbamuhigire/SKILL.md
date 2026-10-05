---
name: 16-ai-data-flow-and-dpia-peterbamuhigire
title: AI Data-Flow and DPIA Skill
description: Use when mapping AI data flows and assessing privacy necessity, lawful basis, risks, controls, residual risk, and consultation triggers. Use DPA/privacy-doc-set for contractual documents and responsible-ai-declaration for broader AI governance.
author: peterbamuhigire
author_url: https://github.com/peterbamuhigire/chwezi-sdlc-documentation/tree/main/09-governance-compliance/16-ai-data-flow-and-dpia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
sources:
- title: Ai Agent Tool Call Data Flow Crosslink
  path: references/ai-agent-tool-call-data-flow-crosslink.md
- title: Ai Data Flow Diagram Conventions
  path: references/ai-data-flow-diagram-conventions.md
- title: Ai Dpia Addendum Template
  path: references/ai-dpia-addendum-template.md
---

# AI Data-Flow and DPIA Skill

<!-- dual-compat-start -->

## Use When

- Use when mapping AI data flows and assessing privacy necessity, lawful basis, risks, controls, residual risk, and consultation triggers. Use DPA/privacy-doc-set for contractual documents and responsible-ai-declaration for broader AI governance.

## Do Not Use When

- Do not use for AI features that demonstrably process no personal data.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Feature_PRD_Spec.md, AI_Data_And_Knowledge_Base_Spec.md, DPA, sub-processor list, Multi_Tenancy_Architecture_Spec.md, base DPIA (if exists). | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| AI Data-Flow and DPIA | Accountable reviewer, control owner, auditor, or release authority | Every data flow shall name source, sink, classification, transfer mechanism, training-exclusion verdict, retention. Every processor shall have a contract reference. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Data-Flow and DPIA evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every data flow shall name source, sink, classification, transfer mechanism, training-exclusion verdict, retention. Every processor shall have a contract reference.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Data-Flow and DPIA from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

## Core Instructions

### Step 1: Inventory data flows

For each AI feature trace every data flow:

- User -> our service.
- Our service -> retrieval store.
- Our service -> model gateway.
- Model gateway -> model provider.
- Model provider -> response back through gateway.
- Gateway -> conversation log.
- Gateway -> billing-event store.
- Eval pipeline -> judge-LLM provider.
- Red-team -> separate set.

For each flow capture: source, sink, data classes, classification, transfer mechanism (TLS + signed claim), training-exclusion verdict, retention.

### Step 2: Data-flow diagram

Draw the diagram per `references/ai-data-flow-diagram-conventions.md`. Tenant boundary, organisation boundary, jurisdiction boundary, processor boundary. Use distinct symbols for personal data, sensitive personal data, and aggregate / anonymised.

### Step 3: AI DPIA addendum

Augment the base DPIA (if exists) or write standalone. Sections:

- Nature, scope, context, purpose of the AI processing.
- Lawful basis (per GDPR Art. 6 + Art. 9 where applicable).
- Necessity and proportionality assessment.
- Risks to data subjects (with AI-specific risks: opacity, hallucination, automated decisions, retraining drift, prompt-injection leak).
- Measures to address risks (eval harness, red-team, abstain rule, human-in-the-loop, isolation, encryption).
- Residual risk.
- Consultation if residual risk remains high (Art. 36).

### Step 4: Consent capture

For features requiring consent (regulated regions, generative features, high-risk), state where and how consent is captured, the lawful-basis fallback, and the revocation flow.

### Step 5: Training-data exclusion evidence

Per provider: contract clause reference, technical endpoint flag, audit cadence, audit date.

### Step 6: Cross-border transfer mechanism

EU -> US: Adequacy Decision (DPF) or SCCs + transfer impact assessment + supplementary measures. Kenya: data-residency commitment + DPA s.49. Nigeria: NDP Act 2023 Schedule. South Africa: POPIA s.72.

### Step 7: AI-specific risk register

Augment the base risk register:

- Hallucination affecting data subjects (incorrect data attributed to a person).
- Prompt-injection leading to disclosure.
- Cross-tenant retrieval leak.
- Model provider sub-processor change without sufficient notice.
- Training-data exclusion lapse (provider changes terms).
- Conversation log surfacing PII unintentionally.

### Step 8: Write the doc

`AI_Data_Flow_And_DPIA.md` sections: 1) Data Flow Inventory, 2) Data-Flow Diagram, 3) AI DPIA (full Art. 35 form), 4) Consent Capture, 5) Training-Data Exclusion Evidence, 6) Cross-Border Transfer Mechanism, 7) AI-Specific Risk Register, 8) Sign-off Ledger.

## Agent-specific data-flow elements (additions)

When agent features are present, the data-flow inventory shall additionally capture:

- Agent service-principal flow — every system the agent acts as principal against (per-tenant scope).
- Tool-call flow per tool in the action catalogue (source, sink, classification, retention).
- Memory tier flow — scratchpad / episodic / long-term; tenant opt-in flag; erasure SLA.
- Approval-event flow — signed event capture and storage.
- Action audit-log flow — append-only store; hash-chain integrity job.

These additions support SOC 2 P3, ISO/IEC 27001 A.5.34, and HIPAA §164.502 evidence rows in the agent compliance evidence pack (`09-governance-compliance/25-ai-agent-evidence-pack-spec`).

## Standards

- GDPR Art. 35 + Art. 36
- EU AI Act Art. 27 (fundamental-rights impact assessment)
- Kenya DPA 2019 s.31
- Nigeria NDP Act 2023 Art. 28
- South Africa POPIA s.71-72
