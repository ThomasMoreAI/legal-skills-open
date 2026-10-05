---
name: reg-gap-analysis-uk-agents
title: /reg-gap-analysis
description: Diff a new or changed UK regulation, ICO guidance, or enforcement development against current privacy notice and practice — outputs a gap list and a remediation plan with owners and dates. Use when new ICO guidance drops, a UK data-protection regulation changes, the user asks "does [regulation] affect us", "gap analysis for [statute]", "compliance check against [ICO guidance]", "UK GDPR reform — do we need to change anything", or pastes regulatory text or an ICO announcement.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/privacy-legal-uk/skills/reg-gap-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /reg-gap-analysis

1. Load `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → privacy notice commitments, UK regulatory footprint, DSAR process, DPA playbook.
2. Run the workflow below.
3. Scope: does the regulation / guidance apply? (UK jurisdiction, controller/processor status, sector, threshold, in-force date)
4. Extract requirements → diff against current state → gap list.
5. Remediation plan with owners, dates, prioritisation.
6. Save dated doc. Even "no gaps" gets documented.

```
/privacy-legal-uk:reg-gap-analysis "ICO Direct Marketing Guidance update"
```

```
/privacy-legal-uk:reg-gap-analysis "Data (Use and Access) Act automated decision-making provisions"
```

```
/privacy-legal-uk:reg-gap-analysis
[paste ICO guidance / statutory text]
```

---

# UK Data Protection Regulation-to-Practice Gap Analysis

## Purpose

The ICO issues new guidance. The UK Government enacts a Data Act amendment. PECR reform passes. Something moves — and now you need to know what, if anything, you have to change.

This skill diffs the new requirement against what you currently do (per `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → privacy notice commitments + the practices documented in DPIAs) and produces a gap list with a remediation plan.

The scope is explicitly UK-law: UK GDPR, DPA 2018, PECR, NIS Regulations, OSA 2023, ICO guidance, and sector-specific UK obligations. EU GDPR is a separate regime — note where the two diverge (post-Brexit UK/EU divergence tracking).

## Load current state

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`:
- `## Privacy notice commitments` — what you've publicly promised data subjects
- `## Regulatory footprint` — what UK regimes already apply
- `## DSAR process` → systems list — what you actually do operationally
- `## DPA playbook` — your processor/controller positions

If the regulation doesn't apply (wrong jurisdiction, below threshold, different sector), the gap analysis is one line: "Doesn't apply. Here's why: [reason]. No action needed."

## Workflow

### Step 1: Scope the regulation / guidance

Before diffing, answer:

- **Does it apply?**
  - **Jurisdiction:** UK-enacted primary legislation or secondary legislation? ICO guidance (persuasive, not binding law)? EU-origin rule (no longer binding in UK post-Brexit)? If a rule is EU GDPR only and not UK GDPR, note it applies to EU data subjects but not UK-only processing.
  - **Controller / processor applicability:** does the rule apply to controllers only, processors, or both?
  - **Threshold:** revenue, user count, data volume, sector?
  - **Sector carve-outs:** children's services, financial services, health, law enforcement?
- **When?**
  - Effective date for primary legislation
  - In-force date for secondary legislation (SI) and statutory codes
  - ICO guidance: no fixed effective date, but immediate relevance to ICO enforcement expectations
  - Any phase-in or transitional provisions?
- **What's actually new?**
  - Many UK data-protection developments are amendments to existing UK GDPR or DPA 2018 provisions. Identify the delta from what you already comply with, not the full text.
  - Post-Brexit divergence: if the development reflects a UK/EU divergence (UK moving away from EU GDPR interpretation), note both positions.

### Step 2: Extract requirements

Read the regulation or guidance. List every substantive requirement as a discrete item:

| # | Requirement | Citation (OSCOLA) | Category |
|---|---|---|---|
| 1 | [requirement as stated] | [e.g., UK GDPR, art 22 (as amended); DPA 2018, s 14; ICO guidance 'DPIA guidance' (ICO, 2024)] | [Notice / Rights / Security / Processor / Consent / Governance / Transfer / Children] |

