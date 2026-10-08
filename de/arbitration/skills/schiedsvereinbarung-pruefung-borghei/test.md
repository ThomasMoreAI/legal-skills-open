---
skill: schiedsverfahren-adr/schiedsvereinbarung-pruefung
fact_pattern: |
  Mandantin ist eine GmbH, die Photovoltaikanlagen an private Hauseigentümer
  verkauft. In ihren AGB steht: "Streitigkeiten aus diesem Vertrag
  entscheidet ein Schiedsgericht in Frankfurt." Ein Kunde hat vor dem
  Landgericht auf Rückabwicklung geklagt; die Klageerwiderung ist noch
  nicht eingereicht, ein Termin zur mündlichen Verhandlung steht in sechs
  Wochen an. Parallel besteht ein Liefervertrag mit einem spanischen
  Modulhersteller, dessen Klausel auf die "Internationale Handelskammer in
  Frankfurt" verweist, ohne Schiedsort und Schiedsrichterzahl zu regeln;
  dort wurde der Mandantin am 10.03.2026 die Zusammensetzung eines
  Schiedsgerichts mitgeteilt, bei dem der Hersteller zwei von drei
  Schiedsrichtern benannt hat.

must_cite:
  - "§ 1025 ZPO"
  - "§ 1029 ZPO"
  - "§ 1030 ZPO"
  - "§ 1031 ZPO"
  - "§ 1032 ZPO"
  - "§ 1034 ZPO"
  - "§ 1040 ZPO"
  - "§ 1043 ZPO"
  - "§ 1062 ZPO"
  - "§ 126a BGB"

must_appear:
  - "Verbraucher"
  - "eigenhändig"
  - "gesonderte"
  - "Schiedsort"
  - "Trennungsprinzip"
  - "zwei Wochen"
  - "eines Monats"
  - "Oberlandesgericht"
  - "undurchführbar"
  - "legal_calc"

must_flag:
  - "Verbraucherform des § 1031 Abs. 5 ZPO missachtet"
  - "Schiedseinrede zu spät erhoben"
  - "Zweiwochenfrist des § 1034 Abs. 2 ZPO übersehen"
  - "Schiedsort mit Verhandlungsort verwechselt"
  - "Trennungsprinzip ignoriert"
---

# Test — schiedsvereinbarung-pruefung

Struktureller Smoke-Test. Die Ausgabe muss die AGB-Schiedsklausel gegenüber dem privaten Hauseigentümer an § 1031 Abs. 5 ZPO scheitern lassen, die Schiedseinrede im Landgerichtsverfahren als vor Beginn der mündlichen Verhandlung zur Hauptsache zu erhebende Rüge terminieren, die ICC-Klausel auf Bestimmtheit und Undurchführbarkeit nach § 1032 Abs. 1 ZPO prüfen, die fehlende Schiedsrichterzahl über § 1034 Abs. 1 S. 2 ZPO auf drei ergänzen und die Zweiwochenfrist des § 1034 Abs. 2 ZPO ab 10.03.2026 berechnen. Schiedsort und Verhandlungsort sind zu trennen; das zuständige OLG nach § 1062 ZPO ist zu benennen.

Run: `python ../../../scripts/eval.py --skill schiedsverfahren-adr/skills/schiedsvereinbarung-pruefung`
