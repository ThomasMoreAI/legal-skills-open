---
skill: verkehrsrecht/stvg-haftungspruefung
fact_pattern: |
  Mandant (Fahrer 1) fährt innerorts auf das vor einer Ampelanlage
  verkehrsbedingt abbremsende Fahrzeug von Fahrer 2 auf. Beide
  Fahrzeuge sind haftpflichtversichert. Reparaturkosten brutto laut
  SV-Gutachten 8.400 EUR, Wiederbeschaffungswert 7.000 EUR, Restwert
  1.200 EUR. Fahrer 2 lässt das Fahrzeug reparieren und nutzt es
  unstreitig weiter. Mandant beauftragt Prüfung der Quote und der
  ersatzfähigen Schadensposten.

must_cite:
  - "§ 7 StVG"
  - "§ 17 StVG"
  - "§ 18 StVG"
  - "§ 115 VVG"
  - "§ 249 BGB"
  - "§ 254 BGB"

must_appear:
  - "Halterhaftung"
  - "Fahrerhaftung"
  - "Betriebsgefahr"
  - "130%"
  - "Wiederbeschaffungsaufwand"
  - "Anscheinsbeweis"
  - "Direktanspruch"
  - "Quotelung"

must_flag:
  - "Pauschalquote ohne Subsumtion"
  - "130%-Grenze ohne Weiternutzungsnachweis"
  - "Verjährung § 14 StVG"
---

# Test — stvg-haftungspruefung

Struktureller Smoke-Test. Erwartet werden Quotelung nach § 17 StVG (Anscheinsbeweis Auffahrunfall), Direktanspruch § 115 VVG, 130%-Prüfung mit Weiternutzungsnachweis.

Run: `python ../../../scripts/eval.py --skill verkehrsrecht/skills/stvg-haftungspruefung`
