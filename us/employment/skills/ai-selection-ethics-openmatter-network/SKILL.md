---
name: ai-selection-ethics-openmatter-network
title: AI selection ethics (Concern 11)
description: 'Use when evaluating the professional-ethics obligations around an AI/ML personnel selection tool under the APA Ethics Code — Concern 11 of Tippins, Oswald & McPhail (2021). Covers Ethics Code Section 9 (9.01 Bases for Assessments, 9.02 Use of Assessments, 9.03 Informed Consent), the difference in consent standards for researchers (8.05) vs. those employing tools, and how reliability, validity, and fairness are intertwined with ethical duties. Triggers: "APA ethics AI hiring", "is it ethical to use this assessment", "informed consent assessment", "ethics code section 9", "psychologist responsibility AI selection", "implied consent job applicant".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-selection-ethics
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI selection ethics (Concern 11)

SIOP members are bound by the **APA Ethical Principles of Psychologists and Code of Conduct**. A review
of **Section 9 (Assessment)** surfaces several ethical concerns for newer forms of assessment. The
central message: **reliability, validity, and fairness are not separate from ethics — they are
intertwined with it.** It is the **professional responsibility** of I-O psychologists to require
information about reliability, validity, and fairness when deciding whether a selection system —
technology-enhanced or otherwise — can be used to make inferences about job performance.

## The governing standards (APA Ethics Code, Section 9)

- **9.01 Bases for Assessments.** Psychologists base the opinions in their recommendations, reports, and
  evaluative statements on **information and techniques sufficient to substantiate their findings.**
  → An opinion that an AI tool selects good employees must rest on **sufficient evidence**, not vendor
  assertion.
- **9.02 Use of Assessments.** Psychologists use instruments **whose validity and reliability have been
  established for the population tested.** When validity/reliability have **not** been established, they
  **describe the strengths and limitations** of results and interpretation.
  → If an AI tool lacks established reliability/validity for your applicant population, that must be
  disclosed and its limitations described — not glossed.
- **9.03 Informed Consent.** Psychologists **obtain informed consent** for assessments (per Standard
  3.10), **except** when (1) testing is **mandated by law or governmental regulation**; (2) consent is
  **implied** because testing is a **routine** educational, institutional, or organizational activity
  (e.g., when participants **voluntarily apply for a job**); or (3) the purpose is to evaluate
  **decisional capacity.** Informed consent includes an explanation of the **nature and purpose** of the
  assessment, **fees, third-party involvement, limits of confidentiality,** and a **sufficient
  opportunity to ask questions** and receive answers.

## Where AI strains these standards

- **Implied consent may not reach incidental data.** Implied consent covers **routine** testing when
  someone applies for a job — but it is **not clear** that implied consent extends to **data the
  candidate may not be aware is being obtained** (scraped social media, facial/voice analysis). This
  links directly to `ai-candidate-data-control`.
- **Different consent standards for builders vs. users.** The informed-consent standards differ for
  **researchers developing** selection tools (Ethics Code **8.05**) versus those **employing** them
  (Guzzo et al., 2015; Dekas & McCune, 2015). Know which role you're in.
- **Sufficient evidence to substantiate findings.** If an ML algorithm infers that applicants will have
  a higher likelihood of good performance, **what is the quality and strength of the evidence** behind
  that inference (9.01)? Establishing reliability and validity is an **ethical**, not merely technical,
  obligation, because the recommendation made from the test score must be supported.

## The integrating point

I-O psychologists must **determine whether ethical standards are being met or can be met** when working
with AI tools. That means they must:
- establish (or require evidence of) **validity and reliability** of the instruments used for selection
  (9.02), and
- have the **evidence to support the recommendation** made from the test score (9.01), and
- ensure **appropriate consent** (9.03), recognizing the gaps around uncontrolled/unaware data.

In short, the ethical duty operationalizes the scientific concerns: you cannot ethically deploy a tool
whose reliability, validity, and fairness you cannot vouch for.

## Questions to ask

- Is there **sufficient evidence** to substantiate the findings/recommendations the tool produces
  (9.01)?
- Have **validity and reliability been established for the population tested** — and if not, are
  strengths/limitations clearly described (9.02)?
- Is **informed consent** properly obtained or appropriately implied — and does any implied consent
  actually cover **data the candidate is unaware of** (9.03)?
- Are you acting as a **developer (8.05)** or a **user** of the tool, and have you applied the right
  consent standard?

## Pitfalls

- Relying on vendor claims rather than evidence "sufficient to substantiate findings" (9.01).
- Using a tool without reliability/validity established for **your** applicant population, and not
  disclosing the limitation (9.02).
- Stretching "implied consent" to cover scraped or incidental data the candidate never knew about
  (9.03).
- Confusing the consent obligations of tool **developers** with those of **employers/users**.
- Treating ethics as separate from psychometrics rather than as their enforcement.

## Checklist

- [ ] Evidence is sufficient to substantiate the tool's recommendations (9.01)
- [ ] Reliability/validity established for the tested population, or limitations described (9.02)
- [ ] Informed consent obtained or properly implied; coverage of unaware/uncontrolled data examined (9.03)
- [ ] Developer (8.05) vs. user consent role identified and correct standard applied
- [ ] Reliability/validity/fairness evidence required as an ethical precondition for deployment

## See also

`ai-candidate-data-control` (consent for uncontrolled data) · `ai-validity-evidence` · `ai-reliability`
· `ai-selection-legal-landscape` (APA Code as professional, not legal) ·
`ai-fairness-lenses` (legal/ethical/moral lens) ·
`ai-audit-meta-components` (respect / ethical-standards conformance)

*Source: Tippins, Oswald & McPhail (2021), Concern: "Ethics."*
