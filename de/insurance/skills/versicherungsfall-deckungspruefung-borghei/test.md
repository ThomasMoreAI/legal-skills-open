---
skill: versicherungsrecht/versicherungsfall-deckungspruefung
fact_pattern: |
  Mandant hat seit 2015 Wohngebäudeversicherung (VGB 2014). Im März
  trat im Badezimmer im OG nach und nach Wasser unter dem Boden aus;
  Sachverständiger stellt undichte Silikonfuge an der Duschtasse fest,
  Schaden ca. 18.000 €. Versicherer lehnt mit Verweis auf AVB-Klausel
  "Nässeschäden infolge Abnutzung sind ausgeschlossen" ab. Mandant
  bestreitet, dass es sich um Abnutzung handele.

must_cite:
  - "§ 1 VVG"
  - "§ 305c Abs. 2 BGB"
  - "§ 307 BGB"
  - "§ 28 VVG"

must_appear:
  - "Versicherungsfall"
  - "Risikoausschluss"
  - "Leistungsfreiheit"
  - "Empfängerhorizont"
  - "durchschnittlichen Versicherungsnehmers"
  - "Unklarheitenregel"
  - "Beweislast"

must_flag:
  - "verhüllte Obliegenheit"
  - "VVG aF"
  - "Frist"
---

# Test — versicherungsfall-deckungspruefung

Struktureller Smoke-Test. Drei Prüfungsstufen (Versicherungsfall / Risikoausschluss / Leistungsfreiheit) müssen sichtbar abgearbeitet, AVB-Auslegung am Empfängerhorizont des durchschnittlichen VN orientiert, Unklarheitenregel § 305c Abs. 2 BGB und Beweislastverteilung adressiert sein.

Run: `python ../../../scripts/eval.py --skill versicherungsrecht/skills/versicherungsfall-deckungspruefung`
