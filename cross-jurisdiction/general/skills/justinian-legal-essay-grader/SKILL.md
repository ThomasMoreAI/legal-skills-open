---
name: justinian-legal-essay-grader
title: Justinian — Legal Essay Grader
description: Use when a student submits a written legal essay, exam answer, or practice response for automated grading. Evaluates issue spotting, rule accuracy, application depth, conclusion quality, IRAC organization, and writing clarity on a bar-exam-style 0–100 scale with per-dimension 0–10 subscores and concrete, line-cited feedback. Adapts standard to student level (1L through bar candidate). Jurisdiction-aware, including MENA-specific rules and statute citations (UAE, KSA, Lebanon, Egypt, DIFC, ADGM).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-legal-essay-grader
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Legal Essay Grader

## When to use this

Use this skill when:

- A student submits a practice essay or exam answer for grading
- A trainer needs consistent, rubric-based feedback across multiple submissions
- A bar candidate wants scored mock answers with a model answer comparison
- A law professor or TA wants automated first-pass scoring before human review

This skill grades the written output; [[justinian-irac-coach]] coaches interactively during drafting. Use both: coach first, then grade the final draft.

## Inputs required

1. **Student essay** — the full text to be graded
2. **Fact pattern / question** — what the essay was supposed to address
3. **Student level** — `1L`, `2L/3L`, `bar candidate`, or `trainee lawyer` (defaults to `bar candidate` if unspecified)
4. **Jurisdiction** (optional) — if the question tested a specific jurisdiction's law, note it so rule-accuracy scoring is calibrated

## Grading dimensions

Six dimensions, each scored 0–10.

### 1. Issue spotting (0–10)

Did the student identify all legally significant issues?

| Score | Standard |
|-------|---------|
| 9–10 | All major and minor issues spotted; hierarchy correct |
| 7–8 | All major issues spotted; one minor issue missed |
| 5–6 | Most major issues; one major issue missed |
| 3–4 | Multiple major issues missed |
| 1–2 | Only surface issue spotted |
| 0 | No issue identification at all |

**Grader action:** List every issue the fact pattern contained. Mark each as (spotted / missed / partially addressed). Deduct proportionally.

### 2. Rule statement (0–10)

Is each rule accurate, complete (all elements), and properly sourced?

| Score | Standard |
|-------|---------|
| 9–10 | Accurate, complete, sourced (statute / principle / leading case) |
| 7–8 | Accurate + mostly complete; minor element omitted or source missing |
| 5–6 | Partially accurate; key element misstated or wrong statute cited |
| 3–4 | Rule present but substantially inaccurate or missing elements |
| 1–2 | Only a vague reference to a legal concept |
| 0 | No rule stated |

**MENA-specific calibration:** Verify that the student cited the correct instrument (e.g., distinguishing UAE Federal Decree-Law 33/2021 Arts. 9–10 for non-competes from DIFC Employment Law, or the Lebanon Code of Obligations and Contracts from a French Civil Code article).

### 3. Application (0–10)

Does the student tie each rule element to specific facts?

| Score | Standard |
|-------|---------|
| 9–10 | Element-by-element analysis; specific facts quoted; both sides considered where facts permit |
| 7–8 | Most elements applied to facts; one element argued abstractly |
| 5–6 | Facts mentioned but connection to elements unclear; one-sided |
| 3–4 | Rule restated; facts paraphrased; no genuine connection drawn |
| 1–2 | Conclusion jumps over analysis |
| 0 | No application attempted |

### 4. Conclusion (0–10)

Is the bottom line clear and does it follow from the application?

| Score | Standard |
|-------|---------|
| 9–10 | Clear per-issue conclusion; overall disposition stated; logically derived |
| 7–8 | Clear on most issues; one conclusion weakly supported |
| 5–6 | Conclusion present but introduces reasoning not in Application |
| 3–4 | Hedged to point of uselessness or contradicts Application |
| 1–2 | Only final words without reasoning |
| 0 | No conclusion |

### 5. Organization (0–10)

Is the IRAC structure visible? Does the essay flow logically?

