---
name: pharma-reg-summary
title: Pharmaceutical Regulation Compliance Summary
description: Generates structured pharmaceutical regulatory compliance summaries covering FDA approval pathways, patent/IP intersections (Orange Book, Hatch-Waxman), and marketing restrictions (off-label, DTC, Anti-Kickback). Use when preparing FDA compliance overviews, submission readiness assessments, or promotional compliance reviews.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pharma-reg-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Pharmaceutical Regulation Compliance Summary

Produces an actionable regulatory compliance summary structured around FDA frameworks, patent/IP strategy, and promotional compliance.

## Prerequisites

Gather before starting:

1. **Product portfolio** — marketed products, pipeline compounds, therapeutic areas
2. **Regulatory filings** — pending NDAs/ANDAs/BLAs, active INDs, post-approval commitments
3. **Commercial activities** — speaker programs, DTC campaigns, consulting arrangements
4. **Compliance history** — warning letters, consent decrees, audit findings

## Quick Start

Structure every summary into three sections:

1. **Drug Approval & Post-Market Obligations** — pathway requirements, safety reporting, PMRs/PMCs
2. **Patent & IP Regulatory Intersections** — Orange Book, exclusivity, Hatch-Waxman
3. **Marketing & Promotional Compliance** — off-label rules, financial compliance, DTC advertising

## Core Workflow

### 1. Drug Approval & Post-Market Obligations

| Pathway | Requirements | Pitfalls |
|---------|-------------|----------|
| NDA 505(b)(1) | Full clinical data, CMC, labeling | Data integrity gaps, incomplete safety DBs |
| ANDA 505(j) | Bioequivalence, Para IV certs | Improper BE design, cert errors |
| BLA 351(a) | Biosimilarity/interchangeability | Analytical similarity gaps, immunogenicity |
| Expedited (BT/FT/AA) | Post-market confirmatory requirements | Missing confirmatory trial milestones |

Per-product checklist:

- [ ] IND compliance (21 CFR 312): 7/15-day safety reports, annual reports, protocol amendments
- [ ] Data integrity (21 CFR 11): electronic records, GCP/GLP/GMP
- [ ] Post-market: FAERS reporting (15-day expedited, 90-day periodic), REMS if applicable
- [ ] PSURs/PBRERs for internationally marketed products
- [ ] PMR/PMC tracking with deadlines and escalation triggers

### 2. Patent & IP Regulatory Intersections

| Framework | Authority | Key Points |
|-----------|----------|------------|
| Orange Book | 21 CFR 314.53 | Patent listings for drug/method of use; improper listings → antitrust risk |
| Purple Book | 42 USC § 262 | Reference product exclusivity, biosimilar interchangeability |
| Hatch-Waxman | 21 USC § 355(j)(2)(A)(vii) | Para I–IV certs, 30-month stay, 180-day FTF exclusivity |
| Patent term extension | 35 USC § 156 | One per product; file within 60 days of approval |
| Pediatric exclusivity | 21 USC § 355a | 6-month addition; written request compliance required |
| NCE exclusivity | 21 USC § 355(c)(3)(E) | 5-year NCE, 3-year new clinical investigations |

Flag in every summary:

- [ ] Patent strategy alignment with submission timelines
- [ ] Orange Book use code accuracy (delisting petition / FTC risk)
- [ ] Upcoming exclusivity expirations and generic/biosimilar entry risk

### 3. Marketing & Promotional Compliance

**Off-label promotion** — Prohibited under 21 USC § 331(d) (misbranding). Narrow exceptions: unsolicited requests (on-label redirect via medical affairs), peer-reviewed reprints under 21 USC § 360aaa. DOJ pursues under FCA theories.

**Promotional materials** — Fair balance required (21 CFR 202.1). Substantial evidence standard for efficacy claims. File Form FDA 2253 at first use.

**Digital/social media** — Follow FDA draft guidance for space-constrained formats. Monitor owned channels for misinformation. Disclose KOL/influencer arrangements per FTC + Sunshine Act.

**DTC advertising** — Broadcast: major statement + toll-free number/website. Print: brief summary of PI. Submit to OPDP; use Advisory Comment process for novel claims.

**Financial compliance:**

| Statute | Key Rules |
|---------|-----------|
| Anti-Kickback (42 USC § 1320a-7b) | Safe harbors: FMV compensation, written agreements, legitimate services |
| Sunshine Act (42 USC § 1320a-7h) | Report transfers of value >$10; track meals, consulting, speaking |
| FCA (31 USC § 3729) | Off-label promotion as predicate for FCA liability |

## Compliance Checklist

- [ ] SOPs for submissions, safety reporting, labeling updates
- [ ] Commercial team training on promotional boundaries (annual + new hire)
- [ ] MLR (medical-legal-regulatory) review of all promotional materials
- [ ] Audit program: labeling, ad claims, speaker program FMV
- [ ] PMR/PMC tracking with escalation triggers
- [ ] Whistleblower/compliance hotline and investigation protocols
- [ ] International harmonization assessment (EMA, PMDA) if applicable

## Pitfalls

- **Missing product-type distinctions** — requirements differ for small molecule vs. biologic vs. generic; always separate
- **Controlled substances** — DEA scheduling overlay adds requirements; flag when applicable
- **State law variance** — state Sunshine laws and marketing consent statutes may impose additional obligations
- **Stale citations** — mark uncertain or recently updated authorities with [VERIFY]
- **Scope creep** — present regulatory facts; do not provide legal conclusions on enforcement risk — let counsel assess
- **International gaps** — if international operations exist, note material FDA vs. EMA differences
