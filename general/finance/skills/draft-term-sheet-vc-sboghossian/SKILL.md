---
name: draft-term-sheet-vc-sboghossian
title: VC Term Sheet (Priced Round)
description: Use when drafting a non-binding term sheet for a priced VC investment round (Seed, Series A, or later). Covers all standard VC term sheet provisions including share type, pre-money/post-money mechanics, option pool, anti-dilution, liquidation preferences, protective provisions, board composition, ROFR/co-sale/drag, information rights, founder vesting, and the no-shop. Marks binding vs non-binding sections explicitly. Notes that DIFC and ADGM are increasingly the preferred jurisdictions for MENA tech VC rounds in preference to onshore UAE or KSA.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-term-sheet-vc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# VC Term Sheet (Priced Round)

A VC term sheet is the blueprint for a priced equity investment — it specifies the commercial terms of the deal (valuation, share type, economic rights, governance rights, protective provisions) before the parties incur the cost of definitive documentation. A well-drafted term sheet eliminates the costly surprises that derail deals during documentation.

## When to use this

- Lead investor has concluded preliminary due diligence and is ready to propose terms
- Company has received a verbal indication of interest and needs to formalize the term sheet
- Reviewing / negotiating an incoming term sheet (see [[review-term-sheet-founder-side]] / [[review-term-sheet-investor-side]])
- Converting a SAFE or convertible note to equity through a priced round

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company + founders + current cap table | Post-money calculation requires precise pre-money cap table | Must provide |
| Lead investor + syndicate members | Determines who signs; who has board seats | Must provide |
| Round size | Total investment amount | Must provide |
| Pre-money vs post-money valuation | The single most negotiated number; affects everyone's dilution | Pre-money valuation is standard; clarify explicitly |
| Option pool size and timing | Whether pool is created pre-investment (dilutes founders more) or post-investment (dilutes everyone) | Option pool shuffle pre-money is investor standard; founders resist |
| Liquidation preference | Economic protection for investors on exit | 1x non-participating is market standard for Series A |
| Board composition | Who controls the board | Must agree before signing |

## Complete Term Sheet Structure

### I. OFFERING TERMS

#### Security
Preferred Stock ("Series A Preferred" or "Seed Preferred") — or the applicable designation.

#### Pre-Money Valuation
[Amount]. This is the value of the company immediately before the investment. Post-money = Pre-money + investment amount.

**Option pool mechanics (the "option pool shuffle"):**
Pre-money valuation is typically calculated on a fully diluted basis including an option pool of [X]% of the post-closing fully diluted capitalization. If the pool is insufficient, it must be increased before closing — this dilutes founders, not investors. The term sheet should state whether the pre-money valuation is calculated on a pre-pool-expansion or post-pool-expansion basis.

#### Investment Amount
[Total round size], of which Lead Investor commits [Amount] and other investors [Amount]. May include a pro-rata right for existing investors (angels, SAFEs, etc.) if they are participating.

#### Per-Share Price
[Amount] per share, calculated as: Pre-Money Valuation ÷ Fully Diluted Pre-Money Share Count. Attach a pre/post money cap table as Exhibit A.

#### Dividends
Non-cumulative preferred dividends at [8%] per annum, payable if and when declared by the Board. Alternatively: dividends payable only on liquidation or redemption, prior to distributions to ordinary shareholders.

Market standard: non-cumulative dividends that are declared at board discretion; cumulative dividends are investor-aggressive and founder-unfriendly.

---

### II. ECONOMIC TERMS

#### Conversion
- Voluntary: investor may convert Preferred to Ordinary at any time at 1:1 ratio
- Mandatory: automatic conversion on a Qualified IPO (proceeds ≥ [X] at price ≥ [Y]x the Series A price) or vote of holders of [>50%] of Preferred

#### Anti-Dilution
**Broad-based weighted average** (market standard): if the company issues new shares at a price below the Series A price, the conversion price of the Series A Preferred adjusts by a weighted average formula that accounts for the relative number of new shares vs existing shares.

Full-ratchet anti-dilution (conversion price adjusts fully to the new lower price) is highly founder-unfriendly and should be resisted.

