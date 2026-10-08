---
name: pa-workflow-regulatory-enforcement-likelihood-scorer-sboghossian
title: Regulatory — Enforcement Likelihood Scorer
description: Use when counsel or a compliance team needs to assess and score the likelihood that a specific compliance gap will attract regulatory enforcement action. Produces a risk-tier rating (Critical / High / Medium / Low) based on regulator focus areas, recent enforcement patterns, company profile, and industry-specific risk factors. Designed for MENA regulators (CBUAE, SAMA, DFSA, VARA, SDAIA) and international frameworks (FCA, SEC, FinCEN).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-regulatory-enforcement-likelihood-scorer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulatory — Enforcement Likelihood Scorer

## Purpose

Not all compliance gaps carry the same risk. A documented policy gap in an area the regulator is actively inspecting is materially different from a procedural gap in a low-scrutiny domain. This workflow scores each identified compliance gap on enforcement likelihood — enabling a compliance team or board to prioritize remediation spending based on real risk exposure rather than theoretical completeness.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Compliance gap(s) to score | Yes | Free text description or structured from [[pa-workflow-regulatory-compliance-gap-matrix]] |
| Jurisdiction | Yes | Determines which regulator's behavior is analyzed |
| Regulatory domain | Yes | AML/CFT, data protection, capital markets, cybersecurity, etc. |
| Company profile | Yes | Industry sector, license type, company size, ownership structure |
| Recent regulatory inspection history | If available | Prior findings indicate regulator's current attention areas |
| Enforcement actions in same sector (past 24 months) | Recommended | Signals current enforcement campaign |
| Self-disclosure status | Optional | Some regulators credit proactive disclosure |

## Scoring Methodology

### Factor 1 — Regulator focus intensity

Score 1–5 (5 = highest enforcement activity):

| Score | Definition |
|---|---|
| 5 | Active enforcement campaign in this domain — multiple public actions in past 12 months |
| 4 | Elevated scrutiny — regulator has publicly flagged this area; inspections are underway |
| 3 | Standard supervision — this is a routine inspection area |
| 2 | Low historical enforcement — few public actions; regulator capacity is limited |
| 1 | Virtually no enforcement record — regulator has not publicly acted on this issue |

**MENA regulator focus areas as of 2025:**

| Regulator | High-focus areas (4–5) |
|---|---|
| CBUAE | AML/CFT (PEP screening, beneficial ownership), open banking compliance, correspondent banking |
| SAMA | Cybersecurity (active fines), open banking readiness, consumer protection in lending |
| DFSA | AML for designated non-financial businesses, crypto/virtual asset firms, fund governance |
| VARA | Marketing compliance, licensing completeness, custody requirements |
| SDAIA | Data subject rights, cross-border data transfers, consent management |
| FSRA | Fund domiciliation, AML for regulated activities, corporate governance |
| CBE (Egypt) | AML/CFT (FATF action plan), foreign exchange compliance |
| BDL | Capital controls compliance, reporting obligations (limited enforcement capacity) |

### Factor 2 — Severity of the gap

Score 1–5:

| Score | Gap type |
|---|---|
| 5 | Complete absence of a required control (no policy, no process, no evidence) |
| 4 | Policy exists but is not implemented or monitored |
| 3 | Policy implemented but with documented deficiencies |
| 2 | Procedural gap only; substantive control is in place |
| 1 | Technical or documentation gap; substantive compliance is present |

### Factor 3 — Company profile (visibility and risk)

Score 1–5:

| Score | Company profile |
|---|---|
| 5 | Large, systemically important, publicly listed, or recently acquired entity |
| 4 | Mid-size licensed institution with significant retail customer base |
| 3 | Standard licensed entity; no special risk factors |
| 2 | Small or niche entity; limited regulatory interface |
| 1 | Non-regulated or minimally regulated entity |

### Factor 4 — Recent inspection and enforcement history

| Factor | Score modifier |
|---|---|
| Entity was inspected within 12 months and gap was flagged | +2 |
| Entity received a formal regulatory warning in past 24 months | +2 |
| Entity proactively disclosed the gap to the regulator | -2 |
| Industry peers have been publicly sanctioned for same gap | +1 |
| No prior enforcement history for this entity | 0 |
| Voluntary remediation is demonstrably underway | -1 |

