# Bermuda 🇧🇲 — Property Due-Diligence Playbook

ISO2: `bm`. Status: ✅ Fully populated (researched 2026-05-28).

> **Critical framing — read first**: Bermuda is a **self-governing British Overseas Territory** in the **North Atlantic** (~1,035 km / 643 mi ESE of Cape Hatteras, North Carolina — **NOT** in the Caribbean), running on **English common law** with its own apex court, the **Supreme Court of Bermuda**. The currency **BMD is pegged 1:1 to USD** and USD circulates interchangeably at par ([Bermuda Monetary Authority](https://www.bma.bm/)). The single most important due-diligence gate is that Bermuda operates **one of the world's most RESTRICTIVE foreign-buyer regimes**: a non-Bermudian may purchase residential property **ONLY above a statutory Annual Rental Value (ARV) floor** — **house ARV ≥ USD/BMD 126,000** or **condominium ARV ≥ USD/BMD 25,800** (set 1 Jan 2016, [gov.bm — Minister Fahy ARV-reduction remarks](https://www.gov.bm/articles/minister-fahy-remarks-reduction-arv-levels-residential-property) ❌ DEPRECATED — primary source removed; verify with gov.bm Housing & Property / Dept of Immigration — **figures >12 months old; re-verify current floor before any binding step**) — AND must obtain an **Alien Landholding Licence (ALL)** from the Minister under **Part VI of the Immigration and Protection Act 1956** (anti-fronting provisions block trust/nominee circumvention). On grant of the ALL a **licence fee** of **~12.5% (house) / ~8% (condo) / ~6.5% (resort) / ~6% (Permanent Resident's Certificate holder)** of the purchase price is payable — **these percentages are from SECONDARY legal/realtor guides, cross-consistent but NOT confirmable on a primary gov.bm fee schedule — verify exact current % at the Department of Immigration before relying**. Tax stack: **NO income tax, NO capital gains tax, NO inheritance/estate tax** — government revenue is payroll tax, customs duty, **annual Land Tax** (banded on ARV) and **Stamp Duty** (marginal conveyance bands 2.1 / 3.15 / 4.20 / 6.3 / 7.35% under the Stamp Duty Act 1976 as amended 2023). **Title** is registered electronic title via the **Land Title Registry Office (LTRO)** under the **Land Title Registration Act 2011**. **Hurricane HAZARD is high** (North Atlantic hurricane belt, season ~Jun–Nov) **but VULNERABILITY is low** — Bermuda's reef-limestone/concrete construction + the catchment **Bermuda roof** + strict building code + status as a top-3 global reinsurance hub make the residential stock exceptionally resilient and well-insured. **Water has no island-wide piped mains for most homes**: each property collects its own potable supply via the white stepped Bermuda roof into an underground **rainwater tank** — a genuine ownership cost + risk line, not a footnote. **Confirm** ARV floors, ALL licence fee %, land-tax bands, stamp-duty bands and tank condition at primary sources **before any binding step**. Authoritative primary sources: **[Government of Bermuda (gov.bm)](https://www.gov.bm/)**, **[Department of Immigration](https://www.gov.bm/department/immigration)**, **[Office of the Tax Commissioner / Land Tax](https://www.gov.bm/land-tax)**, **[Land Title Registry Office (LTRO)](https://www.gov.bm/department/land-title-and-registration)**, **[Department of Land Valuation](https://www.gov.bm/property-valuations-bermuda)**, **[Bermuda Monetary Authority (BMA)](https://www.bma.bm/)**.

## Country profile

- **Geography**: North Atlantic archipelago of **~7 main islands + ~170 islets**, total land area **~54 km² (~21 sq mi)** (sources vary 50–54 km²; the Main Island is ~22.5 km long × ~1.6 km wide). ~1,035 km / 643 mi ESE of Cape Hatteras, North Carolina (CIA World Factbook / Britannica — *verify exact distance at primary geographic source*). Among the **most densely populated** territories on earth (~1,200–1,300 people/km²) and reportedly one of the **most expensive residential markets** per sq ft (secondary press/realtor framing — no primary global index; supported by the ~$750–$1,000/sq ft construction cost and ~$1m island-average headline in the price section below).
- **Capital**: **Hamilton** (City of Hamilton, Pembroke Parish). Other key centres: **St George's** (UNESCO World Heritage old town, east end), **Somerset** (Sandys, west end). **9 parishes**: Sandys, Southampton, Warwick, Paget, Pembroke, Devonshire, Smith's, Hamilton Parish, St George's.
- **Population**: **~64,000** (2016 census 63,779; ~63,935–64,600 commonly cited for 2024 per Worldometer/Macrotrends — *verify current at [gov.bm Department of Statistics](https://www.gov.bm/department/statistics)*). Mildly declining; ageing demographic; ~93% urban.
- **GDP per capita**: among the **highest in the world** (frequently cited >USD 100,000 nominal — *verify current at gov.bm Department of Statistics / World Bank*). Economy is **two-pillar**: international business (insurance / **reinsurance — a top-3 global reinsurance hub**) + tourism.
- **Currency**: **Bermudian dollar (BMD / Bd$)** — **pegged 1:1 to USD**; USD circulates interchangeably at par ([Bermuda Monetary Authority](https://www.bma.bm/)). No structural FX risk for USD-base buyers (see `--currency`).
- **Languages**: **English (official, sole)** — all contracts, deeds, statutes in English.
- **Legal system**: **English common law** + Bermudian statutes. Apex court is the **Supreme Court of Bermuda** (superior court of record); final appeal lies to the **Court of Appeal for Bermuda** and ultimately the **Judicial Committee of the Privy Council** (London). Conveyancing has moved to **registered electronic title** under the **Land Title Registration Act 2011** (LTRA 2011) administered by the **Land Title Registry Office (LTRO)** — mid-transition from the older deeds system (not every parcel is yet registered).
- **Admin / cadastre**:
  - **[Land Title Registry Office (LTRO)](https://www.gov.bm/department/land-title-and-registration)** — electronic register of legal estates/interests in land; registered-title system (guarantees title). Statutory basis **LTRA 2011**, amended by **LTRA 2017**, **Land Title Registration (Recording & Documents) Act 2017**, **Land Registration Rules 2018**.
  - **[Department of Land Valuation](https://www.gov.bm/property-valuations-bermuda)** — assesses the **Annual Rental Value (ARV)** of every property; the ARV drives BOTH the foreign-buyer floor (see eligibility) AND annual Land Tax (see `--tax`). Public ARV search at `http://www.landvaluation.bm/`.
  - **Office of the Tax Commissioner** — administers Land Tax + Stamp Duty.
- **Identifier**: parcel reference under the LTRO register (registered parcels) + the property's **ARV assessment** (Land Valuation). No French-style universal numéro de parcelle for unregistered (deeds-system) parcels.
- **Title concept**: **freehold (fee simple)** dominant; **condominium / strata** common; the ARV-floor regime (below) governs which freehold/condo titles a non-Bermudian may even acquire.
- **Recent reforms (12-month watchlist)**:
  - **"Work From Bermuda" One Year Residential Certificate DISCONTINUED 28 February 2025** — the 2020-launched remote-worker route is **ENDED**; remaining residence avenues for non-employed persons are **Permission to Reside on an Annual Basis** + the **Economic Investment Certificate** ([Mondaq — "The End Of The Digital Nomad Visa", 2025](https://www.mondaq.com/work-visas/1619512/the-end-of-the-digital-nomad-visa-how-else-can-individuals-reside-in-bermuda) + Citizen Remote — *secondary; verify current routes at [gov.bm Immigration](https://www.gov.bm/department/immigration)*). See `--visa`.
  - **Stamp Duty Act 2023 amendment** — marginal-rate conveyance system introduced; first-time-buyer exemption threshold raised from $750,000 to $1,000,000; stamp duty on mortgage transfers abolished; adjudication fee $212 from 1 Apr 2023 ([gov.bm — Amendments to the Stamp Duty Act 2023](https://www.gov.bm/stamp-duty-tax-legal-transactions)).
  - **BELCO 2026 residential tariff** effective 1 Jan 2026 ([belco.bm](https://belco.bm/know-your-rate-and-bill/)) — see `--mains`.

---

## 🇧🇲 Foreign buyer eligibility (READ FIRST)

This section determines whether a transaction is even **legally possible**. Bermuda runs **one of the most restrictive residential foreign-buyer regimes anywhere** — the gating mechanism is a **statutory ARV floor + a discretionary Ministerial licence + a substantial percentage licence fee**, NOT a simple registration. Misreading this gate is the single most expensive mistake a non-Bermudian buyer can make.

### Legal basis

- **Immigration and Protection Act 1956, Part VI** — "provisions to protect land in Bermuda for Bermudians"; includes robust **anti-fronting provisions** preventing use of trust/nominee/company arrangements to circumvent the protections (*verify statute citation at [gov.bm](https://www.gov.bm/)*).
- **Land Title Registration Act 2011** (+ 2017 amendments + Land Registration Rules 2018) — registered-title system administered by the LTRO.
- **Stamp Duty Act 1976** (amended 2023) + **Land Tax Act / Land Valuation framework** — transaction + holding taxes (Office of the Tax Commissioner).

### Buyer category matrix

| Buyer category | Right |
|---|---|
| **Bermudian (status / citizen)** | Full freehold; no ARV floor; no Alien Landholding Licence; standard conveyancing |
| **Spouse of a Bermudian (qualifying)** | Treated favourably — *verify current rules at Dept of Immigration* |
| **Permanent Resident's Certificate (PRC) holder** | May purchase **any** property (NOT bound by the ARV floor) **except government-subsidised housing**, **but STILL requires an Alien Landholding Licence**; licence fee **~6%** of price (house or condo) — *secondary; verify at gov.bm*. Restrictions: individual name only (not trust/company), residential use of the licensee, no sub-division, **rental only with the Minister's permission** |
| **Non-Bermudian (no PRC)** | May ONLY acquire property whose **ARV ≥ the statutory floor** (house **$126,000** / condo **$25,800**), **AND** must obtain an **Alien Landholding Licence**, **AND** pays a licence fee of **~12.5% (house) / ~8% (condo) / ~6.5% (resort)** of price — *percentages secondary; verify at gov.bm* |
| **Non-Bermudian company / trust** | Heavily restricted; anti-fronting provisions apply; specialist legal advice essential |

### The ARV-floor system (who can buy what)

A non-Bermudian (without a PRC) may **ONLY** purchase residential property whose **Annual Rental Value (ARV)** — the notional annual rent assessed by the Department of Land Valuation, the SAME figure used for Land Tax — is **at or above a statutory floor**. ⚠️ **The ARVs published by the Department of Land Valuation are anchored to a valuation date of 1 July 2014, not to current rental levels** ("The ARVs published through this website represent rental values current on or about the valuation date of 1st July 2014 and not current levels of rental value" — Department of Land Valuation, 2026-09-18 verified). A property's ARV is therefore **not** a current-market rent and must not be read as one; confirm the assessed ARV on the current Valuation List before treating a property as clearing the floor.

| Dwelling type | Minimum ARV a non-Bermudian may acquire | Effective date | Source |
|---|---|---|---|
| **House (free-standing)** | **$126,000** (reduced from $153,000) | 1 Jan 2016 | [gov.bm — Minister Fahy ARV-reduction remarks](https://www.gov.bm/articles/minister-fahy-remarks-reduction-arv-levels-residential-property) ❌ DEPRECATED — primary source removed; verify with gov.bm Housing & Property / Dept of Immigration |
| **Condominium** | **$25,800** (reduced from $32,400) | 1 Jan 2016 | [gov.bm — same](https://www.gov.bm/articles/minister-fahy-remarks-reduction-arv-levels-residential-property) ❌ DEPRECATED — primary source removed; verify with gov.bm Housing & Property / Dept of Immigration |

> ⚠️ These thresholds were last changed **1 Jan 2016** — primary-sourced to the Minister Fahy remarks page, but **>12 months stale; re-verify the current floor at [gov.bm Housing & Property](https://www.gov.bm/residents/housing-and-property) / Dept of Immigration before output**. They are policy-set and have been adjusted historically (2014, 2016). **Note**: a secondary realtor source (JBM Realty) lists the condo floor as $32,400 — that figure CONTRADICTS the primary $25,800 (the primary figure wins; the $32,400 is the pre-2016 level).
> **Effect**: a non-Bermudian is **locked out of the bulk of the market** — only the **top ARV tier of houses + a slice of condos** qualify. In practice a licence-eligible house entry price is well into the **multi-million USD** range.

### Licence to acquire — the Alien Landholding Licence (ALL)

A non-Bermudian (and a PRC holder) must apply to the **Minister** (Dept of Immigration) for sanction to acquire — issued as an **Alien Landholding Licence (ALL)** ("licence to acquire"). **The transaction CANNOT complete without it.**

- **Application fee**: **$1,706** (per secondary realtor/legal guides; described as refundable if the licence is granted) — *VERIFY current application fee at gov.bm; secondary-only*.
- **Processing**: can take **months** (a PRC application is cited at up to ~6 months — *secondary; verify*).
- **Conditions** typically attached: specific named property, individual name only (not trust/company for PRC), residential use of the licensee, no sub-division, rental only with Ministerial permission.

### Foreign-purchaser licence fee (% of value) — the real cost

On grant of the ALL, a licence fee is payable as a **percentage of the purchase price** — this is the headline foreign-buyer tax and it is **substantial**:

| Buyer / property type | Licence fee | Source tier |
|---|---|---|
| **Non-Bermudian — house** | **~12.5%** of price | secondary (Appleby, JBM Realty, Sinclair, Cranfields, ICLG) — **verify at gov.bm** |
| **Non-Bermudian — condominium** | **~8%** of price | secondary — **verify at gov.bm** |
| **Property in a designated tourist/resort development** | **~6.5%** of price | secondary — **verify at gov.bm** |
| **PRC holder — house OR condo** | **~6%** of price | secondary — **verify at gov.bm** |

> ⚠️ **The 12.5% / 8% / 6.5% / 6% licence-fee percentages are from SECONDARY sources** (Bermuda law firms + realtors — Appleby, JBM Realty, Sinclair, Cranfields, ICLG Private Client). They are **cross-consistent across multiple independent sources** but **could NOT be pulled off a primary gov.bm fee schedule** (the acquisition-by-non-Bermudian gov.bm page lists only gazette notices, no fee table). The independent fact-check audit (2026-05-28) confirmed these as **UNVERIFIABLE against primary**. Tag every use `(per legal/realtor guides — verify exact current % at gov.bm Dept of Immigration fee schedule)`. **These are large, decision-driving numbers — do NOT present as primary-sourced fact.**
> Combined with stamp duty (`--tax`), a non-Bermudian buying a house faces **~12.5% licence fee + up to 7.35% marginal stamp duty + ~1.5–2% legal**, a **~15–22% transaction-cost load on top of price** — THE defining feature of the Bermuda regime.

### Compliance / AML

- **Source-of-funds documentation** required; KYC/AML obligations on attorneys + realtors as regulated professionals.
- **Anti-fronting** (Part VI, BIPA 1956): using a Bermudian or a structure to "front" for a non-Bermudian acquisition is prohibited and policed.
- **Beneficial-ownership disclosure**: under Bermuda's AML / corporate framework for corporate-held real estate.

### Verification path (before any reservation)

1. **Confirm the ARV** of the target property at the Department of Land Valuation (`http://www.landvaluation.bm/`) — does it clear the floor for your buyer category?
2. **Confirm buyer category** (Bermudian / PRC / non-Bermudian) and the applicable licence fee % with a Bermudian attorney.
3. **Budget the full transaction stack**: licence fee % + marginal stamp duty + legal ~1.5–2% + $1,706 application + $212 adjudication.
4. **Pull the title**: LTRO register search (registered parcel) or deeds/abstract (unregistered parcel — buyer's attorney handles first registration).
5. **Apply for the Alien Landholding Licence** to the Minister — gates completion; allow **months**.
6. **Tank + roof inspection** (see `--mains`) — water supply is property-specific in Bermuda.

---

## Section: `--price`

### Primary sources

- **[Department of Land Valuation](https://www.gov.bm/property-valuations-bermuda)** — assesses **ARV (annual rental value)** for every property; public search `http://www.landvaluation.bm/`. **This is the ONLY official "value" Bermuda publishes — it is a RENTAL value, NOT a sale-price index.**
- **No primary government sale-price index exists for Bermuda.** All sale-price figures below are **listing / press-derived (secondary)**.

### Listing platforms

- **Coldwell Banker Bermuda Realty** — `https://www.bermudarealty.com/`
- **Rego Sotheby's International Realty** — `https://www.regosothebysrealty.com/`
- **Sinclair Realty / Coldwell Banker** — `https://www.sinclairrealty.com/`
- **L.P. Gutteridge** — `https://www.lpg.bm/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **Bermuda Property Link / KW Bermuda** — secondary aggregators
- **JamesEdition / Christie's International** — ultra-prime international syndication (secondary)

### 2025-2026 price benchmarks

> **All figures below are `est.` / listing- + press-derived (SECONDARY).** Bermuda publishes **ARV (rental value), not a sale-price index** — there is **no primary HPI**. The one semi-primary anchor is the ~$1m island-average headline (Royal Gazette press, 2025). **Cross-check with ≥ 3 active listings on the same parish before relying.** Values in USD ≈ BMD (1:1 peg).

| Market / area | Typical price (USD, secondary) | Notes |
|---|---|---|
| **Island-wide average home** | **~$1,000,000** | "cost of average Bermuda home is $1m" — Royal Gazette, 28 May 2025 (*secondary press; headline median proxy*) |
| **Construction cost** | **~$750–$1,000 / sq ft** | among the highest globally (2025, *secondary realtor guides*) |
| **Paget Parish** (gracious estates, harbour views) | **~$3m–$10m** | luxury listings (JamesEdition / realtors — *secondary*) |
| **Tucker's Town** (St George's — ultra-prime; private beaches, yacht docks; historic foreign-ultra-wealthy enclave) | **frequently $10m+** | luxury listings (*secondary*) |
| **Hamilton / Pembroke** (central, waterfront) | **premium central pricing** | *data not publicly available — verify with current listings / Land Valuation ARV* |
| **Warwick / Southampton** (south-shore beaches, condos) | mid-to-upper market | *verify with current listings* |

> **The ARV floor reframes price**: a non-Bermudian house buyer is effectively shopping **ONLY the top ARV tier** — so practical entry prices for licence-eligible houses sit in the multi-million range regardless of the island "average".

### Compute

1. **Confirm ARV first** (`http://www.landvaluation.bm/`) — it determines eligibility (foreign buyer) AND Land Tax band. Sale price and ARV are different numbers.
2. **USD/sq ft = price ÷ built-area sq ft** (Bermuda listings quote square feet). Compare to ≥ 3 active listings on the same parish.
3. **Trap — eligibility, not just affordability**: a non-Bermudian must check the property clears the ARV floor BEFORE valuing it on price. A cheaper home below the floor is simply **not purchasable** by a non-Bermudian.
4. **Trap — tank/roof condition** (see `--mains`) materially affects value + carrying cost; inspect.
5. **Trap — registered vs unregistered title**: LTRA-2011-registered parcels are faster/cleaner to convey than unregistered deeds-system parcels.

### Key terms

- **ARV (Annual Rental Value)** — notional annual rent assessed by Land Valuation; drives the foreign-buyer floor + Land Tax
- **Alien Landholding Licence (ALL)** — Ministerial sanction a non-Bermudian/PRC needs to acquire
- **Licence fee** — % of price payable on grant of the ALL (the headline foreign-buyer cost)
- **Land Tax** — annual property tax banded on ARV
- **Stamp Duty** — one-time marginal conveyance tax
- **PRC (Permanent Resident's Certificate)** — right to live + work in Bermuda; more favourable buyer category
- **Bermuda roof** — white stepped limestone roof that catches rainwater into the property's tank

---

## Section: `--traffic`

### Sources

- **[Transport Control Department (TCD), gov.bm](https://www.gov.bm/department/transport-control)** — vehicle registration + the **one-car-per-household** policy.
- **[Department of Public Transportation](https://www.gov.bm/department/public-transportation)** — pink buses + ferries.
- **OSM** fallback via Overpass — `highway` tag class.

### Reality

Bermuda is a **tiny, dense island** (~54 km²) with a single arterial spine (Middle Road / Harbour Road / South Road run roughly parallel east-west). There is **no public AADT portal**. Congestion is structural, not data-published — peak flow into and out of **Hamilton** (the employment centre) at morning + evening rush is the defining traffic reality.

- **One-car-per-household cap**: car ownership is historically restricted to **one private car per residential dwelling** to manage congestion (*verify current rule at [TCD](https://www.gov.bm/department/transport-control)*). Mopeds/scooters + buses + ferries fill the gap; **no rideshare** historically; taxis + minibuses operate.
- **Drive on the LEFT.** General speed limit is low island-wide (**~35 km/h** — *verify current limit at TCD*).
- **Tourists may not rent cars** historically (only scooters / "Twizy"-style minicars + taxis) — *verify current rules*.

### Coarse OSM fallback

| OSM `highway` | Bermuda road class | Typical relative load |
|---|---|---|
| `primary` | Middle Road / South Road / Harbour Road arterials | highest — Hamilton approaches |
| `secondary` | parish connectors | moderate |
| `tertiary` / `residential` | lanes / tribe roads | low |

### Verdict bands (heuristic — calibrate on-site)

- 🟢 residential tribe road / lane, away from Hamilton approaches
- 🟡 parish connector road
- 🟠 Middle/South/Harbour Road segments near Hamilton at peak
- 🔴 Hamilton CBD approaches at morning + evening rush (the structural island bottleneck)

### Caveats

- **Hamilton-centric commute**: the employment centre concentrates peak flow; living west (Sandys/Southampton) or east (St George's) means a long single-route commute.
- **Cruise-ship days** (Dockyard, Sandys / Hamilton) surge pedestrian + bus + taxi demand seasonally.
- **No motorway / no rail** — the former Bermuda Railway is now the **Railway Trail** (recreational).

---

## Section: `--tax`

> **Headline**: Bermuda has **NO income tax, NO capital gains tax, NO inheritance/estate tax, NO annual wealth tax**. Government revenue is **payroll tax, customs duty, Land Tax** (annual, banded on ARV) and **Stamp Duty** (one-time, marginal conveyance bands). Real-estate-specific burdens for a foreign buyer also include the **Alien Landholding Licence fee** (see Foreign buyer eligibility) — economically a one-time foreign-buyer transfer tax.

### Annual property tax — Land Tax (banded on ARV)

Administered by the **Office of the Tax Commissioner** on the **ARV** set by the Department of Land Valuation. Billed **twice yearly (March & September)**; late interest cited at **7%/yr** ([gov.bm/land-tax](https://www.gov.bm/land-tax)).

**Private-dwelling progressive bands** (gov.bm/land-tax, fetched 2026-05-28):

| ARV band | Rate (marginal on the portion in band) |
|---|---|
| $0 – $11,000 | 0.80% |
| $11,001 – $22,000 | 1.80% |
| $22,001 – $33,000 | 3.50% |
| $33,001 – $44,000 | 6.50% |
| $44,001 – $90,000 | 17.00% |
| $90,001 – $120,000 | 35.00% |
| $120,001+ | 55.00% |

> ⚠️ The live gov.bm/land-tax fetch returned an **ambiguous structure** — alongside the marginal bands above it rendered a **flat base figure (~$150)** for the lowest tier; whether that $150 is per-period (×2 = ~$300/yr) needs reconciling. **Land Tax IS marginal/banded on ARV**; **verify the exact base-row treatment + current effective FY at [gov.bm/land-tax](https://www.gov.bm/land-tax) before relying.** Note the top marginal rate (55%) is on the ARV portion above $120,000 — high-ARV homes (i.e. exactly the homes a non-Bermudian must buy) carry a **material annual Land Tax**.
- **Commercial**: 9.5% (from 1 Jul 2019); **Economic Empowerment Zones**: 7%; **tourist properties**: 8.9% (gov.bm/land-tax — *verify current*).
- **Senior relief**: residents **65+** owning/occupying their dwelling — exemption up to **$1,791/yr** for ARV up to **$45,500** (gov.bm/land-tax — *verify current*).

### Stamp Duty on conveyance — marginal bands

Administered by the Office of the Tax Commissioner. **Stamp Duty Act 1976**, amended **2023** (marginal-rate system; first-time-buyer exemption raised from $750k to $1,000,000; stamp duty on mortgage transfers abolished) ([gov.bm/stamp-duty-tax-legal-transactions](https://www.gov.bm/stamp-duty-tax-legal-transactions), fetched 2026-05-28).

**Conveyance of Bermuda real property — marginal bands:**

| Slice of value | Rate |
|---|---|
| First $100,000 | **2.1%** |
| Next $400,000 (to $500k) | **3.15%** |
| Next $500,000 (to $1m) | **4.20%** |
| Next $500,000 (to $1.5m) | **6.3%** |
| Over $1.5m | **7.35%** |

- **Conveyance of NON-Bermuda property**: 1%.
- **Adjudication fee**: **$212** (from 1 Apr 2023).
- **First-time-buyer / Primary Family Homestead exemptions** exist (gov.bm "Stamp Duty Relief" + "Primary Family Homestead Designation") — **but these generally target BERMUDIANS; do NOT assume a non-Bermudian buyer qualifies. Verify applicability.**

### Closing-cost stack — non-Bermudian buying a HOUSE (illustrative; verify each %)

| Item | Rate / amount | Source tier |
|---|---|---|
| **Alien Landholding Licence fee** | **~12.5%** of price (house) | secondary — verify at gov.bm |
| **Stamp Duty (conveyance)** | marginal 2.1 → 7.35%; **~7.35% on slice > $1.5m** | PRIMARY (gov.bm) |
| **ALL application fee** | **$1,706** (refundable if granted) | secondary — verify |
| **Adjudication fee** | **$212** | PRIMARY |
| **Buyer attorney's fees** | **~1.5–2.0%** of price | secondary — verify |
| **Total foreign-buyer load** | **~15–22% on top of price** | composite |

> This **~15–22% load** is THE defining feature of the Bermuda regime and the headline number a non-Bermudian buyer needs.

### Capital gains / inheritance / wealth / income

- **NO capital gains tax.**
- **NO inheritance / estate tax; NO gift tax** (stamp duty applies to dutiable transfers including some gifts — verify).
- **NO wealth tax.**
- **NO personal income tax** (revenue is payroll tax on employers/employees + customs duty).

### Future risk

- **OECD Pillar Two corporate income tax (15%)**: Bermuda has introduced a **Corporate Income Tax** for in-scope large MNEs (€750M+ consolidated revenue) effective fiscal years from 2025 — **affects in-scope multinationals, NOT individual property owners** (*verify scope at gov.bm if buying via a corporate structure*).
- **Land Tax / Stamp Duty bands** are revisited at budget cycles — re-verify each budget.

⚠️ Verification: confirm the property's **current ARV** + **Land Tax band** + **stamp-duty bands** + applicable **licence fee %** at [gov.bm/land-tax](https://www.gov.bm/land-tax), [gov.bm/stamp-duty-tax-legal-transactions](https://www.gov.bm/stamp-duty-tax-legal-transactions), Land Valuation, and a Bermudian attorney **before contract**.

---

## Section: `--rental`

### Renting out as a foreign owner — heavily restricted

- **Non-Bermudian owner**: renting out the property requires a **PERMIT from the Minister** — permission is "usually given provided the owner is living off the island" (*secondary realtor/legal — verify at gov.bm*). i.e. you generally **CANNOT buy-to-let as an absentee investor freely**; the regime is built around **owner-occupation, not yield**.
- **PRC holder**: rental **only with the Minister's permission** (per ALL licence restriction).
- **Vacation / short-term rentals**: regulated — gov.bm "Vacation Rentals Fact Sheet and Forms" (a registration regime exists). **Verify current rules + any registration fee at gov.bm.**

### Long-term residential rentals

- Governed by ordinary contract + Bermudian landlord-tenant law (English common-law derivation). High rents track the high cost of living + scarce supply.

### Yield benchmarks

> **No primary government rental-yield index exists for Bermuda.** Given ~$1m+ entry prices, high carrying costs (Land Tax up to 55% marginal on high ARV, hurricane insurance, tank maintenance), and the **Ministerial-permit constraint on foreign-owner letting**, gross yields are typically **LOW relative to capital value**.
> **`data not publicly available — no primary yield index; estimate only`. Do NOT rely on a fabricated yield %.** Model any rental case off ≥ 3 comparable actual lettings + a written confirmation of letting permission.

### Strategic notes

- The defining rental fact is **regulatory, not financial**: a non-Bermudian generally needs the **Minister's permission to let** and that hinges on living off-island. Treat Bermuda as an **owner-occupier / second-home jurisdiction**, not a buy-to-let market.
- Hurricane insurance + tank maintenance are real operating-cost lines for any let property.

---

## Section: `--work=<profession>`

### Reality

Working in Bermuda requires being **Bermudian**, the **spouse of a Bermudian**, or a **PRC holder**; **everyone else needs an employer-sponsored work permit** under the immigration framework ([gov.bm — Types of work permits](https://www.gov.bm/types-work-permits)). The property thesis for most foreigners is **second-home / international-business-secondee / high-net-worth**, not local job-seeking. The **"Work From Bermuda" remote-worker certificate is DISCONTINUED** — the Ministry of Economy and Labour stopped accepting applications effective **28 Feb 2025** ([forms.gov.bm — Work From Bermuda](https://forms.gov.bm/work-from-bermuda)) (2025 data, source Bermuda Ministry of Economy and Labour); see `--visa`.

### Job platforms

- **[gov.bm — Job Board / Public Service](https://www.gov.bm/)** for civil-service roles
- **Bermuda Job Board / LinkedIn Bermuda** (active for insurance / reinsurance / finance / legal)
- **Royal Gazette classifieds**
- International-business secondment via reinsurance/insurance employers (the dominant skilled-migration channel)

### Visa routes for working

| Route | Eligibility | Authority |
|---|---|---|
| **Work permit (employer-sponsored)** | Bermudian employer + justification the role cannot be filled by a Bermudian | Dept of Immigration |
| **PRC (Permanent Resident's Certificate)** | Long-residence / qualifying categories — confers right to live + work | Dept of Immigration |
| **Spouse of a Bermudian** | Marriage to a Bermudian | Dept of Immigration |
| **Economic Investment Certificate** | Qualifying investment in Bermuda | Dept of Immigration (*verify current threshold*) |

### Salary benchmarks

- Salaries in **international business (insurance / reinsurance / finance / law)** are **high** by global standards, matching a very high cost of living. **No primary salary index captured — verify at gov.bm Department of Statistics; do NOT fabricate figures.**

### Catchment

- **Hamilton / Pembroke**: the employment centre — international business, government, professional services, retail.
- **Elsewhere**: hospitality + services + trades; thin formal employment outside Hamilton.

---

## Section: `--risks`

### Primary hazard sources

| Source | URL | What it gives |
|---|---|---|
| **Bermuda Weather Service** | `https://www.weather.bm/` | Hurricanes, tropical storms, marine forecasts |
| **US National Hurricane Center (NHC)** | `https://www.nhc.noaa.gov/` | Atlantic-basin authoritative track + intensity |
| **[Department of Planning](https://www.planning.gov.bm/)** | `https://planning.gov.bm/` | Building code, hurricane-repair guidelines |
| **Bermuda Government (gov.bm)** | `https://www.gov.bm/` | Emergency measures, EMO |

### Hurricane — HIGH hazard, LOW vulnerability

- **Position**: Bermuda sits in the **North Atlantic hurricane belt**; direct hits + near-misses recur. Season **~1 June – 30 November**.
- **Historical reference events** (date-stamped; *verify any specific damage figure before quoting*): **Hurricane Fabian (2003)** — most destructive in modern memory; **Gonzalo + Fay (2014)**; **Nicole (2016)** — Cat 3 near-direct hit. *Do NOT fabricate damage costs — none sourced here.*
- **BUT exceptionally resilient building stock**: traditional construction = **massive reef-limestone / concrete-block walls + heavy cemented limestone tile "Bermuda roofs"**, engineered under a **strict building code** to withstand sustained winds well over 100 mph (99% Invisible / RMS / OBMI — *secondary but well-corroborated; verify building-code specifics at [planning.gov.bm hurricane-repair guidelines](https://planning.gov.bm/index.php/planning-guidelines-for-hurricanes-repairs/)*).
- **Insurance**: nearly every building is insured; Bermuda is **one of the world's largest reinsurance centres**, so domestic primary insurers cede catastrophe risk efficiently. Property insurance is available and the market sophisticated — but **hurricane/wind cover is a material cost line**. **Get a binding quote pre-purchase.** *Do NOT fabricate a premium figure — none sourced.*
- **Risk framing**: hurricane **HAZARD is high** but **VULNERABILITY is low** (code + construction + insurance) — **net residential risk moderated, not absent**. State both sides.

### Coastal flood / storm surge / sea-level rise

- **Storm surge** on low coastal parcels is the principal acute coastal mechanism in a strike.
- **Sea-level rise**: IPCC AR6 projects rising Atlantic SLR through 2100 — exposure for low-elevation coastal parcels; model parcel-level via Climate Central (`https://coastal.climatecentral.org/`). Bermuda's limestone topography gives modest relief inland.

### Freshwater scarcity (a resilience risk)

- **No rivers or lakes**; most homes depend on the **rainwater tank** (see `--mains`). A prolonged dry season or a contaminated/undersized tank = no potable water. **Tank capacity + condition is a genuine risk line**, not a footnote.

### Seismic / volcanic

- **No seismic risk of note**; **no volcanic risk** (Bermuda is a mid-ocean volcanic seamount cap, long extinct — not an active arc).

### Risk dashboard — typical Bermuda residential

| Class | Severity | Action priority |
|---|---|---|
| **Hurricane (hazard)** | 🟠 | Confirm code-compliant reef-limestone/concrete build + Bermuda roof + binding insurance quote |
| **Hurricane (vulnerability, well-built stock)** | 🟢–🟡 | Resilient construction + reinsurance-deep market moderates net risk |
| **Storm surge / coastal flood** | 🟠 (low coastal parcel) / 🟡 (elevated/inland) | Verify elevation + surge exposure; engineering survey for waterfront |
| **Freshwater / tank dependence** | 🟡–🟠 | Inspect tank capacity + condition + roof catchment; budget trucked-water top-ups |
| **Insurance cost** | 🟠 | Material annual cost line; get binding quote pre-purchase |
| **Sea-level rise (long-term)** | 🟡–🟠 | Model 2050+ for low coastal parcels |
| **Title (unregistered deeds-system parcel)** | 🟡 | Specialist attorney; LTRO first-registration if unregistered |
| **Seismic / volcanic** | 🟢 | Not a material factor |

---

## Section: `--mains`

### Water — the signature Bermuda quirk: rainwater tanks, no island-wide piped mains

Bermuda has **NO rivers or lakes and no island-wide piped mains-water network for most homes.** Each building collects its **OWN potable water** via the white stepped **Bermuda roof** into an underground **rainwater tank**:

- **Building regulation** mandates roof catchment guttered to the tank, with **minimum tank capacity tied to roof area** (rule-of-thumb cited: ~80% of roof catchment guttered to tank; ~8 gallons of tank per sq ft of roof, and/or ≥100 gallons per 10 ft of roof) — *secondary (99% Invisible / Bermuda-Online); **verify exact code spec at [planning.gov.bm](https://www.planning.gov.bm/) building code**.*
- **Due-diligence implication**: a buyer **MUST** check tank condition + capacity, roof catchment integrity, and whether **trucked-water top-ups** are routinely needed. **Tank water is a genuine ownership cost + risk line.**
- Some areas have a **government / Watlington Waterworks piped supply or desalination top-up** — **verify availability by parish.**

### Power — BELCO monopoly, among the most expensive in the world

- **[Bermuda Electric Light Company (BELCO)](https://belco.bm/)** — monopoly utility, island-wide grid. Bermuda electricity is **among the most expensive globally** (imported-fuel generation + small grid). Bill = **graduated facilities charge** + **per-kWh energy charge** + **fuel adjustment rate (FAR, set quarterly)**.
- **Residential energy charges (effective 1 Jan 2026, [belco.bm](https://belco.bm/know-your-rate-and-bill/) — PRIMARY)**:

| Block | kWh range | Rate |
|---|---|---|
| Block 1 | up to 250 kWh | **$0.1370 / kWh** |
| Block 2 | 251–700 kWh | **$0.2436 / kWh** |
| Block 3 | above 700 kWh | **$0.3803 / kWh** |

- **Fuel Adjustment Rate (FAR)** Q1 2026: **13.799¢ / kWh** (set quarterly — [belco.bm](https://belco.bm/know-your-rate-and-bill/)).
- **Residential Graduated Facilities Charge**: a fixed monthly fee — exact dollar amount not captured this pass; verify at [belco.bm](https://belco.bm/know-your-rate-and-bill/).
- **Solar / grid-tie** programs exist under the BELCO grid code; given block-3 rates above $0.38/kWh, residential solar economics are attractive (*verify current net-metering / interconnection terms at belco.bm*).
- **Standby generator + inverter** advisable for hurricane-season continuity.

### Connectivity

- Fibre / broadband available island-wide (small, dense island); mobile + fibre ISPs operate. *No primary coverage figure captured — verify provider coverage.*

---

## Section: `--crime`

### Primary source

- **Bermuda Police Service (BPS)** — `https://www.bps.bm/` — crime statistics (data lags; reported via Ministry of National Security).
- **UK FCDO Travel Advice** + **US OSAC Bermuda Country Security Report** — comparative reference.

### Key context

- **2024 crime**: the Bermuda Police Service investigated **3,719 crimes** in 2024; there were **nine (9) murders** on the crime log, **seven of which occurred in a six-week period (24 May – 10 Jul 2024)** ([Royal Gazette, 28 May 2025 — "Weeks reveals 2024 crime statistics"](https://www.royalgazette.com/budget/news/article/20250528/weeks-reveals-2024-crime-statistics/) — *press, citing BPS*).
- **Homicide rate (historical)**: ~**10.9 per 100,000** (2021, World Bank / Macrotrends — *most recent complete rate figure captured*). Bermuda's homicides are predominantly **gang/gun-related**, concentrated among a small number of individuals — **not targeted at visitors or the general resident population**.
- **General safety**: low-to-moderate crime by US comparison; back-streets of Hamilton at night (after bars close) are the main petty-assault setting; **no reported gang violence targeting visitors** (US OSAC / CountryReports — *secondary*).
- **Property crime**: burglary + opportunistic theft; **homes left unoccupied** (second homes) are a target — alarm + caretaker arrangement standard for absentee owners.
- **Cyber / wire fraud against international buyers**: a rising global pattern — **always verify wire instructions verbally with your attorney via a known phone number before sending purchase funds.**

### Verdict bands (Bermuda-specific, heuristic)

- 🟢 most residential parishes (Paget, Warwick, Smith's, Sandys residential) — low resident-facing crime
- 🟡 Hamilton periphery; areas with documented gang activity
- 🟠 specific Hamilton back-streets late at night; known gang-feud micro-areas
- 🔴 (not a general-area designation — Bermuda's serious violence is individual/gang-targeted, not geographically broad)

### Confidence

MEDIUM. BPS publishes aggregated totals (relayed via the Royal Gazette / Ministry of National Security) but not parcel-level detail. **UK FCDO + US OSAC advisories** track current dynamics.

---

## Section: `--amenities`

Universal OSM Overpass logic per `shared/amenities-osm.md`. Bermuda-specific conventions:

- **Supermarket**: **Lindo's**, **The MarketPlace**, **Miles Market**, **Arnold's**, **Supermart**; tag `shop=supermarket`.
- **Pharmacy**: **Phoenix Stores / Phoenix Centre**, **People's Pharmacy**, **Robertson's Drug Store**, **Caesar's Pharmacy**; tag `amenity=pharmacy`.
- **Hospital**: **King Edward VII Memorial Hospital (KEMH, Paget — main acute hospital)**, **Mid-Atlantic Wellness Institute (psychiatric)**; tag `amenity=hospital`. Bermuda Hospitals Board operates KEMH; serious specialist cases are often **air-evacuated to the US (Boston / NYC)** — medical-evacuation insurance is standard practice for residents.
- **Banks**: **HSBC Bermuda**, **Butterfield Bank**, **Clarien Bank**; tag `amenity=bank`.
- **Schools**: public + private (Saltus Grammar School, Warwick Academy, Bermuda High School, Mount Saint Agnes); Bermuda College (tertiary); tag `amenity=school`.
- **Marinas / ferries**: **Royal Bermuda Yacht Club (Hamilton)**, **Dockyard (Sandys)**, ferry terminals (Hamilton ⇄ Dockyard ⇄ St George's); tag `leisure=marina`.
- **Public transport**: government **pink buses** + **ferries**; mopeds/scooters common; **drive on the LEFT**.

### Verdict bands (Bermuda — compact-island geography)

- 🟢 < 1 km / short drive to supermarket + pharmacy (Hamilton, Paget, Warwick, central parishes)
- 🟡 most residential parishes — short drive
- 🟠 far west (Sandys) / far east (St George's) — longer single-route trips to Hamilton + KEMH
- 🔴 (rare — the island is small enough that no point is far in distance, though peak traffic stretches travel time)

⚠️ **Compact-island reality**: the whole island is ~22 km end-to-end — **anywhere is within ~45–60 min drive of Hamilton + KEMH**; medical access is good for routine care, but **serious specialist cases are typically air-evacuated off-island (US)** — medical-evacuation cover is standard.

---

## Section: `--climate`

Universal logic per `shared/climate-projections.md`. Bermuda-specific overrides:

- **Köppen-Geiger**: **Cfa / Af-borderline humid subtropical** — warm humid summers, mild winters (Gulf Stream-moderated); no true dry season; rainfall spread year-round (the basis of the rainwater-tank water supply).
- **Coastal exposure**: every property is near the coast (the island is narrow); modest elevation; the **Bermuda roof + tank** are the climate-adapted vernacular.
- **Reference baseline**: Bermuda Weather Service normals + IPCC AR6 (North Atlantic SIDS band).
- **Key projections** (IPCC AR6, SSP2-4.5 / SSP5-8.5):
  - Annual mean temperature rising; more hot/humid days.
  - **Sea-level rise**: rising Atlantic SLR through 2100 — exposure for low-lying coastal parcels.
  - **Hurricane intensity**: Atlantic-basin Cat 4–5 share trending up — relevant to a hurricane-belt island (offset by resilient construction + reinsurance-deep insurance market).
  - **Rainfall variability**: dry-spell risk matters specifically because of **tank-dependent water supply** — a drier shoulder season stresses household water security.
- **Acute-event flags**:
  - 🟠 Hurricane Cat 3–5 risk (North Atlantic belt; mitigated by code + construction + insurance)
  - 🟠 Insurance-cost line (hurricane/wind cover material)
  - 🟡 Sea-level rise for low coastal parcels (2050+ horizon)
  - 🟡 Drought / dry-spell stress on rainwater-tank water supply
  - 🟡 Heat/humidity rising — cooling (and dehumidification) load

### Climate verdict (typical Bermuda residential, code-compliant, not low-coastal)

🟡 **Watch / Adapt** — high hurricane hazard offset by resilient construction + deep insurance market; ensure code-compliant build + Bermuda roof + binding insurance quote + sound rainwater tank; SLR a 2050+ issue for sub-coastal parcels.

### Climate verdict (low-lying coastal / waterfront parcel)

🟠 **Adapt** — storm-surge + SLR exposure compounds; only acquire with engineering survey + funded insurance + surge mitigation.

### Confidence

HIGH for IPCC AR6 regional projections; MEDIUM for parcel-level surge/SLR specificity.

---

## Section: `--finance`

### Mortgage market

- **Regulator**: **[Bermuda Monetary Authority (BMA)](https://www.bma.bm/)** — prudential supervisor of banks + insurers.
- **Major lenders**:
  - **HSBC Bermuda** — `https://www.hsbc.bm/`
  - **Butterfield Bank (Bank of N.T. Butterfield & Son)** — `https://www.butterfieldgroup.com/`
  - **Clarien Bank** — `https://clarienbank.com/`

### LTV + tenor

> No primary published LTV/tenor matrix captured. Bermudian banks lend to qualifying buyers; foreign buyers typically face **larger down-payments + shorter tenor**. **Verify current LTV / rate / tenor with the lender at quote stage — do NOT rely on a fabricated rate.**

| Borrower | LTV (indicative, secondary) | Notes |
|---|---|---|
| **Bermudian resident, salaried** | higher LTV, longer tenor | *verify with lender* |
| **Foreign / non-resident** | **~20–30% down typical** (i.e. ~70–80% LTV ceiling) | *secondary — verify; shorter tenor* |

### Rate structure + structuring

- Rates track Bermudian bank pricing (USD-linked given the 1:1 peg) — **verify current rate with lender; none fabricated here.**
- **2023 reform abolished stamp duty on mortgage transfers** (gov.bm).
- **Many foreign buyers structure** as a **cash purchase** (the licence-fee + stamp-duty load already front-loads cost) or borrow offshore against home-country security.

### Banking access

- Account opening: **passport + proof of address + references + source-of-funds**; CRS / FATCA self-certification. Bermuda's three retail banks (HSBC, Butterfield, Clarien) dominate.

---

## Section: `--currency`

- **Currency**: **Bermudian dollar (BMD / Bd$)**.
- **Peg**: **1:1 with USD** — administered by the **[Bermuda Monetary Authority (BMA)](https://www.bma.bm/)**; **USD circulates interchangeably at par**.
- **Practical effect for buyer**: **zero structural FX risk for USD-base buyers**; minimal residual risk for EUR/GBP/CAD buyers (USD-correlated). Prices, rents, taxes and licence fees are all effectively USD.
- **No exchange-control gate equivalent to a registration regime** for the *currency* — the gating step in Bermuda is the **Alien Landholding Licence** (see Foreign buyer eligibility), not FX registration. But **source-of-funds / AML documentation is mandatory**.
- **Devaluation risk**: the 1:1 USD peg is long-standing and underpinned by Bermuda's role as an international-finance + reinsurance centre; treat as stable but a **policy choice, not a structural certainty** (*monitor BMA*).

---

## Section: `--visa`

> **Critical update**: the **"Work From Bermuda" One Year Residential Certificate** (the 2020-launched remote-worker / digital-nomad route, application fee ~$263) was **DISCONTINUED on 28 February 2025** ([Mondaq — "The End Of The Digital Nomad Visa", 2025](https://www.mondaq.com/work-visas/1619512/the-end-of-the-digital-nomad-visa-how-else-can-individuals-reside-in-bermuda) + Citizen Remote — *secondary; verify at [gov.bm Work From Bermuda FAQ](https://forms.gov.bm/wfb/faq)*). **Do NOT present Work From Bermuda as an active programme.** Remaining residence routes for non-employed / investor persons are below.

| Route | Threshold / eligibility | Notes |
|---|---|---|
| **Permission to Reside on an Annual Basis** | Self-sufficiency / non-employed residence | Renewable annual permission — *verify current criteria + fee at gov.bm Immigration* |
| **Economic Investment Certificate (EIC)** | Qualifying investment in Bermuda | Investor-residence route — *verify current investment threshold + benefits at gov.bm Immigration* |
| **Permanent Resident's Certificate (PRC)** | Long-residence / qualifying categories | Confers right to live + work; more favourable PROPERTY buyer category (no ARV floor; ~6% licence fee) |
| **Work permit (employer-sponsored)** | Bermudian employer + non-Bermudian-cannot-fill justification | The dominant skilled-migration channel (international business) |
| **Spouse of a Bermudian** | Marriage to a Bermudian | Pathway to status over time |
| **"Work From Bermuda" remote-worker certificate** | **DISCONTINUED 28 Feb 2025** | **ENDED** — do not rely on; superseded by routes above |
| **Citizenship-by-investment (CBI)** | **NONE** | Bermuda does NOT operate a CBI scheme |

> **Property ≠ residency in Bermuda.** Buying property does **not** itself confer the right to reside or work. The Alien Landholding Licence governs *acquisition*; residence is a separate immigration question (PRC / EIC / Permission to Reside / work permit). Confirm both tracks with a Bermudian attorney **before committing**.

(Source: [gov.bm Department of Immigration](https://www.gov.bm/department/immigration) + [gov.bm — One Year Residential Certificate (now discontinued)](https://www.gov.bm/online-services/one-year-residential-certificate) + Mondaq / Citizen Remote — *primary department + secondary aggregators; verify current routes, thresholds + fees at gov.bm before relying*)

---

## Cost benchmarks (BM 2026)

| Item | Cost |
|---|---:|
| **Alien Landholding Licence fee — non-Bermudian house** | **~12.5% of price** (*secondary — verify at gov.bm*) |
| **Alien Landholding Licence fee — non-Bermudian condo** | **~8% of price** (*secondary — verify*) |
| **Alien Landholding Licence fee — resort development** | **~6.5% of price** (*secondary — verify*) |
| **Alien Landholding Licence fee — PRC holder** | **~6% of price** (*secondary — verify*) |
| **ALL application fee** | **$1,706** (refundable if granted; *secondary — verify*) |
| **Stamp Duty (conveyance, marginal)** | 2.1% → 7.35%; ~7.35% on slice > $1.5m (PRIMARY gov.bm) |
| **Adjudication fee** | **$212** (from 1 Apr 2023, PRIMARY) |
| Buyer attorney's fees | **~1.5–2.0% of price** (*secondary — verify*) |
| **Total foreign-buyer transaction load (house)** | **~15–22% on top of price** |
| **Annual Land Tax** | banded on ARV, 0.80% → **55% marginal** on ARV > $120,000 (PRIMARY gov.bm — *verify base row + FY*) |
| Hurricane + all-risk insurance | **material annual line — get binding quote** (*no figure fabricated*) |
| BELCO electricity (block 1 / 2 / 3, 2026) | **$0.1370 / $0.2436 / $0.3803 per kWh** + FAR 13.799¢ + facilities charge (PRIMARY belco.bm) |
| Rainwater tank inspection / trucked-water top-up | *property-specific — inspect; budget as a real line* |

---

## Active fiscal incentives + visa programs (2025–2026)

### Tax position (real-estate-relevant)

- **NO income tax / capital gains tax / inheritance tax / wealth tax** — universally applies.
- **OECD Pillar Two Corporate Income Tax (15%)** — applies to **in-scope large MNEs (€750M+ revenue)** from fiscal years 2025; **NOT individual property owners**.

### Residency / investor routes

- **Economic Investment Certificate (EIC)** — investor-residence route (*verify threshold at gov.bm*).
- **Permission to Reside on an Annual Basis** — non-employed self-sufficient residence.
- **Permanent Resident's Certificate (PRC)** — most favourable property buyer category.
- **"Work From Bermuda" remote-worker certificate** — **DISCONTINUED 28 Feb 2025** (do NOT promote as active).
- **Citizenship-by-investment**: **NONE**.

---

## Common listing platforms

- **Coldwell Banker Bermuda Realty** — `https://www.bermudarealty.com/`
- **Rego Sotheby's International Realty** — `https://www.regosothebysrealty.com/`
- **Sinclair Realty / Coldwell Banker** — `https://www.sinclairrealty.com/`
- **L.P. Gutteridge** — `https://www.lpg.bm/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **KW Bermuda / Bermuda Property Link** — secondary aggregators
- **JamesEdition / Christie's International** — ultra-prime international syndication (secondary)

---

## Caveats unique to BM

- **Foreign-buyer regime is RESTRICTIVE — the single most important gate**: a non-Bermudian may buy ONLY above the **ARV floor (house $126,000 / condo $25,800, set 1 Jan 2016 — re-verify)** AND must obtain an **Alien Landholding Licence** AND pay a **percentage licence fee (~12.5% / 8% / 6.5%; ~6% for PRC holders)**. This is NOT a registration formality.
- **Licence-fee percentages are SECONDARY, not primary**: cross-consistent across law firms + realtors but NOT confirmable on a primary gov.bm fee schedule (independent audit 2026-05-28 marked UNVERIFIABLE vs primary). Always tag `verify at gov.bm Dept of Immigration`.
- **ARV is the master number**: it sets BOTH the foreign-buyer floor AND annual Land Tax. Confirm a property's current ARV at the Department of Land Valuation (`http://www.landvaluation.bm/`) before valuing it.
- **Total foreign-buyer transaction load ~15–22%** of price (licence fee + marginal stamp duty up to 7.35% + legal + application + adjudication) — THE defining cost feature.
- **Land Tax is steeply progressive on high ARV** (up to **55% marginal** on ARV > $120,000) — and the homes a non-Bermudian is *required* to buy (above the ARV floor) sit in exactly that high-ARV territory.
- **Rental as a non-Bermudian owner needs the Minister's permission** (and generally requires the owner to live off-island) — **buy-to-let by absentee foreigners is largely closed; treat Bermuda as an owner-occupier regime, not a yield market.**
- **No primary sale-price index exists** — all area prices are listing/press-derived; **ARV (rental value) is the only official "value" Bermuda publishes.** Do NOT present prices as authoritative.
- **Water is property-specific**: most homes have **no piped mains** — each collects potable water via the **Bermuda roof** into an underground **rainwater tank**. **Inspect tank capacity + condition + roof catchment**; budget trucked-water top-ups.
- **BELCO electricity is among the world's most expensive** ($0.1370 / $0.2436 / $0.3803 per kWh blocks, 2026, + quarterly fuel adjustment + facilities charge); solar economics are attractive at block-3 rates.
- **Hurricane: high hazard, low vulnerability** — resilient reef-limestone/concrete construction + strict code + deep reinsurance market moderate net risk, but hurricane insurance is a material annual cost; get a binding quote pre-purchase.
- **Registered vs unregistered title**: Bermuda is mid-transition to LTRA-2011 registered electronic title (LTRO); not every parcel is registered — specialist attorney handles first registration of unregistered (deeds-system) parcels.
- **"Work From Bermuda" digital-nomad certificate is DISCONTINUED (28 Feb 2025)** — do not rely on it; use PRC / EIC / Permission to Reside / work permit.
- **Property ≠ residency**: owning property does not confer a right to live or work — the ALL governs acquisition; residence is a separate immigration track.
- **Wire fraud against international buyers** — verify wire instructions verbally with your attorney via a known phone number before sending funds.
- **No CBI**: Bermuda does NOT operate a citizenship-by-investment programme.

---

## Reddit / forum sources

- **r/bermuda** — primary Bermuda community
- **r/expats** Bermuda threads (relocation, cost of living, work permits)
- **TripAdvisor Bermuda Forum** — practical Q&A
- **The Royal Gazette** (`https://www.royalgazette.com/`) — Bermuda's newspaper of record (policy, crime stats, property market)
- **Bernews** (`https://bernews.com/`) — local news + government announcements
- **Bermuda-Online** (`https://www.bermuda-online.org/`) — long-running reference site (incl. property + the Bermuda roof; *secondary, dated in places*)

## Verification authorities

| Authority | When to call |
|---|---|
| **Government of Bermuda (gov.bm)** | Housing & property hub; cross-cutting |
| **Department of Immigration** | Alien Landholding Licence + PRC + EIC + work permits + residence |
| **Office of the Tax Commissioner** | Land Tax + Stamp Duty + adjudication |
| **Department of Land Valuation** | ARV assessment (drives foreign-buyer floor + Land Tax) |
| **Land Title Registry Office (LTRO)** | Registered title + first registration |
| **Supreme Court of Bermuda** | Land disputes / contentious matters (court, NOT registrar) |
| **Bermuda Monetary Authority (BMA)** | Currency peg + bank/insurer prudential supervision |
| **Department of Planning** | Building code + hurricane-repair guidelines + permits |
| **Bermuda Weather Service** | Hurricane + climate baseline |
| **Bermuda Police Service (BPS)** | Crime statistics + safety |
| **BELCO** | Electricity account + rates + solar interconnection |
| **Transport Control Department (TCD)** | Vehicle registration + one-car-per-household rule |
| **Bermuda Hospitals Board (KEMH)** | Healthcare + air-evacuation pathway |

## Source URL templates

| Source | URL pattern |
|---|---|
| Government of Bermuda — Housing & Property | `https://www.gov.bm/residents/housing-and-property` |
| ARV-floor reduction (Minister Fahy remarks, 2016) | `https://www.gov.bm/articles/minister-fahy-remarks-reduction-arv-levels-residential-property` ❌ DEPRECATED — primary source removed; verify with gov.bm Housing & Property / Dept of Immigration |
| Land Tax (bands, ARV-based) | `https://www.gov.bm/land-tax` |
| Stamp Duty on legal transactions (conveyance bands) | `https://www.gov.bm/stamp-duty-tax-legal-transactions` |
| Stamp Duty Relief | `https://www.gov.bm/stamp-duty-relief` |
| Property valuations / ARV methodology | `https://www.gov.bm/property-valuations-bermuda` |
| Land Valuation public search | `http://www.landvaluation.bm/` |
| Land Title & Registration (LTRO) | `https://www.gov.bm/department/land-title-and-registration` |
| Acquisition of Property by a Non-Bermudian (gazette notices) | `https://www.gov.bm/theofficialgazette` |
| Permanent Resident's Certificate | `https://www.gov.bm/online-services/permanent-residents-certificate-application` |
| Types of taxes in Bermuda | `https://www.gov.bm/types-taxes-bermuda` |
| Types of work permits | `https://www.gov.bm/types-work-permits` |
| Department of Immigration | `https://www.gov.bm/department/immigration` |
| Vacation Rentals Fact Sheet & Forms | `https://www.gov.bm/vacation-rentals-fact-sheet-and-forms` |
| Planning — hurricane-repair guidelines | `https://planning.gov.bm/index.php/planning-guidelines-for-hurricanes-repairs/` |
| BELCO — Know Your Rate and Bill | `https://belco.bm/know-your-rate-and-bill/` |
| Bermuda Monetary Authority | `https://www.bma.bm/` |
| Bermuda Weather Service | `https://www.weather.bm/` |
| Bermuda Police Service | `https://www.bps.bm/` |
| US National Hurricane Center (Atlantic basin) | `https://www.nhc.noaa.gov/` |
| Climate Central Coastal Risk Screening Tool | `https://coastal.climatecentral.org/` |

---

## Status

**Status**: ✅ fully populated as of 2026-05-28
**Confidence**: MEDIUM —
- **HIGH** for the structural/legal framework: Immigration and Protection Act 1956 Part VI (foreign-buyer protection + anti-fronting), Land Title Registration Act 2011 (LTRO registered title), Stamp Duty Act 1976 as amended 2023, Land Tax framework — all primary-citable; registry = LTRO, court = Supreme Court of Bermuda (independent audit 2026-05-28: VERIFIED primary).
- **HIGH** for the **ARV floors (house $126,000 / condo $25,800)** — primary-sourced to gov.bm Minister Fahy remarks (audit 2026-05-28: VERIFIED primary), **BUT set 1 Jan 2016 — re-verify current floor before relying** (a secondary source's $32,400 condo figure is the superseded pre-2016 level).
- **HIGH** for **Stamp Duty conveyance bands (2.1 / 3.15 / 4.20 / 6.3 / 7.35%)** + adjudication $212 — primary (gov.bm, post-2023 amendment); confirm effective FY.
- **HIGH** for **Land Tax being marginal/banded on ARV** (gov.bm primary), **MEDIUM** on the exact base-row treatment (the live page rendered an ambiguous ~$150 base figure alongside the marginal rows — reconcile + confirm FY at gov.bm/land-tax).
- **HIGH** for **BELCO 2026 residential energy charges** ($0.1370 / $0.2436 / $0.3803 per kWh, effective 1 Jan 2026) + Q1 2026 FAR 13.799¢/kWh (belco.bm primary); facilities-charge dollar amount NOT captured (verify).
- **HIGH** for the **1:1 BMD-USD peg** (BMA).
- **HIGH** for the **"Work From Bermuda" certificate being DISCONTINUED (28 Feb 2025)** (Mondaq + Citizen Remote secondary, cross-consistent) — do NOT present as active.
- **MEDIUM-LOW** for the **Alien Landholding Licence fee percentages (~12.5% / 8% / 6.5% / 6%)** + the **$1,706 application fee** — SECONDARY, cross-consistent across multiple law firms + realtors but **UNVERIFIABLE against a primary gov.bm fee schedule** (independent audit 2026-05-28). **Decision-driving — always tagged "verify at gov.bm Dept of Immigration"; do NOT present as primary fact.**
- **MEDIUM** for area price benchmarks + the ~$1m island average — listing/press-derived (no primary sale-price index; ARV is the only official value Bermuda publishes); cross-check ≥ 3 live listings.
- **MEDIUM** for 2024 crime figures (3,719 crimes, 9 murders — Royal Gazette citing BPS; ~10.9/100k 2021 rate — World Bank/Macrotrends).
- **LOW** for the exact rainwater-tank code spec + the BELCO facilities-charge amount + foreign-buyer mortgage LTV/tenor (not captured on primary; verify).
**Last verified**: 2026-05-28 (ARV valuation-date caveat added 2026-09-18 per Department of Land Valuation)

## Extension TODOs

- [ ] **ARV floors** — re-verify current house/condo floor at gov.bm (last primary-set 1 Jan 2016)
- [ ] **Alien Landholding Licence fee %** — obtain the primary gov.bm Dept of Immigration fee schedule to upgrade the 12.5%/8%/6.5%/6% figures from secondary
- [ ] **ALL application fee** — confirm current $1,706 (and refundability) at gov.bm
- [ ] **Land Tax base-row** — reconcile the ~$150 base figure vs marginal bands + confirm effective FY at gov.bm/land-tax
- [ ] **Stamp Duty bands** — confirm effective FY (post-2023 amendment)
- [ ] **BELCO facilities charge** — capture the residential graduated facilities-charge dollar amount
- [ ] **Rainwater-tank building-code spec** — pull the exact catchment/capacity rule from the planning.gov.bm building code
- [ ] **Residence routes** — confirm current EIC + Permission to Reside thresholds/fees post-Work-From-Bermuda discontinuation
- [ ] **Foreign-buyer mortgage terms** — confirm LTV/tenor/rate with Bermudian lenders
- [ ] **OECD Pillar Two CIT** — scope clarifications for corporate-held real estate
- [ ] **Crime** — track BPS 2025 annual statistics + homicide rate update
- [ ] **One-car-per-household + tourist car-rental rules** — confirm current TCD policy
