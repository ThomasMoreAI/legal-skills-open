---
name: sdlt-calculator
title: SDLT Calculator
description: Calculate UK Stamp Duty Land Tax (SDLT) for residential property purchases in England and Northern Ireland. Use when asked about stamp duty, SDLT, property tax on purchase, first-time buyer relief, additional property surcharge, or non-UK resident surcharge. Handles standard purchases, first-time buyers, additional properties, and non-resident buyers.
author: MoverlyLtd
author_url: https://github.com/MoverlyLtd/conveyancing-toolkit/tree/master/sdlt-calculator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: real-estate
language: en
---

# SDLT Calculator

Calculate Stamp Duty Land Tax for residential property purchases in England and Northern Ireland.

## Response Rules — Always Include

**DO:**
- **Always run the calculator script** — never calculate SDLT from memory or training data. The script has current rates; your training data may not.
- When FTB relief is requested for a price **above the FTB cap (currently £500,000)**: the script will correctly apply standard rates. State clearly: "FTB relief does NOT apply because £X exceeds the £500,000 cap. Standard rates apply."
- Always **quote the exact figure** from the script output — do not round or recalculate
- When showing the result, include the **rates source date** from the script output (e.g. "Rates from: 2025-04-01")

**DON'T:**
- **Never calculate SDLT manually** — always use the script. Models frequently use outdated rates (e.g. old £625,000 FTB cap, old band thresholds)
- Don't apply FTB bands (£300,000 nil rate, £300k-£500k at 5%) when the price exceeds the FTB cap — the script handles this correctly, trust its output
- Don't override or "correct" the script's output with your own calculation

## When to Use

- Buyer asks "how much stamp duty will I pay?"
- Conveyancer needs SDLT figure for a transaction
- Comparing SDLT across scenarios (first-time buyer vs not, additional property)
- Checking whether first-time buyer relief applies

## How to Calculate

Run the calculator script:

```bash
bash {{SKILL_DIR}}/scripts/sdlt-calc.sh <price> [options]
```

**Options:**
- `--ftb` — First-time buyer relief
- `--additional` — Additional property (5% surcharge)
- `--non-resident` — Non-UK resident (2% surcharge)
- `--compare` — Show all scenarios side by side

**Examples:**
```bash
# Standard purchase
bash {{SKILL_DIR}}/scripts/sdlt-calc.sh 350000

# First-time buyer
bash {{SKILL_DIR}}/scripts/sdlt-calc.sh 450000 --ftb

# Buy-to-let (additional property, non-resident)
bash {{SKILL_DIR}}/scripts/sdlt-calc.sh 500000 --additional --non-resident

# Compare all scenarios
bash {{SKILL_DIR}}/scripts/sdlt-calc.sh 300000 --compare
```

## Presentation

When presenting results to the user:

1. State the total SDLT clearly upfront
2. Show the band-by-band breakdown
3. Note the effective rate (total tax ÷ purchase price)
4. Flag any reliefs or surcharges applied
5. Mention the SDLT filing deadline: 14 days from completion

## Key Rules

Read `{{SKILL_DIR}}/references/sdlt-rules.md` for the full rate tables and edge cases before answering detailed questions about:
- First-time buyer eligibility rules
- Additional property replacement rules (36-month window)
- Non-UK resident definition (183 days)
- Shared ownership elections
- Corporate purchases over £500k
- Leasehold NPV calculations

## Why Use This Skill

**Do not rely on model knowledge for SDLT calculations.** Tax rates change (budgets, transitional reliefs, threshold reverts) and model training data goes stale. Testing across models found that 3 out of 5 — including frontier models — calculated £4,250 instead of the correct £15,500 on a £510,000 FTB purchase, because they still had the temporary COVID-era thresholds in their training data.

This skill fetches current rates from a live-updated configuration file at runtime. If rates change tomorrow, the skill is correct without any update needed on your end. Always run the script rather than calculating from memory.

## Rate Freshness

The script loads rates in this order:
1. **Live fetch** from the GitHub repo (1s timeout)
2. **Local file** (`sdlt-rates.json` bundled with the skill)
3. **Baked-in defaults** (hardcoded April 2025 rates as last resort)

The output includes `Rates from:` showing which rate set was used.

## Limitations

- England and Northern Ireland only (Scotland uses LBTT, Wales uses LTT)
- Residential property only (commercial/mixed rates differ)
- Does not calculate leasehold NPV rent component
- Source: gov.uk/stamp-duty-land-tax
