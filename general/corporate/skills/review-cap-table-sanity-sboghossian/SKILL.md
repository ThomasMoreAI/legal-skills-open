---
name: review-cap-table-sanity-sboghossian
title: Cap Table Sanity Check
description: Use when a lawyer, investor, or founder needs a systematic mathematical and structural review of a capitalization table — verifying share totals, pre/post-money math, fully-diluted calculations, SAFE and convertible-note conversion, option pool mechanics, preference stack ordering, anti-dilution calculations, and ESOP vesting. Covers standard venture-capital structures (YC SAFEs, standard convertible notes, Series seed/A/B terms) with cross-MENA awareness for UAE ADGM/DIFC structures and KSA arrangements.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-cap-table-sanity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Cap Table Sanity Check

Systematic review of a capitalization table for mathematical accuracy, structural correctness, and consistency with the transaction documents. Catches common errors that regularly escape manual review — especially in complex structures with SAFEs, convertible notes, and multi-round preference stacks.

## When to use this

- Pre-closing review of a funding round: confirm the post-money table matches the term sheet math
- Due diligence as a new investor: verify the table you are investing on is accurate
- Legal review of a shareholders' agreement: check that ESOP, anti-dilution, and preference provisions are correctly reflected
- Audit of a cap table prepared by a third-party cap-table management platform (Carta, Pulley, AngelList)
- Pre-IPO or pre-acquisition cleanup: identify errors before they surface in a data room

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Cap table spreadsheet or data | The subject of review | Required |
| Term sheet or investment agreement | The contractual basis for the current round | Required if reviewing round math |
| Shareholders' agreement | Preference, anti-dilution, and ESOP terms | Required for structural review |
| SAFE and convertible note documents | Conversion terms; valuation cap; discount; pro-rata | Required if SAFEs/notes are on the table |
| Prior round documents | Prior preferences, anti-dilution ratchets | Required if multi-round |

## Review checklist

### 1. Basic arithmetic

- [ ] Total shares issued = sum of all class columns
- [ ] Percentage column: each holder's % = holder shares / total shares × 100; columns sum to 100%
- [ ] Pre-money valuation + investment amount = post-money valuation
- [ ] Price per share = pre-money valuation / pre-money shares outstanding (check whether pre-money or post-money SAFE SAFEs affect the share count denominator)

**Common error**: treating SAFEs as not yet "shares" for the purposes of the share count denominator when computing price per share — depending on whether the SAFE is "pre-money" (YC v2 standard) or "post-money" (YC standard as of 2018), the calculation differs materially.

### 2. SAFE conversion math

SAFEs convert at the next qualified financing. Check:

- **Valuation cap**: SAFE converts at the lower of: (a) cap / shares outstanding on conversion, or (b) price per share in the round. Formula: `conversion price = min(cap / fully-diluted pre-money shares, round price)`
- **Discount**: some SAFEs have a discount rate (e.g., 20%) applied to the round price. `conversion price = round price × (1 − discount rate)`
- **Most Favored Nation (MFN) clause**: if the SAFE has MFN, check whether any subsequent SAFE had a lower cap or higher discount that must be adopted
- **Post-money SAFE (YC v2018+)**: the post-money cap denominator includes the new option pool shares (post-option-pool-shuffle) but excludes converting SAFEs — a frequent source of error
- **Pre-money SAFE (YC pre-2018 / v1.5)**: the pre-money denominator is the pre-round, pre-pool shares — smaller denominator, more dilutive to founders

Verify that the SAFE conversion produces the correct number of shares and is reflected accurately in the resulting ownership percentages.

### 3. Convertible note conversion

- `Shares from note = (principal + accrued interest) / conversion price`
- Accrued interest: `= principal × annual interest rate × (days held / 365)`
- Conversion price: apply the same cap/discount logic as SAFEs, or the specific conversion formula in the note

**Common error**: forgetting to accrue interest on old convertible notes, especially notes that have been outstanding for 2+ years.

### 4. Fully-diluted share count

Fully-diluted shares must include all of the following:
- Common shares issued
- Preferred shares issued (on as-converted basis)
- SAFEs outstanding (converted to shares at applicable conversion price)
- Convertible notes outstanding (converted at applicable conversion price + accrued interest)
- All options outstanding (both vested and unvested)
- All warrants outstanding
- Unissued but reserved ESOP pool shares

**Common error**: excluding unissued ESOP pool shares from the fully-diluted count. Investors typically require the pool to be fully reserved before the round closes (the "option pool shuffle"), meaning those shares must be reflected in the pre-money fully-diluted share count.

### 5. Option pool — pre-money pool expansion

The standard venture term: the option pool is established or expanded pre-closing, using pre-money shares (founder dilution). Steps:

1. Determine the post-closing pool size required (typically 10–20% of post-money fully-diluted)
2. Compute: `new shares for pool = required pool post-money × total post-money shares − existing unissued pool`
3. These new pool shares come from the pre-money share count → dilutes founders before the investor arrives

