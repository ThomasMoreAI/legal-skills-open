---
name: review-term-sheet-founder-side-sboghossian
title: Term Sheet Review — Founder Side
description: 'Use when reviewing a VC or angel investor term sheet from the founder''s perspective. Flags the key economic and control provisions that dilute, constrain, or bind founders: option-pool shuffles, participating liquidation preferences, full-ratchet anti-dilution, overly broad protective provisions, drag-along mechanics, and one-sided vesting. Covers MENA startup context (DIFC, ADGM, KSA Vision 2030 ecosystem, UAE) alongside standard US/UK VC term conventions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-term-sheet-founder-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Term Sheet Review — Founder Side

## When to use this

Use when a founder or their counsel receives a VC or angel term sheet and needs to identify the provisions that most significantly affect founder economics, control, and flexibility. This skill is not a substitute for a full legal review of the final investment documents; it is a structured first-pass of the term sheet that flags issues to negotiate before definitive documents are drafted.

For the investor-side perspective, use [[review-term-sheet-investor-side]].

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Term sheet document | The full term sheet, including attachments | Required |
| Stage | Seed, Series A, Series B — changes what is "standard" | Ask if unclear |
| Jurisdiction | DIFC/ADGM/KSA vs US/UK structures differ materially | Ask if not in document |
| Founder's equity position (pre-round) | Needed to model dilution accurately | Helpful; ask if available |
| Investor identity | Known institutional VC vs first-time investor affects market standard calibration | From document |

## Review Methodology

### 1. Valuation — Pre-Money Clarity and Option Pool Shuffle

**Check**: Is the pre-money valuation stated clearly and unambiguously?

