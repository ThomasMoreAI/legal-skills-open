---
skill: reise-fluggastrecht/reiseruecktritt-insolvenzschutz
fact_pattern: |
  Mandant buchte am 10.02.2026 bei einem kleineren Veranstalter eine
  Pauschalreise für 5.800 EUR mit Reisebeginn am 15.08.2026 und
  leistete eine Anzahlung von 1.200 EUR; einen Sicherungsschein hat
  er nie erhalten. Drei Wochen vor Abreise kommt es im Zielgebiet zu
  gewaltsamen Unruhen; das Auswärtige Amt spricht eine Reisewarnung
  für die Region aus. Zugleich teilt der Veranstalter eine
  Preiserhöhung um 11 % mit Verweis auf gestiegene Kerosinkosten mit.
  Der Veranstalter verlangt für einen Rücktritt 60 % Entschädigung
  und bietet alternativ einen Gutschein an.

must_cite:
  - "§ 651h Abs. 1 BGB"
  - "§ 651h Abs. 2 BGB"
  - "§ 651h Abs. 3 BGB"
  - "§ 651f BGB"
  - "§ 651g BGB"
  - "§ 651e BGB"
  - "§ 651r BGB"
  - "§ 651s BGB"
  - "§ 651t BGB"
  - "§ 307 BGB"

must_appear:
  - "unvermeidbare, außergewöhnliche Umstände"
  - "Bestimmungsort"
  - "Prognosezeitpunkt"
  - "Entschädigungspauschalen"
  - "8 % des Reisepreises"
  - "Sicherungsschein"
  - "Reisesicherungsfonds"
  - "Zahlungssperre"
  - "Rücktrittserklärung"
  - "14 Tagen"

must_flag:
  - "Persönlichen Grund unter § 651h Abs. 3 BGB subsumiert"
  - "Prognosezeitpunkt verschoben"
  - "Pauschale ungeprüft gezahlt"
  - "8-Prozent-Grenze übersehen"
  - "Anzahlung ohne Sicherungsschein geleistet"
  - "Gutschein akzeptiert"
---

# Test — reiseruecktritt-insolvenzschutz

Struktureller Smoke-Test. Der kostenfreie Rücktritt nach § 651h Abs. 3 BGB muss vom Rücktritt gegen Entschädigung nach Abs. 1 und 2 getrennt geführt und auf Umstände am Bestimmungsort begrenzt werden; persönliche Gründe müssen ausdrücklich ausgeschlossen sein. Der Prognosezeitpunkt muss benannt, die Pandemie-Kasuistik als streitig markiert sein. Die 8-Prozent-Grenze des § 651f BGB muss mit dem Kündigungs- bzw. Rücktrittsrecht des § 651g BGB verknüpft sein. Sicherungsschein und Zahlungssperre müssen als Prüfpunkt vor jeder Anzahlung erscheinen.

Run: `python ../../../scripts/eval.py --skill reise-fluggastrecht/skills/reiseruecktritt-insolvenzschutz`
