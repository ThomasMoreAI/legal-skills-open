---
name: prompt-pack-investment-agreement-venture-capital-sboghossian
title: Investment Agreement (Venture Capital)
description: Use when drafting a venture capital investment agreement for a Series A, B, or C round — covering investment terms, preferred share rights, anti-dilution protection, liquidation preference, board composition, investor veto rights, and protective provisions. Applicable for startups raising capital across MENA (UAE, DIFC, ADGM, KSA, LB, EG), UK, EU, and US. Trigger when a startup and its investors need to document a priced equity round and the full suite of investor protections.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-investment-agreement-venture-capital
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Investment Agreement (Venture Capital)

## When to use this

Use this skill when drafting the suite of documents that govern a VC investment in a priced equity round. The core documents in a VC transaction are:
1. **Term sheet** (non-binding; sets out the commercial terms)
2. **Subscription agreement / Investment agreement** (the binding agreement under which the investor commits capital and receives shares)
3. **Shareholders' agreement** (governs ongoing relationship between all shareholders)
4. **Articles of association / Memorandum of association** (amended to reflect new preferred share class)
5. **Board resolutions** (authorizing the issuance)

This skill focuses on the investment/subscription agreement and shareholders' agreement terms that are typical for a Series A, B, or C round.

Typical triggers:
- Startup raising its first institutional round and needing to document investor terms
- Lead investor's counsel preparing the draft investment documentation
- Startup's counsel reviewing investor draft documentation
- MENA VC fund documenting a new portfolio company investment

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and jurisdiction of incorporation | Determines the share issuance mechanics and company law framework | Ask |
| Series designation (A/B/C) | Affects rights relative to existing preferred shares | Ask |
| Investment amount and pre-money valuation | Drives all economic calculations | Ask |
| Investors and their investment amounts | May be a single lead or a syndicate | Ask |
| Corporate structure | Number of shares outstanding; existing share classes | Ask |

## Optional inputs

- Whether there is a lead investor or co-leads
- ESOP pool creation or expansion as part of this round
- Existing investor rights that need to be amended
- Anti-dilution preference from prior rounds (affects new round terms)
- Whether the company operates in regulated sectors (ADGM, DIFC registered companies have specific share issuance requirements)

## Document structure

### Part 1 — Subscription / Investment Agreement

#### 1. Parties and recitals

- Company (the issuer)
- Investors (as listed in the Investment Schedule)
- Existing significant shareholders (sometimes parties to consent anti-dilution, co-sale, etc.)
- Recitals: the Company is raising capital; investors wish to subscribe; parties agree on the terms set out below

#### 2. Investment terms

**Share issuance**:
- Number of Series [A/B/C] Preferred Shares being issued
- Subscription price per share (derived from pre-money valuation ÷ fully diluted shares)
- Total investment amount
- Investor allocation schedule (if syndicated)

**Closing mechanics**:
- Closing date (condition precedent: all CPs satisfied)
- Conditions precedent to closing: no material adverse change; no breach of reps; regulatory approvals obtained; ESOP expanded; employee option plan approved; board and shareholder resolutions passed
- Wire transfer instructions for investment proceeds

#### 3. Representations and warranties

**Company representations**:
- Due organization and good standing
- Capitalization (fully diluted cap table is accurate)
- Authority to enter the investment
- No conflicts with existing agreements
- Financial statements fairly present the financial position
- No material undisclosed liabilities
- IP ownership confirmed
- No material litigation pending or threatened
- No material adverse change since the last accounts date
- Full and fair disclosure of all material information

**Investor representations**:
- Investor is an "accredited investor" or "qualified investor" as applicable
- Investment for own account; no distribution intent
- Investor has the authority to enter into the agreement

#### 4. Covenants

**Pre-closing covenants**:
- Company conducts business in the ordinary course pending closing
- Company does not issue new securities, incur debt, or make material changes without investor consent

