---
name: qsbs-compliance-cure-consulting-group
title: QSBS Compliance Tracker
description: Checks IRC §1202 QSBS qualification for C-corps under both OBBBA regimes. Use when an equity event, entity change, asset growth, or revenue mix could affect QSBS, or for an annual QSBS health check.
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/security/qsbs-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Section 1202 Tests
  path: references/section-1202-tests.md
---

# QSBS Compliance Tracker

> **READ-ONLY SKILL.** Produce analysis only: do not edit files, do not run
> mutating commands, and do not create or delete resources. Under Claude Code
> the `disallowed-tools` frontmatter above blocks Write and Edit.
> Bash stays available for read-only inspection (grep, git log, scanners), so even
> under Claude Code "no mutating commands" is advisory, not enforced.
> **Other runtimes do not enforce it** — Codex and Antigravity ignore those
> fields, and activation there can widen rather than narrow file access — so on
> any runtime other than Claude Code this paragraph is the only guardrail.

**Outcome:** a QSBS Compliance Scorecard (Step 5) per entity, returned in the response, with every test marked PASS / FAIL / AT RISK / UNKNOWN (missing data), every figure labeled with its regime, and every risk given a severity and a mitigation. **Done** when each test has a status and each UNKNOWN names the document that would resolve it.

IRC §1202 Qualified Small Business Stock compliance monitoring. QSBS excludes gain up to a per-issuer cap (the greater of a dollar cap or 10× basis) per shareholder — but qualification is fragile. A single disqualifying event can void the exclusion for affected issuances.

**Two regimes — the issuance date decides which applies** (OBBBA, P.L. 119-21;
verified 2026-09-23, Grant Thornton and *The Tax Adviser* Nov 2025 OBBBA §1202
analyses; reconcile with `tax/irc-lookup/reference/obbba-changes.md`):

| | Stock issued **on or before 2025-07-04** | Stock issued **after 2025-07-04** |
|---|---|---|
| Per-issuer cap | Greater of \$10M or 10× basis | Greater of \$15M or 10× basis; \$15M inflation-indexed for tax years beginning after 2026 |
| Gross-asset test | ≤ \$50M | ≤ \$75M (indexed from 2027) |
| Holding period / exclusion | >5 years → 100% (for stock acquired after 2010-09-27); nothing before 5 years | 3 yrs → 50%, 4 yrs → 75%, 5+ yrs → 100%; unexcluded gain taxed at 28% |

Always label every figure in an output with the regime it belongs to.

This is planning analysis, not tax advice: a wrong QSBS call can cost a founder seven figures of excludable gain, so every output goes to a CPA or tax attorney before anyone acts on it.

## Step 1: Classify the QSBS Task

| Task | Output | Urgency |
|------|--------|---------|
| Initial qualification assessment | Full §1202 checklist with pass/fail per criterion | High — do before any equity event |
| Holding period tracker | Per-shareholder holding period table with 3/4/5-year (post-2025-07-04) or 5-year (earlier) countdown | Ongoing |
| Disqualifying event scan | Risk analysis of proposed corporate action | Critical — run before any structural change |
| Annual health check | Year-end compliance scorecard | Annual |
| Equity event impact | Pre/post analysis of proposed issuance, buyback, or redemption | Before event |
| Entity structure review | C-Corp status verification, subsidiary analysis | On change |

## Step 2: Gather Context

1. **Entity** — which C-Corp? (Vendly Inc., Autograph Health Inc., etc.)
2. **Incorporation** — state, date, current status
3. **Stock issuance history** — dates, shareholders, consideration paid, share classes
4. **Gross assets** — current aggregate gross assets (cash + property + equipment at cost basis, not FMV)
5. **Business activities** — breakdown of qualified vs non-qualified activities by revenue/time
6. **Recent or planned actions** — any redemptions, buybacks, recapitalizations, conversions, or entity changes

## Step 3: §1202 Qualification Criteria

