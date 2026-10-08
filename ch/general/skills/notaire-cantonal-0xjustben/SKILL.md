---
name: notaire-cantonal-0xjustben
title: Cantonal Notary / Notaire
description: 'Swiss cantonal notary / notaire / Notar / notaio co-pilot.

  Use when the user mentions: notarial deed (acte authentique, öffentliche Urkunde, atto pubblico), real-estate sale (vente immobilière, Grundstückkauf), mortgage note (cédule hypothécaire, Schuldbrief), easement / servitude (Dienstbarkeit), condominium constitution (PPE, Stockwerkeigentum, CC 712d), inheritance / succession (CC 457–640), will (testament, testamento, holographic / public / Erbvertrag), executor (exécuteur testamentaire, Willensvollstrecker), matrimonial regime (régime matrimonial, Güterstand), prenup (contrat de mariage, Ehevertrag), SA/AG formation (CO 620), GmbH/Sàrl formation (CO 772), capital increase / reduction, merger / demerger (LFus / FusG), transfer-duty (droits de mutation, Handänderungsabgabe), inheritance tax (cantonal).

  Notariat NOT unified — 3 systems: Latin (GE, VD, VS, FR, NE, JU, TI), free (ZH, SH, AR), mixed (BE, SO, LU, ZG, BS, BL, AG, etc.). **Identify canton FIRST**. Reads cantonal data from data/cantons/<XX>.json field `notariat`.'
author: 0xjustBen
author_url: https://github.com/0xjustBen/paperwork-switzerland/tree/main/notaire-cantonal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ch
practice: general
language: en
sources:
- title: Readme
  path: references/immobilier/README.md
- title: Cedule Hypothecaire
  path: references/immobilier/cedule-hypothecaire.md
- title: Compromis Vente
  path: references/immobilier/compromis-vente.md
- title: Droit Preemption
  path: references/immobilier/droit-preemption.md
- title: Gains Immobiliers Canton
  path: references/immobilier/gains-immobiliers-canton.md
- title: Readme
  path: references/societes/README.md
- title: Sa Formation
  path: references/societes/sa-formation.md
- title: Sarl Formation
  path: references/societes/sarl-formation.md
- title: Transferts Actions
  path: references/societes/transferts-actions.md
- title: Succession Reform 2023
  path: references/succession-reform-2023.md
---

# Cantonal Notary / Notaire

Swiss notariat **not unified**. **Identify canton FIRST**. Wrong canton → wrong system → wrong tariff + wrong procedure.

## When to invoke

Trigger on: real-estate transfer, mortgage-note issuance, PPE constitution, will / pact drafting, prenup, succession opening, SA/GmbH formation, capital change, merger, donation immo, usufruct setup.

## Workflow

1. **Canton identification** (mandatory first step): ask if not given. Load `data/cantons/<XX>.json` → field `notariat` (Latin / Free / Mixed) + cantonal tariff + transfer-duty rate.
2. **Matter classification**: real estate / succession / matrimonial / company / other.
3. **Form check**: authentic form required (most below) → cantonal notary competent.
4. **Cantonal competence**: situs rule for real estate (lex rei sitae); domicile rule for succession (CC 538); registered seat rule for companies (CO 626).
5. **Document list + parties' presence + identity check** (LBA/GwG anti-laundering for cash > CHF 100k).
6. **Filing**: registre foncier / Handelsregister / registre du commerce within deadline.
7. **Output**: deed type + cantonal basis + estimated fees + transfer-duty + next-step deadline.

## Three notarial systems

| System | Cantons | Characteristic | Fee logic |
|---|---|---|---|
| **Latin** | GE, VD, VS, FR, NE, JU, TI | Independent notary, public officer | Fixed cantonal tariff (often % of value) |
| **Free** | ZH, SH, AR | Private notaries in competition | Negotiable for some matters |
| **Mixed / state** | BE, SO, LU, ZG, BS, BL, AG, GR, GL, NW, OW, SG, SZ, TG, UR, ZG | Civil servants OR semi-public | Cantonal salary scale or capped tariff |

→ See `data/cantons/<XX>.json` field `notariat` for precise system.

## Real estate (CC 655–977)

| Operation | Form | Article |
|---|---|---|
| Sale | Authentic deed | **CC 657** |
| Donation immo | Authentic deed | CC 243 |
| Mortgage note (paper / register) | Authentic deed | **CC 842 ss** |
| Easement / servitude | Authentic deed | CC 730 ss |
| Usufruct on immo | Authentic deed | CC 745 |
| Condominium constitution | Authentic deed + regulation | **CC 712d** |
| Exchange | Authentic deed | CC 237 |

```bash
node ../scripts/calc.js mutation --canton GE --price 1200000
```

### Transfer duties (cantonal range)

| Range | Cantons |
|---|---|
| **0 %** (or near) | ZH, ZG, SZ (partial), AR |
| 0.8–1.5 % | UR, OW, NW, SG, GR |
| 1.5–2.5 % | BE, LU, BS, BL, AG, SO, TG, GE (3 % w/ communal) |
| **Up to 3.3 %** | VD, VS, FR, NE, JU, TI |

→ `data/cantons/<XX>.json.fiscalite.droits_mutation_immo_pct`.

### Edge cases — real estate

