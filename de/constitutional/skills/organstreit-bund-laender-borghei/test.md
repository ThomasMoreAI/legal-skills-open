---
skill: verfassungsrecht/organstreit-bund-laender
fact_pattern: |
  Eine Bundestagsfraktion sieht ihr parlamentarisches Informationsrecht
  aus Art. 38 Abs. 1 S. 2 GG dadurch verletzt, dass die Bundesregierung
  eine substantiierte Antwort auf eine Kleine Anfrage verweigert. Die
  Verweigerung wurde der Fraktion vor vier Monaten bekannt. Bitte
  Verfahrenswahl klären (Organstreit / Bund-Länder-Streit / abstrakte
  Normenkontrolle), Antragsberechtigung, Antragsgegenstand,
  Antragsbefugnis und Frist (§ 64 Abs. 3 BVerfGG) prüfen.

must_cite:
  - "Art. 93 I Nr. 1 GG"
  - "Art. 93 I Nr. 2 GG"
  - "Art. 93 I Nr. 3 GG"
  - "§ 63 BVerfGG"
  - "§ 64 BVerfGG"
  - "§ 68 BVerfGG"
  - "§ 76 BVerfGG"
  - "§ 31 BVerfGG"

must_appear:
  - "Verfahrenswahl"
  - "Organstreit"
  - "Bund-Länder-Streit"
  - "abstrakte Normenkontrolle"
  - "Parteifähigkeit"
  - "Antragsberechtigung"
  - "Antragsgegenstand"
  - "Antragsbefugnis"
  - "Frist"
  - "sechs Monate"

must_flag:
  - "Bekanntwerden"
  - "Konkurrenz"
---

# Test — organstreit-bund-laender

Struktureller Smoke-Test. Verfahrenswahl muss explizit getroffen werden, alle drei Verfahrensarten müssen begrifflich auftauchen, Frist § 64 Abs. 3 BVerfGG mit Anker „Bekanntwerden" muss adressiert sein.

Run: `python ../../../scripts/eval.py --skill verfassungsrecht/skills/organstreit-bund-laender`
