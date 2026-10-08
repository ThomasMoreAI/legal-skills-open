---
skill: datenwirtschaftsrecht/data-act-anwendungsbereich
fact_pattern: |
  Mandantin ist ein Hersteller vernetzter Landmaschinen mit 180
  Beschäftigten und 60 Mio. EUR Jahresumsatz; alleinige Gesellschafterin
  ist eine Konzernholding mit 4.000 Beschäftigten. Die Maschinen erheben
  Telemetrie-, Verschleiß- und Ertragsdaten und werden seit 2022
  vertrieben; eine überarbeitete Baureihe soll im Oktober 2026 in Verkehr
  gebracht werden. Ein Kunde verlangt Zugang zu den Rohdaten seiner
  Maschine und deren Weitergabe an eine freie Werkstatt. Die
  Wartungsverträge sind unbefristet und stammen aus 2021. Die Mandantin
  hält die Auswertungsalgorithmen für Geschäftsgeheimnisse und beruft
  sich hilfsweise auf den Datenbankschutz.

must_cite:
  - "Art. 2"
  - "Art. 3"
  - "Art. 4"
  - "Art. 5"
  - "Art. 7"
  - "Art. 13"
  - "Art. 43"
  - "Art. 50"
  - "§ 2 DADG"
  - "§ 15 DADG"
  - "§ 16 DADG"
  - "§ 2 GeschGehG"

must_appear:
  - "vernetztes Produkt"
  - "verbundener Dienst"
  - "Dateninhaber"
  - "Kleinst- oder Kleinunternehmen"
  - "Partnerunternehmen"
  - "Bundesnetzagentur"
  - "12.09.2026"
  - "12.09.2027"
  - "12.01.2027"
  - "Torwächter"
  - "Geschäftsgeheimnis"
  - "legal_calc"

must_flag:
  - "Data Act als Datenschutzthema behandelt"
  - "Größenausnahme ohne Konzernprüfung bejaht"
  - "Geltungsbeginn pauschal"
  - "Rollen vermischt"
  - "Sui-generis-Datenbankschutz behauptet"
  - "Rechtsprechung erfunden"
---

# Test — data-act-anwendungsbereich

Struktureller Smoke-Test. Die Ausgabe muss die Größenausnahme des Art. 7 Abs. 1 wegen des verbundenen Konzernunternehmens **verneinen**, die Konzeptionspflicht des Art. 3 Abs. 1 nur für die ab Oktober 2026 in Verkehr gebrachte Baureihe bejahen und die Altverträge von 2021 als unbefristete Verträge nach Art. 50 UAbs. 6 erst ab dem 12.09.2027 der Missbrauchskontrolle des Art. 13 unterstellen. Der Datenbankschutz muss über Art. 43 gesperrt werden. Die Zuständigkeit der Bundesnetzagentur nach § 2 Abs. 1 DADG und der Bußgeldrahmen des § 15 DADG müssen erscheinen. Es darf keine Data-Act-Rechtsprechung ohne Marker genannt werden.

Run: `python ../../../scripts/eval.py --skill datenwirtschaftsrecht/skills/data-act-anwendungsbereich`
