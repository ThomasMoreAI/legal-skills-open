---
skill: arbeitsrecht/agg-entschaedigung
fact_pattern: |
  Mandantin (54 Jahre, Bilanzbuchhalterin) bewirbt sich auf eine Stelle, die
  mit "Wir suchen einen jungen, dynamischen Kollegen für unser Team" beworben
  wurde. Die Ausschreibung enthält keinen Zusatz "(m/w/d)". Im Vorstellungs-
  gespräch am 05.02.2026 fragt der Geschäftsführer nach der familiären
  Situation und bemerkt, man wolle "eine langfristige Perspektive aufbauen".
  Die Absage geht am 12.02.2026 zu. Das Einstiegsgehalt war mit 5.000 EUR
  brutto ausgeschrieben. Der Arbeitgeber wendet ein, die Mandantin habe sich
  binnen eines Jahres auf 40 vergleichbare Stellen beworben.
must_cite:
  - "§ 15 AGG"
  - "§ 15 Abs. 4 AGG"
  - "§ 15 Abs. 2 S. 2 AGG"
  - "§ 15 Abs. 6 AGG"
  - "§ 22 AGG"
  - "§ 1 AGG"
  - "§ 3 AGG"
  - "§ 61b Abs. 1 ArbGG"
  - "§ 242 BGB"
must_appear:
  - "Indizienbeweis"
  - "Beweislastumkehr"
  - "Geltendmachungsschreiben"
  - "AGG-Hopping"
  - "Deckelung"
  - "Deterministische Berechnung"
  - "Bezifferung"
must_flag:
  - "2-Monats-Frist des § 15 Abs. 4 AGG versäumt"
  - "Klagefrist § 61b ArbGG ab dem Absagedatum gerechnet"
  - "Einstellungsanspruch geltend gemacht"
  - "Indizien nur behauptet, nicht bewiesen"
  - "Ausschreibung nicht merkmalsneutral"
---

# Test — agg-entschaedigung

Prüft das zweistufige Fristenregime, den Indizienkatalog des § 22 AGG und die
Behandlung des Rechtsmissbrauchseinwands.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/agg-entschaedigung`
