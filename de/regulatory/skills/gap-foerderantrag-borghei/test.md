---
skill: agrarrecht/gap-foerderantrag
fact_pattern: |
  Mandant (Ackerbaubetrieb 180 ha, Brandenburg) hat den Sammelantrag
  2025 fristgerecht über das InVeKoS-Portal gestellt. Die Landes-
  behörde hat die Basisprämie um 5 % gekürzt wegen behaupteten Ver-
  stoßes gegen GLÖZ 8 (Mindestanteil nichtproduktive Flächen).
  Mandant hat ausweislich eingereichter Flurstücksliste 4,2 %
  nichtproduktive Flächen ausgewiesen. Bewilligungsbescheid ist vor
  drei Wochen zugegangen. Bitte Widerspruchsbegründung entwerfen
  und Sanktionsbemessung prüfen.

must_cite:
  - "VO (EU) 2021/2115"
  - "VO (EU) 2021/2116"
  - "GAP-KondV"
  - "GAP-DZG"
  - "§ 70 VwGO"
  - "Art. 59 VO (EU) 2021/2116"

must_appear:
  - "Konditionalität"
  - "GLÖZ"
  - "nichtproduktive Flächen"
  - "Verhältnismäßigkeit"
  - "Sanktionsbemessung"
  - "Anwendungsvorrang"
  - "[unverifiziert – aktueller Stand prüfen]"

must_flag:
  - "Verspäteter Sammelantrag"
  - "Doppelförderung"
  - "Vertrauensschutz"
  - "aufschiebende Wirkung"
---

# Test — gap-foerderantrag

Struktureller Smoke-Test. Konditionalitäts-Subsumtion (GLÖZ 8), Verhältnismäßigkeit der Sanktion (Art. 59 VO (EU) 2021/2116) und Widerspruchsfrist § 70 VwGO müssen alle adressiert sein. Konkrete EUR/ha-Beträge und Prozentwerte sind mit `[unverifiziert – aktueller Stand prüfen]` zu markieren.

Run: `python ../../../scripts/eval.py --skill agrarrecht/skills/gap-foerderantrag`
