---
name: ai-validity-evidence-openmatter-network
title: AI validity evidence (Concern 5)
description: 'Use when determining what validity evidence an AI/ML selection tool needs and whether it has it — Concern 5 of Tippins, Oswald & McPhail (2021). Covers validity as the legal/business sine qua non when adverse impact exists, AI tools as "tests" requiring validity, criterion-related vs. content strategies and why content validation is hard for AI, overall model fit (R-squared) as sometimes the only basis, comparative data for less-adverse alternatives, and the minimum documentation requirements. Triggers: "what validity evidence does the AI tool need", "validate an algorithm", "content validation for AI", "R-squared as validity", "document AI validation", "is overall model fit enough".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-validity-evidence
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI validity evidence (Concern 5)

Among I-O psychologists there is **no doubt** about the importance of validity. Evidence of validity
is necessary to demonstrate a selection procedure's effectiveness, and it is a **legal requirement
when adverse impact is observed.** For business and legal-defensibility reasons, **validity is a
*sine qua non* of selection research** — including for AI tools.

This is the AI-specific framing; for *how* to gather validity evidence, use
`criterion-related-validation`,
`content-based-validation`, and
`generalizing-validity-evidence`.

## AI tools are "tests" — so they need validity

AI-based predictors, game-oriented tools, and evaluations of facial features and voice qualities used
to decide whom to hire are **tests under both the law and professional guidelines** (UGESP §2B: a test
is any selection procedure used for an employment decision). Therefore:
- In the **U.S.**, their use must be supported by **validity evidence if adverse impact results.**
- In **all countries**, validity evidence **provides the business justification** for use.

## Which validity strategy — and the AI wrinkle

- **Criterion-related** — a statistical relationship between scores and a relevant criterion
  (correlation/regression). Report strength via **size, confidence interval, and significance**;
  regression should indicate **imprecision** (CIs, bootstrapping, cross-validation). Traditional
  selection rarely models **nonlinearities** (linearity affords interpretability and needs less
  power); ML **does** model and cross-validate nonlinearities, but interpretation is difficult and
  power may or may not be an issue depending on the number of variables and cases.
- **Content** — SMEs relate the **content of the test to job requirements.** Because of the nature of
  AI-based tests, **content validation evidence is often not used at all, or only to supplement** a
  criterion-related study. (When content can't carry the argument, criterion evidence and job analysis
  must.)

### When overall model fit is the only handle
Some ML methods are based on regression (logistic, lasso, ridge, elastic net) and yield **coefficients**
— a "demonstration of a relationship." But complex models (random forests, neural nets) or **clustering**
approaches don't express relationships as apparent, direct coefficients. There, **overall model fit
(analogous to R² in regression) may be the only basis** for establishing the predictor–criterion
relationship — which makes **job analysis all the more important** to ensure job-relevant predictors
and criteria are the ones in the model, even when their weighting is opaque.

## Comparative data and the alternatives duty

Because U.S. employers are obligated to search for **alternative procedures with equal or greater
validity and less adverse impact** (UGESP §3B), **comparative data are particularly important.** The
empirical, meta-analytic history of validities in I-O psychology can serve as a **reasonable baseline
the ML model should have to beat** — but vendor claims of "higher validity / lower adverse impact" are
frequently **unaccompanied by the evidence needed to make the comparison.**

## Fundamental requirements and documentation

A key open question: should users of algorithm-based procedures be **required to provide specific
conceptual and empirical evidence of predictor–criterion relationships**, in addition to overall model
metrics? The *Uniform Guidelines*, *Principles*, and *Standards* all enumerate the components a
technical report should document — yet critical information is **often omitted**, and the problem is
**acute for AI** because so many decisions are made in selecting and tuning the model. Documentation
should let an external party **understand, evaluate, and reproduce** the work. Ask:
- How were data **obtained, prepared, cleaned, transformed, and combined**? What approach handled
  **missing data**?
- With text mining / written responses, were effects of **vocabulary knowledge or verbal fluency
  controlled** where the text wasn't meant to measure verbal ability?
- How was **conflicting applicant data** weighted, discarded, or cleaned?
- Was **one** algorithmic approach taken or **several**, and could an **external party reproduce** the
  analysis?
- Were algorithm choices **a priori** or **post hoc**? Were predictions **combined across algorithms**?
- Was there **post hoc filtering** — inspecting results to pick the algorithm that "looked good"
  (a **suspect** practice)?

## Questions to ask (from the article)

- What is **sufficient evidence of validity** when ML models are used?
- What details of the AI research **must be documented**?
- What details of the AI research **must be shared with users**?

## Pitfalls

- Treating "no adverse impact" as a substitute for validity (see `ai-selection-legal-landscape`).
- Accepting overall model fit (R²/AUC) without job-analytic grounding of the predictors/criterion.
- Accepting "more valid, less adverse impact" claims without the comparative evidence.
- Tolerating post hoc algorithm selection / filtering without cross-validation safeguards.
- Thin documentation that no external party could reproduce.

## Checklist

- [ ] Tool treated as a "test" requiring validity (esp. if adverse impact)
- [ ] Validity strategy chosen (criterion-related / content / generalization) and justified for AI
- [ ] If only overall model fit is available, predictor/criterion job-relevance secured via job analysis
- [ ] Imprecision reported (CIs, bootstrapping, cross-validation)
- [ ] Comparative data vs. traditional/meta-analytic baselines and less-adverse alternatives provided
- [ ] Data prep, missing-data, weighting, and algorithm-selection decisions documented and reproducible
- [ ] Post hoc filtering ruled out or controlled; evidence shared with users

## See also

`criterion-related-validation` · `content-based-validation`
· `generalizing-validity-evidence` · `technical-validation-report`
· `ai-selection-tech-data-algorithms` (why a technology is not "universally valid") ·
`ai-ml-methodology-evaluation` (model-fit metrics) · `ai-job-analysis-and-relevancy` ·
`ai-selection-legal-landscape` · `ai-model-outputs-audit`

*Source: Tippins, Oswald & McPhail (2021), Concern: "Validity."*
