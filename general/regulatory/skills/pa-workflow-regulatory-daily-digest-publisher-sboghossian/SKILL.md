---
name: pa-workflow-regulatory-daily-digest-publisher-sboghossian
title: Regulatory — Daily Digest Publisher
description: Use when a law firm or legal team needs to automatically compile and publish a daily regulatory digest covering MENA jurisdictions (UAE, KSA, LB, EG) and selected international regulators. Aggregates new gazette entries, SAMA, CBUAE, BDL, and SDAIA bulletins, court decisions of regulatory interest, and enforcement trends, then formats and delivers the digest by email and Slack by 8am on weekdays.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-regulatory-daily-digest-publisher
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulatory — Daily Digest Publisher

## Purpose

Regulatory change in MENA is constant and fast-moving. A daily digest ensures that legal teams, compliance officers, and clients stay current without spending hours monitoring multiple official publications. This workflow aggregates, filters, summarizes, and delivers a curated daily digest at 8am on every weekday — covering the key MENA regulatory bodies plus international developments that affect the firm's client base.

## Inputs / Configuration

| Parameter | Default | Override |
|---|---|---|
| Jurisdictions covered | UAE, KSA, LB, EG, DIFC, ADGM, GCC | Add EU, UK, US, or others |
| Regulatory domains | AML/CFT, financial services, data protection, corporate, employment, tax | Narrow or expand per firm practice areas |
| Delivery channels | Email + Slack | Configure recipient list and Slack channel |
| Delivery time | 8:00 AM local (Asia/Beirut default) | Configurable by recipient timezone |
| Language | English summary; Arabic original reference | Add French for Lebanon-specific content |
| Digest frequency | Weekdays only | Can be set to 7 days during high-flux periods |
| Client distribution | Firm-internal by default | Enable opt-in external client distribution |

## Source Monitoring

The following sources are monitored daily:

### UAE
- UAE Official Gazette (Al-Jarida Al-Rasmiya) — federal decrees, ministerial decisions
- Central Bank of UAE (CBUAE) — circulars, guidelines, enforcement notices
- UAE Securities and Commodities Authority (SCA/ESCA) — capital markets regulations
- VARA (Virtual Assets Regulatory Authority) — virtual asset regulations and notices
- DIFC Gazette and DFSA — DIFC legal instruments and DFSA regulatory notices
- ADGM Official Gazette and FSRA — ADGM legislation and FSRA regulatory notices
- Dubai Courts / Abu Dhabi Courts — published judgments of regulatory significance

### KSA
- Umm Al-Qura (Saudi Official Gazette) — Royal Decrees, Council of Ministers decisions
- SAMA — circulars, guidelines, enforcement actions, open banking updates
- SDAIA / NDMO — data protection regulations and guidance
- CMA (Capital Market Authority) — securities and capital market rules
- ZATCA (Zakat, Tax and Customs Authority) — tax and customs regulations
- MISA (Ministry of Investment) — foreign investment regulations

### Lebanon
- Lebanese Official Gazette (Al-Jarida Al-Rasmiya) — laws and decrees
- BDL (Banque du Liban) — circulars and basic decisions
- Higher Banking Commission decisions (when published)

### Egypt
- Egyptian Official Gazette (Al-Jarida Al-Rasmiya) — laws and ministerial decisions
- Central Bank of Egypt (CBE) — banking regulations and AML guidance
- Financial Regulatory Authority (FRA) — non-banking financial sector
- Egyptian Tax Authority (ETA) — tax regulations

### GCC / Regional
- GCC Secretariat — unified standards and protocols
- Arab Monetary Fund (AMF) — regional AML/CFT guidance
- FATF — mutual evaluation reports, guidance notes (especially when MENA countries are assessed)

## Processing Pipeline

### Step 1 — Content ingestion (automated, nightly)

- Crawl official gazette and regulator websites for new publications
- Parse Arabic-language publications (Arabic NLP required)
- Parse English-language publications
- Deduplicate against prior 7 days
- Flag items older than 24 hours that were not captured in prior editions

### Step 2 — Relevance scoring

For each new item, assign:
- **Domain tags** (AML, data protection, corporate, financial services, employment, etc.)
- **Jurisdiction** 
- **Urgency** (IMMEDIATE = compliance deadline within 30 days; HIGH = 31–90 days; ROUTINE = 90+ days or informational)
- **Firm practice area match** (which practice groups and client types are affected)

Filter out: procedural government notices, infrastructure spending announcements, non-regulatory administrative matters.

### Step 3 — Summarization

For each item that passes the relevance filter:

**Summary format:**
```
[JURISDICTION] — [REGULATORY BODY] — [DOMAIN]
[Urgency badge: IMMEDIATE / HIGH / ROUTINE]
[Headline: 1 sentence describing the development]
[Summary: 3–5 sentences — what changed, who is affected, key date]
[Source: link to official publication]
```

Arabic-language items: provide Arabic original reference + English summary. Do not mistranslate — if uncertain, note "Arabic-language summary; verify against original."

### Step 4 — Assembly and formatting

Digest structure:

```markdown
# MENA Regulatory Digest — [Date]

## IMMEDIATE ACTION REQUIRED
[Items with compliance deadlines within 30 days]

## TODAY'S DEVELOPMENTS

### UAE
- [Item 1]
- [Item 2]

### KSA
- [Item 1]

### Lebanon
...

### Egypt
...

### GCC / Regional
...

## UPCOMING DEADLINES THIS WEEK
| Date | Jurisdiction | Requirement |
|---|---|---|
| [date] | UAE | CBUAE Open Banking Phase 2 |

## ENFORCEMENT ACTIONS AND COURT DECISIONS
[Any enforcement notices or published court/tribunal decisions with regulatory implications]

---
*Sources: [list of official publications checked]*
*Next digest: [tomorrow's date] at 8:00 AM*
```

### Step 5 — Delivery

- **Email**: HTML-formatted email to configured recipient list (firm distribution list + opted-in clients)
- **Slack**: summarized version in `#regulatory-digest` channel; IMMEDIATE items also posted to `#urgent-regulatory`
- **Firm portal** (if configured): posted to internal knowledge base
- **Archive**: stored with date stamp for future reference and contradiction checking

## Quality Controls

- If fewer than 3 items are identified on a given day, the digest still publishes with a note: "No new regulatory developments today that meet the relevance threshold."
- If a major development is identified (new law enacted, significant enforcement action), a supplementary alert is sent immediately outside the daily digest cycle — see [[pa-workflow-regulatory-client-alert-drafter-firm-voice]].
- Items are not published in the digest until source verification is complete — no social-media-sourced updates without official publication confirmation.

## MENA Publication Timing Notes

- UAE Official Gazette: published daily except Fridays; usually online within 24 hours of decree issuance
- CBUAE circulars: published directly on CBUAE website; no gazette requirement
- KSA Umm Al-Qura: published Fridays; SAMA circulars published directly
- Lebanese Official Gazette: published Mondays and Thursdays (historically); delays are common
- Egyptian Official Gazette: published daily; available online with some delay

Weekday-only delivery accounts for the Saturday–Sunday weekend in MENA. On Monday mornings, the digest includes Saturday + Sunday items.

## Related Skills

- [[pa-workflow-regulatory-cross-jurisdiction-tracker]]
- [[pa-workflow-regulatory-client-alert-drafter-firm-voice]]
- [[pa-workflow-regulatory-compliance-gap-matrix]]
- [[pa-workflow-regulatory-enforcement-likelihood-scorer]]
