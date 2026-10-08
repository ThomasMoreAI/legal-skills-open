---
skill: wettbewerbsrecht/uwg-abmahnung-pruefung
fact_pattern: |
  Mandantin (Online-Händlerin Haushaltswaren, Kleinunternehmerin
  iSv § 19 UStG) hat von einem Wirtschaftsverband (e. V.) eine
  Abmahnung wegen fehlender Grundpreisangaben auf der Webseite
  erhalten. Gefordert: Unterlassungserklärung mit Vertragsstrafe
  5.100 EUR pro Verstoß und Aufwendungsersatz 295 EUR. Im
  Abmahnschreiben kein Hinweis auf die Eintragung in die Liste
  qualifizierter Wirtschaftsverbände (§ 8b UWG). Frist 7 Tage.

must_cite:
  - "§ 8 UWG"
  - "§ 8b UWG"
  - "§ 8c UWG"
  - "§ 11 UWG"
  - "§ 13 UWG"
  - "§ 13a UWG"

must_appear:
  - "Aktivlegitimation"
  - "Rechtsmissbrauch"
  - "Unterlassungserklärung"
  - "Vertragsstrafe"
  - "Aufwendungsersatz"
  - "Verjährung"
  - "Schwarze Liste"

must_flag:
  - "BAJ-Eintragung"
  - "modifizierte UE"
  - "Kerntheorie"
  - "Wiederholungsgefahr"
---

# Test — uwg-abmahnung-pruefung

Struktureller Smoke-Test. Erwartete Prüfschritte (Aktivlegitimation §§ 8, 8b → formelle § 13 II → materieller Verstoß → § 8c-Missbrauch → Reaktionsoptionen) müssen alle im Output erscheinen.

Run: `python ../../../scripts/eval.py --skill wettbewerbsrecht/skills/uwg-abmahnung-pruefung`
