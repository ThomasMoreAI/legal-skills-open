# Workflows for CIRO (formerly IIROC) Electronic Trading Compliance

1. **System Design**: Place `CiroPreTradeRiskEngine` in the execution path after the algo
   generates the order but *before* the FIX session logic. NI 23-103 does not prescribe
   where the filters sit relative to a smart order router — that placement is the
   participant's decision — but the controls must be under the participant's direct and
   exclusive control (s.3(5)), not the vendor's or the client's.
2. **Configuration**: Set every threshold explicitly and record who approved it:
   - `max_order_quantity` and `max_order_value_cad` — the s.3(3)(a) size and
     credit/capital parameters.
   - `max_price_deviation_pct` — the fat-finger collar. No regulator prescribes a value;
     calibrate per instrument liquidity and document the basis.
   - `max_open_order_notional_cad` — the Policy 7.1 control on unexecuted order value.
     Leaving it `None` disables it; if you do, record where that obligation is met
     instead.
3. **Data Hydration**: Enrich the order with the current reference price and the account's
   owned position in the security. `current_inventory` is a proxy for the UMIR concept of
   ownership, which is broader (securities owned through an agent or trustee, plus the
   deemed-ownership provisions of UMIR 1.2); a firm using a broader definition must feed
   the broader figure. Set `account_is_short_marking_exempt` from account reference data,
   not from strategy configuration — SME status is a property of the account.
4. **Execution**:
   - Call `validate_order(order)` and branch on `is_compliant`, or call `enforce_order(order)`
     and let `RegulatoryViolationError` block the routing path.
   - On rejection, log every `ViolationCode` in `result.violations` — one order can breach
     several controls at once, and truncating to the first hides the rest from supervision.
   - Do **not** retry a rejected order unchanged, and do not widen a threshold at runtime
     to let a specific order through. Threshold changes are a documented control change
     under s.3(5)/s.3(6), not an operational workaround.
5. **Degraded Market Data**: The engine rejects with `REFERENCE_PRICE_UNAVAILABLE` when the
   reference price is missing, zero or non-finite. Treat a burst of these as a feed
   incident and stop the strategy — do not disable the check to keep trading.
6. **Audit Logging**: Write all rejections to immutable (WORM) storage for supervisory and
   regulatory review, and reassess the adequacy of the thresholds on a documented cadence
   as required by NI 23-103 s.3(6).
