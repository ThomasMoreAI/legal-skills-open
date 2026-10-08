---
skill: berufsrecht-anwaltschaft/rdg-abgrenzung
fact_pattern: |
  Startup S betreibt eine Online-Plattform, die Verbrauchern bei
  Fluggastrechten nach VO (EG) 261/2004 hilft: automatisierte
  Anspruchsprüfung anhand eines Fragebogens, Forderungsabtretung an
  S, außergerichtliche Geltendmachung gegenüber Airlines, gerichtliche
  Durchsetzung über Partner-Anwälte. Vergütung 30 % Provision im
  Erfolgsfall. S ist nicht im Rechtsdienstleistungsregister
  registriert. Bitte RDG-Abgrenzung, Vergleich mit BGH wenigermiete.de
  und Empfehlung zur Registrierungspflicht sowie zu den Folgen einer
  unterbliebenen Registrierung (§ 134 BGB, § 3a UWG).

must_cite:
  - "§ 2 RDG"
  - "§ 3 RDG"
  - "§ 5 RDG"
  - "§ 10 RDG"
  - "§ 134 BGB"
  - "§ 3a UWG"
  - "§§ 1, 3 BRAO"

must_appear:
  - "Rechtsdienstleistung"
  - "Anwaltsmonopol"
  - "Inkassodienstleistung"
  - "Nebenleistung"
  - "Schwerpunkt"
  - "Rechtsdienstleistungsregister"
  - "Registrierung"
  - "wenigermiete"
  - "Nichtigkeit"

must_flag:
  - "fehlende Registrierung führt zu Nichtigkeit"
  - "§ 134 BGB-Nichtigkeit"
  - "§ 3a UWG-Rechtsbruch"
---

# Test — rdg-abgrenzung

Struktureller Smoke-Test. § 2 RDG-Subsumtion muss vor Erlaubnistatbeständen geprüft werden. Schwerpunkt-Test bei § 5 RDG-Nebenleistung muss expressis verbis erscheinen. BGH wenigermiete.de (VIII ZR 285/18) muss als Bezugspunkt für Legal-Tech-Inkasso adressiert werden. Folgen unerlaubter RDL müssen § 134 BGB **und** § 3a UWG beide enthalten.

Run: `python ../../../scripts/eval.py --skill berufsrecht-anwaltschaft/skills/rdg-abgrenzung`
