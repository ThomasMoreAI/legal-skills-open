---
skill: agrarrecht/agrar-grundstuecksverkehrsrecht
fact_pattern: |
  Mandant (Investor, kein Landwirt iSv § 1 ALG) hat notariellen
  Kaufvertrag über 22 ha Ackerland in Niedersachsen geschlossen
  (Kaufpreis 28.500 EUR/ha). Die Landwirtschaftsbehörde hat nach
  Einreichung des Vertrags durch den Notar nach § 9 Abs. 1 Nr. 1
  GrdstVG versagt. Begründung: ein örtlicher Landwirt (Hofstelle
  1,8 km entfernt, dokumentierter Aufstockungsbedarf) hat über die
  Siedlungsbehörde das Vorkaufsrecht nach § 4 RSG erklärt; Aus-
  übungsmitteilung an Mandant vor 5 Wochen. Bitte Beschwerde nach
  § 22 GrdstVG / § 9 LwVG prüfen, Frist sichern, ggf. Rückab-
  wicklung Kaufvertrag.

must_cite:
  - "§ 2 GrdstVG"
  - "§ 6 GrdstVG"
  - "§ 9 GrdstVG"
  - "§ 22 GrdstVG"
  - "§ 4 RSG"
  - "§ 6 RSG"
  - "LwVG"

must_appear:
  - "Genehmigungspflicht"
  - "ungesunden Verteilung"
  - "Nichtlandwirt"
  - "aufstockungsbedürftig"
  - "Siedlungsunternehmen"
  - "Vorkaufsrecht"
  - "schwebende Unwirksamkeit"
  - "Landwirtschaftsgericht"

must_flag:
  - "Beschwerdefrist"
  - "Genehmigungsfiktion"
  - "Verkehrswert"
  - "Zivilkammer"
---

# Test — agrar-grundstuecksverkehrsrecht

Struktureller Smoke-Test. Genehmigungspflicht § 2 GrdstVG, Versagungsgrund § 9 Abs. 1 Nr. 1, Siedlungs-Vorkaufsrecht § 4 RSG (Frist 2 Monate), schwebende Unwirksamkeit, Beschwerde § 22 GrdstVG vor OLG-Landwirtschaftssenat und Zuständigkeit Landwirtschaftsgericht (nicht Zivilkammer) müssen alle adressiert sein.

Run: `python ../../../scripts/eval.py --skill agrarrecht/skills/agrar-grundstuecksverkehrsrecht`
