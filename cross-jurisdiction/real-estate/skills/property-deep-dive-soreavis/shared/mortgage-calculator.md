# Mortgage Payment Calculator

Wired to live `--finance` rates per country. Computes monthly P&I payment, total interest paid, amortization schedule, and effective borrowing cost.

## Universal contract

For a given property + buyer profile, return:
1. **Monthly P&I payment** (principal + interest)
2. **Total interest paid over loan life**
3. **Amortization curve** (year-by-year remaining principal)
4. **Effective APR** (incl. mortgage origination fees)
5. **Affordability check** (DTI / DSTI compliance per country)
6. **Stress-test** (payment at +200 bps rate increase)

## Standard formula

```
Monthly Payment = P * (r * (1+r)^n) / ((1+r)^n - 1)

Where:
  P = principal (loan amount = purchase price - deposit)
  r = monthly interest rate (annual rate / 12)
  n = number of monthly payments (years × 12)
```

## Inputs

```yaml
# Input shape — one block per country
country: <ISO2>
purchase_price: <amount in local currency>
deposit_pct: <0.20 typical resident / 0.30+ non-resident>
loan_amount: <auto = purchase_price * (1 - deposit_pct)>
annual_rate_pct: <from --finance per country>
term_years: 25  # typical EU; 30 for US-style
mortgage_type: fixed | variable | tracker
fee_pct: 1.0  # origination fee
```

## Worked examples

### Example 1: France resident — €200k apartment in Paris

```yaml
# France
country: fr
purchase_price: 200000
deposit_pct: 0.20
loan_amount: 160000
annual_rate_pct: 3.5  # FR --finance Apr 2026
term_years: 25
```

- Monthly P&I: **€801**
- Total interest over 25 years: €80,300
- Effective APR (incl. 1% fee + assurance): ~3.7%
- DTI check (FR HCSF max 35%): household must earn min €2,288/mo net to qualify
- Stress-test at 5.5%: monthly P&I → €983 (+€182)

### Example 2: Spain non-resident — €300k Costa Brava

```yaml
# Spain
country: es
purchase_price: 300000
deposit_pct: 0.35  # ES non-resident typical
loan_amount: 195000
annual_rate_pct: 4.0  # ES --finance Apr 2026 (non-res spread)
term_years: 25
```

- Monthly P&I: **€1,029**
- Total interest: €113,700
- Effective APR ~4.2%
- DTI check (ES Bank of Spain): household must earn min €2,940/mo net
- Stress-test at 6%: monthly P&I → €1,256 (+€227)

### Example 3: UK expat — £400k London

```yaml
# United Kingdom
country: uk
purchase_price: 400000  # GBP
deposit_pct: 0.30  # UK non-res typical
loan_amount: 280000
annual_rate_pct: 5.0  # UK --finance Apr 2026 expat rate
term_years: 25
```

- Monthly P&I: **£1,635**
- Total interest: £210,500
- Effective APR ~5.3%
- Stress-test at 7%: monthly P&I → £1,978 (+£343)

### Example 4: Lithuania EU citizen — €180k Vilnius apartment

```yaml
# Lithuania
country: lt
purchase_price: 180000
deposit_pct: 0.15
loan_amount: 153000
annual_rate_pct: 4.0  # LT --finance Apr 2026
term_years: 25
```

- Monthly P&I: **€808**
- Total interest: €89,400
- Bank of Lithuania DSTI check (≤50% of net income): household must earn min €1,616/mo net
- Stress-test at 6%: monthly P&I → €984

## Affordability rules per country (cross-reference `--finance`)

| Country | DTI / DSTI cap | Stress-test required |
|---|---|---|
| FR | HCSF DTI ≤35% | yes (banks internal) |
| DE | Schufa-driven; banks ~40% PTI | yes |
| ES | BdE guidance ~35% | yes |
| PT | BdP ~40% | yes |
| IT | BdI ~33% | yes |
| UK | FCA Mortgage Market Review | yes (+3% above SVR) |
| NL | DNB LTI 4-5x | yes |
| BE | banks ~33% | yes |
| LU | banks ~40% | yes |
| IE | CBI LTI 4x FTB / 3.5x sub | yes (+2% stress) |
| SE | Riksbank: amortisation 2%/yr if LTV>50%, 3%/yr >70% | yes |
| NO | Boligforskriften: DTI ≤5x, stress-test +3 ppts | yes |
| LT | Bank of Lithuania DSTI ≤50% | yes |
| LV | banks ~40% | yes |
| EE | banks ~40% | yes |
| CZ | CNB DSTI ~45% | yes |
| SK | NBS DSTI ≤60%, DTI ≤8x | yes |
| PL | KNF Rekomendacja S | yes |
| HU | MNB JTM ~50% | yes |
| RO | BNR ~40% | yes |
| CH | Tragbarkeit ≤33% imputed at 5% theoretical | yes (5% theoretical rate) |

## Amortization curve sketch

For a 25-year fixed-rate mortgage at 3.5%, principal repaid by year:

| Year | Principal repaid | Interest paid | % of P&I to interest |
|---|---:|---:|---:|
| 1 | 4.5% | 95.5% | 88% |
| 5 | 18% | 82% | 80% |
| 10 | 38% | 62% | 70% |
| 15 | 55% | 45% | 56% |
| 20 | 78% | 22% | 31% |
| 25 | 100% | 0% | 0% |

Longer the term, more is paid in interest (US 30-yr fixed at 6% can exceed 100% of principal in interest paid).

## Stress-test pattern

For each mortgage, run at **base rate + 200 bps**:

```
base_payment = compute(rate=current)
stress_payment = compute(rate=current+0.02)
delta = stress_payment - base_payment
delta_pct = delta / base_payment

if delta_pct > 25%: 🟠 elevated rate-shock risk
if delta_pct > 35%: 🔴 severe — consider longer fixed-period
```

## Cross-section with `--finance`

The calculator pulls from the country playbook's `--finance` section:
- Current 10-yr fixed rate (lender / broker)
- Non-resident LTV cap
- Affordability rule

Cross-reference the per-country playbook before quoting a number.

## Anti-hallucination

- **Don't fabricate rates** — use `--finance` per-country which has source-cited Apr 2026 ranges
- **Show stress-test always** — a single number underestimates risk
- **Affordability rules differ** — be careful applying FR HCSF logic to DE PTI etc.
- **Currency mismatch** — if buyer earns USD/EUR but mortgage is HUF/PLN/RON, surface FX risk explicitly (and note PL CHF ban + HU 2014 conversion)
- **Origination fees** vary 0.5-2% — include in effective APR computation

## Status

Last refreshed: 2026-04-26.
