---
name: research-start-lawdroidai
title: /research-start
description: Research roadmap for a legal issue — statutory starting points, case law areas, agency guidance, secondary sources (NCLC, Shriver Center, practice manuals), search terms for free research tools (CourtListener, Descrybe, Free Law Project) and paid ones if the office has them. Leads and frameworks, NOT authoritative citations; staff verify and develop everything. Use when a staffer asks where to start researching, wants a research roadmap for an issue, or needs gaps identified in existing research.
author: lawdroidAI
author_url: https://github.com/lawdroidAI/legal-aid-plugin/tree/main/skills/research-start
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# /research-start

1. Load `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` → jurisdiction(s), practice areas, funder restrictions.
2. Read the practice-area guide at `guides/<practice-area>.md` if one exists and the issue belongs to that area.
3. Use the workflow below.
4. Frame the issue specifically — jurisdiction, procedural posture, what's at stake. Vague framing produces vague roadmaps.
5. Build the roadmap: statutory starting points (unverified), case law areas (not specific cases), agency guidance, secondary-source pointers, search terms.
6. If the staffer has existing research uploaded: synthesize and identify gaps.
7. Output with prominent "leads not authorities" header. Everything is a starting point the staffer verifies.

```
/legal-aid:research-start "habitability defense to nonpayment eviction in NC"
/legal-aid:research-start "SSI overpayment waiver — without fault standard"
/legal-aid:research-start "U-visa supplement B requirements when no LEA cooperation"
```

---

# Research Start: Roadmap, Not Research

## Purpose

Legal research is essential to civil legal aid practice. But the initial phase — figuring out *what* to research, finding the right statute, understanding the framework — is often the most time-consuming and least valuable part. A staff attorney can spend a morning finding the starting point before doing any actual research.

This skill produces the starting point: statutory candidates, case law areas to investigate, agency guidance to find, secondary-source pointers (poverty law manuals, practice guides, treatise areas), and search terms for both free tools (CourtListener, Descrybe, Free Law Project) and paid ones if the office has access. **None of it is verified. None of it is authoritative. All of it is a lead for the staff attorney to run down.**

This is both an ethical safeguard and a practical one. Citations from memory are how malpractice happens. Citations from a roadmap, verified by the staffer, are how good lawyering happens.

## Load context

`~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` → jurisdiction(s), practice areas, funder restrictions that might bear on the research scope (e.g., LSC class-action restrictions if the research is heading toward systemic remedies).

The practice-area guide at `guides/<practice-area>.md` if one exists → office-specific research conventions, judges' preferences, treatises the office subscribes to.

If the office's CMS or document store contains prior research on similar issues (a brief bank, an issue file), reference it — research compounds across matters in the same practice area.

## Workflow

### Step 1: Frame the issue

The staffer's issue framing determines the roadmap quality. If the framing is vague, surface that before building the roadmap:

> "You asked about 'habitability defense.' To make the roadmap useful, I need:
> - Jurisdiction: which state, and which court level?
> - Procedural posture: pre-litigation defense, motion in pending eviction action, affirmative claim?
> - The specific facts that engage habitability: what conditions, how long, what notice given, what damages?
>
> If you can give me those, the roadmap will be specific. If not, I'll produce a generic framework and you'll do more narrowing yourself."

For a well-framed issue, restate it precisely at the top of the roadmap so the staffer can verify the skill understood:

> **Issue as framed:** Whether a tenant in [state, court] facing nonpayment eviction can assert habitability as an affirmative defense based on [facts]. Procedural posture: [posture]. Funder allocation: [funder]. Funder considerations: [any flags from intake].

### Step 2: Statutory starting points

Identify likely-relevant statutes. For each:
- Statute name and (probable) citation, tagged `[VERIFY: cite — confirm current]`
- What it likely governs
- Which subsection(s) appear most directly relevant to the issue
- A `[VERIFY]` reminder that statutes change and the cite plus text need to be confirmed against the current version

Example output for habitability research:

