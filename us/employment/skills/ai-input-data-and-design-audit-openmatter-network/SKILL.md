---
name: ai-input-data-and-design-audit-openmatter-network
title: AI input-data & model-design audit (Components 1–2)
description: 'Use when auditing the data and foundational design of an AI/ML personnel assessment — Components 1-2 of the Landers & Behrend (2023) framework. Covers input-data population, sampling, range restriction, and incumbent-vs-applicant generalizability; and model design: how the criterion ("ground truth") is defined and its construct validity, why each predictor/feature was included, and whether choices were theory-driven or empirically derived. Triggers: "audit training data", "is the training sample representative", "ground truth validity", "why are these features predictors", "criterion definition in AI hiring", "range restriction in algorithm training data".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-input-data-and-design-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, auditing]
---

# AI input-data & model-design audit (Components 1–2)

The two **far-reaching, hard-to-reverse** decisions at the base of any AI assessment. Get these wrong
and everything built on top inherits the flaw — yet they're often the least documented. Define your
fairness standard first (`ai-fairness-lenses`) and scope via `ai-audit-planning`.

## Component 1 — Input data

**What it is:** the validity and generalizability of the dataset(s) used to **train** the model,
relative to the population where predictions will actually be generated and used.

**Questions to ask:** How were input data collected, in terms of **population** and **research
design**? How did those factors affect **data quality**? Evaluate the population the data were drawn
from, the **sampling techniques**, and the adequacy of the data for the analyses later used to support
claims.

**Apply it (focal example — algorithmic video interview):** Were input data collected from **job
incumbents**? How do incumbents differ from **applicants**? Is there **range restriction** on
variables of interest? A model trained on a *convenient source of existing candidates/incumbents* is
no guarantee of representativeness for **future** applicants — so a key audit goal is to evaluate
**how the developers investigated that assumption and concluded it was not a problem.**

**Audit emphases:**
- This is the AI face of classic validation concerns: **population selection** and the
  **concurrent-vs-predictive** design choice directly shape what can be inferred (see SIOP *Principles*
  via `criterion-related-validation`).
- **Sampling bias** (Lens 3, statistics): nonrandom under-/over-representation (e.g., undersampled
  minorities) makes the model weight patterns of the most-represented group; "we'll just collect a
  more diverse database / oversample" is **not guaranteed** to fix it.
- **Every** training dataset counts — including later **subset datasets** used for more specific
  modeling challenges. Each must meet the **same quality standard**, embedded in a meaningful data
  engineering framework. Don't let a well-vetted primary dataset launder a sloppy secondary one.

## Component 2 — Model design

**What it is:** the **initial** modeling decisions that are difficult to test or change later. The
three most consequential:
1. the **nature of the criterion** modeled,
2. the **set of predictors/features** provided to the model,
3. the **initial set of algorithms** used.

Even when the data are adequate (Component 1), the criterion and the available predictor set **drive
many subsequent steps.** These choices may be made conceptually, empirically, or heuristically — ask
which, and demand the rationale.

**Questions to ask:** What drove the initial model choices (criterion, predictor set, algorithm)?
Were they **informed by theory or empirically derived**? If empirically derived, **from what data —
and of what quality — were they derived**?

**Apply it (focal example):**
- **Criterion / "ground truth" validity is the crux.** "Performance data were available" is not
  enough — audit the **construct validity** of that performance measure as a valid representation of
  *performance*, including a **clear, unambiguous, scientifically defensible definition** of what
  performance is. In computer science this is framed as choosing a **"ground truth," often without any
  explicit consideration of construct validity** — name and close that gap.
- **Predictor inclusion needs a rationale.** Why are **word choice, answer content, voice patterns,
  and visual data** included as predictors? Are those decisions **theoretically supported**? Even
  though weak features can be dropped in later analytic stages, their **initial inclusion is a
  design-stage decision** that creates **technical debt** and **sunk-cost** pressure — and, in the
  focal example, drags in construct-irrelevant correlates (wrinkles→age, skin tone→race/ethnicity,
  makeup→gender) that the designer may not even realize the model is exploiting.

**Audit emphases:**
- Tie criterion definition back to a real **analysis of work**
  (`work-analysis`) — a defensible ground truth requires it.
- Watch **criterion reconceptualization / weighting** decisions: down-weighting task vs. up-weighting
  contextual performance can reduce adverse impact, but such weighting has **validity implications**
  (Sackett et al., 2008) and must be **carefully articulated and defended**, not silently chosen.
- Flag predictors that proxy **protected characteristics**; inclusion-by-default is a finding.

## Pitfalls

- Accepting "data were available" without auditing the criterion's construct validity.
- Treating incumbent-trained models as valid for applicants without addressing range restriction.
- Letting a clean primary dataset excuse unvetted subset datasets.
- Reading "features can be pruned later" as a reason not to justify their initial inclusion.
- Missing predictor proxies for protected class because the developer "didn't intend" them.

## Checklist

- [ ] Training population vs. deployment population compared; representativeness investigated
- [ ] Sampling technique evaluated for sampling bias; range restriction assessed
- [ ] Concurrent-vs-predictive design implications stated
- [ ] All training datasets (incl. subsets) held to the same quality standard
- [ ] Criterion/"ground truth" has a clear, defensible, construct-valid definition tied to work analysis
- [ ] Rationale for each predictor/feature (theory or empirics + data quality) obtained
- [ ] Construct-irrelevant proxies for protected characteristics flagged
- [ ] Criterion weighting choices articulated and defended

## See also

`ai-model-development-audit` · `ai-model-outputs-audit` · `ai-fairness-lenses` ·
`work-analysis` · `criterion-related-validation`
(criterion development, range restriction, concurrent/predictive)

*Source: Landers & Behrend (2023), Table 1 (Components 1–2) and "Components Relating to Models" prose.*
