---
name: dpia-generation-uk-agents
title: /dpia-generation
description: Generate a Data Protection Impact Assessment (DPIA) under UK GDPR Art.35 in house format for a new feature, product, or processing activity. Follows the ICO DPIA template structure. Checks Art.35(3) mandatory triggers, identifies the required DPO consultation, and flags prior ICO consultation (Art.36) where residual high risk remains. Use when the user says "write a DPIA", "data protection impact assessment for", "do we need a DPIA for this", "privacy review this feature", or describes a new data processing activity requiring assessment.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/privacy-legal-uk/skills/dpia-generation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /dpia-generation

1. Load `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → DPIA house style (trigger, structure, depth, sign-off, DPO consultation requirement).
2. Run the workflow below.
3. Check: is a DPIA actually needed? (House trigger + Art.35(3) mandatory triggers + ICO high-risk list — cite primary sources via uk-legal MCP where available, verify currency.)
4. Intake: ask the product/technical team questions. Can pull from PRD or design doc if provided.
5. Write DPIA in house format following ICO template structure. Include privacy notice consistency check.
6. Output with conditions list, named owners, DPO consultation prompt, and Art.36 prior-consultation flag where residual high risk remains.

```
/privacy-legal-uk:dpia-generation "Location sharing feature"
```

```
/privacy-legal-uk:dpia-generation
PRD: [link or paste]
```

---

# UK GDPR Art.35 DPIA Generation

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the matter folder.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty), ask whether it's inside the privilege circle. See canonical `## Shared guardrails → Destination check` in the plugin CLAUDE.md.

**Special note on DPIAs:** A DPIA is not automatically privileged. Where a DPIA is mandatory under Art.35(3) and a prior ICO consultation (Art.36) occurs, the DPIA becomes part of the supervisory record. Under UK GDPR Art.58(1), the ICO may request the DPIA as part of its investigative powers. A privilege claim over a DPIA will only stand where litigation privilege conditions are met (litigation in reasonable contemplation at the time the document was created). Do not assume a DPIA is protected from ICO scrutiny.

## Purpose

A DPIA is the structured analysis required by UK GDPR Art.35 for high-risk processing. It asks: what data, why, how long, who sees it, what could go wrong, what mitigations are in place. This skill structures that analysis and writes the output in this team's format — the one learned from the seed DPIA during cold-start.

Unlike a generic PIA, a UK GDPR DPIA has specific legal requirements: it must be done before the processing begins; it must cover the Art.35(7) mandatory content; the DPO must be consulted (Art.35(2)) where one is designated; and where the assessment concludes that residual high risk remains after mitigations, the controller must consult the ICO before processing (Art.36).

## Jurisdiction assumption

This DPIA is produced under UK GDPR as the primary regime. If EU GDPR also applies (EU data subjects, EU-established controller/processor), note this — the two regimes have parallel DPIA obligations and the ICO is not the EU supervisory authority. A DPIA produced for UK purposes does not automatically satisfy EU GDPR Art.35.

## Load prior context on this feature / activity

Before writing a new DPIA, check the outputs folder for prior work on the same feature, processing activity, or counterparty. Scan for:

- **Prior `use-case-triage` results** — the triage's risk rating, mandatory triggers, Children's Code flags, and PECR conditions are the entry point for this DPIA.
- **Prior `dpia-generation` outputs** for the same or overlapping activity — a superseding DPIA should reconcile what changed, what carried over. A DPIA that silently produces different conclusions than a prior DPIA on the same activity is a contradiction a reviewing DPO cannot see.
- **Prior `dpa-review` outputs** for vendors in scope — the DPA review's findings inform the DPIA's analysis of processor / sub-processor / international transfer risk.

Cite any prior output found:

> "Prior triage ([date]) rated this [risk level] and required [conditions]. This DPIA builds on that finding — [which conditions are satisfied, which remain, which are re-scoped]."

**Carry severity from upstream as a floor** per the cross-skill severity floor rule.

If no prior output is found, say so explicitly.

## Load house style

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## DPIA house style`. That has:
- What triggers a DPIA here (house triggers above the Art.35(3) mandatory floor)
- The structure template from the seed DPIA
- Typical depth
- Who signs off
- Whether DPO consultation is required by default

If the seed DPIA structure is in the config CLAUDE.md, **use it**. The point is that this DPIA looks like the other DPIAs this team produces, not like a generic one. If no seed DPIA was provided, default to the ICO DPIA template structure (set out below).

