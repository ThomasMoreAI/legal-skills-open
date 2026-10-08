---
name: verwaltungsvollstreckung-borghei
title: /verwaltungsrecht:verwaltungsvollstreckung
description: 'Prüfung der Durchsetzung von Verwaltungsakten im gestreckten Vollstreckungsverfahren nach dem VwVG: Zwangsmittel § 6 VwVG, Ersatzvornahme § 10 VwVG, Zwangsgeld § 11 VwVG, unmittelbarer Zwang § 12 VwVG und Androhung § 13 VwVG. Use when eine Behörde einen vollziehbaren Verwaltungsakt zwangsweise durchsetzen will oder ein Betroffener gegen Zwangsmittel vorgehen möchte.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/verwaltungsvollstreckung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:verwaltungsvollstreckung

## Zweck

Befolgt ein Adressat eine durch Verwaltungsakt auferlegte Handlungs-, Duldungs- oder Unterlassungspflicht nicht, kann die Behörde sie mit Zwangsmitteln durchsetzen. Das Verwaltungsvollstreckungsgesetz (VwVG) regelt für den Bund das **gestreckte Verfahren**: Grundverwaltungsakt – Androhung – Festsetzung – Anwendung. Diese Skill prüft, ob die Vollstreckung rechtmäßig ist, ordnet das richtige Zwangsmittel zu und identifiziert Fehler in der Zwangsmittelkette. (Landesvollstreckungsrecht weicht ab; das jeweilige Landes-VwVG ist zu prüfen.)

## Eingaben

- Grundverwaltungsakt (Inhalt: Handlung, Duldung, Unterlassung)
- Vollziehbarkeit (bestandskräftig oder sofort vollziehbar, § 6 Abs. 1 VwVG)
- Art der Pflicht (vertretbar / unvertretbar)
- Bisherige Verfahrensschritte (Androhung, Festsetzung erfolgt?)
- Verhältnis der Belastung zum verfolgten Zweck

## Sub-Agent-Architektur

Drei Prüfstränge wirken in Prosa zusammen. Der **Grundlagen-Agent** prüft die allgemeinen Vollstreckungsvoraussetzungen nach § 6 VwVG (vollziehbarer Grundverwaltungsakt, auf Handlung/Duldung/Unterlassung gerichtet) und die Abgrenzung des gestreckten Verfahrens vom sofortigen Vollzug nach § 6 Abs. 2 VwVG. Der **Zwangsmittel-Agent** wählt zwischen Ersatzvornahme, Zwangsgeld und unmittelbarem Zwang und prüft deren Verhältnismäßigkeit (§ 9 VwVG). Der **Verfahrens-Agent** kontrolliert die Kette Androhung (§ 13 VwVG) – Festsetzung (§ 14 VwVG) – Anwendung auf formelle Fehler. Die Befunde werden zu einer Rechtmäßigkeitsbewertung zusammengeführt.

## Ablauf

### 1. Allgemeine Voraussetzungen ([§ 6 VwVG](https://www.gesetze-im-internet.de/vwvg/__6.html))

- Grundverwaltungsakt, gerichtet auf eine **Handlung, Duldung oder Unterlassung**
- **Vollziehbarkeit**: bestandskräftig oder sofort vollziehbar / aufschiebende Wirkung entfallen (§ 6 Abs. 1 VwVG)
- **Sofortiger Vollzug** ohne vorausgehenden VA nur ausnahmsweise (§ 6 Abs. 2 VwVG) bei gegenwärtiger Gefahr im Rahmen der Befugnisse

### 2. Zwangsmittel ([§ 6 VwVG](https://www.gesetze-im-internet.de/vwvg/__6.html), Katalog)

#### Ersatzvornahme ([§ 10 VwVG](https://www.gesetze-im-internet.de/vwvg/__10.html))

Bei **vertretbarer Handlung** (durch einen Dritten vornehmbar) lässt die Behörde die Handlung auf Kosten des Pflichtigen ausführen.

#### Zwangsgeld ([§ 11 VwVG](https://www.gesetze-im-internet.de/vwvg/__11.html))

Bei **unvertretbarer Handlung** sowie bei Duldungs- und Unterlassungspflichten; Höhe bis 25.000 Euro. Ist das Zwangsgeld uneinbringlich, kann Ersatzzwangshaft angeordnet werden (§ 16 VwVG).

#### Unmittelbarer Zwang ([§ 12 VwVG](https://www.gesetze-im-internet.de/vwvg/__12.html))

Einwirkung auf Personen oder Sachen durch körperliche Gewalt; nur **subsidiär**, wenn Ersatzvornahme oder Zwangsgeld nicht zum Ziel führen oder untunlich sind.

### 3. Verhältnismäßigkeit ([§ 9 VwVG](https://www.gesetze-im-internet.de/vwvg/__9.html))

