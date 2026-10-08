---
skill: barrierefreiheit-bfsg/bfsg-produktkonformitaet
fact_pattern: |
  Mandantin importiert Zahlungsterminals aus Taiwan und vertreibt sie
  seit November 2025 unter eigener Marke in Deutschland und Österreich.
  Eine technische Dokumentation liegt nur auf Englisch und in Auszügen
  vor; eine EU-Konformitätserklärung wurde nicht ausgestellt, die
  CE-Kennzeichnung findet sich allein auf dem Versandkarton. Die
  Sprachausgabe des Terminals fehlt; die Mandantin hält deren Nachrüstung
  für unverhältnismäßig, hat dies aber nicht beurteilt und erhält für die
  Produktlinie einen Landeszuschuss zur Barrierefreiheit. Die
  Marktüberwachungsbehörde des Landes hat am 12.03.2026 mit einer
  Anhörungsfrist von fünf Tagen zur Stellungnahme aufgefordert.

must_cite:
  - "§ 4 BFSG"
  - "§ 6 BFSG"
  - "§ 9 BFSG"
  - "§ 12 BFSG"
  - "§ 16 BFSG"
  - "§ 17 BFSG"
  - "§ 18 BFSG"
  - "§ 19 BFSG"
  - "§ 22 BFSG"
  - "§ 37 BFSG"
  - "§ 28 VwVfG"

must_appear:
  - "Anlage 2"
  - "Anlage 4"
  - "technische Dokumentation"
  - "EU-Konformitätserklärung"
  - "CE-Kennzeichnung"
  - "zehn Tage"
  - "fünf Jahre"
  - "unverhältnismäßige Belastung"
  - "100.000 EUR"
  - "legal_calc"

must_flag:
  - "Rollenwechsel nach § 12 BFSG übersehen"
  - "§ 17 trotz Fördermitteln geltend gemacht"
  - "Konformitätserklärung ohne Ausweis der Ausnahmen"
  - "Anhörungsfrist unter zehn Tagen akzeptiert"
  - "Korrekturmaßnahmen auf den deutschen Markt beschränkt"
---

# Test — bfsg-produktkonformitaet

Struktureller Smoke-Test. Die Ausgabe muss die Mandantin über § 12 BFSG als Hersteller behandeln, die fehlende EU-Konformitätserklärung und die fehlerhaft angebrachte CE-Kennzeichnung als formale Nichtkonformität einordnen, die Berufung auf § 17 BFSG an der fehlenden Beurteilung und an der Sperre des § 17 Abs. 4 wegen des Landeszuschusses scheitern lassen, die Fünf-Tage-Anhörungsfrist an § 22 Abs. 2 S. 2 BFSG messen und die Korrekturmaßnahmen nach § 22 Abs. 3 auch auf den österreichischen Markt erstrecken. Der Bußgeldrahmen des § 37 BFSG ist tatbestandsbezogen zuzuordnen.

Run: `python ../../../scripts/eval.py --skill barrierefreiheit-bfsg/skills/bfsg-produktkonformitaet`
