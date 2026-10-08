---
skill: csrd/eu-taxonomie
fact_pattern: |
  Energieversorger (3.100 EE, 1,2 Mrd. EUR Nettoumsatz) betreibt Windparks, ein Gaskraftwerk und
  ein Stromnetz. Die Investitionsplanung sieht hohe CapEx für Netzausbau und
  Batteriespeicher vor. Frage: welche Tätigkeiten sind taxonomiefähig bzw.
  -konform, und wie werden Umsatz-, CapEx- und OpEx-KPI nach Art. 8
  offengelegt? Eine Netzgesellschaft im Konzern (1.150 EE, 410 Mio. EUR)
  hat für GJ 2024 offengelegt — besteht die Pflicht für 2025 fort?
must_cite:
  - "Taxonomie-VO (EU) 2020/852"
  - "Art. 3 Taxonomie-VO"
  - "Art. 8 Taxonomie-VO"
  - "Art. 9 Taxonomie-VO"
  - "Do no significant harm"
must_appear:
  - "Taxonomiefähigkeit"
  - "Taxonomiekonformität"
  - "Umsatz"
  - "CapEx"
  - "OpEx"
  - "Mindestschutz"
  - "RL (EU) 2026/470"
  - "1.000 Beschäftigte"
  - "450 Mio. EUR"
  - "18.03.2026"
must_flag:
  - "Do no significant harm"
  - "Taxonomiekonformität"
  - "CapEx"
  - "Offenlegungspflicht"
  - "Wave-1"
  - "[unverifiziert - prüfen]"
---

# Test — eu-taxonomie

**Aktualitäts-Assertion (Stand 2026-07):** Der Offenlegungskreis nach Art. 8 Taxonomie-VO folgt dem CSRD-Anwendungsbereich, der durch die Änderungs-RL (EU) 2026/470 (in Kraft 18.03.2026) auf **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz** verengt wurde. Der Energieversorger (3.100 EE / 1,2 Mrd. EUR) ist erfasst; die Netzgesellschaft (1.150 EE / 410 Mio. EUR) ist es **nicht** — trotz Offenlegung für GJ 2024 entfällt die Pflicht für GJ 2025 und GJ 2026. Diese Vorfrage ist dem Tätigkeits-Mapping vorzuschalten.

Run: `cd "/Users/borghei/Projects/The Glass Room/ai-skills-german-law" && python3 scripts/eval.py --skill csrd/skills/eu-taxonomie`
