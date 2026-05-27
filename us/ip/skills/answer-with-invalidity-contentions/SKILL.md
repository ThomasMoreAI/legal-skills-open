---
name: answer-with-invalidity-contentions
title: Answer with Invalidity Contentions
description: Drafts a defendant's Answer with Invalidity Contentions responding to a U.S. patent infringement complaint. Covers FRCP 8(b) admissions/denials, affirmative defenses, and PLR 3-3 invalidity contentions with claim charts under 35 U.S.C. §§ 101, 102, 103, 112. Use when representing a defendant in the pleadings phase of federal patent litigation who must respond to an infringement suit and assert prior art, anticipation, obviousness, or § 112 defenses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/answer-with-invalidity-contentions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [drafting, litigation, pleading]
---

# Answer with Invalidity Contentions

Combined answer and Patent Local Rule 3-3 invalidity contentions for a patent defendant — responds to each complaint allegation while building the invalidity record for trial.

## Prerequisites

1. **Complaint** — all numbered paragraphs requiring response
2. **Asserted patent(s)** — specification, claims, and prosecution history
3. **Prior art** — patents, publications, products, or public uses with qualifying dates
4. **Jurisdiction** — district court and applicable local patent rules (PLR 3-3 or equivalent)
5. **Effective filing date** — pre-AIA (before March 16, 2013) vs. AIA § 102 framework
6. **Accused product/method** — for non-infringement admissions and denials

## Output Structure

### 1. Caption and Introduction
- Full party names, civil action number, division
- Title: DEFENDANT'S ANSWER AND INVALIDITY CONTENTIONS
- Jury demand if not previously filed (FRCP 38)
- Opening denial of infringement of any valid, enforceable claim

### 2. Admissions and Denials (FRCP 8(b))

Respond paragraph-by-paragraph mirroring complaint numbering.

| Response | When | Language |
|---|---|---|
| Admit | Verifiable facts (jurisdiction, patent issuance) | "Defendant admits U.S. Patent No. X was issued on [date]." |
| Admit in part / Deny in part | Mixed fact and legal conclusion | "Admits it manufactures [product]; denies infringement of any valid claim." |
| Lack of knowledge (8(b)(5)) | Within plaintiff's peculiar knowledge | "Lacks sufficient knowledge; treated as denial." |
| Deny | False facts and all legal conclusions | "Defendant denies." |

- Address each sub-part of compound paragraphs individually
- Close: "All allegations not expressly admitted are denied." (FRCP 8(b)(6))

### 3. Affirmative Defenses

Number separately. Apply Twombly/Iqbal plausibility with brief factual predicates.

| # | Defense | Notes |
|---|---|---|
| 1 | Non-infringement | Literal and DOE |
| 2 | Invalidity — §§ 101, 102, 103, 112 | Claim charts in § 5; pled in alternative |
| 3 | Inequitable conduct | FRCP 9(b) particularity; reserved pending discovery |
| 4 | Prosecution laches / Equitable estoppel | If prosecution history supports |
| 5 | License / Exhaustion | If authorized sale or course of dealing |
| 6 | Failure to state a claim | Missing claim specificity |
| 7 | Statute of limitations | 35 U.S.C. § 286 (6-year bar) |
| 8 | Unclean hands / Waiver | As facts support |

Defenses not raised may be waived under FRCP 8(c) — err toward inclusion.

### 4. Counterclaims (if applicable)
- DJ of non-infringement (28 U.S.C. § 2201)
- DJ of invalidity
- State jurisdictional basis separately

### 5. Invalidity Contentions

Each contention requires: (a) reference identification, (b) prior art qualification, (c) claim chart.

**Reference header:** Title, authors/inventors, publication date, publisher/assignee, patent or publication number, prior art basis (AIA § 102(a)(1)/(a)(2) or pre-AIA § 102(a)/(b)/(e)/(g)).

#### § 102 — Anticipation

One chart per reference per claim. Map every limitation.

| Claim Limitation | Prior Art Disclosure (col:line or pg:¶) | Analysis |
|---|---|---|
| [Preamble] | [Ref. p. X, ¶ Y] | [Disclosure explanation] |
| [Element 1a] | [Ref. col. 3:12–25] | [Mapping] |

- Patents: presumed enabling
- NPL: address In re Wands enablement factors
- Show anticipation under any reasonable claim construction

#### § 103 — Obviousness

Apply Graham v. John Deere (scope of art, differences, POSITA level, objective indicia). Motivation to combine per KSR v. Teleflex: explicit suggestion, problem-solution, obvious to try, known elements in established functions.

| Claim Limitation | Primary Ref. | Secondary Ref. | Combination Rationale |
|---|---|---|---|
| [Element 1a] | Ref. A, col. 2:10 | — | Taught by A alone |
| [Element 1b] | — | Ref. B, p. 5 | POSITA would combine: [motivation] |

**Rebut secondary considerations:** commercial success (non-claimed features), long-felt need (art already suggested), failure of others (lack of motivation), unexpected results (predictable to POSITA).

#### § 112 Contentions

| Ground | Standard | Identify |
|---|---|---|
| § 112(a) Written description | Inventor possessed full claim scope at filing | Broad terms unsupported by spec |
| § 112(a) Enablement | No undue experimentation (Wands factors) | Claim breadth vs. spec disclosure |
| § 112(b) Indefiniteness | Reasonably certain to POSITA (Nautilus v. Biosig) | Subjective/relative terms, unbounded functional language |
| § 112(f) Means-plus-function | Spec must disclose corresponding structure | Nonce words without disclosed structure |

#### § 101 — Subject Matter Eligibility (if applicable)

Alice/Mayo two-step: (1) directed to abstract idea, law of nature, or natural phenomenon? (2) inventive concept beyond routine/conventional activity?

### 6. Prayer for Relief
- No infringement of any valid, enforceable claim
- All asserted claims invalid under §§ 101, 102, 103, 112
- Patent unenforceable (if inequitable conduct pled)
- Dismissal with prejudice; costs and fees under § 285
- Declaratory relief; such other relief as the Court deems proper

### 7. Signature Block (FRCP 11)
- Attorney name, bar number, firm, address, contact
- Check local rules for corporate verification requirements

## Guidelines

- **Completeness** — Federal Circuit may preclude invalidity theories omitted from initial contentions; PLR 3-3 omissions can be fatal at trial
- **Concurrent production** — prior art references must be produced to plaintiff with service of contentions (unless publicly available)
- **Page limits** — most districts cap at 35–50 pages; check local rules
- **Pre-AIA vs. AIA** — confirm effective filing date; pre-AIA § 102 subsections differ materially from AIA § 102(a)(1)/(a)(2)
- **Internal consistency** — admitted facts in § 2 must not contradict predicates in § 3 or § 5
- **Verify citations** — confirm statute versions, case holdings, and local PLR numbering for the specific district [VERIFY]
- **Scope** — U.S. federal courts only; ITC proceedings use different procedural rules
