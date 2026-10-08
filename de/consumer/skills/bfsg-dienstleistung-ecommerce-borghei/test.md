---
skill: barrierefreiheit-bfsg/bfsg-dienstleistung-ecommerce
fact_pattern: |
  Mandantin betreibt einen Online-Shop für Haushaltselektronik mit rund
  120 Beschäftigten und bietet ausschließlich Verbrauchern an. Ein
  Prüfbericht vom Januar 2026 weist aus: Bezahlseite ohne
  Tastaturbedienbarkeit, Captcha ohne Alternative, Kontrastwerte
  unterhalb der Norm, keine Textalternativen für Produktbilder. In der
  Fußzeile steht der Satz "Wir bemühen uns um Barrierefreiheit nach WCAG
  2.1 AA". Eine Beurteilung nach § 16 oder § 17 BFSG wurde nie
  vorgenommen; die Geschäftsführung hält die Nachrüstung der Bezahlseite
  für unverhältnismäßig teuer. Ein nach § 15 Abs. 3 BGG anerkannter
  Verband hat bei der Landesbehörde die Einleitung eines Verfahrens
  beantragt und zugleich einen Schlichtungsantrag gestellt. Ein
  Wettbewerber droht mit einer Abmahnung.

must_cite:
  - "§ 14 BFSG"
  - "§ 16 BFSG"
  - "§ 17 BFSG"
  - "§ 32 BFSG"
  - "§ 33 BFSG"
  - "§ 34 BFSG"
  - "§ 37 BFSG"
  - "§ 12 BFSGV"
  - "§ 19 BFSGV"
  - "§ 3a UWG"
  - "§ 16 BGG"

must_appear:
  - "Anlage 3"
  - "Anlage 4"
  - "Marktüberwachungsbehörde"
  - "wahrnehmbar, bedienbar, verständlich und robust"
  - "barrierefreier Form"
  - "fünf Jahre"
  - "Schlichtung"
  - "ausgesetzt"
  - "100.000 EUR"
  - "legal_calc"

must_flag:
  - "Angabe der Marktüberwachungsbehörde fehlt"
  - "Pauschale WCAG-Aussage"
  - "Ausnahme behauptet ohne Beurteilung"
  - "Verbandsantrag als unzulässig behandelt"
  - "Schlichtungsantrag ignoriert"
  - "UWG-Abmahnfähigkeit als geklärt dargestellt"
---

# Test — bfsg-dienstleistung-ecommerce

Struktureller Smoke-Test. Die Ausgabe muss den Shop § 1 Abs. 3 Nr. 5 BFSG und den Anforderungen der §§ 12, 19 BFSGV zuordnen, den Fußzeilensatz als unzureichende Information nach Anlage 3 Nr. 1 verwerfen (insbesondere fehlende Angabe der Marktüberwachungsbehörde), die Berufung auf Unverhältnismäßigkeit mangels Beurteilung nach § 17 BFSG und Anlage 4 zurückweisen, den Verbandsantrag über § 32 Abs. 2 BFSG als zulässig behandeln, die Aussetzung nach § 34 Abs. 4 BFSG anordnen und die UWG-Frage ausdrücklich als ungeklärt kennzeichnen. Ein Maßnahmenplan mit Fristen ist auszuwerfen.

Run: `python ../../../scripts/eval.py --skill barrierefreiheit-bfsg/skills/bfsg-dienstleistung-ecommerce`
