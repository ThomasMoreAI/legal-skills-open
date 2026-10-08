---
name: draft-shareholders-agreement-sboghossian
title: Shareholders' Agreement (SHA)
description: Use when drafting a shareholders' agreement (SHA) for a private company — startup, joint venture, family business, or PE-backed company. Covers governance, reserved matters, transfer restrictions (ROFR, ROFO, drag-along, tag-along), anti-dilution, liquidation preferences, founder vesting, and exit mechanics. Provides MENA-specific adaptations for DIFC, ADGM, UAE onshore, KSA, and Lebanon entity types, flagging the classic deal-breaker tensions between investors and founders.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-shareholders-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Shareholders' Agreement (SHA)

A shareholders' agreement is a private contract between the shareholders of a company — supplementary to the company's constitutional documents (articles of association / memorandum) — that governs the relationship between shareholders, the operation of the board, economic rights, and exit mechanics. It fills the gaps that company law and articles leave open, and it is enforceable between the contracting parties even where the articles are silent.

## When to use this

- VC investment (Series A or later) completing the investment alongside a term sheet
- Seed or early-stage startup with multiple co-founders formalizing their relationship
- Joint venture between two or more corporate parties
- Family business bringing in an external investor or formalizing governance
- PE-backed buyout establishing post-acquisition governance
- Any private company with more than one shareholder wanting governance certainty

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company (name, jurisdiction, entity type, share capital) | Determines which company law applies and what the SHA can override | Must provide |
| Shareholders (names, ownership % at signing) | Parties to the agreement and initial cap table | Must provide |
| Governance: board size, composition, reserved matters threshold | The core governance bargain | Must agree before drafting |
| Transfer restrictions: lock-up, ROFR, ROFO, drag, tag | Determines liquidity and control | Standard investor-friendly defaults below |
| Exit mechanics: IPO trigger, drag threshold, deadlock resolution | How shareholders get out | Must agree |

## Optional inputs

- Preferred share terms (liquidation preference, anti-dilution, conversion)
- Founder vesting terms (if not already in employment contracts)
- Special information rights
- Option pool size and plan summary

## Document Structure

### 1. Definitions and Interpretation
Define: Affiliate, Bad Leaver, Good Leaver, Change of Control, Drag Threshold, ROFR Notice, Reserved Matter, Exit. Note: definitions should be consistent with the articles of association.

### 2. Share Capital and Cap Table

State the current capitalization:
- Class of shares (ordinary, preferred, if any)
- Holder names and holdings
- Total authorized and issued share capital
- Form of Schedule (cap table) — update mechanism should be built in (company secretary certifies current cap table monthly)

### 3. Pre-emption Rights

New share issuances must be offered to existing shareholders in proportion to their holdings before being offered to third parties. Key parameters:
- Offer period: typically 15–30 days
- Price: at the proposed subscription price
- Carve-outs: option pool grants, shares issued pursuant to pre-agreed financing rounds, shares issued on conversion of approved instruments (SAFEs, convertible notes)

### 4. Reserved Matters

A list of actions the company cannot take without the consent of a specified percentage of shareholders (typically 75% or 100% for the most sensitive). A sample reserved matters list:

| Matter | Typical threshold |
|---|---|
| Issue new shares (outside approved option pool or pre-agreed rounds) | 75% |
| Approve a new business plan or material deviation from approved plan | 75% |
| Approve acquisition of another company | 75% |
| Approve disposal of material assets (>10–15% of net assets) | 75% |
| Change of CEO / CFO | Board only, or 50% |
| Approve related-party transactions above a threshold | 75% |
| Incur indebtedness above agreed threshold | 75% |
| Amend the SHA or articles | 100% |
| Wind up or dissolve the company | 75% or 100% |
| Change of company name | 75% |
| Declare a dividend | Board only (ordinary) or 75% (if distributable profits disputed) |
| Approve a key employee share plan | 75% |

Founders want a narrow list; investors want a broad list. The negotiation typically lands at 15–25 items.

### 5. Board Composition and Rotation

