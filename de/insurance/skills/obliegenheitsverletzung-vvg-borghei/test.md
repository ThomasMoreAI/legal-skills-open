---
skill: versicherungsrecht/obliegenheitsverletzung-vvg
fact_pattern: |
  Berufsunfähigkeitsversicherung, Antrag Mai 2021, Vertragsbeginn 01.07.2021.
  Antragsformular fragte in Textform nach "Behandlungen, Untersuchungen
  oder Beschwerden in den letzten 5 Jahren". Mandant hat eine
  orthopädische Behandlung 2018 (Bandscheibenvorfall, 3 Termine) nicht
  angegeben. Im September 2024 stellt Mandant Leistungsantrag wegen
  Berufsunfähigkeit aufgrund Bandscheibenleidens. Versicherer holt
  Auskunft beim behandelnden Arzt ein (Eingang 30.09.2024) und erklärt
  am 12.11.2024 Rücktritt nach § 19 Abs. 2 VVG; hilfsweise Anfechtung
  nach § 22 VVG iVm § 123 BGB.

must_cite:
  - "§ 19 VVG"
  - "§ 21 VVG"
  - "§ 22 VVG"
  - "§ 28 VVG"
  - "§ 123 BGB"
  - "§ 124 BGB"

must_appear:
  - "Belehrung"
  - "Textform"
  - "Monatsfrist"
  - "Kausalitätsgegenbeweis"
  - "grobe Fahrlässigkeit"
  - "Quotelung"
  - "Anfechtung"

must_flag:
  - "§ 21 Abs. 1"
  - "§ 19 Abs. 5"
  - "VVG aF"
---

# Test — obliegenheitsverletzung-vvg

Struktureller Smoke-Test. Belehrungspflicht § 19 Abs. 5 VVG, Monatsfrist § 21 Abs. 1 VVG, Verschuldensstaffel inkl. Quotelung § 28 Abs. 2 Satz 2 und Kausalitätsgegenbeweis § 28 Abs. 3 / § 21 Abs. 2 VVG müssen sichtbar geprüft sein. Keine Anwendung des VVG aF (§ 6 VVG aF Alles-oder-Nichts) — wenn doch: Fehler.

Run: `python ../../../scripts/eval.py --skill versicherungsrecht/skills/obliegenheitsverletzung-vvg`
