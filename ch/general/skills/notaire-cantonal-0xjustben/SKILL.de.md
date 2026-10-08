---
name: notaire-cantonal
metadata: { last_updated: 2026-05-10, jurisdiction: CH, language: de }
description: |
  Copilot kantonales Notariat Schweiz. NICHT vereinheitlicht — drei Systeme: lateinisch (GE, VD, VS, FR, NE, JU, TI), frei (ZH, SH, AR), gemischt (übrige). Öffentliche Urkunden (ZGB 657 Immobilien, ZGB 712d Stockwerkeigentum, OR 620ff AG / 772ff GmbH), Erbrecht (ZGB 457-640, Revision 2023 Pflichtteil Nachkommen 1/2), Güterstände (ZGB 181-251), Erbschaftssteuer (kantonal). **Kanton zuerst identifizieren.**
---

# Kantonaler Notar

Schweizer Notariat **nicht vereinheitlicht**. **Kanton zuerst.**

## Drei Systeme

| System | Kantone | Charakter |
|--------|---------|-----------|
| **Lateinisch** | GE, VD, VS, FR, NE, JU, TI | Urkundsperson, Tarif |
| **Frei** | ZH, SH, AR | Private Notare im Wettbewerb |
| **Gemischt / Amtsnotariat** | BE, SO, LU, ZG, BS, BL, AG, … | Beamte oder halbstaatlich |

→ `data/cantons/<XX>.json` Feld `notariat`.

## Bereiche

### Immobilien
- **Kaufvertrag**: öffentliche Beurkundung (ZGB 657)
- **Schuldbriefe** (ZGB 842ff)
- **Dienstbarkeiten** (ZGB 730ff)
- **Stockwerkeigentum** (ZGB 712d)
- **Handänderungssteuer**: 0 % (ZH, ZG) bis 3.3 % (VD)

```bash
node ../scripts/calc.js mutation --canton GE --price 1200000
```

### Erbrecht (ZGB 457-640)
- **Revision 2023**: Pflichtteil Nachkommen 1/2 (vorher 3/4)
- **Ehegatte**: 1/2 Erbschaft, davon 1/4 pflichtteilgeschützt
- **Erbvertrag** vs eigenhändiges vs öffentliches Testament
- **Willensvollstreckung**
- **Erbschaftssteuer**: kantonal, meist Befreiung für Ehegatte/Nachkommen

### Güterstände (ZGB 181-251)
Errungenschaftsbeteiligung (Standard) / Gütertrennung / Gütergemeinschaft.

### Gesellschaftsrecht
- **AG** (OR 620ff): Min. 100'000, Liberierung 20 % min 50'000
- **GmbH** (OR 772ff): Min. 20'000, voll liberiert
- **Kapitalerhöhung/-herabsetzung**
- **Fusion/Spaltung/Umwandlung** (FusG)

## Output

Kanton + System / Rechtsgrundlage / geschätzte Honorare / erforderliche Unterlagen.