- Board size (typically 3–7 members in early-stage; larger in mature companies)
- Investor board seat: one lead-investor-appointed director per investment round is standard
- Founder board seat: typically guaranteed as long as founder holds above a minimum %
- Independent director: one industry expert; often required by institutional investors
- Observer rights: non-director right to attend board meetings (no vote); investors outside the lead often receive this
- Board quorum: majority of directors, including at least one investor-appointed director and one founder-appointed director (deadlock prevention)

### 6. Information Rights

| Information | Frequency | Recipient |
|---|---|---|
| Management accounts (P&L, balance sheet, cash flow) | Monthly | All shareholders above a threshold holding |
| Annual audited financial statements | Within 90–120 days of year-end | All shareholders |
| Annual budget / business plan | Before start of fiscal year | All shareholders |
| Notice of material adverse events | Promptly | All shareholders |
| Board meeting materials | 7 days before meeting | Directors + observers |
| Cap table certificate | On request | All shareholders |
| Audit rights | On reasonable notice, max twice per year | Investor-appointed directors |

### 7. Transfer Restrictions

#### Lock-up
- Founders are locked up for 3–4 years; transfers within the lock-up period require board and/or majority investor approval
- Some SHAs distinguish between complete lock-up (no transfers at all) and a lock-up with leakage permissions (estate planning, transfers to wholly-owned entities of the founder)

#### Right of First Refusal (ROFR)
Before transferring shares to a third party, the selling shareholder must first offer the shares to existing shareholders at the same price and terms. Process:
1. Seller gives ROFR notice with the proposed price and buyer identity
2. Existing shareholders have 20–30 days to exercise
3. If not fully exercised, seller may proceed to third party within a limited window (typically 60–90 days) at no less than the offered price

#### Right of First Offer (ROFO)
Alternative to ROFR (less common): selling shareholder must invite offers from existing shareholders before approaching third parties. Less certain for the selling shareholder; preferred by buyers (they set the pace).

#### Drag-Along
Holders of [50–75%] of shares may force all other shareholders to sell their shares in the same transaction at the same price and on the same terms. Key drafting parameters:
- Drag threshold (founders want high; investors want low to enable a trade sale)
- Price floor (drag may not be exercised below a certain price per share)
- Sale process fairness (bank opinion on price; approved by independent director)

#### Tag-Along
If a controlling shareholder sells, minority shareholders have the right to join the sale and sell their shares at the same price and on the same terms. Prevents the majority from selling a control premium without sharing it with the minority.

#### Permitted Transfers
Exempt from ROFR: transfers to a wholly-owned affiliate of the transferor, transfers for estate planning to family trusts (provided the original shareholder retains control), transfers under a drag-along.

### 8. Anti-Dilution Protections

Protects investors against future down rounds. Two main mechanisms:

| Mechanism | How it works | Who it favors |
|---|---|---|
| Full ratchet | Conversion price adjusts to the new (lower) price; highly dilutive to founders | Investor (very aggressive; rare in standard rounds) |
| Broad-based weighted average | Conversion price adjusts based on a formula that accounts for the number of new shares issued; less dilutive | Market standard; balances investor protection with founder fairness |

Carve-outs (do not trigger anti-dilution): option pool grants, shares issued on exercise of pre-agreed instruments, shares issued in connection with equipment leasing or bank financing.

### 9. Liquidation Preference

On a liquidation, wind-up, or deemed liquidation (acquisition where proceeds are distributed):
- **1x non-participating**: investor receives 1x their invested amount first; excess goes to all shareholders pro rata (standard for Series A)
- **1x participating**: investor receives 1x their invested amount first, then participates pro rata with ordinary shareholders in the remaining proceeds (more aggressive)
- **Multiple participating**: 2x or higher; founder-unfriendly; rare in strong founder markets

### 10. Founder Vesting

If founders are not subject to vesting through their employment agreements, the SHA should impose:
- Standard: 4-year monthly vesting with 12-month cliff (25% at month 12; 1/48 per month thereafter)
- Acceleration: double trigger (change of control + termination within 12–24 months) is market standard; single trigger is negotiated as a founder-friendly concession
- Good leaver / bad leaver definitions for founders who depart (see [[draft-vesting-schedule]])
- Repurchase option: company may repurchase unvested shares from a departing founder at par value

