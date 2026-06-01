---
name: draft-lawdroidai
title: /draft
description: First draft of a common civil legal aid document — eviction answers, protective order petitions, demand letters, debt validation letters, benefits appeals, asylum declarations, motions to vacate default judgments, FOIA requests, fair hearing requests, and others. Reads practice-area templates from CLAUDE.md and the practice-area guide, applies jurisdiction-specific formatting, propagates funder-restriction flags from intake, marks every uncertain element. Explicitly a starting point requiring staff analysis and managing-attorney review. Use when a staffer needs a first draft of a pleading, letter, petition, declaration, or other document.
author: lawdroidAI
author_url: https://github.com/lawdroidAI/legal-aid-plugin/tree/main/skills/draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# /draft

1. Load `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` → practice-area templates, jurisdiction, local rules, supervision style, funder restrictions, escalation default.
2. Load the matter's intake summary (or eligibility-screening output if intake hasn't run). If no matter context exists, ask the staffer for the case-ID or to paste the relevant facts.
3. Read the practice-area guide at `guides/<practice-area>.md` if one exists.
4. Match document type to template — practice-area-specific from CLAUDE.md, office-specific template if uploaded, generic if neither.
5. Gather required facts from case notes. Flag missing facts as `[FACT NEEDED: ...]`; never guess.
6. Apply jurisdiction-specific formatting (caption, service block, signature line, court-specific local rules).
7. Propagate any `[FUNDING RESTRICTION: ...]` flag from intake. If the drafted action plausibly engages a new funder restriction, raise a new flag.
8. Check for unresolved conflict flags from intake. If present, refuse to draft and route to managing attorney.
9. Output draft with prominent AI-assisted label, inline `[VERIFY]` / `[UNCERTAIN]` / `[FACT NEEDED]` markers, supervision routing per office model.

```
/legal-aid:draft eviction-answer
/legal-aid:draft protective-order case=marisol-2026-04
/legal-aid:draft ssi-appeal
```

---

# Draft: First-Draft Document Generation

## Purpose

A staff attorney spends real hours producing first drafts of routine documents — eviction answers, protective order petitions, demand letters, benefits appeals, asylum declarations, debt validation letters, motions to vacate default judgments. Most of those drafts follow practice-area patterns the office has used hundreds of times. The lawyering is in the facts and the analysis; the structure is repeatable.

This skill generates the first draft from case notes and the office's templates, applies the right jurisdiction's formatting, flags every missing fact, surfaces every funder restriction that the drafted action might engage, and produces a draft the staffer reads critically, edits, and routes for managing-attorney review per the office's supervision model.

**What it explicitly does not do:** produce final work product. Every output is labeled, marked with inline `[VERIFY]` and `[FACT NEEDED]` tags, and gated by the supervision model. A staffer who treats this as final has misunderstood the tool.

## Sequencing and gates

The skill checks four conditions before drafting:

1. **Matter context exists.** If no case-ID is passed and no intake/screening output is in scope, ask the staffer to provide one or paste relevant facts. The skill does not draft from scratch with no context — that's how generic templates leak into production.

2. **Conflict flags from intake are resolved.** If intake raised a conflict flag that the managing attorney has not signed off on, the skill refuses to draft and routes back: "Intake on this matter flagged a conflict that hasn't been resolved by [managing attorney]. Drafting paused — get sign-off first, then re-run."

3. **Funding allocation is set.** If the matter is not yet allocated to a specific funder (or the eligibility-screening matrix is ambiguous), the skill flags this and asks the staffer to confirm with the managing attorney before drafting under a default allocation. The funder allocation determines what funder restrictions apply and what reporting the case rolls up into.

4. **Required practice area is in scope.** If the doc type doesn't match any practice area the office handles per CLAUDE.md, refuse: "[doc type] is in [practice area], which isn't a listed office practice area. Confirm with [managing attorney] that this matter is in scope before drafting."

## Load context

`~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` → practice-area templates, jurisdiction, supervision style, escalation default, funder restrictions, supervision-flag triggers.

The matter's case file → intake summary, eligibility-screening output, comms log, deadlines, any prior drafts and managing-attorney feedback.

