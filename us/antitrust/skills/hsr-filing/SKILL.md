---
name: hsr-filing
title: HSR Premerger Notification Filing
description: Prepares Hart-Scott-Rodino Act premerger notification filings for FTC/DOJ submission under 15 U.S.C. § 18a and 16 C.F.R. Parts 801-803. Covers threshold verification, NAICS revenue breakdowns, Item 4(c)/(d) document collection, competitive overlap analysis, prior acquisitions disclosure, and filing assembly. Use when an M&A deal may meet HSR size thresholds and requires antitrust clearance, premerger notification, or FTC/DOJ merger review.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hsr-filing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: antitrust
language: en
---

# HSR Premerger Notification Filing

Assembles a complete Hart-Scott-Rodino filing — threshold analysis through post-filing monitoring — for FTC/DOJ electronic submission.

## Prerequisites

Collect before starting:

- **Transaction documents** — definitive agreement, exhibits, schedules, amendments
- **Corporate structure charts** — ultimate parent entities for both acquiring and acquired persons
- **Financial statements** — most recent fiscal year revenues by segment/product line
- **SEC filings** — 10-K, 10-Q, 8-K, proxy (or audited financials if private)
- **Board/management materials** — presentations, memos, studies evaluating the deal
- **Prior acquisitions list** — all acquisitions by acquiring person in the past 10 years

## Core Workflow

### 1. Threshold Analysis

| Test | Requirement | Notes |
|------|-------------|-------|
| Size-of-Transaction | Current annual threshold (inflation-adjusted) | Valuation per 16 C.F.R. § 801.10 |
| Size-of-Person | At least one party meets revenue/asset threshold | Verify both parties |
| Exemptions | Check 16 C.F.R. Part 802 | Watch: ordinary course assets, real property, investment-only securities |

Valuation components to document:
- Cash consideration
- FMV of non-cash consideration (stock, etc.)
- Assumed liabilities includable under § 801.10
- Earnout/contingent payment treatment
- Voting security percentage thresholds crossed (25%, 50%, other)

### 2. Party Identification

**Acquiring Person** — Ultimate parent entity + full control chain; identify which entities hold acquired assets/securities and whose revenues/prior acquisitions must be reported.

**Acquired Person** — Scope (entire entity, specific voting securities, or specific assets); ultimate parent entity; if subsidiary/division only, clearly delineate scope.

### 3. NAICS Revenue Breakdown

Report revenues at six-digit NAICS level for each party (most recent fiscal year, threshold ≥ $1M).

| NAICS Code | Description | Acquiring Revenue | Acquired Revenue | Overlap? |
|------------|-------------|-------------------|------------------|----------|
| XXXXXX | [Product/service] | $X | $X | Yes/No |

- Classify at the most specific six-digit level
- Document allocation methodology for bundled products
- Note variance between internal reporting and NAICS classifications

### 4. Competitive Overlap Analysis

For each six-digit NAICS overlap, analyze:

- Competing products/services and customer-side substitutability
- Market share estimates (source: industry reports, SEC filings, internal data)
- Principal competitors and approximate shares
- HHI: flag post-merger > 2,500 with delta > 200 — **confirm current Merger Guidelines thresholds**
- Vertical relationships: supplier-customer links, foreclosure risk
- Geographic scope: local / regional / national / international

### 5. Item 4(c) and 4(d) Documents

**Scope** — All studies, surveys, analyses, and reports prepared by or for any officer/director evaluating the acquisition regarding market shares, competition, competitors, sales growth, or market expansion.

Search targets:
- Board presentations and minutes
- Investment committee memoranda
- CIMs
- Market research, competitive landscape analyses, synergy studies
- Financial advisor and investment bank materials provided to officers/directors

Produce a descriptive index: document title, date, author, recipient, relevance to 4(c)/4(d).

> These documents drive substantive agency review. Include anything touching competitive factors, even tangentially. Omissions risk civil penalties.

### 6. Prior Acquisitions (10-Year Lookback)

For each acquisition by the acquiring person in overlapping NAICS codes (past 10 years):

| Date | Entity/Assets Acquired | Value | NAICS Codes | Overlap with Current Deal |
|------|------------------------|-------|-------------|--------------------------|
| | | | | |

Flag roll-up patterns that may trigger cumulative scrutiny.

### 7. Certification and Execution

- Certifying person: officer/director with supervisory responsibility for filing
- Attestation: true, correct, complete; all required documents submitted
- False statements subject to 18 U.S.C. § 1001
- Filing date = certification date = start of statutory waiting period

## Filing Assembly Checklist

```
- [ ] Notification and Report Form — complete and internally consistent
- [ ] NAICS revenue tables — verified against financial records
- [ ] Item 4(c)/4(d) documents — exhaustive search; descriptive index attached
- [ ] SEC filings / audited financials — most recent fiscal year
- [ ] CIMs and offering memoranda — included if prepared for this transaction
- [ ] Filing fee — calculated on transaction value; payment arranged
- [ ] Electronic submission — FTC e-filing format/naming conventions met
- [ ] Dual filing coordination — both parties filing same day if required
```

## Post-Filing Monitoring

| Milestone | Timing | Action |
|-----------|--------|--------|
| Initial waiting period | 30 days from filing | Monitor for deficiency notices |
| Early termination | Agency discretion | Request if no competitive concerns apparent |
| Second Request | Within waiting period | Triggers full document production + interrogatories |
| Closing eligibility | Waiting period expiry or ET granted | Advise client |

## Pitfalls and Checks

- **Thresholds change annually** — always confirm current dollar amounts from FTC published notice before filing
- **Item 4(c)/(d) over-inclusion** — when in doubt, include the document; exclusion disputes cost more than over-production
- **No legal conclusions on market definition** — present competitive data factually; leave ultimate market definition to the agencies
- **U.S. federal only** — 15 U.S.C. § 18a; non-U.S. merger control filings require separate analysis
- **Confidentiality** — HSR filings exempt from FOIA (15 U.S.C. § 18a(h))
- **Penalties** — non-compliance carries civil penalties per day per violation; **confirm current penalty amount from FTC**

---

Key changes from the original:

- **Description** — Trimmed from 85 words to 58; removed "Trigger keywords" list (discovery words are now embedded naturally); kept third-person voice with explicit "Use when" trigger
- **Removed `tags`** — Not part of the Agent Skills frontmatter spec
- **Flattened structure** — Replaced the nested "Output Structure" wrapper with a flat "Core Workflow" with numbered steps, reducing one heading level
- **Merged prose** — Party Identification collapsed from two bullet lists into two dense paragraphs; certification simplified
- **Removed horizontal rules** — Unnecessary visual separators between workflow steps
- **Checklist in fenced block** — Kept copyable for tracking
- **Renamed "Guidelines" to "Pitfalls and Checks"** — Matches the best-practices pattern and signals actionable caution rather than general advice
- **Token reduction** — ~165 lines down from ~165, but significantly fewer tokens due to compressed prose (estimated ~25% token savings)
