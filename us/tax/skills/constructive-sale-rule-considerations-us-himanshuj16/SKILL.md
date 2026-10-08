---
name: constructive-sale-rule-considerations-us-himanshuj16
title: When to Use
description: Use when hedging an appreciated position in a US taxable account and an offsetting transaction could trigger an immediate constructive sale under IRC 1259, such as a short against the box, offsetting notional contract, or a forward.
author: HimanshuJ16
author_url: https://github.com/HimanshuJ16/Algo-Trading-Skills/tree/main/skills/constructive-sale-rule-considerations-us
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Standards
  path: references/standards.md
- title: Workflows
  path: references/workflows.md
---

## When to Use

Use this skill when managing US taxable portfolios, tax-loss harvesting algorithms, or hedging strategies against appreciated long positions. Under **26 U.S.C. § 1259**, entering into certain offsetting transactions against an appreciated financial position triggers an immediate **constructive sale**: gain is recognized as if the position were sold at fair market value **on the date the offsetting transaction is entered into**, even though the long position is still held.

Only four transaction categories are constructive sales by operation of the statute (§ 1259(c)(1)(A)–(D)):

| Transaction | Citation |
|---|---|
| Short sale of the same or substantially identical property | § 1259(c)(1)(A) |
| Offsetting notional principal contract (equity swap meeting § 1259(d)(2)) | § 1259(c)(1)(B) |
| Futures or forward contract to deliver the property | § 1259(c)(1)(C) |
| Acquiring the property when the appreciated position is itself a short/ONPC/forward | § 1259(c)(1)(D) |

## When NOT to Use

- **Options-based structures.** Collars, in-the-money puts, and similar transactions are **not** listed in § 1259(c)(1)(A)–(D). They can reach § 1259 only through § 1259(c)(1)(E), which applies "to the extent prescribed by the Secretary in regulations" — and Treasury has never issued those regulations. The engine returns `MANUAL_REVIEW_REQUIRED` for these; do not let an agent auto-classify them.
- **Marked-to-market positions.** § 1259(b)(2)(C) excludes positions already marked to market (§ 1256 contracts, securities held under a § 475(f) election) from the definition of an appreciated financial position.
- **Non-US taxpayers or non-US tax regimes.** This skill encodes US federal income tax only.
- **As a substitute for tax advice.** The engine is a deterministic audit aid; a qualified US tax adviser owns the filing position.

## Prerequisites

- Python 3.10+ and the standard library only (`datetime`, `dataclasses`, `typing`, `math`, `logging`).
- Long position cost basis and fair market value **as of the offsetting transaction's entry date** (§ 1259(a)(1) measures gain at that date, not at the reporting date).
- Entry date, close date, and the end of the taxable year **in which the transaction was entered into** (not always Dec 31 — fiscal-year filers supply their own).
- Any disposal of the long position, and any § 246(c)(4) risk-reduction events, in the 60 days after the close.

## Workflow

