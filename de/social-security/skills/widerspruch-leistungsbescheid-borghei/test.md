---
skill: sozialrecht/widerspruch-leistungsbescheid
fact_pattern: |
  Mandant erhält am 06.04.2026 Aufhebungs- und Erstattungsbescheid des
  Jobcenters Musterstadt vom 03.04.2026 über 3.840 EUR, gestützt auf
  § 48 Abs. 1 S. 2 Nr. 3 SGB X i.V.m. § 50 Abs. 1 SGB X. Behörde
  begründet mit nicht gemeldetem Einkommen aus Minijob. Mandant trägt
  vor, Lohnabrechnungen monatlich übermittelt zu haben. Keine Anhörung
  § 24 SGB X erfolgt. Rechtsbehelfsbelehrung im Bescheid korrekt.
  Bitte Widerspruchsschrift und Antrag nach § 86b SGG entwerfen.

must_cite:
  - "§ 84 SGG"
  - "§ 86a SGG"
  - "§ 86b SGG"
  - "§ 87 SGG"
  - "§ 24 SGB X"
  - "§ 35 SGB X"
  - "§ 48 SGB X"
  - "§ 50 SGB X"
  - "§ 63 Abs. 2 SGB X"

must_appear:
  - "Widerspruch"
  - "Ausgangsbehörde"
  - "Bekanntgabe"
  - "Frist"
  - "aufschiebende Wirkung"
  - "Anhörung"
  - "Begründung"
  - "Antrag"
  - "Erstattung"

must_flag:
  - "Falschadressierung"
  - "aufschiebende Wirkung"
  - "Anhörung"
  - "Klagefrist"
  - "Notwendigkeit"
---

# Test — widerspruch-leistungsbescheid

Struktureller Smoke-Test. Erwartet sind: berechnetes Fristende (konkretes Datum, nicht nur "1 Monat"), Adressierung an die Ausgangsbehörde, Antrag § 86b Abs. 1 Nr. 2 SGG, Notwendigkeitsantrag § 63 Abs. 2 SGB X, Anträge im Tenor (Aufhebung + Leistung).

Run: `python ../../../scripts/eval.py --skill sozialrecht/skills/widerspruch-leistungsbescheid`
