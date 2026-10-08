---
skill: kritis-resilienz/kritis-resilienzpflichten
fact_pattern: |
  Ein Betreiber eines Umspannwerks und eines Trinkwasserwerks legt der
  zuständigen Behörde auf deren Nachweisverlangen vom 02.06.2026 ein
  ISO-27001-Zertifikat sowie eine Liste von 40 Sicherheitsmaßnahmen vor.
  Eine eigene Risikoanalyse existiert aus dem Jahr 2021 und behandelt
  ausschließlich Sabotage- und Cyberszenarien; Hochwasser, Ausfall des
  Vorlieferanten und Personalausfall sind nicht betrachtet. Ein
  beauftragtes Audit wurde im April 2026 abgeschlossen, das Ergebnis aber
  nicht an die Behörde übermittelt. Die Geschäftsführung hält den Einbau
  einer Perimetersicherung für zu teuer, hat das aber nirgends
  dokumentiert. Die Behörde droht eine Anordnung an.

must_cite:
  - "§ 4 KRITISDachG"
  - "§ 11 KRITISDachG"
  - "§ 12 KRITISDachG"
  - "§ 13 KRITISDachG"
  - "§ 14 KRITISDachG"
  - "§ 16 KRITISDachG"
  - "§ 17 KRITISDachG"
  - "§ 24 KRITISDachG"
  - "§ 28 VwVfG"

must_appear:
  - "All-Gefahren"
  - "physischer Schutz"
  - "Wiederherstellung"
  - "Stand der Technik"
  - "Zweck-Mittel-Relation"
  - "Gleichwertigkeit"
  - "Audit"
  - "500.000 EUR"
  - "legal_calc"

must_flag:
  - "Cyber-Zertifizierung als Resilienznachweis vorgelegt"
  - "Maßnahmen ohne Zuordnung zu den vier Zielen"
  - "Verhältnismäßigkeit behauptet statt gerechnet"
  - "Audit-Ergebnis nicht übermittelt"
  - "All-Gefahren-Ansatz auf Sabotage verengt"
---

# Test — kritis-resilienzpflichten

Struktureller Smoke-Test. Die Ausgabe muss das ISO-27001-Zertifikat an § 17 KRITISDachG messen und feststellen, dass es den physischen Schutz nach § 13 Abs. 1 Nr. 2 nicht abdeckt, die Risikoanalyse von 2021 als unvollständig im Sinne des All-Gefahren-Ansatzes und des § 12 iVm § 11 KRITISDachG beanstanden, die 40 Maßnahmen den vier Zielen des § 13 Abs. 1 zuordnen, die unterlassene Perimetersicherung über die Zweck-Mittel-Relation des § 13 Abs. 2 dokumentationspflichtig machen und die unterbliebene Übermittlung des Auditergebnisses § 16 Abs. 3 S. 3 iVm § 24 Abs. 1 Nr. 3 KRITISDachG mit bis zu 500.000 EUR zuordnen.

Run: `python ../../../scripts/eval.py --skill kritis-resilienz/skills/kritis-resilienzpflichten`
