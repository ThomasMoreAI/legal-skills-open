---
name: canada-iiroc-electronic-trading-rules-himanshuj16
title: When to Use
description: Use when routing orders to Canadian marketplaces such as TSX, TSX Venture, Cboe Canada or an ATS, where NI 23-103 section 3 and UMIR Rule 7.1 require automated pre-trade controls and UMIR 6.2 order designations on every order.
author: HimanshuJ16
author_url: https://github.com/HimanshuJ16/Algo-Trading-Skills/tree/main/skills/canada-iiroc-electronic-trading-rules
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
sources:
- title: Standards
  path: references/standards.md
- title: Workflows
  path: references/workflows.md
---

## When to Use

Use this skill when deploying algorithms that route orders to Canadian marketplaces (TSX, TSX Venture, Cboe Canada — formerly NEO — CSE, and the ATSs). Under National Instrument 23-103 s.3 and UMIR Rule 7.1, a marketplace participant must run **automated pre-trade controls** over every order before it reaches a marketplace: credit and capital thresholds, price and size parameters, limits on the value of unexecuted orders, and the regulatory designations that UMIR 6.2 requires on entry.

## When NOT to Use

- **Non-Canadian venues.** These controls are jurisdiction-specific. US market access is governed by SEC Rule 15c3-5 (`sec-rule-15c3-5-risk-controls-us`) and the EU by MiFID II RTS 6 (`mifid-ii-algo-trading-compliance-eu`). The short-marking exempt designation has no US or EU analogue — do not port it.
- **As the firm's only short-sale control.** The engine checks *designation*, not the pre-borrow arrangements UMIR requires for certain short sales, and not failed-trade reporting.
- **As a substitute for marketplace-level controls.** CIRO's marketplace threshold regime (single-stock circuit breakers, price freezes) runs at the venue. It does not discharge the participant's own obligation under NI 23-103 s.3(5) to set and control its own filters.

## Prerequisites

- Trading system that produces normalized order objects with side, quantity, limit price (or `None` for a market order), and the account's owned position in the security.
- A live reference price (last traded price) per symbol. The engine **fails closed** when the reference price is missing, zero or non-finite — plan for stale-feed handling rather than being surprised by rejections.
- Firm-determined threshold values. Neither NI 23-103 nor UMIR prescribes any numeric limit; the participant sets, documents and periodically reassesses each one (NI 23-103 s.3(5), s.3(6)).
- A flag identifying accounts that qualify for the "short-marking exempt" designation.

## Workflow

1. **Rule Initialization**: Instantiate `CiroPreTradeRiskEngine` with a `RiskLimits` object. Set `max_open_order_notional_cad` if you want this engine to enforce the unexecuted-order-value control; leaving it `None` disables it and the obligation falls elsewhere in your stack.
2. **Order Interception**: Call `validate_order(order)` synchronously before the order reaches the FIX gateway, and inspect `is_compliant`. If your routing path has no rejection branch, call `enforce_order(order)` instead — it raises `RegulatoryViolationError` so a forgotten return-value check cannot leak an order to the venue.
3. **Input Sanity, Fail Closed**: Non-positive quantity, non-finite or negative price, and an unusable reference price are rejected up front (`INVALID_ORDER_PARAMETERS`, `REFERENCE_PRICE_UNAVAILABLE`). This is deliberate: `NaN` compares `False` against every threshold, so an unchecked `NaN` price would pass every downstream test.
4. **Size, Notional and Aggregate Checks**: Quantity against `max_order_quantity`; this order's notional against `max_order_value_cad`; and, when configured, `open_order_notional_cad + this order` against `max_open_order_notional_cad`. A market order (`price=None`) is valued at the reference price so it is still caught by the notional controls.
5. **Price Collar**: Limit orders deviating more than `max_price_deviation_pct` from the reference price are rejected. Market orders carry no limit price and are not collared — size and notional are their only constraints here.
6. **UMIR 6.2 Designation Check**: Decide the designation *before* routing, not after:
   - If the account is short-marking exempt, **every** order from it — purchase as well as sale — must carry the SME designation and must not also be marked short (UMIR 6.2(1)(b)(ix)). Its use is mandatory, not optional.
   - Otherwise, a sale of a security the account does not own must be marked "short" (UMIR 6.2(1)(b)(viii)) — and a sale fully covered by owned inventory must **not** be. Over-marking is a misdesignation too.
7. **Rejection Handling**: Log every rejection with its `ViolationCode` and halt routing. Persist the record for supervisory review under UMIR 7.1.

> Full procedure: see `references/workflows.md`.
> Standards reference: see `references/standards.md`.
> Printable pre-flight checklist: see `assets/checklist.md`.

## Common Pitfalls

- **Post-Trade Only**: Relying on T+1 drop-copy reconciliation. NI 23-103 s.3(2) requires automated controls *pre-trade*; post-trade monitoring is an addition to them, not a substitute.
- **Failing Open on Missing Market Data**: Skipping the price collar when the reference price is zero, `None` or `NaN`. A gap in the feed is exactly when a fat-finger order is most dangerous — a control that quietly stops running is worse than no control, because nobody notices.
- **Treating SME as an Optional Extra Flag**: Marking a qualifying account's order both "short" and "short-marking exempt", or marking only sales SME and leaving its purchases unmarked. SME replaces the short marker and applies to both sides of the account's flow.
- **Only Checking Under-Marking**: Marking a fully covered long sale as "short" is a UMIR 6.2 misdesignation in its own right and corrupts the audit trail CIRO relies on.
- **Static Price Limits**: Hardcoding a "$50 limit" instead of linking price collars to the current reference price.
- **Confusing Single-Order and Aggregate Controls**: A per-order notional cap does not satisfy the Policy 7.1 control on the value of *unexecuted* orders. A thousand small orders can breach a capital threshold that no single order does.
- **Citing Repealed Rules in Controls Documentation**: UMIR 3.1 (short sale price restrictions, the tick test) was repealed effective September 1, 2012. Short-sale obligations now live in the UMIR 6.2 designations and the pre-borrow provisions.

## Verification

- Simulate a "fat-finger" market order for 1,000,000 shares and confirm the engine blocks it before FIX transmission.
- Submit an order with a `NaN` limit price and with a zero reference price; confirm both are rejected rather than silently passed.
- Submit a purchase from a short-marking exempt account with no designation; confirm `IMPROPER_SME_MARK`.
- Run `python -m unittest discover -s skills/canada-iiroc-electronic-trading-rules/scripts` and confirm all tests pass.

## Related Skills

- `broker-account-margin-call-handling`
- `best-execution-record-keeping-global`
- `sec-rule-15c3-5-risk-controls-us`
- `mifid-ii-algo-trading-compliance-eu`