## Step 0: Is a DPIA needed?

Check the trigger criteria in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. That is the team's house answer.

In addition, **research the currently operative UK GDPR Art.35 mandatory triggers** using the uk-legal MCP and the ICO's published list of processing operations that require a DPIA. Cite the controlling statute and guidance with OSCOLA-style references. Verify currency — the ICO updates its DPIA guidance list. Flag uncertainty rather than guess.

> **No silent supplement.** If the uk-legal MCP returns few or no results for Art.35(3) triggers or DPO consultation requirements, report what was found and stop. Options: (1) broaden the query; (2) check govuk MCP; (3) proceed on model knowledge tagged `[model knowledge — verify]`; (4) flag as unverified and stop. A DPO or solicitor decides.

**Art.35(3) mandatory triggers** `[UK-GDPR-ART.35(3)]`:
1. Systematic and extensive evaluation of personal aspects based on automated processing including profiling, where decisions produce legal or similarly significant effects
2. Large-scale processing of special category data (Art.9) or criminal convictions / offences data (Art.10)
3. Systematic monitoring of a publicly accessible area on a large scale

**ICO list of processing operations that always require a DPIA** — check current ICO guidance via uk-legal or govuk MCP `[ICO-GUIDANCE — verify current list]`.

**Strong indicators (DPIA REQUIRED minimum, not just house trigger):**
- Novel use of technology or existing technology in a new way
- Children's data (any processing of children's personal data by an online service — Children's Code implications)
- Combining datasets from different sources
- Data that could enable discrimination or profiling
- Processing users would not expect
- Re-use of data for an incompatible purpose
- Any processing involving large-scale transfers of personal data to non-adequate countries

If no statutory trigger and no house trigger → write a one-paragraph "no DPIA required" note for the file, explaining why, in case anyone asks. Even "no DPIA needed" gets documented.

## The intake

Before writing anything, get answers to these from the product / technical team. Conversational is fine.

### What and why

- What's the feature / product / change?
- What problem does it solve for users?
- What personal data does it touch? Be specific — "user data" is not an answer. Which fields? Is any of it UK GDPR Art.9 special category data?
- Is any of it new collection, or is it all data you already have?
- What's the processing — storage, analysis, sharing, automated decisions, profiling?

### UK GDPR lawful basis / Art.9 condition

For UK GDPR processing, identify the Art.6 lawful basis for each purpose. For special category data, identify the Art.9 condition *in addition to* the Art.6 basis. Research the specific requirements using the uk-legal MCP where available.

- Is the basis **legitimate interests**? A Legitimate Interests Assessment (LIA) is required: (1) purpose test; (2) necessity test; (3) balancing test. The DPIA must include or reference the LIA.
- Is the basis **consent**? How is consent obtained? Is it freely given, specific, informed, and unambiguous? What is the withdrawal mechanism?
- Is the processing automated decision-making? Does it produce legal or similarly significant effects? (Art.22 — right not to be subject to solely automated decisions)
- Does it involve children? Children's Code compliance check required (DPA 2018 s.123 `[DPA2018-S.123]`).
- Does it involve PECR (cookies, electronic marketing, electronic communications services)?

### Who and where

- Who inside the organisation can access this data? Engineering? Support? Analysts? Data scientists?
- Any third-party processors? If so: new vendor or existing? Is an Art.28 DPA in place or needed?
- Where is data stored? UK? EU? USA? Other? If outside the UK: what transfer mechanism is used (IDTA / UK Addendum / UK adequacy decision)?
- How long is it kept? Is there a deletion schedule or does it live indefinitely?

### What could go wrong

