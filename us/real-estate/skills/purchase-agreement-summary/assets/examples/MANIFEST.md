# Purchase Agreement Summary — Example Manifest

All files in this directory are **synthetic**. Property addresses, parties, brokers, dollar amounts, and dates are fabricated. Nothing here is a real transaction or a real person.

| File | Type | Form basis | Practice notes |
|---|---|---|---|
| `purchase-agreement-summary-example.md` | Finished summary | TREC 20-17 (Texas One to Four Family Residential Resale) | Demonstrates Deal Snapshot, all 15 sections, the chronological deadlines table, and the flag triage. Includes a TX-specific Option Fee callout to show how the state overlay applies. |

## How to use

The example shows the deliverable an agent should produce when given a complete executed Texas residential purchase-agreement package (PA + amendments + addenda + disclosures).

Comparing an agent run to this example:

- All 15 sections in `references/OUTPUT-STRUCTURE.md` should appear, in order.
- Form version must be in the header (e.g., "TREC 20-17").
- Wording will differ; structure must match.
- The Option Fee must be tracked separately from EMD (TX-specific).
- Every value must trace to the Source Map (Section 15).
- The verbatim disclaimer must appear at the end.

Examples for additional state forms (C.A.R. RPA-CA, FAR/BAR, NJAR, etc.) are deferred. The state-overlay table in `references/STATE-OVERLAYS.md` provides sufficient guidance for an agent to handle any state form whose entry exists; for states not in the table, the deliverable should include a "local-counsel review recommended" flag.
