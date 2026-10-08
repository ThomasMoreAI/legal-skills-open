---
skill: energierecht/energieeffizienzpflicht
fact_pattern: |
  Mandantin (Industrieunternehmen, ca. 600 MA, ca. 9 GWh/a
  Endenergieverbrauch im 3-Jahres-Mittel, keine verbundenen
  Großunternehmen) prüft Pflichten nach EnEfG / EDL-G. Frage:
  EnMS- oder UMS-Pflicht nach § 8 EnEfG? Energieaudit-Pflicht nach
  § 8 EDL-G? Schnittstelle zur CSRD-Berichtspflicht E1.
  Bitte Übersicht plus Nachweisführung gegenüber BAFA.
  Zusatzfrage: In einem Werk steht der Austausch der Gasheizung an —
  gilt dafür noch die 65-%-Vorgabe des § 71 GEG?

must_cite:
  - "§ 8 EnEfG"
  - "§ 9 EnEfG"
  - "§ 8 EDL-G"
  - "Empfehlung 2003/361/EG"

must_appear:
  - "KMU"
  - "Energiemanagementsystem"
  - "ISO 50001"
  - "EMAS"
  - "BAFA"
  - "7,5 GWh"
  - "Nicht-KMU"
  - "CSRD"
  - "GModG"
  - "Wärmeplan"
  - "WPG"

must_flag:
  - "verbundene Unternehmen"
  - "Übergangsfristen"
  - "Sanktion"
  - "gestrichen"
  - "30.06.2026"
  - "[unverifiziert - prüfen]"
---

# Test — energieeffizienzpflicht

Struktureller Smoke-Test. Die KMU-Einstufung (Empfehlung 2003/361/EG) muss als Vorfrage geprüft werden; die EnEfG-Schwelle (7,5 GWh/a) muss klar von der EDL-G-Audit-Pflicht (Nicht-KMU) getrennt werden; ISO 50001 / EMAS müssen als Befreiungstatbestand vom Audit nach § 8 Abs. 3 EDL-G erkannt werden; CSRD/ESRS-E1-Schnittstelle muss erwähnt werden.

**Aktualitäts-Assertion (Stand 2026-07):** Die Antwort auf die Heizungsfrage muss lauten, dass die 65-%-Vorgabe **nicht mehr gilt** — §§ 71, 71b–71p und § 72 GEG sind durch das **GModG** (Bundestag 10.07.2026, 323 : 271) gestrichen. Maßgeblich ist stattdessen der **kommunale Wärmeplan nach dem WPG** (Frist 30.06.2026 für Kommunen > 100.000 Einwohner, sonst 30.06.2028). Das Inkrafttreten des GModG ist als `[unverifiziert - prüfen]` zu kennzeichnen. Ein Skill-Stand, der noch die 65-%-Regel lehrt, ist ein Fehlschlag.

Run: `python ../../../scripts/eval.py --skill energierecht/skills/energieeffizienzpflicht`
