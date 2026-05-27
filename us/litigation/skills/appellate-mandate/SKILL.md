---
name: appellate-mandate
title: Appellate Mandate
description: Drafts formal appellate mandates that conclude the appeal process and direct trial courts to implement appellate decisions. Extracts disposition language, remand directives, and procedural history from appellate records to construct jurisdiction-specific mandate orders. Use when preparing mandate orders, returning jurisdiction to lower courts, or formalizing appellate dispositions after ruling.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/appellate-mandate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [brief, drafting]
---

# Appellate Mandate

Drafts the formal order issued by an appellate court concluding the appeal and directing the trial court to implement the appellate decision.

## Prerequisites

Gather before drafting:

1. **Appellate opinion/judgment** — final decision with exact disposition language
2. **Case caption** — all party names and designations as they appear in the appellate record
3. **Case numbers** — both appellate and trial court docket numbers
4. **Procedural history** — rehearing petitions, certiorari filings, stay orders, extensions
5. **Remand instructions** — specific directives from the opinion on scope of further proceedings

## Output Structure

### 1. Caption & Identification

| Element | Requirement |
|---|---|
| Court name | Full formal name of issuing appellate court |
| Receiving court | Full formal name of trial court |
| Party designations | Mirror appellate record exactly |
| Case numbers | Both appellate and trial court numbers |
| Opening recital | "This mandate is issued pursuant to this Court's judgment dated [date]..." |

### 2. Incorporation of Decision

- Attach or incorporate certified copy of the appellate opinion/judgment
- Reference by case name, court, date, and reporter citation if published

### 3. Directive Section

Standard formulation matching actual disposition:

> IT IS ORDERED that the judgment of the [trial court] is [AFFIRMED / REVERSED / REVERSED AND REMANDED / MODIFIED / DISMISSED].

For remands, specify with particularity:

| Remand Type | Required Specificity |
|---|---|
| New trial | All issues or only specified matters |
| Entry of judgment | In whose favor and on what basis |
| Partial remand | Which issues are foreclosed vs. open |
| Conditional (e.g., remittitur) | Exact conditions and implementation steps |
| Damages/remedies | Calculation instructions or caps from opinion |

Extract and incorporate **verbatim** any limiting language from the opinion regarding scope of proceedings on remand.

### 4. Effective Date & Procedural Conditions

Calculate issuance date per applicable rules:

| Jurisdiction | Typical Auto-Issuance Period |
|---|---|
| Federal (FRAP 41) | 7 days after rehearing petition deadline expires |
| Most state courts | 21–30 days after final judgment |

Address in sequence:
1. Rehearing petition filed → if denied, state denial date
2. Certiorari or discretionary review sought → note any stay of mandate
3. Stay lifted or review denied → include dates
4. Extensions tolling issuance period
5. Any order for expedited issuance

### 5. Certification & Authentication

Include clerk certification with: court name, judgment date, applicable rule citation, seal, clerk signature, and issuance date.

Filing instructions for trial court clerk:
- Docketing requirements
- Service obligations on parties
- Required acknowledgment or action timeline

## Pitfalls

- **Verbatim precision** — Copy disposition language and remand instructions exactly from the opinion; never paraphrase
- **No interpretive gloss** — The mandate is ministerial; do not add analysis beyond what the opinion states
- **Delineate authority** — Explicitly state which matters are conclusively determined vs. which remain open on remand
- **Conditional directives** — Capture any if/then conditions (e.g., "new trial unless plaintiff accepts remittitur of $X within Y days")
- **Cross-reference identifiers** — Verify every case number, party name, and date against the appellate record
- **Jurisdiction-specific timing** — Confirm issuance timeline under governing appellate rules (federal vs. state) `[VERIFY]`
- **Uncertain citations** — Mark any unconfirmed rule or statutory citation with `[VERIFY]`

---

Key changes from the original:

- **Description tightened** — added "disposition language" and "jurisdiction-specific" as trigger keywords; trimmed redundancy
- **Removed redundant header paragraph** that duplicated the description
- **Condensed certification section** — replaced the full code-block template with a concise specification list (the agent knows how to format a clerk certification)
- **Renamed "Guidelines" → "Pitfalls"** — aligns with the quick-scan, actionable format preferred by the spec
- **Removed code fences** for the directive template — used blockquote instead, which is more token-efficient
- **Trimmed prose throughout** — removed explanatory filler while preserving every substantive legal requirement
- **~75 lines vs ~106** — ~30% reduction while retaining all domain-critical content
