---
skill: arbeitsrecht/massenentlassungsanzeige
fact_pattern: |
  Mandantin betreibt ein Werk mit 180 regelmäßig Beschäftigten und einen
  angegliederten Vertriebsstandort mit 25 Beschäftigten; ein gemeinsamer
  Betriebsrat besteht. Sie plant, im Werk 22 Arbeitsverhältnisse zu kündigen
  und zusätzlich 6 Aufhebungsverträge anzubieten, alles im Zeitraum vom
  02.03. bis 25.03.2026. Die Geschäftsführung hat den Betriebsrat bislang
  nur mündlich in der Monatssitzung informiert und möchte die Kündigungen
  bereits am 06.03.2026 zustellen.
must_cite:
  - "§ 17 KSchG"
  - "§ 18 KSchG"
  - "§ 17 Abs. 2 KSchG"
  - "§ 17 Abs. 3 S. 1 KSchG"
  - "§ 17 Abs. 3 S. 3 KSchG"
  - "§ 18 Abs. 4 KSchG"
  - "§ 102 BetrVG"
  - "Richtlinie 98/59/EG"
must_appear:
  - "Konsultationsverfahren"
  - "Agentur für Arbeit"
  - "Muss-Angaben"
  - "Soll-Angaben"
  - "Entlassungssperre"
  - "Freifrist"
  - "Betriebsbegriff"
must_flag:
  - "Aufhebungsverträge nicht mitgezählt"
  - "Kündigung vor Abschluss des Konsultationsverfahrens"
  - "Abschrift nach § 17 Abs. 3 S. 1 KSchG vergessen"
  - "Freifrist § 18 Abs. 4 KSchG verstreichen lassen"
  - "Auf die Rechtsprechungsänderung 2024 vertraut, ohne sie zu verifizieren"
---

# Test — massenentlassungsanzeige

Prüft die Trennung von Konsultations- und Anzeigestrang, die Schwellen-
berechnung inklusive Aufhebungsverträgen und die Kennzeichnung der 2024
geänderten Rechtsprechung als verifizierungsbedürftig.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/massenentlassungsanzeige`
