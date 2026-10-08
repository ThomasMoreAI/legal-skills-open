---
name: prompt-pack-corporate-governance-policy-sboghossian
title: Corporate Governance Policy
description: Use when a company needs to draft or update a Corporate Governance Policy covering board structure, director qualifications and independence, board evaluations, succession planning, shareholder engagement, and compliance with applicable governance codes. Relevant across MENA (UAE, KSA, LB, EG) and for entities subject to DIFC/ADGM, DFM, ADX, Tadawul, or international listing requirements. Addresses civil-law and common-law governance frameworks and the intersection with Sharia-compliant governance in GCC markets.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-corporate-governance-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Corporate Governance Policy

A Corporate Governance Policy formalises the structures and processes by which a company is directed and controlled. For listed companies it is a regulatory requirement; for private companies it is increasingly expected by investors, lenders, and regulators — and is the foundation of any credible compliance program.

## When to use this

- A company is preparing for a listing on a regulated exchange (DFM, ADX, Tadawul, LSE, NYSE, Nasdaq) where governance disclosure is mandatory.
- A private company is raising capital and investors require documented governance structures as a condition of investment.
- A company is expanding its board from a founder-controlled structure to include independent directors.
- Regulatory guidance (e.g., UAE Governance Code for public companies, SCA Governance Rules) requires a written governance policy.
- Following a corporate incident or audit finding that exposed governance gaps.
- A group of companies needs a uniform governance framework across multiple jurisdictions.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction of incorporation | Determines the applicable companies law and governance code | Ask the user |
| Company type (listed / private / family business / SOE) | Governance requirements and best practice differ materially | Ask the user |
| Applicable governance code | The policy should comply with any mandatory or applicable voluntary code | Ask the user; see jurisdiction notes below |
| Current board composition | The policy must reflect or improve on the current structure | Ask the user |
| Any specific investor or regulator requirements | Some investors or regulators require specific provisions | Ask the user |

## Optional inputs

- Whether the policy covers subsidiaries and group companies.
- Whether Sharia compliance considerations apply to the board's oversight role (relevant for Islamic finance companies in KSA, UAE, and Bahrain).
- Whether a Nomination and Remuneration Committee already exists or needs to be established.
- Whether the company has a Sharia Supervisory Board in addition to the main board.

## Document structure

### 1. Introduction and purpose
- The company's commitment to high standards of corporate governance.
- The purpose of the policy: to ensure the board operates effectively, consistently, and in compliance with applicable law.
- The governing law and governance code(s) to which the policy relates.
- Date of adoption and review cycle (recommend: annual review).

### 2. Board structure and composition

**2.1 Board size:**
- Define the minimum and maximum number of directors.
- Listed company requirements: UAE (SCA requires minimum 5 directors for listed companies); KSA (CMA requires minimum 5 for listed companies); DIFC/ADGM (companies law governs minimum).

**2.2 Director categories:**
- Executive directors (management role).
- Non-executive directors (oversight role).
- Independent non-executive directors: define independence using the applicable code standard.

**2.3 Independence criteria:**
A director is independent if they:
- Have not been an employee of the company in the past [5] years.
- Do not have a material business relationship with the company.
- Do not represent a significant shareholder.
- Do not have a family relationship with any executive director or senior manager.
- Have not served on the board for more than [9] years without re-evaluation of independence.

**UAE SCA Governance Rules for listed companies:** require at least one-third of board members to be independent non-executives. **KSA CMA:** at least two independent members or one-third, whichever is greater.

**2.4 Family business governance (MENA specific):**
In family businesses — which constitute the majority of MENA private companies — the board composition provisions should address: family vs. non-family directors, the role of a family governance council if any, separation of ownership and management roles, and succession planning across generations.

### 3. Director qualifications and fitness
- Minimum qualifications: relevant experience, financial literacy (at least one member with financial expertise), clean criminal record.
- Continuous professional development requirements.
- Disclosure obligations: directors must disclose any conflict of interest, change in outside directorships, or material change in personal circumstances.
- Fit and proper requirements for directors of regulated entities (DFSA, FSR, SAMA, UAE Insurance Authority).

### 4. Board meetings and decision-making

**4.1 Meeting frequency:**
- Minimum number of meetings per year (listed companies in UAE: at least 4 per year under SCA rules; KSA CMA: at least 4 per year).
- Quorum requirements.

**4.2 Agenda and information:**
- Board papers to be circulated [X] days before each meeting.
- Standard agenda: financials, operational performance, risk report, governance matters, strategic review (at least annually).

**4.3 Reserved matters:**
List decisions reserved for the board (not delegated to management). Minimum list for a commercial company:
- Approval of annual budget and business plan.
- Major capital expenditure above [threshold].
- Acquisitions, disposals, and investments above [threshold].
- Appointment and removal of CEO/CFO.
- Board and committee appointments.
- Material litigation.
- Related party transactions (especially important in MENA family business contexts).
- Approval of annual financial statements.
- Dividend approval.

