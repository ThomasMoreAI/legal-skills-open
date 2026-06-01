---
name: eligibility-screening
title: /eligibility-screening
description: Funding-source-aware screening — income, assets, residency, citizenship/ immigration status, conflicts, and case-type priority. Produces a screening result the intake specialist or staff attorney reviews and the managing attorney approves. Does NOT decide acceptance. Use at the front of every intake, before /client-intake, when a prospective client first contacts the office.
author: lawdroidAI
author_url: https://github.com/lawdroidAI/legal-aid-plugin/tree/main/skills/eligibility-screening
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# /eligibility-screening

1. Load `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` → funding sources, eligibility guidelines, jurisdictions, supervision style, flag triggers.
2. Use the workflow below.
3. Walk through screening in order: income → assets → residency → citizenship/immigration → conflicts → case-type priority.
4. Produce a screening result with classification, applicable funding sources, and any flags.
5. Output the screening result with AI-assisted label, funding-restriction flags, and supervision routing.

```
/legal-aid:eligibility-screening
```

---

# Eligibility Screening

## Purpose

Eligibility screening is the front of the funnel and the most common reason a legal aid office ends up in compliance trouble. Income, assets, residency, citizenship, conflicts, and funder-specific case-type rules all have to be cleared before the office takes on a matter, and the rules vary by funding source on the same matter.

This skill structures the screening, applies the office's configured eligibility guidelines, surfaces flags for managing-attorney review, and produces a result the intake specialist can verify and the managing attorney can approve.

**What it doesn't do:** decide acceptance. Acceptance is the managing attorney's call. This skill recommends.

## Load context

`~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` → funding sources, eligibility guidelines (income, assets, residency, citizenship policy, priority case types, out-of-scope case types), conflict-check process, supervision style, flag triggers.

## Read the practice-area guide if one exists

Check for a practice-area guide at `~/.claude/plugins/config/claude-for-legal/legal-aid/guides/<practice-area>.md`. If one exists for the area this screening is likely heading into, read its priority criteria and any practice-area-specific eligibility nuances (DV exceptions to citizenship restrictions, elderly age cutoff, immigration-specific bars). If one doesn't exist, use the office defaults from CLAUDE.md.

## Workflow

### Step 1: Frame the screen

Open with a short framing line. Do not lead with eligibility questions — lead with the situation, so the prospective client doesn't feel pre-screened out before they've explained why they called.

> "Tell me what's going on — what brought you to the office today?"

Capture the narrative in the prospective client's own words. This determines practice area, urgency, and which funding source's rules apply. **It does not decide eligibility yet.**

### Step 2: Practice-area routing and urgency

From the narrative, identify:
- Primary practice area (housing / family / consumer / immigration / public benefits / civil rights / other)
- Cross-area issues (mark every one — the office may handle one and refer the other)
- Urgency: court date, lockout, deadline, safety issue, irreversible harm imminent

Urgent matters get screened on a fast path: a quick income screen, a fast conflict check, and immediate managing-attorney routing. Do not run a full screen on someone whose lockout is tomorrow morning — flag the urgency and route.

### Step 3: Income screen

Read the office's income standard from CLAUDE.md. Common patterns:

| Funding source | Typical standard | Office variant |
|---|---|---|
| LSC | 125% FPL | Read CLAUDE.md |
| IOLTA / state appropriation | 200% FPL (varies) | Read CLAUDE.md |
| Elderly programs | 300% FPL or no cap (varies) | Read CLAUDE.md |
| DV / VAWA / VOCA | Often no income test for DV-related matters | Read CLAUDE.md |
| Foundation-specific | Per grant terms | Read CLAUDE.md |

Ask:
- Household size (everyone living in the household, including children)
- Monthly gross income from all sources (wages, benefits, child support received, contributions from others)
- Income volatility (was last month representative? is income about to change?)

Output a comparison against each funding source the office runs, **not just one**. A matter may not qualify for LSC funding but may qualify under IOLTA — the screen surfaces both.

