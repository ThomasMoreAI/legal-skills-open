---
name: wiederaufnahme-borghei
title: /strafrecht:wiederaufnahme
description: Prüfung der Wiederaufnahme eines rechtskräftig abgeschlossenen Strafverfahrens – zugunsten des Verurteilten § 359 StPO (neue Tatsachen und Beweismittel als novum), zuungunsten § 362 StPO, Zulässigkeits- und Begründetheitsprüfung §§ 368, 370 StPO; nova, Aditionsverfahren. Use when nach Rechtskraft eines Strafurteils neue Tatsachen oder Beweismittel die Wiederaufnahme rechtfertigen könnten.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/wiederaufnahme
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:wiederaufnahme

## Zweck

Die Wiederaufnahme durchbricht die **Rechtskraft** — den stärksten Bestandsschutz, den ein Strafurteil hat. Sie ist deshalb an enge, abschließend aufgezählte Gründe gebunden. Dieser Skill prüft, ob ein **novum** (neue Tatsache oder neues Beweismittel) oder ein anderer Wiederaufnahmegrund vorliegt, ob der Antrag zulässig ist (Aditionsverfahren) und ob er in der Begründetheitsprüfung Bestand hat.

## Eingaben

- rechtskräftiges Urteil (Gericht, Datum, Tenor)
- Richtung: zugunsten oder zuungunsten des Verurteilten?
- behaupteter Wiederaufnahmegrund (neue Tatsache, neues Beweismittel, falsche Urkunde, Falschaussage, Richteramtspflichtverletzung, Geständnis)
- war der Umstand im früheren Verfahren bekannt / verfügbar?
- Eignung des nova, einen Freispruch / eine geringere Strafe herbeizuführen

## Sub-Agent-Architektur

Die Bearbeitung gliedert sich in drei Prosa-Rollen. Ein Grund-Agent ordnet den Sachverhalt einem der abschließenden Wiederaufnahmegründe zu und prüft insbesondere, ob eine Tatsache oder ein Beweismittel **neu** ist (im früheren Verfahren weder bekannt noch benutzt). Ein Zulässigkeits-Agent führt das Aditionsverfahren durch: Form, Vortrag des Grundes und Bezeichnung geeigneter Beweismittel nach § 368 StPO. Ein Begründetheits-Agent prüft im Probationsverfahren, ob der vorgebrachte Grund hinreichend bestätigt ist und geeignet war, die Entscheidung zu beeinflussen (§ 370 StPO). Die Rollen sind gedankliche Arbeitsschritte, keine getrennten technischen Prozesse.

## Ablauf

### 1. Wiederaufnahme zugunsten ([§ 359 StPO](https://www.gesetze-im-internet.de/stpo/__359.html))

Zugunsten des Verurteilten zulässig u. a., wenn

- eine in der Hauptverhandlung als echt vorgebrachte Urkunde **unecht oder verfälscht** war (§ 359 Nr. 1),
- ein Zeuge oder Sachverständiger eine **vorsätzliche oder fahrlässige Falschaussage / Eidesverletzung** begangen hat (§ 359 Nr. 2),
- ein mitwirkender Richter eine **Amtspflichtverletzung** begangen hat (§ 359 Nr. 3),
- **neue Tatsachen oder Beweismittel** beigebracht werden, die allein oder in Verbindung mit früheren Beweisen geeignet sind, einen **Freispruch** oder eine **geringere Bestrafung** herbeizuführen (§ 359 Nr. 5 — das praktisch wichtigste **novum**).

### 2. Was ist ein novum?

Eine Tatsache oder ein Beweismittel ist **neu**, wenn es dem erkennenden Gericht im früheren Verfahren **nicht bekannt** war und nicht benutzt wurde — unabhängig davon, ob es objektiv schon existierte. Kein novum ist die bloße **neue Würdigung** bereits bekannter Tatsachen. Erforderlich ist zusätzlich die **Eignung**, das Ergebnis zu ändern.

### 3. Wiederaufnahme zuungunsten ([§ 362 StPO](https://www.gesetze-im-internet.de/stpo/__362.html))

Zuungunsten des Angeklagten nur in eng begrenzten Fällen: gefälschte Urkunde zu seinen Gunsten, Falschaussage zu seinen Gunsten, Richteramtspflichtverletzung sowie ein **glaubhaftes gerichtliches oder außergerichtliches Geständnis** des Freigesprochenen. Die Schwelle ist bewusst hoch — Schutz vor doppelter Strafverfolgung (Art. 103 Abs. 3 GG).

