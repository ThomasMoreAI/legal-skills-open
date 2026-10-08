---
skill: reise-fluggastrecht/fluggastrechte-vo-261
fact_pattern: |
  Zwei Mandanten flogen am 10.03.2023 in einheitlicher Buchung von
  Frankfurt über Dubai nach Singapur; ausführendes Unternehmen war
  auf beiden Teilstrecken eine Nicht-EU-Airline. Der Zubringer ab
  Frankfurt startete mit 100 Minuten Verspätung, der Anschluss in
  Dubai wurde verpasst. Das Endziel erreichten die Mandanten mit
  5 Stunden 20 Minuten Verspätung. Verpflegung wurde nicht gestellt;
  die Mandanten buchten selbst ein Hotelzimmer für 140 EUR. Die
  Airline beruft sich pauschal auf ein Gewitter in Dubai. Kenntnis
  aller Umstände hatten die Mandanten am 05.07.2023.

must_cite:
  - "Art. 3"
  - "Art. 4"
  - "Art. 5 Abs. 3"
  - "Art. 7"
  - "Art. 8"
  - "Art. 9"
  - "Art. 12"
  - "§ 195 BGB"
  - "§ 199 BGB"
  - "Art. 7 Nr. 1"
  - "§ 29 ZPO"

must_appear:
  - "ausführende Luftfahrtunternehmen"
  - "Großkreismethode"
  - "Endziel"
  - "250"
  - "400"
  - "600"
  - "außergewöhnliche Umstände"
  - "zumutbare Maßnahmen"
  - "Betreuungsleistungen"
  - "Ultimo-Regel"
  - "legal_calc"
  - "Ausgleichsforderung an die Airline"

must_flag:
  - "Anwendungsbereich nicht geprüft"
  - "Falscher Anspruchsgegner"
  - "Verspätung am Abflug statt am Endziel gemessen"
  - "Betreuungsansprüche vergessen"
  - "Verjährung nicht gerechnet"
---

# Test — fluggastrechte-vo-261

Struktureller Smoke-Test. Der Anwendungsbereich des Art. 3 muss vor jeder Bezifferung stehen und den Fall des Drittstaat-Abflugs mit Nicht-EU-Airline erfassen. Die Dreistufigkeit der Ausgleichsbeträge muss vollständig erscheinen, die Entfernung über die Großkreismethode zum Endziel bestimmt werden. Der Einwand nach Art. 5 Abs. 3 muss zweistufig (Ereignis und zumutbare Maßnahmen) geführt und die Beweislast der Airline zugewiesen werden. Betreuung und Erstattung müssen als vom Ausgleich unabhängige Ansprüche erscheinen. Die Verjährung muss über den Rechner mit der Ultimo-Regel verdrahtet sein.

Run: `python ../../../scripts/eval.py --skill reise-fluggastrecht/skills/fluggastrechte-vo-261`