> **Likely statutory framework (verify all):**
>
> - `[VERIFY: state landlord-tenant act, habitability provisions]` — most states have codified habitability requirements; the staffer confirms the current state code chapter
> - `[VERIFY: state landlord-tenant act, retaliation provisions]` — habitability defense often paired with retaliation claim; confirm if retaliation is statutory or common-law
> - `[VERIFY: state landlord-tenant act, remedies provisions]` — what relief is available; rent abatement, repair-and-deduct, withholding, termination

If multiple statutes plausibly apply, list them all and let the staffer narrow.

### Step 3: Case law areas

Not specific cases — areas of doctrine to investigate.

> **Case law areas to research:**
>
> - Doctrine on what constitutes a "material" breach of habitability in [state]
> - Doctrine on notice requirements before habitability may be asserted defensively
> - Doctrine on whether documented complaints are required or facts are sufficient
> - Doctrine on the interaction between habitability defense and the duty to pay rent
> - Recent (last 5 years) trial-level and appellate decisions in [state] on habitability defenses to nonpayment

For each area: what the doctrine probably says generally (with `[VERIFY]` tags), but no specific case names. The staffer finds the cases.

### Step 4: Agency guidance

Many civil legal aid issues involve administrative agencies (SSA, HUD, USDA/FNS, state Medicaid, state UI, state housing authorities). Identify the agency frameworks:

> **Agency guidance to research:**
>
> - SSA POMS (Program Operations Manual System) — the operational standard for SSI/SSDI determinations; section SI 02220.001 et seq. is overpayment-relevant `[VERIFY: current POMS sections]`
> - SSA HALLEX — the hearing-level standard
> - 20 CFR Part 416 — the regulatory framework
> - Recent SSA emergency messages, Social Security Rulings, or Acquiescence Rulings affecting overpayment standards

For HUD, USDA/FNS, state agencies: parallel structure.

### Step 5: Secondary sources

Civil legal aid practice has its own canon of secondary sources. Surface the relevant ones:

