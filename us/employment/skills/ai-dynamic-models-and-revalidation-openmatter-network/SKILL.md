---
name: ai-dynamic-models-and-revalidation-openmatter-network
title: AI dynamic models & revalidation (Concern 7)
description: 'Use when an AI/ML selection tool uses "dynamic" models or norms that update frequently (sometimes after every administration), or when deciding how often to revalidate and update norms — Concern 7 of Tippins, Oswald & McPhail (2021). Covers the real-change-vs-instability dilemma, technical-report/documentation updates, score adjustments and grandparenting, disparate-treatment risk from candidates evaluated on different variables, applicant-pool shifts affecting validity/range restriction, and revalidation cadence. Triggers: "dynamic models hiring", "algorithm updates after every administration", "how often revalidate AI", "norms updating", "grandparenting test scores", "candidates scored on different variables", "continuous validation".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-dynamic-models-and-revalidation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI dynamic models & revalidation (Concern 7)

ML-derived selection procedures enable analysis that wasn't feasible before, and many vendors **refresh
the algorithm frequently — sometimes after every test administration.** Such "dynamic" procedures
update validation evidence and normative data in **near real time.** That creates a dilemma and several
operational problems.

## The core dilemma

When a dynamic model changes, the change could reflect either:
- a **real change** in the nature of the applicant sample and/or the job (which *should* drive an
  update), **or**
- **sample idiosyncrasies or instabilities** over time that **should not be capitalized on.**

Distinguishing the two is hard — and capitalizing on instability degrades the model.

## Why "dynamic" raises problems

1. **Documentation must keep up.** Validity evidence must be documented in a **technical report.** So
   every update to the underlying selection process requires **updating the technical report** (validity
   *and* normative-data characteristics). **Out-of-date reports are problematic** for legal
   defensibility and for HR records maintenance over time. (See `technical-validation-report`.)
2. **Score adjustments & grandparenting.** Each new selection process may require **adjusting scores**
   already in the database, or a **policy** on how to treat scores produced by different processes at
   different times. Continual adjustment creates administration problems: a candidate **qualified today
   may be unqualified tomorrow** (or vice versa). Changes can include **altering predictor weights,
   adding/removing predictors, and changing interpretations** (e.g., adjusting **cutoff scores**).
   **Grandparenting** policies are administratively hard to manage in high-volume programs. (See
   `selection-decisions-and-scoring`.)
3. **Disparate-treatment / disparate-impact risk.** A result of frequent change is that **different
   candidates are evaluated on different variables depending on when they applied.** If that variation
   relates to a protected characteristic, there's a **disparate-impact** specter; even **without**
   group-level disparate impact, **disparate-treatment** concerns can arise — and the **appearance** of
   such treatment can trigger applicant dissatisfaction and complaints.
4. **Applicant-pool shifts.** Large shifts in the applicant pool can materially affect **reliability,
   validity, range restriction, or range enhancement** on big data — so **monitor key applicant-pool
   characteristics** (demographic, educational). Future shifts in available technologies/data/algorithms
   may change the applicant database and **indicate the ML model should be updated.**
5. **Defining group comparisons.** Frequent algorithm changes make it **harder to define relevant
   applicant pools** for adverse-impact analysis or appropriate **normative groups** for comparison.

## Revalidation & norms updating

Employers have **always** revalidated and updated norms; with AI the difference is the **frequency.**
Traditionally, revalidation was triggered when the job changed, the test was compromised, the applicant
pool shifted substantially, or enough time elapsed to question validity in a legal challenge — and it
was undertaken at **well-spaced intervals** because it was laborious. Today's computing power makes
**continuous updating** far less laborious, which raises a genuinely open question: **how often should
validation be refreshed** to accommodate the nature of new applicant data?

## Questions to ask (from the article)

- Are **dynamic algorithms and norms useful?**
- How should results from dynamic algorithms be **documented to comply with existing and future legal
  and administrative requirements?**
- How **frequently** should tests be revalidated and norms updated?
- What are the **indicators** that revalidation and updates to norms are needed?

## Pitfalls

- Capitalizing on sample instability and mistaking it for real change.
- Letting technical reports/normative documentation fall out of date as the model drifts.
- Unmanaged score adjustments → candidates flipping qualified/unqualified; messy grandparenting.
- Evaluating different applicants on different variables → disparate-treatment exposure (and optics).
- Not monitoring applicant-pool shifts that invalidate prior validity/range assumptions.
- Unstable pool/normative definitions that make adverse-impact analysis incoherent.

## Checklist

- [ ] Each model/norm update justified as real change, not instability
- [ ] Technical report and normative documentation updated with every change
- [ ] Score-adjustment / grandparenting policy defined and administrable
- [ ] Risk that candidates are scored on different variables (disparate treatment) assessed
- [ ] Applicant-pool characteristics monitored for shifts affecting validity/range
- [ ] Revalidation/norms-update cadence and trigger indicators defined
- [ ] Adverse-impact pools and normative groups remain definable under the update regime

## See also

`ai-validity-evidence` · `ai-selection-legal-landscape` ·
`generalizing-validity-evidence` ·
`technical-validation-report` ·
`administration-documentation` (review/updating, records) ·
`selection-decisions-and-scoring` (cutoffs, norms)

*Source: Tippins, Oswald & McPhail (2021), Concern: "Changes to Technologically Enhanced Systems"
(Dynamic models and norms; Revalidation and norms updating).*
