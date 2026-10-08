---
skill: csrd/esrs-berichtspflicht
fact_pattern: |
  Familienunternehmen (Maschinenbau, nicht kapitalmarktorientiert, 1.100 EE
  in DE, 480 Mio. EUR Umsatz, GmbH & Co. KG) als Konzernmutter mit drei
  EU-Tochtergesellschaften. Bisher kein Nachhaltigkeitsbericht. Frage: ist
  das Unternehmen CSRD-pflichtig, ab welchem Geschäftsjahr und mit welchem
  Inhalt — und reicht ein Konzernbericht für die Töchter?
  Zusatz: Eine Schwestergesellschaft (1.100 EE, 320 Mio. EUR Umsatz) hat für
  das Geschäftsjahr 2024 bereits als Wave-1-Unternehmen berichtet. Muss sie
  für 2025 und 2026 weiter berichten?
must_cite:
  - "§ 289b HGB"
  - "§ 289c HGB"
  - "§ 315b HGB"
  - "RL (EU) 2022/2464"
  - "ESRS 1"
must_appear:
  - "Anwendungsbereich"
  - "Größenkriterien"
  - "Konzernebene"
  - "Lagebericht"
  - "limited assurance"
  - "ESRS"
  - "RL (EU) 2026/470"
  - "1.000 Beschäftigte"
  - "450 Mio. EUR"
  - "18.03.2026"
  - "19.03.2027"
  - "200 Mio. EUR"
must_flag:
  - "Omnibus"
  - "Schwellenprüfung"
  - "Konzernebene"
  - "Wave-1"
  - "kumulativ"
  - "[unverifiziert - prüfen]"
---

# Test — esrs-berichtspflicht

**Aktualitäts-Assertion (Stand 2026-07):** Der Skill muss den Anwendungsbereich nach der **Änderungs-RL (EU) 2026/470** (Amtsblatt 26.02.2026, in Kraft 18.03.2026) prüfen: **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz**, kumulativ. Die Wellen-Systematik (Wave 1/2/3) und die vom EP vorgeschlagene 1.750-Schwelle dürfen nicht als geltendes Recht dargestellt werden. Die Schwestergesellschaft im Sachverhalt (320 Mio. EUR) ist **nicht** berichtspflichtig und fällt für GJ 2025 und GJ 2026 aus dem Anwendungsbereich, obwohl sie für GJ 2024 berichtet hat. Umsetzungsfrist 19.03.2027; Drittstaaten-Schwellen 450 Mio. / 200 Mio. EUR.

Run: `cd "/Users/borghei/Projects/The Glass Room/ai-skills-german-law" && python3 scripts/eval.py --skill csrd/skills/esrs-berichtspflicht`
