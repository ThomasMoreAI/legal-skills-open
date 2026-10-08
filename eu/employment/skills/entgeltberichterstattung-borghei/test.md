---
skill: entgelttransparenz-eu/entgeltberichterstattung
fact_pattern: |
  Ein Maschinenbauunternehmen mit 310 Beschäftigten in Deutschland bereitet
  die Entgeltberichterstattung vor. Die HR-Systeme werten bisher nur das
  Grundentgelt aus; Boni, Schichtzulagen und Firmenwagen sind nicht
  strukturiert erfasst. Eine Gruppenbildung existiert nur nach
  Stellenbezeichnung. Eine erste Auswertung zeigt in der Gruppe
  "Vertriebsinnendienst" ein durchschnittliches Entgeltgefälle von 7,4
  Prozent zulasten der Frauen; die Geschäftsführung hält das für durch
  Betriebszugehörigkeit erklärbar, hat das aber nicht dokumentiert. Ein
  Betriebsrat besteht; die Einführung eines neuen Auswertungstools ist
  geplant. Die Geschäftsführung will erst 2027 mit der Datenarbeit
  beginnen.

must_cite:
  - "Art. 4"
  - "Art. 9"
  - "Art. 10"
  - "Art. 12"
  - "§ 17 EntgTranspG"
  - "§ 21 EntgTranspG"
  - "§ 80 BetrVG"
  - "§ 87 BetrVG"

must_appear:
  - "7. Juni 2027"
  - "vorangehende Kalenderjahr"
  - "Quartil"
  - "Median"
  - "variablen"
  - "5 Prozent"
  - "sechs Monaten"
  - "gleichwertig"
  - "legal_calc"

must_flag:
  - "Erst 2027 mit der Datenaufbereitung begonnen"
  - "Nur das Grundentgelt ausgewertet"
  - "Gruppenbildung nach Stellenbezeichnung"
  - "5-Prozent-Schwelle auf den Gesamtbetrieb bezogen"
  - "Rechtfertigung nicht dokumentiert"
  - "Mitbestimmung erst nach dem Systemaufbau geprüft"
---

# Test — entgeltberichterstattung

Struktureller Smoke-Test. Die Ausgabe muss das Unternehmen mit 310 Beschäftigten der jährlichen Berichtspflicht ab dem 07.06.2027 zuordnen und klarstellen, dass über das vorangehende Kalenderjahr berichtet wird, weshalb die Datenarbeit nicht auf 2027 verschoben werden kann. Alle sieben Kennzahlen des Art. 9 Abs. 1 sind zu benennen, insbesondere die variablen und ergänzenden Bestandteile, Median und Durchschnitt nebeneinander sowie die Quartilsverteilung. Die Gruppenbildung ist auf Art. 4 umzustellen. Das Gefälle von 7,4 Prozent im Vertriebsinnendienst ist an Art. 10 Abs. 1 lit. a zu messen, die Betriebszugehörigkeits-Rechtfertigung als dokumentationsbedürftig zu behandeln und die Sechsmonatsfrist des lit. c zu berechnen. Die Mitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG ist vor der Toolauswahl zu klären.

Run: `python ../../../scripts/eval.py --skill entgelttransparenz-eu/skills/entgeltberichterstattung`
