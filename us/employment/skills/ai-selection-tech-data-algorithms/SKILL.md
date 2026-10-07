---
name: ai-selection-tech-data-algorithms
title: 'AI selection: technologies, data, algorithms'
description: 'Use FIRST when evaluating, classifying, or comparing any AI-based or technologically enhanced personnel selection tool — to separate the three independent things it combines: technologies, data, and algorithms (Tippins, Oswald & McPhail, 2021). Establishes that a technology is never "universally valid," that data range from intentional to incidental, and that ML effectiveness depends more on data quality than algorithm choice. Triggers: "evaluate an AI hiring tool", "is this video-interview/game/social-media tool valid", "AI vs ML vs deep learning", "supervised vs unsupervised selection", "big data hiring", "what does this technology actually measure".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-selection-legal-ethical/skills/ai-selection-tech-data-algorithms
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
- legal-ethical
---

# AI selection: technologies, data, algorithms

The starting lens for the whole "scientific, legal, and ethical concerns" framework. Before asking
"is this AI tool any good?", **decompose it into three independent parts** and evaluate each
separately (the "modular approach," Lievens & Sackett, 2017). Conflating them is the root error
behind most overclaiming.

## The three parts

### 1. Technologies — independent of the constructs measured
Examples: online games, video interviews, social media, gamification, VR. Technologies are
**independent from the constructs being measured** and **should not be confused with them** (Arthur &
Villado, 2008; Campbell & Fiske, 1959). Most formats can measure a wide range of constructs, and most
constructs can be assessed by many technologies.

**Consequence (state this in any evaluation):** *a new technology cannot be said to be universally
valid.* "Our video-interview platform is validated" is a category error — validity is a property of
the **inferences about the constructs measured** in a specific use, not of the technology. Demand
evidence about **which job-relevant constructs** are measured, which then informs validity and
fairness.

### 2. Data — a continuum from intentional to incidental
Data vary along a continuum (Oswald, 2020):
- **Intentional** — traditional, controllable responses to a prompt (a test item, an interview
  answer).
- **Incidental** — less intentional/controllable, requiring little or no applicant effort (and
  sometimes little applicant control): social-media posts, facial movements, voice characteristics in
  a video, mouse clicks, response times.

Less obtrusive technologies tend to collect **more incidental data, in massive amounts** (game data =
every click/decision/scenario; video = continuous voice and facial features; "big data" pulled from
resumes, emails, social media). The more incidental the data, the more the concerns about job
relevance, control, consent, and fairness intensify (see `ai-candidate-data-control`).

### 3. Algorithms — AI ⊃ ML ⊃ deep learning
- **AI** — broad term for computer procedures that mimic human decisions/processes/outcomes closely
  enough to appear intelligent.
- **Machine learning (ML)** — subset: the mathematical/statistical procedures underlying these tools.
- **Deep learning** — subset of ML: neural-network-based.
- **Supervised** learning predicts a **criterion** (the criterion "supervises" how predictors are
  used — e.g., predicting supervisory performance ratings); **unsupervised** learning groups
  people/cases into **clusters** with **no criterion** (e.g., applicants like/unlike high performers).

The "learning" happens when algorithms are first exposed to a **training set**; the model is judged on
an independent **test set** (a hold-out sample, k-fold folds, or newly collected data).

## A key claim to carry forward

There are hundreds of ML algorithms, and **different algorithms often make highly similar predictions
with similar overall accuracy** (Domingos, 2012). So in personnel selection, the effectiveness of ML
prediction/clustering is **more likely driven by the availability of high-quality data than by which
ML algorithm is chosen.** Whether the advantages of a large number of predictors offset the
disadvantages of "messy" data must be determined case by case. **Accurate, well-justified predictions
depend on good measurement processes and good data — not on algorithm sophistication.** Don't let a
vendor's algorithm story distract from data-quality and construct questions.

## How to use this skill

1. **Name the three parts** of the tool under review (which technology, what data on the
   intentional–incidental continuum, which algorithm type — supervised/unsupervised).
2. **Reject "the technology is valid"** framing; redirect to *what constructs are measured and is that
   measurement job-relevant, reliable, valid, and fair?*
3. **Locate the data on the continuum** — the more incidental, the more you escalate the
   control/consent/fairness concerns.
4. **Treat algorithm choice as secondary to data quality**; probe the data-generation and
   construct-relevance story.
5. Proceed to the legal frame (`ai-selection-legal-landscape`) and the 11 concerns.

## Pitfalls

- Accepting "this technology is validated" as if validity were a property of the medium.
- Being dazzled by the algorithm while ignoring data quality and construct relevance.
- Missing that incidental data (face, voice, social media) drives the hardest legal/ethical issues.
- Assuming supervised = good and unsupervised = bad (each has distinct evaluation needs).

## Checklist

- [ ] Technology, data type, and algorithm type named and evaluated separately
- [ ] "Universally valid technology" claim rejected; construct/inference framing substituted
- [ ] Data located on the intentional–incidental continuum; control/consent flags raised if incidental
- [ ] Supervised vs. unsupervised identified; training/test-set basis confirmed
- [ ] Data-quality story probed as primary; algorithm choice treated as secondary

## See also

`ai-selection-legal-landscape` · all 11 concern skills · `ai-validity-evidence` ·
`ai-input-data-and-design-audit` (the audit counterpart) ·
`validation-planning`

*Source: Tippins, Oswald & McPhail (2021), "New Forms of Assessment."*
