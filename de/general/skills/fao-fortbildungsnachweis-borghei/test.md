---
skill: berufsrecht-anwaltschaft/fao-fortbildungsnachweis
fact_pattern: |
  Mandant ist Fachanwalt für Arbeitsrecht und für Steuerrecht. Für
  das Berichtsjahr 2024 hat er im Arbeitsrecht 12 Stunden Präsenz-
  Lehrgang plus 8 Stunden interaktive Online-Veranstaltung plus zwei
  Aufsätze in einer Fachzeitschrift absolviert; im Steuerrecht nur
  9 Stunden Präsenz-Lehrgang. Die RAK fordert nach § 15 FAO Nachweis
  ein und droht Widerruf der Fachanwaltsbezeichnung Steuerrecht nach
  § 25 FAO an. Bitte vollständige Stunden-Prüfung, Stellungnahme an
  die RAK und ggf. Klagestrategie zum AGH.

must_cite:
  - "§ 15 FAO"
  - "§ 15 Abs. 1 FAO"
  - "§ 25 FAO"
  - "§ 43c BRAO"
  - "§ 112c BRAO"
  - "§ 74 VwGO"

must_appear:
  - "Fortbildungspflicht"
  - "15 Zeitstunden"
  - "Fachgebiet"
  - "kumulativ"
  - "Selbststudium"
  - "Widerruf"
  - "Verhältnismäßigkeit"
  - "Anwaltsgerichtshof"
  - "Nachholung"

must_flag:
  - "kumulative Pflicht"
  - "Selbststudium-Grenze"
  - "Klagefrist 1 Monat"
---

# Test — fao-fortbildungsnachweis

Struktureller Smoke-Test. Stundenrechnung muss pro Fachgebiet getrennt erfolgen, kumulative Pflicht bei Mehrfach-Fachanwaltschaft muss ausdrücklich genannt werden, Selbststudium-Halbierungs-Grenze § 15 Abs. 4 FAO muss benannt sein. Anfechtungsfrist § 74 VwGO iVm § 112c BRAO muss in der Output-Übersicht erscheinen.

Run: `python ../../../scripts/eval.py --skill berufsrecht-anwaltschaft/skills/fao-fortbildungsnachweis`
