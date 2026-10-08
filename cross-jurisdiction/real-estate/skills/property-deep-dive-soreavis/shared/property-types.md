# Specialized Property Type Templates — `--type=<kind>`

Different property types need different due-diligence emphasis. The standard 9-section run is calibrated for "resale of an existing residential property". Specialized types overlay additional checks specific to the type.

## Available types

| Type | Use when |
|---|---|
| `off-plan` | New build / VEFA / VPF / off-plan / under construction |
| `auction` | Auction property (forced sale, judicial, bank repo) |
| `probate` | Estate / probate / succession sale |
| `plot-only` | Land only — buildability check needed |
| `heritage` | Listed / heritage / monument-classified property |
| `apartment` | Flat / condo / apartment in multi-unit building |
| `house` | Single-family detached or semi-detached |
| `mixed` | Mixed-use (residential + commercial) |
| `agricultural` | Farm / vineyard / agricultural with residence |
| `coastal` | Coastal / second-home / leisure property |
| `commercial` | Pure commercial (out of skill scope — flag) |

Combine: `/property-deep-dive <addr> --all --type=off-plan --journey=foreign-buyer`

---

## 1. Off-plan / new build

### Additional checks beyond standard

#### Developer due diligence

- **Companies House / RCS / KBIS / Handelsregister lookup** — incorporation date, capital, directors
- **Past project portfolio** — completed builds, on-time, quality, snagging
- **Court records** — past disputes / liquidation / liens
- **Online reviews** — buyer feedback, snagging community
- **Site visit** — existing-phase quality (if multi-phase)

#### Contract critical terms

