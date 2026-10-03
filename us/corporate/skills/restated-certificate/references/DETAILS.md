# Restated Certificate - Detailed References

Use this file with `SKILL.md` for formulas and clause checklists that are easier to validate outside the core drafting flow.

## Anti-Dilution Formula (Broad-Based Weighted Average)

```
Adjusted CP = CP x (A + B) / (A + C)

Where:
  CP = Conversion Price in effect immediately before new issuance
  A  = Common shares outstanding on a fully diluted, as-converted basis
  B  = Aggregate consideration received divided by CP
  C  = Number of shares actually issued in the new issuance
```

## Anti-Dilution Carve-Outs Checklist

- [ ] Employee or consultant equity under board-approved plans
- [ ] Bank or equipment-lender securities
- [ ] Strategic partner, vendor, or customer issuances approved by the board
- [ ] Sponsored research or collaboration issuances approved by the board
- [ ] Acquisition consideration approved by the board
- [ ] Conversion or exercise of existing convertible securities
- [ ] Stock splits, stock dividends, or recapitalizations
- [ ] Securities approved by required Preferred holders

## Protective Provisions Checklist

- [ ] Amend charter or bylaws in a way adverse to Preferred
- [ ] Authorize or create senior or pari passu stock
- [ ] Increase or decrease authorized Preferred or Common
- [ ] Declare dividends or distributions on Common
- [ ] Redeem or repurchase Common or Preferred (except narrow employee repurchase carve-outs)
- [ ] Liquidate, dissolve, or wind up
- [ ] Approve a deemed liquidation event (M&A or material asset sale)
- [ ] Amend transaction documents adversely to Preferred
- [ ] Change board size
- [ ] Incur debt above agreed thresholds
- [ ] Exclusively license or dispose of material IP

Confirm whether each item requires a class-wide Preferred vote, separate series votes, or both.

## Liquidation Waterfalls

### Non-Participating Preferred

1. Pay Preferred liquidation preference (OIP x multiple + accrued dividends).
2. Distribute remaining proceeds to Common only.
3. Permit each Preferred holder to elect conversion and share pro rata with Common if economically superior.

### Participating Preferred (with Cap)

1. Pay Preferred liquidation preference.
2. Share remaining proceeds pro rata among Preferred (as-converted) and Common.
3. Stop Preferred participation at the negotiated cap (for example, 3x OIP), then route excess proceeds to Common.

## Math Validation Pass

- Test at low, mid, and high exit values.
- Compare converted vs. non-converted outcomes for each series.
- Verify no circular references in conversion calculations.
- Confirm cap-table assumptions match transaction documents and board materials.
