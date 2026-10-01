---
name: ai-model-outputs-audit-openmatter-network
title: AI model-outputs audit (Component 6)
description: 'Use when auditing the scores an AI/ML personnel assessment produces — Component 6 of the Landers & Behrend (2023) framework. Covers evaluating the quality of model predictions: reliability (consistency over time and repeated administrations), validity evidence (do scores reflect the claimed constructs and predict the outcome), appropriateness of the cross-validation given generalizability claims, and subgroup differences across protected classes and their intersections. Triggers: "evaluate AI assessment scores", "algorithm reliability and validity", "subgroup differences in algorithm scores", "intersectional bias audit", "does the AI score predict performance", "adverse impact of the model outputs".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-model-outputs-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, auditing]
---

# AI model-outputs audit (Component 6)

The payoff component: regardless of how the model was built, **are its scores good?** This is where
the AI audit reconnects most directly to classic psychometrics and the SIOP *Principles* — apply the
personnel-selection skills here, on the model's **actual operational outputs**.

**What it is:** evaluation of the **quality of the predictions** the model generates.

**Questions to ask:** How was prediction quality evaluated — e.g., for **psychometric reliability and
validity**? How was **cross-validation** conducted, and was it **appropriate given the claims about
model generalizability**?

**Apply it (focal example):**
- **Reliability** — Are scores **consistent over time and upon multiple administrations**? A candidate
  who records the same interview twice, or whose video is scored repeatedly, should get stable scores.
- **Validity** — Is there evidence the scores **reflect the predicted constructs they claim to**, and
  relate to the intended outcome? Don't accept a predictive R² as construct validity.
- **Subgroup differences** — Do scores show **differences among classes of interest** — race, gender,
  color, national origin, religion, disability, age — **and combinations of classes** (intersectional
  subgroups)? AI's high-dimensional inputs make intersectional effects both more likely and easier to
  overlook.

## How to audit outputs (bring the Principles to bear)

1. **Reliability evidence.** Identify the conditions you must generalize across (occasions, repeated
   administrations, alternate prompts, re-scoring) and estimate the **matching** reliability. For
   stochastic models or pipelines with random elements, test **score stability under re-run**. See
   `criterion-related-validation` (reliability of measures).
2. **Validity evidence.** Treat the model as a selection procedure: assemble criterion-related and/or
   construct evidence that scores predict the **defensibly defined** outcome (tie back to the
   Component-2 criterion audit). Beware **overfitting**: a cross-validated estimate beats holdout,
   which beats temporal — confirm the **cross-validation matches the generalizability claim** (a tool
   used on future applicants needs evidence that survives **temporal** validation, not just k-fold).
   See `criterion-related-validation` and
   `internal-structure-validation`.
3. **Subgroup / bias analysis — run the right test for the right lens.** A subgroup **mean
   difference** (adverse impact) is a **scrutiny trigger, not a verdict** of bias (Lens 2/3).
   - **Predictive bias / differential prediction** — test on the **operational score as used**
     (the composite the model outputs), not internal sub-features; ask whether a subgroup is
     **underpredicted**, watch power, range restriction, and error-variance homogeneity. See
     `fairness-and-bias-analysis`.
   - **Measurement bias / invariance & DIF** — check whether score meaning is invariant across groups;
     remember psychometric bias **may be expected and "fair"** when groups truly differ on the
     construct (`ai-fairness-lenses`, Lens 3).
   - **Intersectional subgroups** — analyze combinations of classes where data and power allow;
     report what couldn't be analyzed.
4. **Generalizability check.** Confirm the validation sample and cross-validation support the
   population where the tool is deployed (the incumbent-vs-applicant / range-restriction problem from
   Component 1 resurfaces in the output evidence).

## Connecting to the developer's claim

The focal developer claims the algorithm "predicts job performance equally well for all groups using
appropriate modeling techniques." That claim is evaluated **here** — and the paper calls it
**questionable and in need of audit.** Translate it into testable pieces: (a) equal predictive
accuracy across groups, (b) no problematic differential prediction, (c) appropriate modeling — and
require evidence for each.

## Pitfalls

- Accepting predictive accuracy as evidence of construct validity.
- Reporting k-fold validity when the deployment claim requires temporal generalization.
- Testing bias on internal features instead of the operational output score.
- Treating a mean difference as proof of bias, or "no measurement bias" as proof of fairness.
- Ignoring intersectional subgroups because each is small (note the limitation explicitly).
- Skipping score-stability/reliability checks for stochastic pipelines.

## Checklist

- [ ] Reliability estimated for the conditions of intended use; re-run/re-score stability tested
- [ ] Validity evidence ties scores to the defensibly defined criterion (not just R²)
- [ ] Cross-validation method matches the generalizability claim (temporal where deployment drifts)
- [ ] Predictive bias tested on the operational output, framed as underprediction, with adequate power
- [ ] Measurement invariance / DIF considered; expected-vs-problematic differences distinguished
- [ ] Subgroup differences examined across protected classes **and** intersections; gaps reported
- [ ] Developer's "equal prediction for all groups" claim decomposed and each part evidenced

## See also

`ai-input-data-and-design-audit` · `ai-model-development-audit` · `ai-fairness-lenses` ·
`criterion-related-validation` ·
`internal-structure-validation` ·
`fairness-and-bias-analysis` · `selection-decisions-and-scoring`

*Source: Landers & Behrend (2023), Table 1 (Component 6).*
