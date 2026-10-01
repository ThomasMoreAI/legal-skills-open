---
name: ai-reliability-openmatter-network
title: AI reliability (Concern 6)
description: 'Use when evaluating the reliability (score consistency/stability) of an AI/ML selection tool — Concern 6 of Tippins, Oswald & McPhail (2021). Covers reliability as an absolute requirement, what stability means for AI scores, evidence that machine scoring can be as or more reliable than human scoring, the questionable reliability of facial-emotion analysis (including across skin tone, disability, and altered features), and confounds from individual differences in the data generated (e.g., extraversion/verbosity). Triggers: "reliability of an AI assessment", "are the scores stable", "facial emotion recognition reliability", "machine-scored interview reliability", "test-retest for AI hiring", "verbosity confound".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-reliability
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI reliability (Concern 6)

Like validity, **reliability is an absolute requirement** for any test. The *Uniform Guidelines*
require reliability to be evaluated and reported (§§14C(5), 15B(7), 15B(8)); the *Principles* (p. 22)
require predictor scores to exhibit adequate reliability and to identify the **conditions of
measurement** across which one wishes to generalize.

For *how* to estimate reliability, use `criterion-related-validation`
(predictor/criterion reliability) and `ai-model-outputs-audit`.

## What reliability requires of an AI tool

To be reliable, scores must measure KSAOs that are **relatively stable and consistent over time and
setting:**
- An applicant's score should be **about the same if they retook the assessment a week later**
  (memorization notwithstanding).
- Scores should **not be contingent** on day or time of testing, testing conditions, or particular
  equipment **unless those are job relevant.**
- **Reliable changes** in scores should reflect changes in the **job-relevant construct** (gained
  skill) or **reduced irrelevancy** (less anxiety, better understanding of the protocol) — not
  artifacts.
- A **game** score should not reflect idiosyncrasies of the game or baseline skills beyond what's
  normally required (e.g., multikey or mouse facility).

## The evidence is thin and mixed

Reliability evidence for technologically enhanced measures is **often minimal or difficult to obtain**;
when available, results are **mixed.**
- **Machine-scored interviews:** some evidence shows reliability is **high — sometimes higher than
  interviewer-scored** — with substantial agreement with well-trained humans. Because human scorers in
  operational settings are notoriously prone to error and low interrater agreement, there's
  long-recognized **potential for greater reliability and fairness in algorithmic scoring** (Kuncel et
  al., 2013) **so long as job-relevant information is what's being scored.**
- **Facial-feature / emotion analysis:** reliability is **particularly questionable.** Even if facial
  expressions can reliably signal categories of emotion in human judgment (Cowen & Keltner, 2019),
  studies suggest the **faces of people with darker skin are harder to evaluate via AI** (Singer &
  Metz, 2019). It is **unclear how the tool treats** people with **injuries, disabilities, medication
  effects, or altered features** (scars, tattoos) — a reliability *and* fairness problem.

## Confounds from how the data are generated

Threats to reliability can come from **individual differences in the data collected**, not just how
they're measured. For example, **more extraverted applicants provide more detail** in written or
spoken responses, giving the algorithm **more key words** that may relate to **other traits** (cognitive
ability, verbal skills) not necessarily related to extraversion. So big data, ML, or both can end up
**affecting the reliability of *other* traits** the tool claims to measure — a subtle source of
construct-irrelevant variance.

## Questions to ask (from the article)

- How should **reliability be assessed** when AI is used to build the predictive models used for
  selection?
- What should the **minimal requirements for documentation** of reliability be?
- Are **appropriate and sufficient** measures of reliability available and reported for technologically
  enhanced assessments?
- Are the new forms of employment assessment **sufficiently reliable to meet psychometric standards?**

## Pitfalls

- Assuming algorithmic scoring is automatically reliable (it depends on *what* is scored).
- Ignoring stability across occasions/conditions (no test–retest evidence).
- Overlooking lower reliability of facial analysis for darker skin, disabilities, or altered features.
- Missing verbosity/extraversion confounds that contaminate other trait scores.
- Accepting "the model is consistent" without documentation of the conditions of measurement.

## Checklist

- [ ] Reliability evaluated and reported for the conditions of intended use
- [ ] Score stability over time/occasions demonstrated (re-administration / re-scoring)
- [ ] Job-irrelevant dependencies (day, equipment, game idiosyncrasies) ruled out
- [ ] Facial/voice analysis reliability checked across skin tone, disability, altered features
- [ ] Data-generation confounds (e.g., verbosity → other traits) examined
- [ ] Documentation of reliability sufficient to meet UGESP/Principles/Standards

## See also

`ai-validity-evidence` · `ai-ml-methodology-evaluation` · `ai-dynamic-models-and-revalidation`
(stability vs. frequent updating) · `ai-candidate-data-control` (disability/appearance fairness) ·
`criterion-related-validation` (reliability estimation) ·
`fairness-and-bias-analysis` ·
`ai-model-outputs-audit`

*Source: Tippins, Oswald & McPhail (2021), Concern: "Reliability."*