**Post-closing covenants**:
- Information rights: quarterly financial reports; annual audited accounts; budget; access rights for inspection
- ESOP: company will maintain an option pool of [X%] fully diluted
- Anti-dilution cooperation: company will take necessary steps to implement anti-dilution adjustments

### Part 2 — Shareholders' Agreement / Investor Rights Agreement

This document governs the ongoing relationship and is often the most heavily negotiated.

#### 5. Preferred share rights

**Dividend rights**:
- Cumulative or non-cumulative preferred dividend: typically [8%] per annum cumulative OR non-cumulative participating dividend
- Payment condition: at board discretion OR on liquidity event

**Liquidation preference**:
- Multiple: 1x the original investment amount (standard); 1.5x or 2x (aggressive)
- Type:
  - **Non-participating preferred**: investor receives liquidation preference and no further share in remaining proceeds (standard for VC)
  - **Full participating preferred**: investor receives preference THEN participates in remaining proceeds as if converted to common (aggressive; common in MENA deals)
  - **Capped participating preferred**: investor receives preference THEN participates up to a cap of [2–3x] the original investment (a common compromise)
- Liquidation events: winding up; sale of the company; deemed liquidation (merger, IPO sometimes)

**Conversion rights**:
- Automatic conversion to common on IPO (above a minimum market cap threshold)
- Optional conversion at investor's election at any time
- Conversion ratio: initially 1:1; adjusted for anti-dilution

#### 6. Anti-dilution protection

Protects investors against future down-round financing (a new round at a lower price per share):

**Broad-based weighted average anti-dilution** (most commonly used and most founder-friendly of the protective forms):
- New conversion price = old conversion price × [(A + B) / (A + C)]
- Where A = fully diluted shares before new issuance; B = new money ÷ old price (shares that would have been issued at old price); C = actual shares issued
- Effect: new conversion price is reduced based on the size of the down-round

**Narrow-based weighted average**:
- Only counts the specific class of preferred shares in the formula; broader dilutive effect

**Full ratchet** (most aggressive; almost never used in practice):
- Conversion price drops to the price of the new shares; very dilutive for founders

**Carve-outs** (securities that do not trigger anti-dilution):
- Employee ESOP issuances (up to authorized pool size)
- Convertible note conversions pre-agreed
- Acquisitions with board and investor approval
- Strategic partnerships approved by the board

#### 7. Protective provisions (investor veto rights)

Investors typically require the right to approve certain major decisions. These are known as "protective provisions" or "reserved matters."

Standard reserved matters requiring preferred shareholder approval:
- Issuance of new equity securities (other than ESOP)
- Amendments to the company's articles that adversely affect the preferred shareholders
- Any merger, acquisition, sale of all or substantially all assets, or liquidation
- Incurrence of debt above [USD X million]
- Change in the size or composition of the board beyond agreed limits
- Payment of dividends on common shares before preferred
- Material change in the company's business
- Related-party transactions above [USD X] unless approved by independent directors

These are protective, not controlling: the investor is protecting against the founder taking actions that harm the investor, not trying to control day-to-day operations.

#### 8. Board composition

**Typical Series A board for a 5-person board**:
- [2] Common directors (founders / management)
- [1] Series A investor director (nominated by lead investor)
- [1] Independent director (agreed by founders and investors)
- [1] Observer (non-voting; sometimes granted to smaller investors or earlier investors)

**Series B and beyond**: Additional investor seats as the cap table grows; number of independent directors increases.

**Board observer rights**: Some investors who do not get a board seat get observer rights: right to attend board meetings and receive board materials; no voting right.

#### 9. Transfer restrictions

**Right of first refusal (ROFR)**:
- Before any shareholder transfers shares to a third party, other shareholders (or the company) have the right to purchase at the same price and on the same terms as the proposed transfer