- **Reservation contract** (promesse de vente): authentic in VD, GE, FR — simple written form NOT enough.
- **Pre-emption right** (droit de préemption, CC 681): contractual variants require notarial form for > 25 years.
- **Foreigner acquisition** (Lex Koller / LFAIE): non-resident non-EU/EFTA needs authorization for residential property; secondary-residence permits restricted.
- **Cantonal LDTR / LPPPL** (GE, VD): demolition / renovation permits — closure condition for deed.
- **LRS / ZWG**: secondary-residence cap 20 % in affected communes (Verbier, Crans-Montana, St-Moritz, Zermatt) — verify before signing.

## Succession (CC 457–640)

### 2023 reform (in force since 2023-01-01)

- **Compulsory share descendants**: reduced **3/4 → 1/2**.
- **Parents' compulsory share**: **abolished**.
- **Spouse**: 1/2 of estate, of which 1/4 compulsory.
- **Increased disposable quota** → more flexibility for will + inheritance pact.

### Will forms

| Form | Requirements | Article |
|---|---|---|
| Holographic | Entirely handwritten + dated + signed | CC 505 |
| Public | Notary + 2 witnesses | CC 499–504 |
| Oral (emergency) | 2 witnesses, must be transcribed within days | CC 506–508 |
| Inheritance pact (Erbvertrag) | Notary + 2 witnesses, binding contract | CC 512 |

### Edge cases — succession

- **Renunciation pact** (CC 495): heir waives in advance for compensation — irrevocable, notarial.
- **Donations rapportables** (CC 626): gifts to descendants in last 5 y reintegrated unless dispensed.
- **Executor** (Willensvollstrecker, CC 517): designation in will; accepts within 14 days of notice.
- **Inheritance tax** (cantonal):
  - Spouse + direct descendants: **exempt in most cantons**.
  - Exceptions: **VD, NE, JU, AI** — partial tax on descendants in some cases.
  - Collaterals: progressive 10–55 % depending on canton + relation.
- **International succession**: domicile at death (CC 538 + LDIP 86); EU successor regulation does NOT bind CH.
- **Forced heir contesting will**: 1-year action from knowledge (CC 533).

## Matrimonial regimes (CC 181–251)

| Regime | Default? | Notarial form |
|---|---|---|
| **Participation in acquired property** (default since 1988) | ✓ | None to adopt; notarial only for modifications |
| **Separation of property** | Choice | **Notarial contract** (CC 184) |
| **Community of property** (universal or limited) | Choice | **Notarial contract** (CC 184) |

### Edge cases — matrimonial

- **Prenup** (contrat de mariage): before or during marriage, notarial.
- **Post-nup conversion**: must liquidate prior regime first (CC 204).
- **Foreign spouses**: applicable law per LDIP 52 ss — first common domicile, then nationality.
- **Pillar 3a + 2nd pillar**: outside matrimonial regime but split on divorce (CC 122).

## Company law

| Operation | Form | Min capital | Article |
|---|---|---|---|
| **SA / AG formation** | Authentic deed | **CHF 100,000** (≥ 20 % paid, min CHF 50,000) | **CO 620 ss** |
| **GmbH / Sàrl formation** | Authentic deed | **CHF 20,000** fully paid | **CO 772 ss** |
| Capital increase (cash) | Authentic deed | — | CO 650 |
| Capital increase (kind / set-off / intended takeover) | Authentic deed + **audit confirmation** | — | **CO 634b, 652f** |
| Capital reduction | Authentic deed + **audit + 3 creditor calls** | — | **CO 732 ss** |
| Merger / demerger / transformation | Authentic deed + audit | — | **LFus 12, 41, 62** |
| Dissolution / liquidation | Authentic deed (if SA/GmbH) | — | CO 736 |

→ Audit confirmation required → cross-skill `reviseur-agree`.

## LBA / GwG check

Cash transactions or apport > **CHF 100,000**: identify beneficial owner, source of funds, retain documentation (LBA art. 4 ss + DFI Verordnung).

## Outputs

Always indicate:
- **Canton identified** + notarial system (Latin / Free / Mixed).
- **Legal basis** (CC / CO article).
- **Estimated fees** from cantonal tariff (`data/cantons/<XX>.json.notariat.tarif`).
- **Transfer duty** if real estate (`data/cantons/<XX>.json.fiscalite.droits_mutation_immo_pct`).
- **Inheritance tax** estimate if succession.
- **Required documents** + **parties' presence** + identity verification (passport / ID).
- **Filing deadline** (registre foncier: 30 d typical; Handelsregister: immediately after signing).

## Scope boundaries

- Tax optimization of structure → skill `expert-fiscal`.
- Audit confirmations for capital deeds → skill `reviseur-agree`.
- Real-estate management / rent → skill `regie`.
- SME bookkeeping post-incorporation → skill `fiduciaire`.

## Worked example

> "GmbH transformation into AG, capital CHF 100,000, canton VD."

1. **Canton VD**: Latin system → fixed cantonal tariff (`data/cantons/VD.json.notariat.tarif`).
2. **Procedure** (LFus 53 ss): transformation deed, **no liquidation**.
3. **Capital**: existing CHF 20k GmbH + top-up CHF 80k → CHF 100k. Min 20 % paid → ≥ CHF 50k.
4. **Audit confirmation**: required (LFus 62 + CO 634b). Engage `reviseur-agree`.
5. **Documents**: transformation balance sheet (date ≤ 6 months), audit report, revised statutes, board resolution, transformation plan.
6. **Filing**: Handelsregister VD within 3 months of audit report; effective on RC publication (FOSC).
7. **Estimated fees**: notary tariff ≈ CHF 2,500–4,000 + RC fees CHF 600 + audit CHF 1,500–3,000.
