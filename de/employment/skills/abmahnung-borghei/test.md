---
skill: arbeitsrecht/abmahnung
fact_pattern: |
  AN (Sachbearbeiter Buchhaltung) war an drei aufeinanderfolgenden
  Arbeitstagen ohne Krankmeldung nicht erschienen. Erste Abmahnung. AG
  möchte eine BAG-konforme Abmahnung aussprechen mit dem Ziel, bei
  Wiederholung verhaltensbedingt kündigen zu können.

must_cite:
  - "§ 1 KSchG"
  - "§ 626 BGB"
  - "§ 83 BetrVG"
  - "§ 314 Abs. 2 BGB"

must_appear:
  - "Rüge"
  - "Hinweis"
  - "Warnung"
  - "Verhältnismäßigkeit"
  - "Personalakte"
  - "Sanktionsandrohung"

must_flag:
  - "Wertung statt Tatsache"
  - "Sanktionsandrohung"
  - "Tilgungsfrist"
---

# Test — abmahnung

Struktureller Smoke-Test. Erwartete drei Funktionen (Rüge / Hinweis / Warnung) müssen alle im Output erscheinen.

Run: `python ../../../scripts/eval.py --skill arbeitsrecht/skills/abmahnung`
