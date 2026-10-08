---
skill: transportrecht/lieferbedingungen-adsp
fact_pattern: |
  Spediteur S hat den B2B-Auftrag der Mandantin V (Maschinenbauunter-
  nehmen) per E-Mail bestätigt mit dem Hinweis "Es gelten die ADSp in
  ihrer jeweils gültigen Fassung". V hat den ADSp-Text nicht ausdrücklich
  erhalten und nicht widersprochen. Bei der Beförderung einer Maschine
  (Bruttogewicht 2.100 kg, Wert 45.000 EUR) ist ein Schaden in Höhe von
  45.000 EUR entstanden. S verlangt im Anschluss Bezahlung der offenen
  Frachtrechnungen und beruft sich auf das Aufrechnungsverbot Ziff. 27
  ADSp 2017. Bitte (a) Einbeziehung der ADSp, (b) Wirksamkeit der
  Haftungsbegrenzung Ziff. 23 und (c) Aufrechnungsverbot Ziff. 27 gegen
  die streitige Schadensersatzforderung prüfen.

must_cite:
  - "§ 305 BGB"
  - "§ 305b BGB"
  - "§ 307 BGB"
  - "§ 309 BGB"
  - "§ 310 BGB"
  - "§ 449 HGB"
  - "§ 453 HGB"
  - "ADSp"
  - "Ziff. 23"
  - "Ziff. 27"

must_appear:
  - "Einbeziehung"
  - "Inhaltskontrolle"
  - "B2B"
  - "8,33"
  - "SZR"
  - "Aufrechnungsverbot"
  - "Individualabrede"
  - "qualifiziertes Verschulden"

must_flag:
  - "Tageskurs"
  - "rechtskräftig festgestellt"
  - "§ 305 II BGB findet im B2B keine Anwendung"
---

# Test — lieferbedingungen-adsp

Struktureller Smoke-Test. Einbeziehungsmaßstab muss B2B-spezifisch (§ 449 II HGB, kein § 305 II BGB) hergeleitet sein. Inhaltskontrolle § 307 BGB für Ziff. 23 und Ziff. 27 ADSp ist mit § 309 Nr. 3 BGB-Indizwirkung zu prüfen. SZR-Berechnung methodisch mit Tageskurs-Hinweis. Vorrang Individualabrede (§ 305b BGB / Ziff. 2.2 ADSp) und Grenze qualifiziertes Verschulden (§ 435 HGB) explizit.

Run: `python ../../../scripts/eval.py --skill transportrecht/skills/lieferbedingungen-adsp`