Anti-dilution adjustments are not triggered by: option grants, conversion of SAFEs/notes issued in prior rounds, shares issued in acquisition transactions, equipment leasing, bank debt.

#### Liquidation Preference
- **Amount**: [1x] the original Series A purchase price, plus any declared but unpaid dividends ("Preference Amount")
- **Participating vs non-participating**:
  - **Non-participating (standard for Series A)**: on liquidation, investors receive their Preference Amount; if conversion to ordinary and participation would yield more, investors can convert and share pro-rata; excess proceeds after preference go to all shareholders pro-rata
  - **Participating**: investors receive their Preference Amount AND participate pro-rata in all remaining proceeds (double-dip); cap participation at [3x] if this structure is agreed
- **Deemed liquidation events**: include in the definition: merger, consolidation, acquisition where existing shareholders hold <50% post-transaction, sale of all or substantially all assets, exclusive license of all IP; this is critical — without it, investors' liquidation preference may not apply on a common acquisition

#### Redemption
- Investor may demand redemption at [5 years] from closing at [original purchase price + dividends] if the company has not achieved an IPO or trade sale
- Redemption in 3 annual installments to reduce cash impact
- Market standard: no redemption right; redemption is an investor-aggressive term resisted by founders and co-investors

---

### III. GOVERNANCE TERMS

#### Board of Directors

| Seat | Appointed by | Held by |
|---|---|---|
| [1] | Lead Investor | Lead Investor's designee |
| [2] | Founders (jointly) | Founder CEO or designated founder |
| [1] | Mutual agreement | Independent director (industry expert) |

Total: [3 or 5] directors. Investor-appointed director approval required for reserved matters (see below).

#### Observer Rights
[Other named investors] shall have the right to attend board meetings as non-voting observers, provided they hold ≥ [X]% of the outstanding Preferred. Observers are bound by confidentiality.

#### Protective Provisions (Reserved Matters)
The consent of holders of [>50%] of the outstanding Preferred is required for:
1. Amend the articles of association in a manner adversely affecting the rights of the Preferred
2. Create or authorize any security senior to or pari passu with the Preferred
3. Issue any securities except pursuant to approved share plans or agreed future rounds
4. Declare or pay dividends on Ordinary shares before all accrued dividends on Preferred are paid
5. Redeem, repurchase, or retire any Ordinary shares (except buybacks from terminated employees at cost)
6. Liquidate, dissolve, or wind up the company
7. Acquire another company or business for consideration exceeding [X]
8. Undertake material indebtedness (exceeding [Y] in aggregate)
9. Change the nature of the company's business materially
10. Approve any transaction with a related party (founders, existing investors) above [Z] per year

---

### IV. TRANSFER AND EXIT TERMS

#### Right of First Refusal (ROFR) and Co-Sale (Tag-Along)

**ROFR**: Before any founder or major shareholder (holding ≥[X]%) transfers shares, they must first offer them to the Company (10-day right), then to the investors pro-rata (20-day right).

**Co-Sale / Tag-Along**: If a founder transfers shares to a third party after ROFR is not exercised, each investor may participate in the sale pro-rata, on the same terms.

#### Drag-Along
Holders of ≥[50–75]% of all outstanding shares (on an as-converted basis) may require all shareholders to sell their shares in a bona fide arm's-length acquisition on the same terms. Drag exercise requires approval of: the Board AND [>50%] Preferred holders AND [>50%] Ordinary holders.

#### Pre-Emption on New Issues
On new share issuances (excluding option grants and agreed future rounds), investors have the right to participate pro-rata to maintain their percentage ownership.

#### Pro-Rata Rights in Future Rounds
Major investors (holding ≥[X]% of outstanding Preferred) have a right to invest their pro-rata share in any future financing round at the same price and terms offered to other investors.

---

### V. INFORMATION AND REPORTING RIGHTS

