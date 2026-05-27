---
name: cross-examination-summaries
title: Cross-Examination Summary
description: Generates thematic cross-examination summaries from deposition transcripts, sworn statements, and discovery materials with precise page-and-line citations. Highlights inconsistencies, impeachable admissions, and favorable concessions in a trial-ready format. Use when preparing witness cross-examination, building impeachment strategy, or synthesizing testimony across multiple witnesses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cross-examination-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Cross-Examination Summary

Transforms raw witness testimony and discovery materials into a thematically organized impeachment reference with exact citations for courtroom use.

## Prerequisites

1. **Deposition transcript(s)** — page and line numbers intact
2. **Prior sworn statements** — affidavits, interrogatory responses, hearing testimony
3. **Informal statements** — emails, texts, recorded communications
4. **Relevant exhibits** — documents or other witness statements that contradict or corroborate
5. **Case theory summary** — client's narrative and key issues

## Output Structure

### 1. Witness Profile

| Field | Content |
|---|---|
| Name / Role | Relationship to parties, capacity (fact, expert, party) |
| Key Topics | Issues this witness covers |
| Credibility Flags | Bias, motive, prior convictions, interest in outcome |
| Examination Goal | Concessions to secure / narrative to establish / credibility to undermine |

### 2. Thematic Sections

Organize by **case issue**, not transcript chronology. Use this template per theme (typically 4–8):

```
## [Theme Name]

### Witness Position
[Concise paraphrase]

### Key Testimony
> "[Exact quote]"
> — [Source], p. [X], ll. [Y–Z]

### Inconsistencies / Contradictions
- Prior statement: "[Quote]" — [Source], p. [X], ll. [Y–Z]
- Contradicting exhibit: [Ex. No.], [relevant portion]
- Other witness: [Name], [Source], p. [X], ll. [Y–Z]

### Favorable Concessions
- [Undisputable fact] — [Source], p. [X], ll. [Y–Z]

### Knowledge / Perception Gaps
- Lacks personal knowledge of [X] — [Source], p. [X], ll. [Y–Z]

### Impeachment Approach
[1–2 sentence tactic: foundation, sequence, exhibit to use]
```

### 3. Impeachment Priority Matrix

| Rank | Opportunity | Source Citation | Exhibit | Impact (H/M/L) |
|---|---|---|---|---|
| 1 | [Description] | [Doc, p/ll] | [Ex. No.] | H / M / L |

### 4. Concessions Checklist

Facts to lock in early, before confrontational impeachment:

- [ ] [Fact] — [Source], p. [X], ll. [Y–Z]

### 5. Exhibit Integration Map

| Exhibit | Relevant Portion | Contradicts / Supports | Deploy During |
|---|---|---|---|
| Ex. [#] | [Description] | [Source], p. [X], ll. [Y–Z] | [Theme] |

### 6. Cross-Witness Impeachment

Include when multiple witnesses are involved:

| This Witness Says | Conflicts With | Other Witness Says | Citation |
|---|---|---|---|
| "[Quote]" — [Source] | | "[Quote]" — [Name], [Source] | |

### 7. Strategic Overview

- **Examination sequence**: Concessions first, then impeachment, close on [X]
- **Top 3 moments**: Highest-impact confrontations
- **Witness control risks**: Evasive, volatile, over-explains
- **Narrative thread**: One sentence connecting examination arc to case theory

## Pitfalls

- **Citation accuracy is paramount** — verify every page/line reference; the summary's credibility depends on it
- **Exact quotes only** for testimony intended for impeachment; no paraphrased citations
- **Stay non-argumentative** in the body — reserve advocacy for the Strategic Overview
- **Flag evasive or rehearsed answers** in theme section notes
- **One summary per witness** in multi-witness matters; use Section 6 for cross-witness linkage
- **US jurisdiction assumed** — flag state-specific impeachment rules (e.g., FRE 609 prior conviction admissibility; verify applicability in specific forum)

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` are required frontmatter)
- **Tightened description** — shorter, third-person, clear trigger guidance, within 1024 chars
- **Eliminated redundant rows** — empty placeholder rows in the Impeachment Priority Matrix and Concessions Checklist reduced to single exemplar rows (the agent will generate as many as needed)
- **Trimmed horizontal rules** — removed decorative `---` separators between subsections
- **Compressed Strategic Overview** — collapsed from verbose field descriptions to terse bullet format
- **Renamed "Guidelines" to "Pitfalls"** — aligns with best-practice body structure (brief overview → quick start → core workflow → pitfalls)
- **Reduced from ~126 lines to ~88 lines** — well under the 500-line ceiling, preserving all domain-critical structure and legal intent
