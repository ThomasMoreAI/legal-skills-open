---
skill: patentrecht/patentverletzung-klage
fact_pattern: |
  Klägerin ist Inhaberin eines erteilten EP-Bündelpatents, in DE,
  FR und IT validiert, ohne UPC-Opt-out. Beklagte vertreibt seit
  14 Monaten ein Produkt, das sämtliche Merkmale des Hauptanspruchs
  wortlautidentisch verwirklicht. Die Beklagte hatte das Produkt
  zuvor auf einer Messe in Düsseldorf vorgestellt. Die Klägerin
  überlegt Klage am LG Düsseldorf vs. UPC Lokalkammer München.
  Verjährung § 141 PatG für die ersten Verletzungshandlungen
  steht im Raum. Beklagte droht mit Nichtigkeitsklage.

must_cite:
  - "§ 9 PatG"
  - "§ 14 PatG"
  - "§ 139 PatG"
  - "§ 140a PatG"
  - "§ 140b PatG"
  - "§ 141 PatG"
  - "§ 143 PatG"
  - "Art. 64 EPÜ"
  - "Art. 69 EPÜ"

must_appear:
  - "Merkmalsgliederung"
  - "Wortlautverletzung"
  - "Äquivalenz"
  - "Schneidmesser"
  - "dreifacher Schadensberechnung"
  - "Lizenzanalogie"
  - "Verletzergewinn"
  - "Düsseldorf"
  - "UPC"
  - "Opt-out"
  - "Aussetzung"

must_flag:
  - "Verjährung § 141 PatG"
  - "Opt-out-Status nicht geprüft"
  - "§ 143 III PatG"
---

# Test — patentverletzung-klage

Struktureller Smoke-Test. Klageschrift-Gerüst muss eine vollständige Merkmalsgliederung enthalten; Wortlautverletzung und (hilfsweise) Äquivalenz nach BGH-Trias müssen geprüft sein; alle drei Berechnungsmethoden des Schadensersatzes müssen genannt werden; Verjährung § 141 PatG, UPC-Opt-out-Status und Doppelvertretung § 143 III PatG müssen adressiert sein; Forumwahl LG vs. UPC muss strategisch begründet sein.

Run: `python ../../../scripts/eval.py --skill patentrecht/skills/patentverletzung-klage`
