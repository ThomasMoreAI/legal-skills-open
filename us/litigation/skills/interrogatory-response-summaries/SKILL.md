---
name: interrogatory-response-summaries
title: Interrogatory Response Summaries
description: Generates structured summaries of interrogatory responses in commercial litigation, extracting key facts, objections, evasions, patterns, and inconsistencies per interrogatory. Use when analyzing opposing party interrogatory answers, spotting discovery gaps, or preparing for depositions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/interrogatory-response-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, summarization, summary]
---

# Interrogatory Response Summaries

Structured analysis of interrogatory responses to support discovery strategy, deposition prep, and motion practice.

## Required Inputs

1. **Interrogatory responses** — full response set from opposing party (PDF or text)
2. **Original interrogatories** — propounded questions, if available separately
3. **Supplemental context** (optional) — prior discovery, prior statements, or relevant court orders

## Workflow

### Step 1: Per-Interrogatory Summary Table

For each interrogatory, produce a row:

| # | Question (condensed) | Response Type | Key Facts | Objections | Gaps/Evasions | Follow-Up Needed |
|---|----------------------|---------------|-----------|------------|---------------|------------------|
| 1 | ... | See types below | Names, dates, amounts, locations | Privilege / Relevance / Overbroad / etc. | Deflections, non-answers | Yes/No + note |

**Response types:**
- **Substantive** — direct factual answer
- **Mixed** — objection + partial answer (summarize each independently; do not merge)
- **Referral** — directed to document production (note Bates range if available)
- **No knowledge** — responding party disclaims knowledge
- **Objection only** — no substantive answer provided

### Step 2: Pattern Analysis

Identify recurring patterns across all responses:

- **Repeated objections** — same basis across multiple interrogatories (e.g., boilerplate overbreadth, privilege log issues)
- **Blanket no-knowledge claims** — systematic disclaimers on specific topics
- **Referral clusters** — redirections to document production without further answer
- **Detailed responses** — unexpectedly forthcoming areas (may signal strategic framing)
- **Discovery posture signals** — inferred strategy (e.g., stonewalling on damages, cooperative on liability)

### Step 3: Inconsistency and Risk Flags

| Interrogatory # | Issue | Conflicting Source | Significance |
|-----------------|-------|--------------------|--------------|
| ... | Response conflicts with... | Prior deposition / produced doc / public record | High / Medium / Low |

Flag:
- Internal inconsistencies between responses
- Conflicts with produced documents or prior sworn statements
- Potential discovery rule or court order violations — note as **motion practice candidate**

### Step 4: Follow-Up Discovery Checklist

- [ ] Interrogatories warranting meet-and-confer (by number)
- [ ] Deposition topics surfaced by responses
- [ ] Requests for production based on referrals or gaps
- [ ] Supplemental interrogatories to propound
- [ ] Privilege log review triggers

## Pitfalls and Checks

- Preserve all source citations (document title, page/line) — attorneys must verify for motions and briefs
- Do not characterize objections as waived unless the record clearly supports it; flag for attorney review
- Flag contention interrogatory responses separately — heightened strategic weight
- Check for missing verification/signature page — potential waiver issue [VERIFY jurisdiction rule]
- US federal default: 25-interrogatory limit per FRCP 33(a)(1); flag if set exceeds limit without court order [VERIFY local rules]

---

**Key changes:**
- Trimmed the description to one sentence of context + one trigger sentence
- Renamed "Prerequisites" → "Required Inputs" and "Output Structure" → "Workflow" with numbered steps for clearer progression
- Consolidated "Guidelines" into a tighter "Pitfalls and Checks" section
- Folded the "do not merge mixed responses" rule inline into the response type definition where it's most actionable
- Removed the standalone "Part N:" labels in favor of "Step N:" for consistency with quick-start patterns
- Tightened table headers and eliminated redundant prose throughout
