---
name: 15-ai-act-and-regulatory-compliance-doc-peterbamuhigire
title: AI Act and Regulatory Compliance Doc Skill
description: Use when classifying AI features against applicable regulatory regimes and mapping obligations, evidence, owners, gaps, and release conditions. Use regulator-overlap-mapping for multi-regime evidence reuse and responsible-ai-declaration for product disclosure.
author: peterbamuhigire
author_url: https://github.com/peterbamuhigire/chwezi-sdlc-documentation/tree/main/09-governance-compliance/15-ai-act-and-regulatory-compliance-doc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
sources:
- title: Ai Act Regulatory Compliance Doc Template
  path: references/ai-act-regulatory-compliance-doc-template.md
- title: Ai Agent Tier Crosslink
  path: references/ai-agent-tier-crosslink.md
- title: Ai Disclosure Copy Library
  path: references/ai-disclosure-copy-library.md
- title: Eu Ai Act Application Timeline
  path: references/eu-ai-act-application-timeline.md
---

# AI Act and Regulatory Compliance Doc Skill

<!-- dual-compat-start -->

## Use When

- Use when classifying AI features against applicable regulatory regimes and mapping obligations, evidence, owners, gaps, and release conditions. Use regulator-overlap-mapping for multi-regime evidence reuse and responsible-ai-declaration for product disclosure.

## Do Not Use When

- Do not use if the product is non-AI or single-jurisdiction internal-only.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Feature_PRD_Spec.md, AI_Model_Card.md (per feature), AI_Data_And_Knowledge_Base_Spec.md, DPA, regional rollout plan. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A required source, owner, obligation, or acceptance condition is missing | Stop the affected claim and record the gap | Unsupported governance artefact |
| Evidence satisfies the declared acceptance condition | Record the decision and hand off to the named consumer | Ambiguous approval or release |

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
| AI Act and Regulatory Compliance Doc | Accountable reviewer, control owner, auditor, or release authority | Every AI feature shall have an EU AI Act tier verdict with reasoning. Every high-risk feature shall map to Annex IV technical documentation. Every region in scope shall have disclosure copy. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Act and Regulatory Compliance Doc evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every AI feature shall have an EU AI Act tier verdict with reasoning. Every high-risk feature shall map to Annex IV technical documentation. Every region in scope shall have disclosure copy.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Act and Regulatory Compliance Doc from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a required source, owner, obligation, or acceptance condition is missing, stop the affected claim and record the gap. Record the evidence and result in the validation record; this avoids unsupported governance artefact.

## References

- [EU AI Act application timeline](references/eu-ai-act-application-timeline.md): load when any feature has an EU AI Act verdict and needs dated obligations.
- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Core Instructions

### Step 1: EU AI Act classification per feature

For each feature evaluate:

- **Prohibited (Art. 5)** — social scoring, manipulative AI, predictive policing of natural persons, untargeted scraping of facial images, emotion inference in workplace/education, exploiting vulnerability, biometric categorisation by protected characteristic, real-time remote biometric identification in publicly accessible spaces; and, added by the Digital Omnibus on AI (Regulation (EU) 2026/1744), systems generating non-consensual intimate imagery or child sexual abuse material.
- **High-risk (Annex III)** — biometric / critical infrastructure / education-and-training / employment / essential private and public services (including credit and insurance) / law enforcement / migration / administration of justice / influencing elections.
- **Limited-risk (Art. 50)** — chatbots, generative content, deep fakes -- transparency obligations.
- **Minimal-risk** — everything else.

Each feature carries the verdict, the cited Article / Annex point, and the "Applies from" date from [the application timeline](references/eu-ai-act-application-timeline.md) (Annex III high-risk from 2 December 2027, Annex I from 2 August 2028, Art. 50 transparency from 2 August 2026, as amended by the Digital Omnibus on AI).

### Step 2: US sectoral exposure

- FCRA — adverse credit decisions based on AI.
- HIPAA — PHI handling and de-identification.
- EEOC + Title VII — automated employment decisions.
- NYC Local Law 144 — AEDT bias audits.
- Colorado AI Act (SB24-205) — high-risk consumer decisions.
- California AB 2013 + ADMT regulation (2026-) — generative training data + automated decision-making.
- Illinois BIPA — biometric data.
- FTC Section 5 — unfair or deceptive AI claims.

### Step 3: Canadian / UK guidance

- Canada AIDA (pending) and Directive on Automated Decision-Making for federal scope.
- UK ICO guidance on AI + AI Act-equivalent pro-innovation framework.

### Step 4: African regulator overlays

- Kenya ODPC AI guidance (2024).
- Nigeria NDPC advisory on AI processing (2024).
- South Africa POPIA s.71 (automated decision-making).
- Note: Uganda DPPA 2019 has no AI-specific clause yet; profile under general data-protection obligations.

### Step 5: Annex IV technical documentation index

For every high-risk-classified feature build the index (table mapping each Annex IV element to the artefact in our system that satisfies it).

### Step 6: Disclosure copy library

UI copy for required disclosures per region:

- "AI-assisted output" tooltip.
- First-use AI feature disclosure modal.
- High-risk decision human-oversight notice.
- Generative content disclosure (Art. 50).
- Right-to-explanation copy.

### Step 7: Write the doc

`AI_Act_And_Regulatory_Compliance_Doc.md` sections: 1) EU AI Act Classification, 2) US Sectoral Exposure, 3) Canada / UK, 4) African Regulators, 5) Annex IV Technical Documentation Index, 6) Disclosure Copy Library, 7) Open Compliance Items, 8) Review Cadence.

## Agent-specific overlap with SOC 2 / ISO 27001 / HIPAA

When the SaaS ships agent features alongside the AI features covered here, this doc shall cross-link to the agent-specific compliance stack:

- SOC 2: `09-governance-compliance/20-ai-agent-soc2-control-pack` (per-TSC agent-specific implementations).
- ISO 27001: `09-governance-compliance/21-ai-agent-iso27001-control-pack` (Annex A agent treatments).
- HIPAA: `09-governance-compliance/22-ai-agent-hipaa-control-pack` (Security Rule agent treatments; admin-only constraint).
- BAA / DPA: `09-governance-compliance/26-ai-agent-baa-and-data-processing-language`.
- Regulator overlap matrix (one-evidence-many-regimes): `09-governance-compliance/27-ai-agent-regulator-overlap-mapping`.

EU AI Act high-risk classification (Annex III) drives extra documentation that this doc owns (Annex IV technical-documentation index), while the agent-specific operating controls are owned by the agent control packs. The crosswalk in `27-ai-agent-regulator-overlap-mapping` shows where evidence is reused vs where the AI Act demands artefacts unique to itself (e.g., conformity assessment, post-market monitoring per Art. 72, serious-incident reporting per Art. 73).

## Standards

- EU Reg 2024/1689 (AI Act), as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026)
- ISO/IEC 42001
- NIST AI RMF
- US sectoral statutes named above
- Kenya DPA 2019, NDPR / NDP Act 2023, POPIA 2013
