---
name: customs-trade-law
title: Customs Trade Law Skill
description: HTS classification, CROSS ruling research, CIT/CAFC case mapping for US trade law. Analyzes products, finds applicable rulings, and traces legal precedent.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/customs-trade-law
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [trade-law, hts-classification, customs, compliance, import]
---

# Customs Trade Law Skill

## When to Use

- Classifying a product under the Harmonized Tariff Schedule (HTS)
- Researching CBP ruling history for similar products
- Resolving conflicts between HQ and NY rulings
- Mapping CIT/CAFC case law to classification questions
- Building compliance analysis for import transactions

## Audience and Work Shape

Audience: Licensed customs brokers, trade-compliance counsel, or in-house import managers working under a licensed reviewer. Not for self-service use by importers without compliance review, and not for unsupervised drafting of binding ruling requests, Customs Form 28/29 responses, or § 177 submissions.

Work shape:
- **Module 1 (HTS Classification)** — Accretive Judgment. Output is a ranked-candidates worksheet with GRI reasoning and exposed assumptions, handed back to a licensed broker or trade attorney who signs the binding classification call.
- **Module 2 (CROSS Ruling Research)** — Pattern-Matched Review. Output is a list of cited rulings with authority level and current status, reviewed by counsel before reliance.
- **Module 3 (CIT/CAFC Case Mapping)** — Accretive Judgment. Output is mapped precedent with risk framing, reviewed before being cited in any opinion or ruling request.

## Scope and Legal Use

This skill provides legal *support*, not legal advice or a binding classification. A `candidate classification` output is a draft worksheet for the reviewer — not a primary classification, not a § 177 ruling request, and not a basis for entering merchandise.

Three legal failure modes are addressed structurally:

**Advice vs. support.** Outputs are draft worksheets, not finished classification opinions. The skill does not produce a single "primary" HTS number on its own authority. The reviewer-of-record (a licensed customs broker or trade attorney) makes the classification call and signs the deliverable. Misclassification carries civil and potentially criminal exposure under 19 U.S.C. § 1592 (negligence, gross negligence, fraud); the named reviewer — not the skill — bears that responsibility.

**Privilege.** When the skill is used inside counsel's work, outputs should be marked `DRAFT — ATTORNEY WORK PRODUCT / PRIVILEGED` and treated as such. The skill is silent on who the client is in any given matter; the user must determine whether the analysis is being prepared at the direction of counsel for the purpose of giving legal advice, and route storage/circulation accordingly. Do not share draft outputs outside the privileged circle without explicit instruction.

**Accountability.** Every classification worksheet requires a named human reviewer (broker license number or bar number where applicable) before it is acted upon, cited in a § 177 ruling request, or used to support an entry. The skill does not sign off and does not certify a classification as correct.

## How It Works

### Module 1: HTS Classification

**Input:** Product description with **all of**: name, components/composition, principal use, country of origin, and (where relevant) the importer's intended use.

If composition, country of origin, or principal use is missing, halt and ask. Do not infer composition from the product name.

**Process:**
1. Identify candidate headings (4-digit level)
2. Apply General Rules of Interpretation (GRI 1-6)
3. Apply Additional U.S. Rules of Interpretation
4. Determine subheading (6-digit level typically)
5. Surface ranked candidates with GRI reasoning and assumptions
6. Assign confidence band (see Confidence Bands below)

**Output (candidate classification worksheet — for licensed customs counsel or licensed broker review):**
- **Ranked candidate classifications** with HTS numbers (not a single "primary" call)
- For each candidate: GRI path, applicable Section/Chapter Notes, and reasons it is or is not the correct heading
- Explicit assumptions (composition, use, country of origin, end user) made in the analysis
- Confidence band (High / Medium / Low) per the definitions below
- Flagged controversies, GRI 3 essential-character disputes, and unresolved issues
- Reviewer signoff line: name, license/bar number, date, and reviewer's classification call
- Privilege/draft marking on the deliverable

