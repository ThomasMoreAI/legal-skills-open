---
name: prompt-pack-annual-report-governance-section-sboghossian
title: Annual Report Governance Section
description: Use when drafting the corporate governance section of a company's annual report, covering board composition, committee activities, director attendance, remuneration policy, risk management, shareholder engagement, and compliance with the applicable governance code. Corporate governance practice area; relevant to listed companies and regulated entities across MENA and global jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-annual-report-governance-section
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: corporate
language: en
---

# Annual Report Governance Section

## When to use this

Use this skill when preparing the **corporate governance section** of a company's annual report or annual disclosure document. This is a mandatory disclosure for:
- Listed companies (stock exchange requirements)
- Regulated entities (banking, insurance, financial services)
- State-owned enterprises (government reporting requirements in MENA)
- Companies following a voluntary governance code

The governance section is a narrative disclosure — not a legal agreement — but it carries legal and regulatory significance: false or misleading statements expose directors and the company to liability.

---

## Prompt template

> Draft the corporate governance section of [Company's] annual report covering board composition, committee activities, director attendance, remuneration policy, risk management, shareholder engagement, and compliance with [governance code].

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Company name and jurisdiction of listing/regulation | Determines applicable governance code and disclosure requirements |
| Board composition (names, independence status, committee memberships) | Core disclosure content |
| Applicable governance code | DFM/ADX Governance Code; DIFC Companies Law; UK Corporate Governance Code; etc. |
| Reporting period | Year-end date; board meeting dates |
| Committee activities summary | What each committee did during the year |
| Director attendance records | Required disclosure in all MENA governance codes |
| Remuneration policy and actual remuneration | Disclosed at varying levels of detail by jurisdiction |

---

## Document structure

### 1. Introduction — governance overview
- Board's statement on the company's commitment to corporate governance
- Reference to the applicable governance code(s)
- Statement of compliance or "comply-or-explain"
- Any material changes to governance structure during the year

### 2. Board composition and independence

#### 2.1 Board size and diversity
- Number of directors (executive, non-executive, independent non-executive)
- Gender and nationality composition (increasingly required as a disclosure)
- Skills matrix: a table showing the skills and experience each director brings

#### 2.2 Independence assessment
- Criteria for independence applied (refer to the code or articles)
- Identify which directors are independent
- Disclose any relationships or interests that were considered but did not impair independence
- In MENA contexts: majority-government-owned companies or family-controlled companies have specific challenges with independence; disclose the ownership structure and explain how board independence is maintained

#### 2.3 Board tenure
- Date of appointment for each director
- Re-election schedule and rotation policy

### 3. Board meetings and attendance

Disclose per director:
- Number of meetings held during the year
- Number of meetings attended
- Attendance percentage

Present as a table. Directors with attendance below 75% should be flagged and explained.

### 4. Board committees

For each committee (typically Audit, Remuneration/Compensation, Nomination, Risk):
- Name and composition (chair + members; indicate independence)
- Terms of reference / charter summary
- Meetings held and attendance
- Key activities during the year (3–5 bullet points of substantive matters addressed)
- Any significant recommendations made to the board

See [[prompt-pack-board-committee-charter]] for committee charter drafting.

### 5. Remuneration policy and disclosure

Disclosure depth varies significantly by jurisdiction:

| Jurisdiction | Disclosure requirement |
|-------------|----------------------|
| UAE (DFM/ADX listed) | Aggregate director remuneration; individual disclosure for executive directors; Emirates Securities & Commodities Authority (SCA) Governance Code |
| DIFC companies | DIFC Companies Law disclosure; Companies Regulations |
| UK listed | Directors' Remuneration Report (statutory; audited); individual total remuneration for each director |
| KSA (Tadawul listed) | Corporate Governance Regulations (CMA): aggregate and per-director disclosure; related party transactions |
| Egypt (EGX listed) | EGX Governance Code disclosure; EFSA rules |

Contents of remuneration section:
- Remuneration policy principles (how remuneration is set; link to performance; long-term incentives)
- Summary of remuneration components (base salary / fees, short-term bonus, long-term incentives, benefits, pension)
- Aggregate total remuneration for the year (all directors; often also top executives)
- Individual disclosure where required
- Any changes to remuneration policy during the year

### 6. Risk management and internal controls
- Overview of the company's risk management framework
- Role of the board in risk oversight (vs. management's role)
- Key risks identified and how they are managed (headline categories only in governance section; detail in strategic report or risk section)
- Internal audit: confirmation that internal audit function exists; report to Audit Committee
- External auditor: appointment; independence; key audit matters
- Statement on internal control effectiveness (often a formal board statement required under UK Code, SCA Code, etc.)

### 7. Shareholder engagement
- Annual general meeting: date held; key resolutions voted on; any significant opposition
- Other shareholder communication during the year (investor days, results presentations)
- Significant shareholders: disclosure of major shareholdings above threshold (UAE: 5% under SCA rules; UK: 3% under Disclosure Guidance and Transparency Rules)
- Engagement with institutional shareholders on governance matters

### 8. Related party transactions
- Summary of material related-party transactions during the year
- Board process for approving related-party transactions (conflict of interest management)
- Reference to notes in the financial statements for full disclosure

### 9. Compliance statement
- Statement of compliance with the applicable governance code
- Table of comply-or-explain: where the company has not complied with specific code provisions, explain the reason and describe alternative arrangements

---

## Jurisdictional notes

### UAE — SCA Corporate Governance Code
The Securities and Commodities Authority has issued a corporate governance code applicable to listed joint-stock companies. Key requirements: board independence (minimum one-third independent); mandatory audit, remuneration, and nomination committees; annual governance report (separate from annual report in some cases). Note: many UAE family businesses are not listed and follow governance voluntarily.

### KSA — CMA Corporate Governance Regulations
The Capital Market Authority's Corporate Governance Regulations apply to listed Saudi companies. Strong emphasis on board composition, committee structures, and remuneration disclosure. Controlled companies (family or government-owned with a majority stake) have adapted rules.

### DIFC
DIFC Companies Law (DIFC Law No. 5 of 2018) and the DIFC Companies Regulations set out governance requirements for companies incorporated in the DIFC. Listed entities on NASDAQ Dubai follow additional disclosure rules.

### Lebanon
No mandatory governance code for non-listed companies; the Lebanese Corporate Governance Institute has published voluntary codes. Banks regulated by Banque du Liban circulars have specific governance requirements.

---

## Drafting standards

- Governance disclosures must be factually accurate — directors' personal liability exposure if false
- Avoid boilerplate that says nothing: "the board is committed to good governance" without substance is a red flag in regulatory review
- The "comply or explain" principle requires a substantive explanation — not "we do not comply with this requirement" without explanation
- Use plain English (or plain Arabic/French where required) — annual reports are read by investors and analysts, not only lawyers

---

## Common mistakes

- Attendance table omitted or inaccurate
- No explanation for departures from the governance code
- Remuneration disclosure does not meet the jurisdiction's minimum disclosure standard
- Risk section is generic and does not identify the company's specific key risks
- No reference to related-party transactions or the process for approving them

---

## Related skills

- [[prompt-pack-board-committee-charter]] — drafting the committee charters referenced in this section
- [[prompt-pack-board-resolution]] — board resolutions approving the annual report
- [[kb-corporate-governance-mena]] — MENA corporate governance codes reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines disclosure requirements
