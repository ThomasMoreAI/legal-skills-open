---
skill: verbandsklage-vdug/anmeldung-umsetzungsverfahren
fact_pattern: |
  Unsere Mandantin ist Verbraucherin und von einer Abhilfeklage gegen einen
  Stromversorger betroffen. Die mündliche Verhandlung wurde am 14.03.2026
  geschlossen; das Fristende fällt nach unserer Berechnung auf einen
  Samstag. Sie hat bereits im Januar 2026 - vor der Bekanntgabe der
  Verbandsklage im Register - selbst Klage beim Amtsgericht erhoben. Sie
  betreibt nebenbei einen Friseursalon mit drei Angestellten und fragt, ob
  sie deshalb überhaupt anmelden darf. Später teilt der Sachwalter mit
  Schreiben vom 06.07.2026 mit, ihr Anspruch sei nur zur Hälfte berechtigt,
  weil ein Berechtigungsnachweis fehle.

must_cite:
  - "§ 11 VDuG"
  - "§ 16 VDuG"
  - "§ 24 VDuG"
  - "§ 25 VDuG"
  - "§ 28 VDuG"
  - "§ 46 VDuG"
  - "§ 193 BGB"
  - "§ 1 VDuG"

must_appear:
  - "drei Wochen"
  - "vier Wochen"
  - "zwei Wochen"
  - "Versicherung der Richtigkeit"
  - "kleines Unternehmen"
  - "Aussetzung"
  - "Sachwalter"
  - "Umsetzungsfonds"
  - "ohne inhaltliche Prüfung"
  - "legal_calc"

must_flag:
  - "§ 193 BGB angewandt"
  - "Frist ab Registerbekanntgabe"
  - "Versicherung der Richtigkeit vergessen"
  - "Eintragung für eine Anspruchsprüfung gehalten"
  - "Widerspruch ohne Begründung eingelegt"
---

# Test — anmeldung-umsetzungsverfahren

Struktureller Smoke-Test. Die Ausgabe muss die Dreiwochenfrist ab dem 14.03.2026 rechnen und ausdrücklich klarstellen, dass § 193 BGB nach § 46 Abs. 1 S. 2 VDuG **nicht** gilt, das Fristende also auch auf einem Samstag bleibt. Der Friseursalon ist über § 1 Abs. 2 VDuG einzuordnen und die Angabe nach § 46 Abs. 2 Nr. 2 VDuG zu machen. Die im Januar 2026 vor Registerbekanntgabe erhobene Individualklage ist § 11 Abs. 1 VDuG zuzuordnen (Aussetzung bei Anmeldung). Die Sachwaltermitteilung vom 06.07.2026 löst die Vierwochenfrist des § 28 Abs. 2 VDuG aus, die Widerspruchsentscheidung sodann die Zweiwochenfrist des § 28 Abs. 4 VDuG; der Widerspruch ist zu begründen.

Run: `python ../../../scripts/eval.py --skill verbandsklage-vdug/skills/anmeldung-umsetzungsverfahren`
