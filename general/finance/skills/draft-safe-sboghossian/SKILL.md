---
name: draft-safe-sboghossian
title: SAFE — Simple Agreement for Future Equity
description: Use when drafting a SAFE (Simple Agreement for Future Equity) for a startup funding round — based on the Y Combinator post-money SAFE standard, adapted for DIFC/ADGM/Delaware, or adapted for civil-law jurisdictions (LB/FR as "promesse de souscription") or KSA (where convertible debt may be preferable). Covers key economic terms (valuation cap, discount rate, MFN), conversion mechanics (equity financing, liquidity event, dissolution), jurisdictional adaptations, and the critical distinction from convertible notes. Triggers on "SAFE", "simple agreement for future equity", "convertible instrument", "pre-seed funding", or "startup financing" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-safe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# SAFE — Simple Agreement for Future Equity

## When to use this

A SAFE is a short-form investment instrument used in early-stage startup financing. The investor provides cash to the company today in exchange for the right to receive equity (shares) in the future, at a price calculated by reference to the company's next priced funding round. SAFEs are not loans — they have no maturity date, no interest, and do not create debt.

Use this skill when:
- A startup is raising pre-seed or seed capital from angel investors or VCs who accept SAFE structures
- Speed and simplicity are valued over extensive negotiation (SAFEs are typically 5-8 pages)
- The company is not ready for a priced round (no agreed valuation) but needs capital now
- The jurisdiction accepts SAFE structures (DIFC, ADGM, Delaware, Singapore — yes; civil-law MENA with adaptation)

If the parties want a maturity date and interest, use [[draft-convertible-note]] instead. SAFEs are NOT convertible notes.

## Key economic terms — inputs

| Term | What it means | Typical range |
|------|--------------|--------------|
| **Purchase Amount** | The cash invested today | USD 50k to several million |
| **Valuation Cap** | Maximum company valuation at which the SAFE converts; investor's protection against conversion at a very high price | USD 1M to USD 20M+ (pre-seed); higher for seed |
| **Discount Rate** | Investor receives shares at a discount to the next round price | 10-25% (so discount rate = 80-90% of the next round price) |
| **MFN clause** | If company issues subsequent SAFEs on better terms, this SAFE gets upgraded to those terms | Standard: yes |
| **Pro-rata right** | Investor's right to maintain their ownership % by participating in future rounds | Optional — often in a separate side letter |

**Post-money SAFE (YC standard since 2018)**: the Valuation Cap is calculated on a post-money basis (includes the current financing round and SAFE pool). This makes dilution calculations more predictable for both parties.

## Standard YC SAFE — key clauses

### 1. Definitions

**Equity Financing**: a priced round in which the company issues preferred stock to investors for cash, raising at least [a threshold, e.g., USD 1 million] in aggregate proceeds. This is the trigger for SAFE conversion.

**Liquidity Event**: a change of control, merger, or acquisition, or an IPO. Triggers SAFE conversion or payout.

**Dissolution Event**: winding up, bankruptcy, or assignment for benefit of creditors. Triggers return of purchase amount.

**Conversion Price**: the price per share at which the SAFE converts, calculated as the lesser of:
- (a) the **Valuation Cap Price** = Valuation Cap ÷ Company Capitalization (post-money basis)
- (b) the **Discount Price** = the next Equity Financing price per share × (1 - Discount Rate)

If only a Valuation Cap (no discount): use (a) only.
If only a Discount Rate (no cap): use (b) only.
If both: use the lesser of (a) and (b) — Investor gets the better deal.

**Company Capitalization** (for post-money cap calculation): includes all issued shares + all options outstanding + all conversion shares from all SAFEs (including this one). This is the key post-money definition — it means the SAFE holder knows exactly what percentage their cap implies.

### 2. Conversion on Equity Financing

Upon a qualifying Equity Financing:
- The SAFE automatically converts into shares of the class issued in the Equity Financing (typically Series A preferred stock)
- Number of shares = Purchase Amount ÷ Conversion Price
- Investor receives the same class of stock as the lead investor in the Equity Financing, with the same terms, rights, and preferences

**No action required by either party** — conversion is automatic upon the closing of the Equity Financing.

### 3. Conversion on Liquidity Event

Upon a Liquidity Event (M&A, IPO):
- Investor may elect either:
  - (a) Convert at the Conversion Price (using Valuation Cap Price if the M&A valuation is above the cap) and receive merger consideration as an equity holder; or
  - (b) Receive a cash payment equal to the greater of: (i) the Purchase Amount, or (ii) the amount the Investor would have received if they had converted immediately before the Liquidity Event

This gives the Investor the better of: full conversion upside (if the M&A price is above the cap) or return of capital (if the M&A price is below the Purchase Amount per implied share).

### 4. Dissolution

If the Company winds up before an Equity Financing or Liquidity Event:
- SAFE holders are paid the Purchase Amount out of available assets
- SAFE holders rank after creditors but before equity holders (common stockholders)

