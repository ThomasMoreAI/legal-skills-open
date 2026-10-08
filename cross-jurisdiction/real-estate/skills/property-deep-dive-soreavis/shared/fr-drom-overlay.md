# FR DROM overlay — Guadeloupe · Martinique · Guyane · Réunion · Mayotte

> **Scope.** This file is an **overlay**, not a standalone playbook. The five DROM (*Départements et Régions d'Outre-Mer*) are constitutionally **integral parts of the French Republic** (Constitution Art. 73, *Code civil* applies, euro, EU territory, identical land registry framework operated by *DGFiP / Service du cadastre*, same *impots.gouv.fr* portal, same civil courts). Everything in `countries/fr/playbook.md` therefore applies UNLESS a delta is documented below. This file lists ONLY the deltas — fiscal, regulatory, transactional, hazard.
>
> **Parent reference:** [`countries/fr/playbook.md`](../countries/fr/playbook.md) (canonical FR rules — TMP, plus-value, DPE, *carte communale*, *PLU*, *notaire* role, *promesse* / *compromis* / *acte authentique* flow). Use this overlay for `gp`, `mq`, `gf`, `re`, `yt` only.
>
> **Last verified:** 2026-05-27.

---

## 1. Coverage matrix

| ISO | DROM | INSEE dept code | INSEE region code | Capital / *préfecture* | Population (INSEE, ref. year) | Foreign-buyer demand signal | Primary-source verifiability |
|-----|------|-----------------|-------------------|------------------------|-------------------------------|------------------------------|------------------------------|
| `gp` | Guadeloupe | 971 | 01 | Basse-Terre (*préf.*) / Pointe-à-Pitre (econ.) | 383,569 (1 Jan 2022 census, [INSEE Dossier complet 971](https://www.insee.fr/fr/statistiques/2011101?geo=DEP-971)) | Moderate — French metro retirees, US/CA Caribbean buyers | HIGH (full INSEE/DGFiP coverage) |
| `mq` | Martinique | 972 | 02 | Fort-de-France | 360,600 (1 Jan 2023, [INSEE L'essentiel — Martinique](https://www.insee.fr/fr/statistiques/4482393)) | Moderate — French metro retirees | HIGH |
| `gf` | Guyane | 973 | 03 | Cayenne | 293,996 (1 Jan 2023, [INSEE L'essentiel — Guyane](https://www.insee.fr/fr/statistiques/4313999)) | Low — ESA / CNES employees, Suriname-border informal | MEDIUM-HIGH (cadastre gaps in interior, see § 9) |
| `re` | La Réunion | 974 | 04 | Saint-Denis | 889,679 (1 Jan 2023, [INSEE L'essentiel — Guyane / pop. comparative](https://www.insee.fr/fr/statistiques/4313999)) | Moderate — French metro retirees, SA / Madagascar inbound | HIGH |
| `yt` | Mayotte | 976 | 06 | Mamoudzou | ~321,000 (Jan 2024 provisional INSEE estimate; full census Nov 2025–Feb 2026; [INSEE L'essentiel — Mayotte](https://www.insee.fr/fr/statistiques/4632225)) | Very low — French-mainland civil-service postings | MEDIUM (very deficient cadastre, see § 9) |

> *INSEE pop. dates differ across DROM because RP (recensement de la population) for Mayotte is on a 5-year cycle vs annual for the other four DROM.* (Source: [INSEE methodological note](https://www.insee.fr/fr/information/2008354).)

---

## 2. TVA — DROM-specific rates (BIG delta vs metro)

Métropole: standard 20% / intermediate 10% / reduced 5.5% / super-reduced 2.1%.

| DROM | Standard | Reduced | Super-reduced (medicines, press) | Status |
|------|----------|---------|----------------------------------|--------|
| `gp` Guadeloupe | **8.50%** | **2.10%** | 1.05% / 1.75% | TVA applies; BOI-TVA-GEO-20-10 |
| `mq` Martinique | **8.50%** | **2.10%** | 1.05% / 1.75% | TVA applies; BOI-TVA-GEO-20-10 |
| `re` La Réunion | **8.50%** | **2.10%** | 1.05% / 1.75% | TVA applies; BOI-TVA-GEO-20-10 |
| `gf` Guyane | **— TVA provisoirement NON applicable** | n/a | n/a | CGI Art. 294-1 + CIBS Art. L211-7 |
| `yt` Mayotte | **— TVA provisoirement NON applicable** | n/a | n/a | CGI Art. 294-1 + CIBS Art. L211-7 |

**Property impact:**
- New-build (*VEFA / immeuble neuf*) VAT is charged at **8.50% in GP/MQ/RE** vs 20% in métropole → meaningful new-build price advantage (2025 data, source: [impots.gouv.fr — TVA DOM](https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom)).
- Rental services (furnished short-let, *para-hôtellerie*) — reduced 2.10% applies where the métropole rate would be 5.5% or 10% (2025 data, [BOFiP BOI-TVA-GEO-20-10](https://bofip.impots.gouv.fr/bofip/343-PGP.html/identifiant=BOI-TVA-GEO-20-10-20190605)).
- **GF / YT: no TVA on construction services or short-let** — but they have *octroi de mer* instead (§ 4).

> **Forbidden-phrasing reminder:** do not write the rate as a fuzzy band — the rate is exactly 8.50% per BOI-TVA-GEO-20-10. Quote it precisely.

---

## 3. Octroi de mer — dock-due on imported goods (DROM-only)

Legal anchor: [Loi n° 2004-639 du 2 juillet 2004 relative à l'octroi de mer](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294) (Légifrance, LEGISCTA000006099294). Collected by *Direction générale des douanes et droits indirects (DGDDI)*, paid to *régions* and *communes*.

**What it is:** a regional consumption tax levied on goods *imported into* each DROM and on goods *produced* in each DROM above a turnover threshold. Two rates: *octroi de mer externe* (imports) and *octroi de mer interne* (local production); both set by each *conseil régional* (GP/MQ/GF/RE) or *conseil départemental* (YT).

**Property-relevant impacts:**

- **Construction materials** (steel rebar, cement, lumber, tiles, plumbing fixtures, electrical) are heavily *octroi*-loaded since they're almost all imported. The composite cost premium typically lands in the **15–25%** band vs métro depending on category (~est. — calibrated against published rates by *conseils régionaux*; verify the latest *tarif octroi de mer* per material for the specific DROM at [douane.gouv.fr — Octroi de mer](https://www.douane.gouv.fr/lexique/octroi-de-mer)).
- **Renovation budget:** add an explicit "*octroi de mer* premium" line to the cost calc — do not assume métro material pricing.
- **VEFA new-builds:** the *octroi* is embedded in the developer's input prices; it does not show as a separate line on the *acte authentique* but is implicit in the listing price.
- 2025 reform note: the *octroi de mer* has been under structural review since the 2022 *projet de loi de finances* (LFI 2022). The current regime is extended to 31 Dec 2027 per EU Council Decision 2021/991 (verify expiry / extension at [douane.gouv.fr](https://www.douane.gouv.fr/lexique/octroi-de-mer) before any 2027+ transaction).

> **No equivalent in métro France.** This is a DROM-only delta; the metro playbook has nothing to say about *octroi*.

---

## 4. Taxe foncière — DROM abattements (delta vs metro)

Metro: standard *valeur locative cadastrale* × *taux communal/intercommunal/départemental* (no DROM-specific abattement).

DROM-specific abattements (in addition to the general regime):

| Mechanism | Legal anchor | What it grants | Source |
|-----------|--------------|----------------|--------|
| **HLM / SEM abattement** | CGI Art. 1388 bis | 30% abattement on *valeur locative* for social-housing units in *quartiers prioritaires de la ville (QPV)*, applies across France — incl. DROM | [BOFiP BOI-IF-TFB-20-30-30](https://bofip.impots.gouv.fr/bofip/4844-PGP.html) |
| **ZFA-DOM abattement** | CGI Art. 1388 quinquies | Abattement for buildings tied to an *établissement* in a *Zone Franche d'Activité dans les DOM* (revised by LFI 2019, called *ZFANG — Zone Franche d'Activité Nouvelle Génération*) | [BOFiP BOI-IF-TFB-20-30-45](https://bofip.impots.gouv.fr/bofip/11858-PGP.html/identifiant=BOI-IF-TFB-20-30-45-20260204) |
| **New-build 2-year exemption** | CGI Art. 1383 | Same as metro (2 years exonération *constructions neuves*) — no DROM uplift, but base rate already lower thanks to lower *valeurs locatives* | [BOFiP BOI-IF-TFB-10-60](https://bofip.impots.gouv.fr/bofip/1881-PGP.html/identifiant=BOI-IF-TFB-10-60-20211220) |

**Net effect:** *valeurs locatives* in DROM are systematically lower than métro equivalents (legacy of 1970s revisions never fully recalibrated), so headline *taxe foncière* bills tend to be lower than métro for comparable surface — but this is a function of base, not rate. Verify the actual bill via the *avis de taxe foncière* on the seller's *espace personnel impots.gouv.fr* before relying on it (per-listing — verify with DGFiP).

---

## 5. Défiscalisation — Pinel Outre-Mer ENDED 31 Dec 2024

**ENDED.** *Pinel Outre-Mer* (CGI Art. 199 novovicies — overseas variant) terminated for new investments on **31 December 2024**, in line with the metropolitan *Pinel* termination ([service-public.gouv.fr — Pinel/Duflot](https://www.service-public.gouv.fr/particuliers/vosdroits/F31151), 2025 update). Investments made on or before 31 Dec 2024 continue to benefit from the multi-year *réduction d'impôt* schedule (6/9/12 years) under existing rules.

**Active overseas defiscalization regimes still open (post-2024):**

- **Loi Girardin social (logement social)** — CGI Art. 199 undecies C — open through at least **31 Dec 2029** for new social-housing intermediation operations in DROM. One-shot *réduction d'impôt* in year N+1. Verify expiry at [BOFiP BOI-IR-RICI-380](https://bofip.impots.gouv.fr/bofip/9398-PGP.html/identifiant=BOI-IR-RICI-380-20240515).
- **Loi Girardin industriel (équipements productifs)** — CGI Art. 199 undecies B — open, not real-estate; mentioned here only to avoid confusion.

**Post-Pinel successor for direct investors:** as of 2026-05-27, **no direct successor regime has been legislated** for the *Pinel Outre-Mer* slot specifically targeted at individual buy-to-let investors in DROM. A *mission parlementaire* was announced in 2024 by the *ministre délégué chargé des Outre-mer* to scope a replacement, but no statute is yet on the books (verify against the latest [legifrance.gouv.fr search for "outre-mer logement"](https://www.legifrance.gouv.fr/) before relying on any third-party claim of a "Pinel successor"). **Anti-hallucination guard:** do not cite any branded successor name unless you can verify it in the *Journal officiel*.

> **Confidence on successor regime: MEDIUM.** This is a live regulatory gap — the regulatory-watch entry should be revisited at least quarterly until either LFI 2026 or LFI 2027 closes it.

---

## 6. Notary fees — DROM are HIGHER, not lower (CRITICAL CORRECTION)

> **Anti-hallucination flag.** A common (and wrong) public claim is that *frais de notaire* are "lower in DROM" or "~3% in DROM vs 7–8% metro". The opposite is true for the regulated *émoluments* portion: they are **majored** in DROM.

Legal anchor: [Code de commerce, Section 3 — Tarifs des notaires, articles A444-53 à A444-186](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000032132058) (Légifrance, current as of the latest *arrêté* on notary tariffs).

| Territory | *Émoluments* uplift | Source |
|-----------|---------------------|--------|
| Métropole | baseline (0%) | A444-53 et seq. |
| `gp` Guadeloupe | **+23%** | A444-53 et seq. |
| `mq` Martinique | **+24%** | A444-53 et seq. |
| `gf` Guyane | **+25%** | A444-53 et seq. |
| `re` La Réunion | **+40%** | [Autorité de la concurrence Avis 19-A-09 du 11 avril 2019](https://www.autoritedelaconcurrence.fr/sites/default/files/commitments/19a09.pdf), § notaires |
| `yt` Mayotte | **+40%** | Autorité de la concurrence Avis 19-A-09 |

**Total *frais d'acquisition* — what the buyer actually pays at signing:**

The *frais de notaire* line on the *acte authentique* is mostly *droits de mutation à titre onéreux (DMTO)* + small *émoluments*. Because DMTO is the dominant share (~5–5.8% of the price for second-hand) and is set by *département*, total *frais* land **similar to métro (~7–8% for second-hand, ~2–3% for new-build VEFA)**, with the *émoluments* uplift adding a marginal premium (typically ~0.1–0.3% of the headline price in absolute terms — ~est. computed from a typical 1% *émoluments* base × the 23–40% uplift). Verify the exact line items in the *projet d'acte* before signing.

> **Rule for the skill:** when a user lists "frais de notaire" for a DROM, do NOT silently apply a metro 7–8% template. Pull the *émoluments* uplift from the table above, and verify *DMTO départemental* against the [conseil départemental / DGFiP](https://www.impots.gouv.fr/) page for the specific DROM (rates can be temporarily increased per LFI provisions — see metro playbook for the same mechanism).

---

## 7. Indivision crisis — *Loi Letchimy* n° 2018-1244

The *indivision successorale* problem in DROM (especially `yt` Mayotte and `gf` Guyane) is structurally larger than in métro France. Decades of incomplete probate, missing *actes de notoriété*, and oral inheritance customs have left a large share of land held in unresolved co-ownership across many heirs (often dozens, sometimes across generations).

**What** *indivision* **is:** a French civil-law regime (*Code civil* Art. 815 et seq.) where multiple co-owners hold undivided shares of an estate. **Unanimity rule for sale:** under the standard regime, any sale of an *indivis* property requires unanimous consent of all *indivisaires* (with limited Art. 815-5-1 exceptions).

**The Letchimy law** ([LOI n° 2018-1244 du 27 décembre 2018](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037864059), official title: *visant à faciliter la sortie de l'indivision successorale et à relancer la politique du logement en outre-mer*) creates a **DROM-specific exception**: in the five DROM + Saint-Martin + Saint-Barthélemy + Saint-Pierre-et-Miquelon, when an *indivision successorale* has been open for **more than 10 years** and the heirs holding **more than half** (vs unanimous in metro) of the *droits indivis* agree, they can force the sale or the partition — substantially lowering the threshold to unlock blocked estates.

- The law was initially time-limited to **10 years from publication** (so to 31 Dec 2028) — verify the latest extension status against Légifrance before relying on the deadline.
- **Why it matters to a buyer:** if you see a DROM listing where the seller is "*one of several heirs*", check whether the *acte* is being signed under Art. 815 metropolitan rules (needs unanimity) or under Letchimy-law majority rules. The two have different legal bases and different risk of post-sale challenge.

**Practical due-diligence pattern for DROM buyers:**
1. Demand the *acte de notoriété* identifying all *indivisaires*.
2. Ask the seller's *notaire* explicitly: *"L'opération est-elle conduite au titre de la loi n° 2018-1244 ou du régime de droit commun de l'article 815 du Code civil ?"*
3. If Letchimy-based, confirm the >10-year clock and the majority threshold are met *in writing* in the *acte authentique*.

---

## 8. Cadastre deficit caveats — YT and GF first, GP/MQ/RE generally fine

Primary source: [**Cerema — Guide foncier Outre-Mer (2023)**](https://outil2amenagement.cerema.fr/sites/outils2am/files/fichiers/2023/08/Guide_foncier_Outre-Mer.pdf), companion volume [Cerema — La clarification des désordres fonciers (2023)](https://outil2amenagement.cerema.fr/sites/outils2am/files/fichiers/2023/08/Foncier_Outre-Mer_clarification_des_desordres_fonciers.pdf).

> Cerema, verbatim (2023): *"À Mayotte, la mobilisation du foncier est confrontée à un cadastre très lacunaire, une absence de titrement des propriétés ou la présence importante d'habitat informel."*

**Implications for property buyers — per-DROM verdict:**

| DROM | Cadastre status | Buyer guidance |
|------|-----------------|----------------|
| `gp` Guadeloupe | Complete, DGFiP-maintained, full *plans cadastraux* | Normal metro-equivalent DD ([cadastre.gouv.fr](https://www.cadastre.gouv.fr/)) |
| `mq` Martinique | Complete, DGFiP-maintained | Normal metro-equivalent DD |
| `gf` Guyane | Coastal communes covered; **interior + Maroni/Oyapock river borders have cadastre gaps**; informal occupation common in the interior | Verify cadastre coverage at the *parcelle* level via DGFiP service du cadastre for the specific commune before any commitment |
| `re` La Réunion | Complete, DGFiP-maintained | Normal metro-equivalent DD |
| `yt` Mayotte | **VERY DEFICIENT** — Cerema-acknowledged gaps in titrement, large share of informal housing (~30%+ of dwellings per various estimates — verify against latest INSEE *Logement Mayotte*), ongoing *Commission d'urgence foncière* (CUF) titrement programme | **Treat any YT transaction as high-risk on title chain.** Do not close without (a) a *notaire*-issued *acte de notoriété* establishing chain of title, (b) CUF clearance for the parcel if relevant, (c) physical *bornage* by a *géomètre-expert*. **Confidence: MEDIUM** for any YT listing-derived claim. |

---

## 9. Per-DROM natural-hazard + neighborhood specifics

> Pull each section into the relevant `risks_natural` / `risks_climate` / `mains_reliability` slot of the standard skill output. Verify against the [Préfecture *Dossier départemental des risques majeurs* (DDRM)](https://www.gouvernement.fr/risques) for the specific DROM before publishing in a buyer brief.

### `gp` Guadeloupe (Lesser Antilles — Caribbean)

- **Cyclones:** Atlantic hurricane season Jun–Nov; Cat-4/5 hits historically (Hugo 1989, Maria 2017). Build to both the *règles parasismiques* (zonage + rules under décrets n° 2010-1254 and n° 2010-1255 du 22 oct. 2010; since **1 Jan 2024** an *attestation de prise en compte de la règlementation parasismique* is required from the maître d'ouvrage on **every new build** — [ministère de la Transition écologique](https://www.ecologie.gouv.fr/politiques-publiques/tremblements-terre-seismes-france)) **and** the *règles paracycloniques*, which sit in the Code de la construction et de l'habitation arts. **R.132-2-1 à R.132-2-5** ("Prévention des risques cycloniques", inserted by **décret n° 2023-1087 du 23 nov. 2023**) and cover **Guadeloupe, Martinique, La Réunion and Mayotte** — **Guyane is not in the cyclonic-risk zone list**; the implementing joint *arrêté* under R.132-2-5 enters into force no later than **1 Jan 2026** — confirm it has been published before relying on the detailed rules ([Légifrance — CCH Section 3](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043818701); 2026-09-18 verified).
- **Seismicity:** **Zone 5 (forte sismicité)** per the seismic-zonation decree (CGI Art. R563-4, [Légifrance](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000023086525)). Subduction zone (Caribbean plate / North American plate). PGA design accelerations are the highest tier in the French regulatory framework.
- **Volcanic:** *La Soufrière* (massif of *La Grande Découverte*), active stratovolcano on Basse-Terre. Monitored by [Observatoire volcanologique et sismologique de Guadeloupe (OVSG-IPGP)](https://www.ipgp.fr/en/observation/ovs/ovsg/). Last significant phreatic crisis 1976–1977 (evacuation of Basse-Terre). Yellow-alert status periodically.
- **Tsunami:** Caribbean tsunami exposure (e.g., 1867 Virgin Islands earthquake). Coastal `gp` communes in PPR-tsunami zoning.

### `mq` Martinique (Lesser Antilles — Caribbean)

- **Cyclones:** same Atlantic season Jun–Nov; Cat-4/5 exposure.
- **Seismicity:** **Zone 5 (forte sismicité)** — same Caribbean subduction frame as `gp` ([Légifrance R563-4](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000023086525)).
- **Volcanic:** *Montagne Pelée*, active stratovolcano in the north. **8 May 1902 Pelée *nuée ardente* destroyed Saint-Pierre, ~28,000 dead** — the deadliest volcanic disaster of the 20th century. Currently monitored by [Observatoire volcanologique et sismologique de Martinique (OVSM-IPGP)](https://www.ipgp.fr/en/observation/ovs/ovsm/). Yellow-alert status since Dec 2020.
- **Tsunami:** Caribbean exposure analogous to `gp`.

### `gf` Guyane (Amazon basin — South America)

- **Cyclones:** **None of material concern.** Guyane sits below the typical Atlantic hurricane track; tropical depressions occur but not Cat-2+ storms (verify against [Météo-France Guyane](https://meteofrance.gp/fr/) historical climatology).
- **Seismicity:** **Zone 1 (très faible)** per CGI R563-4 — Guianese Shield is tectonically stable.
- **Flooding:** Major risk. Maroni river (Surinamese border) and Oyapock river (Brazilian border) annual flood cycles; interior communes can be inundated for weeks. Coastal flooding (Cayenne, Kourou, Saint-Laurent-du-Maroni) tracked in [PPRI Guyane](https://www.guyane.developpement-durable.gouv.fr/).
- **Other:** dense tropical-forest insolation/humidity (build for high humidity — mold, termites *Coptotermes*); HIV/dengue/leptospirosis health profile relevant for buy-to-let medical-screening tenants; gold-mining-related mercury contamination on some interior watercourses (verify against [ARS Guyane](https://www.guyane.ars.sante.fr/) before any river-front purchase).
- **Economic anchor:** [**Centre spatial guyanais (CSG) at Kourou**](https://centrespatialguyanais.cnes.fr/) — Ariane / Vega launch site operated by CNES + ESA + Arianespace. Drives the Kourou + Cayenne real-estate market via expat staffing.

### `re` La Réunion (Mascarene archipelago — SW Indian Ocean)

- **Cyclones:** SW Indian Ocean cyclone season Nov–Apr. Less frequent than Caribbean Cat-5 but historically severe (Cyclone Hyacinthe 1980, Bejisa 2014, Belal 2024). Build to *règles paracycloniques* per *arrêté préfectoral*.
- **Seismicity:** **Zone 2 (faible)** per CGI R563-4 — hot-spot volcanism dominates over plate-boundary stress.
- **Volcanic:** *Piton de la Fournaise*, **one of the most active basaltic shield volcanoes on Earth** — typical eruption frequency 1–2 per year, monitored by [Observatoire volcanologique du Piton de la Fournaise (OVPF-IPGP)](https://www.ipgp.fr/en/observation/ovs/ovpf/). Eruptions mostly confined to *Enclos Fouqué* zone (low risk to populated areas), but *hors-Enclos* lava-flow risk in *PPR volcanique* zones (Sainte-Rose, Le Tampon).
- **Landslide:** *Cirques* topography (Mafate, Salazie, Cilaos) — high landslide / *éboulement* risk on steep slopes. PPR-mouvements de terrain coverage essential.

### `yt` Mayotte (Comoros archipelago — SW Indian Ocean)

- **Cyclones:** SW Indian Ocean basin, **less frequent direct hits than Réunion** (Mayotte sits further north). However, 2024 Cyclone Chido (Cat-4, 14 Dec 2024) caused catastrophic damage — the most severe in ~90 years — and demonstrated that the historical "lower exposure" framing should not lead to under-engineering. ([Météo-France Mayotte](https://meteofrance.yt/fr/) bilan-cyclone reports.)
- **Seismicity:** Was **Zone 2 (faible)** historically — but reclassified upward in practice since the **2018–2019 Mayotte seismic crisis**. Over [~2,000 felt earthquakes recorded in 2018–2019](http://www.outre-mer.gouv.fr/surveillance-de-fani-maore-volcan-sous-marin-mayotte-lengagement-de-letat-renforce), driven by the submarine volcanic event below.
- **Volcanic — Fani Maoré:** in May 2019 a new submarine volcano was discovered **~50 km east of Mayotte** at ~3,500 m water depth — the volcanic edifice itself rises ~800 m above the seafloor (verify against [CNRS Le Journal — Fani Maoré](https://lejournal.cnrs.fr/articles/fani-maore-le-volcan-sous-marin-qui-a-fait-trembler-mayotte) and BRGM publications). Now officially named **Fani Maoré**, monitored by [REVOSIMA (BRGM/IPGP/Ifremer/CNRS) network](https://www.ipgp.fr/en/observation/national-hosted-infrastructures/revosima/). **This is currently the largest active submarine eruption documented anywhere on Earth.** Implication for property: Mayotte real estate now sits in a known active-volcanic + active-seismic context that is *not yet fully reflected in the regulatory zonation* — apply a precautionary premium.
- **Tsunami:** Mayotte 2018+ event sequence has raised local tsunami-modelling work (BRGM); verify PPR-tsunami status per commune.

> **Anti-hallucination correction.** Fani Maoré is **~50 km east of Mayotte**, not 800 km. The 800-figure is the edifice **height** (~800 m above seafloor). Do not propagate the wrong distance.

---

## 10. Foreign-buyer eligibility — same as metropolitan France

**No DROM-specific restriction.** Because the DROM are integral to the French Republic and EU territory, the metropolitan FR rules apply unchanged:

- EU/EEA/Swiss buyers: full eligibility, no permit ([countries/fr/playbook.md § Foreign-buyer eligibility](../countries/fr/playbook.md)).
- Non-EU buyers: no purchase restriction; standard *acte authentique* + tax-residency rules apply. Non-tax-resident landlords are subject to *prélèvement social* + *prélèvement à la source* on rental income per CGI Art. 197 A.
- *DROM-specific:* no zone-restriction list, no agricultural-land cap unique to DROM beyond the metro *SAFER* preemption right (which DOES apply in DROM).

> **Beware of false-positive scam pattern.** "*You need a special DROM foreign-buyer permit*" is a known social-engineering script. There is no such permit. Verify any such claim against [service-public.fr](https://www.service-public.fr/) or *direction de l'immobilier de l'État* before paying any fee.

---

## 11. Source URL templates table

| Anchor | URL | What to use it for |
|--------|-----|--------------------|
| DGFiP — TVA DOM | https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom | TVA rates per DROM |
| BOFiP — TVA géographique | https://bofip.impots.gouv.fr/bofip/343-PGP.html/identifiant=BOI-TVA-GEO-20-10-20190605 | Definitive TVA-DOM doctrine |
| BOFiP — Taxe foncière outre-mer | https://bofip.impots.gouv.fr/bofip/4844-PGP.html (HLM) · https://bofip.impots.gouv.fr/bofip/11858-PGP.html/identifiant=BOI-IF-TFB-20-30-45-20260204 (ZFA) | Per-mechanism abattement rules |
| Légifrance — Octroi de mer | https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294 | Loi 2004-639 statutory text |
| Douane — Octroi de mer | https://www.douane.gouv.fr/lexique/octroi-de-mer | Current administrative guidance + tariff lookup |
| Légifrance — Loi Letchimy | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037864059 | LOI n° 2018-1244 — indivision DROM |
| Légifrance — Tarifs notaires (DROM uplifts) | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000032132058 | Articles A444-53 et seq. |
| Autorité de la concurrence — avis tarifs notaires | https://www.autoritedelaconcurrence.fr/sites/default/files/commitments/19a09.pdf | Cross-checked DROM uplift table (RE + YT = 40%) |
| INSEE — Mayotte essentials | https://www.insee.fr/fr/statistiques/4632225 | Mayotte demographic + economic baseline |
| INSEE — Guyane essentials | https://www.insee.fr/fr/statistiques/4313999 | Guyane demographic + economic baseline |
| INSEE — Martinique essentials | https://www.insee.fr/fr/statistiques/4482393 | Martinique baseline |
| INSEE — Dossier complet *par département* | https://www.insee.fr/fr/statistiques/2011101?geo=DEP-971 (replace 971→972/973/974/976) | Per-DROM full statistical dossier |
| Cerema — Guide foncier Outre-Mer | https://outil2amenagement.cerema.fr/sites/outils2am/files/fichiers/2023/08/Guide_foncier_Outre-Mer.pdf | Definitive cadastre + indivision DD framework |
| Cerema — Désordres fonciers (companion) | https://outil2amenagement.cerema.fr/sites/outils2am/files/fichiers/2023/08/Foncier_Outre-Mer_clarification_des_desordres_fonciers.pdf | DD procedures + actor list |
| Seismic zonation (CGI R563-4) | https://www.legifrance.gouv.fr/loda/id/LEGITEXT000023086525 | Statutory seismic-zone mapping per DROM |
| REVOSIMA (Mayotte volcano network) | https://www.ipgp.fr/en/observation/national-hosted-infrastructures/revosima/ | Fani Maoré + Mayotte seismic monitoring |
| OVPF (Réunion) | https://www.ipgp.fr/en/observation/ovs/ovpf/ | Piton de la Fournaise eruption bulletins |
| OVSG (Guadeloupe) | https://www.ipgp.fr/en/observation/ovs/ovsg/ | Soufrière bulletins |
| OVSM (Martinique) | https://www.ipgp.fr/en/observation/ovs/ovsm/ | Pelée bulletins |

---

## Status

| DROM | Confidence | Key uncertainty |
|------|------------|-----------------|
| `gp` Guadeloupe | **HIGH** | Octroi de mer per-commune rate must be looked up at transaction time |
| `mq` Martinique | **HIGH** | Same |
| `re` La Réunion | **HIGH** | Confirm seismic zoning hasn't been revised post-Fournaise activity |
| `gf` Guyane | **MEDIUM-HIGH** | Cadastre coverage gaps in interior; flood-plain mapping varies by commune; no TVA but octroi de mer applies |
| `yt` Mayotte | **MEDIUM** | Cadastre very deficient (Cerema 2023); informal-housing prevalence; seismic + volcanic context active and not yet fully reflected in pre-2019 zonation; full census Nov 2025–Feb 2026 will update demographic baseline |

**Last verified:** 2026-05-27 (DROM paracyclonique construction rules corrected 2026-09-18 per Legifrance CCH arts. R.132-2-1 to R.132-2-5).

**Maintenance cadence:**
- TVA rates / *octroi de mer* — verify annually against LFI (loi de finances initiale) revisions.
- Notary *émoluments* uplifts — verify against latest *arrêté* on A444 tariffs.
- Letchimy law deadline — verify extension status against Légifrance before relying on the 10-year clock.
- Mayotte cadastre / CUF programme — verify against latest *outre-mer.gouv.fr* publications.
- Volcano alert levels — verify against IPGP observatory bulletins per transaction.

**Per-listing reminder:** every numeric or fiscal claim derived from this overlay must still be re-verified against the seller's *avis d'imposition*, *acte authentique*, and *certificat d'urbanisme* (CU) for the specific parcel before being relied upon in a buyer brief.
