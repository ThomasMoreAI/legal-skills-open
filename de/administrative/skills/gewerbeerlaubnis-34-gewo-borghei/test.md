---
skill: gewerberecht/gewerbeerlaubnis-34-gewo
fact_pattern: |
  Mandantin ist eine GmbH, die WEG-Verwaltung und Mietverwaltung für
  private Eigentümer betreibt und daneben Immobilien vermittelt. Sie hält
  seit 2019 eine Erlaubnis nach § 34c GewO. Ihr Geschäftsführer wurde im
  Juni 2023 wegen Untreue zu einer Geldstrafe verurteilt; die Behörde hat
  hiervon am 15.09.2025 vollständige Kenntnis erlangt und am 20.05.2026
  den Widerruf der Erlaubnis verfügt sowie die sofortige Vollziehung
  angeordnet. Eine Berufshaftpflichtversicherung für die Verwaltung
  besteht seit 2024 nicht mehr; Weiterbildungsnachweise liegen für keinen
  Mitarbeiter vor. Zusätzlich möchte die Mandantin künftig geschlossene
  Investmentvermögen vermitteln und fragt, welche Erlaubnis sie dafür
  benötigt.

must_cite:
  - "§ 34c GewO"
  - "§ 34f GewO"
  - "§ 35 GewO"
  - "§ 144 GewO"
  - "§ 48 VwVfG"
  - "§ 49 VwVfG"
  - "§ 28 VwVfG"
  - "§ 70 VwGO"
  - "§ 80 VwGO"
  - "§ 882b ZPO"

must_appear:
  - "Regelvermutung"
  - "fünf Jahren"
  - "Berufshaftpflichtversicherung"
  - "20 Stunden"
  - "drei Kalenderjahren"
  - "MaBV"
  - "Jahresfrist"
  - "Widerruf"
  - "Bereichsausnahmen"
  - "legal_calc"

must_flag:
  - "§ 35 GewO statt §§ 48, 49 VwVfG geprüft"
  - "Jahresfrist des § 48 Abs. 4 VwVfG nicht geprüft"
  - "Regelvermutungen als unwiderlegbar behandelt"
  - "Berufshaftpflicht und Weiterbildung des Wohnimmobilienverwalters vergessen"
  - "Abgrenzung zum Aufsichtsrecht übersehen"
---

# Test — gewerbeerlaubnis-34-gewo

Struktureller Smoke-Test. Die Ausgabe muss die Bestandserlaubnis über § 35 Abs. 8 GewO dem Widerrufsregime der §§ 48, 49 VwVfG zuordnen, die Jahresfrist des § 48 Abs. 4 VwVfG ab dem 15.09.2025 berechnen und den am 20.05.2026 verfügten Widerruf daran messen, die Untreueverurteilung der Regelvermutung des § 34c Abs. 2 Nr. 1 GewO zuordnen und deren Widerlegbarkeit ausweisen, die fehlende Berufshaftpflicht nach § 34c Abs. 2 Nr. 3 GewO und die Weiterbildungspflicht nach § 34c Abs. 2a GewO gesondert behandeln und die beabsichtigte Vermittlung geschlossener Investmentvermögen § 34f Abs. 1 S. 1 Nr. 2 GewO mit Abgrenzung zu KWG und WpIG zuordnen.

Run: `python ../../../scripts/eval.py --skill gewerberecht/skills/gewerbeerlaubnis-34-gewo`
