---
name: counterclaim-crossclaim
title: Counterclaim & Crossclaim
description: Drafts court-ready counterclaims and crossclaims for commercial litigation. Analyzes case documents, classifies compulsory vs. permissive counterclaims, ensures procedural compliance with federal/state rules, and structures causes of action with proper element pleading. Use when a defendant must assert affirmative claims against the plaintiff or crossclaims against co-defendants during pleadings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/counterclaim-crossclaim
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Counterclaim & Crossclaim

Drafts counterclaim and/or crossclaim pleadings asserting a defendant's affirmative claims against the plaintiff or co-defendants, satisfying procedural and substantive pleading requirements.

## Prerequisites

1. **Original complaint** — full text with caption, case number, court, filing date
2. **Case documents** — contracts, correspondence, invoices, emails, evidence
3. **Party information** — names, roles, addresses, relationships (including co-defendants for crossclaims)
4. **Jurisdictional details** — court, rules of civil procedure, local rules, formatting requirements
5. **Legal authority** — statutes, regulations, case law for each cause of action

## Quick Start

1. Extract case identifiers and build a chronological fact timeline from provided documents
2. Classify each potential claim as compulsory or permissive (FRCP 13(a)/(b) or state equivalent)
3. Run the procedural compliance checklist below
4. Assemble the pleading using the document structure
5. Verify all element requirements per the cause of action table

## Workflow

### Step 1: Document Review & Fact Extraction

| Task | Details |
|------|---------|
| Extract identifiers | Court, caption, case number, party designations |
| Build timeline | Formation → performance → breach → damages → plaintiff's wrongful conduct |
| Identify counterclaim targets | Same transaction/occurrence (compulsory) or related matters (permissive) |
| Identify crossclaim targets | Co-defendants liable under contribution, indemnification, or independent theories |
| Catalog damages | Specific amounts, dates, causation chain, continuing damages |

### Step 2: Procedural Compliance

- [ ] Compulsory vs. permissive status (FRCP 13(a)/(b) or state equivalent)
- [ ] Crossclaim from same transaction/occurrence (FRCP 13(g) or state equivalent)
- [ ] Statute of limitations for each cause of action
- [ ] Jurisdictional basis: supplemental for counterclaims; independent or supplemental for crossclaims
- [ ] Local rules: caption format, margins, font, spacing, page limits, e-filing
- [ ] Verification requirement (party vs. attorney)
- [ ] Heightened pleading (FRCP 9(b) for fraud: who, what, when, where, how)

### Step 3: Document Assembly

Structure the pleading with these sections in order:

**Caption** — Mirror original complaint; add Counterclaimant/Counter-Defendant/Cross-Claimant/Cross-Defendant designations; title "COUNTERCLAIM AND CROSSCLAIM" (or separate documents per local rules)

**Introductory Statement** — Filing party, capacity, authorizing rule (FRCP 13/state equivalent), compulsory/permissive nature; for crossclaims: co-defendant targets and legal basis

**Jurisdictional Allegations** — Subject matter jurisdiction, supplemental jurisdiction (28 U.S.C. § 1367) `[VERIFY]`, amount in controversy, venue

**Parties** — Full identification with transaction roles; crossclaim defendants: describe liability-creating relationship

**Factual Allegations** (numbered paragraphs) — Incorporate admissions from complaint by reference; deny/qualify inaccurate allegations; present new facts chronologically; allege damages with specificity (nature, timing, causation, amount)

**Causes of Action** (separately numbered counts) — Format: "COUNT [N]: [Legal Theory] ([Counterclaim/Crossclaim] Against [Party])". Each count: incorporate factual paragraphs by reference, satisfy each element, cite controlling authority, include theory-specific allegations (fault percentage for contribution, indemnification clause for contractual indemnity)

**Prayer for Relief** — Compensatory damages, punitive damages (if authorized), injunctive/declaratory relief, attorney's fees (cite basis), pre/post-judgment interest, catch-all clause; separate subsections for counterclaim vs. crossclaim relief

**Verification** (if required) — Party declaration under penalty of perjury

**Signature Block** — Attorney name, bar number, firm, contact; "Attorney for Defendant/Counterclaimant/Cross-Claimant [Name]"

**Certificate of Service** — All parties/counsel, addresses, method, date

## Cause of Action Elements

| Claim | Required Elements |
|-------|-------------------|
| Breach of Contract | Formation → terms → performance → breach → causation → damages |
| Fraud | False statement → materiality → scienter → reliance → causation → damages (plead with particularity) |
| Contribution | Common liability → proportionate fault → right to apportion |
| Contractual Indemnity | Indemnification clause → triggering event → covered claims → notice |
| Common Law Indemnity | Special relationship → passive vs. active fault → right to shift liability |
| Unjust Enrichment | Benefit conferred → knowledge → inequity of retention |

## Pitfalls & Checks

- **Compulsory counterclaim waiver**: Failure to assert a compulsory counterclaim typically results in waiver — flag all potentially compulsory claims
- **Alternative pleading**: Permitted under FRCP 8(d)(2); label "in the alternative" without conceding primary theory
- **Relation back**: Counterclaims generally relate back to the original filing date for limitations, but verify jurisdiction-specific rules
- **Consistency**: Party names, dates, amounts, and contract references must match source documents exactly
- **Cross-references**: Verify all internal paragraph and exhibit references; ensure exhibit labels match text
- **All citations must be verified** — mark uncertain citations with `[VERIFY]`
- **Do not fabricate facts** — plead only from provided case documents
