---
skill: kapitalmarktrecht/wphg-marktmissbrauch
fact_pattern: |
  Vorstand einer im Prime Standard der FWB notierten AG verhandelt seit
  acht Wochen mit einem strategischen Investor über die Veräußerung
  eines Geschäftsbereichs, der ca. 35 % des Konzernumsatzes ausmacht.
  Term Sheet seit gestern unterzeichnet, Signing in 4 Wochen geplant.
  Vorstandsvorsitzender will außerdem in 3 Wochen 5.000 Aktien aus
  einem Mitarbeiterprogramm verkaufen. Bilanzpressekonferenz steht in
  6 Wochen an. Bitte prüfen, ob Ad-hoc-Pflicht besteht, ob Aufschub
  nach Art. 17 IV MAR zulässig ist und welche Pflichten zu
  Insiderliste und Directors' Dealings (Closed Period) bestehen.

must_cite:
  - "Art. 7 MAR"
  - "Art. 14 MAR"
  - "Art. 17 MAR"
  - "Art. 17 IV MAR"
  - "Art. 18 MAR"
  - "Art. 19 MAR"
  - "§ 119 WpHG"
  - "§ 38 WpHG"

must_appear:
  - "Insiderinformation"
  - "präzise"
  - "kursrelevant"
  - "Selbstaufschub"
  - "Berechtigtes Interesse"
  - "Vertraulichkeit"
  - "Insiderliste"
  - "Directors' Dealings"
  - "Closed Period"
  - "unverzüglich"
  - "gestreckten Vorgang"
  - "Endereignis"
  - "05.06.2026"
  - "35 zeitlich gestreckte Vorgänge"

must_flag:
  - "Aufschub Art. 17 IV ohne Dokumentation"
  - "Zwischenschritt nach überholter Geltl-Linie"
  - "Endereignis nicht dokumentiert bestimmt"
  - "Ad-hoc-Gremium nicht nachgeschult"
  - "Closed Period"
  - "Selbst-Bewertung"
---

# Test — wphg-marktmissbrauch

Struktureller Smoke-Test. Die vier Kriterien der Insiderinformation müssen geprüft sein, die drei Voraussetzungen des Selbstaufschubs (Art. 17 IV MAR) explizit abgehakt, Insiderliste und Closed Period adressiert sein.

**Rechtsstand seit 05.06.2026 (EU Listing Act, RL (EU) 2024/2811 / VO (EU) 2024/2809).** Der Sachverhalt ist ein zeitlich gestreckter Vorgang: das unterzeichnete Term Sheet ist ein **Zwischenschritt**. Die Prüfung muss zu dem Ergebnis kommen, dass daraus **keine Ad-hoc-Pflicht** folgt — veröffentlichungspflichtig ist allein das **Endereignis** (hier: Signing). Zugleich muss sie feststellen, dass die Insiderqualität nach Art. 7 MAR **unberührt** bleibt und Handelsverbot (Art. 14) sowie Insiderlisten-Pflicht (Art. 18) bereits jetzt greifen.

Die früheren Assertions unterstellten die überholte Zwischenschritt-Ad-hoc-Pflicht (Geltl-Linie) und wurden auf die Endereignis-Systematik umgestellt.

Run: `python ../../../scripts/eval.py --skill kapitalmarktrecht/skills/wphg-marktmissbrauch`