`~/.claude/plugins/config/claude-for-legal/legal-aid/guides/<practice-area>.md` if one exists → red flags, escalation posture, review gates, funder-restriction overrides, local quirks, office-specific templates.

If the office has the LawDroid LIA-MCP or VIA-MCP connectors enabled and the matter has an associated upstream conversation, that conversation is referenced for client voice and tone (especially relevant for declarations and client letters), but never quoted verbatim — the client's words in a declaration are the client's, captured by staff, not pasted from a chat log.

## Workflow

### Step 1: Identify document and template

From the argument or the staffer's prompt, identify:
- Practice area (housing / family / consumer / immigration / public benefits / civil rights / elder / DV / other)
- Document type
- Whether a specific template applies (CLAUDE.md practice-area template, office-uploaded template, or generic)

If multiple templates could apply (e.g., the office has both a "demand letter — debt collection" and a "demand letter — landlord repair" in the consumer and housing practice areas), confirm with the staffer.

### Step 2: Identify required facts

Each document type has a fact requirement set. For example:

**Eviction answer:**
- Tenant name(s), address, lease term, monthly rent
- Notice received: date served, type (5-day pay-or-quit, 30-day no-cause, etc.), grounds
- Defendant's case theory (tender, habitability, retaliation, statutory defects, none)
- Any habitability conditions, dates, complaints made
- Subsidy involvement (Section 8, public housing, LIHTC)
- Filing court, docket number if known, hearing date

**Protective order petition:**
- Petitioner name, age, relationship to respondent
- Respondent name, last known address, age
- Incident(s) with dates, locations, witnesses
- Children involved (names, ages, current location)
- Firearms in respondent's possession or access
- Existing orders
- Safe address requirement (for confidentiality)

