---
skill: transportrecht/hgb-frachtfuehrerhaftung
fact_pattern: |
  Mandantin (Versender) hat dem Frachtführer F 24 Paletten Elektronik
  (Bruttogewicht insgesamt 6.300 kg, Warenwert 84.000 EUR) zur
  Beförderung Hamburg → München übergeben. Bei Ablieferung am 14.03.
  fehlen 3 Paletten (790 kg, Warenwert 11.200 EUR). F behauptet
  "Diebstahl auf bewachtem Parkplatz". Empfänger hat den Verlust am
  Tag der Ablieferung schriftlich angezeigt. Bitte Haftung nach § 425
  HGB, Höchstbetrag § 431 HGB und mögliche Durchbrechung § 435 HGB
  prüfen sowie Verjährungslauf § 439 HGB darstellen.

must_cite:
  - "§ 425 HGB"
  - "§ 426 HGB"
  - "§ 427 HGB"
  - "§ 431 HGB"
  - "§ 435 HGB"
  - "§ 438 HGB"
  - "§ 439 HGB"

must_appear:
  - "Obhutshaftung"
  - "8,33"
  - "SZR"
  - "Sonderziehungsrecht"
  - "Bruttogewicht"
  - "Leichtfertigkeit"
  - "Schadensanzeige"
  - "Verjährung"
  - "Schnittstellenkontrolle"

must_flag:
  - "Tageskurs"
  - "qualifiziertem Verschulden"
  - "Organisationsverschulden"
---

# Test — hgb-frachtfuehrerhaftung

Struktureller Smoke-Test. Höchstbetrag muss methodisch (8,33 SZR × kg) berechnet, der SZR/EUR-Tageskurs mit Datum gekennzeichnet sein. § 435 HGB ist sauber zu subsumieren (Vorsatz oder Leichtfertigkeit + Bewusstsein wahrscheinlichen Schadenseintritts). Tatfristen § 438 HGB und Verjährung § 439 HGB müssen kalendarisch ausgewiesen sein.

Run: `python ../../../scripts/eval.py --skill transportrecht/skills/hgb-frachtfuehrerhaftung`
