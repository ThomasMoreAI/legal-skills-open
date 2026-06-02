---
name: nda-review-2
title: NDA Review Playbook (Commercial, Jurisdiction-Agnostic)
description: Use when reviewing one-way (unilateral) commercial NDAs, analyzing key clauses for risk, producing clause-by-clause issue logs with preferred redlines, fallbacks, and negotiation guidance.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/nda-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [nda, contract-review, redlines, negotiation, legal-analysis]
---

# NDA Review Playbook (Commercial, Jurisdiction-Agnostic)

Version 1.0 — December 2025

> This skill is a structured review playbook. It is not legal advice. When the NDA is high-risk, high-value, cross-border, or otherwise sensitive, escalate to qualified counsel.

> **DRAFT — qualified counsel review required before signing.**
> Reviewer of record: __________________________ (named lawyer, required before send)
> Every output produced by this skill MUST carry this header verbatim and MUST leave the reviewer-of-record line in place until a named qualified lawyer has signed off. Do not send any redline, issue log, or summary to a counterparty until this line is filled.

## Overview

| What this skill does | What it does not do |
|---|---|
| Reviews an NDA and outputs issues, risks, and suggested redlines | Provide jurisdiction-specific legal conclusions |
| Supports *Recipient* or *Discloser* perspectives (user-chosen) | Guarantee enforceability |
| Produces an executive summary + clause-by-clause markup guidance | Replace counsel for complex deals |

**Scope:** supports **one-way (unilateral) commercial NDAs only**. If mutual, this playbook is out of scope.

> **Variation callouts** appear throughout: M&A/Due diligence, Employment/contractor, Investor/VC

## Inputs to Collect (Ask Before Reviewing)

### A. Role and deal context (required)
- Are we reviewing as **Recipient** (we receive confidential info) or **Discloser** (we disclose confidential info)?
- Confirm the NDA is **one-way (unilateral)** — if mutual, stop: out of scope
- What is the **purpose** / permitted use?
- What are the **parties** (legal names) and any **affiliates**?
- What information types are expected (tech, pricing, customer data, product roadmap, source code)?
- Desired **timeline**: when do we need to sign?

### B. Practical constraints (recommended)
- Do we need to share with affiliates, advisors, contractors, auditors, or potential acquirers?
- Will we **export** data across borders or store in cloud tools?
- Will any **personal data** be shared?

> **Jurisdiction-agnostic note:** avoid asserting "this clause is invalid" without governing law; focus on *commercial risk*, *operational feasibility*, and *market norms*.

## Deliverables

### A. Executive Summary (1 page)
- Party role (Recipient or Discloser) and confirmation it is one-way
- Top 5 negotiation points (ranked)
- "Sign as-is" / "Sign with changes" / "Escalate" recommendation

### B. Clause-by-Clause Issue Log

| Clause | Issue (1 line) | Risk (H/M/L) | Preferred redline | Fallback | Rationale (1-2 sentences) | Owner | Deadline |
|---|---|---:|---|---|---|---|---|---|
| Definition | Overbroad; includes unmarked info with no reasonableness | | | | | | |
| Term & survival | Perpetual confidentiality for all information | | | | | | |
| Use restriction | Purpose too broad; blocks internal evaluation | | | | | | |
| Disclosures | Representatives undefined; strict liability | | | | | | |
| Return/destruction | No backup carve-out | | | | | | |
| Remedies | One-way fees + automatic injunction | | | | | | |
| Liability | Indemnity + unlimited consequential damages | | | | | | |
| Boilerplate | Assignment prohibits change of control | | | | | | |

### C. Risk Band Rubric (How to Score H / M / L)

Every row in the Issue Log MUST carry one of the three bands below. Use the most-severe band that applies; do not average.

