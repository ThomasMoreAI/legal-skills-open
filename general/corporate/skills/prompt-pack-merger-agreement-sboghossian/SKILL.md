---
name: prompt-pack-merger-agreement-sboghossian
title: Merger Agreement
description: 'Use when drafting a merger or amalgamation agreement for a transaction in which two or more entities combine. Covers exchange ratio, representations and warranties, covenants, conditions to closing, termination rights, break fees, and regulatory approval requirements. MENA-focused: addresses UAE Commercial Companies Law, KSA Companies Law, DIFC/ADGM corporate legislation, and cross-border competition filings.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-merger-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Merger Agreement

## When to use this

Use this skill when drafting the definitive agreement governing a merger or amalgamation — the combination of two companies into a single surviving entity. Distinguish from a share purchase agreement (acquisition of a company's shares) and an asset purchase agreement (acquisition of specific assets). Mergers typically involve share exchange rather than cash payment and require corporate law compliance for the merger procedure.

Triggers:
- "Draft a merger agreement for the merger of [Company A] into [Company B]."
- "We need an amalgamation agreement for our GCC restructuring."
- "Draft heads of agreement for a statutory merger under DIFC company law."

**Note on MENA usage**: In most MENA jurisdictions, the formal statutory merger process is less commonly used for commercial M&A than a share purchase or business combination structure. Confirm with local counsel whether a statutory merger procedure is available and appropriate for the target jurisdiction.

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company A and Company B names, jurisdictions | Identifies the parties and applicable law | Ask user |
| Merger structure | Forward merger / reverse merger / amalgamation / scheme of arrangement | Ask user |
| Exchange ratio | Core economic term; number of surviving entity shares per Company A share | Ask user |
| Governing law | Determines applicable corporate law and procedural requirements | Jurisdiction of surviving entity |
| Regulatory approvals required | Competition filings, sector-specific approvals (banking, telecoms, etc.) | Ask user based on jurisdiction |
| Anticipated closing timeline | Determines urgency and covenant structure | Ask user |

## Optional inputs

- Cash component (if mixed cash/share consideration)
- Earnout provisions (if part of consideration is contingent)
- Board recommendation commitment and fiduciary out
- Employee benefit continuation provisions
- No-shop / no-solicitation provisions during the period from signing to closing
- Break fee and reverse break fee

## Document structure

### 1. Recitals
- Brief description of each party
- Purpose: the boards of directors of Company A and Company B have each determined that the merger is in the best interests of their respective companies and shareholders
- Transaction overview: [Company A] will merge with and into [Company B] (the "Surviving Entity") in accordance with the applicable corporate law

### 2. The Merger

**2.1 Merger mechanics**
- At the effective time, Company A shall merge with and into Company B; Company B shall be the Surviving Entity.
- Company A shall cease to exist as a separate legal entity at the effective time.

**2.2 Effective time**
- The merger becomes effective upon filing of the merger certificate / registration with [relevant corporate registry].
- Target effective date: [date / as soon as practicable after conditions are satisfied].

**2.3 Articles of association / constitutional documents**
- The articles of association of the Surviving Entity shall be [as set out in Exhibit X] with effect from the effective time.

### 3. Exchange Ratio and Merger Consideration

**3.1 Exchange ratio**
- Each share of Company A outstanding immediately prior to the effective time shall be converted into the right to receive [X] shares of Company B (the "Exchange Ratio").

**3.2 Adjustment mechanism**
- Exchange ratio is subject to adjustment for any share split, consolidation, reclassification, or dividend occurring between signing and closing.

**3.3 Cash in lieu of fractional shares**
- No fractional shares of Company B shall be issued; Company A shareholders entitled to fractional shares shall receive cash based on the volume-weighted average price of Company B shares for the [10] trading days preceding the effective time.

**3.4 Dissenting shareholders**
- Shareholders of Company A who exercise applicable dissent rights (if any under the governing law) shall receive fair value for their shares as determined under applicable law.
- Note: dissenter / appraisal rights vary significantly by jurisdiction; confirm availability with local counsel.

### 4. Representations and Warranties

Both parties provide standard M&A representations and warranties, typically including:

**Company A represents and warrants**:
- Due incorporation and good standing
- Corporate authority to enter into the agreement and consummate the merger
- No conflict with charter documents, material contracts, or applicable law
- Capitalization: all shares described are validly issued and outstanding; no outstanding options or warrants except as disclosed
- Financial statements: prepared in accordance with [IFRS / US GAAP / applicable local GAAP]; present a true and fair view
- No material adverse change since the balance sheet date
- Compliance with applicable law; no material litigation
- Tax: all material taxes filed and paid
- Intellectual property: owned or licensed as described; no infringement
- Absence of undisclosed liabilities
- Material contracts: list attached; no defaults

**Company B (Surviving Entity) provides reciprocal representations.**

### 5. Covenants

**5.1 Conduct of business pending closing**
From signing to closing, each party covenants to:
- Conduct its business in the ordinary course consistent with past practice
- Not make material changes to compensation, benefit plans, or capital structure without consent
- Not enter into material contracts outside the ordinary course without consent
- Not declare dividends or make distributions without consent
- Use reasonable best efforts to preserve business relationships and key personnel

**5.2 No-solicitation (no-shop)**
From signing to closing, Company A will not solicit, encourage, or facilitate any competing acquisition proposal, subject to a customary fiduciary out allowing the board to respond to an unsolicited superior proposal.

**5.3 Regulatory approvals**
Each party will use best efforts to obtain all required regulatory approvals, including:
- Competition / merger control filings (identify applicable jurisdictions: UAE, KSA, Egypt, EU, etc.)
- Sector-specific approvals (banking: UAE Central Bank, SAMA; telecoms: TRA; etc.)
- Foreign investment approvals (MISA in KSA; UAE Cabinet approval for certain sectors)

**5.4 Shareholder approval**
Each party will promptly convene a general meeting to approve the merger; the board of each party will recommend shareholder approval.

### 6. Conditions to Closing

**6.1 Mutual conditions** (either party may waive):
- Shareholder approval obtained by both parties
- All required regulatory approvals obtained; no injunctions

**6.2 Conditions for Company A's benefit**:
- Company B's representations and warranties are true and correct in all material respects at closing
- Company B has performed all covenants in all material respects
- No material adverse effect has occurred with respect to Company B

**6.3 Conditions for Company B's benefit** (reciprocal):
- Same as above with respect to Company A

### 7. Termination

**7.1 Termination rights**:
- By mutual written consent at any time
- By either party if: closing has not occurred by the outside date (typically [6–12 months] from signing); shareholder approval not obtained; required regulatory approval denied
- By Company B if: Company A board changes its recommendation
- By Company A if: superior proposal is received and fiduciary out exercised

**7.2 Break fee (Termination fee)**:
- If Company A terminates to accept a superior proposal: Company A pays break fee of [2–4]% of transaction value to Company B
- If Company B is unable to close due to failure to obtain regulatory approval: Company B pays a reverse break fee (regulatory break fee) to Company A of [similar or higher amount]

### 8. Indemnification and Survival
- Representations and warranties of both parties shall survive closing for [12 / 18 / 24] months (or not at all in an all-equity deal — common in public mergers)
- Individual claim threshold (basket): [X]
- Aggregate cap on indemnification: [X% of transaction value]
- Exclusions from cap: fraud, willful misrepresentation, fundamental representations (title, capitalization, authorization)

### 9. Miscellaneous
- Expenses: each party bears its own transaction costs unless otherwise agreed
- Governing law and dispute resolution — critical; specify court or arbitration
- Entire agreement, amendment, waiver
- Counterparts and electronic execution

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **UAE (onshore)** | Statutory mergers governed by Federal Decree-Law on Commercial Companies; Arabic-language merger plan must be published and approved by Ministry of Economy; creditor notification periods apply. |
| **DIFC / ADGM** | DIFC Companies Law / ADGM Companies Regulations provide for mergers; English-law framework; suitable for holding-company mergers in financial services. |
| **KSA** | Saudi Companies Law governs mergers; MISA and sector-specific approvals (SAMA, CMA) required; Arabic-language documentation; Sharia-compliant financing of any cash component required for Islamic finance entities. |
| **Egypt** | Mergers governed by Companies Law No. 159 of 1981 and the Capital Market Authority (CMA) for listed companies; creditor protection provisions. |
| **Competition law** | UAE, KSA, and Egypt each have competition laws that may require merger notification if combined market share or transaction value exceeds prescribed thresholds. Cross-border mergers may also require EU and/or third-country filings. |

**Exchange ratio / valuation note**: In MENA statutory mergers, an independent valuation by a court-appointed or regulatory-approved valuer may be required; the exchange ratio must be supported by a fairness opinion. Do not agree an exchange ratio without engaging a financial adviser for the valuation exercise.

## Common mistakes

- **Using US-style merger agreement in a civil-law MENA jurisdiction**: representations and warranty insurance, indemnification baskets, and Delaware corporate law concepts do not map cleanly onto UAE or KSA corporate law; local counsel must adapt.
- **Omitting creditor notification**: most MENA jurisdictions require a notice to creditors period (30–60 days) before a merger becomes effective; this extends the closing timeline and must be included in the planning calendar.
- **Forgetting sector-specific approvals**: a banking, insurance, or telecoms merger that closes without regulatory approval is void; always identify and track all required regulatory approvals before signing.
- **No reverse break fee**: if the deal may fail due to regulatory denial, the buyer/Company B should bear a reverse break fee risk; this is commonly overlooked in domestic transactions.

## Related skills

- [[prompt-pack-letter-of-intent]]
- [[prompt-pack-memorandum-of-understanding]]
- [[prompt-pack-ip-due-diligence-checklist]]
- [[prompt-pack-joint-venture-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
