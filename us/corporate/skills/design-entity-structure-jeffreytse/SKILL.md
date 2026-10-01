---
name: design-entity-structure-jeffreytse
title: Design Entity Structure
description: Use when a founder, freelancer, or small business owner needs to choose and set up the right legal entity — deciding between sole proprietorship, LLC, S-corp, or C-corp based on liability, tax treatment, and funding plans
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/corporate/skills/design-entity-structure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [llc, s-corp, c-corp, founders, tax, liability, startup, freelance]
---

# Design Entity Structure

Choose the right legal entity for your business, model the tax and liability trade-offs, and complete the formation steps in the correct order.

## Why This Is Best Practice

**Adopted by:** Every major law firm's startup practice (Wilson Sonsini, Cooley, Gunderson) runs founders through an entity selection framework before any other work. Y Combinator's standard advice is "Delaware C-corp by default for venture-backed startups; single-member LLC for everything else until you have investors." The IRS check-the-box regulations (1996) created the current menu of options that practitioners now use as a decision tree.

**Impact:** Entity structure affects: (1) personal liability for business debts, (2) self-employment tax (15.3% on all S-corp salary vs. limited to distributions above reasonable comp), (3) investor eligibility (VCs cannot hold S-corp shares), (4) capital gains treatment at exit, and (5) administrative burden. A freelancer who earns $200k/year as a sole proprietor vs. S-corp pays ~$10k–15k more in self-employment tax annually (IRS SE tax rules, 2024). Choosing the wrong structure for VC funding (S-corp instead of C-corp) requires costly restructuring.

**Why best:** Most founders choose entity type based on what they've heard from peers or what's cheapest to form ($0 for sole prop, $50–$500 for LLC). This misses the tax and liability calculus entirely. A structured decision tree — liability first, tax second, funding trajectory third — reaches the right answer systematically and avoids the cost of restructuring later.

Sources: IRS Publication 3402 (Taxation of Limited Liability Companies); Feld & Mendelson, *Venture Deals* (4th ed., 2019); NOLO, *LLC vs. Corporation* (Steingold, 2023); Anderson, *Tax Planning for Corporations and Shareholders* (Thomson Reuters)

## Steps

### Step 1: Assess liability exposure
Does your business carry meaningful liability risk — clients who could sue, physical products, employees, leases, or debt obligations? If yes, you need liability protection (LLC or corporation). If you're a solo freelancer with purely service income and low contract values, sole proprietorship may be acceptable short-term, but you remain personally liable.

### Step 2: Map your funding trajectory (next 3 years)
| Plan | Entities that work |
|------|--------------------|
| No outside investment | LLC (single-member or multi-member), S-corp |
| Angel investors (accredited individuals) | LLC, S-corp (limited), C-corp |
| Venture capital (institutional funds) | C-corp only (most VCs are LPs in pass-through funds and cannot hold S-corp stock) |
| Revenue-based financing | Any |
| IPO eventually | C-corp (Delaware) |

If you plan to raise VC, form a Delaware C-corp. Period.

### Step 3: Model the tax treatment

| Structure | Tax treatment | SE tax | Key trade-off |
|-----------|---------------|--------|---------------|
| Sole proprietor | Pass-through, Schedule C | 15.3% on all net income | Simple; no liability shield |
| Single-member LLC | Pass-through by default (same as sole prop) | 15.3% on all net income | Liability shield; minimal additional tax benefit until S-corp election |
| Multi-member LLC | Pass-through, partnership return (1065) | Varies | Flexible profit/loss allocation |
| S-corp (or LLC electing S) | Pass-through; split into salary + distributions | 15.3% only on salary portion | Saves SE tax above ~$60k net profit; requires payroll |
| C-corp | Double taxation (entity + dividend) | No SE tax; W-2 only | Best for retained earnings, stock options, VC |

**S-corp threshold rule of thumb:** If net self-employment income exceeds $80k/year and you have consistent revenue, model S-corp election. Below that threshold, payroll administration costs may exceed the tax savings.

### Step 4: Choose your state of formation
- **Delaware C-corp:** Standard for VC-backed startups. Mature case law, Court of Chancery, investor familiarity. File in Delaware even if you operate elsewhere; register as foreign entity in home state.
- **Home state LLC:** For local businesses, freelancers, real estate — home state is simpler and cheaper (no dual registration).
- **Wyoming LLC:** Popular for anonymity; no state income tax; no publication requirement. Good for holding companies and privacy-sensitive structures.