**UK citation format (OSCOLA):**
- Primary legislation: *Data Protection Act 2018*, s 15; UK GDPR, art 35(3)
- Secondary legislation: Privacy and Electronic Communications Regulations 2003 (SI 2003/2426), reg 6
- ICO guidance: cite as ICO, '[Title]' (ICO, [year]) — note this is guidance, not binding law
- UK case law: *[Case Name]* [[year]] [court] [reference]

**Categories:**
- **Notice / Transparency** — what you have to tell data subjects (privacy notice content, Art.13/14)
- **Rights** — data subject rights (DSAR-adjacent)
- **Security** — technical and organisational measures
- **Processor / supply chain** — what you have to flow down to processors (Art.28)
- **Consent** — opt-in/soft-opt-in mechanics (UK GDPR + PECR)
- **Governance** — DPO, DPIAs, ROPA, records of consent, ICO notifications
- **Transfer** — international transfers (IDTA, UK Addendum, UK adequacy)
- **Children** — Children's Code obligations (DPA 2018 s.123) and age-verification

### Step 3: Diff against current state

For each requirement:

```markdown
### [Requirement #N]: [short name]

**Regulation / guidance says:** [requirement, quoted or paraphrased, with OSCOLA cite]

**We currently:** [what the config CLAUDE.md / privacy notice / practice shows]

**Gap:** [None | Partial | Full]

**If partial/full gap — what's missing:** [specific]

**Effort to close:** [Notice update only | Policy / process change | Product change |
DPA renegotiation | New governance process | Vendor renegotiation]

**Risk of non-compliance:** [ICO enforcement likelihood, penalty range (£17.5m / 4% global turnover for UK GDPR breaches; £8.7m / 2% for other DPA 2018 breaches), reputational, operational]
```

### Step 4: Prioritise

Not every gap is equal. Sort by:

1. **Hard deadline with teeth** — enacted statute with a specified compliance date + ICO enforcement history for this type of breach + real penalty ceiling
2. **Effort-to-impact ratio** — notice language update is cheap; product rebuild is not
3. **What you've already half-done** — if you're 80% there on the existing requirement, the new requirement delta may be small
4. **ICO enforcement priorities** — the ICO publishes its regulatory strategy and enforcement priorities. If this area is an active ICO enforcement focus, treat as higher priority regardless of abstract legal risk.

### Step 5: Remediation plan

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role).

> **Research-connector pre-flight.** Before emitting the remediation plan, check whether the uk-legal MCP or govuk MCP is reachable for this session. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if neither is reachable, record it in the **Sources:** line — e.g., `not connected — cites from training knowledge; the highest-fabrication items in UK data-protection gap analyses are enacted-vs-pending status, ICO guidance update dates, and pinpoint paragraph references in ICO codes — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## Remediation Plan: [Regulation / guidance name]

**Instrument type:** [UK primary legislation / UK SI / ICO statutory code / ICO guidance / other]
**Effective date:** [date enacted / in force]
**ICO enforcement effective:** [date — may differ from legislative effective date]
**Applies to us?:** [Yes — [why] / No — [why not] / Partial — [which aspects]]

### Must-do before enforcement / effective date

| Gap | Fix | Owner | Due | Status |
|---|---|---|---|---|
| [gap] | [specific fix] | [name] | [date] | [ ] |

### Should-do (lower risk, not blocking)

[same table]

### Already compliant

[list of requirements where gap = None — useful for the "we're mostly fine" message and as evidence of compliance assessment]

### Accepted gaps (risk-accepted, not fixing)

[if any — with documented rationale, who accepted the risk, and review date]

### UK/EU divergence note (if applicable)

[where the new UK requirement diverges from EU GDPR or EDPB guidance — note both positions so the team with EU data subjects knows to handle both]
```

## Common UK regulation categories

When scoping the delta, place the new requirement into a category and then research specifics:

