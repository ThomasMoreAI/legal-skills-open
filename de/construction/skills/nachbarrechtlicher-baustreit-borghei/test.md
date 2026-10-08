---
skill: baurecht/nachbarrechtlicher-baustreit
fact_pattern: |
  Mandant wohnt in faktischem reinem Wohngebiet (§ 34 II BauGB iVm § 3
  BauNVO) in Nordrhein-Westfalen. Auf dem direkt angrenzenden Grundstück
  wurde der Bau einer fünfgeschossigen Wohnanlage durch BauG vom
  10.05.2026 genehmigt. Bekanntgabe an den Mandanten am 12.05.2026.
  Nach Einschätzung des Mandanten ist die Abstandsfläche nach § 6
  BauO NRW um 1,20 m unterschritten; daneben rechnet er mit erheblicher
  Verschattung des Wohn- und Schlafzimmers sowie mit Lärmimmissionen
  aus einer im Untergeschoss geplanten Tiefgarage. Bauausführung soll
  im Juni 2026 beginnen. Bitte Erfolgsaussichten der Drittanfechtung
  und Notwendigkeit des Eilrechtsschutzes (Sofortvollzug § 212a BauGB)
  sowie zivilrechtliche Flanke (§§ 1004, 906 BGB) prüfen.

must_cite:
  - "§ 42"
  - "§ 74 VwGO"
  - "§ 80"
  - "§ 80a"
  - "§ 212a BauGB"
  - "§ 906 BGB"
  - "§ 1004 BGB"
  - "§ 15 BauNVO"

must_appear:
  - "drittschützende Norm"
  - "Abstandsflächen"
  - "Rücksichtnahmegebot"
  - "aufschiebende Wirkung"
  - "Sofortvollzug"
  - "Wesentlichkeit"
  - "Ortsüblichkeit"

must_flag:
  - "drittschützende Norm"
  - "§ 212a"
  - "1 Monat"
---

# Test — nachbarrechtlicher-baustreit

Struktureller Smoke-Test. Drittschützende Norm muss konkret benannt sein (Abstandsfläche LBO; Rücksichtnahmegebot § 15 BauNVO; Gebietserhaltung § 34 II); Sofortvollzug § 212a BauGB und die daraus folgende Notwendigkeit des Antrags § 80 V iVm § 80a VwGO müssen ausdrücklich behandelt werden; 1-Monats-Klagefrist § 74 VwGO muss benannt und ausgerechnet sein; zivilrechtliche Spur muss § 906 BGB-Schritte (Wesentlichkeit, Ortsüblichkeit, Vermeidbarkeit, Geldausgleich) abarbeiten.

Run: `python ../../../scripts/eval.py --skill baurecht/skills/nachbarrechtlicher-baustreit`
