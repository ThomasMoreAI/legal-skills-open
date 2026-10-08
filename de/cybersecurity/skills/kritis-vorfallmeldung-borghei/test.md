---
skill: kritis-resilienz/kritis-vorfallmeldung
fact_pattern: |
  Am 12.05.2026 um 21:40 Uhr stellt die Leitwarte eines Fernwärme- und
  Stromversorgers fest, dass zwei Umspannstationen durch Brandstiftung
  ausgefallen sind; gleichzeitig ist die Fernwirktechnik über einen
  manipulierten Fernzugang kompromittiert worden, und in der
  Kundendatenbank wurden Datensätze abgeflossen. Rund 42.000 Haushalte
  sind ohne Wärme, die voraussichtliche Dauer ist unklar. Die IT-Abteilung
  will erst die forensische Analyse abwarten, bevor gemeldet wird, und
  meint, eine Meldung an das BSI genüge. Grenzüberschreitende Auswirkungen
  auf einen österreichischen Abnehmer sind möglich.

must_cite:
  - "§ 4 KRITISDachG"
  - "§ 13 KRITISDachG"
  - "§ 18 KRITISDachG"
  - "§ 20 KRITISDachG"
  - "§ 24 KRITISDachG"
  - "Art. 33"
  - "§ 121 BGB"

must_appear:
  - "24 Stunden"
  - "unverzüglich"
  - "Kenntnis"
  - "einen Monat"
  - "Bundesamt für Bevölkerungsschutz"
  - "gemeinsame"
  - "grenzüberschreitende"
  - "unberührt"
  - "Anteil"
  - "legal_calc"

must_flag:
  - "Auf Ursachenklärung gewartet"
  - "24 Stunden als Regelzeitpunkt behandelt"
  - "Nur an das BSI gemeldet"
  - "Parallele Meldepflichten übersehen"
  - "Monatsbericht vergessen"
---

# Test — kritis-vorfallmeldung

Struktureller Smoke-Test. Die Ausgabe muss die Absicht, die Forensik abzuwarten, an § 18 Abs. 1 S. 1 KRITISDachG scheitern lassen, die 24-Stunden-Grenze ab Kenntnis am 12.05.2026 um 21:40 Uhr stundengenau ausweisen und zugleich klarstellen, dass „unverzüglich" früher bedeutet, den Monatsbericht nach § 18 Abs. 1 S. 3 terminieren, die Meldung an das BBK über die gemeinsame Meldestelle adressieren und die parallelen Pflichten nach BSIG und Art. 33 DSGVO als eigenständig darstellen (§ 18 Abs. 1 S. 4). Anzahl und Anteil der Betroffenen, Dauer, betroffenes Gebiet und die grenzüberschreitenden Auswirkungen auf Österreich sind nach Abs. 2 aufzunehmen.

Run: `python ../../../scripts/eval.py --skill kritis-resilienz/skills/kritis-vorfallmeldung`
