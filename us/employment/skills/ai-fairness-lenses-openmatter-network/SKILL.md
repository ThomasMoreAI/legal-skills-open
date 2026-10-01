---
name: ai-fairness-lenses-openmatter-network
title: AI fairness lenses
description: 'Use FIRST when evaluating, auditing, or debating whether an AI/ML personnel assessment is "fair" or "unbiased" — to define and defend which meaning of fairness/bias applies before drawing conclusions. Covers the three lenses from Landers & Behrend (2023): individual attitudes (distributive/procedural/ interactional justice), legality-ethicality-morality, and technical domain-embedded meanings (statistics vs. machine learning vs. psychometrics). Triggers: "is this AI hiring tool fair/biased", "what does bias mean here", "algorithmic fairness", "disparate impact vs measurement bias in AI", "bias-variance tradeoff", "define fairness for the audit".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-fairness-lenses
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, auditing]
---

# AI fairness lenses

**Before** you can audit an AI assessment for "fairness" or "bias," you must define which meaning you
are using and defend it. *Fairness* and *bias* have **very different meanings for different audiences
and disciplines.* Failing to articulate the precise standard "can render the results of an audit
uninterpretable across disciplinary lines." This skill gives you the three lenses to choose among and
combine.

Critically: the same word splits. A critic who calls an AI "unfair" may mean what another person
calls "bias"; and "bias" is itself loaded. Name the lens explicitly in any audit.

## Lens 1 — Individual attitudes (justice theory)

The most-invoked lens in public discourse. Use **organizational justice** (a tripartite perception
framework — cognitive, perceptual, emotional) to structure "this feels unfair" claims:

- **Distributive justice** — perceived fairness of *outcomes* (who gets hired). Judged against rules
  of **equality** (same outcome to all), **need** (most to those who need most), or **equity**
  (outcomes proportional to inputs/contribution). People apply different rules to the same decision,
  informed by cultural and social values. Most public "AI is unfair" complaints are implicitly
  distributive.
- **Procedural justice** — perceived fairness of the *rules and procedures* used to decide. Five
  rules often implicated by AI decisions (Ford et al.):
  1. **Opportunity to perform** — candidate feels they got a fair chance to demonstrate their value.
  2. **Job-relatedness / face validity** — e.g., do people believe facial expressions in a video
     interview relate to future performance? (And is evidence of relevance required to justify
     inclusion?)
  3. **Reconsideration / appeal** — algorithmic decisions that can't be appealed violate this.
  4. **Two-way communication** — violated when AI replaces face-to-face human interaction.
  5. **Propriety** — some simply believe AI-based decisions are morally inappropriate.
- **Interactional justice** — perceived fairness of the *interaction* with decision-makers, split
  into **interpersonal** (treated with respect/dignity) and **informational** (given adequate
  information about the decision and how it was reached). Informational justice is directly affected
  by **transparency** about what is assessed and what is done with it; interpersonal justice by the
  **presentation strategy** (e.g., an explanatory video before data collection).

Use this lens to predict and diagnose **candidate reactions** — see `ai-claims-and-stakeholder-audit`
(second-party effects).

## Lens 2 — Legality, ethicality, and morality

Fairness as alignment with shared human values and established professional/legal guidelines —
"governed by a sense of responsibility to others." Two streams:

