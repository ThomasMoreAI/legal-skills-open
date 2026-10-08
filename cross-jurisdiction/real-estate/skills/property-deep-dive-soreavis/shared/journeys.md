# Buyer Journey Templates — `--journey=<type>`

Workflow templates that convert raw findings into decision-ready outputs. Each journey assumes the standard 9 sections (or 10 with `--climate`) have been run; the journey re-shapes the output for a specific decision context.

## Available journeys

| Journey | Use when | Output focus |
|---|---|---|
| `pre-offer` | Before submitting an offer | Walkaway price, top 3 risks, hidden costs, counter-offer logic |
| `post-offer` | After offer accepted, before closing | Notary checklist, surveys, conditions to add, timeline |
| `foreign-buyer` | Non-resident purchase | Visa/golden visa, FX, mortgage caps, tax implications, succession |
| `investor` | BTL or capital-gains play | Yield, BTL math, tax-optimized structure, exit scenarios |
| `renovation` | Property needs work | Cost benchmarks → scope, EPC pathway, grant eligibility |
| `gite-bnb` | Short-let business | Saturation, year-1/2/3 net, Atout France/CIN/AL classification |
| `inheritance` | Estate planning / family transfer | CGT/IHT/CAT scenarios, forced heirship, structures |

Combine with country playbook output: `/property-deep-dive <addr> --all --journey=pre-offer`.

---

## 1. Pre-offer journey

**Goal**: convert section findings into a "make offer at €X with these conditions" decision.

### Output template

```markdown
## Pre-Offer Decision Brief

**Listing price**: €<L>
**Market context**: €<M> commune avg/m² × <m²> = €<M_total> reference
**Walkaway price (calculated)**: €<W>

### The math
- Reference value (commune avg): €<M_total>
- Adjustments:
  - DPE/EPC drag: -€<X> (Class E/F → renovation needed)
  - Renovation envelope: -€<Y>
  - Risk discount (if any): -€<Z>
  - Premium (if any): +€<P>
- **Walkaway**: €<M_total - X - Y - Z + P>
- **Recommended opening offer**: €<W × 0.92 to W × 0.95>

### Top 3 risks
1. 🔴/🟠/🟡 <name> — <impact in €>
2. 🔴/🟠/🟡 <name> — <impact in €>
3. 🔴/🟠/🟡 <name> — <impact in €>

### Hidden costs ledger
| Item | One-time | Annual |
|---|---:|---:|
| Notary / notaire / Notar | €<X> | — |
| Transfer tax (SDLT/registratie/foros etc.) | €<X> | — |
| Inspection / survey | €<X> | — |
| Property tax (IBI/taxe foncière/Grundsteuer/etc.) | — | €<X> |
| Insurance (basic + nat-haz) | — | €<X> |
| Energy (current EPC class) | — | €<X> |
| Mains drains compliance (if rural) | €<X> | — |
| Pyrite/mica/asbestos (if applicable) | €<X> | — |
| **Total Year-1 cash needed** | **€<sum>** | — |

### Conditions to add to offer

- [ ] Subject to satisfactory survey (Level 3 / amiante / DPE)
- [ ] Subject to mortgage approval (clause suspensive in FR)
- [ ] Subject to clean title (no encumbrances on KW/Folio)
- [ ] Possession date: <date>
- [ ] Inclusions: <fittings, white goods, garden equipment>
- [ ] If short-let: subject to license eligibility (CIN/AMA/AL)

### Negotiation levers
- <Specific finding>: ask for €<X> off
- <Specific finding>: ask for credit at closing
- <Specific finding>: ask seller to remediate before completion

### Confidence to proceed
- 🟢 GO — risks understood, walkaway clear, financing path clear
- 🟡 PROBE — need 1-2 verifications first (call mairie, get inspection quote)
- 🔴 PASS — fundamental issue (title, structural, regulatory)
```

---

## 2. Post-offer journey

**Goal**: between accepted offer and closing, ensure nothing slips through.

### Output template

