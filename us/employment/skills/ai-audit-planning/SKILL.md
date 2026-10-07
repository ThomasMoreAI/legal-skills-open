---
name: ai-audit-planning
title: AI audit planning
description: 'Use when scoping or commissioning a psychological audit of an AI/ML personnel assessment — to define which claims the audit will evaluate (validity, utility, lack of bias), establish the auditor''s stance and credibility (internal / external / independent), decide formative vs. summative timing and the audience, and settle data/documentation access and disclosure terms. Triggers: "audit an AI hiring tool", "plan an algorithm audit", "bias audit scope", "internal vs external vs independent auditor", "formative vs summative audit", "NYC Local Law 144 bias audit", "what claims should the audit test".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-audit-planning
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
- auditing
---

# AI audit planning

Scope the **psychological audit** before doing it. A psychological audit is *an impartially conducted
conceptual and empirical evaluation of claims about psychological characteristics — traits, attitudes,
emotions, behaviors, and other quantities not directly observable — as measured or predicted by
algorithms.* The target characteristics are set by the **developers**, and may not correspond to what
the algorithm ultimately measures or predicts — so the audit must surface that gap.

An audit must be **both conceptually grounded in psychometric theory and empirically tested**, using a
research design appropriate to the claims and interpreted according to modern standards of test
evaluation.

## Step 1 — Identify the claim(s) to evaluate

Audits can evaluate claims of any type, but are most valuable for:
- **Validity** — is measurement/prediction of the targeted characteristic done **consistently and
  accurately**? (Most tractable — broad agreement exists via the psychometrics community and the
  *Standards* / SIOP *Principles*.)
- **Utility** — does the algorithm **provide value** from its implementation? (Even within one
  discipline there's disagreement on how to conceptualize value; frameworks include multiattribute
  utility, ROI, litigation liability, triple-bottom-line. In medicine, value ≈ lives saved/suffering
  reduced.)
- **Lack of bias** — the **most complex**, because the claim can be made through any of the three
  fairness lenses. *Failing to articulate the precise standards of fairness/bias can render the audit
  uninterpretable across disciplines.* Resolve this with `ai-fairness-lenses` first.

Write each developer claim as an explicit, testable statement (e.g., "this algorithm predicts job
performance equally well for all groups using appropriate modeling techniques") — then design to
evaluate it. In the focal example, that exact claim is *questionable and should be audited.*

## Step 2 — Establish auditor stance and credibility

Auditors come in three types; **none is automatically credible**:
- **Internal** — employees of the developing company with psychometric/algorithm expertise.
- **External** — consultants hired *by the developer*.
- **Independent** — brought in externally, often (not exclusively) by a regulator.

It's intuitive to rank these by credibility, but **access to data and documentation varies greatly
even within a type** (NDAs can restrict how deeply anyone can probe). So evaluate **every** auditor —
regardless of source — on: their stated **measurement standards and definitions of bias**, whether
they applied them in due course, and the **terms of access and nondisclosure** (what may be withheld
at the company's discretion should itself be disclosed). *Claims that "an algorithmic system has been
audited and is therefore credible" should be viewed skeptically.*

## Step 3 — Decide purpose & timing: formative vs. summative

- **Formative (during development)** — a particularly valuable purpose is to **guide developers** so
  algorithms can be improved before/while deployed. *Careful adherence to core auditing components at
  all stages of development, plus complete documentation, can diminish or even preclude the need for
  post-hoc auditing.* Normalize **routine internal/external auditing** as a public good.
- **Summative (post-hoc)** — verify developer claims and identify adverse effects after deployment;
  recommend corrective actions to remove/minimize them.

Prefer building auditing **into the development lifecycle**, not just bolting it on afterward.

## Step 4 — Identify the audience and disclosure plan

The audit's purpose is often driven by its **intended audience**. Plan to produce results in
**multiple formats** for all relevant audiences (a precise technical report *and* a layperson-friendly
summary for those whose predictions are affected) — see `ai-audit-reporting`. Decide the **release
policy** up front: in general, unless there's a compelling, transparently stated reason, audits **in
the public interest should be released**; withholding risks the credibility of the audit, the company,
and the auditors.

## Step 5 — Secure access and define the evidentiary base

Confirm what data, documentation, and code you can examine, and record access limits as findings in
their own right. The audit will span the **12 components** across three categories (see the collection
README and Table 1):
- **Models** (1–6) → `ai-input-data-and-design-audit`, `ai-model-development-audit`,
  `ai-model-outputs-audit`
- **Information & perceptions** (7–9) → `ai-claims-and-stakeholder-audit`
- **Meta** (10–12) → `ai-audit-meta-components`

Table 1 is **not exhaustive** — a framework for the most important issues. When a claim can't be fully
evaluated within it, ask additional questions tied to relevant professional standards.

## Note on regulatory "bias audits"

Some laws mandate audits (e.g., NYC Local Law 144 requires an annual "bias audit" of automated
employment decision tools; many bills leave "bias" undefined so the term stays adaptable). A
compliance audit and a scientifically meaningful psychological audit are **not the same** — satisfying
a statute's checklist does not establish validity or lack of bias under Lens 1/3. Scope both
explicitly and don't let one masquerade as the other. (Coordinate with counsel on jurisdictional law.)

## Pitfalls

- Starting empirical work before defining the fairness standard (`ai-fairness-lenses`).
- Treating "it was audited" as proof of fairness.
- Ignoring NDA/access limits instead of reporting them as findings.
- Auditing only post-hoc when formative auditing would have prevented the harm.
- Conflating a regulatory compliance audit with a validity/bias audit.

## Checklist

- [ ] Each developer claim written as an explicit, testable statement
- [ ] Claim type(s) classified (validity / utility / lack of bias)
- [ ] Fairness standard defined via `ai-fairness-lenses`
- [ ] Auditor type, access terms, and NDA limits documented and disclosed
- [ ] Formative vs. summative purpose set; lifecycle integration considered
- [ ] Audience(s) and release policy decided
- [ ] 12-component scope mapped to downstream skills; access gaps noted
- [ ] Regulatory vs. scientific audit scope separated

## See also

`ai-fairness-lenses` (prerequisite) · `ai-audit-reporting` · all model/stakeholder/meta audit skills ·
`validation-planning` · `technical-validation-report`

*Source: Landers & Behrend (2023), "Designing an Effective Psychological Audit"; auditor types &
credibility; formative auditing; "Major Components of an Audit" / Table 1.*
