---
skill: migrationsrecht/aufenthaltstitel-pruefung
fact_pattern: |
  Mandantin (Indien, 32 J., Informatikerin, M.Sc.) hat Arbeitsvertragsangebot
  eines deutschen IT-Unternehmens, Bruttojahresgehalt 60.000 €. Abschluss
  ANABIN-bewertet. Sie befindet sich derzeit in Indien. Bitte Titelart
  zuordnen, § 5 AufenthG prüfen und Verfahren (Visumantrag) skizzieren.

must_cite:
  - "§ 4 AufenthG"
  - "§ 5 AufenthG"
  - "§ 18b AufenthG"
  - "§ 6 AufenthG"
  - "§ 39 AufenthG"

must_appear:
  - "Blaue Karte EU"
  - "Lebensunterhalt"
  - "Identitätsklärung"
  - "Ausweisungsinteresse"
  - "Visumverfahren"
  - "Bundesagentur für Arbeit"

must_flag:
  - "Ausweisungsinteresse"
  - "Identitätsklärung"
  - "Gehaltsschwelle"
  - "Verlängerungsantrag"
---

# Test — aufenthaltstitel-pruefung

Struktureller Smoke-Test. Erwartete Prüfung von § 5 AufenthG (Lebensunterhalt, Identitätsklärung, Ausweisungsinteresse, Passpflicht) muss sichtbar sein. Verfahrensseite (Visumverfahren, Beteiligung BA) muss erscheinen.

Run: `python ../../../scripts/eval.py --skill migrationsrecht/skills/aufenthaltstitel-pruefung`
