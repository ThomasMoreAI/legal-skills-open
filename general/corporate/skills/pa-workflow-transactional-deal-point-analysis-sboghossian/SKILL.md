---
name: pa-workflow-transactional-deal-point-analysis-sboghossian
title: Deal Point Analysis
description: Use when an M&A, private equity, or venture transactional lawyer needs to analyze the key deal points in an acquisition agreement, investment agreement, or term sheet against market norms and comparable precedents. Produces a deal-point matrix covering purchase price mechanics, reps and warranties, indemnification, closing conditions, termination rights, and post-closing covenants. MENA-aware (UAE, KSA, DIFC, ADGM) with multi-jurisdiction coverage.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-transactional-deal-point-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Deal Point Analysis

## Purpose

In M&A and investment transactions, the deal-point matrix is the working document that tells counsel at a glance how the agreed or proposed terms compare to market norms and the firm's precedent. This workflow parses a deal document (SPA, investment agreement, or term sheet), extracts the key deal points, maps them against market benchmarks, and flags positions that are off-market on either side.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Transaction document | Yes | SPA, SHA, investment agreement, term sheet, heads of terms |
| Transaction type | Yes | Strategic acquisition, PE buyout, VC investment, minority investment, JV |
| Client's position | Yes | Buyer / investor or seller / target / founder |
| Deal value | Recommended | Material deal points (basket, cap) are often expressed as percentages of deal value |
| Governing law | Yes | Determines which market norms apply |
| Jurisdiction of target | Yes | Affects regulatory approvals, employment matters, and local law reps |
| Precedent deals (if available) | Optional | Enables more specific market comparison |

## Deal Points Analyzed

### 1. Purchase Price and Adjustment Mechanisms

| Element | Extracted position | Market norm | Assessment |
|---|---|---|---|
| Price basis | Enterprise value / equity value | — | — |
| Locked-box vs. completion accounts | Completion accounts | Locked-box preferred in PE | Flag if completion accounts without adequate protections |
| Working capital target | As defined | Typically historical average | Check definition of working capital; NWC manipulability risk |
| Earnout | None / X over Y years | Common in strategic deals; less in PE | Note: earnout disputes are extremely common — check measurement methodology |
| Deferred consideration | — | — | Flag if seller has no security for deferred amounts |

MENA note: UAE and KSA transactions may be structured as share transfers, asset acquisitions, or via free-zone vehicles (DIFC/ADGM SPVs). The structure affects stamp duty (UAE: no transfer tax on shares; asset transfers may trigger registration fees), regulatory approvals, and SAMA / CBUAE change-of-control requirements for regulated entities.

### 2. Representations and Warranties

Key areas to extract and assess:

| Area | Depth of rep (standard / fulsome / thin) | Knowledge qualifier | Material adverse effect qualifier |
|---|---|---|---|
| Financial statements | | | |
| Tax | | | |
| Employment and labor | | | |
| IP | | | |
| Regulatory / licenses | | | |
| Material contracts | | | |
| Litigation | | | |
| Environment | | | |
| Data protection | | | |
| Anti-corruption (FCPA/UK Bribery Act/MENA) | | | |

Flag: absent reps (especially anti-corruption and data protection in MENA M&A — these are increasingly required by DIFC/ADGM/KSA regulatory sign-offs). Thin knowledge qualifiers on financial reps (seller "awareness" should generally not limit financial statement reps).

**MENA-specific reps to include or flag as absent**:
- Saudization/Emiratisation compliance (KSA/UAE — workforce localization requirements)
- Foreign ownership restrictions / MISA approval (KSA) / ADRA registration (UAE mainland)
- Sponsorship and visa status of key employees (UAE — visa sponsorship is not portable; creates HR risk post-closing)
- Anti-bribery compliance under UAE Federal Anti-Corruption Law, KSA government contracting rules

### 3. Indemnification (Cap, Basket, Survival)

