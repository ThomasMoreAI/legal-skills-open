---
name: dpa-review-uk-agents
title: /dpa-review
description: Review a Data Processing Agreement against your UK GDPR Art.28 DPA playbook — auto-detects whether you're processor or controller and applies the right half of the playbook. Checks Art.28 mandatory provisions, sub-processor chain, international transfer mechanisms (IDTA / UK Addendum / adequacy), and privacy notice consistency. Use when the user says "review this DPA", "check this data processing agreement", "customer sent their DPA", "is this DPA okay", or attaches a DPA / processor agreement.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/privacy-legal-uk/skills/dpa-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /dpa-review

1. Load `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → DPA playbook. If placeholders, stop and prompt setup.
2. Get the DPA. Determine direction: are we processor (controller's DPA) or controller (vendor's)? Ask if ambiguous.
3. Run the workflow below — Art.28 mandatory provisions check + term-by-term against the appropriate playbook row.
4. Run international transfer mechanism check.
5. Run privacy notice consistency check.
6. Output: review memo with redlines. Save per house style.

```
/privacy-legal-uk:dpa-review customer-dpa.pdf
```

---

# UK GDPR Art.28 DPA Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

---

## Purpose

DPAs come in two flavours and the review is nearly opposite for each. When a controller sends their DPA, we're defending our operational flexibility as processor. When we send one to a vendor, we're protecting our (and our data subjects') data as controller. Both reviews read from the same `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` playbook but from opposite rows.

Under UK GDPR Art.28, a DPA must contain specific mandatory provisions. A DPA that is merely labelled "data processing agreement" but omits Art.28(3) terms is non-compliant — the first check is always whether the mandatory provisions are present.

## First: which direction?

Before anything else, establish:

- **We are the processor** → controller is sending us their DPA → read `## DPA playbook → When we are the processor` table
- **We are the controller** → we're sending a DPA to a vendor (or reviewing theirs) → read `## DPA playbook → When we are the controller` table

If unclear, ask. Getting this wrong inverts every recommendation.

## Jurisdiction assumption

This review assumes UK GDPR applies as the primary data-protection law. If the DPA also involves EU data subjects or an EU-established controller/processor, EU GDPR applies in parallel — flag this and note that IDTA / UK Addendum (UK side) and EU SCCs (EU side) may both be required.

## Load prior context on this counterparty / activity

Before reviewing, check the outputs folder for prior work on this counterparty or processing activity. Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## Outputs` for the outputs folder path. Scan for:

- **Prior `use-case-triage` results** for the same counterparty / processing activity — the triage produces a risk rating and conditions that this DPA review should honour or explicitly depart from.
- **Prior `dpia-generation` outputs** covering this counterparty / processing activity — the DPIA may have flagged risk mitigations the DPA needs to implement.
- **Prior `dpa-review` outputs** for the same counterparty — earlier DPA reviews set expectations about what was acceptable, what was flagged, and what was settled.

If a prior output is found, cite it in the review:

> "Prior triage ([date]) rated this [risk level] and conditioned approval on [X]. This DPA review is consistent with that finding." — or —
> "Prior triage ([date]) rated this [risk level]. This DPA review departs from that finding because [reason]."

**Carry severity from the upstream output as a floor** per the cross-skill severity floor rule in CLAUDE.md `## Shared guardrails`.

If no prior output is found, say so explicitly.

## Load the playbook

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## DPA playbook`. Also read `## Privacy notice commitments` — the DPA can't contradict what the privacy notice promises data subjects.

## UK GDPR Art.28 mandatory provisions check — first gate

Before running the term-by-term review, check that the DPA contains the **mandatory Art.28(3) provisions**. A DPA that omits these is non-compliant regardless of anything else. Each of the following must be present — if any is absent, it is a 🔴 finding regardless of the rest of the review: `[UK-GDPR-ART.28(3)]`

| Art.28(3) mandatory provision | Present? | Notes |
|---|---|---|
| Art.28(3)(a): Process personal data only on documented instructions of the controller, including transfers to third countries (unless required by UK law) | | |
| Art.28(3)(b): Confidentiality obligation on persons authorised to process | | |
| Art.28(3)(c): Implement appropriate technical and organisational security measures (Art.32) | | |
| Art.28(3)(d): Sub-processor rules — no sub-processor without prior written authorisation (specific or general); if general, inform the controller of changes and give the controller the opportunity to object; any sub-processor DPA imposes the same data-protection obligations | | |
| Art.28(3)(e): Assist the controller with data subjects exercising their rights | | |
| Art.28(3)(f): Assist the controller with security, breach notification, DPIA, and prior consultation obligations | | |
| Art.28(3)(g): Delete or return all personal data at the end of provision of processing services | | |
| Art.28(3)(h): Make available all information necessary to demonstrate compliance; allow and contribute to audits | | |

