# Pre-Flight Checklist

## Placement and control
- [ ] Is the pre-trade risk engine positioned synchronously before the FIX router?
- [ ] Are the controls under the participant's direct and exclusive control, including any provided by a third party (NI 23-103 s.3(5))?
- [ ] Can the automated order system be disabled immediately, with its in-flight orders prevented from reaching a marketplace (NI 23-103 s.5(3))?

## Thresholds
- [ ] Is every threshold set deliberately, with a documented owner and rationale — not left at a library default?
- [ ] Are price collars linked to a live reference price rather than a hardcoded level?
- [ ] Is the value of *unexecuted* orders limited, either via `max_open_order_notional_cad` or somewhere else in the stack (UMIR Policy 7.1)?
- [ ] Is there a documented cadence for reassessing threshold adequacy (NI 23-103 s.3(6))?

## Fail-closed behaviour
- [ ] Are orders rejected — not passed — when the reference price is missing, zero or non-finite?
- [ ] Are non-finite (`NaN`/`inf`), negative or zero quantities and prices rejected before any threshold comparison?
- [ ] Does the routing path either branch on `is_compliant` or use `enforce_order`, so a rejected order cannot leak through an unchecked return value?

## UMIR 6.2 designations
- [ ] Does the engine block a sale that exceeds owned inventory unless it is marked "short"?
- [ ] Does it also block a fully covered sale that is *over*-marked "short"?
- [ ] Is `account_is_short_marking_exempt` sourced from account reference data, and does every order from such an account — purchases included — carry the SME designation and no short marker?
- [ ] Is the SME designation prevented on accounts that do not qualify?

## Audit
- [ ] Are all rejected orders, with every violation code, logged persistently for supervisory review under UMIR 7.1?
- [ ] Does the controls documentation cite current rules only — no reliance on the repealed UMIR 3.1 tick test?