**Do not state a specific FPL dollar figure as if you know the current year's number.** Tag every dollar comparison with `[VERIFY: current FPL table for household size N]`. The intake specialist verifies against the office's posted FPL chart, which the managing attorney is responsible for keeping current.

### Step 4: Asset screen

Read the office's asset rules from CLAUDE.md. Ask about:
- Liquid assets (checking, savings, cash on hand) — flag the cap if applicable
- Primary residence (typically excluded — confirm in CLAUDE.md)
- Vehicle(s) — typically one excluded, additional may count
- Other assets that may or may not count per the office's rules

If the office has no asset test for this funding source, skip this step and note it in the output.

### Step 5: Residency

Read the office's residency rules. Ask about:
- State of residence
- County of residence (if the office is county-scoped)
- Length of residence (rarely required, but some funders require it)
- Where the legal matter is venued (some offices serve the venue rather than the residence)

Flag any mismatch between residence and venue for managing-attorney review.

### Step 6: Citizenship / immigration status

This is the most sensitive step. Approach with care.

LSC-funded programs operate under 45 CFR § 1626, which restricts representation of certain aliens with explicit exceptions for:
- DV survivors (regardless of status, for matters related to the abuse)
- Victims of trafficking, sexual assault, and certain other crimes
- Specific visa categories (U visa applicants, T visa applicants, certain VAWA applicants, etc.)
- Other narrow exceptions

Non-LSC funding (IOLTA, private foundations, state appropriation) typically has different — and usually broader — rules. An office may serve a person with non-LSC funds even when LSC restrictions would prevent serving them with LSC funds.

The skill:
- Reads the office's citizenship/immigration policy from CLAUDE.md
- Asks the prospective client about status only to the extent the office's policy requires it for screening
- Does **not** ask for documentation or specific case numbers — the screening is about funding eligibility, not status verification
- Flags `[FUNDING RESTRICTION: LSC § 1626 — confirm exception or non-LSC funding source]` whenever the matter may engage LSC alien restrictions
- Routes to managing-attorney review whenever there's ambiguity

**If the prospective client appears to be a DV survivor or trafficking victim and the matter relates to that, flag the relevant § 1626 exception by name and route to the office's DV/trafficking specialist if one exists.**

Never tell a prospective client "you are not eligible because of your status." That is a managing-attorney determination, made after the screen.

### Step 7: Conflict check

Per the office's process described in CLAUDE.md. At minimum:

- Opposing party name(s) — does the office represent or have represented them?
- Related parties — anyone else the office might have a conflict with?
- Positional conflicts — is this case asking for something that would hurt another office client?
- Prior contact — has the office previously turned this person away, taken brief advice, or had a consultation?

If the office's case management system is connected, run the check against the CMS. If not, output the names and the structured query the intake specialist should run manually.

Flag for managing-attorney review. Don't resolve the conflict — surface it.

### Step 8: Case-type priority

Read the office's priority case types and out-of-scope case types from CLAUDE.md. Classify the matter:

| Classification | Means |
|---|---|
| **Priority case type — accept track** | Falls within the office's stated priorities and capacity exists |
| **Standard case type — assess capacity** | In scope; managing attorney weighs capacity |
| **Out-of-scope — refer** | Outside practice areas or funder-restricted |
| **Fee-generating — refer** | LSC-restricted if office is LSC-funded |
| **Mixed (priority for one funding source, out-of-scope for another)** | Surface the dual classification |

Note any specific funder restrictions that apply, by funder, with the rule cite where applicable.

### Step 9: Output the screening result

## Output