### Module 2: CROSS Ruling Research

**Input:** Product description or existing candidate classification.

**Process:**
1. Search CBP's CROSS database
2. Evaluate HQ vs. NY authority (HQ overrides NY)
3. Trace revocation chains (identify any ruling later revoked or modified)
4. Assess evidence quality: verified published rulings vs. identifications vs. internal advice
5. Verify status as of run date — flag if CROSS retrieval was incomplete

**Output:**
- List of applicable rulings with full citation
- Authority level (HQ, NY, Chicago, etc.)
- Current status (current / revoked / modified / pending revocation)
- Side-by-side of ruling facts vs. user's product
- Flag where retrieval may be incomplete or status could not be confirmed

### Module 3: CIT/CAFC Case Mapping

**Input:** HTS candidate(s) or product description.

**Process:**
1. Find relevant judicial decisions
2. Extract holdings (note: where the skill retrieves slip-opinion text, the source and retrieval date must be cited)
3. Map precedent to classification risk
4. Identify cases that support or undermine each candidate classification

**Output:**
- List of relevant cases with citations and retrieval source
- Key holdings relevant to the classification question
- Risk framing based on case-law strength (not a litigation prediction)

## Confidence Bands

Each candidate classification carries an explicit band:

- **High** — On-point CBP HQ ruling on materially identical merchandise, no contrary CIT/CAFC precedent, no revocation history, no GRI 3 essential-character dispute. Reviewer still signs.
- **Medium** — NY ruling only, or HQ ruling on an analogous (not identical) product, or any composition/use ambiguity that affects the GRI path. Reviewer attention required; consider whether a § 177 ruling request is preferable.
- **Low / Review** — No on-point CROSS ruling, conflicting HQ/NY rulings, GRI 3(b) essential-character dispute, any special-provision question (Chapter 98 / Chapter 99 / Section 301 / antidumping / countervailing / FTA qualification), or any indication of a revoked authority. **The skill does not output a recommended classification at Low confidence** — it routes to Escalation.

## Out of Scope

This skill addresses HTS classification, CROSS ruling research, and CIT/CAFC case mapping for US imports. It does **not** cover and should not be relied on for:

- Country-of-origin determinations and substantial-transformation analysis
- Section 232 / Section 301 tariff exposure and exclusion requests
- Antidumping (AD) and countervailing duty (CVD) scope and rate determinations
- FTA qualification (USMCA, GSP-successor regimes, KORUS, etc.)
- Customs valuation (transaction value, related-party, assists, royalties)
- Duty drawback claims
- Forced-labor / UFLPA admissibility
- Export controls (EAR, ITAR, OFAC sanctions, FTR)
- Drafting or filing binding ruling requests under 19 CFR § 177
- Responding to CBP Forms 28 / 29 or CF-29 notices of action
- Penalty mitigation under 19 U.S.C. § 1592 or prior-disclosure submissions

Route these to qualified counsel or the appropriate specialist regime.

## Escalation

The skill **stops and routes to a named reviewer or licensed counsel** — rather than producing a recommended classification — in any of the following cases:

1. **GRI 3 essential-character dispute** — any composite good or set where GRI 3(a) or 3(b) does not resolve cleanly.
2. **Conflicting authority** — HQ and NY rulings reach different results, or there is a CIT/CAFC decision pulling against the most analogous CROSS ruling.
3. **No on-point CROSS hit** — no published ruling on materially identical merchandise.
4. **Special-provision question** — any Chapter 98 / Chapter 99 / Section 301 / Section 232 / AD/CVD / FTA preference / forced-labor question.
5. **Revocation or modification flag** — the most analogous ruling has been revoked, modified, or is the subject of a pending revocation notice in the Customs Bulletin.
6. **Incomplete retrieval** — CROSS or CIT/CAFC search did not return reliable, dated results.
7. **§ 1592 exposure indicated** — facts suggest possible prior misclassification, recurring entries on a wrong line, or any pattern that may implicate § 1592 negligence/gross negligence/fraud analysis. Route to trade counsel for privileged review; consider whether a prior disclosure is in play.
8. **Low confidence band per the Confidence Bands section.**

