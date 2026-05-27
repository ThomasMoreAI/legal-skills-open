---
name: claim-construction-order
title: Claim Construction Order
description: Drafts a U.S. federal court Claim Construction Order (Markman order) applying the Phillips v. AWH Corp. intrinsic/extrinsic evidence hierarchy to construe disputed patent claim terms. Use when drafting Markman orders, claim construction memoranda, or disputed-term rulings in U.S. patent litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/claim-construction-order
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Claim Construction Order

Drafts a binding federal court order construing disputed patent claim terms under *Markman v. Westview Instruments, Inc.*, 517 U.S. 370 (1996).

## Prerequisites

- Patent(s) at issue — full text with claims and specification (col./line numbers)
- Prosecution history — file wrapper with paper numbers and pages
- Parties' proposed constructions — joint claim construction chart or equivalent
- Markman record — hearing transcript, expert declarations, briefing
- Case caption — court, division, case number, full party names

## Quick Start

1. Gather intrinsic record (patent, prosecution history, related claims)
2. Map each disputed term to parties' proposed constructions
3. Apply Phillips hierarchy: claim language → specification → prosecution history → extrinsic evidence
4. Draft per-term analysis with pinpoint citations
5. Produce summary table and formal order block

## Order Structure

### Caption & Title
Standard federal court caption. Title: `CLAIM CONSTRUCTION ORDER` or `MEMORANDUM OPINION AND ORDER ON CLAIM CONSTRUCTION`. Follow district local rules.

### Introduction
- Patent number(s) and title(s)
- Procedural posture (post-hearing, post-briefing, or stipulated)
- Number of disputed terms
- Cite *Markman*, 517 U.S. 370; 35 U.S.C. § 112

### Background
- Plain-language technology description
- Accused products/processes (neutral summary)
- Procedural history (complaint, answer, scheduling order, Markman date)

### Legal Standard

| Principle | Rule |
|---|---|
| Governing standard | *Phillips v. AWH Corp.*, 415 F.3d 1303 (Fed. Cir. 2005) (en banc) — ordinary meaning to POSITA at invention |
| Primary source | Claim language in light of specification and prosecution history |
| Specification | "Single best guide"; may supply explicit lexicography |
| Prosecution history | Binding disclaimers and narrowing amendments limit scope |
| Extrinsic evidence | Dictionaries, expert testimony, treatises — secondary; cannot contradict intrinsic record |
| Appellate review | De novo on law; clear error on subsidiary facts — *Teva Pharms. USA, Inc. v. Sandoz, Inc.*, 574 U.S. 318 (2015) |

### Per-Term Construction

For each disputed term:

**Term:** "[exact claim language]" (Claim [X] of U.S. Patent No. [X])
**Plaintiff's Construction:** ...
**Defendant's Construction:** ...

**Intrinsic Evidence:**
- Claim language — usage in asserted and related claims
- Specification — col. [X], ll. [X]–[X]: [quote/paraphrase]
- Prosecution history — Paper No. [X], p. [X]: [disclaimer/amendment]

**Extrinsic Evidence** (only if intrinsic record is ambiguous):
- Source, edition, page

**Court's Construction:** [definitive language]
**Reasoning:** 1–3 sentences supporting the construction.

**Special cases:**
- **Plain meaning** — State explicitly with brief reasoning when no further construction is warranted.
- **Means-plus-function** (§ 112(f)) — Identify function and corresponding specification structure (col./ll.).
- **Indefiniteness** — Flag under *Nautilus, Inc. v. Biosig Instruments, Inc.* [VERIFY]; note without resolving unless record suffices.

### Conclusion
- Summary table: all terms and final constructions
- Note bearing on infringement/validity without prejudging summary judgment
- Confirm constructions bind all subsequent proceedings

### Formal Order Block

> IT IS HEREBY ORDERED that the disputed claim terms of [Patent No(s).] are construed as set forth above. These constructions shall govern all subsequent proceedings in this litigation.
>
> [Optional: parties shall serve amended infringement contentions within __ days.]
>
> SO ORDERED this ___ day of __________, 20___.
>
> [Judge Name]
> United States District Judge

## Pitfalls & Checks

- **Tone** — Authoritative, neutral, analytical. No advocacy or party-favoring language.
- **Pinpoint citations** — Spec: col. and line numbers. Prosecution history: paper number and page. Case law: Bluebook with pinpoints.
- **Internal consistency** — Verify constructions are consistent across related terms; no construction should invalidate claims or read out a disclosed embodiment.
- **Do not** import limitations from preferred embodiments, restate the term as its own construction, or adopt overbroad constructions lacking intrinsic support.
- **Jurisdiction** — U.S. federal patent litigation only. District local rules vary — verify caption format, page limits, required exhibits.
- **[VERIFY]** — All case citations must be verified against current Federal Circuit and Supreme Court precedent before filing.

---

Key changes from the original:

- **Frontmatter**: Removed `tags` (not part of the spec), tightened `description` to be more concise while keeping trigger guidance
- **Added Quick Start**: 5-step workflow giving immediate orientation
- **Flattened structure**: Removed numbered sub-headers (### 1, ### 2...) in favor of named sections — easier to scan
- **Removed code fences** around the per-term template and formal order block — replaced with bold fields and blockquote respectively
- **Removed *Vitronics* from legal standard table** — subsidiary to Phillips and adds token cost without unique value
- **Consolidated Guidelines → Pitfalls & Checks**: Tighter bullets, same substance
- **Reduced ~109 lines → ~93 lines** while preserving all domain-critical content

Want me to retry writing the file, or would you like further adjustments?
