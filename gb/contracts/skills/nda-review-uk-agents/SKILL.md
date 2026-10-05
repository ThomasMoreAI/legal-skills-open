---
name: nda-review-uk-agents
title: NDA Review (UK)
description: 'Reference: fast triage of inbound NDAs into GREEN / YELLOW / RED under English law of confidence and common law principles. Built for sales and BD to self-serve before pinging legal. Loaded by /commercial-legal-uk:review when an NDA is detected.'
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/commercial-legal-uk/skills/nda-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: contracts
language: en
---

# NDA Review (UK)

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination outside the privilege circle, flag it and offer alternatives. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

Most inbound NDAs are fine. A few have landmines. This skill sorts them in under a minute so legal only reads the ones that matter.

**The goal:** a GREEN NDA should need nothing more than a signature. A YELLOW needs a solicitor's eyes on one or two specific things. A RED stops before anyone wastes time.

## UK legal framework

English NDAs are governed by the common law of confidence, primarily based on *Coco v AN Clark (Engineers) Ltd* [1969] RPC 41 (the three-limb test: the information must have a quality of confidence; it must have been imparted in circumstances importing an obligation of confidence; there must be actual or threatened unauthorised use). `[model knowledge — verify]`

There is no specific UK statute governing commercial NDAs. Key principles:
- **Springboard doctrine:** prevents a party from using confidential information to obtain an advantage, even where the information has subsequently become public. `[model knowledge — verify]`
- **Trade secrets:** UK Trade Secrets (Enforcement, etc.) Regulations 2018 provide additional protections for trade secrets (defined as not generally known/ascertainable, commercially valuable, subject to reasonable steps to maintain secrecy). `[model knowledge — verify]`
- **Perpetual confidentiality:** English courts will enforce perpetual obligations for trade secrets; for "mere" confidential information, a court may imply a reasonable time limit. Flag perpetual terms on non-trade-secret information. `[model knowledge — verify]`
- **Remedies:** injunction, account of profits, damages — courts apply balance of convenience for interim injunctions (*American Cyanamid* principles). `[model knowledge — verify]`
- **Scotland:** Scots law of confidence follows broadly similar principles to English law in this area, but under a distinct legal framework. `[model knowledge — verify]`

## Load the playbook first

**Which side?** Before applying the playbook, determine which side the company is on. Usually obvious: if the counterparty is a vendor or partner evaluating your product, you're sales-side; if you're evaluating theirs, you're purchasing-side. Mutual NDAs still have a side — whose paper is it.

**Before triaging anything, read `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` → `## Playbook` → the matching side → `NDA triage positions`.** If no `NDA triage positions` section exists, ask the user for their position on each applicable term and record it before proceeding.

If `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` doesn't cover a term, ask:

> Your playbook doesn't cover [term — e.g., "residuals clauses," "springboard post-termination obligations," "trade secrets vs. confidential information distinction"]. What's your default position — when should this be GREEN, when YELLOW, when RED? I'll add it to `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`.

Then record the answer and proceed.

## Scope check

**Before reviewing NDA-specific provisions, check whether the document is doing more than its name suggests.** UK commercial NDAs can hide: standstills, licensing grants, exclusivity, non-solicits, non-competes, IP assignments, right of first refusal, most-favoured-nation clauses, and arbitration/jurisdiction clauses that govern far more than confidentiality disputes.

If the NDA contains obligations beyond confidentiality: **auto-YELLOW regardless of the NDA-term analysis.** Flag the non-NDA provisions:

> This document is labelled an NDA but contains [standstill / licence grant / non-solicit / exclusivity / IP assignment / ROFR / MFN / broad arbitration]. It's more than an NDA. Route for solicitor review.

Do not silently push a document labelled "NDA" through NDA triage when the substantive obligations are a services agreement, a term sheet, or a covenant package in NDA clothing.

## The triage

Classify the NDA into one of three buckets by applying the positions from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. The bucket definitions below are stable; the *criteria* that fill each bucket come from the playbook.

### GREEN — route to signature

The NDA satisfies every position in the team's playbook, and no term triggers a RED flag per the playbook.

