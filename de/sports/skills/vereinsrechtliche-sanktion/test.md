---
skill: sportrecht/vereinsrechtliche-sanktion
fact_pattern: |
  Mitglied (seit 15 Jahren) eines Schützenvereins (e.V.) ist vom Vorstand
  per Brief vom 03.05. ausgeschlossen worden wegen "vereinsschädigenden
  Verhaltens" auf Facebook (kritische Posts zur Vorstandsführung).
  Anhörung des Mitglieds fand nicht statt. Satzung sieht ein zwei-
  stufiges Verfahren (Vorstand → Ehrenrat) vor; der Ehrenrat wurde nicht
  eingeschaltet. Mandant möchte gegen den Ausschluss vorgehen und seine
  Mitgliedschaft sichern. Zustellung 06.05., heute 22.05.

must_cite:
  - "§ 25 BGB"
  - "§ 32 BGB"
  - "§ 39 BGB"
  - "§ 246 AktG"
  - "Art. 9"
  - "Art. 5"

must_appear:
  - "Anhörung"
  - "Inhaltskontrolle"
  - "Verhältnismäßigkeit"
  - "Bestimmtheit"
  - "1 Monat"
  - "Anfechtungsklage"
  - "Satzung"

must_flag:
  - "Anhörung übergangen"
  - "1-Monats-Frist"
  - "Satzungsgrundlage"
---

# Test — vereinsrechtliche-sanktion

Struktureller Smoke-Test. Anhörungsmangel muss als 🔴 BLOCKER erkannt werden; Anfechtungsfrist (1 Monat analog § 246 AktG) muss im Fristkalender stehen; Inhaltskontrolle der Satzungsnorm "vereinsschädigendes Verhalten" auf Bestimmtheit und Art. 5 GG-konforme Auslegung ist zu prüfen.

Run: `python ../../../scripts/eval.py --skill sportrecht/skills/vereinsrechtliche-sanktion`
