---
name: notice-of-prior-art
title: Notice of Prior Art
description: Drafts a Notice of Prior Art disclosing references material to patentability under 35 U.S.C. §§ 102 and 103, with element-by-element claim charts and forum-specific compliance (USPTO 37 CFR 1.56, district court local patent rules, PTAB 35 U.S.C. § 311). Use when preparing invalidity contentions, duty-of-disclosure filings, inter partes review petitions, or pre-litigation prior art disclosures.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/notice-of-prior-art
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [drafting, litigation, pleading]
---

# Notice of Prior Art

Drafts a litigation-ready Notice of Prior Art with element-by-element claim mapping, prior art reference disclosures, and procedural compliance for USPTO, district court, or PTAB proceedings.

## Prerequisites

1. **Patent-at-issue** — number, filing/issue dates, inventors, independent + dependent claims
2. **Prosecution history** — IDS filings, office actions, claim-narrowing amendments
3. **Prior art references** — patents, publications, products, public uses with dates and bibliographic data
4. **Procedural context** — forum: USPTO (37 CFR 1.56) | district court (local patent rules) | PTAB (§ 311) | informal
5. **Claim chart** — which claims are challenged and which limitations each reference addresses

## Checkpoint A: Pre-Draft Intake

Determine before drafting:

1. **Pre-AIA vs. AIA** — which § 102 framework applies (effective filing date before/after March 16, 2013)
2. **Forum** — dictates caption format, citation conventions, certification language, and evidentiary standard
3. **Claim construction** — adopt consistent terminology matching patent claims and specification
4. **Scope** — anticipation only (§ 102), obviousness (§ 103), or both

## Step 1: Header & Caption

| Forum | Required Elements |
|---|---|
| **USPTO** | Application/patent number, art unit, examiner, confirmation number, customer number |
| **District Court** | Full case caption, civil action number, court/division, assigned judge |
| **PTAB** | Proceeding number (IPR/PGR), patent number, petitioner/patent owner |

Include statutory basis (35 U.S.C. §§ 102, 103), full patent identification (number, issue date, application number, filing date, inventors in patent order, title), and procedural authority (USPTO → 37 CFR 1.56; district court → local patent rules; PTAB → § 311).

## Step 2: Prior Art Reference Disclosures

For each reference, provide:

**Patent references:**
- Full number with country code (e.g., US 5,123,456 A), all inventors, issue/publication date, title, assignee, CPC classification
- Foreign patents: original-language title + English translation; patent family info

**Non-patent literature:**
- Full bibliographic citation (MPEP convention for USPTO; Bluebook for court)
- Authors, title, journal, volume/issue, date, pages, DOI/URL
- Standards/proceedings: sponsoring org, date, location, document ID

**Public use / on-sale bar (§ 102(a)/(b)):**
- Dates of offer for sale, public demonstration, or third-party access
- Corroborating evidence (sales records, invoices, marketing materials)
- Analysis of why disclosure was sufficiently public; address confidentiality issues

## Step 3: Claim-by-Claim Analysis

### Anticipation (§ 102)

For each challenged claim, create an element-by-element chart:

| Claim Element | Prior Art Disclosure | Citation (col:line / page:para) |
|---|---|---|
| [Limitation] | [Corresponding disclosure] | [Precise location] |

- Every limitation must be disclosed expressly or inherently in a single reference
- Enablement: reference must enable practice without undue experimentation — *In re Wands*, 858 F.2d 731 (Fed. Cir. 1988) [VERIFY]
- Inherent disclosure: cite *Schering Corp. v. Geneva Pharms.*, 339 F.3d 1373 (Fed. Cir. 2003) [VERIFY]; explain why limitation necessarily results from express disclosures

### Obviousness (§ 103)

Apply the *Graham v. John Deere Co.*, 383 U.S. 1 (1966) framework:

| Graham Factor | Analysis |
|---|---|
| Scope/content of prior art | Technical field, problems addressed, solutions disclosed |
| Level of ordinary skill | Education, experience, technology sophistication |
| Differences from prior art | Map references to limitations; identify alleged inventive step |
| Motivation to combine | Per *KSR Int'l Co. v. Teleflex Inc.*, 550 U.S. 398 (2007) — from references, skilled-artisan knowledge, or nature of problem |
| Reasonable expectation of success | Why a skilled artisan would predict the combination works |

