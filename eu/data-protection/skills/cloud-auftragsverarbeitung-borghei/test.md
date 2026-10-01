---
skill: it-recht/cloud-auftragsverarbeitung
fact_pattern: |
  Eine Personalabteilung (Verantwortlicher) führt Bewerbungs- und
  Beschäftigtendaten künftig in einem US-SaaS-HR-System. Der Anbieter ist nicht
  unter dem EU-US Data Privacy Framework zertifiziert; der Vertrag enthält keinen
  AVV-Anhang, nennt keine Sub-Auftragsverarbeiter und sieht keine Löschung nach
  Vertragsende vor. Verschlüsselung wird nur „best effort" zugesagt, ein
  Transfer Impact Assessment fehlt. Datenschutzkonforme Bewertung gewünscht.
must_cite:
  - "Art. 28 DSGVO"
  - "Art. 32 DSGVO"
  - "Art. 44 DSGVO"
  - "Art. 83 DSGVO"
must_appear:
  - "Auftragsverarbeitung"
  - "Sub-Auftragsverarbeiter"
  - "Drittlandtransfer"
  - "Audit"
  - "Löschung"
  - "Data Act"
  - "12.09.2025"
  - "12.01.2027"
  - "Wechselentgelte"
  - "Bundesnetzagentur"
must_flag:
  - "Fehlender AVV"
  - "Drittlandtransfer"
  - "Sub-Auftragsverarbeiter"
  - "Bußgeld"
  - "Cloud-Vertrag nur nach DSGVO geprüft"
  - "Falsche Aufsichtsbehörde adressiert"
---

# Test — cloud-auftragsverarbeitung

Struktureller Smoke-Test der drei DSGVO-Achsen (AVV Art. 28, TOM Art. 32, Drittlandtransfer Kapitel V).

**Aktualitäts-Assertions (Stand 2026-07).** Der Skill muss den seit **12.09.2025** anwendbaren **Data Act** (VO (EU) 2023/2854) als **vierte, DSGVO-unabhängige Prüfachse** führen — sie erfasst auch **nicht-personenbezogene** Daten. Gefordert sind insbesondere der vollständige Wegfall der **Wechselentgelte bis 12.01.2027** (bis dahin nur kostenbasiert reduziert), die vertragliche **Ausstiegsunterstützung nach Art. 25** und die Klauselkontrolle nach **Art. 13**.

Die **Bundesnetzagentur** ist nach dem **DADG** (BGBl. 29.05.2026, Bekanntgabe 30.05.2026) die zuständige Behörde — **nicht** die Datenschutzaufsicht. Die beiden `must_flag`-Einträge sichern genau diese zwei Fehler ab: die auf die DSGVO verengte Prüfung und die falsch adressierte Aufsichtsbehörde.
