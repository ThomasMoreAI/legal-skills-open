---
name: uk-marketing-statute-anchors
created: 2026-05-03
retrieved: 2026-05-03
refresh_recommended_by: 2027-05-03
status: source-verified
audience: /slo-marketing, /slo-launch, /slo-sales-funnel, /slo-legal
purpose: |
  Verbatim UK marketing, advertising, and electronic-communications anchors
  for the business skills.
---

# UK marketing statute anchors

This file separates marketing-risk source text from SKILL.md prose. It is not legal advice and does not authorise bypassing `/slo-legal` gate-4 routing for GDPR/PECR matters.

## CAP Code / ASA — non-broadcast advertising code

- authority: Advertising Standards Authority / CAP non-broadcast code
- source_url: https://www.asa.org.uk/codes-and-rulings/advertising-codes/non-broadcast-code.html
- last_checked: 2026-05-03
- quoted_text: "Rules relating to social responsibility; legality and fair competition"
- advisor_use: `/slo-marketing` and `/slo-launch` ad-copy risk warnings. `asa` is medium-confidence in the regulator enum because this is self-regulatory rather than a direct statute row.

## PECR 2003 reg 22 — email direct marketing consent

- authority: Privacy and Electronic Communications (EC Directive) Regulations 2003, regulation 22
- source_url: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22
- data_url: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22/data.xml
- last_checked: 2026-05-03
- quoted_text: "This regulation applies to the transmission of unsolicited communications by means of electronic mail to individual subscribers"
- advisor_use: `/slo-marketing`, `/slo-sales-funnel`, and `/slo-legal` direct-marketing routing.

## PECR 2003 reg 22 — soft opt-in conditions

- authority: Privacy and Electronic Communications (EC Directive) Regulations 2003, regulation 22
- source_url: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22
- data_url: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22/data.xml
- last_checked: 2026-05-03
- quoted_text: "the direct marketing is in respect of that person's similar products and services only"
- advisor_use: `/slo-sales-funnel` cold/warm email distinction and DPO routing.

## DUAA 2025 schedule 13 — PECR enforcement powers

- authority: Data (Use and Access) Act 2025, Schedule 13
- source_url: https://www.legislation.gov.uk/ukpga/2025/18/schedule/13
- data_url: https://www.legislation.gov.uk/ukpga/2025/18/schedule/13/data.xml
- last_checked: 2026-05-03
- quoted_text: "the maximum amount of the penalty that may be imposed by a penalty notice is the higher maximum amount"
- cross_reference: Data Protection Act 2018 s157 defines the higher maximum amount.
- advisor_use: `/slo-marketing` B2C direct marketing and `/slo-legal` PECR risk triage.

## DPA 2018 s157 — higher maximum amount

- authority: Data Protection Act 2018, section 157
- source_url: https://www.legislation.gov.uk/ukpga/2018/12/section/157
- data_url: https://www.legislation.gov.uk/ukpga/2018/12/section/157/data.xml
- last_checked: 2026-05-03
- quoted_text: "£17,500,000 or 4% of the undertaking's total annual worldwide turnover"
- advisor_use: PECR penalty ceiling explanation when DUAA schedule 13 points PECR penalties at the higher maximum amount.

## Refresh discipline

- warn_after: 2027-05-03
- refuse_after: 2028-05-03
- refresh_source_order: legislation.gov.uk, ICO, ASA/CAP for code text, then other official regulator pages.