1. **Appreciated position gate (§ 1259(b))**: If the position is marked to market, or FMV ≤ cost basis, exit with `NOT_APPLICABLE`. § 1259 reaches only positions that would produce gain on a sale.
2. **Per se trigger classification (§ 1259(c)(1))**: Map the offsetting transaction to (A)–(D). If it does not map — a collar, an ITM put, a variable prepaid forward with non-fixed quantity — return `MANUAL_REVIEW_REQUIRED` and escalate. Do **not** infer a trigger from § 1259(c)(1)(E) while no regulations exist under it.
3. **Scope the constructive sale**: A partial hedge constructively sells only the hedged portion. Supply `offsetting_quantity` so gain is pro-rated rather than recognizing the entire lot.
4. **Safe harbor test A — 30-day close (§ 1259(c)(3)(A)(i))**: The transaction must be closed on or before the 30th day after the close of that taxable year. For a Dec 31 year end that is Jan 30; for a Jun 30 year end it is Jul 30. Not closed, or closed later ⟹ `CONSTRUCTIVE_SALE_TRIGGERED`.
5. **Safe harbor test B — 60-day holding (§ 1259(c)(3)(A)(ii))**: The taxpayer must hold the appreciated position throughout the 60-day period *beginning on the close date* (close date is day 1, so the period ends on close + 59 days). Disposal inside that period ⟹ triggered.
6. **Safe harbor test C — 60-day unhedged (§ 1259(c)(3)(A)(iii) via § 246(c)(4))**: No risk-of-loss reduction at any time in that period — no option to sell, no contractual obligation to sell, no open short in substantially identical property, no written call.
7. **Apply the (c)(3)(B) carve-out before concluding**: A risk-reducing transaction entered *inside* the 60-day window is itself **disregarded** if it is closed by the 30th day after the close of the first transaction's taxable year and it independently satisfies clauses (ii) and (iii). Re-hedging inside the window is therefore not automatically fatal — check (c)(3)(B) first. Chained re-hedges are not clearly covered by the statute and return `MANUAL_REVIEW_REQUIRED`.
8. **Emit the § 1259(a) consequences**: On a trigger, recognize `FMV(entry_date) − basis` on the hedged quantity, set the new basis to that FMV (§ 1259(a)(2)(A)) and restart the holding period on the constructive sale date (§ 1259(a)(2)(B)).

> Full procedure: see `references/workflows.md`.
> Statutory citations: see `references/standards.md`.
> Printable pre-flight checklist: see `assets/checklist.md`.

## Common Pitfalls

- **Treating an ITM put or collar as a per se trigger.** § 1259(c)(1) does not list options. Congress left them to regulations under (c)(1)(E) that have never been issued. Auto-recognizing gain here overstates the taxpayer's liability on a position the statute does not reach.
- **Valuing the gain at the reporting date.** § 1259(a)(1) fixes FMV on the constructive sale date — the date the offsetting transaction was entered into. Feeding today's FMV into a December trigger produces a wrong number in both directions. Pass `valuation_date` so the engine rejects a mis-dated price instead of silently using it.
- **Confusing the two rules about puts.** Buying a protective put is not itself a constructive sale, but holding one **does** reduce risk of loss under § 246(c)(4)(A) — so it breaks the § 1259(c)(3)(A)(iii) safe harbor for a *different*, already-closed short. The two questions have different answers.
- **Assuming re-hedging inside the 60 days is always fatal.** § 1259(c)(3)(B) can disregard the second transaction if it is closed by the same 30-day deadline and stands clean on its own 60-day test.
- **Forgetting the holding requirement.** § 1259(c)(3)(A)(ii) requires holding the long *throughout* the 60 days. Closing the short in time and then selling the stock 20 days later loses the safe harbor even though nothing was re-hedged.
- **Hard-coding Jan 30.** The deadline is 30 days after *the taxpayer's* year end. Fiscal-year entities have a different date.
- **Ignoring the related-person rule.** § 1259(c)(1) applies when "the taxpayer (or a related person)" enters into the transaction. Hedging in a second entity or a spouse's account does not avoid the rule; this engine evaluates one account at a time, so aggregate across related accounts before calling it.
- **Applying it to positions held at a loss.** § 1259 reaches only appreciated financial positions (FMV > cost basis).

## Verification

- Instantiate `ConstructiveSaleRuleEngine`. Test an appreciated long ($100k basis, $250k FMV) hedged by a short entered Dec 1, 2025 and closed Jan 15, 2026, held clean for 60 days ⟹ `SAFE_HARBOR_QUALIFIED`. Change the close to Jan 31, 2026 ⟹ `CONSTRUCTIVE_SALE_TRIGGERED` with $150,000 gain, adjusted basis $250/share, and holding period restarting Dec 1, 2025.
- Confirm an `ITM_PUT` offsetting transaction returns `MANUAL_REVIEW_REQUIRED`, not a trigger.
- Run the suite:

```bash
python -m unittest discover -s skills/constructive-sale-rule-considerations-us/scripts
```

## Related Skills

- `wash-sale-rule-tracking-us`
- `cross-strategy-tax-lot-optimization`
- `mark-to-market-election-for-active-traders-us`
- `section-1256-contract-tax-treatment-us-futures`