```markdown
## Post-Offer Closing Plan

**Offer accepted**: <date>
**Target completion**: <date>
**Days to closing**: <N>

### Immediate (next 7 days)
- [ ] Hire notary / solicitor (if not already)
- [ ] Order surveys: <list>
- [ ] Request title/cadastre extract (KW/Folio/Tinglysning)
- [ ] Mortgage application submission
- [ ] Insurance quotes (must be in place at completion)

### Surveys to commission

| Survey | Country specifics | Cost | Time |
|---|---|---:|---|
| Structural (Level 3 / Bauholz / Tilstandsrapport) | <per-country> | €<X> | <days> |
| Asbestos diagnostic | required pre-1996/97 builds | €<X> | <days> |
| Pyrite/mica (IE Mayo/Donegal) | DCBS-eligible? | €<X> | <days> |
| Termite / wood-boring insects | per-country mandatory at sale | €<X> | <days> |
| Lead paint | pre-1949 builds | €<X> | <days> |
| Septic compliance (rural) | mandatory in many EU | €<X> | <days> |
| Radon test | high-radon zones | €<X> | <days> |
| Energy (EPC/DPE/Energimerke) | mandatory | €<X> | <days> |

### Notary appointment checklist

- [ ] Funds confirmed (bank cheque / wire transfer logistics)
- [ ] Compromis/Vorvertrag/contract reviewed
- [ ] Suspensive conditions verified (financing, cancellation)
- [ ] All disclosed easements understood
- [ ] Final walk-through scheduled (24-48h before)
- [ ] Identity documents (passport + proof of address)
- [ ] Tax IDs (NIE/SteuerID/Codice Fiscale/etc.)
- [ ] Power of attorney if remote

### Final walk-through
- [ ] Verify property condition unchanged
- [ ] Verify inclusions present (fittings, appliances, garden equipment)
- [ ] Verify no new damage
- [ ] Photo + video record

### Day of completion
- [ ] Funds transfer confirmed
- [ ] Keys handover
- [ ] Meter readings (electricity, gas, water)
- [ ] Insurance policy active
- [ ] Mail forwarding set up

### Post-completion (first 30 days)
- [ ] Register title at cadastre/Land Registry (typically notary handles)
- [ ] Set up utilities under your name
- [ ] Property tax registration (LPT/IBI/taxe foncière/etc.)
- [ ] Update voter registration if applicable
- [ ] Local resident card / ID (FR carte vitale, ES NIE update)
```

---

## 3. Foreign-buyer journey

**Goal**: surface the cross-border friction that resident-targeted advice misses.

### Output template

```markdown
## Foreign-Buyer Brief

**Buyer's residence**: <country>
**Property location**: <country>
**Currency exposure**: <home currency> ↔ <local currency>

### Visa / residency implications

- **Golden Visa eligibility** (if applicable): <thresholds, e.g., GR €800k/€400k tiers, PT abolished 2023, ES €500k>
- **Investor / non-lucrative visa** alternatives: <country-specific>
- **Tax residence triggers** (183-day rule, center of vital interests): when does buying create tax residence?
- **Spousal visa coordination**: dependents

### Currency + financing

- **FX hedge** strategy: forward, options, multi-currency mortgage
- **Local mortgage cap** for non-residents: typically 60-70% LTV (vs 80-90% for residents)
- **Cross-border mortgage** providers (HSBC International, BNP Paribas International, etc.)
- **Mortgage interest deductibility** — usually NOT deductible against home-country income
- **Repatriating rental income** — withholding tax, double-tax treaty (DTT) coverage
- **Conversion costs**: spread on conversion at notary (often 1-2%)

### Tax implications

| Tax | Rate (non-resident) | Notes |
|---|---:|---|
| Annual property tax | <per-country> | Often higher rate for non-residents |
| Imputed rental income | <e.g., ES IRNR 2% × cadastral value × 24%> | EU vs non-EU rates differ |
| Capital gains | <per-country> | Higher rate for non-residents (e.g., ES 19% non-EU vs 19% EU) |
| Wealth tax (where applicable) | <e.g., ES IP, FR IFI> | Generally non-residents only on local assets |
| Inheritance / gift tax | <per-country> | Often more punitive on non-resident heirs |
| Withholding on rental | <per-country> | DTT may reduce |

### Forced heirship + succession

- **Forced heirship** countries: FR, IT, ES, CH (cantonal), parts of LU
- **Children's reserved share** (réserve héréditaire FR, legítima ES): often 50-75%
- **EU Succession Regulation (Brussels IV)**: lets you elect law of nationality — important for non-EU citizens
- **Cross-border probate** complications: dual probate, sworn translations, apostille
- **Local will** + home-country will coordination
- **Trust / holding co structures**: often disregarded by EU civil-law jurisdictions

### Practical operations

- **Power of attorney** (POA): notarized + apostilled if not local
- **Local bank account**: often required to settle (some countries can do via international account)
- **Tax identification**: NIE (ES), Codice Fiscale (IT), Steuer-ID (DE), N° fiscal (FR), TIN (IE), etc.
- **Property management**: local agency for rentals, maintenance, tax filings
- **Translator / lawyer**: at notary appointment if no local language

### Red flags for foreign buyers

- 🔴 Aggressive sales pitch from developers in tourist areas
- 🔴 "Safe deposit" scams — money to seller before legal due diligence complete
- 🔴 Off-plan with weak guarantees / low-equity developer
- 🔴 Properties listed in foreign currency at unfavorable rate
- 🔴 Pressure to skip independent legal counsel
- 🔴 Cash-only / unusually low listed price (money-laundering red flag)
```

