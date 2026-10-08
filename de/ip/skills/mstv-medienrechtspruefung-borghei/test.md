---
skill: urheber-medienrecht/mstv-medienrechtspruefung
fact_pattern: |
  Mandantin (Geschäftsführerin eines mittelständischen KMU, Sitz NRW)
  wurde in einem journalistisch-redaktionellen Online-Magazin
  (Sitz Hamburg) am 12.05. mit der Tatsachenbehauptung konfrontiert,
  sie habe für ihr Unternehmen am 10.05. „Insolvenz angemeldet". Das
  ist nachweislich unrichtig — kein Insolvenzantrag gestellt, kein
  Verfahren eröffnet. Mandantin nimmt am 18.05. Kenntnis und möchte
  Gegendarstellung verlangen, hilfsweise Berichtigung und
  Unterlassung. Zusätzlich Frage, ob das Online-Magazin
  Impressumspflichten nach § 18 MStV einhält und einen
  Verantwortlichen nach § 18 II MStV ausweist.

must_cite:
  - "§ 18 MStV"
  - "§ 19 MStV"
  - "§ 20 MStV"
  - "§ 823 BGB"
  - "§ 1004 BGB"
  - "Art. 5"
  - "LPresseG"

must_appear:
  - "Tatsachenbehauptung"
  - "Meinungsäußerung"
  - "unverzüglich"
  - "3 Monate"
  - "Aktualität"
  - "Berechtigtes Interesse"
  - "Berichtigung"
  - "allgemeines Persönlichkeitsrecht"
  - "Verantwortlicher"
  - "Impressum"

must_flag:
  - "unverzüglich, spätestens 3 Monate"
  - "Tatsachen-/Meinungs-Abgrenzung"
  - "eigenhändige Unterschrift des Betroffenen, nicht des Anwalts"
  - "Umfang** wesentlich länger als die beanstandete Mitteilung"
  - "§ 935, 940 ZPO"
---

# Test — mstv-medienrechtspruefung

Struktureller Smoke-Test. Die acht Voraussetzungen der Gegendarstellung müssen sichtbar abgearbeitet sein (Tatsachenbehauptung, Betroffenheit, berechtigtes Interesse, Frist, Form, Umfang, Aktualität, sachgerechte Wiedergabe). Inhaltsverbote (Meinung/Werbung/Strafbar) müssen explizit genannt sein. Die parallele Impressumsprüfung § 18 MStV mit Verantwortlichem § 18 II muss in einem eigenen Abschnitt erscheinen.

Run: `python ../../../scripts/eval.py --skill urheber-medienrecht/skills/mstv-medienrechtspruefung`