Any missing mandatory provision is a 🔴 — not negotiable. Flag it before the term-by-term review.

## UK sectoral overlay check (ask first, before the term-by-term walk)

Before walking the term-by-term review, answer: **does the data flowing through this DPA include any sector-specifically regulated category?** UK GDPR supplies one floor; sector-specific UK law often supplies another that does not appear in the generic DPA playbook.

> **Activity-based sectoral overlays — ask first:**
>
> Does this processing touch:
> - **Financial services / FCA-regulated data** (customer financial data, payment card data, "nonpublic personal information" in a regulated firm)? UK GDPR applies; additionally, FCA's SYSC requirements and operational resilience rules may impose specific data-handling and third-party oversight obligations. `[model knowledge — verify FCA requirements]`
> - **Health / clinical data processed by NHS, NHS-contracted organisations, or health and social care bodies**? The NHS Data Security and Protection (DSP) Toolkit requirements apply; data security standards and governance obligations beyond generic UK GDPR. `[ICO-GUIDANCE] [model knowledge — verify DSP Toolkit current version]`
> - **Education records / pupil data** held by schools or their service providers? UK GDPR applies; additionally, DfE data protection guidance for schools, and potentially Children's Code obligations.
> - **Criminal convictions or offences data (DPA 2018 s.10 / UK GDPR Art.10)**? Specific conditions apply — only by public authorities, or where authorised by DPA 2018 Sch.1 conditions. Flag in the DPA: what authorises processing?
> - **Data from children under 18 in an online service** (likely Children's Code scope)? The DPA must address how the processor supports Children's Code obligations if they apply to the controller.
> - **Any other regulated sector** (legal services / SRA, insurance, pensions, charitable sector, etc.)?
>
> If yes to any: the sectoral overlay usually supplements UK GDPR — it doesn't replace it. Research the specific requirements and cite primary sources before stating a floor. `[model knowledge — verify]`

If no sectoral overlay applies, note that explicitly so the reviewing solicitor sees the check ran.

## The term-by-term review

### Core terms (check every DPA)

Walk every DPA through these terms, clause by clause. The specific numeric and substantive positions come from `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## DPA playbook`. The regulatory floors come from primary UK law — use the uk-legal MCP where available.

> **No silent supplement.** If a research query to the uk-legal MCP returns few or no results for a regime's breach window, transfer-mechanism requirement, or sub-processor-change rule, report what was found and stop. Do NOT fill the gap from model knowledge without asking. Say: "The uk-legal MCP returned [N] results for [topic]. Options: (1) broaden the query, (2) check the govuk MCP, (3) proceed on model knowledge tagged `[model knowledge — verify]`, or (4) flag as unverified and stop." A solicitor or DPO decides whether to accept lower-confidence sources.
>
> **Source attribution tiering:**
> - `[settled — last confirmed YYYY-MM-DD]` — stable Art.28 provisions and well-known UK GDPR requirements
> - `[uk-legal MCP]` — retrieved from the uk-legal MCP this session
> - `[verify]` — model-knowledge citations that should be verified
> - `[verify-pinpoint]` — specific subsection letters, paragraph numbers, instrument numbers — highest fabrication risk; always verify

| Term | Looking for | Playbook field | Common fights |
|---|---|---|---|
| **Roles** | Clear controller/processor designation; matches reality | — | Counterparty labels relationship (e.g., "joint controller") in a way that doesn't match reality |
| **Processing scope** | Limited to documented instructions; defined purposes | — | Open-ended scope expanders ("and related purposes") |
| **Art.28(3) mandatory provisions** | All 8 mandatory provisions present and substantive | — | Boilerplate clauses with no real content |
| **Sub-processors** | Current list disclosed, Art.28(2) change mechanism defined | Sub-processor changes | Blanket approval vs. objection right vs. notice-only |
| **Security measures** | Annex references specific controls or standards (Art.32) | Security standards | "appropriate technical and organisational measures" with no annex = empty promise |
| **Breach notification** | Defined trigger ("awareness" vs "confirmation"), defined timeline, sufficient to allow controller to meet 72-hr Art.33 window | Breach notification | Timeline too long for controller to notify ICO; clock trigger vague |
| **Audit rights** | Method (report vs. on-site), frequency, notice, cost | Audit rights | On-site audits on short notice; "at our discretion" |
| **International transfers** | Transfer mechanism identified (IDTA / UK Addendum / adequacy decision), supplementary measures if needed | International transfers | Outdated mechanisms; EU SCCs only (no UK Addendum for UK side) |
| **Deletion/return** | Timeline post-termination, certification option, backup carveout | Deletion on termination | "Commercially reasonable" deletion = undefined obligation |
| **Liability** | Within MSA cap or separate capped carveout | Liability for data | Uncapped data breach liability |
| **Assistance obligations** | Art.28(3)(e)(f) assistance with rights, security, DPIA, breach — substantive not just "shall cooperate" | — | Empty "shall cooperate" language with no specifics |

### When we're the processor: defensive review

Controller DPAs try to push operational burden onto us. For each clause below, compare the controller's ask to the playbook. Where the ask is outside the playbook, push back to our standard position and be ready to fall back to the acceptable position.

| Clause | Risk | Playbook lookup |
|---|---|---|
| Sub-processor approval right (veto) | Can't add infrastructure without counterparty-by-counterparty approval | Apply playbook position on sub-processor changes |
| On-site audit on short notice | Unworkable at scale | Apply playbook position on audit rights |
| Aggressive breach notification window | Demands notice before we know what happened — but must allow controller to meet 72-hr ICO window | Research Art.33 controller obligations `[UK-GDPR-ART.33]`; compare to playbook |
| Hard data residency (single country/DC) | May not match cloud architecture | Apply playbook position on data location |
| Processor liability uncapped | Existential risk | Apply playbook position on liability |
| Controller may issue binding "instructions" via any medium | Open-ended operational control | Define: "instructions documented in the Agreement or agreed in writing" |
| Deletion on very short timeline | Backup and log retention makes immediate deletion impossible | Apply playbook position; document backup rotation carveout |
| Controller requires compliance with EU GDPR (not UK GDPR) | Different regime | Check whether EU data subjects are in scope; if yes, dual compliance may genuinely be needed; if no, push for UK GDPR only |

### When we're the controller: protective review

Vendor DPAs try to give us nothing. For each clause below, compare to the controller-side playbook.

| Clause | Gap | Playbook lookup |
|---|---|---|
| No sub-processor list | Don't know who touches our data | Require published current list + advance notice per Art.28(2) and playbook |
| "Industry standard security" | Means nothing | Require annex with specific controls or reference to a named standard (ISO 27001, Cyber Essentials Plus) |
| No breach notification timeline | They tell us whenever | Research Art.33 controller obligations; require playbook position; must allow controller to meet 72-hr ICO window |
| No audit rights at all | Can't verify anything | Require at minimum an independent audit report per playbook |
| Vendor can use data for "service improvement" or AI training | Potential training on our data | Strike; processing limited to providing the service to us |
| No international transfer mechanism | No lawful transfer mechanism | Research the currently operative UK transfer mechanism for the corridor in question (IDTA / UK Addendum / UK adequacy decision). Cite primary sources and verify currency. A missing mechanism for a non-UK/non-adequate-country transfer is 🔴. |
| No deletion commitment | Data lives forever | Require playbook position on deletion + certification option |
| Art.28(3) mandatory provisions absent | Non-compliant agreement | 🔴 — all 8 Art.28(3) provisions must be present |

## International transfers check

**This is one of the most error-prone areas — research current UK transfer mechanisms before opining.**

For every transfer of personal data to a country outside the UK that is not covered by a UK adequacy decision, a transfer mechanism is required. Use the uk-legal MCP or govuk MCP to retrieve the current list of UK adequacy decisions and IDTA / UK Addendum status.

| Corridor | Check |
|---|---|
| UK → EU/EEA | UK has found the EU/EEA adequate — no additional mechanism needed for UK-to-EU transfers `[verify current UK adequacy list]` |
| UK → USA | UK-US Data Bridge in force since October 2023 — only for transfers to certified US organisations. Verify: (a) US recipient is certified; (b) transfer falls within the Data Bridge scope. If not certified/in scope → IDTA or UK Addendum required. `[model knowledge — verify current status]` |
| UK → other countries | Check UK adequacy list. If no adequacy: IDTA required (the UK's post-Brexit transfer mechanism, issued by the ICO), or the UK Addendum to EU SCCs (where parties already have EU SCCs in place for the EU side). `[verify]` |
| EU → UK | UK has adequacy from the EU side (verify the EU Commission's current list — the EU-UK adequacy decision may be subject to review). `[model knowledge — verify]` |

**IDTA vs. UK Addendum:**
- **IDTA (International Data Transfer Agreement):** The primary UK standalone transfer mechanism. Used where there are no EU SCCs in place. Verify current IDTA version and any associated guidance from the ICO. `[ICO-GUIDANCE]`
- **UK Addendum to EU SCCs:** Used where parties have (or will execute) EU Standard Contractual Clauses (2021 version) for the EU side of a transfer. The UK Addendum amends the EU SCCs to cover UK-originating transfers. `[ICO-GUIDANCE — verify current version]`

A DPA that includes EU SCCs but no UK Addendum does not cover UK-originating transfers. This is a 🔴 for any DPA where UK personal data is being transferred outside the UK/EU.

If a transfer mechanism is missing and there is a non-adequate-country transfer → 🔴. There is no lawful transfer mechanism.

## Consistency check: privacy notice

The DPA you sign can't promise something the privacy notice doesn't cover, and vice versa.

- If the DPA commits to processing only for purposes X, Y, Z — does the privacy notice list those purposes with the correct lawful basis?
- If the privacy notice says "we do not transfer data outside the UK" — does any DPA clause facilitate a transfer to a non-adequate country?
- If the privacy notice names specific processor / sub-processor categories — does the DPA sub-processor list match?
- If the DPA includes a provision allowing the processor to use data for its own purposes (e.g., product improvement, AI training) — does the privacy notice inform data subjects of this?

Flag mismatches. Usually the privacy notice is stale, not the DPA — but someone needs to fix one of them.

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artefact, not a rewrite. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept than wholesale replacements.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase
- Replace a **phrase** before a sentence
- Restructure a **subclause** before replacing the sentence
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and say so in the transmittal

## Output

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# DPA Review (UK GDPR Art.28): [Counterparty]

**Direction:** [We are processor / We are controller]
**Reviewed:** [date]
**Attached to:** [MSA / standalone]

---

## Bottom line

[Two sentences. Can we sign? What has to change?]

**Issues:** [N]🟢 [N]🟡 [N]🟠 [N]🔴

---

## Art.28(3) mandatory provisions

[🟢 All 8 provisions present | 🔴 Missing: list]

---

## Term-by-term

[For each core term: what the counterparty's DPA says, what our playbook says, the gap, the risk, and the proposed redline language.]

---

## International transfers

[Mechanism identified: [IDTA / UK Addendum / UK adequacy decision] | 🔴 Missing — no lawful transfer mechanism]
[Corridor: [UK → X]. UK adequacy covers: [Y]. IDTA/UK Addendum required for: [Z].]

---

## Privacy notice consistency

[🟢 Consistent | 🟡 Flags: list]

---

## Recommended redlines

[Consolidated — ready to send back]

---

## If they won't move

[For each issue: the fallback from the config CLAUDE.md, or escalation routing if no fallback exists]
```

## Gate: signing a DPA

Reviewing a DPA is research. *Signing* it is the consequential act.

**Before proceeding to sign or countersign a DPA:** Read `## Who's using this` in the practice-level CLAUDE.md. If the Role is Non-lawyer:

> Signing a DPA is a legal act — it binds the organisation to specific data-protection obligations that flow to the ICO and to data subjects. Under UK GDPR Art.28, a non-compliant processor DPA is an independent breach. Have you reviewed this with a solicitor or qualified privacy professional? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, direction (processor / controller), the terms that deviate from the playbook and how they were resolved, any open fallback decisions, international transfer mechanism in use, and the three things to ask the solicitor before executing.]
>
> If you need to find a qualified solicitor or barrister: the SRA's [Find a Solicitor](https://solicitors.lawsociety.org.uk/) service or the Law Society of Scotland / Northern Ireland equivalents are the fastest starting points.

Do not proceed past this gate without an explicit yes.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

## What this skill does not do

- It doesn't draft a DPA from scratch. If the answer is "use our template," pull the template from the seed docs path in the config CLAUDE.md.
- It doesn't do the Transfer Impact Assessment itself — it flags when one may be needed (for IDTA processing, a Transfer Risk Assessment / TRA may be required per ICO guidance).
- It doesn't decide whether to accept terms outside the fallbacks. It routes those per the escalation table.
