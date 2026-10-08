---
skill: vergaberecht/ausschreibungspruefung
fact_pattern: |
  Mandantin (IT-Dienstleister, GmbH) möchte sich auf eine
  EU-weite Ausschreibung einer Landesbehörde bewerben (offenes
  Verfahren, Auftragswert 800.000 EUR netto, Vertragslaufzeit
  vier Jahre). Die Vergabeunterlagen nennen vier Zuschlags-
  kriterien (Preis, Qualität, Konzept, Termin), jedoch ohne
  Gewichtung. Als Eignungsanforderung wird ein Mindestumsatz
  von 5 Mio. EUR pro Jahr in den letzten drei Jahren verlangt.
  Lose sind nicht vorgesehen. Angebotsfrist läuft in 18 Tagen.
  Bitte Vergabeunterlagen auf Vergaberechtskonformität prüfen
  und priorisierte Rügeliste mit Fristberechnung erstellen.

must_cite:
  - "§ 97 GWB"
  - "§ 122 GWB"
  - "§ 127 GWB"
  - "§ 31 VgV"
  - "§ 160 Abs. 3 S. 1"

must_appear:
  - "Eignung"
  - "Zuschlagskriterien"
  - "Gewichtung"
  - "Losaufteilung"
  - "Verhältnismäßigkeit"
  - "Rügeliste"
  - "Angebotsfrist"
  - "Bundestariftreuegesetz"
  - "50.000 EUR netto"
  - "Tariftreueerklärung"
  - "Vergabebeschleunigungsgesetz"
  - "01.07.2026"

must_flag:
  - "keine Gewichtung"
  - "Eignungsanforderungen unverhältnismäßig"
  - "Losaufteilung ohne ordnungsgemäße Begründung"
  - "Rügefrist"
  - "Vergaberechtstransformationsgesetz"
  - "Lieferaufträge"
---

# Test — ausschreibungspruefung

Struktureller Smoke-Test. Erwartet wird, dass der Output (1) die fehlende Gewichtung als Verstoß gegen § 127 Abs. 5 GWB identifiziert, (2) den Mindestumsatz von 5 Mio. EUR auf Verhältnismäßigkeit § 122 Abs. 4 GWB / § 45 Abs. 4 VgV prüft, (3) die unbegründete Verweigerung der Losaufteilung § 97 Abs. 4 GWB markiert und (4) die Rügefrist bis Ablauf der Angebotsfrist (§ 160 Abs. 3 S. 1 Nr. 3 GWB) konkret datiert.

**Aktualitäts-Assertions (Stand 2026-07).** Der Skill muss zusätzlich das seit **01.05.2026** geltende **Bundestariftreuegesetz** (BGBl. 2026 I Nr. 119) mit der Schwelle **50.000 EUR netto**, der **Tariftreueerklärung** und den Ausnahmen (Lieferaufträge, Bundeswehr) abbilden sowie das seit **01.07.2026** geltende **Vergabebeschleunigungsgesetz**.

Der Begriff `Vergaberechtstransformationsgesetz` steht bewusst unter `must_flag`: Er darf im Skill **ausschließlich als ausdrücklich gekennzeichnete Namensfalle** vorkommen — als Arbeitstitel eines Ampel-Vorhabens, nicht als Bezeichnung geltenden Rechts. Verschwindet die Warnung, schlägt der Test an.

Hinweis zum Sachverhalt: Auftraggeber ist eine **Landesbehörde**. Das BTTG bindet den **Bund**; ein korrekter Output grenzt daher ab und verweist auf das einschlägige **Landesvergabe-/Tariftreuegesetz**.

Run: `python ../../../scripts/eval.py --skill vergaberecht/skills/ausschreibungspruefung`