### 5. Board committees
Describe each committee established:

**Audit Committee:**
- Composition (minimum [3] members; majority independent; at least one financial expert).
- Responsibilities: oversight of financial reporting, internal controls, external and internal audit, risk management.
- Mandatory for: UAE listed companies (SCA requirement); KSA listed companies (CMA requirement); DIFC/ADGM regulated entities.

**Nomination and Remuneration Committee:**
- Responsibilities: director nomination, independence assessment, succession planning, executive remuneration policy.
- KSA: CMA requires a Nomination and Remuneration Committee for listed companies.

**Risk Committee (for regulated entities and large companies):**
- Oversight of enterprise risk management framework.
- Reporting line to the full board.

**Sharia Supervisory Board (for Islamic finance entities):**
- Composition: minimum [3] scholars with relevant qualifications.
- Role: review and certify Sharia compliance of products and operations.
- Reporting: annual Sharia report to shareholders.
- Required for: UAE Islamic banks, KSA Islamic finance institutions, Bahrain financial institutions under CBB rules.

### 6. Board evaluation
- Annual performance evaluation of the board as a whole, individual directors, and each committee.
- Methodology: self-assessment questionnaire, peer review, or external facilitator (recommended for listed companies at least every 3 years).
- Results: discussed at a board meeting; action plan prepared for any identified gaps.

### 7. Succession planning
- Identification of potential successors for the CEO, CFO, and other key management roles.
- Emergency succession plan (immediate step-up if key person is incapacitated).
- Director succession: proactive identification of candidates for board vacancies; avoid cliff-edge where many independent directors retire simultaneously.
- MENA family businesses: plan must address generational succession and the role of non-family management.

### 8. Shareholder engagement
- Annual General Meeting (AGM): timing, notice requirements, and agenda.
- Minority shareholder rights: information rights, voting rights, related-party transaction approvals.
- Dividend policy: criteria and declaration process.
- Investor relations for listed companies: disclosure obligations, quiet period policy, insider trading policy.
- **UAE:** Federal Companies Law requirements for AGM timing and shareholder notice.
- **KSA:** Companies Law (Royal Decree M/3, 2015 as amended) governs AGM requirements.

### 9. Related party transactions
One of the most important governance provisions in MENA:
- Define related parties (directors, major shareholders, their family members and associated entities).
- Require board approval for any transaction with a related party above a specified threshold.
- Require independent director approval for transactions where a director has a personal interest.
- Listed companies must disclose related party transactions in their annual reports (SCA and CMA rules).
- Maintain a register of interests.

### 10. Reporting and transparency
- Annual report governance section: mandatory disclosures for listed companies.
- ESG / sustainability reporting: increasingly required by DFM, ADX, Tadawul, and institutional investors.
- Whistleblowing: reference to the company's Code of Conduct or speak-up policy.

### 11. Review and amendment
- The policy is reviewed annually by the board (or a designated committee).
- Amendments require board approval.
- Local counsel in each operating jurisdiction reviews the policy before adoption and after any material regulatory change.

## Jurisdictional governance codes

| Jurisdiction | Primary governance instrument |
|---|---|
| UAE (listed) | SCA Corporate Governance Rules for Joint Stock Companies (SCA Decision No. 7 of 2016, as amended) |
| UAE (DIFC) | DIFC Companies Law (DIFC Law No. 5 of 2018) and DFSA CIR/GEN Rulebooks for regulated entities |
| UAE (ADGM) | ADGM Companies Regulations 2020 and FSRA regulations for regulated entities |
| KSA (listed) | CMA Corporate Governance Regulations (updated 2017) |
| Lebanon | Lebanese Companies Law (Decree No. 304 of 1942 as amended); no mandatory listed company code (Beirut Stock Exchange has guidelines) |
| Egypt (listed) | EGX Corporate Governance Code; Financial Regulatory Authority rules |
| GCC (Islamic finance) | AAOIFI Governance Standards (voluntary but widely adopted) |

## Common mistakes

- A policy that lists governance obligations without assigning them to specific bodies (board, committee, management) — unassigned obligations are ignored.
- Independence criteria that are less stringent than the applicable regulatory code — this creates a compliance gap for listed companies.
- No reserved matters list — without it, management takes decisions that should require board approval.
- Related party transaction controls that are aspirational but have no enforcement mechanism (no approval gate, no register).
- Failing to update the policy after listing rules change — governance codes are revised periodically; the policy must track them.

## Related skills

- [[prompt-pack-code-of-conduct]]
- [[prompt-pack-delegation-of-authority-matrix]]
- [[prompt-pack-director-indemnification-agreement]]
- [[prompt-pack-corporate-resolutions]]
- [[prompt-pack-anti-bribery-policy]]
