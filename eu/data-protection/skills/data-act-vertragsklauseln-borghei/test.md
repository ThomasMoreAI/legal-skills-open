---
skill: datenwirtschaftsrecht/data-act-vertragsklauseln
fact_pattern: |
  Ein Maschinenhersteller (Dateninhaber, 900 Beschäftigte) legt einem
  Predictive-Maintenance-Anbieter (Datenempfänger, 35 Beschäftigte,
  6 Mio. EUR Umsatz, keine verbundenen Unternehmen) einen
  Datenbereitstellungsvertrag vor, den er unverändert zur Unterschrift
  stellt. Der Entwurf enthält: einen Haftungsausschluss auch für grobe
  Fahrlässigkeit; das Recht des Herstellers, allein verbindlich zu
  bestimmen, ob die gelieferten Daten vertragsgemäß sind; ein
  Pauschalentgelt von 4.000 EUR monatlich ohne Kalkulationsnachweis
  einschließlich einer Marge von 30 Prozent; ein Verbot, während der
  Laufzeit Kopien der übermittelten Daten zu behalten; sowie ein Recht
  des Herstellers, Format und Umfang der Daten jederzeit ohne Begründung
  zu ändern. Vertragsschluss soll im März 2026 erfolgen.

must_cite:
  - "Art. 8"
  - "Art. 9"
  - "Art. 10"
  - "Art. 13"
  - "Art. 50"
  - "§ 5 DADG"
  - "§ 15 DADG"
  - "§ 307 BGB"
  - "§ 310 BGB"

must_appear:
  - "einseitig auferlegt"
  - "schwarze Liste"
  - "graue Liste"
  - "diskriminierungsfrei"
  - "Gegenleistung"
  - "KMU"
  - "Kalkulation"
  - "Kopie"
  - "Streitbeilegung"
  - "legal_calc"

must_flag:
  - "Art. 13 auf Altverträge angewandt"
  - "Marge gegenüber einem KMU"
  - "Pauschalentgelt ohne Kalkulationsnachweis"
  - "Haftungsausschluss für grobe Fahrlässigkeit"
  - "Art. 13 und §§ 305 ff. BGB vermengt"
---

# Test — data-act-vertragsklauseln

Struktureller Smoke-Test. Die Klauselmatrix muss den Haftungsausschluss und das alleinige Bestimmungsrecht der schwarzen Liste des Art. 13 Abs. 4 zuordnen, das Kopierverbot und den Änderungsvorbehalt der grauen Liste des Art. 13 Abs. 5 Buchst. e und g, und die Marge an Art. 9 Abs. 4 scheitern lassen, weil der Datenempfänger KMU ist. Die zeitliche Anwendbarkeit nach Art. 50 muss geprüft und bejaht werden. Für jede beanstandete Klausel ist eine konforme Alternativfassung auszuwerfen.

Run: `python ../../../scripts/eval.py --skill datenwirtschaftsrecht/skills/data-act-vertragsklauseln`
