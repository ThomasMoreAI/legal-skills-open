# Early Warning Indicators - Scoring Methodology

This reference defines the weighted scoring system for credit risk assessment. Each indicator contributes points to an overall risk score. The framework is designed to surface compounding risk - a single indicator is a signal, but correlated indicators across categories form a pattern that demands immediate action.

## Indicator Categories and Weights

### Category 1 - Financial Indicators (weight: 2x per indicator)

Financial indicators carry the highest weight because they reflect the company's actual ability to meet obligations.

| Indicator | Points | Detection Source |
|---|---|---|
| Revenue decline > 20% YoY | 2 | eKRS financial statements |
| Negative equity (liabilities > assets) | 4 | eKRS financial statements |
| Current ratio below 1.0 | 2 | eKRS (computed) |
| Net losses for 2+ consecutive years | 3 | eKRS financial statements |
| Interest coverage ratio below 1.5 | 2 | eKRS (computed) |
| Debt-to-equity exceeding 4.0 | 2 | eKRS (computed) |
| Financial statements not filed for 12+ months | 3 | eKRS (absence of data) |
| Auditor qualification or disclaimer | 2 | eKRS financial statements |

**Ratio threshold reference:**

- Current Ratio: healthy > 1.5, warning 1.0-1.5, critical < 1.0
- Quick Ratio: healthy > 1.0, warning 0.5-1.0, critical < 0.5
- Debt-to-Equity: healthy < 2.0, warning 2.0-4.0, critical > 4.0 or negative equity
- Net Profit Margin: healthy > 5%, warning 1-5%, critical < 1% or negative
- Interest Coverage: healthy > 3.0, warning 1.5-3.0, critical < 1.5

**Trend analysis rules:**
- Always compare at least 2 years of data. A single year snapshot is insufficient.
- A deteriorating trend across 3+ ratios simultaneously is worth more than any single critical ratio.
- If only one year of data is available, add 1 point for the data gap itself.

### Category 2 - Governance and Behavioral Indicators (weight: 1.5x per indicator)

Governance changes often precede financial deterioration by 6-12 months. They are leading indicators.

| Indicator | Points | Detection Source |
|---|---|---|
| 2+ board members resigned within 6 months | 3 | KRS Board Members Scraper |
| CEO or CFO departure (no public successor) | 2 | KRS Board / BORME Cese |
| Registered address changed to virtual office | 1.5 | KRS / company registry |
| Sole director is also sole shareholder | 1 | KRS Board + CRBR cross-check |
| Power of attorney revoked (Spain) | 1.5 | BORME Revocacion de poderes |
| Officer removal without replacement (Spain) | 2 | BORME Cese without Nombramiento |
| Capital reduction filed | 2 | BORME Reduccion de capital |

### Category 3 - Registry and Legal Indicators (weight: override)

These are the most definitive signals. Active insolvency proceedings override the scoring system entirely.

| Indicator | Points | Detection Source |
|---|---|---|
| Active insolvency proceeding in KRZ | AUTO CRITICAL | KRZ Debtor Registry |
| Bankruptcy declaration in MSiG | AUTO CRITICAL | MSiG Court Gazette |
| Active Konkursverfahren in Ediktsdatei | AUTO CRITICAL | Austria Ediktsdatei |
| Concurso de acreedores in BORME | AUTO CRITICAL | BORME Corporate Acts |
| Restructuring application filed (MSiG) | 6 | MSiG Court Gazette |
| Sanierungsverfahren opened (Austria) | 6 | Austria Ediktsdatei |
| Liquidation notice published | 8 | MSiG / BORME Disolucion |
| Creditor list published (lista wierzytelnosci) | 8 | MSiG Court Gazette |
| Any MSiG announcement (non-insolvency) | 1 | MSiG Court Gazette |

**AUTO CRITICAL** means the company is immediately classified as Critical risk regardless of the total point score. No further scoring is needed - the recommendation is to stop credit and secure existing receivables.

### Category 4 - Market and Behavioral Signals (weight: 1x per indicator)

These signals are not available from registry data - they come from the user's own knowledge, trade credit databases, or market intelligence. Include them in the assessment when the user provides this context.

| Indicator | Points | Source |
|---|---|---|
| Payment terms extension request (30 to 60+ days) | 2 | User knowledge |
| Supplier complaints in trade credit databases | 2 | User knowledge |
| Unusual discounting or fire-sale pricing | 1.5 | User knowledge |
| Key customer contract lost (publicly known) | 1.5 | User knowledge |
| Sector-wide downturn affecting the company's industry | 1 | User knowledge |
| Negative media coverage about financial difficulties | 1.5 | User knowledge |

## Scoring Thresholds

| Total Score | Risk Level | Recommended Action |
|---|---|---|
| 0-2 | **Low** | Standard credit terms. Annual review cycle. |
| 3-5 | **Medium** | Shorten payment terms. Quarterly monitoring. Request updated financials. |
| 6-8 | **High** | Require prepayment or guarantees. Monthly monitoring. Begin sourcing alternatives. |
| 9+ | **Critical** | Stop all credit immediately. Secure existing receivables. Engage legal counsel. |
| AUTO CRITICAL | **Critical** | Same as 9+ - triggered by any active insolvency proceeding. |

## Cross-Category Amplification

When indicators appear across multiple categories simultaneously, the combined risk is greater than the sum of parts. Apply these amplification rules:

- **Financial + Governance** (e.g., declining revenue AND board resignations): add 2 bonus points. This pattern suggests insiders are aware of problems and leaving.
- **Financial + Registry** (e.g., poor ratios AND MSiG announcement): the MSiG announcement confirms what the ratios predicted. Already likely Critical.
- **Governance + Market** (e.g., officer changes AND supplier complaints): add 1.5 bonus points. External parties are reacting to the same internal problems.
- **Three or more categories triggered**: add 3 bonus points. Multi-category distress rarely reverses without formal proceedings.

## Data Freshness Rules

Registry data has varying degrees of staleness. Account for this:

- eKRS financial statements: companies file annually, so data can be up to 15 months old and still be "current." Beyond 15 months, treat the gap as a warning indicator (+3 points).
- MSiG/KRZ: updated daily. If no results found, the data is fresh and reliable.
- BORME: published daily on business days. Results reflect status as of the prior business day.
- Ediktsdatei: updated in real-time by Austrian courts. Very reliable.
- KRS Board: extracted from court filings, so there can be a 1-3 month delay between a change and its appearance in the registry.