### 5. MFN — Most-Favored-Nation

"If the Company issues any Subsequent Convertible Securities [SAFEs or convertible notes] to any other investor within [12] months of the Effective Date on terms that are more favorable to such investor than the terms of this SAFE (including, without limitation, a lower Valuation Cap, a higher discount rate, or any security or collateral), the Company shall promptly notify the Investor and, at the Investor's option, the terms of this SAFE shall be automatically amended to match the more favorable terms."

**Practical effect**: prevents the company from "round-tripping" — raising additional SAFEs on better terms from later investors while this earlier Investor is stuck on worse terms.

### 6. Company representations
The company represents (at the time of signing):
- It is duly organized and authorized to issue this SAFE
- The SAFE constitutes its valid and binding obligation
- No conflict with existing agreements or applicable law
- No litigation pending that would materially affect the company's ability to perform

### 7. Investor representations
The investor represents:
- It is an accredited investor (US) or equivalent sophisticated investor (other jurisdictions)
- It is acquiring the SAFE for investment purposes, not for distribution
- It understands the SAFE is a speculative instrument; the investment may result in total loss

### 8. No voting rights, no interest, no maturity

State plainly:
- "This instrument does not create any debt obligation. It is not a loan. No interest accrues."
- "The Investor has no voting rights prior to conversion."
- "There is no maturity date; this instrument remains outstanding until a conversion event occurs or the Company dissolves."

### 9. Pro-rata side letter (separate, optional)

The pro-rata side letter gives the Investor the right to invest in the Equity Financing to maintain their post-conversion ownership percentage. This is typically a separate one-page letter, not incorporated into the SAFE itself. If requested, draft it as a standalone exhibit.

## Jurisdictional adaptations

| Jurisdiction | Adaptation |
|---|---|
| **Delaware (US)** | Standard YC post-money SAFE works directly; widely understood by investors and lawyers; governed by Delaware corporate law |
| **DIFC** | Standard YC post-money SAFE structure is well-understood; governed by DIFC Contract Law and Companies Law; common-law enforcement; DIFC entities (SPCCs) can issue SAFEs |
| **ADGM** | Same as DIFC; ADGM Companies Regulations 2015; common-law enforcement |
| **Lebanon (LB) / France (FR)** | Civil-law adaptation required. A SAFE in civil-law form is characterized as a "promesse unilatérale de souscription" (unilateral subscription promise) with a conversion condition. The instrument must comply with the applicable commercial code requirements for convertible instruments. Recommended: use a DIFC or Delaware holding company to issue SAFEs if investors are sophisticated; avoid issuing a civil-law SAFE directly at the operating company level without specialist corporate advice |
| **KSA** | Ambiguity under Saudi corporate and Sharia law regarding the treatment of future-equity instruments. The uncertainty (gharar) inherent in a SAFE's conversion mechanism may be challenged. **Recommended alternative for KSA**: use a convertible debt instrument (murabaha-based or otherwise Sharia-compliant convertible note) rather than a SAFE. If the company is incorporated in DIFC or ADGM, the SAFE can be issued at that level with the Saudi operating company as the business vehicle below |

## SAFE vs Convertible Note — key differences

| Feature | SAFE | Convertible Note |
|---|---|---|
| Debt instrument | No | Yes |
| Maturity date | None | Yes (typically 18-24 months) |
| Interest | None | Yes (typically 4-8% per annum) |
| Conversion trigger | Equity Financing / Liquidity Event | Same, or maturity if not converted |
| Balance sheet treatment | Equity instrument (typically) | Debt (liability) |
| Sharia compatibility | Problematic (uncertain future equity) | Can be structured as Sharia-compliant |

The SAFE is appropriate where the parties accept that conversion may never happen (dissolution risk) and where the Investor is investing in the company's growth potential. The convertible note is appropriate where the Investor wants downside protection through debt treatment and an assured maturity date.

## Common mistakes

- **Treating a SAFE as convertible debt** — drafting it with maturity dates and interest rates; this destroys the SAFE's simplicity and creates debt-instrument complications
- **Omitting the MFN clause** — subsequent investors get a lower cap; this SAFE investor is permanently disadvantaged
- **Using a pre-2018 YC SAFE (pre-money)** — the pre-money SAFE creates dilution calculation uncertainty; use the post-money version
- **LB/FR civil-law SAFE without corporate law advice** — the instrument may not be valid or enforceable under the applicable corporate law without specific adaptations
- **KSA operating company issuing a SAFE directly** — Sharia ambiguity and regulatory uncertainty; use an offshore holding company instead

## Critical — SAFEs are not loans

"SAFEs are NOT loans. Do not draft them as convertible notes. If parties want maturity + interest, use [[draft-convertible-note]]."

## Related skills

- [[draft-convertible-note]]
- [[draft-shareholders-agreement]]
- [[draft-joint-venture]]
- [[review-term-sheet]]