Das Zwangsmittel muss in angemessenem Verhältnis zum Zweck stehen; das mildeste geeignete Mittel ist zu wählen.

### 4. Androhung ([§ 13 VwVG](https://www.gesetze-im-internet.de/vwvg/__13.html))

- Zwangsmittel ist **schriftlich anzudrohen**
- Angemessene **Frist** zur Erfüllung
- **Bestimmtes** Zwangsmittel; bei Ersatzvornahme vorläufige Kostenangabe
- Androhung kann mit dem Grundverwaltungsakt verbunden werden

### 5. Festsetzung und Anwendung ([§ 14 VwVG](https://www.gesetze-im-internet.de/vwvg/__14.html))

- Wird die Pflicht nicht fristgerecht erfüllt, wird das Zwangsmittel **festgesetzt**
- Anschließend **Anwendung** (Vollzug)
- Jeder Schritt ist ein selbstständiger, anfechtbarer Verwaltungsakt

### 6. Rechtsschutz des Betroffenen

- Anfechtung der Androhung, Festsetzung und Anwendung (jeweils VA)
- Eilrechtsschutz nach § 80 Abs. 5 VwGO, soweit aufschiebende Wirkung fehlt
- Einwendungen gegen den Grundverwaltungsakt sind grundsätzlich präkludiert, wenn dieser bestandskräftig ist

## Quellen

### Statute

- [§ 6 VwVG](https://www.gesetze-im-internet.de/vwvg/__6.html) (Zulässigkeit des Verwaltungszwangs, Zwangsmittel)
- [§ 9 VwVG](https://www.gesetze-im-internet.de/vwvg/__9.html) (Zwangsmittel, Verhältnismäßigkeit)
- [§ 10 VwVG](https://www.gesetze-im-internet.de/vwvg/__10.html) (Ersatzvornahme)
- [§ 11 VwVG](https://www.gesetze-im-internet.de/vwvg/__11.html) (Zwangsgeld)
- [§ 12 VwVG](https://www.gesetze-im-internet.de/vwvg/__12.html) (unmittelbarer Zwang)
- [§ 13 VwVG](https://www.gesetze-im-internet.de/vwvg/__13.html) (Androhung der Zwangsmittel)
- [§ 14 VwVG](https://www.gesetze-im-internet.de/vwvg/__14.html) (Festsetzung der Zwangsmittel)

### Kommentare

- Engelhardt / App / Schlatmann, VwVG/VwZG, 12. Aufl.
- Sadler / Tillmanns, VwVG/VwZG, 10. Aufl.
- Maurer / Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl.

### Rechtsprechung

- BVerwG, Urt. v. 13.12.2012 – 3 C 26.11 (Zwangsgeldfestsetzung) `[unverifiziert – prüfen]`
- BVerwG, Urt. v. 21.06.2017 – 6 C 4.16 (unmittelbarer Zwang, Subsidiarität) `[unverifiziert – prüfen]`

## Ausgabeformat

```
VERWALTUNGSVOLLSTRECKUNG (VwVG) — <Mandat> — <Datum>

I.    Grundverwaltungsakt
      Pflicht:                        [Handlung / Duldung / Unterlassung]
      Vertretbar / unvertretbar:      <…>
      Vollziehbarkeit § 6 VwVG:       [bestandskräftig / sofort vollziehbar]

II.   Zwangsmittelwahl
      Ersatzvornahme § 10 VwVG:       [+ / –]
      Zwangsgeld § 11 VwVG:           [+ / –]
      Unmittelbarer Zwang § 12 VwVG:  [+ / – subsidiär]
      Verhältnismäßigkeit § 9 VwVG:   <…>

III.  Verfahrenskette
      Androhung § 13 VwVG:            [erfolgt / fehlt]  Frist: <…>
      Festsetzung § 14 VwVG:          [erfolgt / fehlt]
      Anwendung:                      <…>

IV.   Rechtsschutz
      Anfechtbarer Akt:               <Androhung / Festsetzung / Anwendung>
      Eilrechtsschutz § 80 Abs. 5 VwGO: [erforderlich / nicht]

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Androhung fehlt oder ist unbestimmt** — ohne wirksame Androhung nach § 13 VwVG ist die Festsetzung rechtswidrig.
- **Falsches Zwangsmittel gewählt** — Ersatzvornahme setzt eine vertretbare Handlung voraus; bei unvertretbarer Pflicht ist das Zwangsgeld richtig.
- **Unmittelbarer Zwang ohne Subsidiarität** — § 12 VwVG greift erst, wenn mildere Zwangsmittel nicht zum Ziel führen.
- **Vollziehbarkeit des Grundverwaltungsakts übersehen** — fehlt sie (aufschiebende Wirkung), ist die gesamte Vollstreckung unzulässig.
