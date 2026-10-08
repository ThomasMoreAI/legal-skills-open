---
skill: versicherungsrecht/versicherungsmaklerhaftung
fact_pattern: |
  Gewerbekunde (GmbH) betreibt Lagerlogistik. Versicherungsmakler M
  vermittelt seit 2018 die Geschäftsversicherungen. Im Oktober 2020
  empfiehlt M für die Inhaltsdeckung Versicherungssumme 600.000 €,
  obwohl der Warenbestand ausweislich der Bilanzen ca. 1,2 Mio €
  beträgt. Beratungsprotokoll enthält nur den Satz "Inhaltsdeckung
  empfohlen, Sachversicherung gewünscht". Im August 2024 brennt das
  Lager teilweise ab, Schaden 980.000 €. Der Versicherer rechnet unter
  Berücksichtigung von Unterversicherung ab und zahlt 490.000 €. Die
  GmbH verlangt vom Makler die Differenz von 490.000 €.

must_cite:
  - "§ 60 VVG"
  - "§ 61 VVG"
  - "§ 62 VVG"
  - "§ 63 VVG"
  - "§ 280 BGB"
  - "§ 254 BGB"
  - "§ 195 BGB"
  - "§ 199 BGB"

must_appear:
  - "Sachwalter"
  - "Marktauswahl"
  - "Beratungsprotokoll"
  - "Textform"
  - "Unterversicherung"
  - "Mitverschulden"
  - "Vermutung beratungsgerechten Verhaltens"
  - "Verjährung"

must_flag:
  - "Abgrenzung"
  - "§ 34d GewO"
  - "IDD"
---

# Test — versicherungsmaklerhaftung

Struktureller Smoke-Test. Anspruchsaufbau §§ 60–63 VVG mit Schadensvermutung, Kausalitätsvermutung beratungsgerechten Verhaltens, Mitverschulden § 254 BGB und Verjährung §§ 195, 199 BGB müssen sichtbar geprüft sein. Abgrenzung Makler/Vertreter (§ 59 VVG, § 34d GewO) muss adressiert sein.

Run: `python ../../../scripts/eval.py --skill versicherungsrecht/skills/versicherungsmaklerhaftung`