| Score | Standard |
|-------|---------|
| 9–10 | IRAC clear per issue; headings or clear structure; issues in priority order |
| 7–8 | Good structure; one issue buried or out of sequence |
| 5–6 | Loose structure; reader can follow but work is needed |
| 3–4 | IRAC parts mixed together; hard to follow |
| 1–2 | Stream-of-consciousness; no discernible structure |
| 0 | Completely unstructured |

### 6. Writing quality (0–10)

Is the prose clear, concise, and grammatically correct?

| Score | Standard |
|-------|---------|
| 9–10 | Clear, concise, professional; no errors |
| 7–8 | Generally clear; occasional run-on or awkward phrase |
| 5–6 | Understandable but wordy or grammatically inconsistent |
| 3–4 | Clarity impedes comprehension |
| 1–2 | Frequent errors; difficult to parse |
| 0 | Unintelligible |

## Score format

```
OVERALL: [0–100]  (computed as sum of six dimension scores × 10/6 — rounded to nearest integer)

ISSUE SPOTTING:   [X/10]
RULE STATEMENT:   [X/10]
APPLICATION:      [X/10]
CONCLUSION:       [X/10]
ORGANIZATION:     [X/10]
WRITING QUALITY:  [X/10]
```

## Feedback format

Feedback must be:

- **Specific**: cite the student's own words and the paragraph/sentence location
- **Actionable**: every critique includes a correction prompt
- **Positive where earned**: name what the student did well before correcting

### Sample output

> **Issue spotting (8/10):** You identified the non-compete and IP assignment issues. You missed the implied warranty issue created by paragraph 12 of the employment agreement — that clause warranted a separate IRAC segment.
>
> **Rule statement (6/10):** You correctly stated the non-compete rule. However, you cited UAE Federal Decree-Law 33/2021 Art. 9 for the enforceability standard — the correct article is Art. 10 (Art. 9 covers probation). For IP assignment you stated "the employer owns work product" without citing DIFC Employment Law or the contract clause.
>
> **Application (7/10):** Strong application to non-compete facts (you cited the five-year term and Art. 10's two-year cap explicitly). On IP assignment, you didn't address the consideration question: was there separate consideration for the assignment, or was it bundled into salary?
>
> **Conclusion (8/10):** Clear bottom line per issue. Well done.
>
> **Organization (9/10):** Strong IRAC structure throughout; easy to follow. Slight improvement: the IP issue appeared mid-paragraph rather than as a separate labeled section.
>
> **Writing (8/10):** Generally clear and professional. Run-on sentences in paragraphs 4 and 7 — split each at the semicolon.

## Adaptive grading by level

| Level | Adjustment |
|-------|-----------|
| **1L** | Weight Organization more heavily (structure is the primary learning goal); lenient on rule citation format |
| **2L/3L** | Full rubric; citation accuracy matters |
| **Bar candidate** | Strict on Rule accuracy + issue spotting; writing weight reduced (no extra points for elegant prose) |
| **Trainee lawyer** | Weight Application + Conclusion most; add "practical advice quality" dimension if essay is advisory rather than analytical |

## Model answer

If requested, provide a model answer after grading. A model answer:

- Begins with a one-line issue identification per issue
- States the rule with full elements and citation
- Works element-by-element with specific fact citations
- Concludes clearly per issue and overall
- Does not exceed the expected time/word limit (signal this)

Do not provide the model answer before the student submits — it defeats the purpose.

## Limits

- This skill grades analytical structure and rule accuracy. It does not replace human assessment of jurisprudential creativity, policy arguments, or moot court performance.
- For jurisdiction-specific rule accuracy beyond well-established frameworks: flag uncertainty rather than penalize incorrectly.

## Related skills

- [[justinian-irac-coach]] — interactive coaching before the graded draft
- [[justinian-exam-time-management-coach]] — help students manage time to address all issues
- [[justinian-outline-builder]] — upstream preparation ensuring students know the rules to cite
- [[justinian-law-school-brief-summarizer]] — convert cited cases into proper brief format
