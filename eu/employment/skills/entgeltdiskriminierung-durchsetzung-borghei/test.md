---
skill: entgelttransparenz-eu/entgeltdiskriminierung-durchsetzung
fact_pattern: |
  Eine Teamleiterin bei einem privaten Logistikunternehmen mit 400
  Beschäftigten erfährt am 12.09.2026, dass zwei männliche Teamleiter mit
  vergleichbarer Verantwortung, aber anderer Abteilungsbezeichnung
  monatlich rund 900 EUR mehr Grundgehalt und einen höheren Bonus
  erhalten. Ihr Auskunftsverlangen vom Juli 2026 hat der Arbeitgeber nie
  beantwortet; einen Entgeltbericht gibt es nicht, eine
  Entgeltbewertung wurde nie durchgeführt. Nach dem Verlangen wurde ihr
  die Teilnahme an einem Förderprogramm gestrichen. Der Arbeitsvertrag
  verweist auf einen Tarifvertrag mit dreimonatiger Ausschlussfrist. Sie
  will Nachzahlung für die letzten drei Jahre und Entschädigung.

must_cite:
  - "Art. 4"
  - "Art. 16"
  - "Art. 18"
  - "Art. 20"
  - "Art. 21"
  - "Art. 25"
  - "Art. 157 AEUV"
  - "§ 7 EntgTranspG"
  - "§ 15 AGG"
  - "§ 22 AGG"
  - "§ 612a BGB"

must_appear:
  - "Beweislast"
  - "Transparenzpflichten"
  - "geringfügig"
  - "Nachzahlung"
  - "Boni"
  - "Ausschlussfrist"
  - "drei Jahre"
  - "gleichwertig"
  - "Viktimisierung"
  - "legal_calc"

must_flag:
  - "Beweislastumkehr des Art. 18 Abs. 2 gegen einen privaten Arbeitgeber"
  - "Transparenzpflichtverletzung nicht ausgewertet"
  - "Ausnahme des Art. 18 Abs. 2 UAbs. 2 zu weit gelesen"
  - "Ausschlussfrist des § 15 Abs. 4 AGG versäumt"
  - "Tarifliche Ausschlussfristen übersehen"
  - "Nur das Grundentgelt eingeklagt"
---

# Test — entgeltdiskriminierung-durchsetzung

Struktureller Smoke-Test. Die Ausgabe muss die Gleichwertigkeit über die vier Kriterien des Art. 4 statt über die Abteilungsbezeichnung begründen, die unbeantwortete Auskunft sowie den fehlenden Bericht und die fehlende Entgeltbewertung als Transparenzpflichtverletzungen im Sinne des Art. 18 Abs. 2 auswerten und zugleich klarstellen, dass die Vollumkehr gegenüber einem **privaten** Arbeitgeber nicht unmittelbar gilt, sondern über § 22 AGG und richtlinienkonforme Auslegung zu führen ist. Nachzahlung und Bonus sind gemeinsam nach Art. 16 zu beziffern, die Zweimonatsfrist des § 15 Abs. 4 AGG und die dreimonatige tarifliche Ausschlussfrist (Art. 21 Abs. 3 lässt sie unberührt) sind zu berechnen, und die Streichung des Förderprogramms ist als Viktimisierung nach Art. 25 iVm § 612a BGB und § 16 AGG zu behandeln.

Run: `python ../../../scripts/eval.py --skill entgelttransparenz-eu/skills/entgeltdiskriminierung-durchsetzung`
