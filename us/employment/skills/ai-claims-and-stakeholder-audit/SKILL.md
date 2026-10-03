---
name: ai-claims-and-stakeholder-audit
title: AI claims & stakeholder audit (Components 7–9)
description: 'Use when auditing how an AI/ML personnel assessment is described and how it affects people — Components 7-9 (information & perceptions) of the Landers & Behrend (2023) framework. Covers first-party developer claims (do they honestly and transparently follow from the audit evidence?), second-party effects on those assessed (candidate reactions, justice, false positives vs. false negatives, what is communicated), and third-party understanding (employment-law experts, regulators, community, public). Triggers: "developer marketing claims vs evidence", "candidate reactions to AI hiring", "applicant fairness perceptions", "false positive vs false negative impact", "what do regulators/public think", "transparency of AI hiring claims".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-claims-and-stakeholder-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, auditing]
---

# AI claims & stakeholder audit (Components 7–9)

The model can be technically sound and still be **mis-described** or **harmful in use.** This category
shifts from the model's internals to how information about it is **presented, understood, and
experienced** by three parties. It leans heavily on the **individual-attitudes (justice) lens** — see
`ai-fairness-lenses`.

## Component 7 — First-party interpretation (developer claims)

**What it is:** the **messaging** the algorithm developer puts out about the model.

**Questions to ask:** Does **all** messaging from the developer **logically, honestly, and
transparently** follow from answers developed elsewhere in the audit?

**Apply it (focal example):** Does the developer **claim the model predicts job performance**? **What
evidence in the audit forms the basis** of that claim? Are **important details left out**?

**Audit emphases:**
- Cross-check every public/marketing/sales claim against the **model-audit findings** (Components
  1–6). A claim unsupported by the evidence — or that omits material caveats (range restriction,
  k-fold-only validation, untested intersectional subgroups) — is a finding.
- This is **informational justice** in action: transparency about *what is assessed* and *what is done
  with the data* shapes how fair the system is perceived to be.

## Component 8 — Second-party effects (those assessed)

**What it is:** impact on the people **directly affected** by the algorithm's use (candidates).

**Questions to ask:** **Who** is directly affected, and how have their **outcomes and reactions** been
assessed? What is the **relative impact of acting on false positives versus false negatives** on
second parties?

**Apply it (focal example):** How do **non-selected applicants react** to learning the algorithm did
not score them high enough to be selected? **What information is communicated** to them, and how do
they **evaluate** that information?

**Audit emphases — use justice theory (Lens 1):**
- **Procedural justice** rules the developer may be violating: opportunity to perform, job-relatedness/
  face validity (do candidates believe facial expressions predict performance?), **reconsideration/
  appeal** (algorithmic decisions that can't be appealed), **two-way communication** (AI replacing
  human interaction), and **propriety** (some find AI decisions morally inappropriate).
- **Distributive justice:** which rule (equality/need/equity) do affected people apply to the outcome?
- **Interactional justice:** interpersonal (respect/dignity) and informational (adequate explanation,
  e.g., an explanatory video before data collection).
- **False positives vs. false negatives are not symmetric for second parties.** A false negative
  (a qualified candidate wrongly screened out) harms the individual; weigh it explicitly against false
  positives rather than optimizing a single accuracy number. Tie this to the error-cost reasoning in
  `selection-decisions-and-scoring`.

## Component 9 — Third-party understanding (outside observers)

**What it is:** how **outside observers** perceive and evaluate the system.

**Questions to ask:** How have **perceptions and evaluation by outside observers** been assessed and
incorporated? Have **outside regulatory groups and community organizations** been consulted?

**Apply it (focal example):** How do **experts in employment law** view the documentation and
performance of the algorithm? How does the **public** view this use of algorithms?

**Audit emphases:**
- Solicit **employment-law** review (differential prediction, disparate impact, differential
  treatment — Lens 2) and **community/regulatory** input, rather than assuming internal sign-off
  suffices.
- Public trust is part of the value proposition; transparent, outward-facing evaluation raises it
  (and is a stated benefit of normalizing audits).

## Pitfalls

- Auditing the model but never checking the **claims made about it** against the evidence.
- Optimizing overall accuracy while ignoring the **asymmetric cost of false negatives** to candidates.
- Treating candidate reactions as PR rather than **justice** evidence relevant to fairness.
- No appeal/reconsideration path; no two-way communication.
- Assuming legality without consulting employment-law experts or affected communities.

## Checklist

- [ ] Every developer claim cross-checked against Component 1–6 findings; omissions flagged
- [ ] Informational transparency (what is measured / what is done with data) assessed
- [ ] Directly affected parties identified; reactions/outcomes assessed
- [ ] Procedural, distributive, and interactional justice rules evaluated
- [ ] False-positive vs. false-negative impacts weighed for second parties
- [ ] What is communicated to non-selected candidates reviewed (incl. appeal/reconsideration)
- [ ] Employment-law expert and community/regulatory perspectives obtained
- [ ] Public-perception considerations documented

## See also

`ai-fairness-lenses` (justice; legal lens) · `ai-audit-reporting` (communicating to these audiences) ·
`ai-audit-meta-components` · `fairness-and-bias-analysis` ·
`selection-decisions-and-scoring` (error costs) ·
`administration-documentation` (candidate communications, feedback)

*Source: Landers & Behrend (2023), Table 1 (Components 7–9, "Components relating to information and
perceptions").*
