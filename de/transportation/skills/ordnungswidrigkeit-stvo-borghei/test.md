---
skill: verkehrsrecht/ordnungswidrigkeit-stvo
fact_pattern: |
  Mandantin (38, Außendienstmitarbeiterin) hat Bußgeldbescheid wegen
  Überschreitung der zulässigen Höchstgeschwindigkeit außerorts um
  42 km/h erhalten — Geldbuße, FAER-Punkte, 1 Monat Fahrverbot. Messung
  mit PoliScan Speed M1, Toleranzabzug erfolgt. Zustellungsdatum
  bekannt. Akteneinsicht in Rohmessdaten und Bedienungsanleitung
  bislang nicht beantragt. Mandantin ist beruflich zwingend auf
  Fahrerlaubnis angewiesen.

must_cite:
  - "§ 24 StVG"
  - "§ 25 StVG"
  - "§ 26 StVG"
  - "§ 67 OWiG"
  - "§ 66 OWiG"
  - "§ 4 IV BKatV"
  - "§ 147 StPO"

must_appear:
  - "Einspruchsfrist"
  - "Verfolgungsverjährung"
  - "Akteneinsicht"
  - "Rohmessdaten"
  - "standardisiertes Messverfahren"
  - "Absehen"
  - "Fahrverbot"

must_flag:
  - "Stand BKatV-Anlage"
  - "Punkte- oder Bußgeldhöhe"
  - "§ 21 OWiG"
---

# Test — ordnungswidrigkeit-stvo

Struktureller Smoke-Test. Erwartet werden formelle Bescheidprüfung § 66 OWiG, Verjährung § 26 III StVG, Akteneinsichtsanträge § 147 StPO iVm § 46 OWiG, Absehen § 4 IV BKatV.

Run: `python ../../../scripts/eval.py --skill verkehrsrecht/skills/ordnungswidrigkeit-stvo`