---

## 4. Investor journey

**Goal**: BTL math, tax-optimized structure, exit scenarios.

### Output template

```markdown
## Investor Analysis

**Acquisition price**: €<P>
**All-in purchase costs**: €<P × 1.06–1.15>
**Annual gross rental potential**: €<R> (long-term) or €<R_short> (short-let)
**Country regime**: <regulated rent / free market>

### Yield calculations

| Metric | Long-term | Short-let |
|---|---:|---:|
| Gross yield | <R/P × 100>% | <R_short/P × 100>% |
| Operating expenses | -<X>% (mgmt, repairs, vacancy, insurance) | -<Y>% (incl. cleaning, platform fees) |
| Net yield (pre-tax) | <X>% | <Y>% |
| Net yield (post-tax) | <X>% | <Y>% |
| Cap rate | <NOI/P>% | — |

### BTL math (if mortgage)

- Mortgage: €<M> @ <rate>% / <years>
- Monthly payment: €<X>
- Net cash flow: €<R/12 - mortgage - opex>/mo
- DSCR (Debt Service Coverage Ratio): <NOI / debt service>
- Break-even occupancy: <X>%

### Tax-optimized structure

| Structure | Pros | Cons | Best for |
|---|---|---|---|
| **Sole proprietor** | Simple, low setup cost | Personal liability, marginal tax | Single property, owner-occupier-adjacent |
| **Local LLC** (SARL/Sp z o.o./SRL/etc.) | Liability shield, deductibility | Setup cost, accounting overhead | 2+ properties, BTL portfolio |
| **Holding co** | Multiple-property pooling, tax optimization | Cross-border complexity | International investors |
| **REIT-equivalent** | Professional management, liquidity | Surrender control, fees | Passive investors |

### Country-specific reliefs

- 🇫🇷 **LMNP / LMP** (location meublée non-professionnelle): 50% abatement (micro-BIC) or real expenses (réel) + amortization
- 🇮🇹 **Cedolare secca** 21% (long-term) / 26% (short-let)
- 🇪🇸 **Reducción 60%** for long-term residential rental
- 🇩🇪 **AfA** (Absetzung für Abnutzung): 2-3% depreciation
- 🇬🇧 **Buy-to-let** mortgage interest restricted to 20% basic-rate credit
- 🇮🇪 **FHL abolished April 2025** — short-let now standard property income
- 🇵🇱 **Ryczałt 8.5%/12.5%** flat-rate
- 🇸🇪 **Schablonavdrag** (template deduction) on private rental
- 🇵🇹 **NHR retired 2024** — successor regime IFICI for innovation/research

### Exit scenarios

| Hold | Net yield p.a. | Capital appreciation | Total return |
|---|---:|---:|---:|
| 5 yrs | <X>% | <Y>% | <Z>% |
| 10 yrs | <X>% | <Y>% | <Z>% |
| 20 yrs | <X>% | <Y>% | <Z>% |

### Sensitivity

- +2pp interest rate → DSCR drops to <X>
- Vacancy 6 mo → annual cash flow -€<Y>
- Rent index +CPI: <X>% per year (compounding)
- 10% price drop on exit: total return -<Y>%

### Verdict
- 🟢 **Buy** — yield, fundamentals, growth aligned
- 🟡 **Wait** — yield thin, but macro trend favorable
- 🟠 **Negotiate** — need 5-10% discount to make math work
- 🔴 **Pass** — yield insufficient or risk profile wrong
```