## Composite Score and Risk Tier

```
Enforcement Likelihood Score = (Factor1 × 0.35) + (Factor2 × 0.30) + (Factor3 × 0.20) + Factor4 modifier
```

| Score range | Risk tier | Recommended action |
|---|---|---|
| 4.0–5.0 | CRITICAL | Remediate immediately; consider proactive regulator engagement; engage outside counsel |
| 3.0–3.9 | HIGH | Remediate within 60 days; monitor regulator publications closely |
| 2.0–2.9 | MEDIUM | Include in next compliance cycle; document interim controls |
| 1.0–1.9 | LOW | Address in annual compliance program review |
| Below 1.0 | MINIMAL | Note and monitor; no immediate action required |

## Output

```markdown
## Enforcement Likelihood Assessment — [Client] — [Date]

### Gap assessed: AML/CFT — PEP Enhanced Due Diligence

**Jurisdiction**: UAE
**Regulator**: CBUAE
**Domain**: AML/CFT

| Factor | Score | Rationale |
|---|---|---|
| Regulator focus intensity | 5 | CBUAE conducted 14 public AML enforcement actions in 2024; PEP screening is a stated priority |
| Gap severity | 4 | Policy exists but PEP screening is not consistently applied; no documented escalation process |
| Company profile | 3 | Mid-size licensed payment institution |
| Enforcement history modifier | +1 | A peer institution was publicly fined in 2024 for the same gap |

**Composite score**: (5×0.35) + (4×0.30) + (3×0.20) + 1 = 1.75 + 1.20 + 0.60 + 1 = **4.55**

**Risk tier: CRITICAL**

**Recommended actions**:
1. Appoint a senior owner for PEP screening remediation immediately
2. Implement interim manual screening controls within 2 weeks
3. Complete automated PEP screening solution implementation within 8 weeks
4. Consider proactive disclosure to CBUAE if inspection is imminent — CBUAE has granted credit for voluntary remediation in past cases
5. Engage AML outside counsel to review the remediation plan

**Enforcement scenario**: If inspected today with this gap unaddressed, enforcement action probability is HIGH. Typical CBUAE sanction for AML deficiencies: formal warning + remediation notice (first occurrence); administrative fine (repeat or egregious); in extreme cases, license conditions.
```

## Jurisdictional Enforcement Patterns

### CBUAE (UAE)
Publicly publishes enforcement actions. AML fines are the primary enforcement tool. License suspension is rare but available. Cooperative entities that remediate quickly typically receive more favorable treatment. Consent orders and undertakings are accepted.

### SAMA (KSA)
Public enforcement actions in cybersecurity and consumer protection have increased since 2022. SAMA can suspend licenses, impose fines, and require management changes. Saudi enforcement is less publicly visible than UAE but fines are significant (in millions of SAR for major institutions).

### DFSA (DIFC)
Common-law enforcement model. DFSA issues public notices of enforcement action. Financial penalties + public censure are most common. License withdrawal is available for serious breaches. DFSA has a formal settlements process that incentivizes early resolution.

### VARA (Dubai)
Relatively new regulator (established 2022). Early enforcement is primarily focused on unlicensed activity and marketing compliance violations. Expect enforcement to become more systematic as the regulatory framework matures.

### SDAIA (KSA) / PDPL
The PDPL enforcement regime is in early stages (law effective March 2024). Initial enforcement is likely to focus on the most visible violators and systemic non-compliance. Organizations with large Saudi customer data footprints are highest-risk.

### BDL (Lebanon)
Enforcement capacity is significantly constrained by the ongoing economic and political crisis. Regulatory obligations remain in force legally, but practical enforcement is reduced. However, FATF grey-listing risk for Lebanon creates pressure for documented compliance regardless of local enforcement.

## Related Skills

- [[pa-workflow-regulatory-compliance-gap-matrix]]
- [[pa-workflow-regulatory-cross-jurisdiction-tracker]]
- [[pa-workflow-regulatory-client-alert-drafter-firm-voice]]
- [[pa-workflow-regulatory-daily-digest-publisher]]
