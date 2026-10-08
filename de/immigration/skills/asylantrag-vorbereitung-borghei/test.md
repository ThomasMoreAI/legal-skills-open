---
skill: migrationsrecht/asylantrag-vorbereitung
fact_pattern: |
  Mandant (Syrien, 28 J., aus Idlib) reiste über Griechenland und die
  Balkanroute am 15.03.2024 ein. Eurodac-Treffer Kat. 1 in Griechenland.
  Asylgesuch am 18.03.2024 beim BAMF. BAMF-Anhörung in drei Wochen.
  Bitte Dublin-Vorprüfung, Schutzformen-Triage und Anhörungsstruktur.

must_cite:
  - "§ 3 AsylG"
  - "§ 4 AsylG"
  - "§ 25 AsylG"
  - "§ 29 AsylG"
  - "§ 60 AufenthG"
  - "VO (EU) Nr. 604/2013"
  - "RL 2011/95/EU"

must_appear:
  - "Dublin"
  - "Flüchtlingseigenschaft"
  - "subsidiärer Schutz"
  - "Abschiebungsverbot"
  - "Überstellungsfrist"
  - "Sprachmittler"
  - "Selbsteintritt"

must_flag:
  - "Überstellungsfrist"
  - "qualifizierte ärztliche Bescheinigung"
  - "Folgeantrag"
  - "Suggestion"
---

# Test — asylantrag-vorbereitung

Struktureller Smoke-Test. Dublin-Prüfung **vor** materieller Schutz-Triage; Schutzformen-Reihenfolge § 3 → Art. 16a → § 4 → § 60 V/VII; Frist-Block (Anhörung, Überstellung, Klage) sichtbar; keine vorgefertigten Antworten zur Verfolgungsgeschichte.

Run: `python ../../../scripts/eval.py --skill migrationsrecht/skills/asylantrag-vorbereitung`