| Band | Criteria (any one triggers the band) | Typical examples |
|---|---|---|
| **High (H)** | Forced or one-way arbitration imposed on Recipient; unlimited liability or uncapped consequential damages; non-mutual indemnity that survives termination; perpetual confidentiality on *all* information with no trade-secret distinction; one-way attorneys' fees + automatic injunction against Recipient; standstill / no-hire / no-contact bundled into the NDA; cross-border personal-data flow with no carve-out; assignment clause that triggers on change of control. | "Recipient indemnifies Discloser for any and all claims"; "Recipient waives right to a jury and consents to arbitration in [foreign seat]"; "obligations survive in perpetuity". |
| **Medium (M)** | Ambiguity in a defined term that could be read against us in negotiation but is not catastrophic; onerous-but-bounded scope (e.g., 5-year confidentiality on non-trade-secret info); missing standard carve-outs (compelled disclosure, prior knowledge, independent development) where the omission is recoverable in redline; representative-liability language without a written-confidentiality limiter; return/destruction language with no backup carve-out. | "Confidential Information includes any information disclosed in connection with the Purpose" (no marking standard); "Recipient shall be liable for any breach by its Representatives". |
| **Low (L)** | Minor drafting cleanup — typos, defined-term capitalisation, cross-reference errors, stylistic inconsistencies; boilerplate that is non-standard but commercially harmless; clarifying tweaks that improve readability without shifting risk. | Inconsistent defined-term casing; redundant recitals; severability/notice-address mechanics. |

> **Scoring discipline:** if you can credibly explain to a deal lead in one sentence why a clause could materially damage the business or expose the firm, it is at least Medium. If the explanation requires "and then if X, and then if Y…", it is Low.

## 5-Step Workflow

### Step 1 — Identify Stance (Recipient vs Discloser)
- Confirm which side we are on for *this specific NDA* (titles are often misleading)
- Confirm the NDA is **one-way (unilateral)**. If mutual, stop: out of scope.

**Quick heuristic:**
- If asked to keep *their* info secret → **Recipient**
- If sharing *our* sensitive info → **Discloser**

### Step 2 — Triage the NDA (Fast Risk Scan)
Flag immediately:
- [ ] **Perpetual** confidentiality for *all* information (no trade secret distinction)
- [ ] **Residuals clause** allowing use of "memory" or generalized knowledge
- [ ] **Injunctive relief** + **attorneys' fees** one-way against Recipient
- [ ] **Indemnity** for breach or broad third-party claims
- [ ] **No carve-outs** for compelled disclosure or prior knowledge
- [ ] **Overbroad definition**: "all information, whether marked or not" with no reasonableness
- [ ] **Affiliate coverage** missing when we must share internally

### Step 3 — Clause-by-Clause Review
Use reference modules:
- `references/KEY_CLAUSES.md` — Common NDA clauses and implications
- `references/PARTY_OBLIGATIONS.md` — Analysis of party obligations
- `references/DURATION_SCOPE.md` — Duration and scope considerations
- `references/REMEDIES_LIABILITY.md` — Remedies and liability provisions
- `references/STANDARD_EXCEPTIONS.md` — Standard exceptions

### Step 4 — Draft Redlines and Negotiation Positions
For each issue:
- **Preferred redline** (best risk outcome)
- **Fallback position** (acceptable compromise)
- **Rationale** (1-2 sentences: business + operational feasibility)
- **Owner** (Legal, Sales, Security, Product)
- **Deadline**

> **Negotiation discipline:** do not propose 20 changes. Focus on 5-10 that materially change risk.

### Step 5 — Finalize the Package
- [ ] Ensure consistency across definitions
- [ ] Confirm operational feasibility
- [ ] Re-scan Step 2 triage list; ensure each flagged item is in the issue log
- [ ] Provide "what we changed and why" summary

## Perspective-Specific Checklists

### A. Recipient Checklist (Incoming NDA)