- If this data was involved in a personal data breach, what's the likely harm to data subjects?
- Could this data be used to discriminate, even accidentally or indirectly?
- Would data subjects be surprised this processing is happening? (The ICO's "reasonable expectations" test — not a legal standard but a useful indicator of high risk)
- Is there an adequate objection / opt-out mechanism? Should there be?
- What could go wrong technically (security) and organisationally (access control, insider threat)?

## Writing the DPIA

**Use the seed DPIA structure from the config CLAUDE.md.** If none was captured during setup, use the ICO DPIA template structure below.

The ICO's published DPIA template covers these sections (verify current ICO guidance for the latest version `[ICO-GUIDANCE]`):

1. Identify the need for a DPIA
2. Describe the processing
3. Consultation process
4. Assess necessity and proportionality
5. Identify and assess risks
6. Identify measures to reduce risk
7. Sign off and record outcomes

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Data Protection Impact Assessment: [Feature / Product Name]
## UK GDPR Art.35

**Prepared by:** [name] | **Date:** [date] | **Status:** DRAFT / APPROVED
**Product owner:** [name] | **Privacy reviewer:** [name]
**DPO consulted?:** [Yes — [name] — [date] / Not yet / N/A — no designated DPO]

---

## Executive summary

[Two sentences: what this is, whether it can proceed. E.g., "Feature X processes location
data to provide real-time navigation. Processing uses consent as the lawful basis and is
consistent with the privacy notice. Two mitigations are required before launch; no
Art.36 prior ICO consultation needed after implementing mitigations."]

**Overall risk (after mitigations):** [Reviewer to set: 🟢 Low / 🟡 Medium / 🟠 High / 🔴 Very high — residual high risk = Art.36 prior ICO consultation required]

---

## 1. Identify the need for a DPIA

**Mandatory Art.35(3) trigger?** [Yes — [specify trigger] | No]
**ICO high-risk list trigger?** [Yes — [specify] | No | Could not confirm — verify current ICO list `[ICO-GUIDANCE]`]
**House trigger met?** [Yes | No]
**DPIA required because:** [one sentence]

---

## 2. Description of processing

**What:** [the feature, in plain English]
**Data categories:** [specific fields — not "user data"; identify if any are Art.9 special category or Art.10 criminal data]
**Data subjects:** [customers / end users / employees / children / etc.]
**Purpose:** [why — tie to data subject benefit and business need]
**New collection?** [yes — these fields are new / no — reusing existing data]
**Nature of processing:** [storage / analysis / automated decision-making / profiling / sharing / etc.]
**Scope:** [scale — how many data subjects, geographic extent, duration]

---

## 3. Consultation process

**DPO consultation:** [DPO consulted? Yes — [name], [date], [summary of advice given] / Not yet — required under UK GDPR Art.35(2) before finalising DPIA `[UK-GDPR-ART.35(2)]` / N/A — no designated DPO]
**Stakeholders consulted:** [product team / engineering / security / legal]
**Data subjects consulted or represented?:** [Yes — [how] / No — [reason; note Art.35(9) says the controller shall seek the views of data subjects or their representatives where appropriate]]

---

## 4. Necessity and proportionality

| Question | Assessment |
|---|---|
| Is the processing necessary for the stated purpose? | |
| Is the processing proportionate to the purpose? | |
| **UK GDPR Art.6 lawful basis:** | [basis for each purpose] |
| **UK GDPR Art.9 condition (if special category data):** | [condition + DPA 2018 Sch.1 condition if applicable] |
| If legitimate interests: LIA completed? | [Yes — [ref] / No — required before processing begins] |
| Data minimisation: is only the minimum necessary data collected? | |
| Purpose limitation: will data be used only for stated purposes? | |
| Storage limitation: is a defined retention period in place? | |
| **Children's Code applicable?** | [Yes — [conditions identified] / No — [reasoning]] |
| **PECR applicable?** | [Yes — [specific regs and consent/notice mechanism] / No] |

---

## 5. Identify and assess risks

**Risk quality standard:** Risks must be specific and tied to the design, not generic. "Data breach" is not a risk — "location history accessible by support staff via admin console without audit logging" is a risk.

| # | Risk | Description | Likelihood | Impact | Risk level |
|---|---|---|---|---|---|
| 1 | [specific risk] | [design-specific description] | L/M/H | L/M/H | 🟢/🟡/🟠/🔴 |

**Privacy notice consistency:**

| Policy commitment | Consistent? | Notes |
|---|---|---|
| [commitment from config CLAUDE.md privacy notice section] | 🟢 / 🟡 Partial / 🔴 Conflict | |

---

## 6. Identify measures to reduce risk

| # | Risk ref | Mitigation | Owner | Due | Status |
|---|---|---|---|---|---|
| 1 | [#] | [specific, actionable — not "improve security"] | [name] | [date] | Done / Planned / Gap |

**Residual risk after mitigations:** [assessment — must be specific]

**🔴 If residual high risk remains after all mitigations:** Prior ICO consultation under UK GDPR Art.36 is required before the processing begins. Do not proceed without it. `[UK-GDPR-ART.36]`

---

## 7. Data subject rights

| Right | Can be exercised for this processing? | How |
|---|---|---|
| Access (Art.15) | | |
| Erasure (Art.17) | | |
| Rectification (Art.16) | | |
| Portability (Art.20) (if consent / contract basis + automated processing) | | |
| Objection (Art.21) | | |
| Restriction (Art.18) | | |
| Rights re automated decision-making (Art.22 if applicable) | | |

---

## 8. Recommendation and sign-off

[APPROVED / APPROVED WITH CONDITIONS / CHANGES REQUIRED / NOT APPROVED / PRIOR ICO CONSULTATION REQUIRED BEFORE PROCESSING BEGINS]

**DPO sign-off:** [name, date, notes — UK GDPR Art.35(2) requires DPO consultation; their views must be documented `[UK-GDPR-ART.35(2)]`]
**Controller sign-off:** [name, date]

**Conditions before launch (if any):**
- [ ] [specific action with owner and deadline]

**Art.36 prior ICO consultation:** [Required — [reason] / Not required — residual risk is [level] after mitigations]
```

## Risk quality standards

Risks in a DPIA must be **specific and tied to the design**, not generic.

| Bad risk | Why bad | Better |
|---|---|---|
| "Data breach" | Applies to everything; says nothing | "Location history accessible by support staff via admin console without audit logging — a malicious insider could track a data subject undetected" |
| "Non-compliance with UK GDPR" | Circular — the DPIA is supposed to assess compliance | Name the specific article and the gap |
| "Users might not like it" | Vague | "Data subjects who have objected to profiling under Art.21 may still have inferred scores generated because the objection flag is not checked in this flow" |

Aim for 2-5 real risks, not 15 generic ones.

## Privacy notice diff

Every DPIA should cross-check against the privacy notice commitments in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. Common drift:

- Notice says "we collect X, Y, Z" — new feature collects W. Notice update needed before launch, or stop collecting W.
- Notice states a lawful basis — new feature uses a different basis. Inconsistency in how you describe your lawful basis to data subjects under Art.13/14.
- Notice says retention is "no longer than necessary for [purpose]" — new feature retains data for a new purpose not stated in the notice.
- Notice says "we do not transfer data outside the UK" — new feature uses a processor in a non-adequate country. Add the transfer mechanism to the notice.

Flag every mismatch. One of them has to change before launch.

## Handoff

- **To product team:** Conditions list with owners and deadlines. Not "improve security" — "implement audit logging for the support-console location lookup, owner: [eng lead], before launch."
- **To DPO (mandatory for mandatory DPIAs):** UK GDPR Art.35(2) requires the controller to seek the advice of the DPO, where designated. The DPO's views must be documented in the DPIA. Do not finalise a mandatory DPIA without DPO consultation.
- **To the ICO (if Art.36 applies):** Where the DPIA concludes that residual high risk remains, the controller must consult the ICO before processing begins (Art.36). The ICO then has 8 weeks (with a possible 6-week extension) to provide advice. `[UK-GDPR-ART.36(2)]`
- **To reg-gap-analysis skill:** If the DPIA uncovered a privacy notice inconsistency, that skill tracks the notice update.

## Gate: submitting a DPIA to the ICO or disclosing to a third party

Producing an internal DPIA is documentation. *Submitting it to the ICO* (under Art.36) or *disclosing it voluntarily to a third party or regulator* is the consequential act.

**Before submitting a DPIA to the ICO under Art.36 or disclosing to any regulator:** Read `## Who's using this` in the practice-level CLAUDE.md. If the Role is Non-lawyer:

> Submitting a DPIA to the ICO under Art.36 has legal consequences — the document becomes part of the supervisory record and any material omission or error becomes enforcement exposure. Have you reviewed this with a solicitor or DPO? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: regime and mandatory trigger, why Art.36 prior consultation is required, the risks identified, residual risk after mitigations, the specific ICO-facing questions, and the three things to ask the professional before submitting.]
>
> If you need to find a qualified solicitor or barrister: the SRA's [Find a Solicitor](https://solicitors.lawsociety.org.uk/) service is the fastest starting point.

Do not proceed past this gate without an explicit yes.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced.

## What this skill does not do

- It doesn't approve the processing. A human (DPO, solicitor, or designated sign-off authority) approves the DPIA.
- It doesn't conduct the prior ICO consultation (Art.36) — it flags when one is required and drafts the documentation to support it.
- It doesn't design the mitigation. It describes what needs mitigating; engineering designs the fix.
- It doesn't produce the formal ICO consultation submission — that is a more structured document; the DPIA output provides the content, but the submission format should follow current ICO guidance.
