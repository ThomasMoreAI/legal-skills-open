---
skill: umweltrecht/uvp-verfahrenspruefung
fact_pattern: |
  Vorhabenträger plant in Brandenburg einen Windpark mit 18
  Windenergieanlagen Gesamthöhe je 230 m. Im 5-km-Umkreis stehen zwei
  bestehende Windparks mit jeweils 6 Anlagen, ein dritter ist
  beantragt. Die Genehmigungsbehörde hat eine allgemeine Vorprüfung
  des Einzelfalls § 7 Abs. 1 UVPG durchgeführt und UVP-Pflicht
  verneint, ohne kumulative Wirkungen § 10 UVPG zu dokumentieren.
  Bitte UVP-Pflicht prüfen, Vorprüfung auf Plausibilität bewerten und
  Rechtsfolgen für einen späteren Genehmigungsbescheid nach § 4 UmwRG
  einordnen.

must_cite:
  - "§ 5 UVPG"
  - "§ 7 UVPG"
  - "§ 10 UVPG"
  - "Anlage 1 UVPG"
  - "Anlage 3 UVPG"
  - "§ 4 UmwRG"
  - "§ 2 UmwRG"

must_appear:
  - "UVP-Pflicht"
  - "Vorprüfung"
  - "kumulative"
  - "Plausibilitätskontrolle"
  - "Dokumentation"
  - "Verfahrensfehler"
  - "Aufhebung"
  - "Verbandsklage"

must_flag:
  - "Altrip"
  - "Kausalität"
  - "Klagebefugnis"
---

# Test — uvp-verfahrenspruefung

Struktureller Smoke-Test. Output muss UVP-Pflicht (Anlage 1 + Kumulation § 10) sauber prüfen, Vorprüfung gegen Anlage 3 abgleichen und Verfahrensfehlerfolgen § 4 Abs. 1 vs. Abs. 1a UmwRG differenziert behandeln.

Run: `python ../../../scripts/eval.py --skill umweltrecht/skills/uvp-verfahrenspruefung`
