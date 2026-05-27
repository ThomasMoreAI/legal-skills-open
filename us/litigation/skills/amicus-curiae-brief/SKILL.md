---
name: amicus-curiae-brief
title: Amicus Curiae Brief
description: Drafts filing-ready U.S. amicus curiae briefs with rule-anchored compliance, additive thesis selection, record-safe fact handling, and verified authority control. Trigger when asked to draft an amicus or friend-of-the-court brief, prepare FRAP 29/32 or Supreme Court Rule 37 amicus filings, draft consent/leave or disclosure language, or handle amicus procedural requirements at any stage.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/amicus-curiae-brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [brief, drafting]
---

# Amicus Curiae Brief

Produces a procedurally compliant, substantively additive amicus brief. The amicus must deliver a perspective the parties cannot — restating party arguments risks striking, sanctions, or credibility loss.

## Quick Start

1. Gather intake (forum, stage, party briefs, amicus profile, disclosure facts)
2. Build compliance map from governing rules
3. Select an additive thesis that fills a gap in party arguments
4. Draft brief with record-safe fact handling
5. Verify all authorities and run quality audit

## Intake (Mandatory)

Collect before drafting (skip only if user says "use defaults"):

- **Forum/stage** — court, caption, docket number, cert vs. merits, panel or en banc
- **Deadlines** — docket schedule, amicus-specific orders
- **Party briefs** — at minimum the supported party's principal brief
- **Record anchors** — record cites used by parties for adjudicative facts
- **Amicus profile** — entity, mission, expertise, relationship to parties
- **Position** — supports petitioner/respondent/neither; requested disposition
- **Consent/leave** — consent status, whether motion for leave is needed
- **Disclosure facts** — authorship and funding (Rule 29(a)(4)(E) / Rule 37.6)
- **Formatting** — word/page limits, font, cover color, copy counts
- **Sources** — primary sources for legislative facts or empirical claims

**Defaults if unspecified:** federal circuit FRAP 29; standard amicus word limits; hybrid expertise/systemic-consequences thesis.

## Step 1: Compliance Map

| Field | Details |
|---|---|
| Rule Set | FRAP 29/32, Supreme Court Rule 37, or state rule |
| Deadline | Date/time and trigger brief |
| Word/Page Limit | Rule section and numeric limit |
| Required Sections | Interest, disclosures, summary, argument, conclusion |
| Certificates | Compliance, service, corporate disclosure if required |
| Filing Format | ECF/PDF, paper copies, cover color `[VERIFY]` |
| Local Deviations | Circuit/state additions |
| Signature | Admitted counsel; Supreme Court Bar if applicable |

## Step 2: Select Additive Thesis

Extract party argument chain; identify the gap. Choose one primary thesis:

- **Expertise translation** — technical/industry knowledge parties lack
- **Systemic consequences** — how ruling affects non-parties and broader systems
- **Doctrinal harmonization** — fit with related precedent or statutory schemes
- **Historical/structural framing** — legislative history, original understanding, institutional design

State thesis in one sentence for the Summary of Argument.

### Record-Safety Rules

| Fact Type | Use | Support Required |
|---|---|---|
| Adjudicative | Only as in record | Record cite from briefs/record |
| Legislative | Context only | Primary sources, stable cites |
| Predictive | Cautious language | Empirical or governmental sources |

## Step 3: Draft Brief

Structure:

1. Cover Page
2. Table of Contents / Table of Authorities
3. Disclosure Statement (FRAP 29(a)(4)(E) or Rule 37.6)
4. Statement of Interest of Amicus Curiae
5. Summary of Argument
6. Argument — conclusion-style headings; each section ties to verified source or record cite; address counterarguments; translate technical content for judges
7. Conclusion
8. Certificate of Compliance / Certificate of Service / Signature Block

Use bracketed placeholders (`[VERIFY]`, `[X words]`, `[date]`) for any unconfirmed detail.

### Disclosure and Certificates (Verbatim Required)

- **Disclosure statement** (FRAP 29(a)(4)(E), Supreme Court Rule 37.6, or forum equivalent): copy current rule language verbatim after verification; do not paraphrase required rule text.
- **Certificate of Compliance**: include rule citation, exact word count, statement of typeface/style compliance if required, signer name, date, and signature line. Use verbatim rule language where mandated.
- **Certificate of Service**: include rule citation, service method(s), service date, recipient list (or filing-system service statement if permitted), declarant name, date, and signature line. Use verbatim rule language where mandated.

```text
Certificate of Compliance
Rule: [FRAP 32(g)(1) / controlling forum rule]
Word count: [X words]
Required rule text: [PASTE VERBATIM TEXT REQUIRED BY CONTROLLING RULE]
Date: [YYYY-MM-DD]
Signature: [Name /s/]

Certificate of Service
Rule: [FRAP 25(d) / FRAP 25(c) / controlling forum rule]
Service method: [ECF / email / mail / personal service]
Service date: [YYYY-MM-DD]
Served on: [Names or category of recipients as required]
Required rule text: [PASTE VERBATIM TEXT REQUIRED BY CONTROLLING RULE]
Date: [YYYY-MM-DD]
Signature: [Name /s/]
```

## Step 4: Deliverables

Prefix every output with:

1. **Assumptions** — forum, posture, consent status, thesis, governing rules
2. **Open Items** — missing briefs, unconfirmed rules, outstanding disclosure facts

## Post-Draft Check (Mandatory)

Ask after delivering initial draft:

1. Does the thesis add a perspective the party briefs do not?
2. Are disclosure facts (authorship, funding) confirmed?
3. Should additional authorities or empirical sources be added?
4. Is the tone correct for this court and amicus role?

## Quality Audit

Verify before finalizing:

- [ ] Rule text confirmed against current forum rules
- [ ] Consent/leave requirements satisfied
- [ ] Disclosure statement matches rule text and confirmed facts
- [ ] Thesis is additive — no duplication of party arguments
- [ ] All adjudicative facts tied to record cites
- [ ] All legislative facts sourced and context-framed
- [ ] Unverified authorities flagged `[VERIFY]`
- [ ] TOC/TOA accurate; word count within limits
- [ ] Assumptions and open items listed prominently

## Critical Rules

- Never restate party arguments — thesis must be additive
- Never introduce adjudicative facts outside the record
- Never fabricate citations, rule text, or empirical data — flag `[VERIFY]` if unconfirmed
- Do not assume FRAP applies — confirm state appellate rules when applicable
- Supreme Court briefs: Rule 37.6 disclosures + Supreme Court Bar signature `[VERIFY]`
- State rules (CA 8.200(c), NY 500.23) must be independently confirmed `[VERIFY]`
- All output requires attorney review before filing