Verify: the pool expansion math is correctly reflected in the pre-money denominator used to compute the investor's price per share.

### 6. Preference stack ordering

For each class of preferred shares:
- **Liquidation preference amount**: standard is 1× non-participating preferred (investor gets back their money first; then converts to common to participate). Some rounds have 1× participating (investor gets 1× back + participates in remainder).
- **Participating with cap**: investor participates up to a total of Nx their original investment, then converts.
- **Stack ordering**: Series B preferred liquidates before Series A preferred liquidates before common — confirm the seniority stack matches the investment documents.
- **Waterfall calculation**: for a hypothetical exit at [X], compute each class's payout in order. Verify the table correctly shows the distribution.

**Critical check**: anti-dilution ratchets from prior rounds must be re-computed if the new round price is below the prior round price (a "down round"). If anti-dilution is triggered, the prior round investors receive additional shares (or a lower conversion price) — this must be reflected before the new round is calculated.

### 7. Anti-dilution math

Most venture-backed preferred shares carry broad-based weighted average anti-dilution protection:

`New Conversion Price = Old Conversion Price × (Old Shares + Consideration ÷ Old Price) ÷ (Old Shares + New Shares)`

Where:
- `Old Shares` = fully-diluted pre-new-issuance shares
- `Consideration` = total consideration for the new issuance
- `New Shares` = shares issued in the new round

Verify: if the new round is a down round, re-compute the conversion price for affected prior classes and confirm the resulting additional shares are included in the table.

Narrow-based weighted average and full-ratchet anti-dilution provide more protection for investors and are more dilutive to founders — confirm which applies under the SHA.

### 8. Drag-along and tag-along trigger thresholds

These are not mathematical checks but document-consistency checks:
- The drag-along threshold (e.g., 60% of preferred + majority of common) must match the SHA
- The tag-along rights (each seller must give co-sale rights to others pro-rata) must be consistent with the cap table structure
- Confirm that the current ownership structure actually satisfies or would satisfy the drag/tag thresholds

### 9. ESOP vesting

- Standard: 4-year vesting with 1-year cliff (25% vests at the 1-year anniversary; remainder monthly over 36 months)
- Check: grant date, cliff date, monthly vesting schedule, acceleration provisions
- Unvested options: shown as "outstanding" in the cap table but employees have no current right to those shares
- Early-exercise provisions (83(b) elections): common in US tech; check whether applicable in the jurisdiction
- ESOP expiry: standard is 90 days post-termination to exercise vested options; 10-year expiry from grant date — check alignment with option grant agreement

## Output format

```json
{
  "findings": [
    {
      "row": "cell or row reference",
      "issue": "description of the error or inconsistency",
      "expectedValue": "what the correct value should be",
      "actualValue": "what the table currently shows",
      "severity": "critical | material | minor",
      "category": "arithmetic | SAFE-conversion | option-pool | preference | anti-dilution | vesting"
    }
  ],
  "summaryStats": {
    "totalSharesVerified": boolean,
    "fullyDilutedCorrect": boolean,
    "postMoneyMathCorrect": boolean,
    "safeConversionVerified": boolean,
    "antiDilutionChecked": boolean
  },
  "reconciledTable": "note: corrected cap table provided as separate output if corrections were material",
  "flagsForCounsel": ["items requiring legal document review or founder/investor confirmation"]
}
```

## MENA-specific notes

### UAE ADGM / DIFC structures
Many MENA startups are structured with a UAE holdco in ADGM or DIFC holding a UAE operating company. Cap table mechanics follow standard venture-capital conventions (ADGM Companies Regulations closely track English company law). Key distinction: ADGM/DIFC entities use the concept of "authorized share capital" — ensure the authorized capital is sufficient to accommodate the post-round fully-diluted share count, or update the Memorandum of Incorporation.

### KSA
Saudi Arabia's new Companies Law (Royal Decree M/132 of 2022) introduced more flexibility in company structures but venture equity structures in KSA typically use a foreign holding company (ADGM, DIFC, Cayman, or Delaware) with a KSA operating subsidiary. Cap-table review should cover the holding structure, not just the KSA entity.

### Common bugs (summary)

1. Treating post-money SAFEs as pre-money SAFEs in the conversion denominator
2. Failing to accrue interest on old convertible notes
3. Excluding unissued ESOP pool shares from the pre-money fully-diluted denominator
4. Forgetting anti-dilution ratchet recalculation in down rounds
5. Mis-applying the option pool shuffle (computing it post-money rather than pre-money)
6. Not updating authorized capital in UAE/UK entities after a new share issuance

## Related skills

- [[research-jurisdiction-comparison]]
- [[review-compliance-gap-analysis]]
- [[draft-sha-standard]]
- [[review-governing-law-conflict]]
