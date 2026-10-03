---
name: ai-audit-reporting
title: AI audit reporting
description: 'Use when writing up and releasing the results of a psychological audit of an AI/ML personnel assessment — producing a precise, comprehensive technical report for testing professionals AND a layperson-friendly summary for those the predictions affect, establishing the auditor''s standards and credibility in the report, and deciding on public release. Triggers: "write the AI audit report", "release the bias audit results", "dual-audience audit report", "should we publish the audit", "auditor credibility statement", "communicate algorithm audit findings".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-audit-reporting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, auditing]
---

# AI audit reporting

An audit only creates value if its results are **communicated to the right audiences** and, where the
public interest is at stake, **released.** Reporting is also where the auditor's own **credibility** is
established or lost.

## Produce results in multiple formats (dual-audience)

Present results in **multiple formats to meet the needs of all relevant audiences.** At minimum:

1. **A precise, comprehensive technical report** for review by **testing professionals** — detailed
   enough that another competent professional could evaluate and, ideally, reproduce the audit's
   reasoning. Mirror the structure of a `technical-validation-report`, but
   organized around the **12 components** and the **claims evaluated**.
2. **A layperson-friendly summary** for **whomever the audit's predictions will directly affect**
   (e.g., candidates) — clear, accurate, non-technical, addressing the fairness concerns in the terms
   those audiences actually use (justice/transparency — see `ai-fairness-lenses`).

One format cannot serve both audiences; write both.

## Suggested technical-report structure

- **Claims evaluated** — each developer claim as an explicit statement, classified as
  validity / utility / lack-of-bias (from `ai-audit-planning`).
- **Fairness standard(s)** — the lens(es) and precise definitions used (`ai-fairness-lenses`), stated
  so conclusions are interpretable across disciplines.
- **Findings by component (1–12)** — model (1–6), information & perceptions (7–9), meta (10–12), each
  with evidence, gaps, and access limitations encountered.
- **Auditor credibility statement** (see below).
- **Recommended corrective actions** — to remove or minimize adverse effects, and (for formative
  audits) to improve the model.
- **Limitations** — what could not be evaluated, and why (NDA, missing documentation, small
  intersectional subgroups, etc.).

## Establish credibility *in* the report

**No auditor or audit is automatically credible.** "This system has been audited and is therefore
credible" deserves **skepticism.** So the report must let readers judge the audit itself by disclosing:

- the **measurement standards and definitions of bias/fairness** applied, and that they were applied
  in **due course** across the components;
- the auditor's **type and relationship** to the developer (internal / external / independent);
- the **terms of access and nondisclosure** — including **what could be withheld at the company's
  discretion** (the existence and scope of withholding should itself be disclosed).

Access and documentation vary even within auditor type, so transparency about access is essential to
interpreting the findings.

## Decide on release — default to disclosure in the public interest

**Unless there is a compelling, transparently stated reason not to,** an audit whose results are **in
the public interest should be released.** Organizations may choose otherwise, but doing so **risks the
credibility** of the audit, the company that built the algorithm, and the auditors. Public-facing,
transparent, open audits are especially warranted when a system has **outsized societal impact.**

**Normalize routine auditing.** Treat regular internal *and* external auditing as a **public good**
that raises the probability algorithmic systems in general are valid, valuable, and fair — and that
builds public trust. Formative auditing folded into development, with complete documentation, can
**diminish or even preclude** the need for post-hoc audits.

## Pitfalls

- Shipping only a technical report (affected people can't use it) or only a summary (professionals
  can't evaluate it).
- Implying "audited = trustworthy" without exposing standards and access terms.
- Hiding what was withheld under NDA instead of disclosing that it was withheld.
- Suppressing a public-interest audit, harming everyone's credibility.
- Reporting findings without **actionable corrective recommendations**.

## Checklist

- [ ] Technical report (component- and claim-structured) produced for professionals
- [ ] Layperson summary produced for affected audiences, in their fairness terms
- [ ] Fairness lens(es) and precise standards stated for interpretability
- [ ] Auditor type, relationship, and access/NDA terms disclosed (incl. what was withheld)
- [ ] Findings, gaps, and limitations reported honestly per component
- [ ] Corrective actions recommended (and, if formative, improvement guidance)
- [ ] Release decision made; public-interest default to disclosure applied and any non-release justified

## See also

`ai-audit-planning` (audience & release policy set up front) · `ai-fairness-lenses` ·
all model/stakeholder/meta audit skills · `technical-validation-report`
(structure parallel)

*Source: Landers & Behrend (2023), "Designing an Effective Psychological Audit" — multiple-format
reporting, releasing results in the public interest, normalizing routine auditing, and auditor
credibility.*