Escalation produces a structured handoff (not a classification): the question presented, the rulings and cases retrieved, the assumptions made, what is missing, and a recommended next step (§ 177 ruling request, internal compliance review, or trade-counsel referral). The named reviewer — licensed customs broker, licensed customs attorney, or in-house trade-compliance counsel — owns the call from that point forward.

## Limitations

- This skill is a research assistant, not a substitute for legal advice
- Classification determinations require physical examination of merchandise in some cases
- CROSS rulings are persuasive to CBP, not precedential, and may be revoked or modified — status must be verified as of the run date
- Case-law analysis should be verified against the current HTS edition and applicable statute
- The skill does not access CROSS, the Customs Bulletin, or CIT/CAFC dockets through a declared MCP or allowlisted retrieval tool; users must verify cited rulings and decisions independently and treat any quoted text as requiring source confirmation

## QA Remediation (LegalQuants, 2026-05)

LegalQuants applied a QA-remediation pass to this skill in May 2026, following the Legal Skill Design Framework used by the Legal Builder Hub. Original substantive authorship and attribution remain with M. Onur Kafkas; LegalQuants's contribution is structural.

Changes made in this pass:

1. **Frontmatter** — added `version`, `last_reviewed`, and `last_reviewed_by` fields. Author attribution preserved.
2. **Audience and Work Shape** — added explicit audience (licensed customs brokers / trade-compliance counsel / supervised in-house import managers) and labelled the work shape of each module (Accretive Judgment for Modules 1 and 3; Pattern-Matched Review for Module 2).
3. **Scope and Legal Use** — added a three-mode legal-failure section covering advice-vs-support, privilege handling (draft work-product marking), and accountability (named reviewer with broker license / bar number). Added explicit reference to **19 U.S.C. § 1592** civil and criminal penalty exposure for misclassification and assigned that exposure to the reviewer-of-record, not the skill.
4. **HTS Classification output reframed** — Module 1 no longer outputs a "Primary classification with HTS number." It now outputs a **ranked candidates worksheet** labelled "candidate classification — for licensed customs counsel review," with GRI reasoning per candidate, exposed assumptions, confidence band, and a reviewer signoff line.
5. **Confidence Bands** — added explicit High / Medium / Low definitions, and made Low confidence trigger Escalation rather than a classification output.
6. **Out of Scope** — enumerated adjacent regimes that this skill does not cover (origin, Section 232/301, AD/CVD, FTA qualification, valuation, drawback, UFLPA, export controls, § 177 ruling drafting, CF-28/29 responses, § 1592 penalty mitigation).
7. **Escalation** — added a named-reviewer-handoff section covering eight specific triggers including GRI 3 disputes, conflicting authority, no on-point CROSS hit, special-provision questions, revocation flags, incomplete retrieval, and any indication of **§ 1592 exposure** (with explicit prior-disclosure framing routed to trade counsel).
8. **Input requirements** — Module 1 now halts and asks if composition, country of origin, or principal use is missing, rather than inferring composition from the product name.
9. **Retrieval-mechanism caveat** — added a Limitations note that CROSS and CIT/CAFC retrieval is not declared through a specific MCP/allowlist and that users must verify cited rulings and decisions independently.

Technical substance — the GRI methodology, the HQ/NY authority hierarchy, the revocation-chain logic, the CIT/CAFC mapping approach — is unchanged from the original. The remediation is structural: it restructures outputs as draft worksheets handed back to a licensed reviewer, defines confidence bands, enumerates escalation triggers, and addresses § 1592 exposure, privilege handling, and accountability that the original SKILL.md left to a one-line disclaimer.
