---
skill: handelsrecht/handelsregister-eintragungspflicht
fact_pattern: |
  Mandant betreibt seit drei Jahren mit einem Partner einen
  Online-Shop für Industriebedarf als GbR. Jahresumsatz im laufenden
  Jahr ca. 2,4 Mio. EUR, sechs Beschäftigte, externe Lagerlogistik,
  doppelte Buchführung wird geführt. Bisher keine Eintragung im
  Handelsregister. Mandant fragt, ob er sich eintragen lassen muss,
  welche Firma er führen darf und wie sich eine (Nicht-)Eintragung
  gegenüber Geschäftspartnern auswirkt.

must_cite:
  - "§ 1 HGB"
  - "§ 2 HGB"
  - "§ 6 HGB"
  - "§ 15 HGB"
  - "§ 29 HGB"
  - "§ 377 HGB"

must_appear:
  - "Istkaufmann"
  - "Kannkaufmann"
  - "Formkaufmann"
  - "kaufmännische Einrichtung"
  - "negative Publizität"
  - "positive Publizität"
  - "Anmeldepflicht"
  - "Handelsregister"

must_flag:
  - "deklaratorische Wirkung"
  - "Gutgläubigkeit"
  - "Rügepflicht"
---

# Test — handelsregister-eintragungspflicht

Struktureller Smoke-Test. Alle vier Kaufmannskategorien (Ist/Kann/Land-Forst/Form) müssen geprüft, die drei Stufen des § 15 HGB sauber unterschieden und die Folgewirkung § 377 HGB adressiert werden.

Run: `python ../../../scripts/eval.py --skill handelsrecht/skills/handelsregister-eintragungspflicht`