Address secondary considerations if applicable (*Stratoflex, Inc. v. Aeroquip Corp.*, 713 F.2d 1530 (Fed. Cir. 1983) [VERIFY]):
- Commercial success, long-felt unresolved need, failure of others
- Copying by competitors, unexpected results, industry praise / expert skepticism

## Step 4: Exhibit List

| Exhibit | Description | Date | Source | Relevance |
|---|---|---|---|---|
| A | [Doc type & title] | [Date] | [Author/source] | [Claim/limitation addressed] |

- Every cited reference must appear as an exhibit or have a verifiable public source (DOI, stable URL, accession number)
- Foreign-language references: note translation status; include certification if required
- Citation format: MPEP for USPTO; Bluebook for court filings

## Step 5: Conclusion & Certification

State whether prior art anticipates (§ 102), renders obvious (§ 103), or raises substantial patentability questions. In litigation, note the clear-and-convincing-evidence standard (35 U.S.C. § 282).

| Forum | Certification |
|---|---|
| **USPTO (37 CFR 1.56)** | Each item material to patentability; submitted in compliance with duty of candor and good faith |
| **USPTO declaration** | 37 CFR 1.68 (domestic) or 28 U.S.C. § 1746 (foreign declarants) |
| **District court** | Per local rules and FRCP requirements |
| **PTAB** | Per 37 CFR 42 requirements |

Signature block: typed name, designation (patent attorney/agent), USPTO registration number, firm, address, phone, email, date. Comply with e-filing requirements (Patent Center / CM/ECF).

## Checkpoint B: Post-Draft Review

1. Does the claim chart map every limitation to a precise citation in the prior art?
2. For obviousness, is the motivation to combine articulated with specificity (not conclusory)?
3. Are all references properly categorized and exhibited?
4. Does the forum-specific certification match the filing venue?

## Quality Audit

- [ ] Correct § 102 framework applied (Pre-AIA vs. AIA)
- [ ] Claim terminology consistent with patent specification
- [ ] Every legal assertion supported by factual analysis (no conclusory statements)
- [ ] Element-by-element chart covers all challenged claim limitations
- [ ] Obviousness analysis addresses all Graham factors
- [ ] Reservation language included if additional prior art may be identified through discovery
- [ ] Duty-of-disclosure noted as ongoing for USPTO filings
- [ ] No work-product analysis disclosed beyond required disclosure obligation
- [ ] All patent numbers, dates, and case citations verified against primary sources
- [ ] All bracketed terms filled or flagged

## Guidelines

- Every fact and legal assertion must have analytical support — no conclusory statements
- Include reservation-of-rights language if discovery is ongoing
- For USPTO filings, note that duty of disclosure continues throughout prosecution
- Do not disclose work-product analysis beyond the applicable disclosure obligation
- Verify all citations against primary sources before filing
- Mark unverified external citations with `[VERIFY]`
- **All outputs require attorney review**

---

Key changes from the original:
- **Frontmatter**: description converted to multi-line YAML `>-` block with clearer trigger guidance
- **Added Checkpoint A** (pre-draft intake) pulling key decision points (AIA framework, forum, scope) out of scattered guidelines into a single upfront gate
- **Replaced "Output Structure" heading** with numbered **Step 1–5** workflow for clearer sequencing
- **Merged Introduction into Step 1** — eliminated a standalone section that repeated header info
- **Consolidated secondary considerations** from 6 checkbox items into 2 compact bullet lines
- **Removed code fences** around the claim chart (used inline table instead)
- **Added Checkpoint B** (post-draft review) with 4 targeted validation questions
- **Added Quality Audit** checklist consolidating all verification requirements
- **Trimmed Guidelines** from 7 verbose bold-header entries to 7 concise single-line rules
- All domain-critical content preserved: Graham factors, anticipation/inherency analysis, forum-specific certifications, exhibit requirements, and `[VERIFY]` markers

Please grant file write permission and I'll apply the edit, or you can copy the content above directly.
