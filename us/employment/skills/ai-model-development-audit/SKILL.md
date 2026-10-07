---
name: ai-model-development-audit
title: AI model-development audit (Components 3–5)
description: 'Use when auditing how an AI/ML personnel assessment was actually built once its design was set — Components 3-5 of the Landers & Behrend (2023) framework: model development (refinement and cross-validation strategy, documentation), model features (feature engineering — NLP tokens vs. topics, speech-to-text, extracted facial/voice features), and model processes (the estimation algorithm, alternatives explored, and stress tests for bias). Triggers: "audit feature engineering", "k-fold vs holdout vs temporal validation", "NLP bag-of-words bias", "speech-to-text reliability", "how was the model refined", "stress test the algorithm for bias", "model development documentation".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-model-development-audit
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags:
- community
- io-psychology
- ai-assessment
- auditing
---

# AI model-development audit (Components 3–5)

Where design becomes a working model. Guidance from the *Principles*/*Standards* gets thin here and
**machine-learning expertise becomes essential** — many decisions live only in code (R/Python) or in
developers' heads and are **highly idiosyncratic to the specific model.** The audit's job is to drag
those decisions into documentation and test their effect on validity and bias.

## Component 3 — Model development

**What it is:** the specific approach used to **refine** the model after the initial design. Highly
idiosyncratic; the central evaluative question is whether it is **documented**.

**Questions to ask:** Once the initial model was created, how was it **refined**? What approaches were
taken, and what likely effect did they have? **Is every decision about every model created during
development fully documented?**

**Common failure — selective cross-validation reporting:** A frequent issue is the choice among
**k-fold**, **holdout**, and **temporal** cross-validation. Performance typically ranks
*k-fold ≥ holdout ≥ temporal* (temporal is worse because model performance **decays over time**). So
developers may report **only k-fold** results — potentially hiding information or signaling an
incomplete development process. **Audit move:** all three approaches could be run and compared; if
they weren't, the **reasons for the omissions should be identified.** Temporal validation matters most
for an operational hiring tool whose population drifts.

**Criterion reconceptualization recurs here too:** refinement often re-weights the criterion (e.g.,
**task vs. contextual performance**). Down-weighting task and up-weighting contextual performance can
**reduce adverse impact**, but alternative weighting schemes carry **validity implications** (Johnson,
2001; Sackett et al., 2008) and must be **explicitly articulated and defended**, not quietly tuned for
a fairness metric.

## Component 4 — Model features

**What it is:** the **feature-engineering** process that turns raw input data into the final
predictors. The area where ML resources most exceed existing psychological guidance.

**Questions to ask:** How were raw input data engineered into model features? Was the process
**conceptually or empirically driven**? What **alternative** feature-engineering approaches were
explored?

**Apply it (focal example):**
- **NLP / bag-of-words:** word counts become **tokens** — entailing *hundreds of decisions* about the
  nature of language and its meaningfulness to the prediction. Tokens may be raw **frequencies** or,
  alternatively, built from **topics**. A **topic-based** model can **reduce bias by minimizing the
  influence of dialect** — yet that choice has **validity impacts** that must be evaluated. Neither is
  free.
- **Speech-to-text conversion** is itself a (often **third-party**) ML model whose "state of the art"
  is a **constantly moving target**, with direct implications for **reliability and validity**. Audit
  the **quality** of the conversion, not just the downstream scorer.
- **Extracted facial/voice features:** ask *which* facial features emerged from analyzing video and
  *what biases* were explored in the engineering process (recall the wrinkles/skin-tone/makeup proxies
  from design).
- **Every step between "raw input data" and "engineered features" must be fully investigated** — this
  is where construct-irrelevant variance is silently introduced.

## Component 5 — Model processes

**What it is:** the specific **estimation process** by which the final model generates predicted
scores (the choice among the many available ML algorithms and how inputs are combined into a score).

**Questions to ask:** How does the model **use inputs to generate scores**? How were **alternative
approaches explored and evaluated**?

**Apply it (focal example):** What **stress tests** were conducted, and what **types of bias** were
investigated? **Did these tests result in changes to the model — and if so, how and why?** A model
that was never stress-tested for bias, or where tests were run but never acted on, is a finding.

**Audit emphases:**
- Remember the **bias-variance tradeoff** (Lens 3, ML): regularization (ridge/lasso/elastic net)
  **intentionally** introduces bias to improve out-of-sample accuracy — desirable, but it sacrifices
  coefficient interpretability, complicating "why did it score me this way" explanations relevant to
  procedural/informational justice.
- Probe whether **alternative algorithms** were genuinely compared or whether one was chosen by
  convenience/familiarity.

## Pitfalls

- Accepting **k-fold-only** performance without asking why holdout/temporal were omitted.
- Ignoring **performance decay over time** for an operational tool.
- Treating speech-to-text / third-party preprocessing as a black box exempt from audit.
- Letting criterion re-weighting tune a fairness metric without defending the validity cost.
- Accepting "the model is regularized" without examining interpretability/justice consequences.
- No documented stress tests, or tests run but never acted upon.

## Checklist

- [ ] Every refinement decision documented (or the gaps recorded as findings)
- [ ] Cross-validation strategy examined; k-fold/holdout/temporal compared or omissions justified
- [ ] Performance-decay (temporal) risk assessed for the operational population
- [ ] Criterion re-weighting decisions articulated and defended on validity grounds
- [ ] Feature engineering traced step-by-step from raw input to final features
- [ ] NLP choices (tokens vs. topics) and their bias/validity tradeoffs evaluated
- [ ] Speech-to-text / third-party preprocessing quality audited
- [ ] Estimation algorithm and alternatives evaluated; bias-variance consequences considered
- [ ] Bias stress tests documented, with resulting model changes (or their absence) explained

## See also

`ai-input-data-and-design-audit` (upstream) · `ai-model-outputs-audit` (downstream) ·
`ai-fairness-lenses` (bias-variance, measurement bias) ·
`criterion-related-validation` (cross-validation, weighting, corrections)

*Source: Landers & Behrend (2023), Table 1 (Components 3–5) and "Components Relating to Models" prose.*