### 11. Exit Mechanics

#### IPO
- IPO trigger: requires approval of [75%] of shareholders
- Lock-up post-IPO: founders and existing investors subject to 90–180-day lock-up post-listing
- Cooperation: all shareholders cooperate with underwriters' requirements; no blocking of IPO process

#### Trade Sale
- Drag-along mechanics (see above) enable a forced sale
- Board process: typically requires independent financial advisor's opinion on fairness of price

#### Deadlock Resolution
If the board or shareholders are deadlocked on a reserved matter, typical mechanisms:
1. Escalation to senior management/founders (informal cooling-off)
2. Mediation (structured, time-limited)
3. Buy-sell (Russian roulette): either party may trigger; one party names a price; the other must buy at that price or sell at that price
4. Compulsory winding-up (last resort; may destroy value)

### 12. Confidentiality and Non-Compete

- Shareholders (particularly investor-appointed directors who see competitively sensitive information) are bound by confidentiality
- Non-compete on shareholders with active roles in the business: should mirror employment contract provisions and be reasonable in scope and duration

### 13. Governing Law and Dispute Resolution

- Arbitration (DIAC, ADGM Arbitration, ICC, LCIA, AAA) is strongly preferred for MENA-nexus SHAs because court enforcement of SHA terms (especially drag-along mechanics) is less reliable in civil-law systems
- Governing law: English law (for DIFC / ADGM structures); KSA law (for KSA-licensed entities); Lebanese law (for LB SARLs)

## Jurisdictional Adaptations

### DIFC / ADGM
Full English-law SHA conventions apply. SHA is a private document between shareholders; the Articles of Association are the public constitutional document. Provisions restricting share transfer in the SHA should be mirrored in the articles to bind future transferees who may not be party to the SHA.

### UAE Onshore
LLCs are governed by Federal Decree-Law 32/2021. The SHA supplements the company's Memorandum and Articles of Association (MOA). Crucially:
- The MOA is a public document filed with the DED; the SHA is private
- Transfer restrictions in the SHA must be consistent with the MOA to be enforceable
- Some SHA provisions (pre-emption, drag-along) are not well-established in UAE onshore courts; arbitration is essential

### KSA
LLCs are governed by the Companies Law. Capital increases and transfer of shares require notarization and registration with the Ministry of Commerce. SHA terms should be consistent with the company's Articles and the Companies Law; reserved matters beyond what the Companies Law prescribes are enforceable contractually (between shareholders) but may not bind third parties.

### Lebanon
SAL (Société Anonyme Libanaise) and SARL (Société à Responsabilité Limitée) are governed by the Lebanese Code of Commerce. SHA fills the gap left by the code. Drag-along enforcement requires consent of all partners under SARL rules (since a partner change requires all partners' agreement); structure as a drag "obligation to vote" rather than an automatic forced transfer.

## Classic Deal-Breaker Tension Points

| Issue | Founder position | Investor position | Compromise |
|---|---|---|---|
| Drag threshold | High (>75%) | Low (<50%) | 50–75% with price floor |
| Reserved matters list | Narrow (5–10 items) | Broad (20+ items) | ~15 items with materiality thresholds |
| Anti-dilution | Narrow-based weighted average | Broad-based weighted average or full ratchet | Broad-based weighted average |
| Vesting acceleration | Single trigger | Double trigger | Double trigger with 25% single-trigger concession |
| Pre-emption proportionality | Founders can buy more than their pro rata (blocking) | Pro-rata only | Pro-rata with over-allotment right for lead investor |
| Information rights threshold | High (only major shareholders) | Low (all investors including small angels) | Threshold at ~3–5% holding |
| Deadlock resolution | No mechanism (preserves status quo) | Buy-sell / Russian roulette | Mediation first, then buy-sell after 60 days |

## Related skills

- [[draft-term-sheet-vc]]
- [[draft-safe]]
- [[draft-articles-of-association]]
- [[draft-share-purchase-agreement]]
- [[draft-vesting-schedule]]
- [[review-sha-founder-side]]
