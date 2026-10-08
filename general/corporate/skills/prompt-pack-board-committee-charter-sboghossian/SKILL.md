---
name: prompt-pack-board-committee-charter-sboghossian
title: Board Committee Charter
description: Use when drafting the charter (terms of reference) for a board committee — Audit, Remuneration/Compensation, Nomination/Governance, or Risk — covering purpose, composition, independence standards, duties, meeting requirements, reporting obligations, and authority to retain advisors. Corporate governance practice area; covers MENA-listed company governance codes (UAE SCA, KSA CMA, DIFC Companies Law) and international standards.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-board-committee-charter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Board Committee Charter

## When to use this

Use this skill when drafting the formal **charter** (also called terms of reference) for a board-level committee. A charter defines the committee's mandate, membership, and operating procedures. It is adopted by the full board and is a foundational governance document.

Most governance codes and regulators in MENA and internationally require certain standing committees. The main committees addressed by this skill:
1. **Audit Committee** — financial reporting, internal audit, external auditor oversight
2. **Remuneration/Compensation Committee** — director and executive pay
3. **Nomination/Governance Committee** — board composition, succession, governance
4. **Risk Committee** — enterprise risk oversight (especially for financial institutions)

---

## Prompt template

> Draft a charter for [Company's] [Audit/Compensation/Nomination/Risk] Committee. Include purpose, composition requirements, independence standards, duties and responsibilities, meeting frequency, reporting obligations, and authority to retain advisors.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Company name and jurisdiction | Determines which governance code applies; composition requirements vary |
| Committee type | Audit, Remuneration, Nomination, Risk — each has different mandatory requirements |
| Board size and composition | Charter must reflect realistic composition possibilities |
| Applicable governance code | SCA (UAE), CMA (KSA), DIFC Companies Law, UK Code, etc. |
| Whether company is listed, regulated, or private | Listed company charters must comply with exchange rules; regulated entities (banks, insurers) have additional requirements |

---

## Document structure (all committee types)

### 1. Purpose and authority
- Committee name and the committee's core mandate (2–3 sentences)
- Delegation by the full board: the committee acts on behalf of and reports to the board; it does not have management authority
- Authority to retain independent advisors (counsel, consultants, experts) at the company's expense — this is a standard governance protection

### 2. Composition

#### 2.1 Size
- Minimum and maximum number of members
- All members must be non-executive directors; majority or all must be independent (as defined)

#### 2.2 Independence standards
Define "independent" by reference to the applicable governance code:

| Jurisdiction | Independence definition |
|-------------|----------------------|
| UAE (SCA Code) | Director who is not an executive; has no material relationship with the company or related parties; has not been an employee in the last 3 years |
| KSA (CMA Code) | Director who is not a controlling shareholder, relative of the CEO, or employee; no material financial relationship with the company |
| DIFC Companies Law | Independent: not an employee; no material business relationship; no family relationship with other directors or officers; meets the definition in the Companies Regulations |
| UK Corporate Governance Code | Annex B independence criteria; majority of board (excluding Chair) should be independent NEDs |

Flag that independence assessments must be disclosed in the annual governance report — see [[prompt-pack-annual-report-governance-section]].

#### 2.3 Chairperson
- Appointed by the full board or elected by committee members
- Must be independent
- **Audit Committee**: the Chair should have financial literacy or expertise (required under most codes; UAE SCA requires at least one member with financial/accounting experience)
- **Remuneration Committee**: the Chair must be independent; the CEO may not chair

#### 2.4 Membership changes
- Committee members are appointed annually by the full board
- Removal: by the full board only
- Vacancies: filled by the full board within [60/90] days

### 3. Duties and responsibilities

#### Audit Committee duties
Core responsibilities (universal across governance codes):
- **Financial reporting**: review the integrity of the company's financial statements; review significant accounting judgements and estimates; review the annual and interim reports before board approval
- **Internal audit**: oversee the internal audit function; approve the internal audit plan; ensure the internal audit function has adequate resources and independence
- **External auditor**: recommend appointment, re-appointment, or removal of the external auditor to the board/shareholders; review external auditor independence (ensure no prohibited non-audit services); approve the external audit scope and fees; review audit findings
- **Internal controls**: review the effectiveness of the company's internal controls over financial reporting; review management's reports on internal control
- **Whistleblowing**: oversee the company's whistleblowing mechanism; ensure employees can report concerns without fear of retaliation
- **Related party transactions**: review and approve related party transactions above defined thresholds

MENA-specific: in UAE (SCA Code) and KSA (CMA Code), the Audit Committee must include at least one member with financial expertise. The committee must report to shareholders at the AGM.

#### Remuneration/Compensation Committee duties
- **Remuneration policy**: design and recommend to the board the company's remuneration policy for directors and senior management
- **Individual remuneration**: approve or recommend the remuneration of each executive director and the CEO
- **Incentive plans**: design, oversee, and administer short-term (annual bonus) and long-term (equity incentive) plans
- **Contractual terms**: review contractual terms for new executive director appointments (notice periods, change of control provisions)
- **Disclosure**: oversee the remuneration report in the annual report

MENA-specific: success/conditional fees and performance-linked remuneration for board members are subject to shareholder approval in UAE (SCA Code); KSA prohibits variable board remuneration in some contexts — verify current rules.

#### Nomination/Governance Committee duties
- **Board succession**: identify and evaluate candidates for board membership; establish selection criteria; oversee the nomination process
- **Skills and diversity**: review the board skills matrix; identify gaps; recommend board diversity goals
- **Independence assessment**: make annual assessments of each director's independence; recommend to the full board
- **Corporate governance**: review the company's governance practices; recommend improvements; oversee compliance with the applicable governance code
- **Board evaluation**: oversee the annual board performance evaluation process

#### Risk Committee duties (for financial institutions and large corporates)
- **Risk appetite framework**: review and recommend to the board the company's risk appetite statement
- **Risk oversight**: oversee the enterprise risk management framework; review key risk reports; escalate emerging risks to the full board
- **Risk function**: oversee the Chief Risk Officer; ensure adequate resources and independence for the risk function
- **Regulatory capital** (for financial institutions): oversee regulatory capital adequacy and liquidity risk management

### 4. Meetings

- **Frequency**: Audit Committee: at least 4 times per year; others: at least 3 times per year (or as required)
- **Quorum**: majority of members; or as specified in the charter
- **Agenda**: Chair (with committee secretary) prepares agenda; members may add items
- **Attendees**: relevant management, external auditor (Audit Committee), and advisors may attend as invitees; committee may meet without management
- **Minutes**: comprehensive minutes maintained; reviewed and approved at the next meeting; filed in corporate records
- **Written resolutions**: permitted between meetings if urgency requires; same quorum/majority applies

### 5. Reporting

- **To the board**: present summary of each committee meeting's deliberations and recommendations to the next board meeting
- **Formal recommendations**: formal recommendations to the board (e.g., approval of financial statements, external auditor appointment) must be recorded in board minutes
- **Annual report**: each committee Chair provides a report of the committee's activities for the annual governance section — see [[prompt-pack-annual-report-governance-section]]
- **Shareholders** (Audit Committee): report to AGM on committee activities and auditor independence

### 6. Authority and resources

- **Independent advisors**: the committee has authority to retain, at the company's expense, independent counsel, financial advisors, auditors, or other specialists it deems necessary
- **Access**: committee members have unrestricted access to management and company records
- **Budget**: annual budget approved by the full board

### 7. Review of the charter

- Review annually for compliance with applicable governance code updates
- Recommend amendments to the full board for approval

---

## Jurisdictional notes

### UAE (SCA Code for listed companies)
- Audit Committee: mandatory; minimum 3 members; all non-executive; majority independent; at least one with financial expertise
- Remuneration Committee: mandatory; minimum 3 members; majority independent; CEO must not be a member
- Nomination Committee: mandatory; minimum 3 members; majority independent
- Risk Committee: recommended for financial institutions; regulated banks must comply with CBUAE corporate governance standards

### KSA (CMA Corporate Governance Regulations)
- Audit Committee: mandatory for listed companies; minimum 3 members; majority independent; at least 2 with financial/accounting experience
- Remuneration and Nominations Committees: mandatory; composition requirements per CMA regulations
- Board member remuneration: shareholder approval required; limits on variable components

### DIFC
- DIFC Companies Law requires an audit committee for public companies (listed or large private); specific independence and financial expertise requirements
- Financial institutions: DFSA Corporate Governance Module imposes additional committee requirements

### Lebanon
- No mandatory committee regime for private companies; voluntary committees for good governance; banks regulated by Banque du Liban circulars have specific committee requirements

---

## Common mistakes

- Charter silent on CEO attendance at committee meetings (for Audit and Remuneration, the CEO should not attend the compensation setting for themselves; state this explicitly)
- No reference to the applicable governance code — charter will quickly become outdated when the code is revised
- Independence criteria not defined — creates annual assessment disputes
- No authority to retain independent advisors — committees without this authority are hamstrung
- Charter not reviewed or updated after governance code amendment

---

## Related skills

- [[prompt-pack-board-resolution]] — board resolution adopting or amending the committee charter
- [[prompt-pack-annual-report-governance-section]] — annual disclosure of committee activities
- [[kb-corporate-governance-mena]] — MENA governance code reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines mandatory composition requirements
