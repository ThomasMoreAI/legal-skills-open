---
skill: europarecht/vertragsverletzungsverfahren
fact_pattern: |
  Ein Bundesland hat eine EU-Luftqualitäts-Richtlinie nur lückenhaft
  umgesetzt; die Grenzwerte für NO2 werden in mehreren Städten seit
  Jahren überschritten. Die EU-Kommission hat ein Mahnschreiben nach
  Art. 258 AEUV an die Bundesrepublik gerichtet, Reaktionsfrist zwei
  Monate. Das Landesministerium fragt nach Antwortstrategie, Risiko
  eines späteren Zwangsgelds nach Art. 260 II AEUV und der
  innerstaatlichen Lastenverteilung Bund/Land.

must_cite:
  - "Art. 258 AEUV"
  - "Art. 260 AEUV"
  - "Art. 4 Abs. 3 EUV"
  - "Art. 23 GG"

must_appear:
  - "Mahnschreiben"
  - "Begründete Stellungnahme"
  - "Pauschalbetrag"
  - "Zwangsgeld"
  - "Streitgegenstandsbindung"
  - "Bund-Länder"

must_flag:
  - "Antwortfrist"
  - "Art. 260 III AEUV"
  - "Lastenverteilung"
---

# Test — vertragsverletzungsverfahren

Struktureller Smoke-Test. Die drei Verfahrensstufen (Mahnschreiben → Begründete Stellungnahme → Klage) und die Sanktionsstufe (Art. 260 II) müssen explizit auftauchen; Bund-Länder-Koordination muss adressiert sein.

Run: `python ../../../scripts/eval.py --skill europarecht/skills/vertragsverletzungsverfahren`
