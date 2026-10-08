---
skill: vergaberecht/vergabe-eu-schwellenwert-pruefung
fact_pattern: |
  Kommunaler Auftraggeber (Stadt mit 60.000 EW, juristische Person
  des öffentlichen Rechts) plant Beschaffung einer Fachsoftware
  einschließlich vierjähriger Wartung. Geschätzter Wert: 70.000 EUR
  netto pro Jahr, Gesamtlaufzeit 48 Monate, Verlängerungsoption
  zweimal 12 Monate. Eine Aufteilung in Lose (Lizenz / Wartung /
  Schulung) wird erwogen. Bitte Auftragswert nach § 3 VgV ermitteln,
  Schwellenwertprüfung durchführen und Verfahrensart vorschlagen.

must_cite:
  - "§ 99 GWB"
  - "§ 106 GWB"
  - "§ 3 VgV"
  - "§ 14 VgV"
  - "RL 2014/24/EU"

must_appear:
  - "Vollwertprinzip"
  - "Lossplitting"
  - "Schwellenwert"
  - "Oberschwellen"
  - "Verfahrensart"
  - "VO (EU)"
  - "Bundestariftreuegesetz"
  - "50.000 EUR netto"
  - "Vergabebeschleunigungsgesetz"
  - "Direktauftrag"

must_flag:
  - "Verlängerungsoption"
  - "Splittingverbot"
  - "Schwellenwert-Stand"
  - "Vergaberechtstransformationsgesetz"
  - "Landesvergabe"
---

# Test — vergabe-eu-schwellenwert-pruefung

Struktureller Smoke-Test. Erwartet wird, dass der Output das Vollwertprinzip § 3 Abs. 1 VgV anwendet, Verlängerungsoptionen in die Schätzung einrechnet, das Splittingverbot § 3 Abs. 7 VgV adressiert und die Schwellenwerte mit `[unverifiziert]`-Markierung versieht.

**Aktualitäts-Assertions (Stand 2026-07).** Der Skill muss zwei Wertschwellen sauber trennen: den **EU-Schwellenwert** und die davon unabhängige **BTTG-Schwelle von 50.000 EUR netto** für Bundesaufträge (in Kraft seit 01.05.2026, BGBl. 2026 I Nr. 119; ausgenommen Lieferaufträge und Bundeswehr). Ebenfalls gefordert: der Hinweis, dass **Direktauftrags- und Unterschwellen-Wertgrenzen** durch das seit **01.07.2026** geltende **Vergabebeschleunigungsgesetz** verändert wurden und nicht aus älteren Mustern übernommen werden dürfen.

`Vergaberechtstransformationsgesetz` steht unter `must_flag`, weil der Skill diesen Ampel-Arbeitstitel **ausdrücklich als falschen Gesetzesnamen kennzeichnen** muss. `Landesvergabe` sichert die Abgrenzung Bund/Land — im Sachverhalt ist der Auftraggeber eine **Kommune**, das BTTG greift dort nicht.

Run: `python ../../../scripts/eval.py --skill vergaberecht/skills/vergabe-eu-schwellenwert-pruefung`
