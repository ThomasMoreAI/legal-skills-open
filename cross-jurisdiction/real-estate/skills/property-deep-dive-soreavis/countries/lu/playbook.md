# Luxembourg (LU) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: EUR (eurozone founder)
**Lang**: Luxembourgish / French / German official (notary acts most commonly French; sometimes German; occasionally Lëtzebuergesch); **English not an official notarial language**

---

## Country profile

Luxembourg is a small Grand Duchy (~660k pop) with the most expensive property market in Europe at peak (mid-2022; Switzerland/Monaco have since edged ahead). **Sharp 2022-24 correction (~12-15% nominal)**, returned to growth Q1 2025 (+3.7% YoY apartments). Cross-border worker volume = ~228,000 = ~47% of LU workforce (STATEC frontaliers data — verify current quarterly release at STATEC) — but commuters live in FR/DE/BE precisely because LU housing is unaffordable, so they don't pressure rental demand. Bëllegen Akt €40k stamp-duty credit made permanent July 2025. Major tax-base reform (IFON, IMOB, INOL) phased 2026-2030. Cross-border commuter dynamic, trilingual notary-act language reality, and Esch-Belval contamination-legacy zones are key country-specific quirks.

---

## Section: `--price`

**Primary index**: **STATEC HPI** (quarterly)
- https://statistiques.public.lu/en/publications/series/logement-chiffres.html
- Most recent: **Logement en chiffres Q2 2025** at https://statistiques.public.lu/en/publications/series/logement-chiffres/2025/logement-02-25.html

**Trajectory**:
- **Mid-2022 peak → 2024 trough**: nominal residential prices fell roughly **12-15%** (sharpest correction in any EU country during cycle)
- **Q1 2025**: STATEC apartments avg sale price **€8,094/m²**, **+3.7% y/y nominal** — 2nd consecutive quarter of growth after seven down quarters. Inflation-adjusted ~+2% y/y
- **Q1 2025 Luxembourg City** (commune-level, Observatoire de l'Habitat): citywide avg **€12,106/m²** (down ~1% y/y at city level despite national rise — segmentation matters)
- **Top neighbourhoods Q1 2025** (asking prices):
  - **Belair**: €14,489/m² (most expensive)
  - **Limpertsberg**: €13,000–14,000/m² (-5.9% y/y, biggest drop)
  - **Kirchberg**: €12,542/m²
  - **Gasperich/Cloche d'Or**: €12,787/m²
- **Early 2026 outlook** (est., extrapolated from the STATEC Q1/Q2 2025 recovery trajectory above — not an official STATEC forecast): apartments ~+2-4% nominal, new-builds ~+3-6%, houses ~+1-3%

**Observatoire de l'Habitat** (LISER + Min Logement joint): https://logement.public.lu/fr/observatoire-habitat.html — best for sub-commune detail.

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| athome.lu | https://www.athome.lu/ | Dominant aggregator, Mediahuis-owned |
| immotop.lu | https://www.immotop.lu/ | Casa.it/Immobiliare.it group (403 to curl HEAD; loads in browser) |
| wortimmo.lu | https://www.wortimmo.lu/ | Luxemburger Wort newspaper portal — strong upper-mid segment |
| opportunity.lu | https://opportunity.lu/ | Boutique/professional |
| notariat.lu | https://www.notariat.lu/ | Notary chamber auction listings |

**Verdict bands**:
- 🟢 within ±10% of STATEC city/commune segment avg
- 🟡 ±20%
- 🟠 ±30%
- 🔴 >±30% — Belval contamination history? Esch-Alzette fill? Heritage lock?

---

## Section: `--traffic`

- **Administration des ponts et chaussées** road authority
- Real-time CFL/AVL traffic
- OSM Overpass universal

---

## Section: `--tax`

### Transfer tax on purchase (acquisition)

- **Standard total 7%** = **6% droit d'enregistrement + 1% droit de transcription** (statutory basis: **Loi modifiée du 7 août 1920 sur l'enregistrement et la transcription**)
- **LU-Ville surtaxe communale** (mixed-use/commercial only): **+3% (commercial) / +3.6% (mixed-use)** on top of 7% on real-estate mutations in Luxembourg-Ville for mixed-use buildings (e.g. retail-on-ground + apartments above), commercial buildings, offices, garages, and building plots in residential zones where buyer does NOT commit to building a single-family home/apartment building within 5 years. **Purely-residential acquisitions are EXEMPT** (2026-05-27 verified, source: pfi.public.lu / CMS Real Estate Tax Guide LU) — verify with notaire if any commercial element.
- **Bëllegen Akt** ("cheap act") tax credit:
  - Increased from €30k → **€40,000 per natural person** (€80k per couple) by Law 2024
  - Amendment trail: **Loi du 22 mai 2024** (initial 30k→40k temporary); **Loi du 4 avril 2025** (extended temporary window to 30 Jun 2025); **made PERMANENT for deeds executed from 1 July 2025 by Loi du 3 juillet 2025** (project deposited June 2025) (2026-05-27 verified, source: gouvernement.lu / Legilux)
  - At €40k/person, effectively wipes out transfer tax on first ~€570k per buyer (€40k / 7% ≈ €571k). Couple buying ~€1.14M can have zero transfer tax
  - Conditions: principal residence, 2-year occupation requirement, LU-resident OR non-resident — no nationality restriction but must occupy
  - Source: https://guichet.public.lu/en/citoyens/aides/logement-construction/aides-indirectes/credit-impot-actes-notaries.html