**Co-sale right (tag-along)**:
- If a founder sells shares, investors have the right to sell a pro-rata portion of their own shares on the same terms ("tagging along" with the founder's sale)
- Prevents founders from exiting while investors are left behind

**Drag-along right**:
- If a majority of shareholders (or a specified threshold) approve a sale of the company, they can drag remaining shareholders along on the same terms
- Protects against a holdout blocking a sale that the majority supports

**Lock-up**:
- Founders' shares subject to a vesting schedule (typically 4 years, 1-year cliff)
- Unvested shares subject to reverse vesting (company can repurchase at nominal cost on founder departure before vesting)

#### 10. Information rights

- Quarterly unaudited financial statements within [45] days of quarter-end
- Annual audited financial statements within [90–120] days of year-end
- Annual budget and operating plan before the start of each fiscal year
- Notice of any material adverse development
- Inspection rights: access to books and records on reasonable notice

#### 11. Pre-emptive rights (pro-rata rights)

- Investors have the right to participate in future financing rounds to maintain their percentage ownership
- Pro-rata: each investor can subscribe for new shares in proportion to their current holding
- Major investor pro-rata right: investors above a threshold (e.g., 5% ownership) get "super pro-rata" rights to invest more than their proportional amount (negotiated)

## Jurisdictional notes

### MENA corporate structures for VC investment

| Jurisdiction | Entity type | Key considerations |
|---|---|---|
| **DIFC (offshore)** | DIFC Company; DIFC LLC | DIFC Companies Law is common-law friendly; preferred shares with full VC terms work well; foreign investors; used as investment holding company for MENA regional businesses |
| **ADGM (offshore)** | SPV or operating company | ADGM Companies Regulations; similar to DIFC; increasingly used for fund structures |
| **UAE Mainland** | LLC (limited company) | Most restrictive for VC: UAE LLC law does not well support preferred share classes with complex economics; most VC-backed startups incorporate in DIFC/ADGM or offshore (Cayman, BVI) with a UAE operating subsidiary |
| **KSA** | Closed Joint Stock Company (CJSC) | CJSC can issue preferred shares; Capital Market Law governs; MISA approval for foreign investment; Sharia compliance required for interest-based instruments |
| **Lebanon** | SAL (Société Anonyme Libanaise) | Lebanese company law supports preferred shares but documentation is civil-law-style; political instability makes onshore investment unattractive; offshore holdco common |
| **Cayman Islands** | Exempted Company | Industry standard for US and international VC; clean, well-understood share class mechanics; used as holdco for MENA operating companies |

### Islamic finance considerations (KSA)

In KSA, VC investment structures must be Sharia-compliant:
- Conventional liquidation preferences (effectively a guaranteed return) may be challenged as involving riba (interest)
- Mudaraba (profit-sharing) and musharaka (equity partnership) structures are Sharia-compliant alternatives
- Sukuk (Islamic bonds) rather than convertible notes
- KSA VC practitioners increasingly use CMA-approved structures that balance investor protection with Sharia compliance; seek specific KSA counsel

## Common mistakes

- **Using US-style VC docs for UAE/KSA entities**: US Delaware-standard documents reference SEC regulations, Delaware corporate law, and US tax concepts that have no application to UAE or KSA entities; use documents tailored to the applicable corporate law.
- **Full participating preferred in all rounds**: Full participating preferred gives investors a double-dip (liquidation preference + common participation); this is aggressive and will reduce the company's attractiveness to future investors; negotiate non-participating or capped participating.
- **Broad drag-along rights**: A drag-along triggered at a low threshold (simple majority) can force founders into a fire-sale; negotiate a higher threshold (e.g., 70–75% of fully diluted shares) and founder consent requirements for drags.
- **No founder vesting in MENA startups**: Many MENA startups do not implement founder vesting; without it, a co-founder who departs early takes their full equity; investor should require reverse vesting as a closing condition.
- **Missing regulatory consents**: For UAE onshore or KSA operating companies, FDI approvals and sector-specific regulatory approvals may be required before the investment closes; these must be conditions precedent, not afterthoughts.

## Related skills

- [[prompt-pack-escrow-agreement]]
- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-disclosure-letter]]
- [[prompt-pack-equity-incentive-plan-summary]]
