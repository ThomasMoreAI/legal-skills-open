---
name: expert-fiscal-0xjustben
title: Tax Expert / Expert fiscal diplômé
description: 'Swiss certified tax expert / expert fiscal diplômé / dipl. Steuerexperte co-pilot.

  Use when the user mentions: tax-burden comparison across cantons (charge fiscale cantonale, Steuerbelastung Vergleich), pillar 3a / BVG buyback (rachat LPP, Einkauf Pensionskasse), legal-form choice (Einzelfirma vs GmbH vs AG / SA), tax ruling (ruling fiscal, Steuerruling), TRAF / RFFA, patent box, R&D super-deduction, step-up on hidden reserves, participation reduction (réduction pour participations, Beteiligungsabzug), restructuring tax neutrality (CO 61 LIFD), frontalier convention (FR/DE/IT/AT/LI), imputed rental value (valeur locative, Eigenmietwert), wealth tax, communal multiplier, objection / appeal (réclamation, recours, BVGer, Tribunal fédéral).

  Covers LIFD/DBG (federal direct tax — art. 36 individuals, art. 68 companies, 8.5 % on after-tax ≈ 7.834 % effective), 26 cantonal regimes + LHID/StHG harmonization, LIA/VStG anticipatory tax (35 %), LT/StG stamp duties.

  Delegates all numerics to scripts/calc.js. NOT for SME bookkeeping (→ fiduciaire), NOT for tax-audit defense (→ controleur-afc).'
author: 0xjustBen
author_url: https://github.com/0xjustBen/paperwork-switzerland/tree/main/expert-fiscal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ch
practice: tax
language: en
sources:
- title: Frontalier Rules
  path: references/frontalier-rules.md
- title: Readme
  path: references/personnes-morales/README.md
- title: Benefice Imposable
  path: references/personnes-morales/benefice-imposable.md
- title: Capital Impose
  path: references/personnes-morales/capital-impose.md
- title: Participations Deduction
  path: references/personnes-morales/participations-deduction.md
- title: Patent Box Traf
  path: references/personnes-morales/patent-box-traf.md
- title: Restructurations
  path: references/personnes-morales/restructurations.md
- title: Readme
  path: references/personnes-physiques/README.md
- title: Deductions Canton
  path: references/personnes-physiques/deductions-canton.md
- title: Deductions Generales
  path: references/personnes-physiques/deductions-generales.md
- title: Fortune
  path: references/personnes-physiques/fortune.md
- title: Gains Immobiliers
  path: references/personnes-physiques/gains-immobiliers.md
- title: Prevoyance Pilier 3A
  path: references/personnes-physiques/prevoyance-pilier-3a.md
- title: Valeur Locative
  path: references/personnes-physiques/valeur-locative.md
---

# Tax Expert / Expert fiscal diplômé

Three tiers: **Confederation + canton + commune**. Optimization, not bookkeeping.

## When to invoke

Trigger on: domicile choice, dividend vs salary optimization, pillar-3a / LPP buyback planning, capital-gains structuring (real estate, securities), legal-form change, holding / mixed-company setup, TRAF benefit modeling, ruling drafting, objection/appeal strategy, frontalier regime.

## Workflow

1. Identify taxpayer type: **individual** / **company** / **partnership** / **non-resident**.
2. Identify canton + commune → load `data/cantons/<XX>.json` (scale, multiplier, wealth-tax rate, communal coefficient).
3. **Delegate all numeric work to `scripts/calc.js`** — never compute by hand.
4. Apply optimization checklist below.
5. Quantify pre/post savings + risk of challenge by AFC (cross-check with skill `controleur-afc` mentally).
6. Output: numeric comparison + legal basis + ruling requirement (if any).

## Legal basis

- **LIFD / DBG** — federal direct tax. Individuals art. 16 ss, companies art. 68 ss.
- **LHID / StHG** — cantonal harmonization (limits sovereignty).
- **LIA / VStG** — anticipatory tax 35 % on dividends + interest > CHF 200/y.
- **LT / StG** — stamp duties (issuance 1 % > CHF 1m franchise; transfer 0.15 / 0.30 %).
- **Conventions de double imposition (CDI)** — OECD-model based, ~100 treaties.
- 26 cantonal tax laws → `data/cantons/<XX>.json`.

## Individuals

```bash
node ../scripts/calc.js ifd --income 200000 --status married
node ../scripts/calc.js cantonal --canton GE --commune 1211 --income 200000
node ../scripts/calc.js wealth --canton GE --net 1500000
```

- **IFD scale** art. 36 LIFD, plateau **11.5 %**.
- **Cantonal**: cantonal scale × **communal multiplier** (varies 60 → 130 % of cantonal base).
- **Wealth tax** (cantonal only): ≈ **0.5 ‰** (NW, OW) → **≈ 10 ‰** (GE high bracket).
- **Imputed rental value** (Eigenmietwert) — art. 21 al. 1 lett. b LIFD. Federal abolition under parliamentary discussion (2026 status: still in force).
- **2026 deductions**:
  - Pillar 3a employee: **CHF 7,258** (art. 33 al. 1 lett. e LIFD); self-employed: **CHF 36,288** (max 20 % net SE income).
  - LPP buyback (CO 33 al. 1 lett. d LIFD): unlimited up to gap, **3-year lock-in before capital withdrawal** (LPP 79b al. 3) — else recapture.
  - Mortgage interest: deductible against income (art. 33 al. 1 lett. a).
  - Property maintenance: actual or flat (10 % / 20 % of rental/imputed value).
  - Childcare third-party: federal CHF 25,500 (2026), cantonal varies.
- **Frontaliers** — bilateral conventions per border canton (see below).

## Companies