---

## 5. Renovation builder

**Goal**: convert findings into a quote-ready scope + EPC pathway.

### Output template

```markdown
## Renovation Plan

**Property condition**: <"Good" / "Renovation needed" / "Major work">
**Current EPC/DPE**: <class>
**Target class** (resale or rental): <class>

### Scope by priority

#### Priority 1: Health & safety
- [ ] Asbestos abatement: €<X>
- [ ] Lead paint encapsulation: €<X>
- [ ] Electrical re-wire (pre-1980 builds): €<X>
- [ ] Mains drains compliance (if rural): €<X>
- [ ] Radon mitigation (if high-zone): €<X>
- [ ] Structural / foundation: €<X>

#### Priority 2: Building envelope
- [ ] Roof: €<X>
- [ ] Walls insulation (ITE/internal): €<X>
- [ ] Windows (double/triple-glaze): €<X>
- [ ] Doors: €<X>

#### Priority 3: Systems
- [ ] Heating system (heat pump? solar?): €<X>
- [ ] Hot water: €<X>
- [ ] Ventilation (MVHR for tightly-sealed): €<X>
- [ ] Plumbing: €<X>

#### Priority 4: Finishes
- [ ] Kitchen: €<X>
- [ ] Bathrooms: €<X>
- [ ] Floors: €<X>
- [ ] Walls / paint: €<X>

### EPC pathway

| Step | Action | EPC change | Cost | Cumul |
|---|---|---|---:|---:|
| 1 | Loft insulation | E → D | €<X> | €<X> |
| 2 | Cavity wall | D → C | €<X> | €<X+X> |
| 3 | Heat pump | C → B | €<X> | €<sum> |
| 4 | Solar PV + windows | B → A | €<X> | €<sum> |

### Country-specific grants (2025-2026)

- 🇫🇷 **MaPrimeRénov'**: up to €70k for full renovation
- 🇩🇪 **BAFA + KfW**: 40% subsidy on heat pumps + 70% on EE-loans
- 🇪🇸 **PREE / Bono Reto Demográfico**: regional grants
- 🇮🇹 **Ecobonus / Superbonus** (reduced 65-90% from 2024-2026)
- 🇸🇪 **Skattereduktion ROT/RUT** (rotavdrag): 30% on labour
- 🇫🇮 **ARA / Energy renovation grant**: up to €15k
- 🇳🇴 **Enova**: heat pump, insulation, PV grants
- 🇮🇪 **SEAI Better Energy Homes** + Better Energy Warmer Homes
- 🇬🇧 **Boiler Upgrade Scheme**: £7,500 for heat pumps
- 🇵🇱 **Czyste Powietrze** (post-31 Mar 2025: heat pumps + PV only)
- 🇵🇹 **Edifícios Mais Sustentáveis**

### Payback analysis

| Action | Cost | Energy savings/yr | Payback |
|---|---:|---:|---:|
| Insulation | €<X> | €<Y> | <Z>yrs |
| Heat pump | €<X> | €<Y> | <Z>yrs |
| Solar PV | €<X> | €<Y> | <Z>yrs |

### DIY vs contractor mix
- DIY: <list — paint, basic tile, simple plumbing>
- Contractor: <structural, electrical, gas, certified energy retrofit>
- **Caveat**: many countries require certified installer for grant eligibility

### Total investment + ROI

- Total budget: €<X>
- Expected EPC class post-work: <class>
- Resale value uplift estimate: €<Y>
- Payback (energy + value): <Z> years
- Annual rent increase potential: €<W>
```

---

## 6. Gîte / B&B business plan

**Goal**: realistic year-1/2/3 net based on area saturation + regulatory regime.

### Output template

