---
name: hmrc-vcm-index
created: 2026-04-25
retrieved: 2026-05-03
refresh_recommended_by: 2027-05-03
status: source-verified — refreshed for business-skill-improvements M1
audience: /slo-equity (M3) + /slo-fundraise (M4)
purpose: |
  Citation index for HMRC Venture Capital Schemes Manual anchors used by
  /slo-equity and /slo-fundraise when triaging SEIS/EIS qualification.
  Every cited paragraph carries a source URL, retrieval date, and short
  verbatim quote.
sources:
  - https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual
  - https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm34080
  - https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm3000
  - https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm31000
  - https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm33020
  - https://www.gov.uk/guidance/venture-capital-schemes-apply-for-advance-assurance
---

# HMRC Venture Capital Schemes Manual — citation index

> Retrieval date: **2026-05-03**.
> NOT legal / tax advice; NOT a substitute for HMRC guidance or accountant review.
> This file is a citation index summarising the published HMRC manual paragraphs that `/slo-equity` and `/slo-fundraise` cite when triaging SEIS / EIS qualification questions.

## Top retroactive-disqualification triggers

When a founder asks about SEIS / EIS qualification, the advisor skill checks the founder's situation against these triggers before drafting Advance Assurance or term-sheet artifacts. Each trigger fires `gate-1-regulated` (HMRC) and routes to accountant plus specialist lawyer where drafting rights or company-control questions are in scope.

### Trigger 1 — Control / independence requirement (VCM34080)

- authority: VCM34080 — SEIS income tax relief: issuing company: control and independence requirement
- source_url: https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm34080
- last_checked: 2026-05-03
- quoted_text: "There must be no arrangements at any time during period A by virtue of which this test could be breached"
- triage_routing: lawyer (corporate structure) + accountant (tax position)

### Trigger 2 — Company under control of another company (VCM34080)

- authority: VCM34080
- source_url: https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm34080
- last_checked: 2026-05-03
- quoted_text: "The company is not a qualifying company if it is under the control of another company"
- triage_routing: lawyer + accountant

### Trigger 3 — Qualifying-trade drift into excluded activities (VCM3000)

- authority: VCM3000 — Excluded activities: contents
- source_url: https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm3000
- last_checked: 2026-05-03
- quoted_text: "VCM3010 Meaning of 'excluded activities'"
- triage_routing: accountant with specialist VCT/EIS review for borderline cases

### Trigger 4 — SEIS income-tax relief withdrawal/reduction surface (VCM31000)

- authority: VCM31000 — Seed Enterprise Investment Scheme: income tax relief: contents
- source_url: https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm31000
- last_checked: 2026-05-03
- quoted_text: "Withdrawal or reduction of SEIS relief: contents"
- triage_routing: accountant

### Trigger 5 — Abingdon Health marker: preferential share-rights review

- authority: VCM33020 — SEIS: income tax relief: general requirements: shares requirement
- source_url: https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/vcm33020
- last_checked: 2026-05-03
- quoted_text: "A right carried by a share is a preferential right if that right takes priority over a right carried by some other share"
- case_marker: Abingdon Health Limited v HMRC [2016] TC 05525 is retained as a specialist-review marker; this M1 pass did not locate a stable official tribunal/GOV.UK text endpoint for the judgment, so downstream skills must cite the HMRC preferential-rights anchor above as the primary source.
- triage_routing: lawyer (articles/share-rights drafting) + accountant (SEIS/EIS tax impact)

## Advance Assurance — process anchor

- authority: GOV.UK Venture Capital Schemes Advance Assurance guidance
- source_url: https://www.gov.uk/guidance/venture-capital-schemes-apply-for-advance-assurance
- last_checked: 2026-05-03
- advisor_rule: `/slo-fundraise` asks whether Advance Assurance has been applied for before drafting SEIS/EIS-sensitive fundraising artifacts.
- practical_floor: Apply at least 6 weeks before term-sheet signature where SEIS/EIS Advance Assurance affects the fundraising story.

## Triage gate prose for `/slo-fundraise`

When `/slo-fundraise` is invoked for any term-sheet drafting, SAFE math, or pitch narrative, the skill MUST surface these questions before drafting:

1. "Have you applied for Advance Assurance, and if so, when?" If not applied, route to accountant before SEIS/EIS-sensitive drafting.
2. "Are you a 51%-owned subsidiary or controlled by another company / connected persons (VCM34080)?" If yes or unclear, route to lawyer + accountant.
3. "Have you audited your qualifying-trade status against VCM3000 in the last 12 months?" If no, warn and recommend accountant review.
4. "Are any share rights preferential against another class (Abingdon Health marker / VCM33020)?" If yes or unsure, hard-block drafting and route to lawyer.

## What this file is NOT

- NOT legal / tax advice.
- NOT exhaustive on SEIS / EIS qualification.
- NOT a substitute for HMRC's manual or for accountant / specialist advice.

## Refresh cadence

- warn_after: 2027-05-03
- refuse_after: 2028-05-03
- quarterly_check: https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual/updates
- triggered_refresh: Budget statements or HMRC VCM updates affecting SEIS/EIS qualification parameters.
