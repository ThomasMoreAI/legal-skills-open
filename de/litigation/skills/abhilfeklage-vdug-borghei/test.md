---
skill: verbandsklage-vdug/abhilfeklage-vdug
fact_pattern: |
  Wir vertreten eine Bank, gegen die eine Abhilfeklage auf Zahlung eines
  kollektiven Gesamtbetrags von 12 Mio. EUR wegen unwirksamer
  Zustimmungsfiktionsklauseln erhoben wurde. Betroffen sind rund 210.000
  Girokonten aus vier Vertragsgenerationen mit unterschiedlichen
  Entgeltmodellen; ein Teil der Kunden hat Entgelterhöhungen ausdrücklich
  zugestimmt, ein Teil hat widersprochen, bei einem Teil ist Verjährung
  denkbar. Die Klageschrift behauptet pauschal Gleichartigkeit und nennt
  weder Einzelbeträge noch eine Berechnungsmethode. Die mündliche
  Verhandlung wurde am 14.03.2026 geschlossen. Wir sollen die
  Individualisierungsrüge vorbereiten und für den Fall eines
  Abhilfegrundurteils die Urteilsformel mitgestalten.

must_cite:
  - "§ 14 VDuG"
  - "§ 15 VDuG"
  - "§ 16 VDuG"
  - "§ 17 VDuG"
  - "§ 18 VDuG"
  - "§ 19 VDuG"
  - "§ 21 VDuG"
  - "§ 287 ZPO"

must_appear:
  - "Gleichartigkeit"
  - "Berechnungsmethode"
  - "Berechtigungsnachweise"
  - "Abhilfegrundurteil"
  - "Abhilfeendurteil"
  - "Sachwalter"
  - "zulassungsfrei"
  - "Gruppenbildung"
  - "legal_calc"

must_flag:
  - "Gleichartigkeit behauptet statt dargelegt"
  - "Berechnungsmethode erst im Umsetzungsverfahren entwickelt"
  - "Revision für zulassungsbedürftig gehalten"
  - "Kollektiven Gesamtbetrag als Haftungsobergrenze behandelt"
  - "§ 287 ZPO übersehen"
---

# Test — abhilfeklage-vdug

Struktureller Smoke-Test. Die Ausgabe muss die pauschale Gleichartigkeitsbehauptung an § 15 Abs. 1 Nr. 1 und Nr. 2 VDuG messen, die vier Vertragsgenerationen sowie Zustimmung, Widerspruch und Verjährung als Individualisierungseinwände aufbereiten und Gruppenbildung als Gegenstrategie benennen, die fehlenden Angaben nach § 15 Abs. 2 VDuG rügen, für ein Abhilfegrundurteil praktikable Berechtigungsnachweise nach § 16 Abs. 2 Nr. 2 VDuG vorschlagen, die Schätzung nach § 19 Abs. 2 VDuG iVm § 287 ZPO adressieren, auf das Erhöhungsrisiko nach § 21 VDuG hinweisen und die zulassungsfreie Revision nach § 18 Abs. 4 VDuG mit Frist ausweisen. Die Anmeldefrist ist ab dem 14.03.2026 zu rechnen.

Run: `python ../../../scripts/eval.py --skill verbandsklage-vdug/skills/abhilfeklage-vdug`
