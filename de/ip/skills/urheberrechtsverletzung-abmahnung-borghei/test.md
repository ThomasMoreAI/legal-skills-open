---
skill: urheber-medienrecht/urheberrechtsverletzung-abmahnung
fact_pattern: |
  Mandantin (Berufsfotografin, gewerblich tätig) entdeckt ein eigenes
  Lichtbildwerk (Architekturfotografie, 2021 entstanden, mit
  Urhebervermerk auf der Originalwebsite) unverändert und ohne
  Urhebernennung auf der kommerziellen Produktseite eines
  Online-Möbelhändlers (GmbH). Keine Lizenzierung erfolgt.
  Mandantin möchte Abmahnung versenden, Unterlassung verlangen,
  Schadensersatz nach Lizenzanalogie (MFM 2020) zzgl. 100 %-Zuschlag
  wegen fehlender Urhebernennung.

must_cite:
  - "§ 2 UrhG"
  - "§ 15 UrhG"
  - "§ 19a UrhG"
  - "§ 72 UrhG"
  - "§ 97 UrhG"
  - "§ 97a UrhG"
  - "§ 101 UrhG"
  - "§ 102 UrhG"

must_appear:
  - "Werkqualität"
  - "Aktivlegitimation"
  - "öffentliche Zugänglichmachung"
  - "dreifache Schadensberechnung"
  - "Lizenzanalogie"
  - "MFM"
  - "Verletzergewinn"
  - "Unterlassungserklärung"
  - "§ 97a II"
  - "Wiederholungsgefahr"

must_flag:
  - "Pauschale § 97a III-Deckelung"
  - "Schutzdauer § 64 UrhG"
  - "Verjährung § 102 UrhG"
  - "Aufschlag bei fehlender Urhebernennung"
---

# Test — urheberrechtsverletzung-abmahnung

Struktureller Smoke-Test. Erwartete Anspruchsstufen (Werkqualität → Aktivlegitimation → Verletzungshandlung → Schranken → §§ 97 ff. Rechtsfolgen → § 97a Abmahnung) müssen alle im Output erscheinen. Dreifache Schadensberechnung muss in allen drei Varianten dargestellt werden, auch wenn die Mandantin sich für die Lizenzanalogie entscheidet.

Run: `python ../../../scripts/eval.py --skill urheber-medienrecht/skills/urheberrechtsverletzung-abmahnung`
