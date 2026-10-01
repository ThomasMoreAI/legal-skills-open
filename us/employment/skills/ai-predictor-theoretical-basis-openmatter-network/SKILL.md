---
name: ai-predictor-theoretical-basis-openmatter-network
title: 'AI predictors: theoretical basis (Concern 1)'
description: 'Use when an AI/ML selection tool uses predictors with no clear theoretical or job-analytic rationale — scraped data (resumes, social media, emails, the Internet), voice/facial features, or opaque big-data correlations. Covers the debate over whether predictors need a theoretical basis, proxy-variable risk (e.g., ZIP code for race), and how the presence or absence of adverse impact changes the analysis. Maps to Concern 1 of Tippins, Oswald & McPhail (2021). Triggers: "atheoretical predictors", "scraped data hiring", "why does this variable predict", "proxy variables in AI hiring", "is a correlation enough", "predictor with no rationale".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-predictor-theoretical-basis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI predictors: theoretical basis (Concern 1)

Many technologically enhanced assessments use a wide variety of data **scraped from applications,
resumes, social media, emails, or the Internet**, then run through hundreds of candidate ML
algorithms. The **substantive nature** of the included variables and their **linkages to job
requirements** are often **unknown**.

## The problem

- **No substantive rationale.** Past-employer data scraped from resumes might show that employment at
  Employers A, B, C predicts future performance while D, E, F do not — with no substantive *post hoc*
  explanation, even when all six are in the same business. Theology coursework might "predict" sales
  success. Voice or facial characteristics may have **no obvious theory** linking them to KSAOs or
  performance — justification is "inferred at best and unknown at worst."
- **Proxy variables.** Atheoretical predictors readily encode protected characteristics. In credit
  scoring, **ZIP code is a known proxy for race**; AI using millions of correlations can base
  decisions on such hidden relationships. A predictor can "work" statistically while being a
  construct-irrelevant proxy.
- **Interpretability ≠ relevance.** Even when relationships are interpretable, they may have **little
  practical or conceptual relevance** to the work performed (Braun & Kuljanin, 2015). Big data is
  often massive, messy, and missing.

## The debate (represent both sides honestly)

I-O psychology has long debated whether predictors need a theoretical basis:
- **"Theory matters."** The traditional basis for including a measure is the extent to which it
  reflects a **KSAO necessary to perform the job, as determined by a job analysis.** The *Standards*
  and *Principles* embed this in the very definition of validity: "the degree to which accumulated
  evidence **and theory** support specific interpretations of scores… entailed by the proposed uses"
  (*Principles*, p. 96; *Standards*, p. 225; emphasis added).
- **"Prediction is enough."** Others hold that if scores correlate with a relevant criterion
  (performance, engagement, turnover), they're useful predictors and the rationale is merely "nice to
  know."

The article's resolution: if the **only** purpose is mechanical prediction, studying constructs and
jobs is "merely a response to regulatory requirements." But if the purpose **looks beyond simple
prediction**, understanding the predictive relationship yields **improved measures, broader coverage
of the performance domain, greater generalizability, and assurance** that the system is sensible with
respect to recruiting, training, diverse applicant pools, and **change over time.** Systematic research
also surfaces **additional variables and data sources** that may predict, mediate, or explain work
behavior (Rotolo & Church, 2015).

## How adverse impact changes the calculus

- **Without adverse impact**, even a job-irrelevant predictor would not legally require the "job
  related / business necessity" defense (Title VII) and is not unlawful *per se*. From this view,
  theory can look like an avoidable intellectual exercise.
- **With adverse impact**, job relatedness — which rests on relevance/theory established via job
  analysis — becomes a legal requirement (see `ai-selection-legal-landscape`,
  `ai-job-analysis-and-relevancy`).

So the theoretical-basis question is partly **scientific** (do we want to *understand* prediction?)
and partly **contingent on adverse impact** (do we legally *have to*?). The deeper issue: is selection
research **propelled by science**, prioritizing understanding applicants' suitability through the lens
of **job requirements** — or is it an **atheoretical, purely empirical** activity to maximize predicted
outcomes?

## Questions to ask (from the article)

- Are theoretical justifications necessary in employment testing?
- Is a technologically enhanced measure that predicts organizational outcomes **sufficient**, or does
  one need to understand **why** that prediction occurs?
- Do theoretical justifications **improve practice** in employment testing?
- Do the considerations about theoretical justification **change when there is adverse impact versus
  when there is not?**

## Pitfalls

- Accepting "it predicts, so who cares why" when the use goes beyond one-shot mechanical prediction.
- Missing proxy variables that encode protected characteristics through hidden correlations.
- Assuming interpretability implies job relevance.
- Treating a serendipitous, unreplicated correlation as a justified predictor.

## Checklist

- [ ] Each predictor's substantive link to a job-relevant KSAO examined (or its absence noted)
- [ ] Proxy-variable risk for protected characteristics assessed
- [ ] Purpose clarified: mechanical prediction only, or understanding/coverage/generalizability?
- [ ] Adverse-impact status checked and its legal implications applied
- [ ] Atheoretical/serendipitous relationships flagged for replication before use

## See also

`ai-job-analysis-and-relevancy` · `ai-selection-legal-landscape` · `ai-validity-evidence` ·
`work-analysis` · `criterion-related-validation`
(predictor choice, rationale) · `ai-input-data-and-design-audit`

*Source: Tippins, Oswald & McPhail (2021), Concern: "Lack of a Theoretical Basis for Predictors."*