```markdown
## Short-Let Business Plan

**Property**: <address>
**Configuration**: <whole house / 1 unit / 2 units / B&B 3 rooms>
**Sleep capacity**: <N people>
**Country regime**: <CIN/AL/AMA/Heimagisting/etc.>

### Saturation analysis

- **Existing units in commune**: <N>
- **Population**: <P>
- **Units per 100 inhabitants**: <ratio>
- **Verdict**: <oversaturated / saturated / room to grow>

### Realistic occupancy (Year 1, 2, 3)

| Metric | Year 1 | Year 2 | Year 3 |
|---|---:|---:|---:|
| Occupancy rate | 25-35% | 35-45% | 45-55% |
| Avg nightly rate | €<X> | €<X+Y> | €<X+Z> |
| Gross income | €<a> | €<b> | €<c> |
| Operating costs | -€<a*0.4> | -€<b*0.35> | -€<c*0.3> |
| **Net before tax** | **€<a*0.6>** | **€<b*0.65>** | **€<c*0.7>** |
| Tax (TMI 30% + URSSAF) | -€<X> | -€<Y> | -€<Z> |
| **Net after tax** | **€<X>** | **€<Y>** | **€<Z>** |

### Regulatory: classification + licensing

| Country | Optimal classification | Why |
|---|---|---|
| 🇫🇷 | **Atout France classement (1-5★)** | 50% abatement + 6% URSSAF (vs 30% + 21%) |
| 🇮🇹 | CIN registration + cedolare secca 21% | Mandatory Jan 2025 |
| 🇪🇸 | Vivienda turística (regional) | Per-CCAA different |
| 🇵🇹 | AL registration | Lisbon suspension still active |
| 🇬🇷 | AMA + primary-use status | Athens + Cyclades restrictions |
| 🇩🇪 | Per-Kommune | Berlin/München strict |
| 🇮🇪 | Failte Ireland register | RPZ rules |

### Operating cost structure

- **Cleaning**: €<X> per turnover (or % of nightly)
- **Linens / consumables**: €<X>/yr
- **Utilities** (vacant + occupied avg): €<X>/yr
- **Insurance** (commercial use): €<X>/yr
- **Platform fees** (Airbnb 3-15% / Booking 15-20%): €<X>/yr
- **Property management** (if outsourced): 15-25% of gross
- **Maintenance reserve**: 5-10% of gross
- **Marketing (own website, listing photography)**: €<X>/yr
- **Local taxe de séjour / tourist tax**: collected from guest, paid to commune

### Marketing channels

- **Direct booking site** (own website, beds24/lodgify): saves platform fees
- **Airbnb + Booking + Vrbo**: reach + reviews
- **Local tourist board** (e.g., FR Gîtes de France): credibility + bookings
- **Partner with regional experiences** (wine tours, cooking classes)

### Differentiation strategies

- **Theme** (artist retreat, music workshop, equestrian, foraging)
- **Service** (welcome basket, on-property activities)
- **Atypical** (yurt, treehouse, restored mill)
- **Niche** (digital nomad with fiber + coworking)

### Break-even point

- Cost to operate: €<X>/yr fixed
- Variable cost per night booked: €<Y>
- Break-even nights/year: <N>
- Break-even occupancy: <%>

### Verdict
- 🟢 **Strong play** — saturation low, demand high, regulatory clear
- 🟡 **Marginal** — saturation moderate, need differentiation
- 🟠 **Tight** — saturation high, need premium positioning
- 🔴 **Don't pursue** — saturation extreme + regulatory tightening
```

---

## 7. Inheritance modeling

**Goal**: surface the succession + tax cost of ownership transition.

### Output template