**Option pool shuffle (founder's biggest dilution trap)**:
- If the term sheet states "pre-money valuation of USD 10M, post-money of USD 12M, with a 15% option pool to be created pre-closing" — the option pool is created out of the pre-money value, meaning the founders absorb the dilution from the new option pool, not the investor.
- Result: founders' effective pre-money is reduced by the option pool size.
- Better position: negotiate for the option pool to be created post-closing (from the combined cap table), or agree to a smaller pre-closing option pool and expand it post-closing if needed.

**MENA context**: DIFC and ADGM structures follow UK/US VC conventions on option pools. KSA Vision 2030 ecosystem increasingly adopts international VC terms, but Saudi-incorporated companies (closed joint-stock companies / JSCs) have specific requirements for employee share schemes under Saudi Companies Law.

### 2. Liquidation Preference

The liquidation preference determines who gets paid first in a sale, wind-down, or IPO below a certain valuation.

**Standard (founder-acceptable)**: 1× non-participating preferred — investor gets back their investment (or its pro-rata share of proceeds if higher); then remaining proceeds are distributed to common/ordinary shareholders (founders). Investor does not participate in remaining proceeds once preference is satisfied.

**Dangerous variants**:

| Type | Description | Founder impact |
|---|---|---|
| Participating preferred | Investor takes 1× preference AND then participates pro-rata in remaining proceeds | Double-dip — significantly reduces founder exit economics |
| Participating with cap | Participating preferred but capped at 2× or 3× invested amount | Better than uncapped; still not ideal |
| 2× non-participating | Investor takes 2× preference before founders get anything | Heavy; reduces founder returns unless exit is very high |
| Multiple + participating | Worst case; rare in institutional VC | Walk-away territory for most founders |

**Recommendation**: push for 1× non-participating. If investor insists on participating, cap participation at 2–3× and convert to non-participating above the cap.

### 3. Anti-Dilution Protection

Anti-dilution protects investors if the company later raises money at a lower valuation (a "down round").

**Acceptable (market standard)**: Broad-based weighted-average — the conversion price of preferred shares is adjusted using a formula that takes into account both the new shares issued and the total shares outstanding. The adjustment is mild.

**Problematic**: Full ratchet anti-dilution — the investor's conversion price is adjusted to the new, lower round price, regardless of the number of new shares issued. Even a single share issued at a lower price triggers maximum dilution of the founder's stake.

Flag full ratchet as a critical issue. Market norm among institutional VCs is broad-based weighted-average.

**Carve-outs from anti-dilution**: both approaches typically exclude issuances of shares under: the option pool; convertible instruments already outstanding; shares issued as consideration for acquisitions; certain lender warrants. Check that carve-outs are reasonable.

### 4. Board Composition

**Founder-acceptable structure** (early stage):
- 2 founder seats
- 1 investor seat (lead investor)
- 1 independent seat (mutually agreed, ideally agreed-upon definition of "independent")

**Red flags**:
- Investor board seats equal to or exceeding founder seats — founders cannot override investor vetoes
- Investor control over the selection of the "independent" board member — effectively gives investor 2 seats
- Absence of a mechanism to add founder-aligned seats as the company grows

**MENA context**: DIFC companies use common-law board governance; ADGM similar. KSA JSCs have specific board composition rules under Saudi Companies Law — investor rights may need to be structured as shareholder agreements rather than articles of association.

### 5. Protective Provisions (Investor Veto Rights)

Protective provisions give investors a veto over certain company actions even if they are a minority shareholder.

**Reasonable protective provisions** (standard list):
- Sale of the company (whole or majority)
- Issuance of securities senior to or pari passu with the investor's preferred shares
- Amendment to articles / charter that adversely affects the preferred class
- Taking on debt above a defined threshold
- Liquidation or dissolution

**Overreach — flag and negotiate**:
- Veto over ordinary-course hiring decisions above a salary threshold (too operational)
- Veto over any new commercial contract above a low value (e.g., USD 50K) — paralyzes management
- Veto over changes in business direction without limiting to material/fundamental changes
- Veto over budget approval in general — unless coupled with a deadlock-resolution mechanism

**MENA note**: protective provisions in DIFC/ADGM are typically in the SHA. In UAE onshore, protective provisions in the articles of association for LLCs are technically possible but UAE Companies Law gives certain rights to all shareholders that limit the ability to restrict minority rights.

### 6. Founder Vesting

**Market standard**: 4-year vesting, 1-year cliff (25% of shares vest after 12 months; remainder vest monthly over the following 36 months).

**Founder-friendly additions**:
- Credit for time already served (e.g., if founders have been working for 18 months before the investment, they should receive credit for the first 18 months)
- **Single-trigger acceleration on Change of Control**: founder's unvested shares accelerate on a CiC, even if not terminated. Less standard but good for founders in early-stage deals.
- **Double-trigger acceleration**: unvested shares accelerate if both (a) CiC occurs AND (b) founder is terminated without cause within 12 months. More standard than single-trigger; negotiate hard for this.

**Flag**:
- Vesting applied to already-earned shares without credit for prior service
- No acceleration of any kind on CiC — founder can be fired on Day 1 of CiC and lose unvested shares
- Vesting tied to company performance milestones in addition to time — creates risk of being vested out by factors outside founder's control

### 7. Drag-Along Rights

Drag-along allows a specified group of shareholders to force all other shareholders to approve a sale of the company.

**Balanced drag-along**:
- Threshold: majority of preferred + majority of common (including founders) + board approval
- Price: not less than the liquidation preference (protects smaller investors from being dragged into a sale below their return threshold)

**Red flags**:
- Investor can drag alone with only a majority of preferred — founders have no veto over a sale they disagree with
- No minimum price protection — founders can be dragged into a distressed sale at any price
- Drag-along extends to blocking an IPO (unusual but flag)

### 8. ROFR and Co-Sale Rights

**Right of First Refusal (ROFR)**: before a founder can sell their shares to a third party, the company (and then the investors) have the right to purchase those shares on the same terms. This is standard and acceptable.

**Co-Sale (Tag-Along)**: if a founder sells shares to a third party, investors have the right to sell their shares on the same terms. This is also standard and acceptable.

**Flag**:
- ROFR applies to shares received on exercise of options (unusual; founders should retain flexibility over their options)
- Co-sale with a drag component — investor can force founder to sell in a co-sale scenario
- Double-trigger ROFR (ROFR on ROFR) — company waives, then investors have the right, then if all investors waive, they all have another bite — creates excessive friction

### 9. Exclusivity / No-Shop

**Standard**: exclusivity (no-shop) for 30–60 days from signing the term sheet.

**Flag**:
- Exclusivity over 90 days — ties up the company for a deal that may not close
- No defined termination mechanism if investor delays due diligence
- Exclusivity that applies to all financing discussions, not just this specific investor
- No long-stop date — exclusivity runs until investor decides to terminate

**Expense reimbursement**: investor's legal fees typically covered by the company up to a cap (USD 25–50K for Series A). Flag: no cap on legal fees; fees reimbursed even if investor walks away.

### 10. IP Assignment and Non-Compete from Founders

**IP assignment**: investors will require founders to confirm they have assigned all IP to the company. This is non-negotiable. Check: (a) the assignment is documented; (b) it covers pre-incorporation work; (c) it covers work done on personal equipment.

**Non-compete and non-solicitation**: also largely non-negotiable for founders. Check:
- Term: typically 12–24 months post-employment/departure (not 5+ years — that is unusual)
- Geographic scope: must be reasonable — if company operates only in UAE, a global non-compete is overbroad
- Functional scope: restricted to the company's actual business — not so broad as to prevent founder from working in any technology

**MENA enforceability note**:
- UAE: non-competes are enforceable but courts may reduce unreasonable scope/duration (Labour Law)
- KSA: non-competes are enforceable in commercial law context; must be tied to legitimate business interest
- DIFC/ADGM: English-law reasonableness test; courts will not enforce unreasonable restraints of trade

## Output Format

```json
{
  "findings": [
    {
      "provision": "<term sheet section>",
      "issue": "<description>",
      "severity": "critical|high|medium|low",
      "market_standard": "<what is typical>",
      "recommended_position": "<what to negotiate for>",
      "fallback": "<minimum acceptable position>"
    }
  ],
  "overall_founder_risk": "critical|high|medium|low",
  "deal_killers": ["<provisions that should not be accepted>"],
  "priority_negotiations": ["<ranked list of items to push on>"]
}
```

## MENA Jurisdictional Notes

**DIFC / ADGM**: Both free zones support English-law company structures with sophisticated VC term sheet conventions. Preferred shares, drag-along, and anti-dilution are all well-recognized legal instruments in these jurisdictions.

**KSA**: Saudi Companies Law (Royal Decree M/3 of 2015) governs JSCs and LLCs. VC-style preferred share rights are increasingly adopted in Saudi JSCs, but some investor-protection provisions may need to be structured differently from their US/UK equivalents. Engage Saudi counsel for definitive structuring.

**UAE (onshore)**: UAE LLC legislation limits some of the customization available in DIFC/ADGM; preferred share economics may need to be structured via contractual rights in an SHA rather than in the articles.

## Related Skills

- [[review-term-sheet-investor-side]]
- [[review-msa-deep-review]]
- [[review-unusual-terms-detector]]
- [[draft-safe-note]]
- [[draft-sha]]
- [[review-ip-ownership-clarity]]
