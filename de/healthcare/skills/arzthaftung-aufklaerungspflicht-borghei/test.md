---
skill: medizinrecht/arzthaftung-aufklaerungspflicht
fact_pattern: |
  Patientin (62 J.) unterzieht sich elektiver Bandscheiben-OP an der
  LWS. Aufklärungsgespräch erfolgte am Vorabend ca. 21:30 Uhr durch
  Stationsärztin (1. Weiterbildungsjahr Anästhesie, nicht Neurochirurgie).
  Standard-Aufklärungsbogen unterschrieben, Gespräch ca. fünf Minuten.
  Operation lege artis. Postoperativ Cauda-equina-Syndrom mit
  bleibender Blasen- und Mastdarmlähmung. Patientin macht geltend, sie
  sei nicht über das Cauda-Risiko und nicht über konservative
  Behandlungsalternativen aufgeklärt worden. Klinik beruft sich auf
  hypothetische Einwilligung.

must_cite:
  - "§ 630a BGB"
  - "§ 630e BGB"
  - "§ 630d BGB"
  - "§ 630h BGB"
  - "§ 823 BGB"
  - "§ 253 BGB"
  - "§ 223 StGB"
  - "§ 199 BGB"

must_appear:
  - "Selbstbestimmungsaufklärung"
  - "Sicherungsaufklärung"
  - "Bedenkzeit"
  - "Behandlungsalternativen"
  - "Beweislast"
  - "hypothetische Einwilligung"
  - "Entscheidungskonflikt"
  - "30 Jahre"
  - "§ 199 II BGB"

must_flag:
  - "Aufklärung durch nicht qualifiziertes Personal"
  - "Sachverständigenbedarf"
  - "Hypothetische Einwilligung"
---

# Test — arzthaftung-aufklaerungspflicht

Struktureller Smoke-Test. Erwartet wird ausdrückliche Prüfung aller fünf Absätze § 630h BGB (jedenfalls negativ), Behandlung der Bedenkzeit-Frage, Einordnung der hypothetischen Einwilligung als restriktive Verteidigungslinie und Hinweis auf § 199 II BGB.

Run: `python ../../../scripts/eval.py --skill medizinrecht/skills/arzthaftung-aufklaerungspflicht`
