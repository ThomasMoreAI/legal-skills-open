---
skill: sozialrecht/sgb-vi-rentenanspruch
fact_pattern: |
  Mandant M. (52 J.) ist seit 14.08.2025 arbeitsunfähig (chronische
  Wirbelsäulenerkrankung). Reha-Maßnahme Frühjahr 2026 ohne Erfolg.
  Sozialmedizinisches Gutachten DRV v. 03.04.2026 attestiert
  Leistungsvermögen < 3 h täglich auf dem allgemeinen Arbeitsmarkt.
  Versicherungsverlauf: 12 Jahre Pflichtbeiträge, zuletzt 5 Jahre
  durchgehend. Kein Berufsschutz (geb. 1973). Bitte Prüfung Anspruch
  auf Rente wegen Erwerbsminderung.

must_cite:
  - "§ 43 SGB VI"
  - "§ 50 SGB VI"
  - "§ 51 SGB VI"
  - "§ 99 SGB VI"
  - "§ 9 SGB VI"
  - "§ 60 SGB I"

must_appear:
  - "Wartezeit"
  - "besondere versicherungsrechtliche Voraussetzungen"
  - "volle Erwerbsminderung"
  - "Leistungsfall"
  - "Reha vor Rente"
  - "Antrag"
  - "Hinzuverdienst"

must_flag:
  - "Streckungstatbestände"
  - "Reha"
  - "sozialmedizinisches Gutachten"
  - "Antragsfrist"
---

# Test — sgb-vi-rentenanspruch

Struktureller Smoke-Test. Erwartete Prüfungsachsen (versicherungsrechtliche Voraussetzungen → persönliche Voraussetzungen → Antragsmodalitäten) müssen alle im Output erscheinen. Bei Erwerbsminderung muss die Differenzierung volle / teilweise EM angesprochen werden.

Run: `python ../../../scripts/eval.py --skill sozialrecht/skills/sgb-vi-rentenanspruch`
