---
name: template-synthesizer
title: Template Synthesizer Skill
description: Guides the full lifecycle of drafting any commercial contract — from context elicitation and model document synthesis through outline approval and final Word document delivery. Use for all contract drafting work, whether the attorney provides model agreements to synthesize, a single precedent to generalize, or no precedent at all. This skill replaces the contract-drafting skill and should be the default for any new agreement. For reviewing or redlining an existing counterparty agreement, use the nda-review or contract-playbook-capture skills instead.
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/template-synthesizer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

# Template Synthesizer Skill

## Overview

This skill governs Darwin Legal's process for drafting a new commercial agreement. It works in three modes:

- **Synthesis mode** (one or more model agreements provided): read models, analyze conflicts and gaps, surface decisions, draft from model language where possible
- **No-precedent mode** (no models provided): skip the document analysis phases; surface decisions based on training
- **Express mode**: skip the full process and produce a best-effort draft immediately

The process is deliberately front-loaded. Decisions are made before drafting begins. Language is drawn from model documents wherever possible. New language is a last resort.

**Identifying Information Strip.** This is absolute and has no exceptions. Every template produced under this skill must be stripped of all client-specific and deal-specific identifying information before delivery. This includes: company names, individual names, addresses, dates, dollar amounts, deal-specific quantities, and any other information that ties the document to a specific transaction or client. Replace stripped information with clearly bracketed placeholders: `[COMPANY NAME]`, `[DATE]`, `[DOLLAR AMOUNT]`, `[GOVERNING LAW STATE]`, etc.

---

## Mode Selection

At the outset, determine which mode applies:

**Express Mode:** If the attorney says anything equivalent to "skip the process," "just draft it," or "express mode," go directly to Phase 5. Produce a best-effort draft based on training, apply the consistency check, deliver the draft and post-draft report.

**No-Precedent Mode:** If no model documents are provided, skip Phase 2 and Phase 3. Proceed from Phase 1 directly to Phase 4, where decisions are surfaced based on training rather than document analysis.

**Synthesis Mode:** Default when one or more model documents are provided. Follow all phases in order.

---

## Phase 1: Context

**Goal:** Understand what the attorney is building before analysis begins.

**If model documents are provided:** Read them in full first. Then present a brief initial read to the attorney covering: (a) the agreement type as Claude characterizes it, (b) the key commercial terms as Claude reads them, and (c) any notable structural features or anomalies. Ask the attorney to confirm, correct, or expand on this read before proceeding.

Attorney direction always overrides Claude's read of the documents. If the attorney's stated intent conflicts with what the documents appear to do, flag the tension clearly and follow the attorney's direction.

**In all modes, ask the attorney to confirm or provide:**

- What type of agreement does this template need to govern?
- Who are the typical parties — what roles do they play? (e.g., licensor/licensee, service provider/client)
- What types of transactions or relationships will this template be used for? Is the deal structure consistent across uses, or does the template need to accommodate variation?
- Are there known constraints: jurisdiction, governing law, regulatory context, firm-specific standards?
- Is there anything in the model documents the attorney wants to preserve as-is, or anything they already know they want to change?

Do not proceed to Phase 2 until context is confirmed.

---

## Phase 2: Analysis and Decision Menu

*Skip this phase if no model documents are provided (No-Precedent Mode).*

**Goal:** Analyze the model documents and immediately surface all decisions required before drafting begins. Analysis and decisions are presented together in a single output — do not separate them into two rounds.

For each model document, inventory the following provision areas in enough detail to identify how each is handled:

- Grant/scope of rights or services
- Payment structure: basis, calculation, timing, adjustments
- Reporting and audit rights
- IP ownership: pre-existing IP, work product, improvements, joint development carve-outs
- Exclusivity: scope, duration, compensation
- Representations and warranties: what each party warrants and the applicable standard
- Indemnification: scope, trigger, procedure, caps
- Limitation of liability: what is excluded, any caps
- Term and termination: initial term, renewal, termination triggers, cure periods, effects of termination
- Governing law and dispute resolution: jurisdiction, arbitration vs. litigation, venue

Present findings and decisions together in a single numbered list. For each item:

- **One sentence describing the issue** (conflict between models, gap, optional provision, or generalization required)
- **Where relevant:** the legal or commercial consequence of each approach and which model(s) support each option
- **A recommendation** — be direct; if one approach is materially better, say so and explain why
- **The decision required:** stated as a clear choice

Flag differences in legal or commercial outcome, not differences in phrasing. Two provisions that say the same thing differently are not a conflict. Do not flag standard market exceptions or immaterial items.

For optional language items: describe the provision, when it applies, and recommend whether to include it as a default, as a bracketed alternative, or as an exhibit/addendum.

For generalizations: describe what must become a placeholder and what placeholder label to use.

Do not proceed to Phase 3 (if applicable) or Phase 4 until the attorney has responded to all decision items.

---

## Phase 3: Precedent Research

*Skip this phase in No-Precedent Mode and Express Mode.*
*Include this phase in Synthesis Mode when the attorney requests it or when model documents are sparse on key provisions.*

**Goal:** Supplement model documents with publicly available comparable agreements where model language is absent or thin.

Search SEC EDGAR and other public sources for comparable executed agreements. For each useful precedent:
- Identify the parties and deal type
- Note what it contributes to specific provisions that are undercovered in the model documents
- Note where it diverges from the current deal and why

