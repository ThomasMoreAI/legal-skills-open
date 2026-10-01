---
name: ai-candidate-data-control-openmatter-network
title: AI candidate data control (Concern 8)
description: 'Use when an AI/ML selection tool uses data the candidate does not control or did not knowingly provide — scraped social-media/Internet data, or incidental data like facial micro-expressions, voice, and appearance — Concern 8 of Tippins, Oswald & McPhail (2021). Covers the loss of applicant control, job-irrelevance and "is it fair," reputation-scrubbing services and adverse impact, the absence of a clear legal/ethical rule, informed consent (Illinois AIVI Act), and the range of policy approaches. Triggers: "scraped social media hiring", "data outside applicant control", "facial appearance in hiring", "is it fair to use this data", "informed consent for AI hiring data", "online reputation scrubbing".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-candidate-data-control
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, legal-ethical]
---

# AI candidate data control (Concern 8)

Traditionally, applicants control to a large degree **what they present** to an employer — effort on
ability tests, answers on personality/SJT measures, demeanor in interviews, resume and application
content. Using information **outside** those sources is not new ("word of mouth," references,
background and credit checks). What's new with AI is the **scale and the loss of applicant control.**

## What changed

- **Scraped data outside the applicant's control.** Employers can search the Internet and large
  databases for evidence of "inappropriate behavior" (poor judgment), but such data often contain
  **irrelevant information** — demographics (Zhang et al., 2020), political affiliation (Roth et al.,
  2020). Applicants have **increasingly less control** over the type and relevance of personal data
  organizations extract from social media. They may try **impression management** via profiles
  (Schroeder & Cavanaugh, 2018), but in some cases they **did not post the information themselves**, it
  was **substantially altered**, or it was **posted without intent** to be shared. Online information is
  often **suspect, dated, or lacking context.**
- **Reputation-scrubbing services and adverse impact.** Companies that help manage online reputations
  are **not free**; to the extent their availability/affordability varies by **race/ethnicity or other
  demographics**, these "scrubbing" services may **contribute to adverse impact** that is **difficult to
  detect.**
- **Incidental data that candidates cannot alter.** Images, video, audio, facial micro-expressions, and
  voice purport to convey job-relevant emotions — but **physical appearance beyond grooming is outside
  most people's control** (skin color, voice timbre, basic speech patterns, the features of one's face).
  This raises **special problems** for people who look or speak differently due to **cultural
  differences (minorities, immigrants), physical differences (disabilities, diseases, injuries),
  gender, and age.**

## The crux: "Is it fair?"

Irrelevant variables may well predict performance; the essential question is **"Is it fair?"** There is
**no law or guideline requiring an employer to use only data presented by the candidate** (except in
the realm of **privacy statutes**), and **no specific ethical standard** requiring it either. Yet there
is a **moral dilemma.** The article lays out a spectrum of approaches:
- **One extreme — press ahead.** Use this kind of data, on the rationale that applicants have **never**
  controlled everything an employer sees and uses.
- **Other extreme — use no data beyond the candidate's control.** This would entail careful review even
  of traditional forms like **biodata.**
- **A moderate approach — informed consent.** Being legislated in laws like the **Illinois AI Video
  Interview Act** (`ai-selection-legal-landscape`): require **informed consent before** an employer
  bases a selection decision on data beyond the applicant's control.

## Questions to ask (from the article)

- **Is it fair** to use data that are **outside the control** of an applicant?
- **Should** employers seek out data on the Internet at all?
- Would there be **legal issues** associated with **not** seeking information about some behaviors (e.g.,
  poor judgment, behavioral deviancy, CWBs)?
- How long should applicants' **past failures or mistakes** affect their future job prospects, and what
  mistakes should be considered (criminal history, online behavior, **early-life behavior**)?

## Pitfalls

- Using scraped data without confirming relevance, recency, accuracy, or that the candidate authored it.
- Ignoring that paid reputation-scrubbing can create undetectable adverse impact.
- Scoring appearance/voice features that candidates cannot change (disability/cultural/age fairness).
- Assuming "no law against it" settles the **fairness/ethics** question (it doesn't).
- Treating implied consent as covering data the candidate doesn't know is being collected (see
  `ai-selection-ethics`).

## Checklist

- [ ] Data sources classified by applicant control (provided vs. scraped vs. incidental/uncontrollable)
- [ ] Job relevance of out-of-control data interrogated ("Is it fair?")
- [ ] Accuracy/recency/authorship/context of scraped data verified
- [ ] Adverse-impact risk from scrubbing-service disparities considered
- [ ] Appearance/voice/disability/cultural/age fairness evaluated
- [ ] Consent approach chosen along the spectrum; statutory consent (e.g., Illinois) satisfied
- [ ] Privacy-statute compliance confirmed with counsel

## See also

`ai-selection-ethics` (informed consent) · `ai-applicant-reactions-and-communications` ·
`ai-selection-legal-landscape` (Illinois AIVI Act, privacy)
· `ai-reliability` (appearance/disability) · `candidate-accommodations`
(disability, linguistic/cultural) · `ai-claims-and-stakeholder-audit`

*Source: Tippins, Oswald & McPhail (2021), Concern: "Control Over the Data Presented to an Employer."*
