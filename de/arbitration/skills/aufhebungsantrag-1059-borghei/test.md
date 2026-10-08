---
skill: schiedsverfahren-adr/aufhebungsantrag-1059
fact_pattern: |
  Unsere Mandantin hat einen DIS-Schiedsspruch mit Schiedsort Hamburg am
  20.11.2026 per Boten erhalten; erlassen wurde er ausweislich des
  Rubrums am 12.11.2026. Sie beanstandet, das Schiedsgericht habe ihren
  zentralen Zeugen nicht vernommen (im Verfahren protokolliert gerügt),
  über einen im Schiedsvertrag nicht erfassten Gegenanspruch aus einem
  anderen Vertrag mitentschieden und die Beweislast falsch verteilt.
  Zusätzlich hält sie die Zinsberechnung für rechnerisch falsch. Die
  Gegenseite hat am 05.01.2027 beim OLG die Vollstreckbarerklärung
  beantragt. Die Mandantin fragt, ob sie sich auf die Verteidigung im
  Vollstreckbarerklärungsverfahren beschränken kann.

must_cite:
  - "§ 1054 ZPO"
  - "§ 1058 ZPO"
  - "§ 1059 ZPO"
  - "§ 1060 ZPO"
  - "§ 1062 ZPO"
  - "§ 1063 ZPO"
  - "§ 1065 ZPO"

must_appear:
  - "drei Monate"
  - "Empfang"
  - "ordre public"
  - "Teilaufhebung"
  - "Kausalität"
  - "Präklusion"
  - "Zurückverweisung"
  - "Rechtsbeschwerde"
  - "Oberlandesgericht"
  - "legal_calc"

must_flag:
  - "Dreimonatsfrist ab Erlass statt ab Empfang gerechnet"
  - "Frist verstreichen lassen"
  - "Révision au fond betrieben"
  - "Ordre public als Auffangargument"
  - "Kausalität bei Nr. 1 lit. d nicht dargelegt"
  - "Teilaufhebung nicht beantragt"
---

# Test — aufhebungsantrag-1059

Struktureller Smoke-Test. Die Ausgabe muss die Dreimonatsfrist ab dem 20.11.2026 (Empfang), nicht ab dem 12.11.2026 (Erlass) berechnen, die falsche Beweislastverteilung und die Zinsberechnung als nicht aufhebungsfähige révision au fond einordnen (Zinsen ggf. über § 1058 ZPO), die Mitentscheidung über den nicht erfassten Gegenanspruch § 1059 Abs. 2 Nr. 1 lit. c mit Teilaufhebung zuordnen, die unterbliebene Zeugenvernehmung unter lit. b und lit. d mit Kausalitätsdarlegung prüfen und ausdrücklich davor warnen, sich allein auf die Verteidigung im Vollstreckbarerklärungsverfahren zu verlassen (§ 1060 Abs. 2 S. 3 ZPO). Zuständiges OLG und Rechtsbeschwerde sind zu benennen.

Run: `python ../../../scripts/eval.py --skill schiedsverfahren-adr/skills/aufhebungsantrag-1059`