```markdown
## Inheritance & Succession Plan

**Property**: <address>
**Country**: <jurisdiction>
**Owners**: <list>
**Heirs (anticipated)**: <list>

### Forced-heirship analysis

| Country | Forced share | Notes |
|---|---|---|
| 🇫🇷 | Réserve héréditaire 50% (1 child) – 75% (3+) | Cannot disinherit children |
| 🇮🇹 | Quota legittima 50-75% | Spouse + children protected |
| 🇪🇸 | Legítima 50-66% | Per CCAA variation |
| 🇨🇭 | Pflichtteil 50-75% | Per cantonal civil law |
| 🇩🇪 | Pflichtteil 50% of intestate share | Children + spouse |
| 🇵🇱 | Zachowek 50% (or 66% for minors) | Cannot disinherit |
| 🇬🇧 | No forced heirship | Full testamentary freedom |
| 🇮🇪 | Spousal Legal Right Share 33-66% | Spouse only |

### EU Succession Regulation (Brussels IV)

- Lets EU residents elect **law of nationality** to govern succession
- Important for: foreign owners, dual nationals, cross-border families
- Election must be in writing in the will
- **Doesn't apply** to: UK, IE, DK (opted out), non-EU jurisdictions

### Tax burden at succession

| Tax | Rate | Threshold |
|---|---:|---|
| 🇫🇷 Droits de succession (children) | 5–45% | €100k abatement per child |
| 🇮🇹 Imposta successioni (children) | 4% | €1M each |
| 🇪🇸 Impuesto sucesiones | 7.65–34% | Per CCAA (huge variation) |
| 🇩🇪 Erbschaftsteuer (children) | 7–30% | €400k abatement per child |
| 🇬🇧 IHT | 40% | £325k nil-rate band |
| 🇮🇪 CAT (Group A) | 33% | €335k threshold |
| 🇸🇪 No inheritance tax | 0% | (abolished 2005) |
| 🇳🇴 No inheritance tax | 0% | (abolished 2014) |
| 🇵🇹 Imposto Selo | 10% (non-direct heirs) | Spouses + children exempt |

### Cross-border issues

- **Dual taxation**: home + property country may both tax
- **Double-tax treaty (DTT)** for inheritance: rare; check specific countries
- **Apostille + sworn translation** of all documents
- **Probate timing**: 6-24 months
- **Estate freeze** during probate — heirs can't sell

### Pre-mortem optimization strategies

| Strategy | What it does | Best for |
|---|---|---|
| **Donation en démembrement** (FR) | Transfer bare ownership, retain usufruct | Reduce IHT base |
| **Schenken mit Nießbrauch** (DE) | Same — gift with usufruct | Reduce ErbSt base |
| **SCI** (FR Société Civile Immobilière) | Hold property in family company | Easier transfer of shares vs property |
| **Trust** | Common-law jurisdictions only | Limited use in civil-law EU |
| **Lifetime gifting** | Use annual exemptions | Spread tax base over years |
| **Holding company** | International tiering | Complex international families |

### Recommended structure based on profile

- **Single-property primary residence**: simple will, exemption-aware
- **Multi-property portfolio**: SCI / family LLC + lifetime gifting
- **Cross-border heirs**: Brussels IV election + local will in each jurisdiction
- **Non-EU heirs (forced heirship)**: explicit Brussels IV election to home law
- **Blended family / step-children**: testamentary precision + survivor protection

### Verdict
- 🟢 **Plan in place** — heirs identified, tax-optimized, cross-border handled
- 🟡 **Refresh needed** — outdated will, life event since last review
- 🟠 **Action required** — forced-heirship surprise, cross-border complications
- 🔴 **Critical gap** — no will, conflicting jurisdictional rules, large tax exposure
```

---

## How to invoke

```
/property-deep-dive <addr> --all --journey=pre-offer
/property-deep-dive <addr> --tax --rental --journey=investor
/property-deep-dive <addr> --journey=foreign-buyer
/property-deep-dive <addr> --journey=renovation --save
```

Multiple journeys can be requested:
```
/property-deep-dive <addr> --journey=pre-offer,foreign-buyer
```

## Confidence labels

Each journey has its own confidence rating:
- **HIGH**: All input data current, country playbook fully populated, jurisdiction clear
- **MEDIUM**: One or two assumptions (e.g., interest rate, occupancy)
- **LOW**: Outdated data, multi-jurisdictional, regulatory in flux

## Caveats

- Journeys are **decision aids**, not legal/tax advice
- Always include "Consult local notary/solicitor/tax advisor" footer
- Numbers are scenario projections, not commitments
- Cross-border journeys need dual-jurisdiction professionals

## Forbidden hallucinations

- Never invent a tax bracket without sourcing
- Never claim "exempt" without citing legal article
- Never give percentages without rate basis
- Always surface jurisdictional caveats
