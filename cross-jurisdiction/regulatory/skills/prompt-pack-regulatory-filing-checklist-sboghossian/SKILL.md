---
name: prompt-pack-regulatory-filing-checklist-sboghossian
title: Regulatory Filing Checklist
description: Use when a company secretary, compliance officer, or lawyer needs a comprehensive checklist of regulatory filings required for a specific entity type in one or more jurisdictions. Covers annual filings, change notifications, beneficial ownership disclosures, financial reporting deadlines, and penalties for late submission. Particularly relevant for companies incorporated in or operating through UAE (onshore, DIFC, ADGM), KSA, Lebanon, and Egypt.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-regulatory-filing-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

# Regulatory Filing Checklist

## When to use this

Use this skill when:
- A company secretary or compliance officer needs a master checklist of all regulatory filings due in a given calendar year.
- A new entity has been incorporated and the team needs to understand ongoing filing obligations from day one.
- A company is being audited or is in M&A due diligence and needs to verify that all statutory filings are current.
- A company has recently changed status (e.g., converted from LLC to PJSC, added a new subsidiary, changed its auditor) and needs to understand the change-notification filings triggered.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Entity type** | LLC, PJSC, free-zone company, branch, partnership, foundation — each has distinct obligations | Ask before drafting |
| **Jurisdiction(s) of incorporation and operation** | Filing obligations differ materially across UAE onshore, DIFC, ADGM, KSA, LB, EG | Ask; do not assume |
| **Licensed activities** | Financial services, healthcare, and real estate companies have sector-specific filing obligations in addition to corporate filings | Ask if regulated sector |
| **Financial year-end** | Determines specific calendar deadlines for accounts filing and tax returns | Default: 31 December; adjust if different |

## Optional inputs

- **Beneficial ownership (UBO) profile** — needed to assess UBO register obligations across jurisdictions.
- **Group structure** — parent company or subsidiaries can trigger consolidated reporting obligations.
- **Current compliance status** — whether any filings are overdue (affects urgency prioritization).

## Document structure (checklist output)

The checklist should be organized as a table or structured list with the following columns:
- **Filing / Notification type**
- **Regulatory authority**
- **Deadline** (specific date or trigger event + window)
- **Frequency** (annual, biannual, event-triggered)
- **Responsible party** (company secretary, CFO, legal counsel)
- **Penalty for late/non-filing**
- **Status** (to be completed by the client)

### UAE — Onshore LLC / Mainland Company

| Filing | Authority | Deadline | Penalty Reference |
|---|---|---|---|
| Trade licence renewal | DED / relevant emirate authority | Annual; before expiry date | Varies; AED 250–1,000+ per day late |
| Annual return / financial statements filing | MoE (Ministry of Economy) / Commercial Register | Within 1 month of AGM; AGM within 4 months of financial year-end | UAE Commercial Companies Law |
| Ultimate Beneficial Owner (UBO) register | MoE | Within 60 days of incorporation; updates within 15 days of change | Cabinet Resolution No. 58 of 2020; penalties up to AED 100,000 |
| Real Beneficiary Register | MoE | Same as UBO | — |
| Audit appointment notification | — | Annual; before year-end | Requirement under Commercial Companies Law |
| Change of directors notification | Commercial Register | Within 15 days of change | — |
| Change of address / registered office | Commercial Register / DED | Within 30 days | — |
| VAT return | FTA (Federal Tax Authority) | Monthly or quarterly (based on threshold) | Penalty: 2% of unpaid VAT immediately; additional 4% if unpaid after 7 days |
| Corporate Tax return | FTA | Within 9 months of financial year-end | Corporate Tax Law (effective June 2023) |
| MOHRE Wage Protection System (WPS) | MOHRE | Monthly | Suspension of new work permit applications |
| Workmen's Compensation Insurance renewal | MOHRE | Annual | — |

### DIFC

| Filing | Authority | Deadline | Penalty |
|---|---|---|---|
| Annual return | DIFC Registrar of Companies | Within 2 months of anniversary of incorporation | USD 500–5,000 |
| Financial statements | DIFC Registrar | Within 6 months of financial year-end | — |
| UBO / Beneficial Ownership Register | DIFC Registrar | Maintain and update within 14 days of change | — |
| Director / officer changes | DIFC Registrar | Within 14 days | — |
| Auditor appointment | DIFC Registrar | Annual (for regulated entities: also DFSA notification) | — |
| DFSA regulatory return | DFSA | Quarterly / annual depending on license category | DFSA Rules |
| AML/CFT annual compliance report | DFSA | Annual | DFSA AML Module |

