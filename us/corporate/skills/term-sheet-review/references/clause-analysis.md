# Clause-by-Clause Analysis Guide

Detailed guidance for analyzing each term sheet clause.

## Table of Contents
1. [Valuation](#1-valuation)
2. [Liquidation Preference](#2-liquidation-preference)
3. [Dividends](#3-dividends)
4. [Anti-Dilution](#4-anti-dilution)
5. [Pay-to-Play](#5-pay-to-play)
6. [Board Composition](#6-board-composition)
7. [Protective Provisions](#7-protective-provisions)
8. [Drag-Along Rights](#8-drag-along-rights)
9. [Voting Rights](#9-voting-rights)
10. [Pro-Rata Rights](#10-pro-rata-rights)
11. [Information Rights](#11-information-rights)
12. [Registration Rights](#12-registration-rights)
13. [ROFR and Co-Sale](#13-rofr-and-co-sale)
14. [Founder Vesting](#14-founder-vesting)
15. [No-Shop Period](#15-no-shop-period)

---

## 1. Valuation

### What to Look For
- Pre-money vs. post-money valuation
- Option pool size and whether it's in pre-money
- Fully-diluted basis (includes all options, warrants, convertibles)

### Analysis Framework

**Option Pool Shuffle**: If option pool is included in pre-money, calculate the effective pre-money:
```
Effective Pre-money = Stated Pre-money - Option Pool Value
```

Example: $10M pre-money with 20% option pool on $12M post = $2.4M pool
- Founders effectively getting $7.6M pre-money valuation

### Investor Perspective
- Higher valuation = lower ownership percentage
- Option pool in pre-money protects against dilution
- Consider: Is valuation justified by traction/market?

### Startup Perspective
- Lower valuation = more dilution
- Negotiate option pool size based on actual 18-month hiring needs
- Consider: Will high valuation create down-round risk?

### Negotiation Tips
**For startups**: Push for option pool sized to actual hiring plan, not arbitrary 20%
**For investors**: Ensure fully-diluted includes all outstanding convertibles

---

## 2. Liquidation Preference

### What to Look For
- Multiple (1x, 1.5x, 2x)
- Participating vs. non-participating
- Seniority (pari passu vs. senior)
- Deemed liquidation events definition

### Analysis Framework

Calculate payout scenarios at different exit values:

**Non-participating 1x** (market standard):
- Exit < Investment: Investor gets all proceeds
- Exit > Investment: Investor chooses preference OR conversion (takes better option)

**Participating 1x** (double-dip):
- Investor gets 1x preference PLUS pro-rata share of remainder

Example: $10M investment for 20% at $50M exit
- Non-participating: $10M (preference) vs $10M (20% of $50M) = $10M
- Participating: $10M + 20% of $40M remaining = $18M

### Investor Perspective
- Downside protection in modest exits
- Participating preferred maximizes returns in middle exits
- Multiple preferences protect against down rounds

### Startup Perspective
- Non-participating preserves upside for common shareholders
- Participating can wipe out common in middle exits
- Multiple preferences make modest exits worthless for founders

### Negotiation Tips
**For startups**: 1x non-participating is market; push back hard on participating or multiples
**For investors**: If seeking participating, consider a cap (e.g., 3x total return)

---

## 3. Dividends

### What to Look For
- Rate (typically 6-8%)
- Cumulative vs. non-cumulative
- Payable when declared vs. accruing

### Analysis Framework

**Non-cumulative** (market): Only paid if board declares; rarely actually paid
**Cumulative**: Accrues whether or not declared; adds to liquidation preference over time

Example: $10M investment with 8% cumulative dividend over 5 years
- Adds $4M to liquidation preference = $14M before common sees anything

### Investor Perspective
- Cumulative dividends provide time-value compensation
- Rarely actually paid; primarily affects exit math
- Consider if company can actually support dividend payments

### Startup Perspective
- Cumulative dividends silently increase liquidation preference
- Non-cumulative is standard and preferable
- Participating + cumulative is highly unfavorable

### Negotiation Tips
**For startups**: Insist on non-cumulative; it's market standard
**For investors**: If seeking cumulative, consider it compensation for longer hold periods

---

## 4. Anti-Dilution

### What to Look For
- Full ratchet vs. weighted average
- Broad-based vs. narrow-based weighted average
- Exceptions (standard carve-outs)

### Analysis Framework

**Broad-based weighted average formula**:
```
CP2 = CP1 × (A + B) / (A + C)
Where:
- CP2 = New conversion price
- CP1 = Old conversion price
- A = Shares outstanding before new issue
- B = Money raised / CP1 (what you'd get at old price)
- C = Actual shares issued
```

**Full ratchet**: Conversion price drops to new round price entirely

Example: Series A at $1.00, down round at $0.50
- Weighted average: Might adjust to $0.85 depending on round size
- Full ratchet: Drops to $0.50 (2x the shares for Series A investors)

### Standard Exceptions
- Shares issued on conversion of preferred
- Employee options under board-approved plan
- Shares from stock splits/dividends
- Strategic partnership shares (with board approval)

### Investor Perspective
- Protects against down-round dilution
- Full ratchet provides maximum protection
- Consider: Does aggressive anti-dilution discourage future investors?

### Startup Perspective
- Broad-based weighted average is acceptable
- Full ratchet severely punishes founders in any down round
- Narrow-based gives more protection than broad-based

### Negotiation Tips
**For startups**: Broad-based weighted average only; never accept full ratchet
**For investors**: Standard broad-based is sufficient; full ratchet may hurt future fundraising

---

## 5. Pay-to-Play

### What to Look For
- Trigger (any round vs. down round only)
- Consequence (conversion to common vs. loss of specific rights)
- Pro-rata requirement

### Analysis Framework

Pay-to-play requires existing investors to participate in future rounds or face consequences:
- **Soft**: Lose anti-dilution protection or pro-rata rights
- **Hard**: Preferred converts to common stock

### Investor Perspective
- Ensures continued support from existing investors
- Prevents free-riders in difficult rounds
- May limit flexibility if fund is fully deployed

### Startup Perspective
- Helps ensure investor support in tough times
- May complicate future rounds if investors can't participate
- Consider investor fund lifecycle and reserves

### Negotiation Tips
**For startups**: Pay-to-play can be helpful; consider "soft" version
**For investors**: Ensure exceptions for reasonable circumstances (fund timing, etc.)

---

## 6. Board Composition

### What to Look For
- Number of seats and who elects each
- Board size expansion triggers
- Observer rights
- Committee membership requirements

### Analysis Framework

| Configuration | Control | Rating |
|---------------|---------|--------|
| 3 seats: 2F, 1I | Founder control | Founder-friendly |
| 3 seats: 1F, 1I, 1Ind | Balanced | Market (Series A) |
| 5 seats: 2F, 2I, 1Ind | Balanced | Market (Series B+) |
| Any investor majority | Investor control | Investor-friendly |

### Investor Perspective
- Board seat provides governance rights and information
- Observer seat is acceptable alternative
- Committee seats (compensation, audit) provide specific oversight

### Startup Perspective
- Maintain board control through Series A at minimum
- Independent directors should be mutually agreed
- Too many board seats = slower decision-making

### Negotiation Tips
**For startups**: 2 founder + 1 investor for seed/A; independent should be mutually chosen
**For investors**: If can't get seat, negotiate observer rights with full information access

---

## 7. Protective Provisions

### What to Look For
- Scope of veto rights
- Threshold (majority vs. supermajority of preferred)
- Board-level vs. stockholder-level protections

### Standard Provisions (acceptable)
- Charter/bylaw amendments affecting preferred
- Create senior or pari passu stock
- Increase authorized preferred
- Redeem/repurchase shares
- Declare dividends
- Liquidate/sell company
- Change board size

### Aggressive Provisions (negotiate carefully)
- Annual budget approval
- Hire/fire executives
- All debt issuance (vs. above threshold)
- Any equity issuance
- Change business line
- Individual option grants
- Spending above small threshold

### Investor Perspective
- Protections prevent value destruction
- Standard provisions are reasonable governance
- Operational controls may be warranted in distressed situations

### Startup Perspective
- Standard protections are acceptable
- Operational vetos can paralyze the business
- Negotiate thresholds (e.g., debt > $500K vs. any debt)

### Negotiation Tips
**For startups**: Accept standard provisions; push back on operational controls
**For investors**: Consider which protections are truly necessary for investment protection

---

## 8. Drag-Along Rights

### What to Look For
- Trigger threshold (who must approve)
- Minimum price/return thresholds
- Exceptions and limitations

### Analysis Framework

Drag-along forces all shareholders to sell if specified parties approve:
- Typical trigger: Board + majority preferred + majority common
- May include minimum price (e.g., 2x liquidation preference)

### Investor Perspective
- Ensures clean exit without minority holdouts
- Important for acquirer certainty
- Consider: Does threshold protect your interests?

### Startup Perspective
- Acceptable with appropriate triggers
- Ensure common stockholders have voice in approval
- Consider minimum price protection for founders

### Negotiation Tips
**For startups**: Ensure common majority required; consider minimum return threshold
**For investors**: Standard provision; focus on appropriate approval threshold

---

## 9. Voting Rights

### What to Look For
- As-converted voting
- Separate class votes
- Protective provision triggers

### Analysis Framework

Preferred typically votes:
- With common on as-converted basis for most matters
- As separate class for protective provisions
- May have separate vote for board seat election

### Both Perspectives
Generally non-controversial; focus on protective provisions and board composition instead.

---

## 10. Pro-Rata Rights

### What to Look For
- Major investor threshold
- Calculation basis (fully diluted vs. preferred only)
- Over-subscription rights
- Super pro-rata (more than proportional share)

### Analysis Framework

Pro-rata right = maintain ownership percentage in future rounds

Example: 10% owner with pro-rata in $10M round can invest $1M

### Investor Perspective
- Essential right to maintain ownership
- Over-subscription rights valuable when other investors don't participate
- Super pro-rata indicates strong conviction

### Startup Perspective
- Standard for major investors
- Too many pro-rata holders can crowd out new investors
- High major investor threshold limits who gets these rights

### Negotiation Tips
**For startups**: Limit to major investors; set reasonable threshold ($250K-$500K seed, $500K-$1M Series A)
**For investors**: Ensure right covers all future equity (not just preferred)

---

## 11. Information Rights

### What to Look For
- Financial statement frequency (monthly, quarterly, annual)
- Audit requirements
- Budget and capitalization table
- Access to facilities/management

### Standard Package
- Annual audited financials
- Quarterly unaudited financials
- Monthly financials (for major investors)
- Annual budget (30 days before fiscal year)
- Updated cap table (quarterly)

### Investor Perspective
- Information rights essential for portfolio monitoring
- Monthly financials help identify issues early
- Management access enables value-add support

### Startup Perspective
- Standard information rights are acceptable
- Consider administrative burden of frequent reporting
- Limit access to competitors

### Negotiation Tips
**For startups**: Exclude competitors from information rights
**For investors**: Ensure information rights survive as long as investment does

---

## 12. Registration Rights

### What to Look For
- Demand registration (how many, when)
- S-3 registration rights
- Piggyback rights
- Lock-up provisions
- Expenses

### Analysis Framework

Registration rights matter primarily for IPO scenarios:
- **Demand**: Force company to register shares (usually 3-5 years post-closing)
- **S-3**: Shelf registration (lower cost, after company is public)
- **Piggyback**: Join company's registration statement

### Both Perspectives
Less negotiated in early stages; more important in growth rounds. Standard provisions are generally acceptable.

---

## 13. ROFR and Co-Sale

### What to Look For
- Company vs. investor ROFR
- Co-sale (tag-along) rights
- Permitted transfers
- Process and timing

### Analysis Framework

**ROFR**: Company/investors can purchase shares before third-party sale
**Co-sale**: Investors can sell alongside founder in third-party sale

### Investor Perspective
- Prevents founders from cashing out while investors hold illiquid stock
- ROFR prevents undesirable shareholders
- Co-sale provides liquidity opportunity

### Startup Perspective
- Standard provisions are acceptable
- Ensure permitted transfers for estate planning
- Process shouldn't unduly delay legitimate sales

### Negotiation Tips
**For startups**: Ensure reasonable permitted transfers (trusts, family members)
**For investors**: Focus on co-sale rights; ROFR provides information and control

---

## 14. Founder Vesting

### What to Look For
- Vesting schedule (typically 4 years monthly)
- Cliff period (typically 1 year)
- Credit for prior service
- Acceleration (single vs. double trigger)

### Analysis Framework

**Standard**: 4-year vesting, 1-year cliff, monthly thereafter

**Single-trigger acceleration**: Vesting accelerates on change of control
**Double-trigger**: Requires change of control AND termination

### Investor Perspective
- Vesting aligns founder incentives with long-term success
- Double-trigger preferred (keeps founders engaged post-acquisition)
- Consider credit for time already invested

### Startup Perspective
- Credit for prior service is reasonable
- Double-trigger acceleration protects against unfair termination
- Consider 50-100% acceleration on double-trigger

### Negotiation Tips
**For startups**: Negotiate credit for time served; double-trigger acceleration
**For investors**: Standard 4-year vesting; double-trigger preferred over single

---

## 15. No-Shop Period

### What to Look For
- Duration (30-90 days)
- Scope (equity, assets, M&A)
- Fiduciary out
- Break-up fee

### Analysis Framework

No-shop prevents company from soliciting other offers during due diligence.

| Duration | Rating |
|----------|--------|
| 30 days | Founder-friendly |
| 45 days | Market standard |
| 60 days | Investor-friendly |
| 90+ days | Aggressive |

### Investor Perspective
- Protects time and expense of due diligence
- Longer period provides more certainty
- Break-up fee compensates if deal falls through

### Startup Perspective
- Shorter period maintains negotiating leverage
- Fiduciary out allows response to superior offers
- Avoid break-up fees in early rounds

### Negotiation Tips
**For startups**: 30-45 days maximum; no break-up fee for early stages
**For investors**: 45-60 days reasonable; fiduciary out is standard
