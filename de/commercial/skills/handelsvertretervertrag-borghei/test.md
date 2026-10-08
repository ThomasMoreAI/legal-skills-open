---
skill: handelsrecht/handelsvertretervertrag
fact_pattern: |
  Mandant (Hersteller von Industriearmaturen, GmbH) will mit einem
  selbständigen Handelsvertreter einen Vertrag für die Vermittlung
  in DE und AT abschließen. Provision 5 % auf Bestands- und Neukunden,
  Bezirksvertretung. Vertragsdauer unbestimmt. Mandant fragt zugleich,
  wie ein etwaiger späterer Ausgleichsanspruch nach § 89b HGB
  ausfallen würde (Annahme: Vertrag läuft 7 Jahre, Provisionsumsatz
  im letzten Jahr 120.000 EUR aus Neukunden, davon 80 % auf eigene
  Tätigkeit zurückgehend, Branchenabwanderung 20 %).

must_cite:
  - "§ 84 HGB"
  - "§ 86 HGB"
  - "§ 86a HGB"
  - "§ 87 HGB"
  - "§ 89 HGB"
  - "§ 89b HGB"
  - "§ 90a HGB"
  - "RL 86/653/EWG"

must_appear:
  - "Provisionsverluste"
  - "Unternehmervorteile"
  - "Billigkeit"
  - "Höchstgrenze"
  - "Jahresprovision"
  - "Ausschlussfrist"
  - "Karenzentschädigung"
  - "Unabdingbarkeit"
  - "Ingmar"

must_flag:
  - "Ausschlussfrist § 89b Abs. 4"
  - "im Voraus ausschließen"
  - "Sogwirkung"
---

# Test — handelsvertretervertrag

Struktureller Smoke-Test. Die fünf Berechnungsstufen § 89b HGB (Provisionsverluste / Unternehmervorteile / Billigkeit / Höchstgrenze / Ausschluss) müssen alle auftauchen; die 1-Jahres-Ausschlussfrist § 89b Abs. 4 S. 2 HGB ist als Wiedervorlage zu kennzeichnen; § 90a HGB Karenzentschädigung als Voraussetzung des Wettbewerbsverbots zu nennen.

Run: `python ../../../scripts/eval.py --skill handelsrecht/skills/handelsvertretervertrag`