### ADGM

| Filing | Authority | Deadline | Penalty |
|---|---|---|---|
| Annual return | ADGM Registration Authority | Within 2 months of anniversary | USD 250+ |
| Financial statements | ADGM RA | Within 6 months of year-end | — |
| Beneficial ownership register | ADGM RA | Within 14 days of change | — |
| FSRA regulatory return | FSRA | Quarterly / annual per license | FSRA Rules |
| AML/CFT report | FSRA | Annual | FSRA AML Rulebook |

### KSA

| Filing | Authority | Deadline | Penalty |
|---|---|---|---|
| Commercial Register renewal | Ministry of Commerce | Annual | SAR 500–5,000 |
| Zakat / Tax return | ZATCA | Within 120 days of financial year-end for zakat; VAT quarterly | Late-filing penalties apply |
| GOSI (social insurance) employer registration and monthly contributions | GOSI | Monthly | 2% monthly on outstanding amounts |
| Saudization (Nitaqat) report | HRSD | Quarterly | Risk of licence suspension |
| CMA regulatory filing (listed companies) | CMA | Semi-annual and annual financial reports | CMA Listing Rules |
| SAMA prudential return (financial institutions) | SAMA | As specified per licence | SAMA Instructions |
| UBO / Beneficial Ownership | Ministry of Commerce | Within 30 days of establishment; updates within 15 days | — |

### Lebanon

| Filing | Authority | Deadline | Notes |
|---|---|---|---|
| SAL / SARL annual general meeting | Commercial Register, Ministry of Justice | Within 4 months of year-end | Lebanese Commercial Code Art. 197 |
| Financial statements filing | Commercial Register | After AGM approval | — |
| Syndic des experts-comptables (audit) | — | Mandatory for SAL; optional for SARL below threshold | — |
| NSSF (social security) employer declarations | NSSF | Monthly / annual | Lebanese Labour Law |
| Income tax return | Ministry of Finance | Within 75 days of year-end | — |

### Egypt

| Filing | Authority | Deadline | Penalty |
|---|---|---|---|
| Annual financial statements | Egyptian Companies Registry (GAFI / MCDR) | Within 3 months of year-end | EGP 5,000–50,000 |
| General assembly minutes filing | Companies Registry | Within 15 days of meeting | — |
| Beneficial ownership declaration | Egyptian Money Laundering Combating Unit (EMLCU) | At incorporation; updates within 15 days | — |
| Tax return | Egyptian Tax Authority | Within 4 months of year-end | 2% penalty of unpaid tax per month |
| Social insurance (NRISC) | Social Insurance Authority | Monthly | — |

## Drafting standards

- Present the checklist as a live document the client can fill in and use as a compliance tracker.
- Always note: "Deadlines are subject to change by regulatory circular; verify with official sources before use."
- Add a "Last verified" date to the checklist so the client knows when it was prepared.
- Flag entries where the penalty for non-compliance is particularly severe or where late filing triggers automatic licence suspension.
- For regulated entities (financial services, healthcare, real estate), include a note that sector-specific filings are not exhaustive in the corporate filing checklist — a separate sector compliance calendar is needed.

## Common mistakes

- **Treating free zone and mainland deadlines as identical.** DIFC, ADGM, DMCC, JAFZA each have their own registrar and their own deadlines — do not consolidate.
- **Missing UBO / beneficial ownership register obligations.** These are frequently overlooked and carry significant penalties across all MENA jurisdictions.
- **Assuming the same financial year-end across jurisdictions.** A group may have different year-ends in different jurisdictions; verify per entity.
- **Omitting sector-specific filings.** A corporate checklist covers Companies Law obligations; a bank, insurance company, or listed entity has a separate layer of prudential / market-conduct filings.

## Related skills

- [[prompt-pack-regulatory-change-impact-assessment]]
- [[prompt-pack-shareholders-resolution]]
- [[prompt-pack-related-party-transaction-policy]]
- [[prompt-pack-share-purchase-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
