---
skill: barrierefreiheit-bfsg/bfsg-anwendungsbereich
fact_pattern: |
  Mandantin betreibt einen Online-Shop für Fahrradzubehör (B2C und B2B),
  beschäftigt acht Personen bei 3,4 Mio. EUR Jahresumsatz und 1,1 Mio. EUR
  Bilanzsumme. Sie vertreibt außerdem seit August 2025 einen selbst
  entwickelten E-Book-Reader als Zugabeartikel. In ihren Filialen stehen
  seit Mai 2013 Zahlungsterminals. Auf der Website liegen ein
  Produktvideo von März 2024, eine seit 2019 nicht mehr geänderte
  Presseseite und ein eingebundener Kartendienst eines Drittanbieters.
  Ein Rahmenvertrag über die Shop-Wartung wurde im Januar 2025 mit
  Laufzeit bis Ende 2032 geschlossen.

must_cite:
  - "§ 1 BFSG"
  - "§ 2 BFSG"
  - "§ 3 BFSG"
  - "§ 38 BFSG"
  - "§ 37 BFSG"
  - "§ 12a BGG"

must_appear:
  - "abschließend"
  - "Kleinstunternehmen"
  - "weniger als zehn"
  - "elektronischen Geschäftsverkehr"
  - "E-Book-Lesegeräte"
  - "Selbstbedienungsterminals"
  - "28. Juni 2025"
  - "27.06.2030"
  - "15 Jahre"
  - "BITV 2.0"
  - "legal_calc"

must_flag:
  - "Kleinstunternehmensausnahme auf Produkte erstreckt"
  - "Kleinstunternehmen falsch definiert"
  - "Katalog als Beispielsliste behandelt"
  - "B2B-Angebote einbezogen"
  - "Archivausnahme überdehnt"
  - "§ 38 Abs. 2 ab dem Stichtag gerechnet"
---

# Test — bfsg-anwendungsbereich

Struktureller Smoke-Test. Die Ausgabe muss die Kleinstunternehmenseigenschaft am Umsatz von 3,4 Mio. EUR scheitern lassen, jedenfalls aber klarstellen, dass § 3 Abs. 3 BFSG den E-Book-Reader als Produkt nicht ausnimmt. Der Shop muss § 1 Abs. 3 Nr. 5 BFSG zugeordnet, das B2B-Segment ausgenommen werden. Das Produktvideo von März 2024 und die Presseseite müssen an § 1 Abs. 4 Nr. 1 und Nr. 5 gemessen, der Drittkartendienst an Nr. 3 und Nr. 4 geprüft werden. Die Zahlungsterminals von Mai 2013 sind über § 38 Abs. 2 mit Fünfzehnjahresfrist ab Ingebrauchnahme zu behandeln, der Wartungsvertrag über § 38 Abs. 1 S. 2 mit der Grenze 27.06.2030.

Run: `python ../../../scripts/eval.py --skill barrierefreiheit-bfsg/skills/bfsg-anwendungsbereich`
