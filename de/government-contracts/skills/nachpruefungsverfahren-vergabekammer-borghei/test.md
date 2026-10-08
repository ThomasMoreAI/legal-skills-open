---
skill: vergaberecht/nachpruefungsverfahren-vergabekammer
fact_pattern: |
  Mandantin (mittelständischer IT-Dienstleister, GmbH) hat ein
  Angebot im offenen Verfahren einer Landesbehörde abgegeben
  (Auftragswert 450.000 EUR netto, Oberschwellenbereich). Am
  TT.MM.JJJJ erhielt sie elektronisch die Information nach § 134
  GWB, dass ihr Angebot wegen fehlender Vergleichbarkeit der
  Referenzen ausgeschlossen werde. Die Stillhaltefrist läuft.
  Mandantin hält den Ausschluss für rechtswidrig (Eignungsmaßstab
  intransparent). Bitte Antragsbefugnis und Rügeobliegenheit
  prüfen sowie Nachprüfungsantrag an die zuständige Vergabekammer
  entwerfen.

must_cite:
  - "§ 134 GWB"
  - "§ 155 GWB"
  - "§ 159 GWB"
  - "§ 160 GWB"
  - "§ 168 GWB"
  - "§ 169 GWB"
  - "§ 165 GWB"

must_appear:
  - "Antragsbefugnis"
  - "Rügeobliegenheit"
  - "10 Kalendertage"
  - "Stillhaltefrist"
  - "Suspensiveffekt"
  - "Akteneinsicht"

must_flag:
  - "Rüge verspätet"
  - "Stillhaltefrist"
  - "Beschwerdefrist"
---

# Test — nachpruefungsverfahren-vergabekammer

Struktureller Smoke-Test. Erwartet wird, dass der Output Antragsbefugnis (§ 160 Abs. 2 GWB) dreigliedrig prüft, die Rügeobliegenheit (§ 160 Abs. 3 GWB) mit Anknüpfungszeitpunkt benennt und die 10-Kalendertage-Frist sowie die Stillhaltefrist § 134 Abs. 2 GWB (10 KT elektronisch) berechnet.

Run: `python ../../../scripts/eval.py --skill vergaberecht/skills/nachpruefungsverfahren-vergabekammer`