| Information | Frequency | Threshold for eligibility |
|---|---|---|
| Monthly management accounts | Monthly (within 10 days of month-end) | ≥[X]% holding |
| Annual audited financial statements | Annually (within 90 days of year-end) | All Preferred holders |
| Annual budget and business plan | Before start of fiscal year | All Preferred holders |
| Board meeting materials | 7 days before each meeting | Directors and observers |
| Cap table | On request (quarterly certification) | All Preferred holders |

Investors above a threshold also have reasonable audit rights (on 5 business days' notice; not more than twice per year).

---

### VI. FOUNDER PROVISIONS

#### Founder Vesting
All founders' shares that are unvested as of the closing date shall be subject to:
- **4-year monthly vesting with 12-month cliff**: 25% vests at month 12 from the founder's commencement date (not from the investment date); remainder vests in equal monthly installments over the following 36 months
- **Acceleration**: double-trigger acceleration — if (a) a change of control occurs AND (b) the founder is terminated without cause or resigns for good reason within [12] months after the change of control, [100%] of the founder's unvested shares accelerate
- **Repurchase right**: unvested shares may be repurchased by the company at par value on departure; vested shares are retained by the departing founder
- **Good leaver / bad leaver**: on departure for cause (bad leaver), company may repurchase vested shares at the lower of cost and market; on departure without cause (good leaver), vested shares are retained

---

### VII. CONDITIONS, EXCLUSIVITY, AND EXPENSES

#### No-Shop / Exclusivity
From the date of execution until [30–45 days], the company and its founders shall not, directly or indirectly, solicit, initiate, or enter into discussions or negotiations with any other person regarding an alternative financing of any kind.

**This clause is BINDING.**

#### Conditions Precedent
- Completion of satisfactory due diligence by Lead Investor
- Execution of definitive documentation (SHA, articles, subscription agreement)
- Board and shareholder approvals
- Legal opinions from counsel in the company's jurisdiction

#### Expenses
The company shall reimburse Lead Investor's reasonable legal fees in connection with the transaction, up to [Amount], regardless of whether the transaction closes.

---

### VIII. BINDING VS NON-BINDING

**BINDING provisions** (effective from signature):
- Exclusivity / No-shop (Section VII)
- Confidentiality
- Expense reimbursement cap (Section VII)
- Governing law for the term sheet

**NON-BINDING provisions**: all economic, governance, and transfer terms — these are subject to negotiation during definitive documentation and are contingent on completion of due diligence and legal review.

---

### IX. GOVERNING LAW

For MENA tech rounds:
- **DIFC or ADGM**: English-law-governed SHA; DIFC or ADGM Courts or arbitration; widely preferred by institutional investors for enforceability and sophistication of the forum
- **Delaware (US)**: if the company has a Delaware holding company (common for US VC participation); Delaware corporate law applies; standard NVCA documentation
- **KSA**: if the company is a KSA-incorporated entity, the SHA and investment terms must comply with KSA Companies Law; institutional investors may require a DIFC or Delaware holdco above the KSA opco

## Common Mistakes

- **Pre-money vs post-money confusion**: "USD 5M at USD 20M" — does this mean USD 20M pre-money (so USD 25M post-money, 20% dilution) or USD 20M post-money (so USD 15M pre-money, 25% dilution)? State "pre-money valuation" explicitly.
- **Option pool not modeled**: forgetting to model the option pool expansion before calculating per-share price; this inflates apparent dilution for founders
- **Non-participating preference on low exits**: with 1x non-participating preference on a 3x liquidation, investors prefer to convert; the liquidation preference only has value on small exits; model several scenarios to understand the economics
- **No cap on participation**: participating preferred without a cap creates an investor windfall on large exits; founders should push for a [3x] cap on participation before conversion
- **"Qualified IPO" definition**: if the bar is set too high (price per share, total proceeds), the mandatory conversion trigger may never be met and investors hold preferred indefinitely
- **Drag-along requiring unanimity**: if drag requires 100% consent, a single minority holder can block a trade sale; market practice is 50–75% threshold with Board approval

## Related skills

- [[draft-shareholders-agreement]]
- [[draft-safe]]
- [[draft-vesting-schedule]]
- [[review-term-sheet-founder-side]]
- [[review-term-sheet-investor-side]]
