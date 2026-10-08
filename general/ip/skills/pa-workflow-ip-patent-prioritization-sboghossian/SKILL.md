---
name: pa-workflow-ip-patent-prioritization-sboghossian
title: IP — Patent Prioritization
description: Use when an IP team or lawyer needs to systematically prioritize which inventor disclosures to file as patents. Orchestrates novelty screening, commercial value estimation, geographic filing strategy, deadline management, and cost-benefit analysis across MENA (UAE, KSA, LB, EG) and major PCT jurisdictions. Triggers on inventor disclosure submissions, GitHub commits, Drive documents, or Slack discussions flagged for IP review.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-ip-patent-prioritization
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP — Patent Prioritization

## Purpose

Patent filing resources are finite. This workflow converts a raw queue of inventor disclosures into a ranked, decision-ready priority list. It outputs a scored matrix that an IP counsel can bring to the patent committee or present to management within one working day of receiving disclosures.

## Inputs / Signals

| Input | Required | Notes |
|---|---|---|
| Inventor disclosure(s) | Yes | Free text, form, GitHub commit message, Slack thread, or Drive doc |
| Company product roadmap | Recommended | Needed for commercial value scoring |
| Existing patent portfolio summary | Recommended | Avoid filing over already-protected ground |
| Filing budget (annual / per-disclosure cap) | Optional | Enables hard cost-benefit cutoff |
| Target markets | Optional | Defaults to US + EP + WO (PCT) + home jurisdiction |
| Urgency flags | Optional | Any known publication dates, conference talks, or prior disclosures by third parties |

## Logic

### Step 1 — Intake and normalization

Parse each disclosure into structured fields:
- Inventor(s) name and employment status (confirms assignment chain)
- Date of first reduction to practice (or earliest verifiable date)
- Technical domain (hardware, software, chemistry, method, design)
- Claim candidates — what is new and non-obvious? Extract in plain language
- Existing publications or prior disclosures (inventor's own publications count as prior art after 12 months in US, immediately in most non-grace-period jurisdictions)

### Step 2 — Novelty preliminary check

Perform a fast prior-art screen (see [[pa-workflow-ip-prior-art-search-orchestrator]] for the full search; this step is a 15-minute triage):
- Run claims against USPTO, EPO Espacenet, and WIPO PatentScope full-text search
- Flag: clearly anticipated (stop), likely novel (proceed), uncertain (escalate)
- Note: UAE, KSA, and other GCC patent offices examine under Paris Convention and PCT rules; a disclosure that clears US/EP almost always clears GCC

### Step 3 — Commercial value estimate

Score 1–10 on three axes:
1. **Revenue protection**: does this invention read on a current or planned revenue line?
2. **Blocking value**: does it foreclose a competitor from copying a key feature?
3. **Licensing / monetization**: is there a realistic third-party licensing market?

Flag if: the invention relates to core product differentiation (high priority regardless of cost), or if it is a "me-too" feature with no blocking value (consider trade secret instead).

### Step 4 — Filing deadline urgency

| Event | Deadline impact |
|---|---|
| Public disclosure (talk, publication, demo) | 12-month grace period in US; no grace in EP/MENA — file **before** disclosure |
| Provisional filed (US) | 12 months to convert to non-provisional or PCT |
| PCT filing (WO) | 18–30 months national phase deadline per jurisdiction |
| Priority application filed | 12-month Paris Convention priority window |

Flag any disclosure already past the grace period for non-US jurisdictions — EP, UAE (via UAE Patent Office / ESMA), KSA (SAIP), LB (via IDAL/Ministry of Economy) — as these require immediate attention or waiver of those jurisdictions.

### Step 5 — Geographic coverage strategy

Default filing strategy by tier:

| Tier | Jurisdictions | When to use |
|---|---|---|
| Core | US + EP + PCT | Almost all commercially significant inventions |
| MENA add-on | UAE, KSA, EG | If company sells or manufactures in the region |
| GCC block | UAE, KSA, BH, OM, QA, KW | Use GCC Patent Office (GCCPO) for a single application covering all 6 |
| Lebanon | LB via IDAL | Manufacturing or origin marks only; enforcement is weak |
| Selective | JP, CN, IN, KR | Only if prior-art search and product road map justify cost |

Note: UAE is a signatory to the Paris Convention and PCT. KSA joined PCT in 2013. Egypt joined in 2003. Lebanon is a Paris Convention signatory but not PCT — file nationally via the Lebanese Industrial Property Office.

### Step 6 — Cost-benefit analysis

Estimate total cost per disclosure:
- Prosecution cost (drafting + filing fees, country by country)
- Maintenance fees over 10-year horizon
- Expected revenue protection value (discounted)
- Probability of grant (high for hardware/method, lower for software-heavy in EP and MENA)

Output: **net present value estimate** and recommendation (file / defer / trade-secret / abandon).

## Output

```json
{
  "prioritized_queue": [
    {
      "disclosure_id": "INV-2025-042",
      "title": "Adaptive rate-limiting algorithm for API throttling",
      "score": {
        "novelty": "likely_novel",
        "commercial_value": 8,
        "urgency": "immediate",
        "blocking_value": 7
      },
      "recommended_filing": ["US", "EP", "PCT", "UAE", "KSA"],
      "deadline": "2025-09-01",
      "estimated_cost_usd": 32000,
      "recommendation": "FILE — core product protection, revenue-generating feature"
    }
  ],
  "deferred": [...],
  "trade_secret_candidates": [...],
  "abandoned": [...]
}
```

## Jurisdictional Notes

- **UAE**: File with UAE Ministry of Economy IP Department or through ESMA. PCT national phase: 20 months from PCT filing. Examination is substantive.
- **KSA**: File with Saudi Authority for Intellectual Property (SAIP). Software patents are restrictive — method claims preferred over system claims for software-heavy inventions.
- **Egypt**: Egyptian Patent Office (EGYPO). Paris Convention only (not PCT). 20-year term. Software and business-method patents are difficult.
- **Lebanon**: Lebanese Ministry of Economy, Directorate of Industrial Property. No PCT. 15-year term. Enforcement is unreliable — trade secret may be preferable.
- **DIFC / ADGM**: These free zones do not have their own patent systems; patents are registered at the UAE national level and apply territory-wide.
- **GCC Patent Office (GCCPO)**: Single filing covers all 6 GCC states. Examination modeled on EPO. Highly cost-effective for regional coverage.
- **Grace period trap**: Unlike the US, most MENA and European jurisdictions have no inventor grace period. Any public disclosure before filing destroys patentability in EP, UAE, KSA, and EG.

## Common Mistakes

- Filing US only and missing the 12-month Paris window for MENA markets
- Treating software inventions as unpatentable in all MENA jurisdictions — method-of-operating-a-system claims often pass examination
- Failing to assign rights from inventors before filing (especially contractors and seconded employees)
- Missing the GCC Patent Office as a single-application path to six markets
- Confusing trade-secret and patent strategies — inventions that are reverse-engineerable need patent protection; non-observable processes can be kept secret

## Related Skills

- [[pa-workflow-ip-prior-art-search-orchestrator]]
- [[review-ip-freedom-to-operate]]
- [[kb-ip-patent-prosecution-mena]]
- [[draft-patent-provisional]]
- [[pa-workflow-transactional-deal-point-analysis]]
