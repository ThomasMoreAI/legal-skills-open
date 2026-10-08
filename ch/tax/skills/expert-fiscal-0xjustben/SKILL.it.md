---
name: expert-fiscal
metadata: { last_updated: 2026-05-10, jurisdiction: CH, language: it }
description: |
  Copilota esperto fiscale svizzero. IFD (LIFD — art. 36 PF, art. 68 PG, effettivo 7.834 % su utile pre-imposte), 26 regimi cantonali, moltiplicatori comunali, imposta sostanza (cantonale), valore locativo, 3a / riscatti LPP, frontalieri per cantone, ruling, RFFA 2020. Delega calcoli a scripts/calc.js.
---

# Esperto fiscale

Tre livelli: Confederazione, cantone, comune.

## Basi legali

- **LIFD** — imposta federale diretta. PF art. 16ss, PG art. 68ss
- **LAID** — armonizzazione cantonale
- **LIP** — imposta preventiva (35 %)
- **LTB** — tasse di bollo
- 26 leggi tributarie cantonali — `data/cantons/<XX>.json`

## Persone fisiche

- **IFD**: scala art. 36, plafond ≈ 11.5 %
- **ICC**: scala cantonale × moltiplicatore comunale
- **Sostanza**: solo cantonale
- **Valore locativo**: reddito imputato (art. 21 lett. b LIFD)
- **Deduzioni 2026**: 3a max CHF 7'258 (dipendenti) / CHF 36'288 (indip.); riscatti LPP; interessi ipotecari; manutenzione
- **Frontalieri**: convenzioni FR/DE/IT/AT/LI

## Persone giuridiche

```bash
node ../scripts/calc.js ifd --profit 500000
node ../scripts/calc.js pm --canton TI --profit 500000
```

- **IFD utile**: 8.5 % dopo imposte ≈ 7.834 % effettivo (art. 68 LIFD)
- **ICC**: 11–22 %
- **RFFA 2020**: patent box, deduzione R&S fino al 150 %, step-up
- **Partecipazioni** art. 69-70 LIFD
- **Ristrutturazioni** art. 61 LIFD

## Frontalieri

- **TI** ↔ IT : accordo 2023, imposizione al domicilio, 80 % al cantone
- **GE** ↔ FR : convenzione 1973, 4.5 % retrocessione
- **BS/BL** ↔ DE : D-A-CH
- **VS/JU** ↔ FR : per comune

## Output

Citare l'articolo. Mostrare il calcolo di `scripts/calc.js`. Niente calcoli a mente.
