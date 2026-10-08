---
skill: kritis-resilienz/kritis-governance-haftung
fact_pattern: |
  Eine kommunale Energie-GmbH betreibt registrierungspflichtige kritische
  Anlagen. Die Geschäftsführung besteht aus zwei Personen; nach der
  Geschäftsordnung ist ausschließlich der technische Geschäftsführer für
  Sicherheit zuständig, der kaufmännische hält sich für nicht befasst. Die
  Resilienzmaßnahmen wurden vollständig an einen externen Dienstleister
  vergeben; Berichte an die Geschäftsführung gibt es nicht. Eine
  Perimetersicherung wurde aus Kostengründen gestrichen, ohne dass dies
  protokolliert wurde. Die Behörde hat eine vollziehbare Anordnung nach
  § 16 Abs. 2 S. 1 erlassen, der nicht Folge geleistet wurde; zusätzlich
  wurde das Ergebnis eines Audits nicht übermittelt. Die Gesellschafterin
  prüft nun Regressansprüche, die Behörde ein Bußgeldverfahren.

must_cite:
  - "§ 4 KRITISDachG"
  - "§ 13 KRITISDachG"
  - "§ 16 KRITISDachG"
  - "§ 20 KRITISDachG"
  - "§ 24 KRITISDachG"
  - "§ 43 GmbHG"
  - "§ 130 OWiG"
  - "§ 30 OWiG"

must_appear:
  - "Überwachungspflicht"
  - "Organisationsmaßnahmen"
  - "Gesamtverantwortung"
  - "Innenhaftung"
  - "subsidiär"
  - "1.000.000 EUR"
  - "500.000 EUR"
  - "Zweck-Mittel-Relation"
  - "legal_calc"

must_flag:
  - "Delegation als Pflichterfüllung behandelt"
  - "Haftungsgrundlage falsch gewählt"
  - "Ressortverteilung als Enthaftung verstanden"
  - "Unterlassene Maßnahmen nicht protokolliert"
  - "Bußgeldrahmen pauschal"
---

# Test — kritis-governance-haftung

Struktureller Smoke-Test. Die Ausgabe muss die vollständige Auslagerung an den Dienstleister an § 20 Abs. 1 KRITISDachG messen und die verbleibende Überwachungspflicht benennen, die Ressortverteilung über den Grundsatz der Gesamtverantwortung relativieren, die Innenhaftung vorrangig auf § 43 GmbHG und nur subsidiär auf § 20 Abs. 2 KRITISDachG stützen, die gestrichene Perimetersicherung als fehlende Dokumentation der Zweck-Mittel-Relation nach § 13 Abs. 2 einordnen und die beiden Bußgeldtatbestände tatbestandsgenau zuordnen: Zuwiderhandlung gegen die vollziehbare Anordnung nach § 24 Abs. 1 Nr. 2 lit. b und die unterbliebene Audit-Übermittlung nach Nr. 3 mit bis zu 500.000 EUR. §§ 130 und 30 OWiG sind zu adressieren.

Run: `python ../../../scripts/eval.py --skill kritis-resilienz/skills/kritis-governance-haftung`
