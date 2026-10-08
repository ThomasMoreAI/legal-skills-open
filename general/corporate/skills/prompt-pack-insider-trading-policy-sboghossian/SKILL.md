---
name: prompt-pack-insider-trading-policy-sboghossian
title: Insider Trading Policy
description: Use when drafting an insider trading policy for a listed or pre-IPO company — covering the definition of material non-public information (MNPI), trading blackout periods, pre-clearance requirements, trading plan procedures, tipping prohibitions, and consequences of violations. Applicable for companies listed on UAE markets (DFM, ADX), Saudi Exchange (Tadawul), Lebanon Stock Exchange, Egyptian Exchange, London Stock Exchange, and US markets. Trigger when a company's board or legal counsel needs to establish or update its securities trading compliance policy.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-insider-trading-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Insider Trading Policy

## When to use this

Use this skill when drafting or updating an insider trading policy — the internal governance document that prohibits trading in the company's securities (or the securities of companies it is in a business relationship with) on the basis of material non-public information. Insider trading policies are mandatory for listed companies in all major markets and are best practice for pre-IPO companies and PE-backed entities that regularly deal with M&A or capital market transactions.

Typical triggers:
- Company preparing for IPO on UAE, KSA, UK, or US markets
- Listed company updating its securities compliance policies
- PE-backed company establishing governance standards ahead of an investment
- Company responding to a securities regulator's request for evidence of controls
- Compliance officer preparing the annual policy update

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and listing venue (or planned listing) | Determines applicable securities law | Ask |
| Scope of covered persons | Who the policy applies to: directors, officers, employees, family members? | Ask |
| Blackout period triggers | Earnings release dates; M&A transactions; other specified events | Ask |
| Pre-clearance process | Who approves trades? (General Counsel, Chief Compliance Officer) | Ask |
| Applicable securities law | UAE Capital Market Law, UK MAR, US Exchange Act Section 10(b)/Rule 10b-5 | Ask |

## Optional inputs

- Trading plan (10b5-1 plan or equivalent) provisions
- Special rules for significant shareholders (5%+ holders)
- Prohibition on hedging and pledging company securities
- Equity grant window provisions (when option exercises are permitted)

## Document structure

### Section 1 — Purpose and scope

**Purpose**:
> "This Policy is intended to prevent insider trading, which is illegal, and to protect [Company] and its employees from the regulatory, legal, and reputational consequences of trading on or communicating material non-public information."

**Scope — covered persons**:
- All directors and officers
- All employees
- Contractors and consultants with access to MNPI
- Family members and household members of the above (who benefit from MNPI shared with a covered person)
- Entities controlled by covered persons

The policy should clearly state: the obligation applies to trading in Company securities AND in the securities of any company about which the covered person possesses MNPI (e.g., a potential acquisition target).

### Section 2 — Definition of material non-public information (MNPI)

**Material information**: Information is material if a reasonable investor would consider it important in deciding whether to buy, sell, or hold securities, or if it would likely affect the market price of the securities.

Examples of material information (non-exhaustive):
- Financial results (quarterly or annual earnings; revenue; profit warnings)
- Proposed mergers, acquisitions, joint ventures, or divestitures
- Major contracts won or lost
- Major regulatory approvals or rejections
- Significant litigation outcomes
- Senior management changes (CEO, CFO)
- Dividend declarations, stock splits, or buybacks
- Public offerings of securities or borrowings
- Cybersecurity incidents with potential material impact
- Data breaches

**Non-public information**: Information is non-public until it has been widely disseminated to the investing public through official channels (regulatory filings, press release, market announcement) AND a reasonable period has elapsed for the market to absorb it (typically 2 trading days after public release).

**Important**: Information does not become public just because it is known to some people in the industry or has been discussed informally. The standard is widespread, official public dissemination.

### Section 3 — Prohibited conduct

**Prohibited trading**: No covered person may:
1. Buy, sell, or transfer Company securities while in possession of MNPI
2. Buy, sell, or transfer securities of any other company while in possession of MNPI about that company (acquired through Company employment)

**Tipping prohibition**:
3. Disclose MNPI to any other person (a "tip"), including family members, friends, or business associates, if the covered person knows or has reason to believe the recipient will trade on that information
4. Make recommendations to trade based on MNPI, even without disclosing the specific information

