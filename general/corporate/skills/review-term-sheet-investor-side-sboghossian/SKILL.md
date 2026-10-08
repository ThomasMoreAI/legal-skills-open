---
name: review-term-sheet-investor-side-sboghossian
title: Term Sheet Review — Investor Side
description: Use when reviewing a VC or angel investor term sheet from the investor's perspective. Flags gaps in downside protection, control rights, information access, and founder accountability. Covers liquidation preference adequacy, anti-dilution minimums, board composition, protective provisions, pay-to-play, founder vesting and IP assignment, exclusivity, and deal-killer scenarios. Applies MENA and international VC market standards (DIFC, ADGM, KSA, US, UK).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-term-sheet-investor-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Term Sheet Review — Investor Side

## When to use this

Use when a VC fund, family office, or angel investor needs to review a term sheet (whether drafted by them or by the company's lawyers) from the investor's perspective. The investor's goals are: downside protection (liquidation preference, anti-dilution), governance rights (board seat, protective provisions, information rights), accountability mechanisms (founder vesting, IP assignment), and exit alignment (drag-along, ROFR, co-sale).

For the founder-side perspective, use [[review-term-sheet-founder-side]].

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Term sheet | Full document | Required |
| Investment stage | Seed, Series A, B — calibrates market standard | Ask if unclear |
| Investment size and target ownership | Determines whether protective provisions match stake | From term sheet |
| Jurisdiction | Company registration jurisdiction affects enforceability | From term sheet |
| Prior rounds | Existing cap table and any senior security holders | Ask if available |

## Review Methodology

### 1. Liquidation Preference — Adequacy

The liquidation preference determines investor return in a sale, wind-down, or distribution event.

**Minimum acceptable**: 1× non-participating — investor gets back invested capital (or pro-rata proceeds if higher) before any distribution to common. This is the market floor for institutional investors.

**Stage-appropriate expectations**:

| Stage | Acceptable preference |
|---|---|
| Pre-seed / angel | 1× non-participating is standard; sometimes 1.25× or 1.5× for high-risk early cheques |
| Seed | 1× non-participating; some seed investors negotiate participating with 2× cap |
| Series A / B | 1× non-participating is strong market standard; participating is increasingly rare |
| Late stage (distressed) | 1× or 2× participating may be appropriate given risk profile |

**Flag**:
- 1× non-participating with no cap on distribution proceeds — investor misses growth upside in a pure exit scenario; check whether preferred converts to common for IPO/high-value exits (standard)
- Liquidation preference applies on IPO — generally unacceptable; preferred should convert to common upon IPO

### 2. Anti-Dilution — Minimum Standard

**Acceptable minimum**: broad-based weighted-average anti-dilution. Any round that provides less protection than this is a deal-killer for institutional investors.

**What to verify**:
- Is the formula clearly specified? (Not just "weighted average" — verify it is "broad-based weighted average" incorporating all shares outstanding including option pool)
- Are carve-outs appropriate? (Anti-dilution should not be triggered by: option pool shares; conversion of existing convertible notes; shares issued as M&A consideration; certain lender warrants)
- Is the anti-dilution protection automatically applied or does it require shareholder approval? (Auto-apply is investor-protective)

**Red flag**: company proposing a narrow-based weighted-average (only shares of the same series) — provides less protection than broad-based. Reject.

### 3. Board Composition

**Minimum for lead investor** (Series A, 15–30% ownership):
- 1 board seat for the lead investor
- Observer right (no voting) for follow-on investors or co-investors who did not lead

**Acceptable early-stage structure**:
- 2 founder seats
- 1 investor seat
- 1 independent seat (investor has meaningful role in independent director selection)

**Flag**:
- No board seat for the lead investor on a significant round — unacceptable for institutional Series A+
- Independent director can be removed by founder majority without investor consent — weakens governance
- No mechanism for investor to appoint additional board members as investor's ownership percentage grows (e.g., if anti-dilution triggers additional shares)

### 4. Protective Provisions — Coverage

Protective provisions are investor veto rights over specific company actions. A complete list for institutional investors:

**Core protective provisions** (non-negotiable):
- Sale of the company (merger, acquisition, asset sale, change of control)
- Issuance of any new class of security ranking senior to or pari passu with investor's preferred series
- Amendment to articles/charter that adversely affects the investor's preferred series
- Taking on financial indebtedness above a specified threshold (typically USD 500K to USD 2M depending on stage)
- Any material change in the nature of the company's principal business
- M&A transactions above a specified value
- IPO or public listing (to protect investor's preferences / conversion mechanics)

**Additional protective provisions** (common but often negotiated):
- Issuance of any new equity beyond the reserved option pool
- Entry into any joint venture or partnership
- Licensing of core IP on an exclusive basis
- Related-party transactions above a defined threshold

**Flag**:
- Protective provisions that require a simple majority of preferred to exercise — should require the lead investor's specific consent to avoid being overridden by small holders of preferred
- Missing any of the core provisions above
- Protective provisions that sunset after a defined period (unusual; flag)

### 5. Information Rights

Investors need visibility into the company's performance to manage their portfolio and meet their own fund reporting obligations.

**Standard investor information rights**:

| Right | Frequency | Notes |
|---|---|---|
| Management accounts / financials | Monthly | P&L, cash position, KPIs |
| Annual audited financial statements | Annually | Required by most LP agreements |
| Annual budget and operating plan | Annually before fiscal year start | Right to provide input; not right to approve |
| Notification of material events | Promptly | Litigation, regulatory action, loss of major customer |
| Access to management team | Reasonable | For due diligence follow-up; not unrestricted |
| Cap table and option pool updates | On any change | Investor needs to track dilution |

**Flag**:
- Monthly management accounts absent — investor is flying blind
- Information rights limited to annual audited accounts only — inadequate for active portfolio management
- Budget review right absent — investor cannot anticipate cash needs or track against plan
- No notification obligation for material events (litigation, regulatory action, insolvency risk)

**MENA context**: Gulf-based family offices may be less demanding on monthly management accounts; institutional GPs and LPs expect them. Calibrate against fund type.

### 6. Pro-Rata Rights

The right to participate in future funding rounds to maintain ownership percentage.

**Standard**: pro-rata right through at least Series B (or through all rounds for lead investors).

**Variants**:
- Super pro-rata: right to invest more than one's ownership percentage in future rounds — often contested by founders
- Pro-rata notification requirement: company must notify investor of forthcoming round sufficiently in advance for investor to participate

**Flag**: no pro-rata right at all for a meaningful ownership stake investor — creates unacceptable dilution risk.

### 7. Pay-to-Play

Pay-to-play provisions require existing investors to participate in follow-on rounds (at least pro-rata) or face consequences:
- **Light pay-to-play**: preferred converts to common (loses economic preference) if investor does not participate
- **Heavy pay-to-play**: preferred converts to ordinary shares and loses all protective provisions and board rights

**Investor's perspective**:
- Pay-to-play is acceptable as a company-protection mechanism to ensure pro-rata participation from early investors in difficult rounds
- However, investor should ensure the pay-to-play trigger has a minimum round size threshold (does not apply to small bridge rounds or insider rounds)
- Ensure there is a 30-60 day notice period before the pay-to-play obligation crystallizes

### 8. Drag-Along — Investor Alignment

**Minimum drag-along structure from investor's perspective**:
- Investor (as preferred holder) is part of the majority that can trigger drag-along
- Drag-along applies to all shareholders including founders (prevents a minority of founders blocking a value-creating exit)
- Drag threshold: majority of preferred + majority of common + board approval (prevents investor dragging without board support)

**Flag**:
- No drag-along at all — founders can block a sale that the investor wants
- Drag-along requires all-holders consent — unanimity is unworkable for exits
- Drag threshold set so high that it is practically unusable (e.g., 90% of all shares)

### 9. Founder Vesting and IP Assignment

**Required from investor's perspective**:
- **Founder vesting**: 4-year, 1-year cliff; unvested shares subject to company repurchase right at cost if founder departs without cause. This protects the company (and therefore investors) from a founder walking away with a large unearned equity stake.
- **Double-trigger acceleration**: acceptable; single-trigger acceleration is a red flag — means a founder gets full equity on any acquisition regardless of whether they continue post-CiC
- **IP assignment**: all founders must have assigned all company-related IP to the company, including pre-incorporation work and work done on personal equipment. A missing IP assignment can affect the company's ability to raise future rounds or achieve a clean exit.

**Flag**:
- No founder vesting (founders already fully vested pre-investment) without a vesting restart on acceptable terms
- Single-trigger acceleration on CiC — investor pays for future value; founder captures it on day one of a CiC
- IP assignment incomplete or missing

### 10. Exclusivity, Fees, and Longstop

**Standard**:
- Exclusivity: 30–60 days; should not exceed 90 days without milestone-based extension
- Legal fees: company pays investor's legal fees up to a cap (USD 25–50K for Series A; USD 75–150K for Series B+)
- Longstop: if definitive documents are not signed within 90 days of term sheet, term sheet expires

**Flag**:
- No longstop date — deal drags indefinitely, investor is in limbo
- No legal fee reimbursement — unusual for institutional investors
- Exclusivity with no termination right for investor — investor cannot exit the process if diligence reveals problems

## Deal Killers — Walk-Away Scenarios

| Issue | Why it is a deal-killer |
|---|---|
| No founder vesting | Investor is funding founders who can walk away fully vested immediately |
| Full ratchet anti-dilution offered to existing holders senior to this round | Investor's new money may trigger catastrophic dilution from existing full-ratchet holders |
| IP chain of title broken | Company may not own its core assets |
| No protective provisions at all | Investor has no governance control over material company decisions |
| Founders hold a blocking minority on all key votes | Investor cannot enforce any governance rights |

## Output Format

```json
{
  "findings": [
    {
      "provision": "<section>",
      "issue": "<description>",
      "severity": "critical|high|medium|low",
      "market_standard": "<benchmark>",
      "recommended_redline": "<what investor should push for>"
    }
  ],
  "deal_killers": ["<list of walk-away issues>"],
  "overall_investor_protection": "strong|adequate|weak|unacceptable",
  "priority_redlines": ["<ranked negotiation priorities>"]
}
```

## Related Skills

- [[review-term-sheet-founder-side]]
- [[review-msa-deep-review]]
- [[review-unusual-terms-detector]]
- [[draft-sha]]
- [[draft-safe-note]]
- [[review-ip-ownership-clarity]]
