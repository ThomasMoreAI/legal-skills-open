---
skill: gewerberecht/handwerksrolle-hwo
fact_pattern: |
  Mandant betreibt seit 2024 als Einzelunternehmer einen Betrieb für
  "Badsanierung aus einer Hand". Er verlegt Fliesen, montiert vorgefertigte
  Duschelemente, setzt Sanitärobjekte und schließt sie an vorhandene
  Leitungen an; Leitungsverlegung und Elektroarbeiten vergibt er an
  Nachunternehmer. Er hat 2018 die Gesellenprüfung im Fliesenlegerhandwerk
  bestanden und war ab 01.09.2019 durchgehend in einem Fliesenlegerbetrieb
  beschäftigt, davon ab 01.03.2021 als Vorarbeiter mit eigener
  Kolonnenverantwortung. Eine Eintragung in die Handwerksrolle besteht
  nicht. Die Behörde hat ihm am 15.04.2026 die Fortsetzung des Betriebs
  untersagt; beigefügt ist nur eine Stellungnahme der Handwerkskammer.
  Zusätzlich plant er, in seinem Möbelhandel gelegentlich Küchen zu
  montieren.

must_cite:
  - "§ 1 HwO"
  - "§ 3 HwO"
  - "§ 7 HwO"
  - "§ 7b HwO"
  - "§ 8 HwO"
  - "§ 16 HwO"
  - "§ 117 HwO"
  - "§ 14 GewO"
  - "§ 80 VwGO"

must_appear:
  - "Anlage A"
  - "Anlage B"
  - "wesentliche"
  - "drei Monaten"
  - "Gesamtbetrachtung"
  - "leitender Stellung"
  - "sechs Jahre"
  - "gemeinsamen Erklärung"
  - "Handwerkskarte"
  - "legal_calc"

must_flag:
  - "Berufsbild statt Tätigkeit geprüft"
  - "Dreimonatsgrenze"
  - "Gesamtbetrachtung nach § 1 Abs. 2 S. 3 HwO ausgelassen"
  - "Untersagung ohne gemeinsame Erklärung der Kammern"
  - "Betriebsleiterlösung nach § 7 Abs. 1 HwO übersehen"
---

# Test — handwerksrolle-hwo

Struktureller Smoke-Test. Die Ausgabe muss die einzelnen Arbeitsschritte tätigkeitsbezogen den Gewerben der Anlage A zuordnen (Fliesen-, Platten- und Mosaiklegerhandwerk sowie Installateur- und Heizungsbauerhandwerk), die Montage vorgefertigter Elemente an § 1 Abs. 2 S. 2 Nr. 1 und Nr. 2 HwO messen und die Gesamtbetrachtung nach S. 3 durchführen. Die Ausübungsberechtigung nach § 7b HwO ist zu rechnen: sechs Jahre ab 01.09.2019 und vier Jahre leitende Stellung ab 01.03.2021. Die Küchenmontage im Möbelhandel ist über § 3 HwO als möglicher Neben- oder Hilfsbetrieb zu prüfen. Die Untersagung vom 15.04.2026 ist mangels gemeinsamer Erklärung von Handwerkskammer und IHK nach § 16 Abs. 3 S. 2 HwO als rechtswidrig zu beanstanden.

Run: `python ../../../scripts/eval.py --skill gewerberecht/skills/handwerksrolle-hwo`
