---
name: ico-duaa-index
created: 2026-04-25
retrieved: 2026-05-03
refresh_recommended_by: 2027-05-03
status: source-verified — refreshed for business-skill-improvements M1
source_primary: https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/
source_statute: https://www.legislation.gov.uk/ukpga/2025/18
purpose: |
  Snapshot of the UK Data (Use and Access) Act 2025 commencement timeline,
  PECR changes, and ICO-routing implications. This file is a citation index,
  not legal advice.
---

# DUAA 2025 — commencement timeline + key changes

> Retrieval date: **2026-05-03**.
> Primary statute: https://www.legislation.gov.uk/ukpga/2025/18.
> Operational regulator source: ICO DUAA summary page.

## Commencement anchors

### Royal Assent

- authority: Data (Use and Access) Act 2025
- source_url: https://www.legislation.gov.uk/ukpga/2025/18
- data_url: https://www.legislation.gov.uk/ukpga/2025/18/contents/data.xml
- last_checked: 2026-05-03
- quoted_text: "An Act to make provision about access to customer data and business data"
- event_date: 2025-06-19

### ICO Stage 3 summary date

- authority: ICO DUAA summary of changes
- source_url: https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/
- last_checked: 2026-05-03
- quoted_text: "Stage 3"
- event_date: 2026-02-05
- commencement_note: Retained for compatibility with the existing biz-pack DUAA date test; section-level statute anchors remain the primary authority where legislation.gov.uk exposes commencement effects.

### DUAA s142 commencement power

- authority: Data (Use and Access) Act 2025, section 142
- source_url: https://www.legislation.gov.uk/ukpga/2025/18/section/142
- data_url: https://www.legislation.gov.uk/ukpga/2025/18/section/142/data.xml
- last_checked: 2026-05-03
- quoted_text: "this Act comes into force on such day as the Secretary of State may by regulations appoint"
- commencement_note: Section 142 itself is in force at Royal Assent; later provisions depend on commencement regulations.

### DUAA Stage 6 / complaints-related commencement

- authority: Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026
- source_url: https://www.legislation.gov.uk/uksi/2026/82/regulation/3
- cross_reference: https://www.legislation.gov.uk/ukpga/2025/18/contents/data.xml
- last_checked: 2026-05-03
- quoted_text: "Date=\"2026-06-19\" Qualification=\"wholly in force\""
- commencement_note: The legislation.gov.uk effects metadata records 2026-06-19 commencement for Schedule 10 paragraphs and section 103-related commencement rows.

## Key changes for advisor routing

### PECR direct-marketing charity soft opt-in

- authority: PECR 2003 regulation 22 as amended by DUAA 2025
- source_url: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22
- data_url: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22/data.xml
- last_checked: 2026-05-03
- quoted_text: "A charity may send or instigate the sending of electronic mail for the purposes of direct marketing"
- advisor_use: `/slo-marketing` must still route direct-marketing implementation questions through `/slo-legal`/DPO review.

### PECR penalty ceiling alignment

- authority: DUAA 2025 Schedule 13 and Data Protection Act 2018 section 157
- source_url: https://www.legislation.gov.uk/ukpga/2025/18/schedule/13
- cross_reference: https://www.legislation.gov.uk/ukpga/2018/12/section/157
- last_checked: 2026-05-03
- quoted_text: "the maximum amount of the penalty that may be imposed by a penalty notice is the higher maximum amount"
- penalty_ceiling_quote: "£17,500,000 or 4% of the undertaking's total annual worldwide turnover"
- short_ceiling_label: "£17.5M / 4% global turnover"
- advisor_use: `/slo-legal` and `/slo-marketing` must not downplay PECR risk for email/SMS/push-notification campaigns.

## What this file is NOT

- NOT legal advice.
- NOT authorization to relax the broad GDPR hard-block on `draft` mode.
- NOT exhaustive on DUAA provisions.

## Refresh cadence

- warn_after: 2027-05-03
- refuse_after: 2028-05-03
- triggered_refresh: new ICO DUAA guidance, new commencement regulations, or PECR enforcement guidance updates.
