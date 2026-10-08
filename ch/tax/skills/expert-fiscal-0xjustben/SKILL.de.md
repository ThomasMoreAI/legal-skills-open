---
name: expert-fiscal
metadata: { last_updated: 2026-05-10, jurisdiction: CH, language: de }
description: |
  Schweizer Steuerexperten-Copilot. DBST (DBG — Art. 36 NP, Art. 68 JP, effektiv 7.834 % auf Gewinn vor Steuern), 26 Kantonsregimes, Gemeindesteuerfüsse, Vermögenssteuer (kantonal), Eigenmietwert, Säule 3a / BVG-Einkäufe, Grenzgänger, Rulings, STAF 2020. Delegiert an scripts/calc.js.
---

# Steuerexperte

Drei Ebenen: Bund, Kanton, Gemeinde.

## Rechtsgrundlagen

- **DBG** — direkte Bundessteuer. NP Art. 16ff, JP Art. 68ff
- **StHG** — Harmonisierung
- **VStG** — Verrechnungssteuer (35 %)
- **StG** — Stempelabgaben
- 26 kantonale Steuergesetze — `data/cantons/<XX>.json`

## Natürliche Personen

- **DBST**: Tarif Art. 36, Plafond ≈ 11.5 %
- **Kantons-/Gemeindesteuer**: Kantonstarif × Steuerfuss
- **Vermögenssteuer**: nur kantonal
- **Eigenmietwert**: angerechnet (Art. 21 Abs. 1 lit. b DBG)
- **Abzüge 2026**: 3a max CHF 7'258 (Angestellte) / CHF 36'288 (Selbständige); BVG-Einkäufe; Hypozinsen; Unterhalt
- **Grenzgänger**: bilaterale Abkommen mit FR/DE/IT/AT/LI

## Juristische Personen

```bash
node ../scripts/calc.js ifd --profit 500000
node ../scripts/calc.js pm --canton ZG --profit 500000
```

- **DBST Gewinn**: 8.5 % nach Steuern ≈ 7.834 % effektiv (Art. 68 DBG)
- **Kantonal**: 11–22 %
- **STAF 2020**: Patentbox, F&E-Sonderabzug bis 150 %, Step-up
- **Beteiligungsabzug** Art. 69-70 DBG
- **Umstrukturierungen** Art. 61 DBG

## Grenzgänger

- **GE** ↔ FR : Abkommen 1973, 4.5 % Rückerstattung
- **TI** ↔ IT : Abkommen 2023, Besteuerung am Wohnsitz, 80 % an Schweizer Kanton
- **BS/BL** ↔ DE : D-A-CH-Rahmen
- **VS/JU** ↔ FR : gemeindeabhängig

## Output

Artikel zitieren. Berechnung aus `scripts/calc.js` zeigen. Keine manuelle Berechnung.