```markdown
# Eligibility Screening: [Caller name or ID]

---
[AI-ASSISTED DRAFT — requires staff analysis and managing-attorney review]

**Privilege and confidentiality.** This screening contains information disclosed in the course of a prospective client consultation and is subject to Rule 1.18 duties of confidentiality regardless of whether the office accepts the matter. Keep it in the office's privileged file store; distribution decisions go through the managing attorney.
---

**Date:** [date] | **Screener:** [intake specialist] | **Practice area:** [primary + any cross-area] | **Urgency:** [urgent / time-sensitive / standard]

## Bottom-line recommendation

[Accept under [funding source] | Decline / refer because [reason] | Needs managing-attorney review on [specific issue]]

## Caller's situation (in their words)

[Narrative as given, before legal categorization]

## Screening result by category

### Income
- Household size: [N]
- Monthly gross income: $[amount] `[VERIFY: client-stated — confirm at intake]`
- vs. LSC standard (125% FPL, [N]-person household): `[VERIFY: current FPL table]` — [over / under / at]
- vs. IOLTA standard ([office's IOLTA standard]): [over / under / at]
- vs. [other funding sources]: [over / under / at]

### Assets
- [Per office's rules]

### Residency
- State: [state] | County: [county] — [in service area / out of service area / partially]
- Matter venued in: [court / agency] — [match / mismatch flag]

### Citizenship / immigration
- Status disclosed: [per office's policy on what to ask]
- LSC § 1626 implications: [no engagement / exception applies (cite) / restriction applies — non-LSC funding required]
  `[FUNDING RESTRICTION: ...]` if applicable

### Conflicts
- Opposing party: [name(s)] — [CMS clear / CMS hit — see entry [ID] / manual check needed]
- Related parties: [list]
- Positional: [any concerns]

### Case-type priority
- Practice area: [housing / family / etc.]
- Classification: [priority / standard / out-of-scope / fee-generating / mixed]
- Out-of-scope flags: [list, with rule cite if funder-restricted]

## Cross-practice-area flags

[Any issue outside the primary area that the office may want to address, refer, or both]

## Funding-source matrix

| Funding source | Income OK | Assets OK | Status OK | Case type OK | Result |
|---|---|---|---|---|---|
| LSC | [Y/N/?] | [Y/N/?] | [Y/N/?] | [Y/N/?] | [Eligible / Ineligible / Needs review] |
| IOLTA | [Y/N/?] | [Y/N/?] | [Y/N/?] | [Y/N/?] | [Eligible / Ineligible / Needs review] |
| [Other] | | | | | |

## Managing-attorney review flags

- [Any item that should be reviewed before acceptance, e.g., "Income within 5% of LSC cap; verify against pay stubs"]
- [Any FUNDING RESTRICTION flag]
- [Any conflict requiring resolution]
- [Any urgency requiring fast-path routing]

## Suggested next step

- If accept-track: route to `/client-intake` under [funding source]
- If decline: route to `/client-letter referral` with referral candidates [list]
- If needs-review: queue per supervision style (formal queue / configurable flag / case rounds)

## Premises this screening rests on

- [Each premise the screen used, e.g., "LSC 2024 FPL table applies until [date]"]
- [Office's eligibility profile last updated: [date from CLAUDE.md]]

## Verification prompts before relying on this screen

- Verify household size and income against documentation at intake (pay stubs, benefit letters, last filed tax return)
- Verify residency against any document available (lease, utility bill, ID)
- Run the CMS conflict check if not already automated
- Confirm current FPL table date and the office's current eligibility profile
- Re-run any FUNDING RESTRICTION flag against current funder guidance
```

## Cross-skill propagation

- Any `[FUNDING RESTRICTION: ...]` raised here propagates into `/client-intake`, `/draft`, `/memo`, and `/status` for the matter if accepted.
- Any conflict flag propagates and is repeated in every output until resolved or waived in writing by the managing attorney.
- The funding-source matrix becomes part of the case file — `/lsc-report` reads it for CSR categorization.

## What this skill explicitly does not do

- Decide acceptance.
- State current FPL dollar figures from memory.
- Verify immigration status documentation.
- Resolve conflicts.
- Override the office's eligibility profile.
- Run on a prospective client without the framing line in Step 1.
