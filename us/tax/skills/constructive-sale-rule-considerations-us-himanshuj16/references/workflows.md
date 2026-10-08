# Workflows for the Constructive Sale Rule (26 U.S.C. § 1259)

1. **Position eligibility (§ 1259(b))**:
   - If the position is marked to market (§ 1256 contract, § 475(f) election) ⟹ exit `NOT_APPLICABLE` per § 1259(b)(2)(C).
   - Compute $\text{Unrealized Gain} = \text{FMV}(D_{entry}) - \text{Cost Basis}$, where $\text{FMV}$ is measured on the offsetting transaction's entry date per § 1259(a)(1).
   - If $\text{Unrealized Gain} \le 0 \implies$ exit `NOT_APPLICABLE` (§ 1259 reaches only appreciated positions).
2. **Trigger classification (§ 1259(c)(1))**:
   - Map the offsetting transaction to (A) short sale, (B) offsetting notional principal contract, (C) futures/forward to deliver, or (D) acquisition of identical property.
   - Anything else (collar, ITM put, option strategy) ⟹ `MANUAL_REVIEW_REQUIRED`. § 1259(c)(1)(E) is inert absent Treasury regulations.
3. **Scope (partial hedges)**:
   - $\text{Gain at risk} = \text{Unrealized Gain} \times \frac{\min(Q_{offset},\, Q_{long})}{Q_{long}}$.
4. **Safe harbor verification (§ 1259(c)(3)(A))**:
   - Check (i): $D_{close} \le \text{Tax Year End} + 30\text{ days}$, where the tax year is the one in which the transaction was **entered into**.
   - Define the window $W = [D_{close},\; D_{close} + 59\text{ days}]$ — a 60-day period beginning on the close date.
   - Check (ii): the long position is held throughout $W$ (no disposal on or before $\max W$).
   - Check (iii): no § 246(c)(4) risk-of-loss reduction begins at any time in $W$.
5. **Second-transaction carve-out (§ 1259(c)(3)(B))**:
   - For each risk reduction beginning in $W$, disregard it if it is closed by the same $\text{Tax Year End} + 30\text{ days}$ deadline **and** its own window $W' = [D'_{close},\; D'_{close} + 59\text{ days}]$ contains no disposal and no further risk reduction.
   - A further risk reduction inside $W'$ would require chained relief, which the statute does not clearly authorise ⟹ `MANUAL_REVIEW_REQUIRED`.
6. **Result generation**:
   - All checks pass ⟹ `SAFE_HARBOR_QUALIFIED`; the transaction is disregarded and no gain is recognized.
   - Any check fails ⟹ `CONSTRUCTIVE_SALE_TRIGGERED` on $D_{entry}$:
     - Recognize $\text{Gain at risk}$ (§ 1259(a)(1)).
     - Set adjusted basis per share $= \text{FMV}(D_{entry})$ (§ 1259(a)(2)(A)).
     - Restart the holding period on $D_{entry}$ (§ 1259(a)(2)(B)).
7. **Aggregation before filing**:
   - Repeat per tax lot and per related account (§ 1259(c)(1) reaches "the taxpayer (or a related person)") before reporting.
