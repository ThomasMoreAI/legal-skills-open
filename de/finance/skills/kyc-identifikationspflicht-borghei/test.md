---
skill: geldwaesche-aml-kyc/kyc-identifikationspflicht
fact_pattern: |
  Neukunde einer deutschen Privatbank ist die A-GmbH. Anteilseigner
  ist eine luxemburgische SARL mit 100 %; deren Anteile werden zu
  60 % von einer zypriotischen Holding und zu 40 % von einer
  natürlichen Person Y gehalten. Die zypriotische Holding wird ihrer-
  seits über einen Trust auf Jersey gehalten, wirtschaftlich
  Begünstigter laut Trust Deed ist eine natürliche Person X. Es
  wird ein Investmentkonto mit Anlagevolumen 5 Mio. EUR eröffnet.
  Bitte KYC-Memo mit Identifizierung, wirtschaftlich Berechtigtem,
  Transparenzregister-Abgleich und Pflichtenniveau erstellen.

must_cite:
  - "§ 3 GwG"
  - "§ 10 GwG"
  - "§ 11 GwG"
  - "§ 12 GwG"
  - "§ 15 GwG"
  - "§ 8 GwG"

must_appear:
  - "wirtschaftlich Berechtigt"
  - "Transparenzregister"
  - "25 %"
  - "verstärkte Sorgfalt"
  - "PEP"
  - "Identifizierung"
  - "Aufbewahrung"
  - "fiktiv"
  - "AMLR"
  - "AMLA"
  - "10.07.2027"
  - "10.07.2026"
  - "01.07.2025"
  - "Gap-Mapping"

must_flag:
  - "fiktiver WB"
  - "Transparenzregister-Abgleich"
  - "komplexe Struktur"
  - "AMLR vorzeitig als geltendes Recht angewandt"
  - "10.000 EUR"
---

# Test — kyc-identifikationspflicht

Struktureller Smoke-Test. Trigger der Identifizierungspflicht, WB-Kette über mehrstufige Auslandsstruktur und Transparenzregister-Abgleich müssen sämtlich behandelt werden; bei Jersey-Trust ist verstärkte Sorgfalt nach § 15 III Nr. 3 GwG zu adressieren.

**Aktualitäts-Assertions (Stand 2026-07).** Das **GwG bleibt bis 10.07.2027 der operative Prüfungsmaßstab** — die frühere pauschale AMLR-Notiz `[unverifiziert – Anwendungsbeginn 2027]` ist durch datierte Angaben ersetzt: **AMLA seit 01.07.2025 in Frankfurt operativ**, **AMLD6 Art. 11–13, 15 Umsetzungsfrist 10.07.2026**, **AMLR anwendbar ab 10.07.2027**, EU-weite Bargeldobergrenze **10.000 EUR** (nationale Untergrenzen möglich).

Die `must_flag`-Einträge sichern zwei Fehlannahmen ab, die der Skill ausdrücklich benennen muss: die **vorzeitige Anwendung der AMLR** als geltendes Recht und das Abstellen allein auf die EU-Bargeldgrenze ohne Prüfung des nationalen Rechts.

Run: `python ../../../scripts/eval.py --skill geldwaesche-aml-kyc/skills/kyc-identifikationspflicht`
