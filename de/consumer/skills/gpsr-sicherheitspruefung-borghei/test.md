---
skill: produktrecht/gpsr-sicherheitspruefung
fact_pattern: |
  Mandantin (mittelständischer Importeur mit Sitz in DE) bringt ab
  02/2025 einen Smart-Home-Bewegungssensor in den EU-Markt. Hersteller
  sitzt in CN. Das Produkt enthält ein Funkmodul (Bluetooth Low
  Energy) und wird über einen Online-Marktplatz vertrieben. Mandantin
  fragt nach Pflichten als Importeur, Abgrenzung zur RED 2014/53/EU,
  Pflichten des Online-Marktplatzes (Art. 22 GPSR), Inhalt der
  technischen Dokumentation und Vorfallsmeldepflicht.

must_cite:
  - "VO (EU) 2023/988"
  - "Art. 5"
  - "Art. 9"
  - "Art. 11"
  - "Art. 20"
  - "Art. 22"
  - "Art. 36"
  - "RED"

must_appear:
  - "Importeur"
  - "Hersteller"
  - "Online-Marktplatz"
  - "Risikoanalyse"
  - "technische Dokumentation"
  - "Safety Business Gateway"
  - "Rückruf"
  - "sektorale Harmonisierung"

must_flag:
  - "13.12.2024"
  - "10 Jahre"
  - "unverzüglich"
---

# Test — gpsr-sicherheitspruefung

Struktureller Smoke-Test. Anwendungsbereich (Verbraucherprodukt, sektoraler Vorrang RED) und vollständiger Pflichtenkatalog der relevanten Rolle (Importeur Art. 11) müssen erscheinen; Pflichten der Online-Marktplätze Art. 22 GPSR müssen separat behandelt werden; technische Dokumentation mit 10-Jahre-Aufbewahrung und Safety-Business-Gateway-Meldung müssen vorkommen.

Run: `python ../../../scripts/eval.py --skill produktrecht/skills/gpsr-sicherheitspruefung`
