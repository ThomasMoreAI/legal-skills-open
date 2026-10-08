---
skill: kartellrecht/marktbeherrschung-bewertung
fact_pattern: |
  Mandantschaft (kleinerer Online-Händler) wirft einer großen Platt-
  form (Marktanteil im sachlichen Markt Online-Marktplatz > 50 %, vom
  BKartA voraussichtlich als Unternehmen mit überragender markt-
  übergreifender Bedeutung iSv § 19a I GWB festgestellt) Self-
  Preferencing vor: gleichartige Eigenangebote werden im Ranking
  systematisch vor Drittangeboten platziert; gleichzeitig nutzt die
  Plattform Daten der Drittanbieter zur Optimierung des eigenen
  Sortiments. Bitte Marktabgrenzung, Marktanteilsvermutung § 18 IV
  GWB, Behinderungsmissbrauch § 19 II Nr. 1 GWB und § 19a Abs. 2 Nr. 1
  GWB prüfen sowie parallel Art. 102 AEUV und Verhältnis zum DMA
  anreißen.

must_cite:
  - "§ 18"
  - "§ 19"
  - "§ 19a"
  - "Art. 102"
  - "§ 33"

must_appear:
  - "Marktabgrenzung"
  - "Bedarfsmarkt"
  - "Marktanteil"
  - "Vermutung"
  - "Behinderung"
  - "Self-Preferencing"
  - "objektive Rechtfertigung"
  - "Verhältnismäßigkeit"
  - "Bindungswirkung"

must_flag:
  - "10 %"
  - "Bußgeld"
  - "§ 19a"
  - "DMA"
---

# Test — marktbeherrschung-bewertung

Struktureller Smoke-Test. Output muss Marktabgrenzung (sachlich/räumlich), Marktanteilsvermutung § 18 IV GWB und § 19a GWB sauber trennen, Self-Preferencing als Behinderungsmissbrauch (§ 19 II Nr. 1 GWB, § 19a II Nr. 1 GWB) einordnen, objektive Rechtfertigung mit Verhältnismäßigkeitskontrolle prüfen, Bußgeldrahmen bis 10 % Konzernumsatz und DMA-Schnittstelle (Plugin dsa-dma) erwähnen.

Run: `python ../../../scripts/eval.py --skill kartellrecht/skills/marktbeherrschung-bewertung`