### Step 5: Complete formation in order

1. **Reserve entity name** — Check state business registry; reserve online if available.
2. **Draft and file Articles of Incorporation / Organization** — Online via state SOS website. Cost: $50–$500 depending on state.
3. **Appoint registered agent** — Can be yourself (home state) or a service ($50–$300/yr). Required for legal notices.
4. **Draft Operating Agreement (LLC) or Bylaws (corp)** — Internal governance document. Not filed publicly but legally required in most states. For multi-founder entities, this is where equity splits, decision rights, and buyout provisions live.
5. **Issue founder equity with 83(b) election (C-corp)** — File IRS 83(b) within 30 days of stock issuance. Missed deadline = major tax problem at acquisition.
6. **Apply for EIN** — IRS Form SS-4, online, free. Takes 15 minutes. Required to open business bank account.
7. **Open business bank account** — Maintain strict separation of personal and business funds. Commingling pierces the liability shield.
8. **Elect S-corp status if applicable** — IRS Form 2553, filed within 75 days of formation or by March 15 for the current tax year.
9. **Register for state/local licenses** — Business license, sales tax permit, professional license as required by your industry and locality.

### Step 6: Implement ongoing compliance requirements

| Entity | Annual requirements |
|--------|---------------------|
| Sole prop | Schedule C; quarterly estimated taxes |
| Single-member LLC | Annual report + fee (varies by state); Schedule C or 1065 |
| S-corp | Form 1120-S; payroll (W-2); annual report |
| C-corp | Form 1120; board minutes; annual report; separate from S-corp books |

Failure to maintain compliance (missing annual reports, not holding meetings, commingling funds) = personal liability despite entity formation.

## Rules

- Never operate a multi-founder business as a sole proprietor or without a written operating agreement — equity and control disputes destroy more startups than market risk.
- File the 83(b) election within 30 days of stock issuance. There is no exception and no extension.
- Maintain strict bank account separation. Pay all business expenses from the business account; pay yourself a salary or draw; never pay personal expenses from business funds.
- If you convert from LLC to C-corp for VC, do it before you raise — reorganisations post-funding are expensive and create tax events.
- Get a tax advisor involved before making the S-corp election — the reasonable compensation calculation is where most owners get audited.

## Examples

**Freelance designer, $120k/year net income:** Sole prop is simple but costs ~$18k/yr in SE tax. LLC provides liability shield. S-corp election: pay $65k salary (reasonable comp), $55k distribution. SE tax applies only to salary → saves ~$8,400/yr. Cost of payroll service: ~$1,200/yr. Net benefit: ~$7,200/yr. Elect S-corp.

**SaaS co-founders, two people, planning VC raise:** Delaware C-corp. Issue 1M shares to each founder at $0.0001/par value. File 83(b) within 30 days. 4-year vesting, 1-year cliff. Add SAFE agreements for first $500k from angels. Do not form as LLC — VC funds cannot hold LLC interests cleanly.

**Real estate investor, 5 rental properties:** Wyoming LLC for each property (asset segregation), holding company LLC at top. No S-corp election (rental income is not self-employment income). No C-corp (double taxation; real estate losses don't pass through corp).

## Common Mistakes

**Forming an LLC and doing nothing else:** An LLC provides liability protection only if you treat it as a separate entity — separate bank account, signed contracts in the LLC name, no personal guarantees unless required. Most small LLCs pierce their own veil through sloppy administration.

**Skipping the 83(b) election:** The 83(b) election starts your capital gains holding period at grant, not vesting. Without it, each tranche of vested equity is taxed as ordinary income at its fair market value on vesting date. At acquisition, this can be catastrophic.

**Choosing S-corp when planning VC:** S-corps cannot have more than 100 shareholders, cannot have non-resident alien shareholders, and cannot have more than one class of stock. Preferred stock (required for VC rounds) automatically disqualifies S-corp status.

**Not drafting an operating agreement for a multi-member LLC:** Without one, your state's default rules govern — which may give each member equal voting rights regardless of equity split, or allow any member to trigger dissolution.

**Registering in a "better" state without foreign qualifying at home:** If you form in Delaware but operate in California, you must foreign qualify in California and pay California taxes and fees regardless. For most small businesses, home state formation is simpler and cheaper.

---

> **Legal disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Entity selection and formation involves tax and legal complexity specific to your situation, jurisdiction, and funding plans. Consult a licensed attorney and CPA before forming a business entity.
