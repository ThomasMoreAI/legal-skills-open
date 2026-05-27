---
name: preliminary-injunction
title: Motion for Preliminary Injunction
description: Drafts a Motion for Preliminary Injunction applying the Winter four-factor test with jurisdiction-specific procedural compliance. Covers merits analysis, irreparable harm, equities balancing, bond, and proposed order language. Use when filing for preliminary injunction, TRO, temporary restraining order, or emergency injunctive relief in federal or state court.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/preliminary-injunction
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Motion for Preliminary Injunction

Drafts a procedurally compliant motion for preliminary injunction that satisfies the applicable multi-factor test and builds an appellate record.

## Prerequisites

Before drafting, collect:

1. Filed or ready-to-file complaint with identified causes of action
2. Supporting documents — contracts, correspondence, declarations, exhibits
3. Court, case number, and applicable rules (FRCP 65 or state equivalent)
4. Evidence of imminent irreparable injury
5. Specific injunctive terms — conduct to be enjoined or compelled

## Quick Start

1. Research jurisdiction — identify governing rule, injunction standard (Winter strict vs. sliding scale), local rules, bond requirements, and emergency/TRO procedures
2. Draft motion following the structure below
3. Verify every factual assertion cites a declaration, exhibit, or document
4. Confirm all legal citations use proper Bluebook format
5. Check page limits and formatting against local rules

## Motion Structure

### 1. Caption and Procedural Framework

- Full party names matching the complaint
- Court name with division/department, case number
- Title: "Plaintiff's Motion for Preliminary Injunction"
- Hearing date or request for expedited consideration
- List simultaneous filings (proposed order, declarations, exhibits)

### 2. Introduction (1-2 pages)

- State exact conduct to enjoin/compel in order-ready language
- Cite procedural authority (Rule 65 or equivalent)
- Preview satisfaction of each factor
- Frame consequences of inaction concretely

### 3. Statement of Facts

- Chronological narrative citing specific exhibits, dates, amounts, and verbatim quotes
- Distinguish undisputed from contested facts with evidentiary support
- No legal conclusions — let facts drive the argument

### 4. Legal Standard

State the Winter four-factor test with controlling authority. Note circuit-specific variations — sliding scale, "serious questions" alternative, heightened standard for mandatory injunctions.

### 5. Factor Analysis

**A. Likelihood of Success on the Merits** — For each cause of action:

| Step | Content |
|---|---|
| Elements | State with controlling citation |
| Application | Map facts to each element with record cites |
| Defenses | Preemptively address and distinguish |
| Adverse authority | Distinguish on facts, supersession, or jurisdiction |
| Threshold issues | Standing, ripeness, limitations, preemption |

**B. Irreparable Harm**

- Identify specific, imminent, non-speculative harm
- Explain inadequacy of monetary damages (goodwill loss, trade secret disclosure, constitutional deprivation, market destruction, unique property)
- Cite jurisdiction-specific authority recognizing the harm category as irreparable
- Show imminence with specificity — what defendant is doing or will do, and when

**C. Balance of Equities**

- Acknowledge defendant's burdens candidly
- Argue plaintiff's harm outweighs: defendant's hardship is self-inflicted, economic, and bond-compensable; plaintiff's is not
- Frame as preserving status quo; if mandatory injunction, justify heightened burden

**D. Public Interest**

- Connect to enforcement of applicable law, constitutional values, or regulatory policy
- Address competing interests and explain why plaintiff's predominate

### 6. Conclusion and Prayer for Relief

Synthesize all four factors, then draft specific injunctive terms in order-ready language:

- Specific prohibitory relief (exact conduct to enjoin)
- Specific mandatory relief, if any (exact conduct to compel)
- Duration or conditions
- Bond amount proposal or waiver request with justification
- Request for expedited hearing or TRO if applicable
- Alternative narrower relief formulations

### 7. Signature Block and Service

Standard signature block, certificate of service, and verification language if jurisdictionally required.

## Critical Checks

- **Injunctive specificity**: Every prohibited/required act must be precise enough for enforcement and contempt proceedings
- **Bond**: Always address — propose amount with rationale, or argue for nominal/no bond with authority
- **Status quo framing**: Courts disfavor mandatory injunctions; frame as preserving status quo wherever possible
- **TRO bridge**: If harm is truly imminent, include or separately file TRO request; address notice impracticability if ex parte
- **Jurisdiction-specific standard**: The test varies materially across circuits and states — never assume Winter alone controls
- **Declarations**: Motion references (not replaces) declarations from witnesses with personal knowledge
- **Page limits**: Many courts impose 25-page limits — allocate space accordingly

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec; only `name` and `description` are required frontmatter
- **Tightened description** — same trigger keywords, fewer tokens (removed redundant enumeration of sub-topics already implied by the main description)
- **Added Quick Start** — gives the agent an immediate 5-step workflow before diving into structure
- **Collapsed Jurisdictional Research table** — folded into Quick Start step 1 instead of a separate verbose section
- **Removed code-fenced legal standard boilerplate** — Claude knows the Winter test; a directive to state it with authority suffices
- **Consolidated Prayer for Relief** — replaced the code-fenced WHEREFORE template with a concise bullet list (same content, fewer tokens)
- **Collapsed Signature Block** — one line instead of four; Claude knows standard signature block formatting
- **Renamed "Guidelines" to "Critical Checks"** — actionable checklist framing, same domain-critical rules preserved
- **Reduced from 147 lines to ~97 lines** — ~34% token reduction while preserving all legal substance
