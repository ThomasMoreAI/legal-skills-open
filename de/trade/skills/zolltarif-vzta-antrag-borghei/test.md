---
skill: aussenwirtschaft-zoll-sanktionen/zolltarif-vzta-antrag
fact_pattern: |
  Importeur (Elektronikhändler) will ein neuartiges Bauteil erstmalig
  aus China einführen: ein „smartes Sensor-Modul" mit integrierter
  SIM-Karte, Gehäuse aus Kunststoff, Hauptfunktion Temperaturmessung
  und Übertragung via Mobilfunk. Die Tarifierung ist intern streitig:
  Kap. 85 (elektrische Geräte) vs. Kap. 90 (Messinstrumente). Importeur
  will einen Antrag auf verbindliche Zolltarifauskunft (Art. 33 UZK)
  stellen, um Rechtssicherheit für die Serieneinfuhr zu erlangen.

must_cite:
  - "Art. 33 UZK"
  - "VO (EU) 952/2013"
  - "AV 1"
  - "AV 3"

must_appear:
  - "Allgemeine Vorschriften"
  - "Warenbeschreibung"
  - "TARIC"
  - "verbindliche Zolltarifauskunft"
  - "120 Tage"
  - "3 Jahre"
  - "EZT"
  - "objektiven Merkmalen"

must_flag:
  - "Einstieg mit AV 3b"
  - "ein Antrag pro Ware"
  - "Erlöschen nach Art. 34 UZK"
---

# Test — zolltarif-vzta-antrag

Struktureller Smoke-Test. AV 1–6 müssen in Reihenfolge geprüft werden; vZTA-Bearbeitungsdauer 120 Tage und Bindungswirkung 3 Jahre müssen erscheinen; Warenbeschreibung muss erschöpfend gefordert sein; Konkurrenz Kap. 85 vs. 90 muss adressiert werden.

Run: `python ../../../scripts/eval.py --skill aussenwirtschaft-zoll-sanktionen/skills/zolltarif-vzta-antrag`
