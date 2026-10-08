---
skill: umweltrecht/bimschg-genehmigungsverfahren
fact_pattern: |
  Mandantin plant in Niedersachsen am Standort Außenbereich (§ 35 BauGB)
  eine Mastanlage mit 2.000 Mastschweineplätzen (je > 30 kg). Nächste
  Wohnbebauung 380 m nordwestlich. Im Umkreis von 600 m FFH-Gebiet
  „Wiesenniederung X". Bitte Genehmigungsbedürftigkeit nach 4. BImSchV
  (Nr. 7.1), Verfahrensart, materielle Voraussetzungen § 5 BImSchG
  prüfen und Drittschutz / Verbandsklagerisiko einordnen.

must_cite:
  - "§ 4 BImSchG"
  - "§ 5 BImSchG"
  - "§ 10 BImSchG"
  - "§ 19 BImSchG"
  - "4. BImSchV"
  - "9. BImSchV"
  - "TA Luft"
  - "§ 2 UmwRG"

must_appear:
  - "Genehmigungsbedürftigkeit"
  - "Anhang 1"
  - "förmlichem"
  - "Öffentlichkeitsbeteiligung"
  - "Schutzpflicht"
  - "Vorsorgepflicht"
  - "Stand der Technik"
  - "Drittschutz"
  - "Verbandsklage"

must_flag:
  - "FFH"
  - "Verhältnismäßigkeit"
  - "BVT"
---

# Test — bimschg-genehmigungsverfahren

Struktureller Smoke-Test. Output muss formelle Voraussetzungen (Verfahren) und materielle Voraussetzungen (§ 5 BImSchG) sauber trennen sowie FFH- und Verbandsklage-Risiko adressieren.

Run: `python ../../../scripts/eval.py --skill umweltrecht/skills/bimschg-genehmigungsverfahren`