**GREEN requires solicitor-reviewed playbook positions.** GREEN is the only path to signature without solicitor review. It cannot be issued against default or absent positions. Before issuing GREEN, check: does the practice profile have a solicitor-reviewed `## NDA triage positions` section? If not:

> I can't issue GREEN without solicitor-reviewed NDA positions in your practice profile. Run `/commercial-legal-uk:cold-start-interview --full` with your commercial solicitor to set them, or route this NDA for solicitor review. Issuing GREEN against defaults means a non-lawyer set the positions the next non-lawyer relies on.

**Output:**

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` `## Outputs`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## NDA Triage: [Counterparty]

GREEN — route to signature

### Executive Summary

No red flags identified under the playbook. Route for signature per standard process.

| Check | Status | Playbook reference |
|---|---|---|
| [Each playbook check] | [pass/fail] | [`~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` section] |

**Next step:** [Submit to CLM standard NDA workflow | Send to [approver from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`] for signature]
```

**Before proceeding past GREEN to signature:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> This step has legal consequences (countersigning an NDA binds the company). Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, NDA direction (mutual / one-way), the playbook checks run, anything the playbook didn't cover, what could go wrong if signed as-is, and the three things to ask the solicitor.]
>
> If you need to find a solicitor or barrister: the Solicitors Regulation Authority (SRA) at sra.org.uk has a Find a Solicitor tool for England & Wales. The Law Society of Scotland (lawscot.org.uk) covers Scottish solicitors. The Bar Council (barcouncil.org.uk) has a Find a Barrister directory.

Do not proceed past this gate without an explicit yes.

### YELLOW — needs a solicitor's eyes on specific items

One or more terms deviate from the playbook but aren't categorical deal-breakers, OR a term appears that the playbook doesn't address.

**Output:**

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## NDA Triage: [Counterparty]

YELLOW — flag for [approver name from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`]

### Executive Summary

- [One-line actionable edit, e.g. "Strike non-solicit clause (Section 6)"]
- [One-line actionable edit]

### Flagged items

**1. [Issue]** — Section [X]
   What: [one line]
   Why flagged: [one line — which playbook position this hits, or "playbook is silent on this"]
   **Legal risk:** [🔴/🟠/🟡/🟢] | **Business friction:** [🔴 Blocks deals / 🟠 Slows deals / 🟡 Confuses customers / 🟢 Invisible]
   Likely resolution: [accept / push back on X / depends on deal context]

[repeat for each flag]

### Everything else

| Check | Status | Playbook reference |
|---|---|---|
| [playbook checks that passed] | pass | [`~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` section] |

**Next step:** Ask [approver] about the flagged items, then route to signature if they're okay with it.
```

### RED — stop, talk to legal first

The NDA hits a position on the playbook's "never accept" list, or the structure of the agreement is incompatible with the team's standard posture.

**Output:**

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## NDA Triage: [Counterparty]

RED — do not submit, talk to legal first

### Executive Summary

- [One-line actionable edit, e.g. "Section 4 — route to Legal for review"]

### Critical issues

**1. [Issue]** — Section [X]
   > "[exact quote]"
   Why this is a problem: [specific risk; cite the playbook position it violates]
   **Legal risk:** [🔴/🟠/🟡/🟢] | **Business friction:** [🔴 Blocks deals / 🟠 Slows deals / 🟡 Confuses customers / 🟢 Invisible]
   Recommended response: [use our paper instead | push back with specific language | walk]

**Next step:** Send this triage to [Head of Legal or named escalation person from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`]. Do not send to CLM or approvals workflow. Do not tell the counterparty we'll sign.
```

## Redline granularity

**Edit at the smallest possible granularity.** Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks." Only replace a whole clause when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft.

## Jurisdiction assumption

This triage applies the governing-law and restrictive-covenant positions recorded in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. Key UK jurisdiction notes:
- **Non-solicits / non-competes:** Enforceable in English law if reasonable in scope, duration, and geographic extent — assessed under restraint of trade doctrine. `[model knowledge — verify]`
- **Scotland:** Scots law of confidence and restrictive covenants — broadly similar principles but under a distinct legal framework; check with a Scotland-qualified solicitor. `[model knowledge — verify]`
- **Perpetual confidentiality:** Enforceable for trade secrets; courts may limit "mere" confidential information to a reasonable period. `[model knowledge — verify]`

If the NDA involves a jurisdiction outside the team's configured posture, flag it and note that the triage may not transfer as written.

## Detailed check reference

For each check below, the bucket (GREEN/YELLOW/RED) is determined by `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. This skill lists the *categories* to check; it does not hardcode thresholds.

### Mutuality

Is the NDA mutual or one-way? Apply the team's position from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. If the playbook doesn't address one-way NDAs for this context, run the one-way questionnaire.

### Definition of Confidential Information

Check scope (marked-only vs. everything-disclosed), marking requirements, oral-disclosure confirmation windows. **Also check:** whether the definition expressly carves out or captures "trade secrets" — if so, the UK Trade Secrets (Enforcement, etc.) Regulations 2018 may provide additional protection but also impose stricter requirements (e.g., reasonable steps to maintain secrecy). `[model knowledge — verify]`

### Carveouts

The five standard carveouts typically present in a UK NDA:

1. Information that is or becomes public (other than through breach)
2. Information the receiving party already had prior to disclosure
3. Information independently developed without reference to the CI
4. Information received from a third party free from restriction
5. Information required to be disclosed by law or court order (with notice to discloser where legally permitted, subject to UK statutory and regulatory disclosure obligations)

**Additional UK flag:** Some UK NDAs include a carveout for disclosures required by FCA, CMA, FRC, ICO, or other UK regulatory bodies — check whether this aligns with the team's position.

### Residuals

A residuals clause lets the receiving party use information retained in unaided memory. Apply `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. If the playbook doesn't address residuals, ask.

### Term and survival

Check the initial term length, the post-term survival period for confidentiality obligations, and whether trade secrets are carved out with longer (potentially perpetual) protection. **Note:** under English law, perpetual confidentiality is valid for trade secrets; for ordinary confidential information, a court may limit it to a reasonable period. `[model knowledge — verify]`

### Restrictive covenants

Check for non-solicits (employee, customer), non-competes, exclusivity, and any restriction on who else the receiving party can engage with. **UK-specific:** Restrictive covenants in commercial contracts are enforceable in English law if reasonable — assessed under restraint of trade doctrine. Courts apply a stricter test than for ancillary restraints in business sale agreements. `[model knowledge — verify]`

### Costs / fee-shifting

Check for fee-shifting provisions. **Note:** English courts default to the "loser pays" rule (CPR 44) in litigation — a contractual fee-shifting clause may simply duplicate default law or could go further. Check whether any fee-shifting is mutual. `[model knowledge — verify]`

### Backup and archival carveout

Check whether the destruction/return clause includes an exception for standard backup and archival retention systems and any applicable statutory retention obligations under UK law (e.g., Companies Act 2006 records, HMRC record-keeping, Limitation Act 1980 limitation periods for documentary evidence). `[model knowledge — verify]`

### Governing law

Per `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` `## Playbook` → `Governing law and venue`. Note: "English law" and "UK law" are not the same — "English law" means England & Wales; "UK law" is not a legal system (Scotland, E&W, and NI are separate). Use precise language.

## Counterparty context

**Large corporate NDAs:** Major corporates generally won't negotiate NDAs. Calibrate: is the RED flag truly a deal-breaker, or is it "different from our form"? If the business relationship matters, the call is whether to accept their paper — escalate that decision, don't make it.

**SME NDAs:** Will usually take our paper. If their NDA has issues, the fastest path is often "let's use ours."

## Integration: CLM

If connected:
- GREEN → offer to create the CLM record in the standard NDA workflow
- YELLOW → offer to create it with a note attached listing the flagged items
- RED → do not create a record; the solicitor decides what happens next

## What this skill does NOT do

- It does not negotiate. It sorts.
- It does not draft an NDA. If the answer is "use our paper," the user pulls our form from CLM or document system.
- It does not make the call on YELLOW items. It surfaces them for a human.
- It does not state a position on any NDA term. Positions live in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`.

## Closing action

Read `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` → `## NDA triage preferences` → `closing_action`.

If configured, append the closing action verbatim at the end of every output.

If `closing_action` is not configured, append: "Route final NDA through your standard approval process."

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. The tree is the output; the solicitor picks.
