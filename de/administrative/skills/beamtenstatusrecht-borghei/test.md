---
skill: beamten-disziplinarrecht/beamtenstatusrecht
fact_pattern: |
  Mandantin ist Kommunalbeamtin (A 11) in Nordrhein-Westfalen. Sie
  wurde mit Schreiben vom 02.06.2026 ohne Anhörung von der
  Sachbearbeitung im Ordnungsamt auf einen Dienstposten im Archiv
  derselben Behörde verwiesen; das Schreiben trägt keine
  Rechtsbehelfsbelehrung. Zeitgleich ordnete der Dienstherr eine
  amtsärztliche Untersuchung an, ohne Anlass und Umfang zu benennen.
  Ferner wurde ihr Antrag auf Genehmigung einer nebenberuflichen
  Dozententätigkeit (vier Wochenstunden) ohne Begründung abgelehnt.
  Ein Sturz auf dem Weg zur Dienststelle im Januar 2026 wurde bislang
  nicht als Dienstunfall gemeldet.

must_cite:
  - "§ 11 BeamtStG"
  - "§ 12 BeamtStG"
  - "§ 14 BeamtStG"
  - "§ 15 BeamtStG"
  - "§ 26 BeamtStG"
  - "§ 36 BeamtStG"
  - "§ 40 BeamtStG"
  - "§ 45 BeamtStG"
  - "§ 45 BeamtVG"
  - "§ 74 VwGO"

must_appear:
  - "Anwendbares Recht"
  - "Umsetzung"
  - "Abordnung"
  - "Versetzung"
  - "kein Verwaltungsakt"
  - "Dienstunfähigkeit"
  - "Untersuchungsanordnung"
  - "anderweitiger Verwendung"
  - "Nebentätigkeit"
  - "Fürsorgepflicht"
  - "Remonstration"
  - "Beihilfe"

must_flag:
  - "Umsetzung als Verwaltungsakt behandelt"
  - "BeamtStG auf Bundesbeamte angewandt"
  - "Meldefrist § 45 BeamtVG versäumt"
  - "Suche nach anderweitiger Verwendung nicht gerügt"
  - "Remonstration nicht dokumentiert"
---

# Test — beamtenstatusrecht

Struktureller Smoke-Test. Schritt 1 muss die Bestimmung des anwendbaren Rechts sein und klarstellen, dass das BeamtStG nicht für Bundesbeamte gilt. Die Dreiteilung Umsetzung / Abordnung / Versetzung muss mit ihrer jeweiligen Rechtsnatur und dem zutreffenden Rechtsbehelf erscheinen. Bei der Zurruhesetzung müssen Untersuchungsanordnung, Gutachtenanforderungen und die Suche nach anderweitiger Verwendung geprüft werden. Die Remonstration muss dreistufig mit der Ausnahme für strafbare Weisungen dargestellt und als Formulierungshilfe hinterlegt sein.

Run: `python ../../../scripts/eval.py --skill beamten-disziplinarrecht/skills/beamtenstatusrecht`
