---
name: quality-checker
title: Quality Checker
description: Run the 8-item legal research quality gate and decide pass/fail with remediation steps.
author: kipeum86
author_url: https://github.com/kipeum86/game-legal-research/tree/main/.claude/skills/quality-checker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Quality Checker

Use this skill at Step 9 against the Step 8 draft before citation audit and final delivery.

## 8-Item Checklist

1. Every key conclusion has at least one Grade A or B `primary`-authority source citation. A secondary source (law-firm memo, academic article, practitioner guide) does not satisfy this requirement regardless of its grade.
2. Legal hierarchy is not conflated.
3. Amendment/effective dates and currency are checked.
4. Jurisdiction level is accurate.
5. Uncertain claims are clearly marked.
6. All 6 mandatory output sections are present (scope & as-of date; conclusion summary; issue tree; detailed analysis; annotated bibliography; verification guide with pinpoints mapping each conclusion to a citation and URL/database target).
7. No D-grade source is cited as a basis (sole or partial) for any conclusion.
8. **No source laundering:** Every factual assertion or legal position attributed to a primary source in the narrative must trace to a directly fetched or verified primary-source text. If a claim was learned from a secondary source, it must either (a) be independently verified against the primary source and cite the primary source, or (b) be explicitly attributed to the secondary source with `[Secondary Commentary]` marking.

## Output Format

```json
{
  "quality_gate": "pass|fail",
  "failed_items": [1, 4],
  "remediation_plan": [
    "Re-enter Step 3 for issue X",
    "Patch section Y with new source Z"
  ]
}
```

## Remediation Policy

- Round 1: collect additional sources for failing items.
- Round 2: patch only failing sections.
- If still failing: deliver with `[Unverified]` tags.

## Pre-flight Check (run at Step 7, before output generation)

Evaluate the analysis result against the five source-level items below.
Items #3 and #6 from the full 8-item checklist (which require the formatted output to exist) are deferred to Step 9.

| Pre-flight # | Full checklist # | Check |
|------|------|-------|
| 1 | #1 | Every key conclusion has at least one Grade A or B `primary`-authority source citation. Secondary sources (regardless of grade) do not satisfy this. |
| 2 | #2 | Legal hierarchy is not conflated — statute, regulation, guidance, and secondary sources are correctly distinguished. |
| 3 | #4 | Jurisdiction level is accurate — federal, state/province, EU-level, and member-state rules are not mixed. |
| 4 | #5 | No uncertain claim is stated as certain — all unconfirmed points use hedged language or `[Unverified]`. |
| 5 | #7 | No D-grade source is cited as a basis (sole or partial) for any conclusion. |
| 6 | #8 | No source laundering — every factual or legal claim presented as primary-source-backed is traceable to a directly fetched/verified primary text, not paraphrased from a secondary source. |

### Pre-flight Output Format

```json
{
  "preflight": "pass|fail",
  "failed_items": [1, 5],
  "failing_issues": [
    {
      "issue_id": "KR-D1-I1",
      "failed_item": 1,
      "reason": "No primary source found for probability-disclosure requirement",
      "retry_keywords": ["게임산업진흥에 관한 법률 시행령 확률형 아이템", "문화체육관광부 고시"]
    }
  ]
}
```

If `preflight` is `"pass"`, proceed immediately to Step 8.
If `preflight` is `"fail"`, execute targeted Step 3 retry for `failing_issues` only, then re-run
the affected portions of Step 6 before re-running this pre-flight check.
