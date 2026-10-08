---
skill: entgelttransparenz-eu/entgelt-auskunftsanspruch
fact_pattern: |
  Eine Softwareentwicklerin bei einem privaten Arbeitgeber mit 180
  Beschäftigten verlangt am 15.07.2026 schriftlich Auskunft über das
  Vergleichsentgelt ihrer Tätigkeit. In ihrer Entgeltgruppe arbeiten vier
  männliche Kollegen mit derselben Tätigkeitsbeschreibung sowie zwei
  Kollegen, deren Aufgaben abweichen, aber vergleichbare Verantwortung
  tragen. Der Arbeitsvertrag enthält eine Klausel, wonach das Entgelt
  streng vertraulich zu behandeln ist. Der Arbeitgeber möchte die Auskunft
  unter Hinweis auf die Betriebsgröße und den Datenschutz vollständig
  verweigern und plant, in künftigen Bewerbungsgesprächen weiterhin nach
  dem bisherigen Gehalt zu fragen. Ein Betriebsrat besteht.

must_cite:
  - "Art. 5"
  - "Art. 6"
  - "Art. 7"
  - "Art. 12"
  - "§ 10 EntgTranspG"
  - "§ 12 EntgTranspG"
  - "§ 15 EntgTranspG"
  - "§ 80 BetrVG"
  - "Art. 157 AEUV"

must_appear:
  - "zwei Monaten"
  - "drei Monaten"
  - "200 Beschäftigten"
  - "sechs"
  - "Median"
  - "gleichwertig"
  - "Verschwiegenheit"
  - "Bringschuld"
  - "legal_calc"

must_flag:
  - "Zwei- und Dreimonatsfrist verwechselt"
  - "Schwellenwert der Richtlinie unterstellt"
  - "Individuelle Entgelte offengelegt"
  - "Frage nach der Gehaltshistorie beibehalten"
  - "Verschwiegenheitsklausel unverändert gelassen"
  - "Vergleichsgruppe nach Stellenbezeichnung"
---

# Test — entgelt-auskunftsanspruch

Struktureller Smoke-Test. Die Ausgabe muss zwischen dem geltenden EntgTranspG (Schwelle von mehr als 200 Beschäftigten nach § 12 Abs. 1, Sechs-Personen-Vergleichsgruppe, Dreimonatsfrist nach § 15 Abs. 3) und der Richtlinie (kein Schwellenwert, zwei Monate nach Art. 7 Abs. 4) unterscheiden und für den privaten Arbeitgeber die fehlende horizontale Wirkung berücksichtigen. Die Vergleichsgruppe ist nach Gleichwertigkeit im Sinne des Art. 4 zu bilden, nicht nach Tätigkeitsbezeichnung. Die Verschwiegenheitsklausel ist an Art. 7 Abs. 5 zu messen, die geplante Frage nach dem bisherigen Gehalt an Art. 5 Abs. 2. Eine vollständige Verweigerung ist zurückzuweisen; stattdessen sind Median bzw. Durchschnittswerte ohne identifizierbare Einzelentgelte auszuweisen und der Betriebsrat einzubinden.

Run: `python ../../../scripts/eval.py --skill entgelttransparenz-eu/skills/entgelt-auskunftsanspruch`