| Element | Extracted position | Typical market range | Flag? |
|---|---|---|---|
| Indemnification cap | X% of deal value | 10–25% (strategic); 15–30% (PE) | Flag if below 10% |
| Basket / deductible | X USD / X% of deal value | 0.5–1.5% (tipping basket); 0.25–0.75% (deductible) | Flag if too high (excludes real claims) |
| Survival period | X months | 18–24 months general; 36 months for tax; unlimited for fraud | Flag if general reps survive 36+ months without basis |
| Fundamental reps | Unlimited / uncapped | Market: uncapped for title, capacity, authorization | Flag if capped |
| Tax indemnity | Yes / No | Required in most MENA M&A | Flag if absent |
| Fraud carve-out | Yes / No | Must be present | Flag if absent |

### 4. Closing Conditions

Flag:
- **Conditions that are entirely within seller's control** (effectively a walk-away right for seller)
- **MAC clause**: definition of Material Adverse Change — is it buyer-favorable (broad) or seller-favorable (narrow)? COVID-type exclusions?
- **Regulatory approvals**: SAMA, CBUAE, MISA, UAE MoEI change-of-control approvals — these can take 3–9 months in MENA. Timetable risk if not already in process.
- **Third-party consents**: material contracts with change-of-control provisions that require consent — flagged as missing from closing conditions

### 5. Termination Rights

| Right | Holder | Trigger | Break fee |
|---|---|---|---|
| Long-stop date termination | Both | Conditions not satisfied by [date] | — |
| MAC termination | Buyer | Material adverse change in target | Reverse break fee if buyer terminates |
| Breach termination | Either | Material breach of representations or covenants | — |

Flag: termination rights without reverse break fees in deals above a certain value (seller has limited remedy if buyer walks without cause). Long-stop dates that are too short for MENA regulatory approvals.

### 6. Non-Compete and Non-Solicit

| Element | Scope | Duration | Geography | Assessment |
|---|---|---|---|---|
| Non-compete | Business activity | X years | Jurisdiction | |
| Non-solicit (customers) | Named customers vs. all customers | X years | — | |
| Non-solicit (employees) | All employees vs. key employees | X years | — | |

MENA enforceability:
- **UAE**: Non-compete enforceability is improving post-2022 Labour Law reform but UAE courts are generally reluctant to enforce overly broad post-employment restrictions. Non-competes in M&A context (seller restrictions) are more consistently enforced than employment-context restrictions.
- **KSA**: Non-competes are enforceable in M&A contexts; Saudi courts apply reasonableness standard on scope and duration.
- **Lebanon**: Non-competes are recognized but enforcement is inconsistent; courts may reduce scope.
- **DIFC / ADGM**: Common-law reasonableness standard applies; well-drafted non-competes tied to legitimate business interests are enforceable.

## Output — Deal Point Matrix

```markdown
## Deal Point Matrix — [Transaction Name] — [Date]
**Transaction type**: Strategic acquisition
**Client position**: Buyer
**Governing law**: DIFC
**Deal value**: USD 45M

| Deal Point | Agreed Position | Market Norm | Flag? | Recommendation |
|---|---|---|---|---|
| Indemnification cap | 12% of deal value ($5.4M) | 15–25% | BELOW MARKET | Push to 15% minimum |
| Basket | 0.75% ($337K tipping) | 0.5–1.0% | OK | — |
| Survival (general reps) | 18 months | 18–24 months | OK | — |
| Fundamental reps | Uncapped | Uncapped | OK | — |
| MAC clause | Standard; no specific exclusions | COVID/macro exclusions now market | AT RISK | Add exclusion for macro events outside target's control |
| Non-compete | 3 years; GCC only | 2–4 years; local market | OK | Confirm enforceability in each GCC state separately |
| Saudization rep | Absent | Required for KSA target | MISSING | Add — KSA subsidiary may have workforce ratio obligations |
| Anti-corruption rep | Generic | Specific FCPA + KSA bribery rep | THIN | Expand; request specific disclosure letter |
```

## Related Skills

- [[pa-workflow-transactional-msa-against-firm-playbook]]
- [[pa-workflow-transactional-clause-library-check]]
- [[pa-workflow-transactional-pia-privacy-impact-assessment]]
- [[review-spa-acquisition]]
- [[persona-investor]]
