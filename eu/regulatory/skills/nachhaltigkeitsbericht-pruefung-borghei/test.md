---
skill: csrd/nachhaltigkeitsbericht-pruefung
fact_pattern: |
  Kapitalmarktorientierte AG (2.400 EE, 900 Mio. EUR Nettoumsatz) erstellt
  erstmals einen ESRS-Nachhaltigkeitsbericht und muss diesen extern prüfen
  lassen. Eine Konzerntochter (1.050 EE, 380 Mio. EUR) hat für das
  Geschäftsjahr 2024 bereits berichten und prüfen lassen und fragt, ob der
  Prüfungsauftrag für 2025 verlängert werden muss. Der bisherige Abschlussprüfer
  soll auch die Nachhaltigkeitsprüfung übernehmen. Frage: wie sind Prüfer-
  bestellung, Prüfungsumfang und Sicherheitsniveau auszugestalten und wie
  hängt die Prüfung mit dem Lagebericht zusammen?
must_cite:
  - "§ 289b HGB"
  - "RL (EU) 2022/2464"
  - "ESRS 1"
  - "limited assurance"
  - "§ 324i HGB-E"
must_appear:
  - "Prüferbestellung"
  - "Prüfungsumfang"
  - "ESRS-Konformität"
  - "reasonable assurance"
  - "Lagebericht"
  - "Prüfungsvermerk"
  - "RL (EU) 2026/470"
  - "1.000 Beschäftigte"
  - "450 Mio. EUR"
  - "18.03.2026"
must_flag:
  - "limited assurance"
  - "ESRS-Konformität"
  - "Omnibus"
  - "Prüfungspflicht"
  - "Wave-1"
  - "[unverifiziert - prüfen]"
---

# Test — nachhaltigkeitsbericht-pruefung

**Aktualitäts-Assertion (Stand 2026-07):** Vor Prüferbestellung und Scoping muss der Skill die **Prüfungspflicht** nach der Änderungs-RL (EU) 2026/470 (in Kraft 18.03.2026) prüfen: **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz**, kumulativ. Die AG (2.400 EE / 900 Mio. EUR) ist pflichtig; die Konzerntochter (1.050 EE / 380 Mio. EUR) ist es **nicht** — sie fällt trotz Berichterstattung für GJ 2024 für **GJ 2025 und GJ 2026** aus dem Anwendungsbereich, der Prüfungsauftrag ist nicht zu verlängern. Das Sicherheitsniveau bleibt **limited assurance**.

Run: `cd "/Users/borghei/Projects/The Glass Room/ai-skills-german-law" && python3 scripts/eval.py --skill csrd/skills/nachhaltigkeitsbericht-pruefung`