- **Milestone payment schedule** — typical:
  - 5% reservation
  - 10-25% on signature
  - 25-30% foundation poured
  - 25-30% roof on (mise hors d'eau)
  - 25-30% completion (livraison)
  - 5% snagging hold-back
- **Late delivery penalties** (FR pénalités de retard, IT penalità per ritardo)
- **Buyer cancellation rights** — typically 10-day cooling-off
- **Specifications** (cahier des charges / Baubeschreibung) — what's included
- **Variations / extras** — pricing for changes
- **Defect period** — typically 1-2 years post-delivery

#### Insurance / guarantees by country

| Country | Required guarantees |
|---|---|
| 🇫🇷 | Garantie d'achèvement (GFA) - mandatory; Garantie biennale (2yr); Garantie décennale (10yr) |
| 🇮🇹 | Polizza fideiussoria mandatory; Garanzia decennale postuma (10yr) |
| 🇩🇪 | Bauträgerversicherung (insolvency cover); Gewährleistung 5yr (defects) |
| 🇪🇸 | Aval bancario or seguro de caución; Decenal (10yr); Trienal (3yr) |
| 🇵🇹 | Garantia 5yr (structural) + 2yr (other) |
| 🇨🇭 | SIA Norm 118 + Bauversicherung |
| 🇬🇧 | NHBC Buildmark or LABC warranty (10yr) |
| 🇮🇪 | Homebond or Premier Guarantee (10yr) |

#### EU: the guarantee now also drives the mortgage (from 12 Aug 2026)

[Commission Delegated Regulation (EU) 2026/849](https://eur-lex.europa.eu/eli/reg_del/2026/849/oj/eng) of 16 April 2026 (OJ L, 2026/849, 23.7.2026 — applies **12 Aug 2026**) sets what counts as an *equivalent legal mechanism* under CRR art. 124(3)(a)(iii)(2), i.e. when an EU lender may treat a property still under construction under the preferential immovable-property risk weight. **Nothing here is a buyer obligation** — it is a bank capital rule — but it decides how cheaply, and whether, the off-plan purchase can be mortgaged. Conditions in art. 1 include: the completion guarantee is **required by the law of the member state where the property is built** (2); the guarantee runs until completion and is in writing (3, 8); the protection provider is a **credit institution or an insurance undertaking** (4) and does **not belong to the lender's group** (5); activation is **timely and unconditional**, and the developer's own default cannot block it (10); where the building holds several units, **one single guarantee covers all of them** (9).

Ask the lender early, since it changes the offer, not the contract: is the national guarantee scheme accepted for preferential treatment on this specific build? Whether a given scheme meets all of art. 1(2)–(13) is the lender's assessment — treat "our guarantee qualifies" as a claim to verify with the bank, not a given.

#### Red flags specific to off-plan

- 🔴 **No completion guarantee** — walk away
- 🔴 **Developer < 3 years incorporated, no past projects**
- 🔴 **Cash-flow-funded** (no construction loan) — high insolvency risk
- 🔴 **Site stalled** for >3 months — financial issues
- 🔴 **Off-plan deposit > 25%** before construction starts → too much risk
- 🔴 **Promised features ("granite countertops") not in cahier des charges**

### Output add-on

```markdown
### Off-plan Specific

**Developer**: <name>
**Companies-house ID**: <X>
**Incorporated**: <date> · **Past projects**: <N> · **Reviews**: <average>

#### Project status
- Phase: <foundation / structure / finishes / completion>
- On schedule: <yes / X-month delay>
- Site visit: <date> — observations <…>

#### Contract
- Milestone schedule: <align with country standard?>
- Late delivery clause: €<X>/day after <date>
- Cancellation: <terms>

#### Guarantees
- ✅/❌ Completion guarantee (GFA / polizza / NHBC)
- ✅/❌ Decennial (10yr structural)
- ✅/❌ Defect period (1-2 yr)
- ✅/❌ Insolvency insurance

#### Verdict
- 🟢 Strong developer + full guarantees + on schedule
- 🟡 Minor delays or guarantees-light
- 🟠 Developer track record concerns
- 🔴 Insolvency risk OR missing completion guarantee
```

---

## 2. Auction property

### Context

- **Time pressure**: typical 2-21 days from listing to bid
- **No reps & warranties**: "as-is, where-is"
- **Reserve vs guide price**: guide may be marketing, reserve is what seller accepts
- **Buyer's premium**: typically 5-15% on top of hammer price
- **Possession**: vacant or tenanted (huge price difference)
- **Why sold at auction**: forced sale, divorce, bank repo, probate, title issues

### Pre-bid checklist

- [ ] **Title pack review** — typically published 1-2 weeks before
- [ ] **Independent solicitor review** of legal pack — non-negotiable
- [ ] **Pre-bid surveys** — at buyer's expense; rapid turnaround needed
- [ ] **Special conditions** (auction-specific) — e.g., 28-day completion vs 14
- [ ] **Vacant possession proven** — eviction status if tenanted
- [ ] **Encumbrances disclosed** — mortgage discharged at sale?
- [ ] **Search results in legal pack** — local, drainage, environmental, planning
- [ ] **Mortgage in principle** if not cash buyer (banks slow on auctions)
- [ ] **Chain of title clear**

### Common auction property issues

| Issue | Impact |
|---|---|
| Title defect (missing deed link) | Unsellable until fixed (months/years) |
| Adverse possession claim | Litigation risk |
| Unregistered land (UK) | Title fraud risk |
| Sitting tenant | Rent < market + can't evict easily |
| Squatters | Possession action needed |
| Outstanding mortgage > sale price | Need lender approval |
| Restrictive covenants | Limit use / development |
| Unknown easements | Right of way, light, etc. |
| Building defects (structural) | "As-is" — buyer absorbs |
| Pyrite / mica (IE) | DCBS possible but limited |
| Listed status not disclosed | Restoration obligations |
| Pre-emption rights (FR mairie, SE kommun, FR SAFER) | Could be exercised within 60-90 days |

### Output add-on

```markdown
### Auction Specific

**Auction**: <house>
**Auction date**: <date>
**Guide price**: €<X>
**Reserve**: <hidden / disclosed>
**Buyer's premium**: <%>
**Estimated completion timeline**: <14 / 28 days>
**Days to bid**: <N>

#### Why at auction (research)
<probate / repo / divorce / quick sale>

#### Legal pack review
- Title clean: ✅ / ❌
- Possession: vacant / tenanted (<term>)
- Encumbrances: <list>
- Special conditions: <list>
- Searches included: <list>

#### Pre-bid budget
- Independent solicitor: €<X>
- Survey: €<X>
- Searches: €<X>
- Insurance quote: €<X> (must be in place at completion)

#### Bidding ceiling
- Guide price: €<X>
- + Buyer's premium: €<Y>
- + Stamp duty / transfer: €<Z>
- + Estimated repair / clean-up: €<R>
- + Pre-emption risk: <not exercisable / 90 days>
- **Walkaway bid ceiling**: €<X+Y+Z+R - margin>

#### Verdict
- 🟢 Clean title + vacant + good guide → bid
- 🟡 Acceptable but tight margin
- 🟠 Multiple concerns; need premium discount
- 🔴 Title defect / adverse claim / large unknown
```

---

## 3. Probate / estate

### Specifics

- **Multiple owners** post-death (heirs in indivision / comunione / sukcesion)
- **Forced heirship** countries (FR/IT/ES/CH/PL): protected shares
- **All heirs must consent** to sale → one objector = no sale
- **Probate timeline**: 6-24 months
- **Estate frozen** during probate — no transfers
- **CGT recalculation** — basis is date-of-death value (step-up)
- **Inheritance tax** filed before sale in some jurisdictions

### Pre-purchase checks

- [ ] **All heirs identified** — genealogist if family tree unclear
- [ ] **All heirs sign** sale authorization (acte de mandat / vollmacht)
- [ ] **Probate complete** (or specific authorization to sell during probate)
- [ ] **No pending heir claims** (e.g., disinherited child suit)
- [ ] **Inheritance tax paid or contracted** by estate
- [ ] **Death certificate in legal pack**
- [ ] **Forced-heirship calculations correct**

### Common probate issues

| Issue | Impact |
|---|---|
| Indivision / comunione | One heir blocks → impasse |
| Disinherited child suit (FR action en réduction) | Sale void if successful |
| Foreign heir (cross-border) | Brussels IV applies, but adds complexity |
| Heir without ID / contact | Genealogist hunt; can take years |
| Tax owed by estate exceeding assets | Sale proceeds clawed back |
| Lifetime gift (donation) within 15 years | Reduce reserved share |
| Pre-deceased heir with descendants | Per stirpes division |

### Output add-on

```markdown
### Probate / Estate Specific

**Decedent**: <name (year of death)>
**Heirs**: <N> people, <list>
**Forced heirship**: ✅/❌ (jurisdiction)
**Probate status**: <opened / pending / closed>
**Estate tax filed**: <yes / no / pending>

#### Sale authorization
- All heirs identified: ✅/❌
- All heirs consenting: ✅/❌
- Genealogist required: <yes / no>
- Forced-share calculations validated: ✅/❌
- Pending litigation: <list>

#### Risks
- Indivision / co-ownership block: <low / med / high>
- Heir contesting: <low / med / high>
- Cross-border complications: <low / med / high>
- Pre-emption right exercise: <jurisdiction-specific>

#### Pre-purchase asks
- Power of attorney from all heirs (if remote)
- Apostille on cross-border heir signatures
- Notarial certification of forced-share calculation
- Confirmed estate-tax payment

#### Verdict
- 🟢 Probate closed, all heirs consenting, clean
- 🟡 Probate active but consensus among heirs
- 🟠 1+ heir holding back, negotiation needed
- 🔴 Litigation pending, indivision impasse
```

---

## 4. Plot-only (buildable land)

### Buildability checklist

- [ ] **Zoning** (PLU/PLUi/Bauleitplan/Piano Regolatore) — residential / mixed / agricultural
- [ ] **Constructability** — set-back, height, footprint, FAR (floor-area ratio)
- [ ] **Coefficient d'occupation des sols** (FR) / Geschossflächenzahl (DE) / similar
- [ ] **Building permit history** — has anything been refused? Why?
- [ ] **Survey** (bornage / Vermessung) — exact boundaries
- [ ] **Soil study** (étude G2 / Bodengutachten) — bearing, drainage, contamination
- [ ] **Utility connections**:
  - Water (public / well)
  - Sewer (mains / septic permit obtainable)
  - Electricity (3-phase / amperage)
  - Gas (mains available?)
  - Fiber / broadband
- [ ] **Access** — public road frontage / easement?
- [ ] **Servitudes** (right of way, electricity line, gas)
- [ ] **Pre-emption right** (mairie / SAFER / kommune)
- [ ] **Flood / landslide / seismic / fire zone**
- [ ] **Existing trees protected** (heritage tree / Natura 2000)
- [ ] **Archaeology** (e.g., FR archéologie préventive — costly redo)
- [ ] **Heritage designation** affecting buildability
- [ ] **CO2 / SDC** (development charges) per country

### Country-specific zoning lookups

| Country | URL pattern |
|---|---|
| 🇫🇷 | PLU per commune; cadastre + SIG locaux |
| 🇮🇹 | PRG/PGT per comune |
| 🇩🇪 | Bauleitplan / B-Plan per Gemeinde |
| 🇪🇸 | Plan General de Ordenación Urbana (PGOU) per municipio |
| 🇬🇧 | Local Plan + Planning Portal `https://www.planningportal.co.uk/` |
| 🇮🇪 | County Development Plan + `https://www.myplan.ie/` |
| 🇵🇹 | PDM Plano Diretor Municipal |
| 🇨🇭 | Zonenplan per Gemeinde |
| 🇦🇹 | Flächenwidmungsplan per Gemeinde |
| 🇸🇪 | Detaljplan per kommun |

### Output add-on

```markdown
### Plot-only Specific

**Plot area**: <m²>
**Zoning**: <residential / mixed / agricultural>
**Buildable footprint**: <m² × FAR>
**Max height**: <m / floors>
**Set-back from boundaries**: <m>

#### Buildability
- Building permit grantable: <high / med / low likelihood>
- Past refusals on this plot: <none / Y reason>
- Special restrictions: <heritage / Natura 2000 / coastal protection>

#### Utilities (km to nearest connection)
- Water mains: <0 / X km>
- Sewer: <0 / X km / septic only>
- Electricity: <connection cost €<X>>
- Gas: <available / not>
- Fiber: <available / not>

#### Soil
- Bearing capacity: <good / poor / requires special foundation>
- Drainage: <good / poor>
- Contamination check: ✅/❌ done
- Archaeology pre-emption: ✅/❌

#### Total cost to make buildable (beyond purchase)
- Soil study: €<X>
- Survey / bornage: €<X>
- Utility connections: €<X>
- Driveway / access: €<X>
- Permits + fees: €<X>
- **Subtotal pre-construction**: €<X>

#### Verdict
- 🟢 Permitted use, clean, all utilities available
- 🟡 Buildable but utility extension needed
- 🟠 Restricted use OR significant pre-construction cost
- 🔴 Effectively non-buildable OR archaeology / heritage block
```

### Landlocked-parcel / access-servitude / right-of-way check

**Fold-in target**: `--type=plot-only`.

A plot or rural parcel can look perfect on a map and still be **legally enclosed** (*enclavé / encravado / enclavada / Notlage*): no frontage on a public road and no **deeded** right of way across the neighbouring land it is reached through. Foreign buyers consistently mistake a *physical* track — a farm lane, a shared drive, a long-used dirt path — for a *legal* access right. It is not. A used-but-undeeded track can be closed by a new neighbour, sold off, or gated, and the buyer is then dependent on a statutory servitude-of-necessity claim that is **compensated, litigated, and slow** — not automatic. Every civil-law family and the common-law world codify a fallback access right for a truly enclosed parcel, but the fallback is a *lawsuit*, not a *title*. The pre-offer job is to confirm access is **already registered against the servient parcel**, not merely claimable.

#### Codified access-servitude by legal family

**Napoleonic / Latin family** — statutory *servitude de passage pour cause d'enclave*, compensated, route = shortest to public road but least damaging to the burdened land:

- **France** — Code civil **Art. 682** (right to a sufficient passage where access to the public road is absent or insufficient, against indemnity). **Art. 685-1**: the servitude extinguishes if the enclave ceases; the location/manner can be fixed by 30 years' continuous use. Precisely: the location/manner of the enclave servitude can be acquired by **30 years' continuous use** (Art. 685-1), *not* the general 30-year *prescription acquisitive* of the underlying right of passage — Art. 682's right itself is imprescriptible while the enclave subsists; only its *assiette* (route/mode) is set by 30-year usage. Source: [Légifrance Art. 682](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006430276) · [Art. 685-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006430309).
- **Spain** — Código Civil **Art. 564** (*servidumbre de paso forzoso*): owner of a finca enclosed among others' land and with no exit to a public road may demand passage against prior indemnity; *necesidad* is the operative test (TS doctrine), route least damaging to the servient predio. Arts. 564–570 regulate the regime. Source: [CC Arts. 564 ff. — noticias.juridicas](https://noticias.juridicas.com/base_datos/Privado/cc.l2t7.html).
- **Italy** — Codice Civile **Art. 1051** (*passaggio coattivo*): owner whose land is surrounded and has no access to a public road, nor can obtain it without excessive expense/inconvenience, has the right to passage over neighbouring land; passage fixed where access is shortest and damage least. Source: [Brocardi Art. 1051](https://www.brocardi.it/codice-civile/libro-terzo/titolo-vi/capo-ii/sezione-iv/art1051.html).
- **Portugal** — Código Civil **Art. 1550** (*servidão legal de passagem em benefício de prédio encravado*): owners of land with no, or insufficient, communication to the public road may compel a passage servitude over neighbouring rural land. **Art. 1553** fixes the location (least-prejudicial parcel, least-inconvenient mode/place). Source: [CC Art. 1550 — informador.pt](https://informador.pt/legislacao/lexit/codigos/direito-civil/codigo-civil/livro-iii-direito-das-coisas/titulo-vi-das-servidoes-prediais/subtitulo-iv-do-exercicio-e-tutela-dos-direitos-9/capitulo-iii-servidoes-legais/seccao-i-servidoes-legais-de-passagem/artigo-1550-o-servidao-em-beneficio-de-predio-encravado/).
- **Latin-American codes** mirror the French/Spanish article verbatim or near-verbatim (e.g. derecho/servidumbre de paso for *predio enclavado*). Cite the **local code article** in the country playbook — do not assume the FR/ES number transfers; verify against the national civil code text. Latin-American article numbers are **not** assumed to equal FR Art. 682 / ES Art. 564 — the playbook must cite the **national civil code's** own article; this fold-in deliberately does not assert a specific LATAM number.

**Germanic family** — *Notweg / Notwegrecht*, court-fixed direction and scope, monetary annuity (*Geldrente*) not lump sum:

- **Germany** — BGB **§ 917** (*Notweg*): if a parcel lacks the connection to a public way necessary for proper use, the owner may demand neighbours tolerate use until access is created; direction and scope fixed by court if needed; neighbours compensated by a money rent (§ 917(2)). Source: [§ 917 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__917.html).
- **Switzerland** — ZGB **Art. 694** (*Notweg*): owner without sufficient access from his land to a public road may claim a right of way from neighbours against full compensation, directed first at the most reasonable neighbour by prior ownership/access, then at whoever suffers least. Source: [ZGB Art. 694 — kisos.ch](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de).
- **Austria** — **Notwegegesetz** (RGBl. 1896, substantially unchanged; access granted by court, extensive case law on social-change adaptation). Verify current consolidated text at [RIS — Bundesrecht](https://www.ris.bka.gv.at/).

**Common-law world** — no automatic statutory servitude; access is a *property interest* that must be **expressly granted, implied, or prescriptively acquired**, and (under registered title) **noted on the register**:

- **Easement of necessity** — implied only where a conveyance of part leaves a parcel with *no legally enforceable access at all* (strict necessity, narrowly construed). Anchor instrument across UK/IE/US/CA/AU/NZ.
- **Implied grant — rule in *Wheeldon v Burrows* (1879) 12 ChD 31**: on a sale of part, the buyer takes quasi-easements that were *continuous and apparent*, *necessary for reasonable enjoyment*, and used by the vendor at the time of the grant. *Wheeldon v Burrows* is **grant-only** — it does *not* reserve access for a vendor's retained land: a vendor selling the road-fronting part and keeping the rear plot must **expressly reserve** access or the retained rear plot is left enclosed (a recurring trap in subdivided/lotted rural sales). Source: [Wheeldon v Burrows — Wikipedia](https://en.wikipedia.org/wiki/Wheeldon_v_Burrows).
- **Prescriptive easement** — long uninterrupted use (period varies by jurisdiction) as of right; evidentiary, not on the register until established/registered.
- **Registered / Torrens right of way** — the only access form a buyer can rely on at offer stage: an easement/right-of-way registered against both the dominant and servient titles; the burden *runs with the land*. Caveat: Torrens "indefeasibility" is **not absolute for easements** — an *unregistered* easement (by necessity, prescription, or statute) can still bind a Torrens parcel; a clean register face is **necessary but not sufficient**, so the surveyor step and a local-counsel encumbrance review remain required. Source: [Torrens title — Wikipedia](https://en.wikipedia.org/wiki/Torrens_title); [Easement — Wikipedia](https://en.wikipedia.org/wiki/Easement).

#### Pre-offer verification path

Run this *before* any offer on a plot/rural parcel reached via land you will not own. Do not rely on the listing, the agent's map, or a visible track.

1. **Cadastre / land-registry access record.** Pull the official parcel extract (FR: *plan cadastral* + *matrice* via [cadastre.gouv.fr](https://www.cadastre.gouv.fr/); ES: *Catastro* + *nota simple* from *Registro de la Propiedad*; IT: *visura catastale*; PT: *certidão predial* from *Conservatória do Registo Predial*; DE: *Grundbuch* extract; common-law/Torrens: official title register + plan). Confirm whether the parcel **fronts a public road** at all. If it does not, it is presumptively enclosed.
2. **Registered easement / servitude entry.** On the **servient** parcel(s) the access crosses, check the *charges / encumbrances* section for a recorded right of way naming this parcel as dominant tenement (FR: servitude conventionnelle in the *acte* + Service de publicité foncière; DE: *Grunddienstbarkeit* in Grundbuch Abt. II; Torrens: easement instrument number on both titles). **No entry = no deeded access**; a statutory servitude-of-necessity exists only as a *claim to be litigated*, not a present right.
3. **Surveyor / géomètre confirmation.** Commission a licensed surveyor (FR *géomètre-expert*, ES/PT *topógrafo*, DE *öffentlich bestellter Vermessungsingenieur*, common-law registered/licensed surveyor) to physically locate the access corridor, confirm it matches the registered route and width, and flag mismatch between deeded line and used track. The used track is frequently *not* where the registered easement runs.
4. **Compel-access litigation route + cost band.** If no registered access exists, price the statutory-servitude action *before* offering, treat it as a condition, and discount accordingly:
   - **Civil-law (FR/ES/IT/PT/DE/CH/AT)**: an action to establish the servitude (FR *tribunal judiciaire*; ES *juicio ordinario*; DE Zivilgericht) plus a court-set indemnity/annuity to the servient owner and a surveyor's report. `est.` cost band typically **€5,000–€20,000+ in legal/expert fees**, **12–36 months**, hostile-neighbour cases at the high end — *verify with a local notaire/abogado/Rechtsanwalt for the specific jurisdiction and parcel; figures are an order-of-magnitude calibration, not a quote.*
   - **Common-law**: declaratory action / easement-by-necessity or prescription claim; cost and timeline jurisdiction-dependent; obtain a written quote from a local property litigator before offer.
   - In all cases: a parcel whose only access is an *unlitigated statutory claim* should be valued as **landlocked until access is registered**, not as if access exists. Make registration of a deeded right of way a **condition precedent** in the offer, or walk. Cost/timeline bands here are **`est.` order-of-magnitude calibration only**, explicitly flagged for local-counsel verification — not sourced quotes.

---

### Connect-from-scratch utilities (raw plot / rural new-build)

*Distinct from `--mains` (an existing dwelling's utility reliability/quality) and from the access/right-of-way sub-block (legal access to the parcel): this covers ONLY the connect-from-scratch decision for a raw plot / rural new-build — bringing grid electric, mains water, and foul drainage to a parcel that may have none.*

A serviced-looking plot can be a financial trap. A listing that says "building plot" almost never means "connected plot". The three connect-from-scratch decisions a foreign plot buyer must price BEFORE offering are: (1) **grid electricity** — a distance-based connection quote that can swing from a few thousand to five-figure depending on metres to the nearest network and the utility's connection-charge regime; (2) **mains water** — present at the boundary, extendable at cost, or absent (forcing a well/borehole + abstraction permit); (3) **foul drainage** — mains sewer vs a mandatory on-site septic / packaged treatment plant whose feasibility is itself a permit gate. In most legal families, the planning/building permit will not issue, or the sale/sale-deed cannot complete, until the drainage solution is proven — so this is a go/no-go on the parcel, not a post-purchase task. Bands below are order-of-magnitude `est.` framing only; **always obtain a written quote from the named local utility before relying on any figure** — distance to network is the dominant cost variable and is parcel-specific.

#### Connect-from-scratch by jurisdiction / legal-family

- **France — SPANC (foul) + Enedis (electric) + viabilisation.** A parcel not served by mains sewer ("tout-à-l'égout") needs **assainissement non collectif (ANC)**: an on-site septic/treatment installation controlled by the commune's **SPANC** (Service Public d'Assainissement Non Collectif). Technical prescriptions: **Arrêté du 7 septembre 2009** (installations ≤ 1,2 kg/j DBO5), under **CGCT art. L.2224-8 / R.2224-17** and **Code de la santé publique art. L.1331-1-1**; the SPANC conformity report is one of the diagnostics annexed to the sale under **CCH art. L.271-4** ([Légifrance arrêté du 7 sept. 2009](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000021125886/); [Chambre des Notaires Gironde — diagnostic ANC](https://chambre-gironde.notaires.fr/vos-besoins/immobilier-besoins/le-diagnostic-des-installations-dassainissement-non-collectif/)). For a raw plot the SPANC issues a *projet*-stage conformity opinion that gates the permis de construire; a non-conform existing system passes the one-year-to-fix obligation to the buyer. Electric: **Enedis** "raccordement / viabilisation" — request a devis on Enedis-Connect; for BT ≤ 36 kVA the proposal arrives ~10 working days (no extension) to ~6 weeks (network extension needed), then ~6 weeks–4 months to works ([ENGIE — raccordement terrain non viabilisé](https://particuliers.engie.fr/demenagement/conseils-demenagement/conseils-raccordement/raccordement-electrique-terrain-non-viabilise.html)). Connection cost band: low-four-figure for a near-network plot rising materially with metres of network extension (`est.`; **the Enedis devis is the only reliable figure** — distance to the réseau is the swing variable). Full viabilisation also bundles water + comms; budget months, not weeks.
- **United Kingdom (E&W) — DNO/ICP (electric) + water undertaker (water) + Building Regs Part H (foul).** New electricity connection runs through the regional **DNO** (or a contestable **ICP**/IDNO for the dig); new water connection through the regional **water undertaker** ([UK Power Networks Services — ICP connection process](https://www.ukpowernetworksservices.co.uk/icp-network-connections/icp-connection-process/)). Foul drainage: **Building Regulations 2010, Schedule 1 Part H (H1/H2)** requires connection to a public sewer where reasonably practicable; only where not feasible may a cesspool / septic tank / package treatment plant be used, and a discharge must satisfy the **Environment Agency General Binding Rules** (or need a permit if it exceeds the rules — e.g. >2 m³/day to ground, within a groundwater Source Protection Zone 1, or within 50 m of a drinking-water source) ([Building Regs Approved Document H, 2015 ed.](https://assets.publishing.service.gov.uk/media/5a80cf9ded915d74e33fc8ae/BR_PDF_AD_H_2015.pdf); [HoC Library — sewerage connections for new housing](https://commonslibrary.parliament.uk/sewerage-connections-for-new-housing-developments-in-england/)). Cost/lead-time is distance- and capacity-driven; get DNO + water-undertaker quotes during planning (`est.` — both are formal quoted processes, **rely on the DNO/undertaker quote not a rule of thumb**).
- **Germany — Erschließung / Erschließungsbeitrag (BauGB §§ 123–135).** A plot is only legally buildable when "erschlossen" (serviced — road, water, foul, power access). Under **Baugesetzbuch §§ 123 ff., 127, 129, 133, 135** the municipality recovers servicing-facility cost from owners as an **Erschließungsbeitrag** (owner share up to 90%, municipal minimum 10% per § 129); in Bavaria/Baden-Württemberg the **KAG** (Kommunalabgabengesetz) applies instead ([§ 127 BauGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bbaug/__127.html); [Erschließungsbeitrag overview](https://www.juraforum.de/lexikon/erschliessungsbeitrag)). A nominally cheap plot can carry a large unbilled Erschließungsbeitrag (municipality has up to 4 years post-completion to bill); **ask the Gemeinde in writing whether the plot is fully erschlossen and whether any Erschließungs-/KAG-Beitrag is outstanding or pending** before offering (`est.` — amount is per-municipal-ordinance, not generalisable).
- **Spain — suelo rústico / no urbanizable "no licence to connect".** Rústico / suelo no urbanizable rarely has infrastructure; the owner bears all servicing cost and connection is **not guaranteed** — utilities may refuse to connect a parcel without a valid building licence, and on rústico that licence is itself exceptional (agricultural/livestock/public-interest justification, regional minimum-plot rules — e.g. Valencia ~10,000 m²) ([HG.org — building on rustic land Spain](https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283); [Rivera Lawyers — urban vs rural purchases](https://riveralawyersfirm.com/legal-differences-between-urban-and-rural-property-purchases-in-spain/)). Self-sufficiency (solar, well, septic/depuradora) is often the only path. Verify with the **ayuntamiento** whether connections are physically and legally possible BEFORE offering — a connectable urbano plot and an un-connectable rústico plot can look identical in a listing.
- **Portugal — terreno rústico, no infrastructure, municipal licence gate.** Rústico land typically has no water/sewer/electricity/road; a project will not be approved unless water (**EDP/distributor**), electricity, and a wastewater solution (**fossa séptica or ETAR doméstica** where no public sewer) are all designed by a qualified technical team, and the **câmara municipal** issues a building licence only after project approval — isolated parcels far from infrastructure are rarely approved ([idealista — construir em terreno rústico guia](https://www.idealista.pt/news/imobiliario/habitacao/2024/12/03/67072-construir-casas-em-terrenos-rusticos-um-guia-para-proprietarios); [AC Arquitetos — construir em solo rústico exceções](https://www.ac-arquitetos.com/post/construir-em-solo-rustico-excecoes-legais-em-portugal)). Treat connectability as a câmara-confirmed pre-offer item. Portugal-rústico guidance is from idealista/AC-Arquitetos (secondary — ⚠️ cross-check the specific câmara); no Portuguese building-code article number could be confirmed without a further call, so it is asserted at narrative level only.
- **United States (rural) — well + septic + perc test + utility line-extension.** No mains water → private well (drilling + often a state/county water-well permit); no mains sewer → on-site septic, gated by a **percolation ("perc") / soil test** the county health department generally requires before a septic permit and hence before a building permit; perc results have a limited validity (~2–5 years, jurisdiction-specific) ([Building Advisor — soil & perc testing](https://buildingadvisor.com/buying-land/septic-systems/soil-and-perc-testing/); [Land Limited — septic & perc raw-land guide 2026](https://landlimited.com/blogs/septic-systems-perc-tests-for-raw-land-complete-2026-buyers-guide-cost-map)). Perc test order-of-magnitude band ~$300–$1,900, septic permit a few hundred dollars more (`est.`, county-variable — **a failed perc can make the parcel unbuildable; condition the offer on it**). Electric line-extension is distance-priced: the co-op/utility typically covers a first stretch then charges per linear foot beyond, escalating with overhead-vs-underground and pole count ([HomeGuide — cost to get utilities on land](https://homeguide.com/costs/cost-to-get-utilities-on-land)). **Get the utility's written line-extension estimate; do not rely on per-foot averages.**
- **Costa Rica / rural-LATAM coastal — frequently no service at all.** Many coastal/rural lots have no grid (**ICE** or local co-op) and no public water; a building permit requires a **water-availability letter (carta de disponibilidad de agua)** from **AyA** or the local **ASADA** — without it the municipality will not issue the permit; no public water → a well needs a concession from the environment ministry ([Remax — Costa Rica water letter](https://www.remax-oceansurf-cr.com/water-letter-when-buying-a-lot); [GAP — utilities in Costa Rica](https://gap.cr/utilities-in-costa-rica/)). ICE connection ~1–3 weeks where infrastructure exists, but months + line-extension cost where it does not (`est.`). Maritime-zone overlay compounds it: first 200 m public domain, next 150 m concession (not freehold) — a no-service coastal lot may also be un-titleable; this maritime-zone point is cross-referenced from CR playbook scope as a *compounding* factor, not a primary connect-from-scratch claim. Verify the water letter exists/obtainable and ICE infrastructure reaches the lot BEFORE offering.
- **Generic civil-law line (other jurisdictions).** Across most civil-law systems the pattern recurs: the **municipality/commune controls the building/planning permit and conditions it on a proven drainage solution** (mains-sewer connection or an approved on-site treatment installation), the **distribution utility quotes a distance-based connection charge** with a multi-month lead, and a parcel formally classified non-urban / agricultural may be **legally un-connectable regardless of physical proximity** to a line. Where this block has no country-specific entry: treat utility connectability as `data not publicly available — verify with the local municipality (planning/permit office) and the distribution utility in writing before offer`.

#### Pre-offer verification path (universal)

1. **Confirm mains availability at each utility, in writing.** Ask the electricity distributor, the water undertaker/utility, and the sewerage authority/municipality, per the parcel reference (cadastral ID), whether each main is present at the boundary, extendable, or absent. A listing's "services available" claim is seller-controlled — tag it `(per listing — verify with the named utility)`.
2. **Obtain the distance-based connection quote(s).** Request the formal connection/extension quote (FR Enedis devis; UK DNO + water-undertaker quote; US utility line-extension estimate; DE Gemeinde Erschließungs-/KAG status; CR ICE + water letter). Distance to the network is the dominant cost variable — never substitute a per-foot/per-metre rule of thumb for the parcel-specific quote.
3. **Test septic feasibility and clear the compliance gate.** Where no mains sewer: confirm an on-site system is permissible and feasible — US perc/soil test (condition the offer on a pass); FR SPANC project-stage conformity opinion; UK Part H + Environment Agency General Binding Rules eligibility; PT/ES qualified-technician wastewater design. A failed/ineligible drainage test can make the parcel unbuildable.
4. **Confirm the planning/building permit will allow the connection at all.** On non-urban / rústico / agricultural land the permit (and thus the legal right to connect) may be exceptional or refused regardless of physical proximity. Confirm buildability and connection-permissibility with the municipal planning office before relying on any quote.
5. **Fold the full cost + lead-time into the offer.** Sum connection charges + on-site system + tests/permits + any servicing contribution (DE Erschließungsbeitrag), and price the multi-month lead-time as carrying cost. Make the offer conditional on (3) and (4) where the drainage/permit outcome is unresolved.

> **Confidence (this sub-block): MEDIUM.** FR/UK/DE/US statute-and-scheme citations verified to primary or near-primary sources (Légifrance, gesetze-im-internet.de, gov.uk Approved Document H, HoC Library); ES/PT/CR entries rest on secondary practitioner sources (⚠️ cross-check the specific municipality). All cost/lead-time figures are order-of-magnitude `est.` only and MUST be replaced by a parcel-specific utility quote before reliance. Last verified: 2026-05-15.

---

## 5. Heritage / listed property

### Specifics

- **Restoration obligations** — original materials, traditional methods
- **Consent regime** for any change (interior + exterior)
- **Heritage authority approval** — slow (months to years)
- **Higher restoration costs** — specialist craftsmen, original materials
- **Tax incentives** — many jurisdictions offer relief for restoration
- **Insurance premium** — typically 50-100% above standard
- **Smaller buyer pool** at resale → liquidity discount

### Country-specific

| Country | Listing levels | Authority | Tax incentive |
|---|---|---|---|
| 🇫🇷 | ISMH (inscrit), MH (classé), patrimoine remarquable | DRAC + ABF | Loi Malraux: deduct 22-30% of works for 4 yrs; Monuments historiques: 100% deductible if open to public |
| 🇮🇹 | Vincolo + Beni culturali | Soprintendenza | Bonus 110% / Restauro 50% |
| 🇩🇪 | Denkmalschutz (per Bundesland) | Denkmalbehörde | §7i EStG: 9% × 8yrs + 7% × 4yrs depreciation on restoration |
| 🇪🇸 | BIC (Bien de Interés Cultural) | Cultura + CCAA | IRPF 30% reduction + ICIO exemption |
| 🇬🇧 | Grade I, II*, II | Historic England / Cadw / HES | VAT 5% on alterations, but full VAT on like-for-like repairs (post-2012) |
| 🇮🇪 | Protected Structure | Local Planning Authority | Heritage Council grants |
| 🇵🇹 | IIM / IIP / MN | Direção Geral do Património Cultural | IRS deduction up to €500/yr |
| 🇸🇪 | K-märkt / byggnadsminne | Länsstyrelse | Limited grants |
| 🇨🇭 | Per-canton | Kantonale Denkmalpflege | Various |

### Pre-purchase checks

- [ ] **Listing register entry** — print certificate
- [ ] **Restoration obligations document** (FR : arrêté de classement / inscription)
- [ ] **Past works approved / disapproved** — any pending complaints?
- [ ] **Roof, masonry, joinery condition** — heritage materials very expensive
- [ ] **Existing furniture / features listed** (some countries list interior elements)
- [ ] **Open-to-public obligations** (FR MH classé)
- [ ] **Insurance availability** at reasonable premium
- [ ] **Specialist craftsman availability** in region

### Output add-on

```markdown
### Heritage Property Specific

**Listing**: <country-specific level (e.g., FR MH classé / UK Grade II / DE Denkmal)>
**Date of listing**: <YYYY>
**Listed elements**: <façade, roof, interior, garden>
**Authority**: <DRAC + ABF / Soprintendenza / Historic England / etc.>

#### Restoration obligations
- Original materials required: ✅/❌
- Traditional methods required: ✅/❌
- Consent for: <list of restricted works>
- Open-to-public: <yes (X days/yr) / no>

#### Past works
- Approved: <list>
- Refused: <list>
- Pending complaints: <list>

#### Tax incentives applicable
- <country-specific scheme>
- Estimated value: €<X>/yr for <Y>yrs

#### Cost premium estimate
- Restoration premium vs standard: +30-100%
- Specialist craftsmen: <local availability>
- Insurance premium: +50-100%
- Liquidity discount at resale: -10-20%

#### Verdict
- 🟢 Well-restored, tax-relieved, niche buyer profile
- 🟡 Restoration backlog manageable
- 🟠 Major restoration required + slow consent
- 🔴 Crumbling + restrictive consent regime
```

---

## 6. Apartment vs House — what differs

### Apartment-specific checks

#### HOA / management body

- **VME / ACP / sameieforening / Eigentümergemeinschaft / etc.** — read AGM minutes (3 yrs)
- **Reserve fund** balance — minimum required by law in some countries
- **Maintenance plan** (MJOP NL / vedlikeholdsplan NO / piano di manutenzione IT)
- **Outstanding works** — assessment levies upcoming
- **Disputes** — neighbor / management / contractor

#### Building common parts

- **Roof, façade, common stairs, lift, garage, garden**
- **Last major works** date + cost
- **Lift maintenance contract**
- **Fire safety compliance**
- **Façade cleaning + repointing schedule**
- **Heating system** (collective vs individual)

#### Apartment-specific docs

- **Splitsingsakte** (NL) / **règlement de copropriété** (FR) / **Teilungserklärung** (DE) / **regolamento condominiale** (IT)
- **Number of units in building** + private vs communal
- **Voting rights** in HOA
- **House rules** (pets, short-let, noise, parking)

#### Country-specific apartment red flags

- 🇫🇷 **Charges de copropriété** in arrears (seller? other co-owners?)
- 🇮🇹 **Spese condominiali** unpaid > 2 months
- 🇩🇪 **WEG** (Wohnungseigentümergemeinschaft): Hausgeld + Sonderumlage
- 🇳🇴 **Borettslag fellesgjeld** — shared building debt; check ratio
- 🇸🇪 **Bostadsrättsförening** (BRF) — financial health critical
- 🇫🇮 **Asunto-Oy** — vastike (charge), planned putkiremontti (pipe renovation)
- 🇪🇸 **Comunidad de propietarios** — derramas (special levies)

### House-specific checks

- **Roof** — last replaced? Insulated? Tile/slate type?
- **Heating + DHW system** — type, age, efficiency
- **Plumbing** — material (lead?), main shut-off, septic vs mains
- **Electrical panel** — age, capacity, RCDs, smart meter
- **Garden boundaries** — bornage / Vermessung / fence agreement
- **Outbuildings** — garage, shed, pool — taxed?
- **Driveway access** — easement vs ownership
- **Neighbor disputes** — fence, hedge, boundary, noise
- **Trees** — protected, easement, branches over property
- **Drainage** — surface water, soakaway
- **Parking** — on-street, off-street, EV charging
- **Garden maintenance** — outdoor tap, irrigation, hose access

### Output add-on (apartment)

```markdown
### Apartment Specific

**Building**: <units>, built <year>, last major works <year>
**HOA**: <VME / ACP / etc.>
**Monthly charges**: €<X>
**Reserve fund**: €<Y> (= <Z> months of operating)

#### HOA health
- AGM attendance: <%>
- Vote splits: <consensus / contested>
- Outstanding levies: €<X> (next 3 yrs)
- Litigation: <list>

#### Building condition
- Roof age: <Xyr>
- Façade: <last cleaned / repointed>
- Lift: <maintained, no breakdowns>
- Common heating: ✅/❌ (collective / individual)

#### Verdict
- 🟢 Healthy HOA, well-maintained, no surprises
- 🟡 Some deferred maintenance, manageable
- 🟠 Significant assessment levies upcoming
- 🔴 HOA in financial distress / major works required
```

### Output add-on (house)

```markdown
### House Specific

**Type**: <detached / semi-detached / terraced>
**Roof**: <type, age, insulation>
**Heating**: <type, age>
**Plumbing**: <mains drains / septic, age>
**Electrical**: <panel age, RCD, capacity>

#### Boundaries + outdoor
- Bornage: ✅/❌ (date)
- Fence agreement with neighbors: ✅/❌
- Easements: <list>
- Trees protected: <list>

#### Major systems age
- Roof: <Xyr (life expectancy Y)>
- Boiler: <Xyr>
- Plumbing: <Xyr>
- Electrical: <Xyr>

#### Verdict
- 🟢 Modern systems, clean boundaries, no disputes
- 🟡 Minor system updates needed in 5yrs
- 🟠 Major systems aging, significant 5-yr capex
- 🔴 Systems failing + boundary disputes + pre-emption rights
```

### Leasehold / ground-rent / enfranchisement trap

**Fold-in target**: `--type=apartment-vs-house`.

In a handful of common-law / mixed jurisdictions, "buying a flat" does not mean buying the land. You buy a **time-limited lease** (often 99, 125, 250 or 999 years) carved out of a freehold or Crown title. Two traps recur for foreign apartment buyers: (1) the **wasting-asset cliff** — value and mortgageability collapse as the unexpired term shortens (the ~80-year "marriage value" line in England & Wales; the ~60-year decay / ~30-year loan-rejection line in Singapore); and (2) **escalating ground rent** — historic doubling / RPI-linked ground-rent clauses that can render a lease un-sellable and un-mortgageable. A short lease or a toxic ground-rent clause is a *latent* defect: it is invisible on a viewing and often understated by the listing. Always extract the **unexpired term** and the **ground-rent clause** before offer. In civil-law freehold-only countries this whole section is N/A — flats are sold as freehold condominium units (no ground rent, no lease cliff).

#### Leasehold jurisdictions

- **GB (England & Wales)** — Tenure forms: freehold, leasehold (flats predominantly leasehold; long leases 99/125/250/999yr), commonhold (rare). Ground rent: new long residential leases granted on/after 30 Jun 2022 capped at a **peppercorn** (zero economic) under the **Leasehold Reform (Ground Rent) Act 2022** (in force 30 Jun 2022; 1 Apr 2023 retirement homes — legislation.gov.uk / en.wikipedia.org/wiki/Leasehold_Reform_(Ground_Rent)_Act_2022); pre-2022 leases keep their original clause — historic **doubling** (e.g. every 10/25yr) and RPI-linked clauses persist and are the main toxicity. Mortgageability cliff: most lenders require ~**80–85 years unexpired** at purchase (many decline <70–80yr); **no marriage value is payable if >80yr unexpired when the extension notice is served** — below 80yr marriage value is split **50/50** between leaseholder and freeholder, sharply raising cost (lease-advice.org/lease-extension/flats/marriage-value); very short leases (<~60yr) are effectively cash-only. The ~80-year marriage-value line and ~85-year lender comfort line are **market/lender conventions, not statutory thresholds** — exact lender cut-offs vary by bank; treat as `est.` / lender-dependent and verify with the specific lender. Enfranchisement/extension route: statutory lease extension / collective enfranchisement / individual freehold purchase via the **First-tier Tribunal (Property Chamber)** on disputed valuation; cost driver = unexpired term, ground rent capitalised, and (still, as of 2026) marriage value below 80yr. Reform + status: **Leasehold and Freehold Reform Act 2024** (Royal Assent 24 May 2024 — legislation.gov.uk/id/ukpga/2024/22) will abolish marriage value and cut extension costs, but **most provisions remain UN-COMMENCED as of May 2026** — only the removal of the 2-year ownership qualifying period, right-to-manage and building-safety provisions are in force; a freeholder judicial review was dismissed Oct 2025 (Court of Appeal permission to appeal granted 1 Apr 2026); the enfranchisement valuation reforms come into force only after drafting flaws are fixed in the Commonhold and Leasehold Reform Bill (MHCLG consultation, 2 Jul 2026), a Bill announced 13 May 2026 and not yet introduced as of Sep 2026 (House of Commons Library, commonslibrary.parliament.uk/leasehold-reform-in-england-and-wales, 2026). Do not advise a GB (E&W) buyer that marriage value is gone — the LFRA 2024 marriage-value abolition is **NOT commenced as of May 2026**; it still applies below ~80yr; re-verify commencement at commonslibrary.parliament.uk before any output. Free official guidance: **LEASE — Leasehold Advisory Service** (lease-advice.org).
- **GB (Scotland)** — Tenure forms: predominantly **freehold-equivalent** outright ownership; long residential leases were largely converted to ownership and ultra-long leases (>175yr) converted by the **Long Leases (Scotland) Act 2012**; feudal tenure abolished by the **Abolition of Feudal Tenure etc. (Scotland) Act 2000** (legislation.gov.uk). Ground rent: feu duty abolished — **no ongoing ground-rent / lease-cliff regime for residential**; flats held under tenement law with factoring (service) charges, not ground rent. Mortgageability cliff: N/A for ownership. Note: **Scotland is structurally different from England & Wales — do not apply E&W leasehold logic to a Scottish flat**; verify title at Registers of Scotland (ros.gov.uk).
- **IE (Ireland)** — Tenure forms: freehold, and leasehold subject to **ground rent** (older houses/flats on long leases). Ground rent: a fixed (usually nominal, non-escalating) annual ground rent to a superior landlord; modern apartments are typically long-leasehold with service charges + sinking fund rather than significant ground rent. Mortgageability cliff: lenders prefer long unexpired terms; very short residual leases are a financing problem (verify with lender — threshold not centrally published). Enfranchisement/extension route: statutory **Ground Rents Purchase Scheme** under the **Landlord and Tenant (Ground Rents) (No. 2) Act 1978** (irishstatutebook.ie/eli/1978/act/16) — residential occupiers can **buy out the ground rent / enlarge to freehold** via the Vesting Certificate procedure administered by **Tailte Éireann** (Land Registry; >80,000 buy-outs since 1978 — tailte.ie/services/ground-rents); two paths: consent of landlord or arbitration. Reform + status: clarified by the **Landlord and Tenant (Ground Rents) (Amendment) Act 2019** (a prior tenant no longer counts as predecessor of the landlord, widening eligibility — mccannfitzgerald.com, 2019). Cost driver: capitalised ground rent multiple + arbitration fee (low for nominal ground rents).
- **SG (Singapore)** — Tenure forms: freehold, 999-year leasehold (legacy, no longer granted), **99-year leasehold** (now standard for new private and all HDB), 103/110yr variants. Ground rent: no recurring ground rent — the value erosion is **lease decay** itself. Mortgageability cliff: bank LTV falls as the lease shortens; value typically weakens once **<~60–70yr remain**; properties with **<30–35yr** unexpired commonly face **loan rejection** and CPF-use restrictions (industry-reported, not a single statutory figure — these ~60yr decay and ~30–35yr loan-rejection figures are industry-reported lender behaviour, not a statutory rule; verify with lender / CPF Board for the specific unit). Enfranchisement/extension route: **no statutory right to renew or top-up**. Private leasehold owners may *apply* to **Singapore Land Authority (SLA)** for a discretionary fresh-99yr **lease top-up** at a premium (approval not guaranteed — sla.gov.sg). HDB flats: no renewal — flat reverts to State at expiry with no compensation unless selected for **SERS** (rare, generous) or **VERS** (broader, lower compensation, resident-vote-driven) (hdb.gov.sg). Reform + status: 999yr leases discontinued; VERS framework announced (long-dated, not yet operational at scale, 2026).
- **HK (Hong Kong)** — Tenure forms: virtually all land is **Government leasehold** (no freehold except St John's Cathedral); flats are units under a Government lease + Deed of Mutual Covenant. Ground rent: **Government rent** = 3% of rateable value per annum on most post-1985 / extended leases (Lands Department — landsd.gov.hk). The historic concern is the **2047 land-tenure question** (many leases expiring 30 Jun 2047). Mortgageability cliff: short residual government-lease terms affect mortgage tenor; verify with bank (no single published cut-off). Enfranchisement/extension route: no leaseholder enfranchisement; **extension is at Government discretion** — 1997 policy: non-renewal-clause leases may be extended 50yr without premium but at 3% rateable-value annual rent (legco.gov.hk, landsd.gov.hk). Reform + status: **Extension of Government Leases Ordinance (Cap. 648)** — in force **5 Jul 2024** (info.gov.hk/gia/general/202407/04/P2024070400682.htm) — statutory mechanism for **automatic 50-year extension** of qualifying general commercial/residential/industrial leases (without renewal right, not STT/SPL) by an "Extension Notice" gazetted ~6yr before expiry, **no additional premium** but 3%-of-rateable-value annual government rent on extension; first notice (5 Jul 2024) covered 376 lots; Basic Law Art. 7 confirms HKSARG power to grant land beyond 2047 (news.gov.hk/eng/2024/12/20241227, devb.gov.hk, 2024). Verify lot status / Non-extension List at Lands Department.
- **AE (UAE — Dubai / Abu Dhabi)** — Tenure forms: **freehold** (foreigners, only in designated areas — Dubai since the Freehold Decree of 2002 / Regulation No. 3 of 2006; e.g. Dubai Marina, Palm Jumeirah, Downtown), **leasehold** (typically 30–99yr, land remains with the original owner), usufruct, musataha. Ground rent: no UK-style escalating ground rent; leasehold = fixed-term right to use, often a service-charge regime rather than ground rent. Mortgageability cliff: a 99-yr leasehold functions close to freehold for most buyers; short residual lease terms reduce financeability — verify with lender. Enfranchisement/extension route: **no statutory leaseholder enfranchisement** — renewal/extension is contractual with the landowner/master developer, not a tribunal right. Reform + status: ownership type and any time limitation are recorded on the **Dubai Land Department (DLD)** title deed (dubailand.gov.ae) — freehold deeds carry no time limit; always confirm freehold vs leasehold on the DLD deed before offer (u.ae/en/information-and-services/moving-to-the-uae/expatriates-buying-a-property-in-the-uae, 2026). Abu Dhabi: comparable freehold/leasehold/usufruct/musataha split — verify with DARI (Abu Dhabi).
- **AU (Australia — ACT / Canberra only)** — Tenure forms: rest of Australia is freehold (Torrens); the **ACT is leasehold** — nearly all land is Commonwealth-owned and held on a **99-year Crown lease** (Planning and Development Act 2007; system rooted in the 1910 Seat of Government Act prohibition on freehold disposal — planning.act.gov.au/community/buy/leasing-and-titles/crown-leases). Ground rent: no escalating ground rent on standard residential Crown leases (a separate optional **Land Rent Scheme** lets buyers rent the land instead of paying for it upfront). Mortgageability cliff: not a practical issue — lenders treat ACT Crown leasehold like freehold because renewal is near-automatic; on purchase you take the **balance** of the term. Enfranchisement/extension route: a 99-yr lease can be **renewed for a fresh 99yr on application for an administrative fee** at the leaseholder's election (unless the Territory needs the land) — there is no marriage-value or wasting-asset trap analogous to E&W; the **ACT is the only Australian leasehold jurisdiction**, the rest of Australia being freehold. Reform + status: political discussion about converting ACT to freehold continues but would require federal cooperation; **no change as of 2026** (canberratimes.com.au, 2025). Other Australian states: freehold — N/A.

#### Freehold-majority — no leasehold/ground-rent regime (one line per region)

- **Western Europe & Nordics (FR, DE, IT, ES, PT, NL, BE, AT, CH, IE-apartments-mostly, scandinavia)** — civil-law freehold / condominium ownership; flats sold as freehold units with co-ownership shares + service charges (copropriété / WEG / condominio / VvE), **no ground-rent or lease-decay tenure** — if a listing claims "leasehold", verify at the national land registry (e.g. FR cadastre/Service de la publicité foncière, DE Grundbuch, ES Registro de la Propiedad, NL Kadaster).
- **Central & Eastern Europe (CZ, SK, PL, HU, RO, etc.)** — civil-law freehold-only; apartments are freehold units under unit-ownership law, **no ground-rent / leasehold tenure** — verify at the national cadastre (e.g. CZ ČÚZK, SK Kataster, PL Księgi Wieczyste) if a listing claims leasehold.
- **North America (US, CA, MX)** — predominantly freehold / fee simple (US condos = fee-simple units; rare exceptions: ground-lease condos in NYC/Hawaii, First Nations leasehold land in Canada, Mexican *fideicomiso* trust within the restricted coastal/border zone — these are property-specific, not a national leasehold regime); **no general ground-rent tenure** — verify on the county/land-title record if a listing references a ground lease.
- **Latin America (BR, AR, CL, CO, etc.)** — civil-law freehold-only; apartments are freehold (*propiedad horizontal*), **no ground-rent / leasehold tenure** — verify at the national property registry if leasehold is claimed.
- **Rest of common-law / mixed Asia & elsewhere (TH, MY, ID, PH, IN, ZA, etc.)** — *property-specific*, not blanket: most allow freehold for nationals but impose **foreign-ownership structural restrictions** (e.g. TH foreigners freehold condos only up to the 49% building quota / land via leasehold or company; MY/ID/PH leasehold or quota rules) — this is a foreign-ownership-structure issue, not a UK-style ground-rent trap; covered under the foreign-buyer journey, not here. Verify at the national land office; **do not apply E&W marriage-value logic outside GB (E&W)**.

This block covers tenure-form leasehold (UK-style ground rent / lease decay) only. **Foreign-ownership structural restrictions** (TH 49% condo quota, fideicomiso, etc.) are a different problem handled in the foreign-buyer journey — do not conflate.

#### Pre-offer leasehold checklist

1. **Unexpired term** — exact years/months remaining on the lease *today* (not the original grant length). Get it from the lease + title register, not the listing. GB (E&W): is it above the ~80–85yr lender line? SG: is it above the ~60yr soft / ~30yr loan-rejection line?
2. **Ground-rent clause** — read the actual clause: amount, review basis (fixed / RPI / **doubling**), review frequency. A doubling clause is a red flag for resale and mortgageability (GB pre-2022 leases especially).
3. **Marriage-value / wasting-asset threshold** — GB (E&W): below ~80yr unexpired, marriage value inflates extension cost (still applicable as of May 2026 — LFRA 2024 abolition NOT yet commenced). SG: model the value/financing decay curve at your intended exit horizon.
4. **Service charge vs ground rent — separate them** — service/factoring charge (building running cost) is *not* ground rent; both must be quantified. Get 3 years of service-charge accounts, reserve/sinking-fund balance, and any pending major-works levy (Section 20 in GB).
5. **Enfranchisement / extension cost estimate** — obtain a written estimate (GB: surveyor + LEASE valuation; IE: ground-rent buy-out figure via Tailte Éireann; SG: indicative SLA top-up premium) *before* offer, and price it into the bid.
6. **Lender pre-check** — confirm a real mortgage offer is achievable on this specific unexpired term *and* this ground-rent clause; some lenders reject toxic ground-rent clauses outright even on long leases.
7. **Reform exposure** — GB (E&W): is the deal sensitive to LFRA-2024 commencement timing? Track via House of Commons Library / LEASE. HK: confirm 2047 lot status / extension treatment at Lands Department.

<!-- Verified sources: legislation.gov.uk (LRGRA 2022, LFRA 2024 ukpga/2024/22, Abolition of Feudal Tenure Scotland Act 2000); commonslibrary.parliament.uk/leasehold-reform-in-england-and-wales; lease-advice.org; irishstatutebook.ie/eli/1978/act/16; tailte.ie/services/ground-rents; mccannfitzgerald.com (2019 Amendment Act); sla.gov.sg; hdb.gov.sg; landsd.gov.hk; legco.gov.hk; devb.gov.hk; info.gov.hk/gia/general/202407/04/P2024070400682 (Extension of Government Leases Ordinance Cap.648 in force 5 Jul 2024); news.gov.hk/eng/2024/12/20241227; dubailand.gov.ae; u.ae expatriates-buying-a-property; planning.act.gov.au/community/buy/leasing-and-titles/crown-leases; canberratimes.com.au (2025). Last verified: 2026-05-15. Confidence: HIGH on statute identity + GB/HK reform status; MEDIUM on numeric lender cliffs (lender-convention, labelled est.). -->

---

## How to invoke

```
/property-deep-dive <addr> --all --type=off-plan
/property-deep-dive <addr> --all --type=heritage --journey=foreign-buyer
/property-deep-dive <addr> --all --type=apartment --integrity
/property-deep-dive <addr> --type=plot-only --price --tax
```

Type detection:
- Auto-detected from listing URL or address descriptor where possible
- Manually overridden with `--type=<kind>`

## Output integration

When `--type=<kind>` is requested, the output adds an "## <Type>-Specific Analysis" section after the standard sections.

Multiple types can stack:
- `--type=apartment,heritage` → both sections appear

## Confidence labels

- **HIGH**: Type-specific data accessible (developer registry, HOA documents, heritage register)
- **MEDIUM**: Type-specific check possible but limited (auction with partial legal pack, HOA without minutes)
- **LOW**: Type-specific data unavailable (off-plan with no developer history, plot with no zoning data)

## Forbidden hallucinations

- Never claim "buildable" for plot without checking zoning
- Never claim heritage tax incentive without verifying
- Never minimize off-plan risk without checking guarantees
- Never invent past auction sale prices
- Always surface jurisdictional caveats (consent regime, forced heirship)

## Cross-references

- `--type=off-plan` pairs strongly with `--integrity` (developer due diligence)
- `--type=auction` pairs strongly with `--integrity` (compressed timeline = higher fraud risk)
- `--type=probate` pairs with `--journey=inheritance`
- `--type=plot-only` pairs with `--risks` + `--mains` + `--climate`
- `--type=heritage` pairs with `--tax` (heritage incentives)
- `--type=apartment` pairs with `--rental` (HOA may restrict short-let)
