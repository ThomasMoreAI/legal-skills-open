---
name: devils-advocate
title: Devil's Advocate Review
description: Challenge formatting decisions with 5-7 specific questions. Checks section ordering, content placement, missing elements, alternative structures, and compliance gaps.
author: maxwell2732
author_url: https://github.com/maxwell2732/my-submission-formatting-agent/tree/main/.claude/skills/devils-advocate
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Devil's Advocate Review

Critically examine a formatted manuscript and challenge its structural and formatting decisions with 5-7 specific questions.

**Philosophy:** "We arrive at the best possible submission through active dialogue."

---

## Setup

1. **Read the formatted manuscript** (the file being challenged)
2. **Read the journal guidelines** in `guidelines/[journal].yml`
3. If applicable, **read the formatting report** for context on decisions made

---

## Challenge categories

Generate 5-7 challenges from these categories:

### 1. Section ordering challenges
> "Would the argument flow better if we moved X before Y?"

### 2. Content placement challenges
> "Does this material belong in Methods or Results?"

### 3. Gap challenges
> "Is there a missing transition between these sections?"

### 4. Alternative structure challenges
> "Here are 2 other ways to organise this content for the journal."

### 5. Compliance challenges
> "This requirement might not be fully met — here's why."

### 6. Word count challenges
> "This section is disproportionately long. What could be condensed or moved to supplementary?"

### 7. Reviewer perspective challenges
> "A referee might question this framing. Consider an alternative."

---

## Output format

```markdown
# Devil's Advocate: [Manuscript Title]

## Challenges

### Challenge 1: [Category] — [Short title]
**Question:** [The specific question]
**Why it matters:** [What could go wrong at review/submission]
**Suggested resolution:** [Specific action]
**Sections affected:** [Section names]
**Severity:** [High / Medium / Low]

[Repeat for 5-7 challenges]

## Summary verdict
**Strengths:** [2-3 things done well]
**Critical changes:** [0-2 changes before submission]
**Suggested improvements:** [2-3 nice-to-have changes]
```

---

## Principles

- **Be specific:** Reference exact sections and requirements
- **Be constructive:** Every challenge has a suggested resolution
- **Be honest:** If the formatting is good, say so
- **Prioritize:** Compliance gaps > structural suggestions
- **Think like a reviewer:** Where will referees push back?
