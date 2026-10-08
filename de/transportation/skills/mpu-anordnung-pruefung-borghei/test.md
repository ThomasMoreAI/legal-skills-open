---
skill: verkehrsrecht/mpu-anordnung-pruefung
fact_pattern: |
  Mandant (47) wurde mit BAK 1,7 ‰ am Steuer angehalten. Strafgerichtlich
  Entziehung der Fahrerlaubnis nach § 69 StGB, Sperrfrist § 69a StGB
  abgelaufen. Wiedererteilungsantrag gestellt. Die Fahrerlaubnisbehörde
  ordnet MPU nach § 13 S. 1 Nr. 2 lit. c FeV an. Anordnung enthält
  Fragestellung "Klärung der Fahreignung" ohne weitere Konkretisierung.
  Frist zur Beibringung 2 Monate. Hinweis nach § 11 VIII S. 2 FeV
  fehlt. Bitte Rechtmäßigkeit prüfen und Widerspruchsbegründung
  entwerfen.

must_cite:
  - "§ 13 FeV"
  - "§ 11 FeV"
  - "§ 28 VwVfG"
  - "§ 37 VwVfG"
  - "§ 74 VwGO"
  - "§ 80 VwGO"

must_appear:
  - "Bestimmtheit"
  - "Anhörung"
  - "Hinweis"
  - "Nichteignung"
  - "Sofortvollzug"
  - "Klagefrist"

must_flag:
  - "Beibringungs-Frist verstreichen lassen"
  - "Hinweis § 11 VIII S. 2 FeV"
  - "nicht selbstständig anfechtbar"
---

# Test — mpu-anordnung-pruefung

Struktureller Smoke-Test. Erwartet werden Trigger-Subsumtion § 13 S. 1 Nr. 2 lit. c FeV, formelle Prüfung (Bestimmtheit, Hinweispflicht), Fristenkalender (§ 74 VwGO).

Run: `python ../../../scripts/eval.py --skill verkehrsrecht/skills/mpu-anordnung-pruefung`
