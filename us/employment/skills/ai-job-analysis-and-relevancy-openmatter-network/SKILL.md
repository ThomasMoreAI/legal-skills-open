---
name: ai-job-analysis-and-relevancy-openmatter-network
title: AI job analysis & job relevancy (Concerns 2–3)
description: 'Use when checking whether an AI/ML selection tool is grounded in an adequate analysis of work and is demonstrably job-related — Concerns 2-3 of Tippins, Oswald & McPhail (2021). Covers whether a job analysis is necessary (even with a strong criterion-related relationship), acceptable forms and rigor, O*NET and competency-model limits, collecting task importance ratings, SME-judgment agreement, and the legal meaning of job relatedness. Triggers: "does the AI tool need a job analysis", "is this algorithm job-related", "competency model vs job analysis for AI", "O*NET as job analysis", "job relevancy of scraped predictors", "Guardians job analysis".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-job-analysis-and-relevancy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI job analysis & job relevancy (Concerns 2–3)

Professional standards, legal guidelines, and case law all require selection systems to be **tied to
job requirements**, established through an **analysis of work** (Morgeson et al., 2020). For AI tools
built from convenient or scraped data, this is frequently the weakest link. (The article treats these
two concerns together because requirements for a job analysis are hard to separate from job
relevancy.)

This skill is the AI-specific framing; for *how* to conduct a work analysis, use
`work-analysis`.

## Why job analysis matters here

- Traditionally, job analysis is the basis for identifying the **KSAOs** required and the appropriate
  variables for selection, and for **developing criteria / defining the performance domain.**
- *Uniform Guidelines* §14B(2) requires a **review of job information** for criterion-related validity;
  the *Principles* state job analysis defines appropriate **predictors** and establishes the
  **relevance of the criteria.**
- **In practice, many test users skip or abbreviate job analysis** — assuming, say, that all sales
  jobs are alike and a generic "sales test" transfers. Without a job analysis you cannot know (a) that
  the test's purported skills are the ones predicting in **this** organization, or (b) that the skills
  the job requires match those the test measures. Predictors and criteria may then be **wrong,
  inadequate, or unfair.**

### Is job analysis still needed when predictor–criterion relationships are strong?
A live question: if a predictor set empirically predicts a criterion (locally or meta-analytically),
does job relatedness still need a job analysis? **Risks of saying "no":** a **spurious** relationship
can masquerade as job relatedness. *Example:* "leadership experience" correlates with managerial
performance, but **gender also correlates** with both (men more often given leadership opportunities)
— gender should be irrelevant, yet the relationship may be found. Like **ZIP-code-as-race** in credit
scoring, AI's millions of correlations can rest decisions on hidden, illegitimate relationships.
Without a job analysis to identify, define, and measure the KSAOs, predictors and criteria "may be
used that are wrong, inadequate, or unfair."

## Forms and rigor of job analysis

- Legal/professional guidelines allow **many acceptable methods** but are **silent on how
  comprehensive** the analysis must be. *Guardians* (2d Cir. 1980) holds job analysis should be
  **systematic and accurate regardless of methodology.**
- **Competency models:** many test publishers apply a **standard competency model across
  organizations**, with loose ties to the actual tasks/behaviors of incumbents. Competencies may be
  specific KSAOs, broad KSAOs, or even organizational **aspirations** ("Demonstrates amazing customer
  service at all times"). Generic competency lists (e.g., Hunt, 1996) used for all jobs/levels for
  efficiency may not be **complete** relative to a specific job. Test publishers often omit a critical
  competency the test doesn't measure.
- **O*NET** is a useful **starting point** for tasks/KSAOs but **should not substitute for a complete
  job analysis** (it has limitations given how the data were collected).
- **Collecting task information** (frequency/importance ratings): UGESP requires measures of task
  importance/criticality and documents them as Essential (§15B(3)). This step is **often skipped**,
  yet collecting task ratings **orients SMEs to actual job requirements and away from stereotypes** —
  and reliability/validity of KSAO judgments rises when KSAOs are **concrete and tied to specific
  tasks** (Morgeson et al., 2020, p. 375).
- **SME judgment quality:** interrater agreement (ICC) **assumes SMEs are similarly knowledgeable or
  trained** — an assumption **rarely evaluated** in practice.

## Job relevancy / job relatedness (the legal anchor)

- **Job relevancy** = the core features of a job (KSAOs, work behaviors, environment), determined by
  job analysis. U.S. law **requires job relatedness** for tests with adverse impact (Title VII
  disparate impact → "job related for the position and consistent with business necessity").
- The *Uniform Guidelines* establish the explicit requirement to conduct a job analysis **whenever
  undertaking a criterion-related validation study** (§3.14(A)).
- The *Principles* allow several routes to job relatedness: appropriate **criterion-related validity
  coefficients**, the **job relevance of the content**, or the **construct measured** (*Principles*,
  p. 90). Validity is a function of evidence supporting interpretation **for specific purposes.**
- **The AI gap:** technologically enhanced tools may **predict outcomes** ("job related" in a
  statistical sense) yet **not be based in a job analysis** — leaving job relevance unestablished and
  legal defensibility weak.

## Questions to ask (from the article)

- Is a job analysis necessary if predictors and criteria are strongly related in a criterion-related
  study?
- Is a job analysis necessary to justify an operational performance measure (e.g., KPIs) used as the
  validation criterion?
- To what extent is a **competency model** an adequate substitute for a job analysis?
- Is it important to have a **complete** list of competencies?
- How much **rigor** in the job-analysis methodology is necessary to establish job requirements?
- Is **O*NET** an acceptable source for a complete list of KSAOs?
- Is it important to collect **task information** (e.g., frequency and importance ratings)?
- If a job analysis is not conducted, can job relevancy be demonstrated for the assessments or the
  criteria? Is predictor–criterion correlation **alone** sufficient to establish job relatedness under
  the *Uniform Guidelines*?

## Pitfalls

- Deploying a generic "sales test" (or vendor competency model) without analyzing the local job.
- Treating a strong predictor–criterion correlation as proof of job relatedness (spurious/proxy risk).
- Using O*NET or an aspirational competency list as a complete job analysis.
- Skipping task importance ratings, then over-relying on stereotype-tinged SME KSAO judgments.
- Never checking whether SMEs are comparably knowledgeable before trusting interrater agreement.

## Checklist

- [ ] A systematic, accurate job analysis underlies predictors and criteria (or its absence is flagged)
- [ ] Spurious/proxy relationships ruled out via job-analytic grounding
- [ ] Competency model's rigor and completeness for the specific job evaluated
- [ ] O*NET used only as a starting point, not a substitute
- [ ] Task importance/criticality information collected and documented
- [ ] SME comparability assessed before relying on agreement statistics
- [ ] Job-relatedness route (criterion / content / construct) identified for legal defensibility

## See also

`work-analysis` (how-to) · `ai-predictor-theoretical-basis` ·
`ai-validity-evidence` · `ai-selection-legal-landscape` ·
`ai-input-data-and-design-audit`

*Source: Tippins, Oswald & McPhail (2021), Concerns: "Job Analysis" and "Job Relevancy."*
