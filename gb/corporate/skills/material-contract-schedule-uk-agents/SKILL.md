---
name: material-contract-schedule-uk-agents
title: /material-contract-schedule
description: Build the material contracts disclosure schedule from diligence findings, applying the SPA/APA's Material Contract definition and formatting per the agreement's schedule format. Use when user says "build the contracts schedule", "disclosure schedule", "schedule to the SPA", "material contracts list", or when drafting disclosure schedules under English law.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/corporate-legal-uk/skills/material-contract-schedule
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: corporate
language: en
---

# /material-contract-schedule

1. Load SPA/APA → Material Contract definition + schedule format.
2. Use the workflow below.
3. Apply definition to diligence findings. Flag edge cases.
4. Format per agreement. Consent overlay feeds closing checklist.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The SPA/APA has a warranty: "Schedule [X] lists all Material Contracts." This skill builds that schedule from the diligence findings — which contracts are material per the agreement's definition, in the format the agreement requires. In English law M&A this is typically a warranty schedule delivered at exchange (and updated to completion on a locked-box deal) or at completion.

## Load context

- SPA/APA draft — for the definition of "Material Contract" and the schedule format
- `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → materiality thresholds (may differ from the agreement definition — use the agreement's)
- Diligence findings from diligence-issue-extraction — contract-level data

## Workflow

### Step 1: Get the definition

Pull the definition of "Material Contract" from the SPA/APA — the agreement definition controls. Deal-structure differences (share purchase vs. asset purchase / business transfer) can change how a prong is interpreted:

- **Share purchase:** target's contracts remain in force (no assignment required). Change-of-control provisions may still be triggered. Warranties speak as at exchange / completion.
- **Asset purchase / business transfer:** contracts must be novated or assigned with counterparty consent unless the contract permits assignment without consent. TUPE applies to employees assigned to the business.

Regulated-industry overlays (financial services, healthcare, defence, government contracting) can add consent requirements under FSMA 2000 (FCA authorisation, PRA consent), sector regulators, or Crown Proceedings Act 1947 (Crown contracts).

Common prong categories to look for in the SPA/APA definition — these are not a substitute for reading the agreement, and the list the agreement uses controls:

- Value threshold (annual or aggregate — typically expressed in £)
- Term length
- Change-of-control or anti-assignment provision
- Exclusivity or non-compete
- Top N customer or supplier contracts
- Real property leases / licences
- IP licences (in-bound and out-bound)
- Related-party agreements (CA2006 s.190 thresholds relevant)
- Government / public sector contracts
- Contracts outside the ordinary course
- Contracts with regulators or public bodies

The agreement's definition is the test. Apply it mechanically — every contract that meets any prong in the agreement's definition goes on the schedule.

### Step 2: Apply the definition to the findings

For each contract reviewed in diligence:

| Contract | Meets prong(s) | Include |
|---|---|---|
| [name] | [£X+ annual value; CoC provision] | Yes |
| [name] | [none] | No |

**Edge cases to flag for human decision:**
- Contract is £X-1 (just under threshold) but important to the business
- Contract meets a prong but is being terminated anyway
- Oral agreements or side letters that may or may not count
- Contracts silent on assignment where governing law default matters (English law: assignment of the burden of a contract generally requires counterparty consent; assignment of the benefit may be possible without consent — `[model knowledge — verify]`)

### Step 3: Gather schedule data

For each included contract, the schedule typically needs:

| Field | Source |
|---|---|
| Counterparty name (full legal name) | Contract |
| Contract title/type | Contract |
| Date | Contract |
| Term / expiration | Contract |
| Annual/total value (£) | Contract or management data |
| Which materiality prong it meets | Step 2 analysis |
| Consent required for the deal | Diligence finding |
| VDR reference | Diligence inventory |
| Governing law | Contract |

Pull from existing diligence extractions. If a field is missing, flag it — don't guess.

### Step 4: Format per the agreement

Disclosure schedules in English-law SPAs have a format — usually a numbered list or a table, sometimes with sub-parts by contract type. Match the format of the other schedules in the draft agreement.

```markdown
## Schedule [X] — Material Contracts

The following are the Material Contracts as at the date hereof:

### (a) Customer Contracts

1. [Agreement Title], dated [date], between [Target] and [Counterparty].
   [Brief description if the format calls for it.]
   [VDR: path]

2. [...]

### (b) Supplier Contracts

[...]

### (c) Real Property Leases

[...]

[etc. — sub-parts per the agreement's definition structure]
```

### Step 5: Consent tracking overlay

Separately (not in the schedule itself — this is internal), track which scheduled contracts require consent.

> The consent overlay and any pre-exchange working draft of the schedule are derived from privileged diligence materials and inherit their LPP status. Distribution beyond the privilege circle can waive privilege. The schedule itself, once delivered as a warranty schedule in the executed SPA/APA, is a deal document and is not privileged; strip any internal annotations before delivery.

| Schedule # | Counterparty | Consent required | Basis | Status | Owner | Due |
|---|---|---|---|---|---|---|
| [X](a)(1) | [name] | Yes — CoC §12.2 | Anti-assignment | Requested | [name] | [date] |

**UK-specific consent considerations:**
- English law assigns the burden of a contract only with consent; the benefit may be assignable without consent depending on the clause and the nature of the contract.
- Government contracts: novation requires Crown consent; formal Crown novation deed required.
- FCA-authorised entities: change of control requires Part XII approval; allow 3-6 months.
- Regulated utilities (Ofgem, Ofwat, Ofcom, CQC): licence transfer or consent from relevant regulator.

This feeds closing-checklist.

## Cross-check

Before delivering:

- Every contract that met a prong is on the schedule (completeness)
- No contract is on the schedule that doesn't meet a prong (no over-disclosure — it's a warranty, not a data dump)
- Schedule is consistent with the other warranties (a contract on Schedule [X] that creates a charge should also be on the charges schedule)
- Every entry has a VDR cite so buyer's solicitors can find the underlying doc

## Handoffs

- **From diligence-issue-extraction:** Contract-level findings are the input.
- **To closing-checklist:** Consent items go on the checklist.

## What this skill does not do

- It doesn't decide the materiality definition — that's in the SPA/APA.
- It doesn't obtain consents — it tracks which ones are needed.
- It doesn't draft the warranty — it populates the schedule the warranty references.
- It doesn't advise on whether TUPE applies — it flags the question; employment counsel advises.
