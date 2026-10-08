---
skill: migrationsrecht/abschiebungsschutz
fact_pattern: |
  BAMF-Bescheid (Asylantrag als offensichtlich unbegründet abgelehnt
  § 30 AsylG, Abschiebungsandrohung § 34 AsylG in den Iran) wurde
  gestern zugestellt. Mandant leidet ausweislich qualifizierter
  ärztlicher Bescheinigung an schwerer koronarer Herzerkrankung mit
  Reanimationsbedürftigkeit. Bitte Eilantrag § 80 V VwGO iVm § 36 III
  AsylG entwerfen und § 60 VII AufenthG-Argumentation aufbereiten.

must_cite:
  - "§ 80 VwGO"
  - "§ 36 III AsylG"
  - "§ 60 AufenthG"
  - "§ 60a AufenthG"
  - "§ 74 AsylG"
  - "Art. 3 EMRK"

must_appear:
  - "1 Woche"
  - "qualifizierte ärztliche Bescheinigung"
  - "Ernstliche Zweifel"
  - "Abschiebungsverbot"
  - "Reisefähigkeit"
  - "Frist"

must_flag:
  - "§ 36 III AsylG"
  - "1 Woche"
  - "§ 60a IIc"
  - "Dublin-Überstellungsfrist"
---

# Test — abschiebungsschutz

Struktureller Smoke-Test. Frist **1 Woche § 36 III AsylG** muss prominent erscheinen; qualifizierte ärztliche Bescheinigung § 60a IIc als Voraussetzung für § 60 VII-Argumentation muss adressiert sein; Antragsart (§ 80 V VwGO vs. § 123 VwGO) korrekt gewählt.

Run: `python ../../../scripts/eval.py --skill migrationsrecht/skills/abschiebungsschutz`
