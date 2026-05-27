---
name: amicus-interest-statement
title: Amicus Interest Statement
description: Drafts the "Interest of Amicus Curiae" section of an amicus brief. Establishes institutional credibility, tethers the amicus's interest to the specific legal question, articulates non-party impacts, and embeds disclosure guardrails under FRAP 29 and Supreme Court Rule 37. Trigger when drafting amicus briefs, friend-of-the-court filings, interest statements, amicus disclosures, or when the user asks why an organization belongs in a case.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/amicus-interest-statement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [brief, drafting]
---

# Amicus Interest Statement

The Interest of Amicus Curiae section is the credibility gateway. Courts scrutinize amicus filings for "me-too" redundancy — a weak interest statement signals the brief wastes the court's time. This skill produces a statement that passes the clerk test: can someone explain in one sentence why this amicus belongs in this case?

## Pre-Draft Intake

Gather before drafting (skip only if user says "use defaults" or "just draft"):

1. **Case context** — caption, court, docket number, stage, questions presented, decision below
2. **Amicus identity** — legal name, entity type, founding year, membership size/scope, coalition status
3. **Mission & expertise** — mission statement, core programs, publications, prior amicus filings, domain expertise
4. **Concrete stake** — who is affected, through what mechanisms (compliance costs, enforcement changes, chilling effects)
5. **Parties' briefs** (if available) — to identify the amicus's unique perspective
6. **Disclosure facts** — (a) who authored the brief, (b) party/counsel funding, (c) other monetary contributors
7. **Governing rules** — FRAP 29, S.Ct. Rule 37, or state rules; flag if unknown

**Defaults when user doesn't respond:** stakeholder advocate posture; FRAP 29 rules; disclosure withheld pending confirmation. Label all defaults. Request missing disclosure facts before finalizing.

## Core Workflow

### 1. Anchor to the Legal Issue

Open by connecting the amicus to the specific question presented. Mirror the language of the questions presented.

> Amicus curiae [Organization] submits this brief to assist the Court in resolving whether [legal issue]. Because [Organization] [work tied to issue], the Court's resolution will have significant consequences for [constituency] and for [system/market/program].

- Name the specific statute/provision at issue — not generic values
- Distinguish amicus perspective from parties' arguments
- Show why *this* amicus in *this* case on *this* question

### 2. Describe the Organization with Verifiable Specifics

> [Organization] is a [entity type] founded in [year] that represents [members/constituency] across [scope]. Its work includes [2-4 activities], including [activity relevant to the issue].

- Use verifiable facts (membership numbers, founding year, programs) — no superlatives ("leading," "premier")
- Be candid about advocacy posture; disclose coalition composition when filing jointly
- Omit programs unconnected to the case

### 3. Establish Expertise Mapped to the Doctrinal Choice

Select 2-3 expertise pillars from: operational experience with the statutory scheme, technical knowledge of the regulated subject, published research or data, professional standards, litigation pattern awareness.

> Amicus has particular expertise relevant to the Court's analysis of [issue], including (1) [pillar], which informs how [rule] functions in practice; and (2) [pillar], which bears on [consequences] of adopting [proposed standard].

### 4. Articulate Concrete Non-Party Impact

Translate doctrine into real-world effects via causal chains, not conjecture.

> If the Court holds that [rule], then [mechanism], which would [consequence]. Because [Organization] works directly with [group], it has a concrete perspective on how [standard] will shape [behavior].

- Define affected populations specifically — not "all Americans"
- Describe mechanisms, not speculation
- Do not argue the merits here

### 5. Calibrate Tone and Harmonize Disclosures

**Neutral expertise posture:**
> Amicus does not file to support any party as such, but to assist the Court by providing [technical/historical/industry] context relevant to [provision].

**Stakeholder advocate posture:**
> Amicus supports [party position] because the decision below threatens to [consequence] for [constituency], whom amicus serves through [programs].

Draft as though every sentence will be excerpted by opposing counsel.

**Disclosure:** Include only when user affirmatively confirms facts. Mark unconfirmed elements `[VERIFY]`.

> Pursuant to [Rule], amicus curiae states that no counsel for a party authored this brief in whole or in part, and no person or entity other than amicus curiae or its counsel made a monetary contribution intended to fund the preparation or submission of this brief.

### 6. Produce Deliverable

Prefix every output with:
1. **Assumptions Used** — court, posture, tone, governing rules
2. **Open Items** — missing disclosures, unverified facts, rule uncertainties

Keep the Interest Statement to 1-3 paragraphs.

## Rules Reference

| Forum | Rule | Key Requirement |
|---|---|---|
| U.S. Supreme Court | Rule 37.1 | Must bring matter not already presented by parties |
| U.S. Supreme Court | Rule 37.6 | Authorship and funding disclosures |
| Federal Circuits | FRAP 29(a)(4)(D) | Statement of amicus's interest |
| Federal Circuits | FRAP 29(a)(4)(E) | Authorship and funding disclosures |
| California | Rule 8.520(f) | Relationship to parties; identify other filings on same issue |
| 7th Circuit | Local practice | Must demonstrate unique contribution |
| State courts | Varies | Check local rules for motion-for-leave and extra-record restrictions |

All rule citations require verification against current text before filing. `[VERIFY]`

## Post-Draft Checklist

Ask after delivering the draft:

1. Are all organizational facts verified and current?
2. Does the statement distinguish this amicus's perspective from the parties'?
3. Are disclosure facts confirmed for inclusion?
4. Should tone shift — more neutral or more advocacy?

## Quality Checks

- **Clerk test**: One-sentence explanation of why this amicus belongs in this case
- **Issue tethering**: Names the specific legal question at stake
- **Non-redundancy**: Articulates what amicus uniquely provides beyond the parties
- **Mission alignment**: Stated interest consistent with the organization's mission
- **Factual support**: Every claim traceable to user input or flagged `[VERIFY]`
- **Disclosure consistency**: No contradictions between interest statement and disclosures
- **Adversarial resilience**: No sentence exploitable out of context
- **Procedural compliance**: Required disclosures present and correctly placed
- **Length**: 1-3 paragraphs — this is not the argument section

## Guardrails

- Flag all organizational facts for attorney verification
- Mark unverified citations `[VERIFY]`
- Do not resolve conflicts of interest — flag for attorney review
- Do not draft disclosures without user confirmation of underlying facts
- Do not invent organizational facts, membership numbers, or program descriptions
- All output requires licensed attorney review before filing