**Demand letter (collection defense):**
- Creditor or collector name, contact information
- Original debt amount, current claimed amount
- Account number, dates of activity
- Defendant's identity verification position
- Statute of limitations analysis (jurisdiction's SOL, age of debt)
- FDCPA / state UDAP violations alleged

Pull each from the matter's intake summary and prior drafts. For each missing fact, mark inline as `[FACT NEEDED: <specific fact> — needed for <where in draft>]`. Never guess.

### Step 3: Jurisdiction-specific formatting

Apply caption format, service block, signature line, and any local rules:

- Caption per court (case caption format varies by jurisdiction and court level)
- Title of court and division
- Case number (if known; else `[CASE NUMBER]`)
- Service block per local rule (some courts require certificate of service in the document; some require separate; some accept e-filing certificate)
- Signature line with bar admission and office contact per CLAUDE.md
- Any judge-specific preferences from the practice-area guide

If the office uploaded local rule supplements at cold-start, defer to them. If not, use state defaults and flag: "Format used: state default. Office did not upload local rules; confirm against current local rules of [court] before filing."

### Step 4: Funder-restriction propagation and net-new flagging

From the matter's intake output:
- Read every `[FUNDING RESTRICTION: ...]` flag still live on the matter
- Propagate each into a "Funder considerations" block in the draft, positioned where the relevant content begins

Then check whether the *drafted action* itself plausibly engages any funder restriction not already flagged:

- Drafting a class-action complaint under LSC funds → `[FUNDING RESTRICTION: LSC class-action prohibition — confirm funding allocation before filing]`
- Drafting any document soliciting attorneys' fees under LSC funds → `[FUNDING RESTRICTION: LSC fee-generating restriction — confirm allocation and managing-attorney approval]`
- Drafting an asylum-related filing under LSC funds for a client whose § 1626 status is ambiguous → `[FUNDING RESTRICTION: LSC § 1626 — confirm exception applies or matter is on non-LSC funds]`
- Drafting a DV-related document where the safe address could appear → `[CONFIDENTIALITY: VAWA / state-DV-confidentiality — review address handling before filing]`

Each net-new flag goes at the top of the draft above the document text, and the relevant inline location.

### Step 5: Draft generation

Generate the document using:
- The practice-area template (CLAUDE.md / office-specific / generic, in that priority)
- Facts pulled from the matter
- Jurisdiction-specific formatting
- Practice-area guide local rules and judge preferences if applicable

Mark inline:
- `[FACT NEEDED: ...]` — missing required fact
- `[VERIFY: ...]` — claim included but should be verified before filing (citations, dates, legal standards)
- `[UNCERTAIN: ...]` — language the skill is unsure about; the staffer reviews and edits
- `[STAFF REVIEW: ...]` — section that requires the staffer's own analytical contribution, not the skill's

For citations: every cite is tagged `[VERIFY: cite — check current]`. Even known-good cites get this tag because the citation database may have updated.

### Step 6: Supervision routing

Per the supervision style in CLAUDE.md:
- **Formal queue:** Output is labeled "Routed to [managing attorney] review queue" and the next-action note is "Wait for managing-attorney sign-off in queue before any further work on this document."
- **Configurable flags:** If any review-gate trigger from the practice-area guide is hit, the output is labeled "CHECK WITH MANAGING ATTORNEY BEFORE FILING/SENDING." If no trigger, standard verification prompts only.
- **Lighter-touch:** Standard verification prompts; no additional gates.

### Step 7: Output

## Output

```markdown
# Draft: [Document type] for [Case ID]

---
[AI-ASSISTED DRAFT — requires staff analysis and managing-attorney review per office supervision model]

**Practice area:** [area] | **Funder allocation:** [funder(s)] | **Generated:** [date]
**Template basis:** [office-uploaded / CLAUDE.md / generic]
**Jurisdiction:** [state, court, division]
---

## Funder considerations

[Each propagated `[FUNDING RESTRICTION: ...]` flag from intake]
[Each net-new flag the draft raises]

## Document

[The drafted document, with inline `[FACT NEEDED]`, `[VERIFY]`, `[UNCERTAIN]`, `[STAFF REVIEW]` markers]

## Pre-filing / pre-sending checklist

- [ ] Fill every `[FACT NEEDED: ...]` from case file or client follow-up
- [ ] Verify every `[VERIFY: ...]` citation against CourtListener or Descrybe
- [ ] Resolve every `[UNCERTAIN: ...]` by review or rewrite
- [ ] Complete every `[STAFF REVIEW: ...]` section with the staffer's analysis
- [ ] Resolve every funder consideration with the managing attorney's sign-off if material
- [ ] Confirm jurisdiction formatting against current local rules
- [ ] Confirm signature line, bar info, and contact details are current
- [ ] Route per supervision model: [formal queue / configurable flag / managing-attorney review at next rounds]

## Premises this draft rests on

- Practice area: [from intake or argument]
- Funder allocation: [from intake — confirm before filing if uncertain]
- Template: [path or "generic — confirm office template doesn't exist"]
- Jurisdiction formatting: [local rules path or "state default — verify against current local rules"]
- Facts: [from intake summary dated X / from staffer notes dated Y / `[FACT NEEDED]` for the rest]

## What to verify before this leaves the office

[Re-stated key verifications: citations, jurisdiction formatting, funder allocation, conflict re-check if material time has passed since intake]
```

## Cross-skill propagation

- The draft is logged to the matter's case file. `/status` can reference it. `/case-transfer` includes it in the handoff.
- Funder considerations raised here propagate forward — if the draft becomes a filing, the `[FUNDING RESTRICTION: ...]` flag stays live on the matter until resolved.
- If a `[STAFF REVIEW: ...]` marker indicates a legal-analysis gap, the staffer can run `/memo` to scaffold the analysis before completing the draft.

## What this skill does NOT do

- Produce final work product. Every output is a starting point.
- Verify legal citations. Tags every cite for verification; the staffer verifies.
- Decide funder allocation or resolve conflicts. Flags both; the managing attorney resolves.
- Draft documents in practice areas the office doesn't handle. Refuses with a routing message.
- Quote upstream LIA/VIA conversation verbatim. The skill uses upstream context for tone reference; client statements in declarations come from staff-captured interviews, not chat logs.
- Override the supervision model. Even in "lighter-touch" mode, the AI-assisted label and verification markers stay.
- Apply state law from memory. Jurisdiction-specific elements come from CLAUDE.md ingest, the practice-area guide, or are flagged as state default for verification.
