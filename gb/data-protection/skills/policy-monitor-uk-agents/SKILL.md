---
name: policy-monitor-uk-agents
title: /policy-monitor
description: 'Keep the UK privacy notice current with practice. Two modes: sweep of saved DPIAs, DPA reviews, and triage results to find policy drift; or direct query for a proposed new practice. Watches for ICO enforcement notices and guidance updates. Use when the user asks "does our notice cover this", "we want to start doing X — does the notice need updating", "run the policy monitor", "privacy notice sweep", or wants to find where the privacy notice no longer matches what the team actually does.'
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/privacy-legal-uk/skills/policy-monitor
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /policy-monitor

**Sweep mode** (no argument or `--sweep`):
1. Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → outputs folder path, policy document, last sweep date.
2. Run the workflow below. Scan outputs folder for files since last sweep.
3. For each output: extract approved practices → diff against current notice commitments.
4. Classify gaps: REQUIRED (notice misrepresents current practice or processing has no notice coverage) vs ADVISABLE (notice silent but not in conflict).
5. For each gap: quote current notice, describe gap, draft suggested language.
6. Update Last policy sweep date in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`.

**Direct query mode** (with description argument):
1. Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → current notice commitments + actual notice document.
2. Parse proposed practice. Diff against notice: data categories, purposes and lawful bases, third parties / processors, retention, data subject rights, international transfers.
3. Output: covered / missing / conflicting + suggested language for each gap + timing recommendation.

**Schedule:** Set up a recurring reminder in your own scheduler (calendar, task manager, or CI) to run `/privacy-legal-uk:policy-monitor` weekly.

```
/privacy-legal-uk:policy-monitor
/privacy-legal-uk:policy-monitor "We want to start using behavioural data to personalise onboarding emails"
```

---

# UK Privacy Notice Monitor

## Purpose

Privacy notices drift from practice in one direction: practice moves forward, notice stays behind. A DPIA approves a new data category. A DPA is signed with a processor not mentioned anywhere. A triage result approves a new use case with a disclosure requirement the notice doesn't yet make. Months later, someone reads the notice and it doesn't reflect what actually happens — a transparency failure under UK GDPR Art.5(1)(a) and Art.13/14.

This skill catches the drift before it becomes an ICO enforcement issue — either by crawling the outputs folder, or by answering the direct question: "we're about to start doing X, what does that mean for the notice?"

The output is always the same: here's the gap, here's the suggested language.

**UK GDPR Art.5(1)(a) lawfulness, fairness, and transparency** requires that personal data is processed lawfully, fairly, and in a transparent manner. A notice that doesn't reflect current practice is a transparency failure — and a potential ICO enforcement finding.

---

## Load current state

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`:
- `## Who we are` → `## Regulatory footprint` — the UK regimes in scope (UK GDPR / DPA 2018 / PECR / Children's Code / NIS / OSA / sector-specific)
- `## Privacy notice commitments` — the commitments extracted from the published notice
- `## Outputs` — outputs folder path, privacy notice document location, last sweep date

If `## Outputs` contains `[PLACEHOLDER]`:
> "Outputs aren't configured yet. I can still run a direct-query check — describe what you're planning to do and I'll diff it against your current notice. To enable the crawl sweep, run `/privacy-legal-uk:cold-start-interview` and provide the outputs folder path."

Read the actual privacy notice document from the path in `## Outputs`. The commitments in the config CLAUDE.md are a summary; the actual document is authoritative for suggesting edits.

### Privacy commitments live on multiple surfaces — sweep all of them

The privacy notice is one surface. UK organisations make binding commitments in at least five more places that the ICO actively scrutinises for inconsistencies:

1. **Cookie consent banners / CMPs.** The consent management platform promises specific cookie categories and purposes. PECR Reg.6 requires prior informed consent for non-essential cookies — the CMP and the notice must be consistent. If the notice says "we use analytics cookies" and the CMP only offers "strictly necessary," there is a conflict. ICO has enforced against CMP misconfigurations. `[PECR-REG.6] [ICO-GUIDANCE]`
2. **App Store privacy labels.** Apple App Privacy and Google Data Safety are self-declared and visible to users and regulators. A controller that updates the privacy notice but not the App Store label has a user-visible inconsistency. Check: when was the label last updated? Does it match the current notice's data categories, purposes, and sharing?
3. **In-product consent flows.** The actual screens where data subjects make data-use choices (onboarding consents, settings toggles, "we've updated our notice" dialogs). The notice says what you do; the consent flow says what the data subject agreed to. They must match — particularly for consent as a lawful basis.
4. **Children's Code commitments.** Where the Children's Code (DPA 2018 s.123) applies, the ICO expects controls and transparency standards consistent with the 15 Children's Code standards. These may create additional notice obligations beyond standard Art.13/14 requirements.
5. **Sector-specific notices.** Where a sector-specific regime applies (e.g., ICO Children's Code, NHS DSP Toolkit notice requirements, FCA-regulated firm data-handling), the sector-specific notice obligations run in parallel with the general notice. Check these separately.

**Add fields to the practice profile for each surface's location and last-updated date.** The sweep checks each against the current notice and flags divergence: "Privacy notice updated [date]. App Store label last updated [earlier date] — may not reflect the new data category. CMP last configured [date] — verify cookie purposes match the notice."

### Sector-specific notice obligations

If `## Regulatory footprint` includes any of the following, the sweep diffs practice against that obligation in addition to the privacy notice:

| Footprint entry | Obligation | What to flag |
|---|---|---|
| **Children's Code (DPA 2018 s.123)** | ICO Age Appropriate Design Code — 15 standards including notice and transparency requirements for children | Outputs implying new data categories, new processing purposes, or new vendors affecting children's data that aren't reflected in notice or CMP; Children's Code-specific consent requirements |
| **PECR** | Cookie notice / consent mechanism; direct marketing opt-in/soft-opt-in records | Outputs implying new cookie use, new direct-marketing channels, or changes to the consent/soft-opt-in mechanic |
| **NIS Regulations 2018** | Competent authority notifications; security incident reporting | Outputs implying changes to data-processing scope that affect NIS notification obligations |
| **OSA 2023** | Transparency and user information obligations for in-scope services (Ofcom regulated) | Outputs implying processing for content moderation, age assurance, or user safety that has notice implications |
| **NHS / DSP Toolkit** | NHS Data Security and Protection requirements | Outputs implying new data categories, new third-party processors, or changes to data flows that require DSP Toolkit notice updates |

**If no sector-specific obligation is configured for a regime in the footprint**, surface this as a standing gap on every sweep, not a one-time finding.

**Ask the user if the footprint is ambiguous.** If `## Regulatory footprint` says "UK GDPR" but the outputs scan surfaces children's data, health data, or financial data categories, surface the footprint-vs-practice mismatch.

---

## Mode detection

**Sweep mode:** No argument, `--sweep`, or triggered by schedule.
→ Scan the outputs folder. Diff all outputs since last sweep against current notice.

**Direct query mode:** User provides a description of a proposed new practice.
→ Diff that practice against current notice. Suggest updates.

---

## Mode 1: Sweep

### Determine scope

Read `## Outputs` → **Last policy sweep** date. Scan for output files in the outputs folder that are dated after that date. If no date is recorded, scan all files and note: "First sweep — scanning all outputs."

If the outputs folder is empty or has no new files since the last sweep:
> "No new outputs since [last sweep date]. Notice appears current with recent practice. Next scheduled sweep: [date]."

Update **Last policy sweep** in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` to today's date after completing the sweep.

### What to read in each output type

**DPIAs:**
- Extract: data categories processed, purposes and lawful bases, third-party processors / sub-processors, retention periods, international transfers and transfer mechanisms, data subject rights implications, any conditions placed on the processing
- Flag: anything not present in the current notice commitments

**DPA reviews (signed or approved):**
- Extract: processors added, data locations agreed, processing purposes covered, any Art.28 obligations to data subjects created by the DPA terms, international transfer mechanisms used
- Flag: processors not mentioned in the notice (if notice names them), new processing categories, new data locations, new transfer mechanisms not in the notice

**Triage results (DPIA REQUIRED / PROCEED outcomes):**
- Extract: what was approved, any conditions imposed that imply a public commitment (e.g., "disclosure to affected data subjects required before launch")
- Flag: approved practices not covered by notice, conditions that require notice language

**DSAR responses:**
- Extract: any new data categories surfaced that weren't in previous DSAR responses, any new systems added to the systems list
- Flag: data categories collected but not stated in notice

### Gap identification

For each flagged item, assess:

**REQUIRED update** — the notice makes a commitment that this output contradicts, or the processing is occurring and the notice has no coverage at all. Not updating creates a transparency failure under UK GDPR Art.5(1)(a) and Art.13/14.

> Example: Notice says "we collect name, email, and account information." A DPIA approved collection of precise location data. Notice says nothing about location data. That's a REQUIRED update — you are processing data you haven't disclosed to data subjects.

**ADVISABLE update** — the notice is silent but not in conflict. The processing is defensible without updating, but cleaner and more transparent with it.

> Example: Notice says "we may share data with service providers who assist us in operating our service." A DPA was signed with a new analytics provider. Notice doesn't name the provider but doesn't exclude them either. Advisable to be more specific, especially if the provider does anything data subjects would not expect.

**PECR-specific flag** — where the gap relates to cookies or electronic marketing, a PECR consent / notice issue is flagged separately (not just a UK GDPR notice gap).

### Sweep output format

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role]

# UK Privacy Notice Monitor — Sweep Report

**Date:** [date]
**Outputs scanned:** [N files] | **New since last sweep:** [N files]
**Gaps found:** [N] REQUIRED | [N] ADVISABLE | [N] PECR-specific

---

## REQUIRED updates

### [Gap 1 short name]

**Source:** [filename / output type that triggered this]
**UK GDPR obligation:** [Art.5(1)(a) transparency / Art.13(2) / Art.14(2) / other]
**What's happening:** [plain description of the new practice]
**Current notice:** [quote the relevant section — or "No coverage"]
**Gap:** [what's missing or inconsistent]

**Suggested language:**
> *Add to [section name]:*
> "[Drafted notice text — specific, consistent with house style of the actual notice]"

---

[repeat for each REQUIRED gap]

---

## ADVISABLE updates

### [Gap name]

**Source:** [filename]
**What's happening:** [description]
**Current notice:** [quote or "Silent"]
**Suggested language:**
> *Add to / update [section]:*
> "[Drafted text]"

---

## PECR-specific flags

### [PECR gap name]

**Source:** [filename]
**PECR provision:** [Reg.6 (cookies) / Reg.22 (email/SMS marketing) / other]
**Issue:** [description]
**Action required:** [specific PECR compliance action — consent mechanism, notice update, etc.]

---

## Sectoral notice coverage

| Regime | Notice configured | Last updated | Status |
|---|---|---|---|
| Children's Code | [path / not configured] | [date] | 🟢 Current / 🟡 Review / 🔴 NOT CONFIGURED |
| PECR consent mechanism | [path / not configured] | [date] | |
| [Other sector] | | | |

---

## No action needed

[List outputs scanned where no gaps were found — confirms they were reviewed]

---

## Next steps

- [ ] Review REQUIRED updates — each needs a decision before the associated feature/processing goes live (or immediately if already live — prompt action reduces ICO enforcement risk)
- [ ] Review ADVISABLE updates — lower urgency but worth addressing at next notice refresh
- [ ] Review PECR-specific flags — PECR is enforced independently by the ICO
- [ ] Update App Store privacy label / Google Data Safety label if data categories changed
- [ ] Next scheduled sweep: [date]
```

---

## Mode 2: Direct query

### Parse the proposed practice

Extract from the user's description:
- What personal data is being collected or processed?
- What's the purpose and proposed lawful basis?
- Who else is involved (processors, joint controllers, third parties)?
- Who are the data subjects? Children?
- Is there any automated decision-making or profiling?
- Any new disclosure to data subjects required?
- Any cookies or electronic marketing implications (PECR)?
- Any international transfer?

If the description is vague, ask one clarifying question before proceeding. This mode should be fast.

### Policy diff

Check the proposed practice against every relevant section of the current notice:

| Check | Current notice says | Proposed practice | Verdict |
|---|---|---|---|
| Data categories | [what notice lists] | [new category if any] | 🟢 Covered / 🟡 Gap / 🔴 Conflict |
| Purposes | [stated purposes] | [new purpose] | |
| Lawful bases | [bases stated in notice] | [basis for new purpose] | |
| Third parties / processors | [stated parties] | [new party if any] | |
| International transfers | [stated transfers + mechanisms] | [new transfer if any] | |
| Retention | [retention commitment] | [implied retention] | |
| Data subject rights | [rights offered] | [any new rights implications] | |
| Disclosure / notice | [what notice says about telling data subjects] | [what this practice requires under Art.13/14] | |
| PECR | [CMP / direct marketing commitment] | [any new PECR implications] | |
| Children's Code | [children's Code commitments if applicable] | [children's Code implications] | |

### Direct query output format

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role]

# UK Privacy Notice Check: [Proposed practice in one line]

**Bottom line:** [NOTICE UPDATE REQUIRED / ADVISABLE / NO UPDATE NEEDED]

---

## What's covered

[List aspects of the proposed practice already addressed by the current notice — confirms they don't need to change]

## What's missing

### [Gap 1]

**Current notice:** [quote or "Silent"]
**UK GDPR obligation:** [Art.13(2)(d) recipients / Art.13(2)(f) transfers / other]
**What's needed:** [why this gap matters]

**Suggested language:**
> *Add to [section]:*
> "[Drafted text]"

## What conflicts

### [Conflict 1 — if any]

**Current notice says:** [quote]
**Proposed practice does:** [what conflicts]
**Resolution:** [which one needs to change and why]

---

## PECR implications

[If applicable: specific PECR obligation triggered, consent/notice requirement, suggested action]

---

## Timing

[If any gap is REQUIRED: "Notice update should happen before this practice goes live."
If ADVISABLE: "Can proceed; update at next notice refresh."]
```

---

## Suggested language quality standards

Notice language should:
- Match the voice and style of the existing notice (read the actual document, not just the config CLAUDE.md summary, before drafting)
- Be specific enough to be meaningful but not so specific that routine changes break it ("processors who assist us in operating our service" ages better than naming every processor)
- Not make commitments the team can't keep (e.g., don't draft "we will never transfer data outside the UK" if transfers occur)
- Flag where a broader notice position change might be needed, not just a sentence addition
- For lawful basis statements: be specific — not just "we process your data to improve our services" but "we process your data to improve our service on the basis of our legitimate interests (UK GDPR Art.6(1)(f)) in developing and improving our products"

When drafting, always say which section to add to. If the right section doesn't exist, say so and suggest creating it.

**UK GDPR Art.13/14 required content checklist** — if updating the notice, verify the updated notice still contains all mandatory Art.13/14 content: `[UK-GDPR-ART.13] [UK-GDPR-ART.14]`

- Identity and contact details of the controller
- Contact details of the DPO (where applicable)
- Purposes and lawful bases for each processing activity
- Legitimate interests (where used) — the specific interest
- Recipients or categories of recipients
- International transfers and transfer mechanisms
- Retention periods or criteria
- Data subject rights (access, rectification, erasure, restriction, portability, objection, Art.22 rights)
- Right to withdraw consent (where consent is the basis)
- Right to complain to the ICO
- Whether providing data is a statutory or contractual requirement and consequences of failure to provide
- Existence of automated decision-making and profiling (where applicable)

---

## Schedule integration

Set up a recurring reminder in your own scheduler (calendar, task manager, or CI) to run `/privacy-legal-uk:policy-monitor` weekly or after any new DPIA or DPA review is completed.

Whenever the sweep runs, it updates `## Outputs` → **Last policy sweep** in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

If the sweep surfaced more than ~10 drift findings, or any time the user asks: offer the dashboard. Shape the offer for this output — counts by surface (notice clause / DPIA / DPA / triage), counts by severity, and a sortable grid of findings with source artefact and recommended remediation.

## What this skill does not do

- It doesn't update the privacy notice itself — it drafts suggested language and flags decisions, but a DPO or solicitor reviews and approves every change.
- It doesn't catch new UK legislation — that's `reg-gap-analysis`. This skill monitors internal practice drift, not external legal changes.
- It doesn't enforce that outputs are saved — if the team isn't saving DPIAs to the configured folder, the sweep won't find them. The direct-query mode works without saved outputs.
- It doesn't read email or Slack for informal decisions — only structured outputs saved to the configured folder.
