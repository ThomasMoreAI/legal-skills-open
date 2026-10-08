---
skill: ki-governance/ki-risikoassessment
fact_pattern: |
  Mittelständische Wirtschaftskanzlei (40 Berufsträger) will einen
  LLM-gestützten Vertragsanalyse-Assistenten einführen. Anbieter ist
  ein US-amerikanischer Cloud-Provider (SaaS). Eingabe sind anonyme
  Mandantenverträge (M&A, NDA). Speicherung in EU-Region des Anbieters
  laut DPA, aber Sub-Processor in den USA bei Modellbetrieb. Bitte
  strukturiertes Risikoassessment nach ISO/IEC 23894 / NIST AI RMF
  inkl. KI-VO-Triggerprüfung und Berufsrechts-Bewertung.

must_cite:
  - "Art. 28 DSGVO"
  - "Art. 22 DSGVO"
  - "Art. 35 DSGVO"
  - "§ 43e BRAO"
  - "§ 203 StGB"
  - "ISO/IEC 23894"
  - "NIST AI RMF"
  - "Art. 6 KI-VO"
  - "Art. 4 KI-VO"

must_appear:
  - "Risikoklassifizierung"
  - "Risk-Treatment"
  - "Drittlandtransfer"
  - "Wiedervorlage"
  - "AVV"
  - "Schulung"
  - "ki-vo-compliance"

must_flag:
  - "KI-VO-Pflichten inhaltlich doppeln"
  - "AVV vergessen"
  - "§ 43e BRAO"
  - "Proxy-Variablen"

must_not_appear:
  - "[generiert]"
---

# Test — ki-risikoassessment

Struktureller Smoke-Test. Risikoassessment muss die KI-VO-Risikoklasse als Trigger benennen (mit Querverweis auf `ki-vo-compliance`, ohne dortige Pflichten zu doppeln), DSFA Art. 35 DSGVO auslösen, AVV Art. 28 DSGVO und Drittlandtransfer adressieren, Berufsrechts-Trigger (§ 43e BRAO, § 203 StGB) ziehen und konkrete Wiedervorlagefrist setzen.

Run: `python ../../../scripts/eval.py --skill ki-governance/skills/ki-risikoassessment`