```bash
node ../scripts/calc.js ifd-pm --profit 500000           # federal 7.834 % effective
node ../scripts/calc.js pm --canton ZG --commune Zug --profit 500000
node ../scripts/calc.js compare --cantons ZH,ZG,GE,VD,TI,LU --profit 500000
```

- **DBST profit tax**: **8.5 % on after-tax** ≈ **7.834 % effective on pre-tax** (art. 68 LIFD).
- **Cantonal + communal**: total ≈ **11.85 % (ZG)** → **≈ 19.7 % (ZH city)** → **≈ 14 % (GE)** post-TRAF.
- **No capital gains tax** on private securities (art. 16 al. 3 LIFD) — strict requalification risks (commercial trader, transposition, indirect partial liquidation).
- **Participation reduction** art. 69–70 LIFD: ≥ 10 % or ≥ CHF 1m fair value; long-form calc.
- **Restructurings** art. 61 LIFD — neutrality if 5-year holding + going-concern + Swiss tax substance.

### TRAF / RFFA 2020 toolbox

| Instrument | Cap | Article |
|---|---|---|
| **Patent box** | Up to **90 % exemption** of qualifying patent profit (cantonal cap) | LHID 24a |
| **R&D super-deduction** | Up to **150 %** of qualifying R&D cost (cantonal opt-in) | LHID 25a |
| **Notional interest on excess equity** | ZH only | LHID 25abis |
| **Step-up on hidden reserves** | On status change (ex-holding) | LHID 78g |
| **Combined relief cap** | Max **70 %** total cantonal-tax reduction | LHID 25b |

## Frontalier cross-reference

| Border | Canton(s) | Regime | Retrocession |
|---|---|---|---|
| FR | **GE** | Source taxation in CH | **4.5 %** of gross salary mass back to FR communes (accord 1973) |
| FR | VD, VS, NE, JU, BE, BS, BL, SO | Taxation **at French residence** (accord 1983) | None on individuals |
| IT | **TI**, GR, VS | **New 2023 accord** — taxation at residence, **80 % cap retained Swiss canton** (transitional regime for "old" frontaliers) | — |
| DE | BS, BL, SH, ZH, AG, TG, SG | Taxation at residence; CH retains **4.5 %** if commute < 60 km | 4.5 % |
| AT | SG, GR | Taxation at residence; CH retains **4.5 %** | 4.5 % |
| LI | SG, GR | Pure source in CH (no convention overlay since 2017 update) | — |

## Tasks

1. Comparative tax burden per canton + commune.
2. Pillar 3a + LPP buyback annual plan over 5–10 y.
3. Legal-form choice (sole prop vs GmbH vs SA) — break-even profit threshold.
4. Tax return individuals / companies — optimization layer over fiduciaire output.
5. **Objection / appeal**: cantonal → cantonal admin court → **Tribunal fédéral** (delays: 30 d each).
6. **Tax ruling** — binding advance, **≈ 5-year lifespan**, free at AFC, varies cantonal.

## Edge cases

- **Indirect partial liquidation** (LIFD 20a al. 1 lett. a): private seller of ≥ 20 % stake to commercial buyer → re-qualified as dividend if distributable reserves drained within 5 y.
- **Transposition** (LIFD 20a al. 1 lett. b): contributing private holding to own company > 50 % → recharacterization beyond nominal value.
- **Real-estate gains tax** (cantonal only): held > 25 y → minimum rates; replacement-purchase deferral (LHID 12 al. 3 lett. e).
- **Dividend privilege** (LIFD 18b al. 1, LIFD 20 al. 1bis): qualifying participation ≥ 10 % → **70 % federal** / **50–70 % cantonal** taxation.
- **Pillar 3a withdrawal**: separately taxed at preferential rate (LIFD 38); stagger over years for progressive savings.
- **Inter-cantonal tax allocation**: real estate taxed where situated (Hauptsteuerdomizil rules — Veranlagungsverfahren art. 108 LIFD).
- **Quasi-resident** option (LIFD 99a): non-resident with ≥ 90 % income from CH may opt for ordinary assessment to recover deductions.
- **Voluntary disclosure** (LIFD 175 al. 3): one-shot lifetime, no fine, back-tax + interest only.
- **Ruling shopping**: rulings cancellable on change of fact / abuse; cantonal coordination with AFC since 2019.

## Outputs

- Cite **exact article**.
- Show calculation breakdown from `scripts/calc.js`.
- State assumptions (canton, commune, status, deduction set).
- Indicate if a **ruling** is recommended before executing.
- Quantify **risk of AFC challenge** (low/medium/high).

## Scope boundaries

- SME bookkeeping / VAT / payroll → skill `fiduciaire`.
- Audit-side tax review (adversarial) → skill `controleur-afc`.
- Statutory audit → skill `reviseur-agree`.
- Notarial deeds (capital changes, holding incorporations) → skill `notaire-cantonal`.

## Worked example

> "PM avec 500 000 CHF de bénéfice, comparer ZH vs ZG."

1. **DBST**: 7.834 % × 500k = **CHF 39,170** (both, federal flat).
2. **Canton+commune**:
   - ZG (Zug city): combined ≈ **11.85 %** → ≈ **CHF 59,250** total tax.
   - ZH (Zürich city): combined ≈ **19.7 %** → ≈ **CHF 98,500** total tax.
3. **Delta**: ≈ CHF 39k/y savings ZG vs ZH (≈ 0.8 % effective rate spread).
4. **Caveat**: domicile = effective management substance (≥ 1 board member + decision-making in canton) — else AFC requalifies under inter-cantonal rules.
5. **Optimization layer**: TRAF patent box (if IP) → additional 90 % exemption on qualifying profit, capped at 70 % combined relief.
