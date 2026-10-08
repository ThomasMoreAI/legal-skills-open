---
skill: aussenwirtschaft-zoll-sanktionen/ausfuhr-dual-use-pruefung
fact_pattern: |
  Mandantin (Maschinenbau, Baden-Württemberg) will eine 5-Achs-CNC-
  Fräsmaschine mit Genauigkeit < 4 µm an einen türkischen Endkunden
  aus der Luft- und Raumfahrtindustrie liefern. Türkische Tochter eines
  europäischen Konzerns. Es liegt eine Endverbleibserklärung vor, in der
  ausschließlich zivile Anwendungen erklärt werden. Mandantin fragt, ob
  eine Einzelgenehmigung erforderlich ist, ob EU001 greifen kann, und
  wie das Catch-all-Risiko zu bewerten ist.

must_cite:
  - "VO (EU) 2021/821"
  - "Art. 3"
  - "Art. 4"
  - "AWG"
  - "§ 18 AWG"
  - "Anhang I"

must_appear:
  - "Güterklassifikation"
  - "Catch-all"
  - "militärische Endverwendung"
  - "EU-Allgemeine Genehmigung"
  - "BAFA"
  - "ELAN-K2"
  - "Endverbleibserklärung"
  - "Wartepflicht"

must_flag:
  - "Sanktions-Vorrang"
  - "Catch-all"
  - "Versand vor Genehmigung"
---

# Test — ausfuhr-dual-use-pruefung

Struktureller Smoke-Test. Die 4 Stufen müssen alle im Output erscheinen; Catch-all Art. 4 darf nicht übersprungen werden; § 18 AWG-Strafbarkeitshinweis muss enthalten sein; EU-AGG-Prüfung darf nicht unter den Tisch fallen.

Run: `python ../../../scripts/eval.py --skill aussenwirtschaft-zoll-sanktionen/skills/ausfuhr-dual-use-pruefung`
