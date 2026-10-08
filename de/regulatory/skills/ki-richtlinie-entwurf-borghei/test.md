---
skill: ki-governance/ki-richtlinie-entwurf
fact_pattern: |
  Sozietät mit 35 Berufsträgern (Partnerschaft mbB) will eine
  verbindliche interne KI-Richtlinie einführen. Aktuell nutzen
  Mitarbeitende uneinheitlich ChatGPT Free, Copilot und einen
  spezialisierten Vertragsanalyse-Anbieter. Es gibt kein KI-Inventar,
  keinen Genehmigungsprozess und keinen einheitlichen Schulungsstand.
  Bitte Entwurf der Richtlinie inklusive Rollen, Lieferanten-
  management nach § 43e BRAO, Schulungskonzept nach Art. 4 KI-VO
  und Vorfallsmanagement.

must_cite:
  - "Art. 4 KI-VO"
  - "Art. 5 KI-VO"
  - "Art. 28 DSGVO"
  - "Art. 32 DSGVO"
  - "§ 43e BRAO"
  - "§ 203 StGB"
  - "§ 87 BetrVG"
  - "ISO/IEC 42001"

must_appear:
  - "Geltungsbereich"
  - "Grundsätze"
  - "Genehmigungsprozess"
  - "Rollen"
  - "Lieferantenmanagement"
  - "Schulung"
  - "Vorfallsmanagement"
  - "Wiedervorlage"
  - "AVV"
  - "ki-vo-compliance"

must_flag:
  - "KI-VO-Pflichten in die Richtlinie kopieren"
  - "Schulung Art. 4 KI-VO"
  - "§ 87"
  - "mitwirkende Personen"

must_not_appear:
  - "[generiert]"
---

# Test — ki-richtlinie-entwurf

Struktureller Smoke-Test. Richtlinien-Entwurf muss elf Paragraphen plus Anlagen abdecken, KI-VO-Pflichten querverweisen statt zu doppeln, AVV nach Art. 28 DSGVO und § 43e BRAO bei der Lieferantenklausel ansprechen, Schulungspflicht Art. 4 KI-VO als verbindlichen § 8 ausgestalten und Mitbestimmung § 87 I Nr. 6 BetrVG nicht übersehen.

Run: `python ../../../scripts/eval.py --skill ki-governance/skills/ki-richtlinie-entwurf`
