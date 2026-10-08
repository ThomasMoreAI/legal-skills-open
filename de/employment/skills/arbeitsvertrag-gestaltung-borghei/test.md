---
skill: arbeitsrecht/arbeitsvertrag-gestaltung
fact_pattern: |
  Mandantin (Gebäudereinigungsunternehmen, 60 Beschäftigte) verwendet ein
  Vertragsmuster aus dem Jahr 2015. Es enthält eine einstufige Ausschlussfrist
  von zwei Monaten mit Schriftformerfordernis und ohne Ausnahme für den
  Mindestlohn, die Klausel "Sonderzahlungen erfolgen freiwillig und
  jederzeit widerruflich", eine Abgeltungsklausel "mit dem Gehalt sind alle
  Überstunden abgegolten" sowie eine salvatorische Klausel. Die Verträge
  werden neuerdings nur noch als PDF per E-Mail versandt; ein Empfangsnachweis
  wird nicht angefordert. Kündigungen sollen künftig ebenfalls per E-Mail
  erklärt werden.
must_cite:
  - "§ 307 Abs. 1 S. 2 BGB"
  - "§ 310 Abs. 4 S. 2 BGB"
  - "§ 309 Nr. 13 BGB"
  - "§ 3 MiLoG"
  - "§ 2 NachwG"
  - "§ 4 NachwG"
  - "§ 623 BGB"
  - "§ 126b BGB"
  - "§ 106 GewO"
must_appear:
  - "zweistufige"
  - "Ausschlussfrist"
  - "Widerrufsvorbehalt"
  - "Freiwilligkeitsvorbehalt"
  - "geltungserhaltenden Reduktion"
  - "Blue-Pencil-Test"
  - "Empfangsnachweis"
  - "Textform"
  - "Schriftform"
must_flag:
  - "Ausschlussfrist ohne Mindestlohnausnahme"
  - "Salvatorische Klausel als Sicherheitsnetz"
  - "Freiwilligkeits- und Widerrufsvorbehalt kombiniert"
  - "Pauschale Überstundenabgeltung"
  - "Textform des § 2 NachwG mit der Kündigungsform verwechselt"
  - "Empfangsnachweis nicht angefordert"
---

# Test — arbeitsvertrag-gestaltung

Prüft die AGB-Kontrolle der Standardklauseln, die Mindestlohn-Ausnahme in der
Ausschlussfrist und die Abgrenzung Textform (Nachweis) / Schriftform (§ 623 BGB).

Run: `python scripts/eval.py --skill arbeitsrecht/skills/arbeitsvertrag-gestaltung`