- **UK GDPR / DPA 2018 amendment** — changes to the core UK data-protection framework; verify via legislation.gov.uk and uk-legal MCP
- **ICO statutory code** — mandatory codes under DPA 2018 (Children's Code, Data Sharing Code, etc.); legally binding as relevant considerations in ICO enforcement
- **ICO guidance** — persuasive, not binding; but ICO enforces against its own guidance positions
- **PECR reform** — changes to the cookie / direct marketing / electronic communications regime
- **NIS / NIS2-equivalent UK reform** — security incident reporting for essential services / DSPs
- **OSA 2023 implementation** — Ofcom codes of practice for user-to-user / search services
- **Sector-specific obligation** — FCA, NHS/DHSC, Ofsted, DfE, etc.
- **International transfer framework update** — new UK adequacy decision, IDTA version update, UK Addendum version update, UK-US Data Bridge changes
- **ICO enforcement notice / penalty notice** — signals current enforcement approach; not binding on others but highly instructive

For each category, **research the currently operative requirements** using the uk-legal MCP and govuk MCP before drafting the gap analysis. Cite primary sources. Verify currency. Flag uncertainty for DPO or solicitor verification.

> **No silent supplement.** If the uk-legal MCP returns few or no results for a regulation, guidance document, or enforcement development, report what was found and stop. Say: "The uk-legal MCP returned [N] results for [topic]. Options: (1) broaden the query; (2) check govuk MCP; (3) proceed on model knowledge tagged `[model knowledge — verify]`; (4) flag as unverified and stop." A DPO or solicitor decides.
>
> **Source attribution tiering:**
> - `[settled — last confirmed YYYY-MM-DD]` — stable, well-known UK GDPR and DPA 2018 provisions
> - `[uk-legal MCP]` — retrieved from the uk-legal MCP this session
> - `[govuk MCP]` — retrieved from the govuk MCP this session
> - `[verify]` — model-knowledge citations to verify
> - `[verify-pinpoint]` — specific subsection letters, schedule paragraph numbers, statutory instrument numbers — always verify

## UK/EU post-Brexit divergence tracking

Where the gap analysis concerns an area where UK and EU law may diverge, explicitly note both positions:

- **UK position:** [what UK GDPR / DPA 2018 / ICO currently says]
- **EU position:** [what EU GDPR / EDPB currently says]
- **Practical impact:** [if you have EU data subjects, you need to comply with both; if you are UK-only, EU GDPR doesn't apply]

Areas of known or potential divergence (as of 2026 — verify current state via uk-legal MCP):

- Automated decision-making (Art.22 / equivalent): UK reform proposals may change ADM provisions
- Legitimate interests recognised under UK law vs. EDPB guidance on legitimate interests
- ROPA obligations: potential UK reform to threshold for smaller organisations
- International transfers: UK adequacy list differs from EU; UK-US Data Bridge vs. EU-US DPF are parallel but distinct frameworks
- Cookie rules: PECR reform may move UK away from ePrivacy Directive-aligned approach

`[model knowledge — verify current divergence status via uk-legal or govuk MCP]`

## Integration with other skills

**From DPIA generation:** DPIAs flag privacy notice inconsistencies → those feed here as known gaps.
**From policy-monitor:** Policy-monitor finds internal practice drift → reg-gap-analysis handles incoming external legal changes. Different directions of change.
**From use-case-triage:** Triage results that identified a new UK regulatory obligation → reg-gap-analysis provides the full compliance assessment.

## Output

Save as a dated markdown document. The remediation plan table becomes a tracker — update status as items close.

If the gap analysis concludes "no gaps, we're compliant," still write the doc — it is useful evidence of compliance assessment if the ICO asks.

**Close with a citation-verification note:**

> Citations in this output were generated by an AI model. Before relying on any UK statute, SI, ICO guidance, or enforcement action, check it against the uk-legal MCP, legislation.gov.uk, ico.org.uk, or a qualified legal research source for accuracy and current status. Source tags on each citation (e.g., `[model knowledge — verify]`) show where it came from; `verify` tags carry higher fabrication risk and should be checked first.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

## What this skill does not do

- It doesn't interpret ambiguous UK regulatory language authoritatively. When the reg is unclear, say so: "This section could be read as [A] or [B]. [A] is the conservative read. Consider seeking ICO guidance or outside counsel if this is material."
- It doesn't track regulatory changes proactively. It runs when you point it at a change.
- It doesn't implement fixes. It plans them.
- It doesn't replace legal advice on whether the regulation applies. Whether a new requirement applies to a specific organisation is a legal question — this skill provides a structured analysis; a solicitor or DPO makes the call.