Run each test; all must hold at the same time, and several must hold continuously through the holding period. Report every finding, including low-severity ones — ranking happens in the scorecard. Read `references/section-1202-tests.md` when computing gross assets, classifying revenue as qualified vs. services, fixing clock-start dates, or checking state conformity.

### Test 1: C-Corporation Requirement
- Entity must be a domestic C-Corporation at time of stock issuance
- S-Corp, LLC, LP, or foreign corp stock does NOT qualify
- **Check**: Read articles of incorporation, verify no S-election (Form 2553) filed
- **Disqualifier**: Only stock issued while the entity is a C-Corp can be QSBS, and the corporation must remain a C-Corp during substantially all of the holder's holding period. An S election or conversion therefore blocks new QSBS and puts the exclusion on already-issued shares at risk — treat it as CRITICAL and get counsel before any conversion.

### Test 2: Original Issuance
- Stock must be acquired at original issuance (not secondary market)
- Must be acquired for money, property (not stock), or services
- Convertible debt that converts counts if conversion is into newly issued stock
- SAFE conversions count if resulting stock is newly issued
- **Check**: Review cap table for secondary transfers, stock purchase agreements

### Test 3: Gross Asset Test (≤ \$50M pre-2025-07-05 issuances / ≤ \$75M later issuances)
- Aggregate gross assets must not exceed the threshold for that issuance's regime (\$50M if issued on or before 2025-07-04; \$75M, indexed from 2027, if issued after) at any time from incorporation through immediately after the stock issuance
- Gross assets = cash + adjusted basis of all property (NOT fair market value)
- Includes assets of subsidiaries (>50% owned)
- **Check**: Balance sheet at each issuance date, adjusted basis records
- **Disqualifier**: Exceeding the applicable threshold at any point before or immediately after an issuance disqualifies that issuance and all later issuances; stock already issued keeps its status

### Test 4: Active Business Test (>80% Qualified)
- At least 80% of assets (by value) must be used in the active conduct of one or more qualified trades or businesses
- Measured continuously during substantially all of the holding period
- **Excluded businesses** (these do NOT qualify):
  - Professional services (health, law, engineering, accounting, consulting, financial services)
  - Banking, insurance, financing, leasing, investing
  - Farming
  - Mining, oil, gas
  - Hotels, motels, restaurants (operating, not SaaS for them)
- **Software/SaaS IS qualified** — building and selling software products qualifies
- **Consulting revenue is NOT qualified** — if >20% of revenue comes from consulting/professional services, risk increases
- **Check**: Revenue breakdown by activity type, employee time allocation

### Test 5: Holding Period (regime-dependent)
- Stock issued on or before 2025-07-04: must be held **more than 5 years** for any exclusion.
- Stock issued after 2025-07-04: **3 years → 50%, 4 years → 75%, 5 years → 100%** exclusion.
- **§1045 is a rollover, not an exclusion**: if QSBS held **more than 6 months** is sold, the holder may elect to defer the gain by buying replacement QSBS within **60 days**; the holding period tacks onto the replacement stock. Gain is deferred, not excluded.
- **Check**: Issuance date per shareholder, the regime it falls under, and the 3/4/5-year anniversaries