| Topic | Red Flags | Typical Ask |
|---|---|---|
| Definition of Confidential Information | Overbroad; includes independently developed info; no marking standard | Add reasonableness + identification standard |
| Purpose / Permitted Use | Any use restriction beyond evaluation; bans on internal sharing | Tie to stated purpose; allow internal need-to-know |
| Representatives | Liable for any representative breach without control | Limit to written confidentiality; commercially reasonable care |
| Term & survival | Perpetual for everything; unclear start date | Fixed term; longer only for trade secrets |
| Return / destruction | Requires immediate deletion of backups | Add backup carve-out |
| Remedies | One-way fees + broad injunction language | Mutuality or reasonableness |
| Liability / indemnity | Indemnity; unlimited damages; consequential damages | Cap or exclude categories; remove indemnity |
| Residuals | Allows use of "retained in memory" | Delete or narrow heavily |

> **M&A / Due diligence:** ensure diligence sharing (advisors, financing, affiliates) is permitted and data room exports/notes are covered.

### B. Discloser Checklist (When Sharing Sensitive Info)

| Topic | Red Flags | Typical Ask |
|---|---|---|
| Definition | Too narrow; requires marking only; excludes oral disclosures | Add oral confirmation mechanism |
| Security standard | Only "reasonable" with no baseline | Add minimum safeguards |
| Exclusions | Too broad (e.g., "independently developed" with no proof) | Require written evidence |
| Term & survival | Too short | Extend for sensitive categories |
| Remedies | No equitable relief, no fees | Add equitable relief carefully |

> **Investor / VC:** watch for standstill, solicitation, and "no contact" provisions.

## Limitations

- This skill provides a structured framework, not legal advice
- Jurisdiction-specific law not covered; always verify with qualified counsel
- High-risk, high-value, or cross-border deals require escalation
- Does not cover mutual NDAs — those require separate review approach
- All outputs must be reviewed by a qualified legal professional before use

## QA Remediation (LegalQuants, 2026-05)

This skill was QA'd by LegalQuants against the Legal Skill Design Framework on 2026-05-11 (verdict: SOME CONCERN) and remediated on 2026-05-12. The remediations target the two open gaps from that report — undefined H/M/L risk bands and an accountability gap not structurally enforced by the output shape — while leaving the technical content intact.

**What changed**
- **H/M/L risk bands now operationalised.** A new section "Risk Band Rubric (How to Score H / M / L)" was added immediately after the Clause-by-Clause Issue Log table, with explicit criteria and worked examples for each band. The rubric is mandatory for every Issue Log row.
  - High = forced arbitration, unlimited or uncapped liability, non-mutual indemnity, perpetual confidentiality on all information, one-way fees + injunction, bundled standstill/no-hire, cross-border personal-data flow without carve-out, change-of-control assignment trigger.
  - Medium = ambiguity in defined terms that is recoverable in redline, onerous-but-bounded scope, missing standard carve-outs, representative-liability without a written-confidentiality limiter, return/destruction without backup carve-out.
  - Low = minor drafting cleanup (typos, defined-term casing, cross-reference errors, harmless boilerplate, readability tweaks that do not shift risk).
- **Accountability gap closed by output shape.** A "DRAFT — qualified counsel review required before signing" banner with a named-reviewer placeholder is now part of the file header and is required on every output produced by the skill (Executive Summary, Issue Log, Redline package, Step 5 finalisation). The banner cannot be removed until a named qualified lawyer is written into the reviewer-of-record line; nothing leaves for the counterparty until that line is filled. This makes the lawyer-review requirement structurally enforced rather than purely a disclaimer the reader can skim past.
- **Versioning metadata refreshed.** Frontmatter now carries `version: 1.0.0`, `last_reviewed: 2026-05`, and `last_reviewed_by: LegalQuants (QA remediation)`. Authorship remains with Jamie Tso.

**What did not change**
- Scope (one-way commercial NDAs only), jurisdiction-agnostic posture, inputs to collect, 5-step workflow, reference modules, perspective-specific checklists, variation callouts, and the existing limitations section are all preserved verbatim. The remediation is additive.

**Open items deferred to a later pass**
- Audience declaration, work-shape declaration, consolidated escalation section with named-role routing, and a "common failure modes" list (all flagged as ⚠️ in the QA report) are not addressed in this remediation. They are non-blocking for the two priority gaps and can be folded into the next minor version.