**Short sales**: No covered person may sell Company securities short (betting against the Company's stock price). Short sales are both illegal in most markets and contrary to this policy.

**Derivatives and hedging**:
5. No covered person may engage in transactions involving options, puts, calls, swaps, or other derivatives on Company securities (other than exercising stock options granted by the Company under its equity plans)
6. No covered person may enter into hedging transactions that effectively allow them to hold Company securities without the economic risk of ownership (collars, forward contracts, etc.)

**Pledging**:
7. No covered person may pledge Company securities as collateral for a loan unless specifically approved by the Board Compensation Committee

### Section 4 — Blackout periods

**Regular blackout periods**:
- Commence: [2–4] weeks before the expected announcement of quarterly or annual financial results
- End: [48 hours / 2 trading days] after the public announcement
- Specific dates for the current year are communicated annually by the Compliance Officer

**Event-driven blackout periods**:
- A special blackout period applies whenever a covered person becomes aware of a specific material event (pending M&A, regulatory action, major contract, earnings revision)
- The Compliance Officer will notify covered persons when a special blackout is in effect; covered persons who become aware of MNPI must self-impose a blackout even if not notified

**Exception for 10b5-1 plans / approved trading plans** (see Section 5)

### Section 5 — Pre-clearance requirements

**Covered persons who must pre-clear**:
- Directors and officers
- Designated senior employees (list by role: CFO, General Counsel, heads of business units with access to MNPI)

**Pre-clearance procedure**:
1. Submit a pre-clearance request to the Compliance Officer at least [2] business days before the proposed transaction
2. State: the type of transaction (buy/sell/gift); the number of shares; the proposed date
3. The Compliance Officer will approve or deny the request within [1] business day
4. Approval does not mean the covered person is free from their own obligation to ensure they do not possess MNPI; pre-clearance is an additional safeguard, not a waiver
5. Approved transactions must be completed within [5] business days of approval; if not completed, a new pre-clearance request is required

**Records**: The Compliance Officer maintains a log of all pre-clearance requests and decisions.

### Section 6 — Trading plans

In markets where trading plans equivalent to US SEC Rule 10b5-1 are permitted (US listed companies; analogous provisions exist in UK and EU), covered persons may establish a pre-approved trading plan:
- The plan must be entered into at a time when the covered person does not possess MNPI
- The plan must be in writing and specify the amount, price, and timing of future trades in advance
- The plan must be approved by the Compliance Officer before adoption
- A cooling-off period applies between adopting the plan and first trade (US: minimum 90 days for non-directors; 120 days for directors and officers, or until the next quarterly earnings, whichever is later)
- Plans cannot be modified or cancelled while the covered person possesses MNPI

### Section 7 — Post-termination obligations

The prohibition on trading on MNPI continues after a covered person's employment or relationship with the Company ends:
- Former employees retain MNPI they acquired during their employment
- The trading prohibition applies until the information is public or is no longer material
- In practice, former directors and officers should wait until the next scheduled public disclosure before trading

### Section 8 — Reporting and certification

**Annual certification**: All covered persons must certify annually that they have read, understood, and complied with this policy.

**Reporting violations**: Any covered person who becomes aware of a potential violation of this policy must report it immediately to the Compliance Officer or General Counsel (or to the Audit Committee if the General Counsel is involved).

**Reporting to regulators**: The Company will cooperate with any investigation by the applicable securities regulator. Directors and officers who receive an inquiry from a regulator regarding securities trading must notify the General Counsel immediately.

### Section 9 — Consequences of violations

**Regulatory consequences**:
- UAE (SCA): Securities and Commodities Authority regulations on market manipulation and insider trading; criminal penalties including fines and imprisonment
- KSA (CMA): Capital Market Law; criminal prosecution by the Capital Market Authority; disgorgement of profits; administrative sanctions
- UK (FCA): UK Market Abuse Regulation (UK MAR); criminal prosecution under Criminal Justice Act 1993; unlimited fines; imprisonment up to 7 years
- EU (MAR): Market Abuse Regulation; harmonized sanctions across EU member states; criminal and administrative penalties
- US: Securities Exchange Act Section 10(b), Rule 10b-5; SEC enforcement; criminal prosecution (DoJ); up to 20 years' imprisonment; treble damages in civil actions

**Employment consequences**:
- Violations of this policy constitute grounds for immediate termination for cause
- Violations may result in disgorgement of trading profits as a condition of employment continuation

### Section 10 — Education and training

- All covered persons receive training on this policy at onboarding and at least annually thereafter
- Training materials and records are maintained by the Compliance Officer

## Jurisdictional notes

### UAE and KSA — Market Abuse

**UAE**: SCA Resolution No. 11 of 2020 concerning Standards of Institutional Discipline and Institutional Governance (and the Securities and Commodities Authority Law) prohibit insider trading and market manipulation. ADX and DFM require listed companies to adopt and maintain written insider trading policies. The UAE Criminal Code and Capital Markets Law impose criminal sanctions.

**KSA**: Capital Market Law (Royal Decree M/30); CMA Regulations on Market Conduct and Price Stabilization prohibit trading on material non-public information. The CMA actively enforces; criminal prosecution and disgorgement of profits are the standard consequences.

**Lebanon Stock Exchange**: Listed companies are subject to Capital Markets Authority regulations; insider trading prohibitions are established in the Capital Market Law framework.

**Egypt (EGX)**: Capital Market Law (Law No. 95 of 1992) and Financial Regulatory Authority regulations prohibit insider trading; penalties include fines and criminal prosecution.

### 10b5-1 equivalent plans in non-US markets

The US Rule 10b5-1 plan concept has inspired similar safe-harbor frameworks in some markets (UK and some EU jurisdictions under MAR). In MENA, trading plan safe harbors are less developed; seek specific local counsel advice before establishing a trading plan for executives in MENA-listed companies.

## Common mistakes

- **Only covering equity securities**: Policies should also cover debt securities (bonds), derivative instruments, and rights/warrants related to Company securities — not just common shares.
- **No family member coverage**: Many enforcement actions involve trading by family members who received tips; the policy must expressly cover transactions by household members.
- **Generic MNPI definition**: A definition limited to "confidential information" is not enough; list specific categories of information to ensure covered persons understand what counts.
- **No consequence for violations**: A policy without stated consequences for violations is not credible; include both regulatory consequences (external) and employment consequences (internal).
- **No 10b5-1 plan cooling-off period**: US-listed companies must comply with SEC 2023 Rule 10b5-1 amendments requiring extended cooling-off periods; older policies without this are non-compliant.

## Related skills

- [[prompt-pack-esg-policy-framework]]
- [[prompt-pack-executive-employment-agreement]]
- [[prompt-pack-engagement-letter]]
- [[prompt-pack-investment-agreement-venture-capital]]
