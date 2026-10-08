---
name: research-recent-amendments-tracker-sboghossian
title: Recent Amendments Tracker
description: Use when a user asks whether a statute is current, whether something has recently changed in a jurisdiction, or whether a previously researched answer has been superseded. Checks official gazettes, legislative portals, and regulator notices across MENA (Lebanon Official Gazette, KSA Umm Al-Qura, UAE Federal and emirate gazettes, DIFC Laws portal, ADGM Legislation portal) and secondary jurisdictions (EU Official Journal, FR Légifrance, UK legislation.gov.uk). Returns current version date, last amendment summary, notable interpretive rulings, and pending changes with status.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-recent-amendments-tracker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Recent Amendments Tracker

Find recent changes to a statute, regulation, or legal rule — and check whether a previously researched position is still current law. Essential for any legal work relying on regulatory text that may have changed, particularly in MENA jurisdictions undergoing rapid legislative reform.

## When to invoke

This skill is invoked:

1. **Directly**: when the user asks "has X changed recently?", "is this still good law?", or "what's the latest on [regulation]?"
2. **Automatically alongside**: [[research-statute-lookup]] and [[research-case-law-search]] — a cached answer about a statute may be stale; this skill checks freshness.
3. **In deep research**: as step 4 of [[research-deep-research-orchestrator]] to verify that gathered sources are current.
4. **Before delivering any client-facing regulatory answer**: especially in UAE, KSA, and DIFC where reform has been intensive post-2020.

## Why this matters in MENA

MENA jurisdictions have undergone unusually rapid legislative reform in recent years:

- **UAE**: New commercial companies law, new labor law (FDL 33/2021), new personal data protection law (2021), new arbitration law amendments, new criminal procedure reforms — all since 2020.
- **KSA**: Vision 2030 reform program has produced structural changes in foreign investment rules, capital markets, commercial courts, labor law, and entertainment regulation since 2016, with ongoing amendments.
- **DIFC**: Regular updates to DIFC Laws and the DFSA Rulebook — sometimes annually.
- **Lebanon**: Legislative near-paralysis since 2019, but BDL and SIC circulars have continued — these may be the operative legal rule even where Parliament has not acted.

## Sources by jurisdiction

### Lebanon
- **Al-Jarida Al-Rasmiya** (الجريدة الرسمية) — the official gazette of Lebanon. Published amendments to laws and legislative decrees. Physical copies available; online access limited but improving.
- **BDL Circulars** — Banque du Liban circulars are a primary source for banking and financial regulation, often more current than statute.
- **SIC Notices** — Special Investigation Commission notices on AML/sanctions.
- Check date of last Gazette publication for the specific law; many Lebanese laws are pre-1975 and have seen few amendments.

### KSA
- **Umm Al-Qura** (أم القرى) — the official gazette of Saudi Arabia. Publishes Royal Decrees, Council of Ministers decisions, and ministerial regulations. Published weekly.
- **Bureau of Experts at the Council of Ministers (BOE)** — consolidated texts of regulations post-amendment.
- **SAMA, CMA, SCFHS circulars** — regulator-level guidance that may precede or supplement statutory amendments.
- Note: Umm Al-Qura is in Arabic; Hijri calendar dates require conversion.

### UAE Federal
- **UAE Federal Official Gazette** (Al-Jarida Al-Rasmiya Al-Ittihadia) — Federal Decree-Laws, Cabinet Resolutions, Ministerial Decisions.
- **MOJ website** for consolidated law texts.
- **Per-emirate executive council decrees** — Dubai Executive Council, Abu Dhabi Executive Council — relevant for emirate-level matters.

### DIFC
- **DIFC Laws portal** (difclaw.ae) — consolidated, version-controlled texts of all DIFC Laws and Regulations.
- **DFSA Rulebook** (dfsa.ae) — updated in modules; date-specific versions available.
- This is one of the best-maintained legal portals in the region for tracking amendments.

### ADGM
- **ADGM Legislation portal** (legislation.adgm.com) — all ADGM Regulations, Rules, and Guidance.
- FSRA Rulebook for financial services.

