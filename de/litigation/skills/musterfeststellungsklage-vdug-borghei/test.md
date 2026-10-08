---
skill: verbandsklage-vdug/musterfeststellungsklage-vdug
fact_pattern: |
  Ein Verbraucherverband will gegen einen Kfz-Hersteller
  Musterfeststellungsklage erheben. Entwurf der Feststellungsziele: (1) die
  im Fahrzeugtyp X verbaute Abschalteinrichtung sei unzulässig, (2) der
  Hersteller habe sittenwidrig gehandelt, (3) den betroffenen Käufern stehe
  ein Schadensersatzanspruch in Höhe von mindestens 15 Prozent des
  Kaufpreises zu. Rund 8.000 Käufer sind betroffen; 300 haben bereits
  Individualklagen erhoben, die überwiegend vor der geplanten
  Registerbekanntgabe eingereicht wurden. Parallel ist zu denselben
  Vorgängen ein KapMuG-Musterverfahren gegen die Konzernmutter eröffnet.
  Der Hersteller fragt, ob ihn ein späteres Musterurteil in den
  Individualprozessen bindet und ob er die Klage abwehren kann.

must_cite:
  - "§ 1 VDuG"
  - "§ 4 VDuG"
  - "§ 8 VDuG"
  - "§ 11 VDuG"
  - "§ 18 VDuG"
  - "§ 41 VDuG"
  - "§ 42 VDuG"
  - "§ 46 VDuG"

must_appear:
  - "Feststellungsziele"
  - "Bindungswirkung"
  - "angemeldet"
  - "Aussetzung"
  - "Klageverbot"
  - "Abhilfeendurteile"
  - "Revision"
  - "KapMuG"
  - "legal_calc"

must_flag:
  - "Bindungswirkung auf Abhilfeendurteile erstreckt"
  - "Wirkungen des § 11 ohne Anmeldung angenommen"
  - "Feststellungsziele mit Individualmerkmalen befrachtet"
  - "Vorrang der Abhilfeklage unterstellt"
  - "Berufung eingelegt"
  - "KapMuG als Sperre behandelt"
---

# Test — musterfeststellungsklage-vdug

Struktureller Smoke-Test. Die Ausgabe muss Feststellungsziel (3) als individualitätsbehaftet und damit untauglich verwerfen, die Ziele (1) und (2) auf Bestimmtheit prüfen, die drei Wirkungen des § 11 VDuG getrennt darstellen — Aussetzung der vor Registerbekanntgabe erhobenen Individualklagen nur bei Anmeldung (Abs. 1), Klageverbot für Angemeldete (Abs. 2), Bindungswirkung nur für angemeldete Verbraucher (Abs. 3) mit der ausdrücklichen Ausnahme für Abhilfeendurteile nach § 18 — das parallele KapMuG-Verfahren über § 1 Abs. 3 VDuG als unschädlich einordnen und die Revision nach § 42 VDuG statt einer Berufung benennen.

Run: `python ../../../scripts/eval.py --skill verbandsklage-vdug/skills/musterfeststellungsklage-vdug`
