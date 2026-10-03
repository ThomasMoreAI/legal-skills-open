---
name: uk-consumer-statute-anchors
created: 2026-05-03
retrieved: 2026-05-03
refresh_recommended_by: 2027-05-03
status: source-verified
audience: /slo-legal, /slo-marketing, /slo-pricing
purpose: |
  Verbatim UK consumer-law anchors for founder-advice artifacts. This file
  is a provenance layer, not legal advice.
---

# UK consumer statute anchors

Every quote below was checked against the linked primary or official source on 2026-05-03. Skills cite these anchors by section name instead of restating consumer law from memory.

## Consumer Rights Act 2015 s49 — reasonable care and skill

- authority: Consumer Rights Act 2015, section 49
- source_url: https://www.legislation.gov.uk/ukpga/2015/15/section/49
- data_url: https://www.legislation.gov.uk/ukpga/2015/15/section/49/data.xml
- last_checked: 2026-05-03
- quoted_text: "the trader must perform the service with reasonable care and skill"
- advisor_use: B2C service terms, SaaS service obligations, and `/slo-pricing` cancellation/refund warning surfaces.

## Consumer Contracts Regulations 2013 reg 29 — right to cancel

- authority: Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013, regulation 29
- source_url: https://www.legislation.gov.uk/uksi/2013/3134/regulation/29
- data_url: https://www.legislation.gov.uk/uksi/2013/3134/regulation/29/data.xml
- last_checked: 2026-05-03
- quoted_text: "The consumer may cancel a distance or off-premises contract at any time in the cancellation period"
- advisor_use: B2C distance/off-premises cancellation triage.

## Consumer Contracts Regulations 2013 reg 30 — normal cancellation period

- authority: Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013, regulation 30
- source_url: https://www.legislation.gov.uk/uksi/2013/3134/regulation/30
- data_url: https://www.legislation.gov.uk/uksi/2013/3134/regulation/30/data.xml
- last_checked: 2026-05-03
- quoted_text: "the cancellation period ends at the end of 14 days after the day on which the contract is entered into"
- advisor_use: `/slo-legal` and `/slo-pricing` cooling-off-period warnings.

## DMCC 2024 — consumer protection and subscription context

- authority: Digital Markets, Competition and Consumers Act 2024
- source_url: https://www.legislation.gov.uk/ukpga/2024/13/contents
- data_url: https://www.legislation.gov.uk/ukpga/2024/13/contents/data.xml
- last_checked: 2026-05-03
- quoted_text: "to make provision relating to the protection of consumer rights and to confer further such rights"
- advisor_use: `/slo-marketing` and `/slo-pricing` B2C subscription, renewal, and consumer-protection routing.

## Refresh discipline

- warn_after: 2027-05-03
- refuse_after: 2028-05-03
- refresh_source_order: legislation.gov.uk section/data endpoints first; GOV.UK regulator guidance only for operational interpretation.
