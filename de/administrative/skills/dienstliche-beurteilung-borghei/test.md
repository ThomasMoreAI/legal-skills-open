---
skill: beamten-disziplinarrecht/dienstliche-beurteilung
fact_pattern: |
  Mandant ist Bundesbeamter (A 12) und erhielt zum Stichtag
  01.04.2026 eine Regelbeurteilung mit der Gesamtnote "entspricht
  den Anforderungen", nachdem er in den beiden Vorbeurteilungen mit
  "übertrifft die Anforderungen erheblich" bewertet worden war.
  Aufgabenzuschnitt und Vorgesetzte sind unverändert. Von den zwölf
  Einzelmerkmalen sind neun in der zweitbesten Stufe bewertet; die
  Begründung des Gesamturteils besteht aus einem Satz. Die Behörde
  verweist auf Richtwerte; die Vergleichsgruppe umfasst sieben
  Personen. Ein Beförderungsverfahren läuft bereits.

must_cite:
  - "§ 21 BBG"
  - "§ 9 BeamtStG"
  - "Art. 33 Abs. 2 GG"
  - "§ 113 VwGO"
  - "§ 114 VwGO"
  - "§ 123 VwGO"

must_appear:
  - "Anwendbares Recht"
  - "Beurteilungsrichtlinie"
  - "Beurteilungsspielraum"
  - "Verfahrensfehler"
  - "Unrichtiger Sachverhalt"
  - "Sachfremde Erwägungen"
  - "allgemeingültiger Wertmaßstäbe"
  - "Regelbeurteilung"
  - "Anlassbeurteilung"
  - "Richtwerte"
  - "Vergleichsgruppe"
  - "Plausibilisierung"
  - "Gegenvorstellung"
  - "Neubeurteilung"

must_flag:
  - "Angriff auf die Bewertung als solche"
  - "Antrag auf eine bestimmte Note"
  - "Beurteilungsrichtlinie nicht beschafft"
  - "Pauschales Bestreiten"
  - "Quotierung ungeprüft hingenommen"
---

# Test — dienstliche-beurteilung

Struktureller Smoke-Test. Schritt 1 muss die Bestimmung des anwendbaren Rechts sein. Die vier Kategorien der eingeschränkten gerichtlichen Kontrolle müssen einzeln benannt sein. Die Plausibilisierungspflicht muss als Folge substantiierten Bestreitens erscheinen. Der Rechtsschutz muss auf Neubeurteilung gerichtet sein, nicht auf eine Note, und der parallele Eilantrag nach § 123 VwGO muss erwähnt werden. Eine Formulierungshilfe für die Gegenvorstellung ist Pflicht.

Run: `python ../../../scripts/eval.py --skill beamten-disziplinarrecht/skills/dienstliche-beurteilung`
