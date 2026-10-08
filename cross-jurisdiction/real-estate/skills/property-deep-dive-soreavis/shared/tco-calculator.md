# TCO Calculator — 30-Year Total Cost of Ownership

Bridges `--tax`, `--finance`, `--insurance`, `--notary`, and `--mains` into one usable number. Computes the 30-year total carrying cost of owning a property, in the local currency.

## Universal contract

For a given property + buyer profile, return:
1. **Initial outlay** (purchase price + closing costs + setup costs)
2. **Year-by-year operating cost** (mortgage P&I + property tax + insurance + maintenance + utilities + management fees)
3. **30-year cumulative outlay** (nominal)
4. **30-year cumulative outlay** (real, inflation-adjusted to today's currency)
5. **Imputed sale value at exit** (asking - capex - CGT - notary - agent commission)
6. **Net cost of ownership** = (Year 30 outlay) - (sale proceeds)

## Inputs

```yaml
# Input shape — one block per country
country: <ISO2>
purchase_price: <amount in local currency>
ownership_type: primary_residence | rental_investment | second_home
buyer_residency: resident | non_resident_eu | non_resident_non_eu
deposit_pct: <0.20 typical for resident, 0.30+ for non-resident>
mortgage_term_years: 25  # standard
mortgage_rate_fixed_pct: <from --finance>  # e.g., 3.5
mortgage_type: fixed | variable | tracker
local_inflation_rate_pct: <from --macro>  # e.g., 2.5
expected_property_appreciation_pct_yoy: <from --price trajectory>  # e.g., 2.0
hold_period_years: 30  # default for "buy & hold" analysis
```

## Cost components

### A. Initial outlay (year 0)

```
purchase_price
+ transfer_tax (% from per-country playbook)
+ notary_fee (% from per-country playbook)
+ registration_fee (% from per-country playbook)
+ property_inspection / diagnostics (€500-2,000)
+ mortgage_setup_costs (1-3% of loan)
+ furniture / immediate_capex (estimate: 2-5% of price)
= TOTAL_INITIAL
```

### B. Annual operating costs (years 1-30)

```
mortgage_P&I (computed from rate, term, principal)
+ property_tax (annual, from per-country playbook §tax)
+ home_insurance — building + contents (annual, from --insurance; ~0.15-0.30% of rebuild value for standard
   peril; non-standard perils — flood / cyclone / earthquake / subsidence — may add 30-200% via national pool
   surcharge OR fail underwriting entirely on cliff-risk addresses; cross-link to --insurance § Insurability
   cliff + --climate hazard layer; non-owner-occupied uplift if rented out; see shared/scams-postcompletion.md
   for absentee-owner policy-void traps)
+ maintenance_capex (1-2% of property value/year, real)
+ utility_costs (heating, electric, water — varies wildly by country)
+ HOA_fees / condominium_dues / strata_levies (where applicable, ~1-3% of price/year for apartments)
   ⚠️ Reserve-fund-health flag — pull the sinking-fund / capital-reserve balance + the last 3 years of
   special-levy history from the AGM minutes BEFORE offer (jurisdiction-specific reserve regimes: AU-NSW
   capital-works fund + mandatory 10-year plan, US FL SIRS every 10y, ON every 3y, BC every 5y, FR fonds de
   travaux + DTG buildings >15y, IT fondo speciale per-works — see shared/property-management.md and
   shared/property-types.md § Apartment-vs-house reserve fund). Under-funded reserve → expect special-levy
   shock of 10-100% of one year's dues within 5 years; surfaces as an unbudgeted line that breaks the TCO.
+ country_specific_recurring (see § B.1 — e.g. MX fideicomiso annual fee in Restricted Zone, HK government
   rent, GB ground rent, AE service charge, JP 修繕積立金, SG MCST sinking fund, FR THRS second-home tax)
+ rental_management_fees (if rental investment, 8-15% of gross rent)
+ rental_income_tax (if rental, see per-country --tax)
- rental_income (if rental, see per-country --rental)
= ANNUAL_NET_CASH_FLOW
```

### B.1 Country-specific recurring lines (foreign-buyer trap registry)

Recurring TCO lines that don't fit the universal `property_tax + insurance + HOA` shape and routinely
break a foreign buyer's 30-year model when missed at offer. Pull figures from the country playbook, not
from this table — these are pointers, not authoritative rates. All figures `est.` order-of-magnitude.

| Country / scope | Line | Typical band | Trigger | Cross-ref |
|---|---|---|---|---|
| **MX** Restricted Zone (50 km coast / 100 km border) | **Fideicomiso annual fee** | USD 350-1,000 / year | Constitutional Art. 27 — foreign ownership in Restricted Zone is held via a bank trust; ~50-year renewable term; one-off setup USD 2,000-3,000 | `countries/mx/playbook.md` § Foreign-buyer fideicomiso |
| **GB (E&W)** pre-2022 leasehold flats | **Ground rent** | £0-500 / year (peppercorn on post-30 Jun 2022 long leases per LRGRA 2022) — pre-2022 doubling / RPI clauses can spiral | Lease clause; LFRA 2024 marriage-value abolition **NOT commenced as of May 2026** — do not assume it is gone | `shared/property-types.md` § GB (England & Wales) leasehold |
| **HK** | **Government rent** | 3% of rateable value / year | Most post-1985 / extended Government leases; Cap. 648 Extension Ordinance in force 5 Jul 2024 carries the same 3% on extension | `shared/property-types.md` § HK |
| **SG** | **MCST management + sinking fund** | SGD 250-800 / month typical condo | Building Maintenance and Strata Management Act — mandatory MCST levy split between operating and sinking fund | `shared/property-types.md` § SG |
| **AE Dubai / Abu Dhabi** | **Service charge** | AED 8-30 per sq ft / year (Dubai DLD Service Charge Index published annually) | Master-developer / community service charges + cooling DEWA-district + chiller; volatility on handover years | `shared/property-types.md` § AE |
| **JP** | **Kanrihi 管理費 + Shuzenseki tsumitatekin 修繕積立金** | ¥15,000-40,000 / month combined (apartment) | Management fee + long-term-repair sinking-fund contribution; *tsumitatekin* re-priced upward on the 30-yr 大規模修繕 cycle — model the ramp, not the year-1 figure | `countries/jp/playbook.md` |
| **CH** | **Eigenmietwert** (imputed rental income tax) | Variable — assessed % of imputed rent added to taxable income | Federal popular vote of 28 Sept 2025 ABOLISHED Eigenmietwert effective **1 Jan 2029** — model both pre- and post-2029 scenarios | `shared/home-tax.md` § CH |
| **FR** second homes | **Taxe d'habitation sur les résidences secondaires (THRS)** | €500-3,000 / year (commune-set; major-city surcharge up to 60%) | THRS retained for second homes (general THR abolished 2023); 1,461 communes can levy a 5-60% **majoration** under CGI Art. 1407 ter; surcharge **applied by default in zones tendues** (zones tendues décret list — verify per commune) | `countries/fr/playbook.md` § tax |
| **IT** | **TARI** (waste tax) + **TASI residual** | €150-500 / year typical apartment | Comune-set on m² + occupants; primary residence often exempt from IMU but TARI applies regardless | `countries/it/playbook.md` § tax |
| **ES** | **IBI catastral revaluation shock** | 10-30% jump on revaluation year | IBI based on *valor catastral*; revaluations can lag a decade then jump in one cycle — surprise post-completion line | `countries/es/playbook.md` § tax |
| **US** CA / FL / LA | **Insurance non-renewal premium** | 50-300% above national average, OR market-of-last-resort (FAIR Plan / Citizens) | Climate-driven carrier withdrawal; CA FAIR Plan + FL Citizens + LA Citizens are state-backed last-resort pools — explicit cost-band uplift, not implicit | `shared/insurance.md` § Insurability cliff |
| **AU** any apartment | **Special levy on capital-works shortfall** | AUD 5,000-100,000+ lump-sum | Sch 1 SSMA 2015 — owners-corp can pass a special levy by ordinary resolution; binds all lots; flammable-cladding rectification + concrete-cancer + waterproofing are recurring drivers | `shared/property-management.md` § AU-NSW |
| **PH / TH / ID** apartment / villa | **Common-area dues + sinking fund** | Variable | Condominium Act (PH) / juristic-person fee (TH) / IPL (ID) — verify rate and reserve-balance at AGM minutes; lower transparency than CH/AU/SG strata regimes | per-country playbook |

These lines are **separate from the universal schema** — model each as its own row in the 30-year cash-flow
table, not folded into `HOA_fees`. The MX fideicomiso and CH Eigenmietwert are the highest-impact recurring
lines specific to foreign-buyer / non-foreign-buyer asymmetry: each can shift the TCO by 5-15% over 30 years.

### C. Sale costs at year N

```
gross_sale_value (= purchase_price * (1 + appreciation_yoy)^N)
- capital_gains_tax (per-country playbook §tax — primary residence often exempt; rental almost never)
- agent_commission (from --exit, typically 3-7% in EU, 5-6% in US/CA)
- notary_seller_fees (from --notary)
- pre-sale capex (refresh costs ~1-2% of sale value)
= NET_SALE_PROCEEDS
```

### D. Net cost of ownership (Year 30)

```
TOTAL_INITIAL + Σ(ANNUAL_NET_CASH_FLOW for 30 years) - NET_SALE_PROCEEDS = NET_TCO
```

Adjust to real terms using local inflation.

## Move budget — the one-time relocation cash event (separate from the 30-year TCO)

The 30-year TCO above is the *ownership* cost. A relocating foreign buyer also faces a **one-time relocation cash event** at the move itself that buyers systematically under-budget — and it is NOT part of the carry, so show it as a separate lump sum, never amortised into the annual figure. Most of these lines are already sourced elsewhere in the skill; this block **composes** them. Per § Anti-hallucination below, present it as a **3-scenario band (lean / central / heavy)**, never a single number.

```
MOVE_BUDGET (one-time, at relocation) =
    closing_costs            (from § A — sourced, per-country)
  + visa_blocked_deposit     (LIQUIDITY LOCK, not a sunk cost — see ⚠️)
  + tor_customs_exposure     (duty + VAT only on NON-qualifying goods)
  + international_shipping    (est. band — 3 quotes)
  + pet_relocation           (est. band)
  + vehicle_delta            (sell-at-origin vs ship-and-comply)
  + onboarding_friction      (deposits + healthcare gap + DL re-test + tax-ID fees)
  + runway                   (user_months × buyer's own monthly burn)
```

| Line | Band (est. unless sourced) | Sourced home / note |
|---|---|---|
| **Closing costs** | per-country, **sourced** (transfer tax + notary + agent + registration) | `§ A. Initial outlay` — *not* an estimate; pull the real per-country figure |
| **Visa blocked-deposit / proof-of-funds** | DE *Sperrkonto* **€11,904/yr** (2026); per-country statute | `shared/finance-banking.md` § Visa-linked blocked-deposit. ⚠️ a *blocked* deposit is a **liquidity lock released back to you monthly**, not money spent — budget it committed-not-available, not as a cost |
| **ToR customs exposure** | **€0 if you qualify**; else standard duty + import VAT/GST on the non-qualifying portion | `shared/relocation-household-customs.md` — file the named form (ToR1 / CBP 3299 / B534…) BEFORE shipping; verify the commodity code |
| **International shipping** | est. **~US$2,500–19,000** (20-ft → 40-ft container, route-dependent) | est. only — get **3 FIDI/IAM-accredited quotes**; not a primary figure |
| **Pet relocation** | est. **€500–6,000 per pet** (higher on AU/NZ/JP FAVN-titer routes) | `shared/relocation.md` § Pets — quarantine FEES at mpi.govt.nz / DAFF |
| **Vehicle delta** | est. **€2k–25k** (compliance + shipping, or the sell-at-origin / rebuy-at-destination loss) | `shared/relocation.md` § Vehicle import — often cheaper to sell and rebuy |
| **Onboarding friction** | est. **€1k–3k** baseline (utility deposits €300–800 + healthcare-gap insurance €500–1,500 + DL re-test €100–2,000 + tax-ID consulate fees €10–100) | `shared/relocation.md` mitigation #7 |
| **Runway** | **user_months × monthly burn** — the buffer until income / rental income starts | set by the user; wire to the cost-of-living basket if/when that ships |

**Illustrative band** (single adult, intra-EU → EU, furnished move, qualifying ToR, 3-month runway): lean ~€6k (sell-most, small shipment, no pet/car) · central ~€18k · heavy ~€45k+ (full 40-ft container + pet + shipped car + 6-month runway). **The lever that moves it most is sold-vs-shipped** — more shipped = higher freight + more ToR paperwork; more sold = higher rebuy cost at destination. Always run the user's own sold-vs-shipped split rather than a default.

⚠️ **Do not fold the blocked deposit into the "money gone" total** — it is returned to the mover in monthly tranches after arrival (a cash-flow lock, not a sunk cost); show it on its own line. Every line except closing costs is an **estimate band** — never a point figure (per § Anti-hallucination).

## Worked example: rural Adriers, FR — €145,000 listing

```yaml
# France
country: fr
purchase_price: 145000
ownership_type: primary_residence
buyer_residency: resident
deposit_pct: 0.20
mortgage_term_years: 25
mortgage_rate_fixed_pct: 3.5  # from --finance
local_inflation_rate_pct: 2.0  # from --macro
expected_property_appreciation_pct_yoy: 1.5  # rural FR conservative
hold_period_years: 30
```

**Year 0 initial outlay**:
- Purchase: €145,000
- Frais de notaire (~7-8% existing): €11,000
- Furniture + immediate capex: €5,000
- Mortgage setup: ~€1,500
- = **€162,500 initial**

**Annual operating** (year 1):
- Mortgage P&I (€116k loan, 3.5% fixed, 25y): ~€7,000/yr
- Taxe foncière (Adriers commune-typical): ~€500/yr
- Assurance habitation — building + contents incl. Catnat surcharge 12 → 20% on 1 Jan 2025 (verify primary arrêté): ~€450/yr
- Maintenance (1.5% of price): ~€2,200/yr
- Utilities (rural, oil/wood heating): ~€1,800/yr
- THRS (second-home — N/A for primary residence; would add €0-1,500/yr if second home in a zone tendue commune)
- = **~€11,950/yr** (primary residence)

**Year 30 cumulative (nominal)**:
- Initial: €162,500
- 25 yrs mortgage: €175,000 (P&I)
- 5 yrs no-mortgage: €0 P&I
- 30 yrs taxe foncière + insurance + maintenance + utilities: ~€155,000 (with 2% inflation)
- = **~€492,500 cumulative outlay**

**Year 30 sale**:
- Property at 1.5%/yr: €145k * 1.015^30 ≈ €227,000
- CGT exempt (primary residence)
- Notary seller: 0% (buyer pays)
- Agent commission ~5% (FR FNAIM): -€11,400
- = **Net sale: €215,600**

**Net TCO**:
- €492,500 - €215,600 = **€276,900 net 30-yr cost**
- Inflation-adjusted (real €): ~€176,000 in today's purchasing power

**Implication**: 30-yr "cost of housing yourself" in this Adriers property = ~€176k real (vs ~€500/mo rent equivalent for 30 yrs = ~€180k). Roughly break-even rent vs buy at this scale, with appreciation upside if FR rural prices recover.

## Comparison output

The TCO calculator can be combined with `--compare` to show TCO across countries for the same nominal property value:

```
/property-deep-dive --compare=fr,it,es,pt,gr --tco --price=200000 --hold=30
```

→ Outputs a 5-country TCO comparison table.

## Confidence + sensitivity

The calculator output is sensitive to:
1. **Mortgage rate** (±0.5% changes 30-yr P&I by ~10-15%)
2. **Inflation rate** (real vs nominal divergence)
3. **Appreciation rate** (most volatile — back-test against `--price` history)
4. **Maintenance assumption** (1-2% range — older buildings need more)
5. **CGT regime** (varies — check primary-residence exemptions)

Always run a sensitivity table on rate + appreciation + maintenance.

## Anti-hallucination

- **Don't quote a single TCO number** — always show 3 scenarios (pessimistic / central / optimistic)
- **Pull rates from `--finance` per-country**, not generic
- **Pull tax/CGT from per-country `--tax` section** — don't extrapolate
- **Surface what the user can't predict** (rate path, inflation path, appreciation path) and let them set the dial
- **Real vs nominal**: always show both; many users only think in nominal and underestimate

## Implementation notes

This is a calculator pattern — the values come from per-country playbooks. The skill should:
1. Pull `--tax`, `--finance`, `--insurance`, `--notary` from the country playbook
2. Default unknown maintenance / utilities to country averages
3. Allow overrides via flags (`--rate=3.0`, `--appreciation=1.5`)
4. Output both nominal + real
5. Show sensitivity table

## Status

Last refreshed: 2026-05-26.
