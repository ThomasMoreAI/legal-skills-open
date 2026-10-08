# Standards for the Constructive Sale Rule (26 U.S.C. § 1259)

Jurisdiction: **United States federal income tax only.** All requirements below
are **mandatory statutory rules**, not guidance. Section 1259 was enacted by the
Taxpayer Relief Act of 1997 (Pub. L. 105-34, § 1001).

| Requirement | Citation | Engineering standard |
|---|---|---|
| Appreciated financial position | § 1259(b)(1) | Applies only where there "would be gain were such position sold, assigned, or otherwise terminated at its fair market value". Loss and break-even positions are out of scope. |
| Marked-to-market exclusion | § 1259(b)(2)(C) | Positions marked to market (e.g. § 1256 contracts, securities under a § 475(f) election) are NOT appreciated financial positions and MUST be excluded before any trigger test. |
| Per se triggers | § 1259(c)(1)(A)–(D) | Short sale; offsetting notional principal contract; futures or forward contract to deliver; and acquiring the property where the appreciated position is itself a short/ONPC/forward. |
| Non-enumerated transactions | § 1259(c)(1)(E) | Other transactions with "substantially the same effect" are constructive sales only "to the extent prescribed by the Secretary in regulations". No such regulations have been issued, so collars and in-the-money options MUST NOT be auto-classified as constructive sales; escalate for human review. |
| Non-marketable security contracts | § 1259(c)(2) | A contract for sale of a non-marketable security (as defined in § 453(f)) is excluded if it settles within one year. Not modelled by this engine — out of scope for exchange-traded strategies. |
| Safe harbor — 30-day close | § 1259(c)(3)(A)(i) | The transaction MUST be "closed on or before the 30th day after the close of such taxable year" — the taxable year in which it was entered into. Deadline = that year end + 30 days; it is not universally Jan 30. |
| Safe harbor — 60-day holding | § 1259(c)(3)(A)(ii) | The taxpayer MUST hold the appreciated financial position "throughout the 60-day period beginning on the date such transaction is closed". Day 1 is the close date, so the period ends on close + 59 days. |
| Safe harbor — 60-day unhedged | § 1259(c)(3)(A)(iii) | At no time in that 60-day period may the taxpayer's risk of loss be reduced "by reason of a circumstance which would be described in section 246(c)(4)". |
| Risk-of-loss reduction | § 246(c)(4)(A)–(C) | An option to sell, a contractual obligation to sell, an open short sale of substantially identical property, or writing a call. The flush text carves out qualified covered calls (§ 1092(c)(4)); this engine does NOT model that carve-out — flag QCCs for manual review. |
| Second-transaction carve-out | § 1259(c)(3)(B) | A risk-reducing transaction entered during the 60-day window is disregarded for the (A)(iii) test if it is closed by the 30th day after the close of the first transaction's taxable year AND itself satisfies clauses (ii) and (iii) of (A). Chained relief is not clearly authorised; escalate. |
| Gain measurement | § 1259(a)(1) | Gain is recognized "at its fair market value on the date of such constructive sale" — the date the offsetting transaction is entered into, not the reporting date. |
| Post-sale consequences | § 1259(a)(2)(A)–(B) | Basis MUST be adjusted for the gain recognized, and the holding period MUST be determined as if the position were acquired on the constructive sale date. |
| Related persons | § 1259(c)(1) | The rule applies when "the taxpayer (or a related person)" enters into the transaction. Aggregate related accounts before evaluating. |

## Primary sources

- 26 U.S.C. § 1259 — https://uscode.house.gov/view.xhtml?req=(title:26%20section:1259%20edition:prelim)
- 26 U.S.C. § 1259 (Cornell LII) — https://www.law.cornell.edu/uscode/text/26/1259
- 26 U.S.C. § 246(c)(4) — https://www.law.cornell.edu/uscode/text/26/246

## Known limitations

- Whether property is "the same or substantially identical" is asserted by the
  caller, not determined by the engine.
- § 1259(c)(2) non-marketable-security contracts and the § 246(c)(4) qualified
  covered call carve-out are not implemented.
- No Treasury regulations exist under § 1259(c)(1)(E); any conclusion about
  collars or in-the-money options is a human judgment call.
