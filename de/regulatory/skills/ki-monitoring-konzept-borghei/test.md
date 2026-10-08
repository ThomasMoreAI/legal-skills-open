---
skill: ki-governance/ki-monitoring-konzept
fact_pattern: |
  Versicherer betreibt ein internes Scoring-Modell zur Tarifkalkulation
  in der Kfz-Sparte. Hochrisiko-Indiz nach Anhang III Nr. 5 lit. a KI-VO
  („Zugang zu wesentlichen privaten Diensten"). Modell wurde vor sechs
  Monaten in Produktion gebracht. Bisher kein dokumentiertes Monitoring,
  Drift wird nicht systematisch gemessen, Override-Quote der Sachbear-
  beiter nicht erfasst. Bitte Monitoring-Konzept mit konkreten KPIs,
  Schwellenwerten und Eskalationswegen.

must_cite:
  - "Art. 12 KI-VO"
  - "Art. 14 KI-VO"
  - "Art. 22 DSGVO"
  - "Art. 32 DSGVO"
  - "ISO/IEC 42001"
  - "NIST AI RMF"

must_appear:
  - "Datendrift"
  - "Concept Drift"
  - "Fairness"
  - "Schwellenwert"
  - "Eskalation"
  - "human-in-the-loop"
  - "Wiedervorlage"
  - "Audit"
  - "ki-vo-compliance"

must_flag:
  - "Drift-Check fehlt"
  - "Override"
  - "Automation Bias"
  - "Schwellenwerte"

must_not_appear:
  - "[generiert]"
---

# Test — ki-monitoring-konzept

Struktureller Smoke-Test. Monitoring-Konzept muss Drift-Metriken (PSI/KS), Fairness-Metriken nach Schutzkategorien, Eskalationsstufen mit Schwellenwerten, Logging-Konformität (Art. 12 KI-VO als Bezug) und human-in-the-loop (Art. 14 KI-VO, Art. 22 DSGVO) adressieren – ohne KI-VO-Pflichten zu doppeln (Querverweis auf `ki-vo-compliance`).

Run: `python ../../../scripts/eval.py --skill ki-governance/skills/ki-monitoring-konzept`
