---
name: uk-employment-statute-anchors
created: 2026-05-03
retrieved: 2026-05-03
refresh_recommended_by: 2027-05-03
status: source-verified
audience: /slo-hire, /slo-legal, /slo-accounting
purpose: |
  Verbatim UK employment-law anchors for advisor skills. Skills cite this
  file instead of paraphrasing statute from model memory.
---

# UK employment statute anchors

These are short quote anchors, not legal advice. Every downstream advisor skill must preserve the `source_url`, `last_checked`, and `quoted_text` provenance when relying on these sections.

## IANA 2006 s15 — right-to-work civil penalty surface

- authority: Immigration, Asylum and Nationality Act 2006, section 15
- source_url: https://www.legislation.gov.uk/ukpga/2006/13/section/15
- data_url: https://www.legislation.gov.uk/ukpga/2006/13/section/15/data.xml
- last_checked: 2026-05-03
- quoted_text: "It is contrary to this section to employ an adult subject to immigration control if"
- advisor_use: `/slo-hire` right-to-work warning and lawyer/accountant routing for immigration-risk hiring.

## ERA 1996 s86 — statutory minimum notice

- authority: Employment Rights Act 1996, section 86
- source_url: https://www.legislation.gov.uk/ukpga/1996/18/section/86
- data_url: https://www.legislation.gov.uk/ukpga/1996/18/section/86/data.xml
- last_checked: 2026-05-03
- quoted_text: "is not less than one week's notice if his period of continuous employment is less than two years"
- advisor_use: `/slo-hire` employment-contract termination and offer-letter triage.

## Pensions Act 2008 s3 — automatic enrolment trigger

- authority: Pensions Act 2008, section 3
- source_url: https://www.legislation.gov.uk/ukpga/2008/30/section/3
- data_url: https://www.legislation.gov.uk/ukpga/2008/30/section/3/data.xml
- last_checked: 2026-05-03
- quoted_text: "This section applies to a jobholder"
- advisor_use: `/slo-hire` and `/slo-accounting` workplace-pension routing.

## Equality Act 2010 s4 — protected characteristics

- authority: Equality Act 2010, section 4
- source_url: https://www.legislation.gov.uk/ukpga/2010/15/section/4
- data_url: https://www.legislation.gov.uk/ukpga/2010/15/section/4/data.xml
- last_checked: 2026-05-03
- quoted_text: "The following characteristics are protected characteristics"
- advisor_use: `/slo-hire` interview rubric, offer, onboarding, and discrimination-risk triage.

## ITEPA 2003 Part 2 Chapter 10 — off-payroll working

- authority: Income Tax (Earnings and Pensions) Act 2003, Part 2 Chapter 10
- source_url: https://www.legislation.gov.uk/ukpga/2003/1/part/2/chapter/10
- data_url: https://www.legislation.gov.uk/ukpga/2003/1/part/2/chapter/10/data.xml
- last_checked: 2026-05-03
- quoted_text: "Workers' services provided through intermediaries to public authorities or medium or large clients"
- advisor_use: `/slo-hire` contractor/SOW IR35 routing and `/slo-accounting` PAYE/NI warning surface.

## Refresh discipline

- warn_after: 2027-05-03
- refuse_after: 2028-05-03
- refresh_source_order: legislation.gov.uk data endpoint first, then GOV.UK/HMRC guidance where statute text points to operational guidance.