### EU
- **EU Official Journal** (eur-lex.europa.eu) — all EU Regulations (directly applicable), Directives, Decisions.
- Filter by CELEX number and date.
- **EUR-Lex "consolidated" texts** are annotated with amendments incorporated.

### France
- **Légifrance** (legifrance.gouv.fr) — consolidated texts of French laws and regulations with amendment history.
- Use the "version en vigueur au" date filter to get the text as of a specific date.
- Available via [[connector-legifrance]].

### UK
- **legislation.gov.uk** — consolidated UK statutes with amendment annotations.
- Clearly flags "up to date with all changes known to be in force" vs "changes not yet incorporated."
- Note: law.gov.uk has limitations on incorporating recent commencement orders — check statutory instrument entries directly.

## What to look for

For each statute or regulation being tracked, check for:

1. **Direct amendments**: legislation that expressly amends specific articles of the original statute
2. **Repeal and replacement**: the original statute has been replaced wholesale by a new instrument
3. **Cabinet/executive decisions implementing the statute**: implementing regulations that operationalize the statute's provisions (often more detailed than the parent law)
4. **Regulator guidance** superseding or softening the literal statutory reading — see [[research-regulator-guidance-lookup]]
5. **Pending bills / draft regulations**: signaled in official policy announcements but not yet enacted — flag as "pending" with current status
6. **Court rulings interpreting recent changes** — the statute may have changed but court interpretation is still forming

## Output format

```
## Amendment Status: [Statute / Regulation Name]

**Jurisdiction**: [jurisdiction]
**Current version date**: [ISO date — the date of the most recent amendment or restatement]
**Research date**: [ISO date — when this check was run]
**Source**: [official gazette / portal name and URL if available]

### Last amendment
**Date**: [ISO date]
**Instrument**: [name + number of amending instrument]
**Summary**: [2–3 sentence description of what changed]
**Impact**: [does this change affect the user's specific question?]

### Notable interpretive rulings since last amendment
[If applicable: list up to 3 court decisions or regulator guidance notes that have clarified or altered the practical effect of the statute since amendment]

### Pending changes
**Status**: [draft / approved / pending commencement / none identified]
**Description**: [if draft or approved: what is proposed; if none: state so]

### Confidence
**High** — sourced directly from official gazette / consolidated portal
**Medium** — sourced from secondary report; primary source verification recommended
**Low** — training data only; no live gazette check was possible; verify before reliance

### Caveats
[Any jurisdiction-specific caution — e.g., Lebanon gazette access gap, KSA Hijri calendar conversion, UAE emirate-level decree not captured in federal gazette]
```

## MENA-specific traps

### UAE: federal vs emirate-level instruments
UAE law operates on two levels: federal (applying across all emirates) and emirate-level (applying in one emirate). A change to a Dubai Executive Council decision does not appear in the Federal Gazette. Check both sources for UAE matters.

### KSA: Hijri calendar
All official KSA dates are in Hijri calendar. When citing or searching, be precise about whether a date is AH (Anno Hegirae) or AD. A one-year error in conversion (approximate Hijri-Gregorian shift) can cause you to miss an amendment.

### Lebanon: gazette backlog
Lebanon's official gazette publication has been delayed and irregular since 2020. In periods of political crisis, enacted laws may not be published in the gazette for months. Check bar association bulletins and secondary sources as a cross-check — but note that official promulgation via the gazette is the trigger for most laws' entry into force.

### DIFC/ADGM: rulebook modules
The DFSA and FSRA publish their rulebooks in modules. An amendment to, say, the DFSA Conduct of Business Module does not require an amendment to the DIFC Companies Law. Check both the relevant statute and the applicable rulebook module.

## Run alongside

Always pair with:
- [[research-statute-lookup]] for the full current statutory text
- [[research-case-law-search]] to check whether courts have interpreted recent amendments

## Related skills

- [[research-statute-lookup]]
- [[research-case-law-search]]
- [[research-regulator-guidance-lookup]]
- [[research-regulation-lookup]]
- [[research-deep-research-orchestrator]]