> **Secondary-source pointers:**
>
> - **NCLC** (National Consumer Law Center) — *Consumer Credit Regulation*, *Fair Debt Collection*, *Fair Credit Reporting*, etc. Reference: nclc.org/library
> - **Sargent Shriver National Center on Poverty Law** — *Clearinghouse Review* archive, online materials
> - **State legal aid practice manuals** — many state legal aid programs publish practice manuals (NC's NCLAP, FL's FLAW, TX's TexasLawHelp.org content) `[VERIFY: current edition]`
> - **Practising Law Institute** materials if the office has access
> - **LSC Tech Center** webinar archives for procedural and practice updates
> - **ABA Commission on Domestic & Sexual Violence** materials for DV-adjacent matters

Tailor by practice area: consumer → NCLC and Fair Debt Collection Practices guidance; housing → NLIHC, NHLP, state landlord-tenant manuals; immigration → AILA practice library if the office has access, CLINIC manuals (free), ILRC manuals; public benefits → NCLEJ for benefits-specific, JustHealth-Action for Medicaid, NELP for unemployment; DV → ABA Commission, NRCDV.

### Step 6: Free-tool search terms

Search terms for free tools the office is most likely to use:

> **CourtListener / Free Law Project searches to run:**
>
> - `"habitability" /5 "eviction" /5 [state name]`
> - `"warranty of habitability" /s "defense"`
> - `[state code section] /p "nonpayment"`
>
> **Descrybe queries:**
>
> - Plain-language query: "Can a tenant assert habitability as a defense to nonpayment eviction in [state]?"
> - Concept query: tenant defense habitability material breach notice requirement
>
> **Google Scholar legal:**
>
> - `[state name] habitability defense site:caselaw.findlaw.com`
> - `[state appellate court name] habitability "warranty"`

If the office has Westlaw, Lexis, or Bloomberg, list parallel paid-tool searches but note: "the free-tool searches above usually surface 80% of what you need; paid searches are for the last 20% of confirmation."

### Step 7: Existing research integration

If the staffer pasted or uploaded existing research, read it and identify:

- **What's been verified:** statutes and cases the staffer has already confirmed against current sources
- **What's still a lead:** items marked `[VERIFY]` or that the staffer pulled from secondary sources without confirming directly
- **Gaps:** doctrine areas the existing research doesn't address that the issue framing suggests should be covered
- **Out-of-scope research:** items that don't bear on the specific issue framed at the top

Synthesize:

> **What the existing research has established (subject to verification):**
> - [Item 1, with confidence note]
> - [Item 2, ...]
>
> **What's still a lead:**
> - [Item 1, why it needs confirmation]
> - [Item 2, ...]
>
> **Gaps:**
> - [Doctrine area 1 not yet addressed]
> - [Doctrine area 2 ...]

### Step 8: Funder-restriction research

If any funder restriction is live on the matter and the research direction could engage it, surface:

> **Funder-restriction research:**
>
> The matter is funded under [LSC]. The research direction (systemic remedies through class action) may engage LSC's class-action prohibition at 45 CFR § 1617. Research:
>
> - Current LSC program rule guidance on § 1617's scope `[VERIFY: LSC website / Inspector General opinions]`
> - Whether the contemplated action qualifies as a "class action" under the rule
> - Whether limited-scope individual representation could achieve client goals without engaging the restriction
> - Whether non-LSC funds could be allocated to a class-action piece if the office wants to pursue it

Funder-restriction research is required when applicable; the skill doesn't omit it.

## Output

```markdown
# Research Roadmap: [Issue, restated precisely]

---
[LEADS, NOT AUTHORITIES — every item below is a starting point that must be verified before relying on it. This skill does not produce citations; the staffer produces citations after research.]

**Date:** [date] | **Matter:** [Case ID if applicable] | **Staffer:** [staffer]
**Jurisdiction:** [state, court level]
**Practice area:** [area]
**Funder allocation:** [funder(s) and any restrictions live]
---

## Issue as framed

[Restatement of the issue, precise enough that the staffer can verify the skill understood]

## Statutory starting points

[Per Step 2]

## Case law areas to research

[Per Step 3 — areas, not cases]

## Agency guidance

[Per Step 4, if applicable]

## Secondary sources

[Per Step 5, tailored to practice area]

## Search terms

### CourtListener / Free Law Project
[Per Step 6]

### Descrybe
[Per Step 6]

### Google Scholar legal
[Per Step 6]

### Office paid tools (if any)
[Per Step 6 if office has Westlaw / Lexis / Bloomberg]

## Funder-restriction research (if applicable)

[Per Step 8]

## Existing research synthesis (if uploaded)

[Per Step 7]

## What to verify before relying on this roadmap

- Every statutory citation listed: confirm against the current state code (statutes get amended; the cite I gave you may be stale)
- Every case law area: research and find the actual cases; this roadmap names doctrines, not authorities
- Every agency guidance reference: confirm against the current POMS / HALLEX / regulation
- Every secondary-source pointer: check the publication date and confirm the office's subscription is current
- Every search term: run them and review results — the search terms are guesses informed by issue framing, not validated queries

## What this roadmap explicitly does not do

- Provide citations. Areas of doctrine, not cases.
- Reach a legal conclusion. The conclusion comes from research and analysis.
- Replace the staff attorney's research. Starting point only.
- Cover every relevant authority. Civil legal aid issues frequently have local-jurisdiction quirks no national roadmap will catch.
```

## Cross-skill propagation

- A completed `/memo` invocation may reference the research roadmap as the basis for its `[RESEARCH NEEDED: ...]` block resolutions.
- If the roadmap surfaces a funder-restriction concern not previously flagged, propagate that to the matter's intake and current draft. New `[FUNDING RESTRICTION: ...]` flags from research are equally binding as ones from intake.

## What this skill explicitly does not do

- Cite cases. Doctrine areas, search terms, statutory candidates with `[VERIFY]` tags. Never a specific case citation.
- Verify any citation. Verification is the staffer's job.
- Reach a conclusion on the legal question. Provides the map; the staffer walks it.
- Replace primary research. A roadmap is not research.
- Substitute for treatise / practice manual consultation. The skill points to the secondary sources; the staffer reads them.
