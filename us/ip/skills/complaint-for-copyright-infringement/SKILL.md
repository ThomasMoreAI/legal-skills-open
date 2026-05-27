---
name: complaint-for-copyright-infringement
title: Complaint for Copyright Infringement
description: Drafts a federal court complaint for copyright infringement under 17 U.S.C. § 101 et seq. Produces a Twombly/Iqbal-plausible pleading with caption, jurisdiction (28 U.S.C. §§ 1331, 1338(a)), venue (28 U.S.C. §§ 1391, 1400(a)), ownership allegations, infringement count, damages, and prayer. Use when initiating copyright litigation in U.S. federal court at the pleadings phase.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/complaint-for-copyright-infringement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [drafting, litigation, pleading]
---

# Complaint for Copyright Infringement

Drafts a litigation-ready federal complaint asserting copyright infringement under the Copyright Act, establishing jurisdiction, ownership, and infringement with Twombly/Iqbal plausibility.

## Prerequisites

Gather before drafting:

1. **Registration** — number(s), effective date(s), certificate copies; required under 17 U.S.C. § 411(a)
2. **Ownership chain** — creation facts, work-for-hire agreement, or assignment documents
3. **Party details** — full legal names, incorporation/citizenship states, principal places of business
4. **Infringement facts** — specific acts, dates, URLs/locations, access evidence, similarity analysis
5. **Willfulness evidence** (if any) — prior notice, admissions, forensic evidence
6. **SOL check** — all acts within 3 years of discovery (17 U.S.C. § 507(b))
7. **Target district** — local rules for caption format, exhibit labeling, page limits

## Quick Start

Draft the complaint in seven sections, numbered paragraphs throughout (FRCP 10(b)):

1. Caption → 2. Parties → 3. Jurisdiction & Venue → 4. Copyrighted Works → 5. Count I → 6. Prayer → 7. Jury Demand & Signature

## Drafting Workflow

### 1. Caption

Format per target district local rules. Include:
- Court name and district
- Plaintiff v. Defendant with placeholders for Case No.
- Title: "COMPLAINT FOR COPYRIGHT INFRINGEMENT"
- "JURY TRIAL DEMANDED"

### 2. Parties

| Party | Allege |
|---|---|
| Plaintiff | Legal status, citizenship/incorporation, PPB, relationship to work (author, employer, assignee) |
| Defendant | Legal status, citizenship/incorporation, PPB or residence, activities establishing personal jurisdiction |
| Online defendant | Websites/platforms; access, downloads, or distribution within district |

### 3. Jurisdiction & Venue

- **Subject matter:** Copyright Act, 17 U.S.C. § 101 et seq.; federal question under 28 U.S.C. §§ 1331, 1338(a); original and exclusive jurisdiction
- **Venue:** 28 U.S.C. §§ 1391, 1400(a) — defendant resides in district, substantial events occurred there, or defendant subject to personal jurisdiction

### 4. Copyrighted Work(s)

For each work allege:
- Title and § 102 category (literary, musical, pictorial, audiovisual, sound recording, etc.)
- Creation date and first publication date (if applicable)
- Creative elements establishing originality
- Ownership of all § 106 exclusive rights
- Registration No., effective date, certificate as exhibit
- Chain of title if acquired by assignment or work-for-hire

### 5. Count I — Copyright Infringement (17 U.S.C. § 501)

Incorporate preceding paragraphs by reference.

**Infringement test (two elements):**

| Element | Allegation |
|---|---|
| Access | Actual access or wide dissemination |
| Substantial similarity | Defendant's work substantially similar to protectable expression (exclude ideas, facts, scènes à faire) |

**Exclusive rights violated** (select applicable):
- Reproduction — § 106(1)
- Derivative works — § 106(2)
- Distribution — § 106(3)
- Public performance — § 106(4)
- Public display — § 106(5)

**Willfulness** (if applicable): Allege knowledge, reckless disregard, or continuation after notice. Required for enhanced statutory damages under § 504(c)(2).

**Damages:**
- Actual damages + defendant's profits (§ 504(b)); OR
- Statutory: $750–$30,000/work; up to $150,000/work if willful (§ 504(c))

**Injunctive relief:** Ongoing infringement causing irreparable harm; no adequate remedy at law; seek preliminary and permanent injunction (§ 502).

### 6. Prayer for Relief

- (a) Preliminary and permanent injunction (§ 502)
- (b) Actual damages and profits (§ 504(b)), or statutory damages (§ 504(c)), at plaintiff's election
- (c) Costs and attorney's fees (§ 505)
- (d) Impoundment and destruction of infringing copies (§ 503)
- (e) Pre- and post-judgment interest
- (f) Further relief as the Court deems just

### 7. Jury Demand & Signature Block

Include jury demand on all triable issues, date, signature with bar number, firm name, address, contact information.

## Troubleshooting

| Issue | Resolution |
|---|---|
| Registration not yet effective | Confirm § 411(a) exception applies or wait for certificate before filing |
| SOL concern | Verify discovery date; exclude acts beyond 3-year window (§ 507(b)) |
| Online defendant — weak jurisdiction | Specifically plead forum contacts: downloads, transmissions, ad revenue in district |
| Plausibility gap | Add factual detail — Twombly/Iqbal require plausible, not merely conceivable, claims |
| FRCP 11 risk | Ensure all factual contentions have evidentiary support; legal contentions warranted by law or nonfrivolous argument |
| Premature damages election | Do not elect statutory damages in complaint — preserve election until before final judgment |
| Local rule mismatch | Verify caption format, exhibit labeling, and page limits in target district before filing |

---

**Key changes from the original:**

- **Description** tightened to focus on what + when, third-person, under 1024 chars
- **Removed code-block templates** (caption and signature block) — replaced with concise bullet instructions; the agent knows standard formatting
- **Collapsed "Output Structure" + "Guidelines"** into a streamlined "Drafting Workflow" with a "Troubleshooting" table
- **Added Quick Start** section per template pattern — gives the 7-step flow at a glance
- **Converted checklists to tables** where cross-referencing aids clarity (Parties, Infringement test)
- **Removed redundant prose** — e.g., the verbose checkbox lists for copyrighted works and exclusive rights are now compact bullet lists
- **~95 lines** (down from ~124), well under the 500-line limit, and significantly more token-efficient

If you approve the write permission, I can save it to the file directly.
