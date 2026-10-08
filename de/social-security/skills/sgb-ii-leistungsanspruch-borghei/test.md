---
skill: sozialrecht/sgb-ii-leistungsanspruch
fact_pattern: |
  Antragstellerin A. (38, deutsch, erwerbsfähig) lebt mit Partner B.
  (45, 1.450 EUR netto aus Vollzeitbeschäftigung) und zwei gemeinsamen
  Kindern (10 und 14 J.) in 90-m²-Mietwohnung. Bruttokaltmiete 900 EUR,
  Heizung 110 EUR. Tagesgeld 6.800 EUR, Familien-Pkw Zeitwert 4.500 EUR.
  Erstantrag Bürgergeld, kein laufender Bewilligungsabschnitt. Bitte
  Vollprüfung des Anspruchs.

must_cite:
  - "§ 7 SGB II"
  - "§ 8 SGB II"
  - "§ 9 SGB II"
  - "§ 11 SGB II"
  - "§ 12 SGB II"
  - "§ 19 SGB II"
  - "§ 20 SGB II"
  - "§ 22 SGB II"
  - "§ 60 SGB I"

must_appear:
  - "Bedarfsgemeinschaft"
  - "Erwerbsfähigkeit"
  - "Hilfebedürftigkeit"
  - "Regelbedarf"
  - "Kosten der Unterkunft"
  - "Karenzzeit"
  - "Vermögen"
  - "Erwerbstätigenfreibetrag"
  - "Mitwirkung"

must_flag:
  - "Karenzzeit"
  - "vorrangige Leistungen"
  - "schlüssiges Konzept"
  - "Mitwirkungspflicht"
---

# Test — sgb-ii-leistungsanspruch

Struktureller Smoke-Test. Erwartete Anspruchsprüfungsschritte (persönliche Voraussetzungen → BG → Bedarf → Einkommen → Vermögen → Rechtsfolge) müssen alle im Output erscheinen. Karenzzeiten § 12 Abs. 3 und § 22 Abs. 1 S. 2 SGB II müssen ausdrücklich addressiert werden.

Run: `python ../../../scripts/eval.py --skill sozialrecht/skills/sgb-ii-leistungsanspruch`
