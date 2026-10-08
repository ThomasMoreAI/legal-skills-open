# IRC §1202 — Detailed Test Reference

## Gross Asset Test: Calculation Method

Aggregate gross assets = sum of:
- Cash and cash equivalents (all accounts)
- Adjusted tax basis of all property (NOT fair market value)
- Equipment at cost basis minus depreciation
- Intellectual property at cost basis (often $0 if internally developed)
- Investments at cost basis
- Subsidiary assets (>50% owned) at adjusted basis

**Common mistakes:**
- Using FMV instead of adjusted basis (makes the number too high)
- Forgetting to include subsidiary assets
- Not tracking assets at each issuance date (the test applies at each issuance)
- Applying the wrong threshold: $50M for stock issued on or before 2025-07-04, $75M (indexed from 2027) for stock issued after

## Active Business Test: Revenue Classification

| Revenue Type | Qualified? | Notes |
|-------------|-----------|-------|
| SaaS subscription revenue | Yes | Core qualified activity |
| Software license fees | Yes | Core qualified activity |
| Platform transaction fees | Yes | Marketplace revenue qualifies |
| API usage fees | Yes | Technology service |
| Consulting/professional services | **No** | §1202(e)(3) excluded |
| Staff augmentation | **No** | Professional services |
| Training/education services | **Maybe** | Depends on structure — if ancillary to software, may qualify |
| Hardware sales (bundled with software) | **Maybe** | Must be incidental to software business |
| Investment income (interest, dividends) | **No** | Not active business |
| Rental income | **No** | Unless substantial services provided |

**The 80% test**: At least 80% of assets (by value) must be used in qualified activities. Monitor the consulting revenue percentage — if Cure Consulting Group performs development work for its own portfolio companies, the payment structure matters:

- **Intercompany service agreement** at arm's length: The portfolio company's payment is an expense, not consulting revenue for QSBS purposes of the portfolio company
- **Revenue attribution**: If the portfolio company itself earns consulting revenue >20%, the active business test is at risk

## Holding Period: Key Dates

The holding clock (more than 5 years for stock issued on or before 2025-07-04; 3/4/5-year tiers at 50/75/100% for stock issued after) starts on the **date of issuance**, not the date of payment or the date of a SAFE.

| Event | Clock Start |
|-------|-------------|
| Cash purchase of stock | Date of issuance on stock certificate/cap table |
| SAFE conversion | Date the SAFE converts to stock (not date SAFE was signed) |
| Option exercise | Date of exercise (not date of grant) |
| Convertible note conversion | Date of conversion |
| Stock received for services | Date of issuance (subject to vesting — 83(b) election matters) |

**83(b) election**: If stock is subject to vesting, filing an 83(b) election within 30 days starts the QSBS clock at grant date. Without 83(b), the clock starts at each vesting date.

## State Tax Implications

QSBS federal exclusion under §1202 does not automatically apply at the state level:

| State | Conforms to §1202? | Notes |
|-------|-------------------|-------|
| Delaware | No state income tax on cap gains for non-residents | N/A for most |
| California | **Does NOT conform** | CA taxes QSBS gains fully |
| New York | **Partial** — conforms to federal | Check current year |
| Texas | No state income tax | N/A |
| Florida | No state income tax | N/A |
| Georgia | Conforms to federal | Check current year |

**Key takeaway**: California founders/shareholders do NOT get QSBS exclusion at the state level. This is a major planning consideration.