### 4. Zulässigkeit — Aditionsverfahren ([§ 368 StPO](https://www.gesetze-im-internet.de/stpo/__368.html))

Der Antrag ist als **unzulässig zu verwerfen**, wenn er nicht in der vorgeschriebenen **Form** angebracht ist, **kein gesetzlicher Wiederaufnahmegrund** geltend gemacht oder **kein geeignetes Beweismittel** angegeben wird. Erst nach Passieren dieser Stufe (Aditionsverfahren) tritt das Gericht in die inhaltliche Prüfung ein.

### 5. Begründetheit — Probationsverfahren ([§ 370 StPO](https://www.gesetze-im-internet.de/stpo/__370.html))

Der Antrag wird **als unbegründet verworfen**, wenn die aufgestellten Behauptungen **keine genügende Bestätigung** finden oder — in den Fällen des § 359 Nr. 1, 2 bzw. § 362 Nr. 1, 2 — die Annahme ausgeschlossen ist, dass die Handlung die Entscheidung beeinflusst hat. Andernfalls ordnet das Gericht die **Wiederaufnahme und Erneuerung der Hauptverhandlung** an (§ 370 Abs. 2 StPO).

### 6. Strategische Bewertung

- novum sauber von bloßer Neubewertung trennen — der häufigste Verwerfungsgrund.
- Eignung konkret darlegen: Warum hätte das Gericht bei Kenntnis anders entschieden?
- geeignete Beweismittel präzise benennen (Gutachten, Zeugen, Urkunden); pauschaler Vortrag scheitert schon im Aditionsverfahren.

## Quellen

### Statute

- [§ 359 StPO](https://www.gesetze-im-internet.de/stpo/__359.html), [§ 362 StPO](https://www.gesetze-im-internet.de/stpo/__362.html), [§ 368 StPO](https://www.gesetze-im-internet.de/stpo/__368.html), [§ 370 StPO](https://www.gesetze-im-internet.de/stpo/__370.html)
- § 364 StPO (Antrag), Art. 103 Abs. 3 GG (ne bis in idem)

### Kommentare

- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 359, § 370 Rn. 1 ff.
- Tiemann, in: KK-StPO, 9. Aufl. 2023, § 359 Rn. 1 ff.
- Beulke, Strafprozessrecht, 15. Aufl. 2023, Rn. 587 ff.

### Rechtsprechung

- BVerfG zur Reichweite der Wiederaufnahme zuungunsten § 362 StPO — Aktenzeichen `[unverifiziert – prüfen]`
- BGH zum Neuheitsbegriff (novum) bei § 359 Nr. 5 StPO — Aktenzeichen `[unverifiziert – prüfen]`

## Ausgabeformat

```
WIEDERAUFNAHME — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Rechtskräftiges Urteil     <Gericht / Datum / Tenor>
II.   Richtung                   [zugunsten § 359 / zuungunsten § 362 StPO]
III.  Wiederaufnahmegrund
      Typ:                        <novum § 359 Nr. 5 / Falschaussage / …>
      novum (neu + nicht benutzt)? [✅ / ⚠️ nur Neubewertung]
      Eignung (Freispruch/mildere Strafe)? [✅ / ⚠️]
IV.   Zulässigkeit (Adition § 368)
      Form / Grund / Beweismittel: [✅ / ⚠️ unzulässig]
V.    Begründetheit (Probation § 370)
      genügende Bestätigung?       [✅ / ⚠️]

Erfolgsaussicht: <…>
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Neubewertung statt novum** — eine bloß andere Würdigung bekannter Tatsachen ist **kein** neues Beweismittel; Antrag scheitert.
- **Eignung nicht dargelegt** — das novum muss geeignet sein, einen Freispruch oder eine geringere Strafe herbeizuführen.
- **Aditionsverfahren** unterschätzt — fehlende Form oder fehlendes Beweismittel (§ 368 StPO) führt zur Verwerfung als unzulässig, bevor die Begründetheit geprüft wird.
- **Wiederaufnahme zuungunsten** überschätzt — § 362 StPO ist eng; Art. 103 Abs. 3 GG (ne bis in idem) setzt enge Grenzen.
- **Rechtskraft** als überwindbar dargestellt, ohne dass ein abschließend aufgezählter Grund vorliegt.
