---
name: traffic-enforcement-summary
title: Traffic Law Enforcement Summary
description: Generates structured summaries of traffic law enforcement data covering DUI metrics, violation trends, enforcement outcomes, and resource allocation. Use when analyzing citation records, arrest statistics, violation reports, or preparing public safety strategic planning documents for law enforcement leadership.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/traffic-enforcement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: criminal
language: en
---

# Traffic Law Enforcement Summary

Synthesizes traffic enforcement data into an executive-ready analytical report with statistical trends, effectiveness metrics, and evidence-based policy recommendations.

## Prerequisites

1. **Enforcement data** — citation records, arrest statistics, case dispositions, violation counts
2. **Temporal scope** — defined reporting period for trend analysis
3. **Geographic scope** — jurisdiction(s) and sub-area breakdowns (precincts, corridors, hotspots)
4. **Comparative baselines** — prior-period data for year-over-year analysis (if available)

## Quick Start

1. Gather enforcement data for the reporting period and jurisdiction
2. Build the report following the six sections below
3. Flag any violation category with >15% year-over-year change
4. Tie every recommendation to a specific data finding
5. Review against the guardrails before delivery

## Report Sections

### 1. Executive Overview

| Element | Content |
|---|---|
| Key findings | Top 3–5 statistically significant trends |
| Critical alerts | Trends requiring immediate attention (spikes, emerging patterns) |
| Top recommendations | Prioritized policy/resource actions tied to findings |
| Reporting period | Date range, data sources, jurisdiction |

### 2. DUI Enforcement Metrics

Present in tables where possible:

- Arrest volume (total, YoY delta, monthly distribution)
- BAC distribution (tiers: 0.08–0.14, 0.15–0.19, 0.20+)
- Repeat offender rate and recidivism patterns
- Case dispositions (conviction, plea, dismissal, diversion rates)
- Refusal-to-test rates and implied consent outcomes
- Drug-impaired driving incidents (if data available)
- Seasonal/temporal patterns (holidays, weekends, time-of-day)

### 3. Traffic Violation Trends

Categorize by infraction type:

| Category | Metrics |
|---|---|
| Speeding | Volume, speed-over-limit distribution, school/construction zones |
| Reckless driving | Counts, accident correlation |
| Distracted driving | Cell phone, other distractions, YoY trend |
| License/registration | Suspended license, unregistered vehicles, uninsured motorist |
| Equipment failures | Lighting, brakes, tires |
| Seatbelt/child restraint | Compliance rates, citation trends |

### 4. Statistical Analysis

- YoY comparisons (raw counts + percentage change)
- Seasonal variation (monthly/quarterly breakdown)
- Peak enforcement periods (day-of-week, time-of-day)
- Geographic hotspot identification (top 10 corridors/intersections)
- Violation-to-accident correlation where data permits
- Per-capita or per-VMT normalization if traffic volume data available

Trend table template:

| Metric | Prior Period | Current Period | Delta (%) | Trend |
|---|---|---|---|---|
| Total citations | | | | ↑/↓/→ |
| DUI arrests | | | | |
| Accident-related | | | | |

### 5. Enforcement Effectiveness

- Citation-to-conviction ratio
- Court disposition patterns (continuances, plea rates, dismissal causes)
- Fine collection rates
- Targeted campaign impact on recidivism
- Officer deployment efficiency (citations per patrol hour, if available)

### 6. Recommendations

Each recommendation must: (1) cite the supporting data finding, (2) specify the action, (3) identify the responsible unit, (4) note resource implications.

| Area | Examples |
|---|---|
| Policy adjustments | Speed threshold changes, enforcement priorities |
| Resource reallocation | Shift scheduling, hotspot deployment |
| Training needs | Emerging violation types, SFST updates, body-cam protocols |
| Technology/equipment | Automated enforcement, data systems, testing equipment |
| Community engagement | Public awareness campaigns, compliance incentives |

## Guardrails

- **Tone**: Professional, suitable for law enforcement executives, elected officials, and public safety boards
- **Tables over prose**: Present statistics in tables; avoid dense narrative
- **Source attribution**: Cite specific data sources, case counts, and time periods throughout
- **Equity**: Flag demographic disparity patterns for leadership review without editorializing
- **National data**: If supplementing with NHTSA/FARS statistics, clearly distinguish from local data
- **Scope**: Stay within analytical and operational scope — do not editorialize on sentencing policy or legislative reform
- **Data quality**: Note limitations (incomplete records, reporting lag, system migration gaps)
- **Length**: Target 5–15 pages depending on data scope

---

Key changes from the original:
- Removed `tags` from frontmatter (not in the spec)
- Tightened the `description` for token efficiency while keeping trigger guidance
- Added a **Quick Start** section for at-a-glance workflow
- Converted checkbox lists (`- [ ]`) to plain bullet lists (checkboxes are for tracking mutable progress, not reference specs)
- Collapsed the verbose "Output Structure" heading into flatter **Report Sections**
- Condensed the recommendations requirements from a numbered list into a single inline sentence
- Renamed "Guidelines" to **Guardrails** with bold-key format for scannability
- Removed the code-fenced trend table template wrapper (kept the table itself inline)
- Removed the "Procedural/resource constraints affecting outcomes" bullet (redundant with recommendations section)
- Overall reduction from 118 lines to ~98 lines with better information density
