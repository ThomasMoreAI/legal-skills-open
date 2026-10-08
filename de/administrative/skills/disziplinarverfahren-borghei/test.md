---
skill: beamten-disziplinarrecht/disziplinarverfahren
fact_pattern: |
  Mandant ist Beamter auf Lebenszeit im Dienst einer Bundesoberbehörde
  (Besoldungsgruppe A 11). Ihm wird vorgeworfen, zwischen März und
  Oktober 2024 wiederholt dienstliche Personendatenbanken ohne
  dienstlichen Anlass abgefragt und Ergebnisse an einen privaten
  Dritten weitergegeben zu haben. Das Disziplinarverfahren wurde am
  15.01.2026 eingeleitet; die Unterrichtung erfolgte am 22.01.2026
  ohne Hinweis auf das Recht, einen Beistand hinzuzuziehen. Parallel
  ermittelt die Staatsanwaltschaft; öffentliche Klage ist noch nicht
  erhoben. Der Mandant ist seit 19 Jahren beanstandungsfrei im Dienst.

must_cite:
  - "§ 47 BeamtStG"
  - "§ 77 BBG"
  - "§ 5 BDG"
  - "§ 13 BDG"
  - "§ 15 BDG"
  - "§ 17 BDG"
  - "§ 20 BDG"
  - "§ 22 BDG"
  - "§ 23 BDG"
  - "§ 33 BDG"
  - "§ 34 BDG"
  - "§ 52 BDG"

must_appear:
  - "Anwendbares Recht"
  - "Landesdisziplinargesetz"
  - "Disziplinarverfügung"
  - "Entfernung aus dem Beamtenverhältnis"
  - "Zurückstufung"
  - "Kürzung der Dienstbezüge"
  - "Persönlichkeitsbild"
  - "Milderungsgründe"
  - "abschließende Anhörung"
  - "Stellungnahme nach § 20 BDG"
  - "legal_calc"

must_flag:
  - "Bundes- und Landesrecht vermengt"
  - "§ 15 BDG nicht gerechnet"
  - "Bindungswirkung überdehnt"
  - "Generalklausel statt Pflichtnorm"
  - "Aktenzeichen erfunden"
---

# Test — disziplinarverfahren

Struktureller Smoke-Test. Schritt 1 muss die Bestimmung des anwendbaren Rechts (Bund vs. Land) sein und beide Regime nebeneinander nennen. Die Maßnahmenleiter des § 5 BDG muss vollständig erscheinen, die Bemessungssystematik des § 13 BDG mit Schwere, Persönlichkeitsbild und Vertrauensbeeinträchtigung. Die Fristentabelle des § 15 BDG muss zeigen, dass für die Entfernung kein Maßnahmeverbot besteht. Die Bindungswirkung nach § 23 BDG muss auf rechtskräftige Urteile begrenzt werden. Der Rechner muss für die Fristen des § 15 BDG verdrahtet sein.

Run: `python ../../../scripts/eval.py --skill beamten-disziplinarrecht/skills/disziplinarverfahren`
