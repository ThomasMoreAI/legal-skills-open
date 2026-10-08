---
skill: arbeitsrecht/urlaubsanspruch
fact_pattern: |
  Mandant war von 2019 bis zur Eigenkündigung zum 31.05.2026 in Vollzeit
  (5-Tage-Woche) beschäftigt; vertraglich waren 30 Urlaubstage vereinbart,
  ohne dass zwischen gesetzlichem Urlaub und Mehrurlaub unterschieden wurde.
  Der Arbeitgeber hat nie schriftlich zur Urlaubsnahme aufgefordert, sondern
  nur einmal jährlich einen Aushang im Pausenraum angebracht. Aus den Jahren
  2021 bis 2025 sind laut Zeiterfassung insgesamt 41 Urlaubstage offen. Von
  Februar 2024 bis Januar 2025 war der Mandant durchgehend arbeitsunfähig.
  Der Arbeitsvertrag enthält eine zweistufige Ausschlussfrist von je drei
  Monaten.
must_cite:
  - "§ 3 BUrlG"
  - "§ 7 BUrlG"
  - "§ 7 Abs. 3 BUrlG"
  - "§ 7 Abs. 4 BUrlG"
  - "§ 9 BUrlG"
  - "§ 11 BUrlG"
  - "§ 195 BGB"
  - "Richtlinie 2003/88/EG"
must_appear:
  - "Hinweis- und Aufforderungsobliegenheit"
  - "15-Monats-Frist"
  - "Abgeltung"
  - "Mehrurlaub"
  - "Verjährung"
  - "Umrechnung"
  - "Urlaubskonto"
must_flag:
  - "Automatischer Verfall zum 31.03. angenommen"
  - "Hinweis nur per Aushang oder Rundmail erteilt"
  - "Verjährung ab dem Urlaubsjahr gerechnet"
  - "Mehrurlaub nicht eigenständig geregelt"
  - "Ausschlussfristen beim Abgeltungsanspruch übersehen"
---

# Test — urlaubsanspruch

Prüft, ob der Skill den automatischen Verfall ausschließt, die Obliegenheiten
katalogisiert, die 15-Monats-Frist korrekt einschränkt und die Abgeltung
beziffert.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/urlaubsanspruch`