Report findings conversationally. Do not quote extensively. Identify what to take from each precedent and for which decision items.

---

## Phase 4: Outline Approval

**Goal:** Get attorney sign-off on the full template structure before drafting.

Produce a structured outline covering every article and section. For each section:
- Section number and title
- One-to-two sentence description of what the section does
- Source: which model document will supply the base language, or note that new drafting is required
- Any remaining open items flagged inline

The outline should confirm that nothing is missing, every conflict is resolved, every gap is addressed, and optional language is positioned correctly.

Ask explicitly for approval. Do not proceed to Phase 5 until the attorney confirms. Revise and re-present if the attorney requests changes.

---

## Phase 5: Draft

**Goal:** Produce a complete master template as a Word document, drawing as directly as possible from model documents.

### Read the Formatting Skill First

Before generating the document, read `/mnt/skills/user/word-contract-formatting/SKILL.md` and follow all Darwin Legal formatting conventions. Output is a `.docx` file.

### Identifying Information

Strip all identifying information before drafting. Do not carry over any of the following from model documents: company names, individual names, addresses, dates, dollar amounts, deal-specific quantities, or any other transaction-specific information. Replace with bracketed placeholders.

### Language Sourcing Hierarchy

Apply in order. Do not move to the next tier unless the prior tier is unavailable:

1. **Direct from model:** Use model document language verbatim where it is generalizable and the attorney's decisions require no modification. Adapt only to strip identifying information and convert party names to role-based placeholders (e.g., "the Licensor," "the Client").

2. **Synthesis from models:** Where more than one model addresses the same provision and the attorney chose an approach supported by one of them, use the chosen model's language as the base and adapt minimally. Where the attorney's decision required a resolution that no single model fully supports, synthesize conservatively from the closest available language.

3. **New language:** Only where a gap must be filled and no model provides usable text, or where a provision must be generalized in a way that requires a new structure. New language must meet four standards — precision, clarity, brevity, plain English — treated as hard priorities in that order. Aim for all four; when they conflict, the ordering governs. Precision is never sacrificed for any of the others.

### Optional Language

Mark optional provisions clearly in the draft:

> `[OPTIONAL — [brief description of when to include]. Delete if not applicable.]`

Where multiple versions of a provision are available (e.g., arbitration vs. litigation), present both with a selector comment:

> `[OPTION A — Arbitration: [provision text]]`
> `[OPTION B — Litigation: [provision text]]`
> `[Select one; delete the other.]`

### Placeholders

Every open commercial term becomes a bracketed placeholder with options where the model documents suggest them:

> `[PLACEHOLDER: Fee structure. See [Model A] §5.1 (fixed fee) or [Model B] §4.2 (per-unit royalty). Confirm with client.]`

Every provision the attorney flagged for generalization becomes a bracketed variable:

> `[CLIENT NAME]`, `[GOVERNING LAW STATE]`, `[TERM IN MONTHS]`

### Consistency Check (Pre-Delivery)

Before delivering the draft, run the following checks:

- **Defined terms:** Every term defined in the Definitions section or inline is used in the body. Every capitalized term used in the body has a definition. No orphaned definitions.
- **Cross-references:** Every internal cross-reference (e.g., "Section 3(b)") refers to a section that exists and covers what the reference says it covers.
- **Optional language:** Every optional provision is clearly marked and the instructions are internally consistent.
- **Identifying information:** Confirm no company names, individual names, addresses, dates, or dollar amounts remain from the model documents.

Correct any errors found before delivering.

### Post-Draft Report (In Chat — Not in Draft)

After delivering the draft, provide a report in the chat covering:

**New Language**
For each provision that required new drafting (Tier 3), identify:
- The section number and title
- A one-sentence description of the provision
- The reason no model language was available or usable

**Language Sourcing Verification**
Confirm that every provision in the draft is accounted for under one of the three tiers. If any provision does not clearly fit — i.e., it is neither direct from a model, a conservative synthesis, nor necessary new language — flag it for attorney review.

**Structural Choices**
Note any provisions that embed a structural choice the attorney should confirm with the client before the template is put into use.

---

## Key Principles

**Model language first.** The primary value of this skill is a template rooted in language that has been negotiated, reviewed, or used — not generic boilerplate. Reach for new drafting only when necessary, and flag it when you do.

**Attorney direction overrides documents.** Claude reads model documents to inform the analysis, not to anchor the outcome. If the attorney's stated intent differs from what the documents do, follow the attorney.

**Conflicts are legal, not textual.** Flag differences in outcome, not differences in phrasing. Two provisions that say the same thing differently are not a conflict.

**Generalizations are decisions.** Every client-specific provision removed from the template is a choice about what the template will and will not do. Surface them explicitly.

**Strip everything.** No company names, individual names, addresses, dates, or dollar amounts survive into the template. This is non-negotiable.

**Recommend, don't just present.** In the decision items, take a position and explain why. The attorney will override where needed, but a clear recommendation is faster than a neutral menu.

**New language standards.** When new language is required, apply four standards in order: precision, clarity, brevity, plain English. These are hard priorities — aim for all four, but when they conflict, the ordering governs. A technically precise provision that requires a defined term chain beats a plain-English approximation that loses the legal meaning.
