---
name: 13-saas-dpa-and-privacy-doc-set-peterbamuhigire
title: SaaS DPA & Privacy Doc Set Skill
description: Use when drafting a SaaS privacy notice, DPA, processing schedule, subprocessor disclosure, retention terms, and data-subject procedures from verified flows and legal review. Use trust-center-document-pack for public assurance material.
author: peterbamuhigire
author_url: https://github.com/peterbamuhigire/chwezi-sdlc-documentation/tree/main/09-governance-compliance/13-saas-dpa-and-privacy-doc-set
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
sources:
- title: Ai Dpa Additions
  path: references/ai-dpa-additions.md
- title: Saas Dpa And Privacy Doc Templates
  path: references/saas-dpa-and-privacy-doc-templates.md
---

# SaaS DPA & Privacy Doc Set Skill

<!-- dual-compat-start -->

## Use When

- Use when drafting a SaaS privacy notice, DPA, processing schedule, subprocessor disclosure, retention terms, and data-subject procedures from verified flows and legal review. Use trust-center-document-pack for public assurance material.

## Do Not Use When

- Do not use when no personal data is processed (rare).
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: Compliance_Docs.md, Multi_Tenancy_Architecture_Spec.md (for regions), sub-processor list, retention obligations, Risk_Assessment.md. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| SaaS DPA & Privacy Doc Set | Accountable reviewer, control owner, auditor, or release authority | DPA shall include SCCs (current EU version) for cross-border transfer. ROPA shall list every processing activity. Breach SLA shall be ≤ 72 hours. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS DPA & Privacy Doc Set evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- DPA shall include SCCs (current EU version) for cross-border transfer. ROPA shall list every processing activity. Breach SLA shall be ≤ 72 hours.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS DPA & Privacy Doc Set from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

Generates the document set that GDPR / POPIA / DPPA / CCPA expect a SaaS processor to publish or hold ready: DPA template, ROPA, retention schedule, breach-notification procedure, DSAR procedure.

## Core Instructions

### Step 1: Draft the DPA

Sections: parties; subject matter; duration; nature & purpose; type of personal data; categories of data subjects; obligations of processor (process only on documented instructions; confidentiality; security; sub-processors with notice and consent; assistance with rights requests; assistance with DPIAs; deletion or return at end; audit rights with notice); obligations of controller; international transfers (Standard Contractual Clauses Annex); liability; term & termination.

### Step 2: Draft the ROPA (Art.30 record)

| Processing activity | Purpose | Categories of data subjects | Categories of personal data | Recipients | International transfers | Retention | Security measures |
|--------------------|---------|----------------------------|----------------------------|------------|------------------------|-----------|-------------------|

Every product feature that processes personal data appears as a row.

### Step 3: Retention & destruction schedule

| Data class | Retention | Destruction method | Verification | Owner |
|------------|-----------|--------------------|--------------|-------|
| Account / billing PII | life of contract + 7 y tax | hard delete after retention | verification query + certificate | privacy officer |
| Operational data | per contract | hard delete on offboarding +30 d grace | verification query | privacy officer |
| Telemetry raw | 13 months | rotate-out | retention policy on bus | platform team |
| Logs | 13 months | rotate-out | retention policy on log store | platform team |
| Backups | per backup retention (e.g. 35 d) | encrypted rotate-out + key destruction | backup audit | platform team |

### Step 4: Breach-notification procedure

- Detection sources: monitoring, audit log, customer report, third-party advisory.
- Confirmation: incident commander confirms within 24 h.
- Risk assessment: scope (tenants, data classes, volume), severity.
- Notify supervisory authority: within 72 h of confirmation (GDPR Art.33) with the prescribed content.
- Notify affected data subjects: where high-risk to rights, without undue delay (Art.34).
- Notify customer (controllers): per DPA SLA — recommend within 24 h of confirmation.
- Record-keeping: every breach logged, regardless of notifiability.

### Step 5: DSAR procedure

- Channels: in-product, support email, postal.
- Authentication: verify identity per published procedure.
- Statutory windows: GDPR 30 d (extendable +60); POPIA reasonable time; CCPA 45 d (+45).
- Right of access: machine-readable export.
- Right to erasure: trigger hard-delete via lifecycle runbook.
- Right to portability: standard JSON/CSV export.
- Right to rectification: in-product UI + audit.
- Right to object / restrict: feature-flag approach.

### Step 6: SCCs

Attach EU Standard Contractual Clauses (Module 2 controller-processor, current version) as an Annex to the DPA where cross-border transfer applies. Note alternative frameworks (UK IDTA, Swiss FDPIC, EU-US Data Privacy Framework).

### Step 7: Write the pack

`DPA_And_Privacy_Pack.md` indexes the docs above.

## Standards

- GDPR (Regulation 2016/679) Articles 28, 30, 32, 33, 34, 35, 44.
- POPIA (South Africa) sections 19, 22, 23.
- DPPA 2019 (Uganda) sections on processor obligations, breach notification, DSAR.
- CCPA / CPRA (California).

## Resources

- `logic.prompt`, `README.md`, `references/saas-dpa-and-privacy-doc-templates.md`.
