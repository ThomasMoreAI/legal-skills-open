# Diwana / Tunisian Customs — tech equipment imports for freelancers

## General framework

Every import into Tunisia is subject to:
1. **Customs duty** (based on the HS code of the goods)
2. **Import VAT**: 19% on (CIF + customs duty)
3. **Customs service fee (RPD)**: about 3% on the customs duty
4. **BCT restrictions** (Circular 2026-04 — see `bct-circulaires.md`)

⚠️ **Myth to bust:** there is **no de minimis threshold** at 1 000 TND or any other amount. Every import, even a symbolic one, goes through a customs declaration. [src: `data/diwana_tariffs.json` → `myths_debunked`]

## Calculation method — CIF

```
CIF = goods cost + insurance + freight
Total payable = CIF + (CIF × duty_%) + (CIF × VAT 19%)
              + (CIF × duty_% × RPD%)
```

### Example — Laptop imported from Amazon US — CIF 2 000 USD ≈ 6 200 TND

```
Customs duty (HS 8471.30) : 0%  →     0 TND
VAT 19% on CIF             : 19% → 1 178 TND
RPD ~3% on duty            : 0   →     0 TND (duty = 0)
                            Customs taxes total ≈ 1 178 TND
Final cost ≈ 6 200 + 1 178 = 7 378 TND
```

### Example — Smartphone imported — CIF 800 USD ≈ 2 480 TND

```
Customs duty (HS 8517.13) : 20% →   496 TND
VAT base                   : 2 480 + 496 = 2 976 TND
VAT 19%                    : 565 TND
RPD ~3% on duty            : 15 TND
                            Total taxes ≈ 1 076 TND
Final cost ≈ 2 480 + 1 076 = 3 556 TND  (+43.4% vs CIF)
```

## Tariffs — common freelancer / dev items

| Item | HS code (indicative) | Duty | VAT | Approx. total load |
|---|---|---|---|---|
| Laptop / portable computer | 8471.30 | **0 %** | 19 % | **19 %** |
| Smartphone | 8517.13 | **20 %** | 19 % | **~42.8 %** |
| Desktop computer | 8471.41/49 | ~10 % | 19 % | ~30.9 % |
| Screen / monitor | 8528.52 | [REQUIRES VERIFICATION] | 19 % | — |
| Keyboard / mouse | 8471.60 | [REQUIRES VERIFICATION] | 19 % | — |
| GPU / graphics card (spare part) | 8473.30 | [REQUIRES VERIFICATION] | 19 % | — |
| Tablet / iPad | 8471.30 | [REQUIRES VERIFICATION — sometimes treated like a smartphone depending on use] | 19 % | — |

[src: `data/diwana_tariffs.json` + trade.gov + agenceecofin.com (decree of 2017, effective 1 January 2018)]

> These tariffs are indicative. The up-to-date official tariff is at **douane.gov.tn/tarif-douanier/** — always check before placing a high-stakes order.

## Import procedure

### Mode 1 — Postal / express parcel (DHL, FedEx, La Poste)

- The carrier files the **customs declaration** for you (typical handling fee 30–80 TND).
- You pay duty + VAT + carrier fees at delivery.
- **Clearance time:** 2–15 days depending on carrier and complexity.

### Mode 2 — Direct import (you order from abroad yourself)

- Hire a licensed **customs broker** (*transitaire*).
- Declaration in SINDA (the customs information system).
- Broker fee: 100–300 TND per file.
- Best fit for expensive professional gear.

### Mode 3 — Bringing it back from a trip

- **Personal-use tolerances** exist but are limited.
- Used personal effects: wide tolerance.
- New equipment: tolerance around 200–300 EUR equivalent.
- Beyond that: declaration and duties apply.

[REQUIRES MANUAL LEGAL VERIFICATION: exact 2026 personal-effects thresholds — they vary with transport mode and time spent abroad]

## Possible exemptions

### Fully exporting company (Investment Code 2016-71)

- Customs duty exemption + VAT suspension on professional equipment.
- Conditions: official "fully exporting" status (more than X% of revenue from export — [REQUIRES VERIFICATION: exact 2026 threshold]).
- Procedure: API (*Agence de Promotion de l'Industrie*) approval.
- For SUARL / SARL only — a patente is not eligible.

### Economic customs regimes (RDE)

- **Temporary admission (AT):** import without duty if re-exported within 6–24 months.
- **Inward processing:** import raw materials, transform, re-export.
- Useful for specific cases (e.g. work with equipment supplied by the client).

## BCT 2026-04 restrictions — critical overlap ⚠️

[src: `bct_circulars.json` + `bct-circulaires.md`]

**BCT Circular 2026-04** restricts access to foreign currency for imports of "non-priority" products. In concrete terms:

- Customs may allow the import → BUT the bank may refuse the international transfer.
- Consequence: you cannot pay the foreign supplier through the official banking channel.
- Legal workarounds: pay with the technological card (within its annual cap), pay from an already-funded PPR Devises account, or wait for a foreign-currency allocation.

**Before any tech-equipment import above 500 EUR**, check:
1. The HS code of the item.
2. The annex of Circular 2026-04.
3. Your technological-card balance (annual cap).
4. Your PPR Devises balance.

> Note: the December 2025 forex announcement does NOT change this for imports. Until the application decrees are gazetted, Circular 2026-04 still gates your access to foreign currency for "non-priority" imports.

## Sources

- `data/sources.json` → `douane-tarif`, `ict-duty-20pct-2018`, `trade-gov-tunisia-tariffs`, `thd-dedouanement-tic`, `ngp-douane-tunisie`, `bct-cir-2026-04`
- `data/diwana_tariffs.json` → full structured schema
- `bct-shield/references/bct-circulaires.md` (BCT interaction)
