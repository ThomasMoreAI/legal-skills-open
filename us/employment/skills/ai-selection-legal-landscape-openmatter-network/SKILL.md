---
name: ai-selection-legal-landscape-openmatter-network
title: 'AI selection: legal landscape'
description: 'Use when assessing the legal and regulatory exposure of an AI-based /  technologically enhanced personnel selection tool (primarily U.S., with global notes). Covers the Uniform Guidelines on Employee Selection Procedures, Title VII disparate impact and the job-relatedness/business-necessity defense, the OFCCP''s 2019 position on AI, the Guardians content-validation case, the Illinois AI Video Interview Act and other state laws, and why "no adverse impact" does not equal "valid." Triggers: "is this AI hiring tool legal", "Uniform Guidelines and AI", "disparate impact algorithm", "OFCCP AI", "Illinois AI Video Interview Act / BIPA", "do we need to validate the algorithm", "adverse impact vs validity".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-selection-legal-landscape
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI selection: legal landscape

The legal/regulatory frame an AI selection tool must survive. This is **decidedly U.S.-centric**
because the legal requirements are, but **many of the concerns apply globally** (validity as business
justification exists everywhere). **Not legal advice — consult qualified counsel.**

> Core principle: AI/ML selection tools are **"tests"** under the law. *Uniform Guidelines* Section
> 2B defines a test as **any selection procedure used as the basis for an employment decision** —
> which sweeps in games, video interviews, facial/voice scoring, resume screeners, and big-data
> models. They are governed by the same rules as any other test.

## The federal framework (U.S.)

### Uniform Guidelines on Employee Selection Procedures (EEOC, CSC, DoL, DoJ, 1978)
- Broadened "test" to **any selection procedure** used for an employment decision (Sec. 2B; the 1979
  Q&A further expanded it to application forms, interviews, training/probationary performance, etc.).
- Adopted **1978**, with very few changes and **none since the 1981 Q&A** (the OFCCP's 2019 FAQs are
  **not** part of the Guidelines). Theoretically and practically dated — yet they remain the
  **controlling administrative rules** for Title VII litigation and are deeply embedded in case law.
  They **must still be considered** when evaluating any procedure that results in **adverse impact**.
- Require a **job analysis** whenever conducting a criterion-related validation study, and specify the
  documentation expected in technical reports.

### Title VII, Civil Rights Act of 1964 — disparate impact
A disparate-impact violation is established when a complaining party shows a practice causes
**disparate (adverse) impact** on the basis of race, color, religion, sex, or national origin **and**
the respondent **fails to demonstrate the practice is job related for the position and consistent with
business necessity** (Sec. 2000e-2(k)(1)(A)(i)). So:
- **Adverse impact** shifts the burden to the employer to show **job relatedness / business
  necessity** — which in practice means **validity evidence** (see `ai-validity-evidence`).
- **Differential treatment** (treating class members differently — e.g., awarding bonus points to a
  group, or modeling class membership) is a distinct, separate legal problem.

### OFCCP (2019 FAQ)
"Irrespective of the level of technical sophistication involved, OFCCP analyzes **all** selection
devices for adverse impact." If a contractor's AI-based procedure has adverse impact, the contractor
**must validate it using an appropriate validation strategy.** AI buys no exemption.

### Search for less-adverse alternatives
U.S. employers are obligated to consider **alternative selection procedures with substantially equal
or greater validity and less adverse impact** (Uniform Guidelines §3B). This makes **comparative
data** important — an AI tool should be compared against alternatives, including traditional measures
whose meta-analytic validity provides a **reasonable baseline the AI must beat**.

### Case law — job analysis in content validation
*Guardians Association of NYC Police Dept. v. Civil Service Commission of NYC* (2d Cir. 1980) and
related cases establish that **job analysis is central** in content-validation disputes and **should
be systematic and accurate regardless of the methodology** used. (See `ai-job-analysis-and-relevancy`.)

## State law (proliferating)
- **Illinois Artificial Intelligence Video Interview Act** (passed May 29, 2019; effective Jan. 1,
  2020): employers using AI to evaluate video interviews must **(a) notify applicants in writing** that
  AI may be used and what characteristics it evaluates, **(b) provide information** on how the
  technology works and what characteristics it uses, and **(c) obtain written consent** before the
  interview. They may **not share the video** except with those with expertise to evaluate it, and
  must **destroy the video within 30 days** of a request.
- Other state legislatures are weighing in; **legislation and policy on the nature, transparency, and
  privacy of applicant data will continue to emerge and evolve.** Re-check current jurisdictional law.

## Professional (not legal) — the APA Ethics Code
SIOP members subscribe to the **APA Ethics Code**, which governs the treatment of candidates and what
psychologists say about tools — an obligation **independent of, and additional to, the law**. See
`ai-selection-ethics`.

## The "no adverse impact ≠ valid" rule

A crucial argument to deploy: **reduced or no adverse impact does not, by itself, justify use.** A
**random-number generator** can winnow a large applicant pool quickly **without** producing adverse
impact — yet it lacks the **reliability, validity, and utility** an organization needs to identify
capable candidates and achieve an acceptable return. It is **incumbent on developers (and users) to
provide sufficient evidence that AI selection tools meet these requirements** — not merely to show
they don't create adverse impact. Vendors often tout "reduced adverse impact" while the empirical
validity evidence is unavailable, making the relevant comparison impossible.

## Pitfalls

- Treating an AI tool as exempt from test-validation law because it's "just an algorithm."
- Relying on "no/low adverse impact" as if it established validity or utility.
- Forgetting the duty to consider less-adverse, equally valid alternatives.
- Overlooking state-specific notice/consent/destruction requirements (e.g., Illinois).
- Assuming the OFCCP 2019 FAQs are part of the Uniform Guidelines (they are not).
- Conflating disparate impact with disparate (differential) treatment.

## Checklist

- [ ] Tool classified as a "test" under UGESP §2B
- [ ] Adverse-impact exposure assessed; validity-defense obligation understood
- [ ] Job-relatedness/business-necessity evidence path identified (→ `ai-validity-evidence`)
- [ ] Less-adverse-alternative comparison considered (§3B)
- [ ] Job-analysis adequacy checked (Guardians) (→ `ai-job-analysis-and-relevancy`)
- [ ] State-law notice/consent/destruction requirements checked (e.g., Illinois AIVI Act)
- [ ] "No adverse impact ≠ valid" argument applied to vendor claims
- [ ] APA Ethics Code obligations noted (→ `ai-selection-ethics`)
- [ ] Counsel engaged for jurisdiction-specific questions

## See also

`ai-validity-evidence` · `ai-job-analysis-and-relevancy` · `ai-candidate-data-control` (consent) ·
`ai-selection-ethics` · `fairness-and-bias-analysis` ·
`criterion-related-validation` (alternatives, validation)

*Source: Tippins, Oswald & McPhail (2021), "New Forms of Assessment" (legal framing), "Disadvantages,"
"Purpose," and the legal threads woven through the concerns.*
