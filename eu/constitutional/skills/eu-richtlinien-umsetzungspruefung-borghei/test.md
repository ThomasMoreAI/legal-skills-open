---
skill: europarecht/eu-richtlinien-umsetzungspruefung
fact_pattern: |
  Eine EU-Verbraucherschutz-Richtlinie räumt Verbrauchern ein
  konkretes Informations- und Widerrufsrecht ein. Die Umsetzungsfrist
  ist seit sechs Monaten abgelaufen; die Bundesrepublik hat nicht
  umgesetzt. Mandant ist Verbraucher und will sich vor dem Amtsgericht
  gegenüber einem privaten Online-Händler unmittelbar auf die
  Richtlinie berufen. Hilfsweise erwägt Mandant Schadensersatz gegen
  die BRD.

must_cite:
  - "Art. 288 AEUV"
  - "Art. 4 Abs. 3 EUV"
  - "Marshall"
  - "Faccini Dori"
  - "Francovich"
  - "§ 839 BGB"

must_appear:
  - "richtlinienkonforme Auslegung"
  - "unmittelbare Wirkung"
  - "vertikal"
  - "horizontal"
  - "hinreichend qualifiziert"
  - "Francovich"

must_flag:
  - "horizontale unmittelbare Wirkung"
  - "contra legem"
  - "funktionaler Staatsbegriff"
---

# Test — eu-richtlinien-umsetzungspruefung

Struktureller Smoke-Test. Die drei Stufen (RL-konforme Auslegung → unmittelbare Wirkung → Francovich) müssen in dieser Reihenfolge geprüft werden; die Abgrenzung vertikal/horizontal muss klar herauskommen.

Run: `python ../../../scripts/eval.py --skill europarecht/skills/eu-richtlinien-umsetzungspruefung`