### Test 6: Redemption Restrictions (§1202(c)(3); Treas. Reg. §1.1202-2)
- **Related-party test**: stock is not QSBS if the corporation redeemed stock from the taxpayer or a related person within **2 years before or 2 years after** the issuance (de minimis exception: aggregate redemptions ≤ \$10,000 or ≤ 2% of the holder's stock)
- **Significant-redemption test**: no stock is QSBS if the corporation redeemed more than **5% of the aggregate value** of all its stock within **1 year before or 1 year after** the issuance (subject to a de minimis exception)
- **Check**: All buyback/redemption transactions within both windows; confirm de minimis figures against the regulation before relying on them

## Step 4: Disqualifying Event Detection

Scan for these red flags; any one can void QSBS for some or all issuances:

| Event | Risk Level | Action |
|-------|-----------|--------|
| S-Corp election filed | **CRITICAL** | Blocks all future QSBS issuance |
| LLC conversion | **CRITICAL** | Ends C-Corp status: no new QSBS, and the holding-period C-Corp requirement is at risk for existing shares |
| Gross assets exceed \$50M (pre-2025-07-05 regime) / \$75M (later regime) | **CRITICAL** | Disqualifies all issuances after threshold crossed |
| Stock buyback >5% within window | **HIGH** | May disqualify specific issuances |
| Revenue mix shifts to >20% consulting | **HIGH** | Active business test at risk |
| Merger or acquisition | **HIGH** | Depends on structure — stock-for-stock may preserve, asset sale may not |
| Stock transferred (not original issuance) | **MEDIUM** | Transferred shares lose QSBS status (exceptions: gift, death, certain partnerships) |
| Significant idle cash / investment assets | **MEDIUM** | Assets not used in active business reduce the 80% test |
| Foreign subsidiary >50% | **MEDIUM** | Must be domestic C-Corp; foreign sub assets may not count toward active business |
| Real estate holding | **LOW** | Rental real estate is generally not "active" unless substantial services |

## Step 5: Output — QSBS Compliance Scorecard

Return this scorecard in the response for each entity (it is read-only output, not a file). Match length to the need; no filler sections or restated summaries.

```markdown
# QSBS Compliance Scorecard — [Entity Name]

**Assessment Date**: [date]
**Entity**: [name], [state] C-Corporation
**Incorporation Date**: [date]
**Status**: QUALIFIED / AT RISK / DISQUALIFIED

## §1202 Test Results

| Test | Status | Detail |
|------|--------|--------|
| C-Corp Status | PASS/FAIL | [current entity type, any elections] |
| Original Issuance | PASS/FAIL | [secondary transfers found?] |
| Gross Asset Test (≤ \$50M or \$75M by issuance regime) | PASS/FAIL | Current: [X]M. Headroom vs applicable threshold: [T-X]M |
| Active Business (>80%) | PASS/FAIL | Qualified: [X]%, Non-qualified: [Y]% |
| Holding Period (3/4/5yr or 5yr by regime) | TRACKING | [table of shareholders with dates] |
| Redemption Window | PASS/FAIL | [related-party 2yr/2yr; significant >5% 1yr/1yr] |

## Holding Period Tracker

| Shareholder | Shares | Issuance Date | Regime (pre/post 2025-07-04) | 3/4/5-Year Dates | Status |
|-------------|--------|---------------|------------------------------|------------------|--------|
| [name] | [count] | [date] | [pre/post] | [dates] | [X yr Y mo to next tier] |

## Risk Factors

| Risk | Severity | Mitigation |
|------|----------|------------|
| [identified risk] | CRITICAL/HIGH/MEDIUM/LOW | [recommended action] |

## Upcoming Events Requiring QSBS Review

- [ ] [planned equity event or corporate action]

## Disclaimer

This assessment is for planning purposes only. It does not constitute tax or legal
advice. Consult a qualified CPA and tax attorney before making decisions based on
QSBS qualification status. IRC §1202 has complex interaction with state tax laws
that vary by jurisdiction.
```

## Step 6: Cure Portfolio QSBS Status

For Cure Consulting Group entities, track these specifically:

| Entity | Key Risk | Monitoring Frequency |
|--------|----------|---------------------|
| Vendly Inc. | Consulting revenue mix (Cure performs dev work — is this "consulting"?) | Quarterly |
| Autograph Health Inc. | Gross asset test as fundraising increases | Each funding round |
| Any new C-Corp | Original issuance documentation at formation | At incorporation |

## Cross-References

- For HIPAA/GDPR/PCI compliance: use `compliance-architect`
- For cap table modeling: use `investor-reporting` or `fundraising-materials`
- For entity structure decisions: consult tax attorney (no skill replaces this)
- For post-OBBBA §1202 figures and authority: use `irc-lookup` (its OBBBA-changes reference, `tax/irc-lookup/reference/obbba-changes.md`)
- For Delaware franchise tax: consult the CPA (no skill covers it)