### Annual property tax (impôt foncier) — REFORM IN FLIGHT

- **Currently very low** — €100-€500/yr typical for residential, often <€200 in Luxembourg City. Based on 1941 unit values × commune coefficient
- **Reform (Bill 8082A)**:
  - 17 July 2025: 66 amendments accelerating IMOB/IFON
  - **IMOB (vacant-land mobilisation tax) applicable from January 2026** but at **0% for first 5 years** (effectively dormant)
  - **New IFON (revalued land tax) earliest 2026, trial 2029, first real tax year 2030**
  - **INOL (vacant-housing tax) earliest 2028**
- **Practical**: 2026 buyers still pay legacy near-trivial impôt foncier; **budget for a real rise late-decade**

### Capital Gains Tax — corrected from common assumption

- **Principal residence**: fully exempt regardless of holding period or gain — unchanged
- **Other property**:
  - Held **<2 years (speculative)**: full progressive marginal rate up to ~45.78% (incl. solidarity)
  - Held **≥2 years**: half-rate (max **21%** base; **~22.89% all-in** including Employment Fund + dependency-insurance surcharges, per [fiduciaire-expert.lu](https://fiduciaire-expert.lu/fr/articles/plus-values-immobilieres/)) (2026-05-27 verified)
  - **Quarter-rate window (10.5%, 1/4 of 42%)** applied to gains realised **1 Jan 2024 → 30 Jun 2025**, with transitional rule allowing the rate where a compromis was signed/registered by 30 Jun 2025 AND notarial act executed by **30 Sept 2025**; both expired post-30 Sept 2025 (2026-05-27 verified, source: impotsdirects.public.lu / fiduciaire-expert.lu)
- **CORRECTION**: LU uses 2-year (not 10-year) speculative threshold. >2yr → half-rate. **No automatic exoneration after 10 years — that's the French rule.**

### Rental income

- **Progressive personal rate** — 8% from €13,230 up to **42% above €234,870** + Employment Fund Surcharge (7%/9% high earners) → effective top ~45.78%
- Standard expenses deductible (mortgage interest, repairs, management, depreciation)

### Mortgage interest deductibility (major 2024 change)

- **Properties available after 31 Dec 2023**: **NO CAP** on mortgage interest deduction against rental or principal-residence income
- Pre-2024 properties remain on tiered per-household-member caps
- Trigger date is **availability** (habitable date), not move-in

### VAT new-build / renovation

- Standard 17%
- **Super-reduced 3%** for principal residence (new-build OR renovation), capped at **€50,000 of tax advantage per dwelling**, habitable surface ≤ 400 m² (excess at 17%)
- **Pre-approval from AED required before works start**
- **Clawback** (with statutory interest) if property not used as principal residence for at least 2 years from 1 Jan following completion
- Investment property / second home: **full 17%**, no super-reduced
- Source: https://pfi.public.lu/fr/citoyen/tva/logement/application-directe-taux-3.html

---

## Section: `--rental`

### STR / Airbnb (2025 reform)

- **Law of 28 February 2025** in force from **1 September 2025** formalises STR registration:
  - All providers must keep local guest record (traveller-form obligation, hotel-style)
  - Future national reference number issued by Ministry; must appear in listings
- **Zoning split**:
  - Residential zone 1 → **max 89 nights/yr**
  - Mixed-use & commercial zones can go higher with proper permit
- **>90 overnight stays/yr threshold** (since 1 Sept 2023): requires **business permit (autorisation d'établissement)** + accelerated training
- **Tourist tax**: per-night, commune-set
- **Luxembourg City**: aligned with national rules; commune declaration mandatory

---

## Section: `--work=<profession>`

EU-quarter institutional staff (Kirchberg), finance (Place Financière), tech (Esch-Belval). Cross-border commute tradition: large daily inflow from FR-Lorraine/DE-Saarland/BE-Luxembourg-province.

---

## Section: `--risks`

### Flood

- **`map.geoportail.lu/theme/eau`** (200) — official flood-zone & flood-risk maps (10/100/extreme return)
- **`inondations.lu`** (200) — operational flood-forecasting + real-time gauge data
- **Highest-exposure rivers**: **Moselle** (Grevenmacher, Remich, Schengen — wine country), **Sûre** (Diekirch, Echternach, Ettelbruck), **Alzette** (Esch-sur-Alzette, Mersch, Pétrusse/Alzette confluence in Luxembourg-Ville Grund/Clausen — high tourist-rental exposure)
- July 2021 flood (regional) caused major damage Alzette + Sûre valleys; 100-yr maps redrawn 2019

### Seismic
- Hazard **very low**. PGA ~0.39 m/s² peak. ~37 quakes/yr; M≥4 every 5-10yr
- Trier-Luxemburg fault traverses but is not a major active source
- Eurocode 8 still applies for new builds — flag for post-2010 construction

### Industrial legacy / contaminated land — important

- **South (Minette region)**: est. ~1,200 hectares of brownfield from steel-industry collapse 1970s-90s (verify against the CASIPO contaminated-sites inventory, below)
- **Esch-Belval**: flagship reconversion (est. ~€1.9bn state investment — verify against Fonds Belval / state budget figures) — University, Rockhal, Cité des Sciences, mixed residential. **Some Belval residential is on remediated/sealed industrial fill** — check **certificat de pollution** / soil report from notaire. Blower Hall closed 2019 for contamination/structural reasons
- **St. Esprit Plateau (Esch)**: served as central landfill — sealed and reshaped
- **Min of Environment** operates **CASIPO** contaminated-sites inventory — surface this as explicit checklist for any Esch / Differdange / Dudelange / Schifflange purchase

### Mandatory diagnostics

- **Passeport énergétique / CPE / Energiepass**: mandatory for sale, rental, new construction, extension, transformation. Must exist **before publishing any listing** — **fines reportedly up to ~€24,789 for advertising without one** (statutory amount is index-linked — verify current figure in the governing CPE règlement / with the Ministry of Energy). Validity 10 years. Classes A+ to I. Since 2024, banks weight class in mortgage decisions
- **Radon**: national reference 300 Bq/m³ (homes & workplaces). National avg ~50 south, ~150 north (granite-influenced Oesling/Ardennes higher). Per-commune map at https://map.geoportail.lu/communes/Luxembourg/carte_radon_communes/. **Not yet a mandatory transaction-time diagnostic** like FR ERP — advisory only
- **No mandated termite/asbestos certificate** at national level for individual residential transactions (asbestos governed by waste/work-safety regs at renovation time, not point-of-sale)

---

## Section: `--mains`

### Cadastre + Land Registry — SPLIT

- **ACT (Administration du Cadastre et de la Topographie)** runs the cadastral plan. https://act.public.lu/
- **Geoportail**: https://geoportail.lu/ — citizen-friendly map viewer with cadastral overlay, flood, radon, PAG (commune zoning) layers
- **AED (Administration de l'Enregistrement, des Domaines et de la TVA)** runs **Bureaux des hypothèques** (mortgage offices = transcription/inscription registers, ownership chain, charges). NOT under ACT. https://pfi.public.lu/
- **Public access to ownership data**: anyone (resident or non-resident) can request a copy of a transcribed act at the competent bureau des hypothèques. Two-step: (1) request "état des inscriptions" against named person, (2) request copies of specific acts. **Paid service**, not free online lookup
- **Direct online register consultation** restricted to professionals (notaries, network operators) on contract; private buyers go through their notaire
- **Buyers cannot self-serve title search** the way they can in UK — instruct the notaire, who pulls the état hypothécaire as part of deed prep

### Utilities

- **Electricity grid**: **Creos Luxembourg** (DSO) — Encevo group. Single national DSO ~95% of country
- **Gas**: also Creos for distribution. Supply contestable but Encevo-affiliated dominant
- **Sudenergie** (south-region, Esch + surrounding communes)
- **Water**: **municipal syndicates** — SEBES (treated water from upper Sûre lake), DEA (commune-level), commune water utilities. Rates set commune-by-commune
- **Wastewater**: SIDEN, SIDERO, SIVEC — connection fees can be material on rural/new-build plots
- **District heating**: **LuxEnergie** in Kirchberg, Cloche d'Or, Belval, Esch — relevant for any apartment on those grids (network connection mandatory in some PAP-NQ zones). Outside these, gas + heat-pump combinations dominant; oil being phased out
- **Internet/fibre**: **POST Luxembourg** incumbent; near-universal FTTH coverage by 2025

---

## Section: `--crime`

See `shared/crime-sources.md`. Luxembourg uses:
- **Police Grand-Ducale**: https://police.public.lu/
- STATEC criminality data

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

---

## Cost benchmarks (Apr 2026)

| Item | Range / typical |
|---|---|
| LU-City Belair €/m² | ~€14,500 (most expensive) |
| LU-City overall €/m² | ~€12,100 (Q1 2025) |
| National apartments avg | ~€8,100 (Q1 2025) |
| Esch-Belval entry €/m² | ~€7,000–9,500 |
| Transfer tax effective (with Bëllegen Akt €40k) | 0% on first ~€570k (per person) |
| Notaire fees | ~1–1.5% (regulated by Grand-Ducal règlement) |
| Total acquisition costs | ~7% standard - Bëllegen Akt credit |

---

## Active fiscal incentives (Apr 2026)

- **Bëllegen Akt €40k credit per person** (permanent since 1 July 2025) on transfer tax for principal residence
- **VAT 3% super-reduced** on principal residence new-build/renovation (cap €50k advantage, ≤400 m²)
- **Mortgage interest uncapped** for properties available post-31 Dec 2023
- **PIT scale 2.5 index brackets** added (inflation neutralisation, TY 2025)

---

## Foreign-buyer rules

- **No nationality restrictions whatsoever** — EU and non-EU treated identically for ownership rights
- **No quotas, no preapproval, no foreign-buyer surcharge.** Same 7% transfer tax, same Bëllegen Akt eligibility (subject to occupation conditions)
- **Mortgage practice (lender-imposed, not legal)**:
  - EU non-resident: lenders typically demand 20-30% deposit
  - Non-EU buyer: 30-40% deposit, often plus LU-domiciled income evidence
  - Local mortgage rates trail ECB; tightened sharply 2022-23, easing 2024-25

---

## Country-specific quirks

- **Cross-border worker volume**: ~228,000 (~47% of LU workforce). FR ~53.6%, DE ~23.4%, BE ~23% (STATEC frontaliers split — figures may have shifted; verify current quarterly release at STATEC). **Implication**: rental market is LU-resident-only (commuters can't rent here cheaply enough to bother), but sale demand has tail-wind from anyone whose situation flips from commuter to resident. Conversely, rental yields are squeezed because high-income tenants frequently pivot to buying. **Pressure on LU property prices comes from in-country residents and EU/finance new arrivals, not from commuters reverse-pressuring the market**
- **Trilingual notary acts** (clarification): Acts drafted in **one** of LU's official languages, most often French, sometimes German, occasionally Lëtzebuergesch. **NOT literally trilingual on the page.** English is not an official notarial language. Foreign buyers without French/German need an interpreter (€200-900) — strongly advised
- **SCI / SARL ownership**: SCI transparent for tax (partner-level, like France). SARL minimum capital €12,500, week to register, separate corporate income (~24-27% effective). For rental investment, SARL/SA can win on capital-gains rate vs personal but loses Bëllegen Akt and principal-residence CGT exemption. SCS/SCSp common for institutional. Personal ownership default for principal residence
- **Kirchberg EU-quarter premium**: ~€12,500/m² but tenant pool institutional (EU staff); lease cycles tied to EU staff rotations (3-5yr typical)
- **Echternach / Vianden / Müllerthal**: rural / tourism-coded, lower €/m² (~€4,500-6,000), STR potential constrained by 89-night zone rule. Heritage rules in Vianden castle precincts
- **Esch-sur-Alzette / Belval**: cheaper entry but contamination/remediation history matters; commuter-belt for cross-border French (Thionville/Metz line)
- **PAP / PAG / PAP-NQ zoning**: every commune has Plan d'Aménagement Général (PAG) and project-level Plans d'Aménagement Particulier (PAP). PAP-NQ ("nouveau quartier") triggers special affordable-housing quota (≥10%). **Always pull on geoportail.lu PAG layer before committing**
- **Notaire fees on top of taxes**: ~1-1.5% of price, regulated by Grand-Ducal règlement. https://notaryfees.lu/ provides calculator
- **No private mortgages / Notarisation mandatory**: all real-estate sales pass before a notaire — non-notarial private deeds not enforceable against third parties
- **Compromis de vente**: usually signed before notarial act, with 10% deposit standard. Cooling-off period less generous than French "loi SRU" 10-day right

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre | ACT | https://act.public.lu/ |
| Geoportail | nat'l SDI | https://geoportail.lu/ |
| Hypothèques (mortgage office) | AED | https://pfi.public.lu/ |
| Citizen services hub | guichet | https://guichet.public.lu/ |
| Notaires | Notariat | https://www.notariat.lu/ |
| Notary fee calculator | notaryfees.lu | https://notaryfees.lu/ |
| Min Logement (Observatoire) | Logement | https://logement.public.lu/ |
| STATEC | Statistics | https://statistiques.public.lu/ |
| Pacte Logement portal | govt | https://pactelogement.lu/fr |
| Inondations forecast | gov | https://www.inondations.lu/ |
| Radon (Santé Sécu) | health | https://santesecu.public.lu/fr/espace-citoyen/departement-sante/rayonnements-et-radioprotection/radon/ |

---

## Source URL templates

| Field | Template |
|---|---|
| Bëllegen Akt | https://guichet.public.lu/en/citoyens/aides/logement-construction/aides-indirectes/credit-impot-actes-notaries.html |
| Impôt foncier | https://guichet.public.lu/en/citoyens/fiscalite/immobilier/impots-taxes-plus-value/impot-foncier.html |
| CPE / Energiepass | https://guichet.public.lu/fr/citoyens/logement/construction-renovation-transformation/certificats-energiepass/demande-passeport-energetique.html |
| VAT 3% direct | https://pfi.public.lu/fr/citoyen/tva/logement/application-directe-taux-3.html |
| Property reform dossier | https://maint.gouvernement.lu/en/dossiers/2022/impot-foncier.html |
| Flood maps | https://eau.gouvernement.lu/fr/domaines-activite/inondations/cartes-des-zones-inondables-et-cartes-des-risques-dinondation.html |
| Radon commune map | https://map.geoportail.lu/communes/Luxembourg/carte_radon_communes/?lang=fr |

---

## Status

**Confidence**: HIGH on STATEC Q1 2025 prices, Bëllegen Akt €40k permanent (June 2025 verified), 7% transfer-tax structure, CGT 2-year speculative + half-rate post-2yr (PwC verified). MEDIUM on per-commune impôt foncier amounts (commune coefficients exist but no consolidated public table — say "consult notaire"), exact post-30-Jun-2025 CGT mechanics for properties straddling temporary regime (verify with adviser if H2 2025 sale). LOW on per-Belair/Limpertsberg/Kirchberg rents (no STATEC-grade source verified to early 2026 — cite Observatoire de l'Habitat by name and let user pull current quarter).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)

---

## Extension TODOs

- IFON 2030 first-real-tax-year tracker (Bill 8082A amendments may shift)
- Esch-Belval contamination per-plot history (link to CASIPO inventory)
- Cross-border worker pivot-to-resident demand model (driving long-term price floor)
