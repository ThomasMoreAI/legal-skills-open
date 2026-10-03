# Reasonableness Review Methodology

How to assess whether medical charges are "usual, customary, and reasonable" (UCR) without testifying as a billing expert. Loaded by Step 5 of the parent SKILL.md.

**Operating principle.** Produce a benchmark **range**, not a single "reasonable amount." The fact-finder (or a retained billing expert) decides reasonableness. Naming benchmark sources, percentiles, and methodology is the deliverable; opining is not.

---

## Three Distinct Numbers (do not conflate)

| Number | What It Is | Where It Lives |
|---|---|---|
| **Chargemaster (billed)** | Provider's list price. Largely arbitrary. | UB-04 / CMS-1500 "Total Charges" |
| **Allowed amount (negotiated)** | What an insurer's contract permits | EOB "Allowed Amount" column |
| **Paid amount** | What was actually transferred (insurer + patient) | EOB "Plan Paid" + "Patient Resp." |

For hospitals, chargemaster commonly runs materially higher than the Medicare-allowed amount for the same service; actual multiples vary by facility, code, and year and must be retrieved, not estimated `[VERIFY per facility/code/CY]`. A chargemaster total alone is not evidence of reasonableness — flag every reasonableness analysis that relies on chargemaster as the only data point.

---

## Benchmark Sources

| Source | Type | How to Cite | Notes |
|---|---|---|---|
| **FAIR Health FH Benchmarks** | Commercial allowed amounts by geozip and percentile (50/75/80/90th) | "FH Benchmarks, geozip ___, percentile ___, retrieved [date]" | Subscription required; commonly used by courts and arbitrators. `[VERIFY: subscription / data run obtained]` |
| **Medicare Physician Fee Schedule (MPFS)** | CMS-set rates by HCPCS, locality, and year | "CMS MPFS, locality ___, CY ___, HCPCS ___" | Public, free; often cited as a floor. Locality matters. |
| **Medicare OPPS / IPPS** | Outpatient APC and inpatient DRG rates | "CMS OPPS APC ___, CY ___" / "CMS IPPS DRG ___, CY ___" | Use for facility benchmarking. |
| **State workers' comp fee schedule** | State-regulated maximums | "[State] DWC fee schedule, CY ___, code ___" | State-specific; many PI cases borrow as a reference even if WC does not apply `[VERIFY admissibility]`. |
| **Commercial allowed-amount data from case EOBs** | Real-world payer rates | "EOB [doc-label, p. N, Bates ___]" | Strongest evidence: it is what was actually paid in this case. |
| **Hospital price-transparency files (CMS rule)** | Posted negotiated rates and self-pay rates per facility | "[Hospital] machine-readable file, retrieved [date]" | Quality varies; often incomplete. `[VERIFY]` each retrieval. |

**Do not invent.** Never quote a FAIR Health percentile, a CMS rate, or a hospital posted rate that has not been actually retrieved. If no benchmark was run, the deliverable says "benchmark not obtained — recommend billing-expert review."

---

## Geographic Adjustment

- FAIR Health uses **geozip** (first three digits of ZIP).
- Medicare uses **locality** (state or sub-state region).
- Workers' comp uses state.
- Always match the benchmark's geography to the place of service, not the patient's home.

## Percentile Methodology

When using FAIR Health or comparable percentile data, present the band — typically 50th, 80th, and 90th percentile — and note where the case charge falls. Do not pick a single percentile as "reasonable" without explicit direction from counsel; courts and arbitrators differ.

---

## Letters of Protection (LOP) Scrutiny

Where treatment is rendered under an LOP (provider holds bill pending settlement):
- Billed amounts under LOP are **commonly higher** than market rates. Treat with skepticism.
- Many LOP providers do not have payer contracts; chargemaster IS the bill.
- Disclosure of LOP, referral source, and any factoring/discounting of the receivable is required in some jurisdictions and is fertile cross-examination ground `[VERIFY: jurisdiction]`.
- Recent appellate trends in some states (e.g., Florida) have addressed admissibility of LOP-related amounts and discount evidence — flag for counsel research `[VERIFY: current jurisdiction law]`.

Action: tag every LOP-billed line item, present chargemaster *and* a Medicare/FAIR Health benchmark side-by-side, and surface the LOP disclosure question.

---

## Billed vs. Paid (Jurisdictional)

The skill's main jurisdictional table (in SKILL.md) governs which measure is admissible. This reference adds the operational guidance:

- **In paid-only jurisdictions** (e.g., California per *Howell v. Hamilton Meats*) `[VERIFY current law]`: the recoverable measure is the amount actually paid or owed; chargemaster differential is not admissible to inflate. Carry billed for context, present paid as primary.
- **In collateral-source-rule jurisdictions**: billed charges may be admissible as evidence of value; collateral payments cannot reduce. Present billed as primary, paid as secondary.
- **In hybrid / "reasonable value" jurisdictions**: present both columns plus a UCR benchmark range; the fact-finder picks.

When counsel has not specified, default to carrying both columns and flag the question in Checkpoint B.

---

## How to Present the Reasonableness Section

A short table per major service category:

| Service | CPT/HCPCS | Billed | Paid | MPFS Reference (locality, CY) | FAIR Health 50th / 80th / 90th (geozip) | Notes |
|---|---|---|---|---|---|---|

Then 1–3 sentences interpreting (without opinion):
- "Charge falls at the 90th percentile of FH commercial allowed amounts for geozip ___."
- "Billed amount is approximately N× the MPFS rate for the same code in this locality."
- "Paid amount aligns with the negotiated rate from [payer] per EOB."

Stop short of "the reasonable charge is $X." That is for the fact-finder or a retained billing expert.

---

## When to Recommend a Billing Expert

Flag for retained billing expert when any of the following are true:
- Total billed exceeds $100,000 (or jurisdiction-specific threshold per counsel).
- LOP-billed treatment makes up a material share of damages.
- Reasonableness is the central disputed issue (defense argues paid-only or UCR).
- A specific code's reasonableness requires PTP/MUE analysis or specialty-specific norms.
- Hospital chargemaster is a load-bearing damages exhibit.

A CPC (Certified Professional Coder), CCS, or CHC credential is typical for billing experts; a CPMA (Certified Professional Medical Auditor) is common for compliance-style audits.

---

## What This Reference Does NOT Do

- Does not contain percentile values or rate tables (must be retrieved live from each authority).
- Does not constitute UCR-expert testimony.
- Does not resolve jurisdictional admissibility — that is counsel's call.

## Anti-Hallucination Rules

- Never quote a FAIR Health percentile, MPFS rate, or hospital posted price without an actual retrieval cite (URL, file, date).
- Never describe a "typical UCR" or "average reasonable charge" as if it were a known number.
- Where data was not obtained, write "benchmark not obtained" — never approximate.
