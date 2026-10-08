---
skill: arbeitsrecht/kuendigungsschutzklage
fact_pattern: |
  Mandant (Lagerleiter, 9 Jahre Betriebszugehörigkeit, Betrieb mit 80 AN,
  Betriebsrat vorhanden) erhält am Donnerstag, 15.01.2026, eine ordentliche
  betriebsbedingte Kündigung zum 30.04.2026, eingeworfen in den Hausbriefkasten
  gegen 16:30 Uhr. Der Betriebsrat hat der Kündigung schriftlich innerhalb
  einer Woche widersprochen. Der Mandant war vom 16.01. bis 30.01.2026 im
  Auslandsurlaub und meldet sich erst am 02.02.2026. Er möchte primär eine
  Abfindung, notfalls die Weiterbeschäftigung. Arbeitsgericht am Sitz in Bayern.
must_cite:
  - "§ 4 KSchG"
  - "§ 5 KSchG"
  - "§ 6 KSchG"
  - "§ 7 KSchG"
  - "§ 54 ArbGG"
  - "§ 12a ArbGG"
  - "§ 102 Abs. 5 BetrVG"
  - "§ 9 KSchG"
  - "§ 187 Abs. 1 BGB"
must_appear:
  - "Fristbeginn"
  - "Zugang"
  - "allgemeine Feststellungsantrag"
  - "Weiterbeschäftigungsantrag"
  - "Güteverhandlung"
  - "Auflösungsantrag"
  - "Vierteljahresverdienst"
  - "Deterministische Berechnung"
must_flag:
  - "Fristbeginn falsch angesetzt"
  - "Präklusion nach § 7 KSchG unterschätzt"
  - "Weiterbeschäftigungsantrag ohne Grundlage"
  - "§ 12a ArbGG nicht erklärt"
---

# Test — kuendigungsschutzklage

Fristen-Smoke-Test. Der Skill muss den Zugang als Fristauslöser benennen, die
3-Wochen-Frist deterministisch berechnen lassen und die Präklusionsfolge des
§ 7 KSchG ausweisen.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/kuendigungsschutzklage`
