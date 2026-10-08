---
skill: umweltrecht/krwg-abfallrechtliche-pruefung
fact_pattern: |
  Industrieller Metallverarbeiter erhält Anordnung der unteren
  Abfallbehörde nach § 47 KrWG. Vorwurf: gewerbliche Siedlungsabfälle
  (Pappe, Folie, Restmüll, Holz) werden entgegen § 14 KrWG nicht
  getrennt gehalten. Anordnung verlangt Trennsystem binnen vier Wochen
  und ordnet sofortigen Vollzug an. Anhörung war auf zwei Werktage
  verkürzt. Bitte Rechtmäßigkeit der Anordnung prüfen und
  Verhältnismäßigkeit der Frist bewerten.

must_cite:
  - "§ 3 KrWG"
  - "§ 6 KrWG"
  - "§ 14 KrWG"
  - "§ 47 KrWG"
  - "§ 28 VwVfG"
  - "§ 80 Abs. 2 Nr. 4 VwGO"
  - "GewAbfV"

must_appear:
  - "Abfallbegriff"
  - "Abfallhierarchie"
  - "Getrennthaltung"
  - "Ermächtigungsgrundlage"
  - "Ermessen"
  - "Verhältnismäßigkeit"
  - "Anhörung"
  - "Sofortvollzug"

must_flag:
  - "Anhörung"
  - "Verhältnismäßigkeit"
  - "Widerspruchsfrist"
---

# Test — krwg-abfallrechtliche-pruefung

Struktureller Smoke-Test. Output muss Abfallbegriff vor Hierarchie vor Pflicht prüfen und bei Anordnung saubere Verwaltungsaktprüfung (Ermächtigung → Tatbestand → Ermessen → Verhältnismäßigkeit → Verfahren) durchführen.

Run: `python ../../../scripts/eval.py --skill umweltrecht/skills/krwg-abfallrechtliche-pruefung`