- **Ethical / moral.** A fair system conforms to relevant and established professional guidelines.
  - The **APA Ethics Code** (2017) five principles bind any psychologist working on such a system:
    beneficence/nonmaleficence, fidelity/responsibility, integrity, **respect for people's rights and
    dignity** (treat people equitably regardless of personal/group characteristics), and **justice**
    (address and minimize one's own biases). Here "bias" ≈ a goal of impartiality, lacking individual
    prejudices and cognitive biases.
  - **AI-specific codes** — OECD *Principles on AI* (2019), Universal Guidelines for AI (UGAI, 2018) —
    reference fair/unbiased decisions but generally **don't define them precisely**; UGAI names
    reliability, validity, and data quality and uses *bias / discrimination / unfairness*
    interchangeably. These tend to leave "bias" vague so it stays applicable as standards evolve —
    effectively delegating the technical definition to Lens 3.
- **Legal.** Laws on discrimination in hiring/housing/admissions often have **precise technical
  definitions** built on statistical concepts and case law. For employment, legally establishing test
  bias generally relies on **differential prediction** (comparing regression lines across legally
  defined classes — race, sex, national origin), used to identify the source/justifiability of
  **disparate (adverse) impact** (differential selection *rates*). Contrast **differential treatment**
  — explicitly treating class members differently (e.g., awarding bonus points to a group, or modeling
  class membership as a predictor). Note: advocacy, bills, and even policy often **muddle** these
  decades-old distinct concepts, sometimes deliberately leaving "bias" vague.

## Lens 3 — Technical domain-embedded meanings of "bias"

All technical definitions share a root: **bias = inaccuracy in estimating a population value from
sample data**, where error splits into **random** vs. **systematic**. But the disciplines diverge:

- **Statistics — sampling bias.** Systematic error in sample representation vs. the population. A
  performance estimate (e.g., R² = .5) won't generalize if the training sample differs nonrandomly
  from the target population (the classic undersampled-minorities / facial-recognition database
  problem). Bias here is a consequence of **improper sampling**; fix by better/representative sampling
  or oversampling underrepresented groups (not guaranteed to work in practice).
- **Machine learning — the bias-variance tradeoff.** ML deliberately *introduces* bias (e.g., ridge,
  lasso, elastic net penalize large weights) to **reduce overfitting and improve out-of-sample
  predictive accuracy.** Here bias can be **positive and desirable** — a property of a well-engineered
  model. Prioritizing "unbiased estimates" above all (as mainstream psychology's low-bias/high-variance
  procedures do) can hurt out-of-sample prediction. The cost: individual coefficients are no longer
  cleanly interpretable.
- **Psychometrics — measurement bias / invariance.** Differences in measurement characteristics
  across identified groups, commonly assessed as **measurement invariance** (CFA latent factors) or
  IRT item parameters. Psychometric bias **may or may not be problematic**: if a measure is meant to
  assess a construct on which groups genuinely differ (e.g., educational attainment shaped by systemic
  opportunity differences), group differences are expected and the test may be **biased-but-fair**.
  Note the psychometric caution that **differential prediction is not a *sufficient* condition for
  bias** — a test can show differential prediction without problematic measurement properties (the
  "six sigma"/manager age example: younger applicants score lower because they've had less exposure,
  yet if managerial experience is job-related the differential prediction may still be considered
  fair).

## How to use the lenses in an audit

1. **State the claim** being evaluated and **who** is raising the fairness concern.
2. **Pick the lens(es)** that match — concerns may invoke any or all three.
3. **Define the standard precisely** within that lens (which justice rule? which legal test? which
   technical bias?) and **write it into the audit** so conclusions are interpretable.
4. **Don't equivocate** — a finding of "no measurement bias" (Lens 3) does not answer a distributive
   or procedural-justice complaint (Lens 1) or a legal disparate-impact question (Lens 2).
5. Carry the chosen standard into the model, stakeholder, and meta audits.

## Pitfalls

- Auditing "fairness" without naming a lens → uninterpretable results.
- Treating any group difference as "bias" (psychometrically it may be expected and fair).
- Assuming "bias is always bad" — in ML, intentional bias improves generalization.
- Conflating differential prediction, disparate impact, and differential treatment.
- Answering a procedural/distributive-justice complaint with a purely statistical result.

## Checklist

- [ ] Fairness concern's source/audience identified
- [ ] Lens(es) selected and named in the audit
- [ ] Precise standard defined within each lens (justice rule / legal test / technical bias type)
- [ ] Cross-lens gaps acknowledged (statistical result ≠ justice answer)
- [ ] Standard documented and propagated to downstream audit components

## See also

`ai-audit-planning` · `ai-model-outputs-audit` (subgroup differences, measurement bias) ·
`ai-claims-and-stakeholder-audit` (justice/candidate reactions) ·
`fairness-and-bias-analysis` (predictive vs. measurement bias in the Principles)

*Source: Landers & Behrend (2023), "Defining Fairness and Bias"; Lenses 1–3; "Contrasting Statistics,
Machine Learning, and Psychometrics Perspectives."*
