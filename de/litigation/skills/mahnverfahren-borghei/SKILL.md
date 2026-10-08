---
name: mahnverfahren-borghei
title: /prozessrecht:mahnverfahren
description: Durchführung des gerichtlichen Mahnverfahrens – Zulässigkeit § 688 ZPO, Mahnantrag und Mahnbescheid § 690 ZPO, Widerspruch § 694 ZPO, Vollstreckungsbescheid § 699 ZPO, Einspruch § 700 ZPO, Verjährungshemmung. Use when eine bezifferte Geldforderung schnell und kostengünstig tituliert oder kurz vor Jahresende die Verjährung gehemmt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/mahnverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:mahnverfahren

## Zweck

Das gerichtliche Mahnverfahren titelt bezifferte Geldforderungen ohne mündliche Verhandlung und ohne Schlüssigkeitsprüfung. Es ist schnell, billig und automatisiert (zentrale Mahngerichte). Sein größter Wert liegt in der **Verjährungshemmung**: Die Zustellung des Mahnbescheids hemmt die Verjährung wie eine Klage. Dieser Skill prüft, ob das Mahnverfahren passt, formuliert den Mahnantrag und führt durch die Eskalationsstufen Mahnbescheid → Vollstreckungsbescheid bzw. die Übergangswege Widerspruch und Einspruch.

## Eingaben

- **Forderung** (Grund, Höhe in EUR, Fälligkeit, Nebenforderungen)
- **Gläubiger und Schuldner** (Name, ladungsfähige Anschrift, Rechtsform)
- **Bisheriger Schriftverkehr** (außergerichtliche Mahnung, Teilzahlungen)
- **Verjährungslage** (Verjährungsbeginn, drohender Fristablauf)
- **Streitstand** (ist die Forderung voraussichtlich streitig?)
- **Zinsen und Kosten** (Verzugszinssatz, vorgerichtliche Anwaltskosten)

## Sub-Agent-Architektur

Die Bearbeitung wird in drei gedankliche Prüfstränge zerlegt, die nacheinander zusammengeführt werden. Ein erster Strang klärt die **Eignung** des Verfahrens – ob eine bezifferte Geldforderung in EUR vorliegt (§ 688 ZPO) und ob der Gegner voraussichtlich kooperiert oder mit Widerspruch zu rechnen ist. Ein zweiter Strang erstellt den **Mahnantrag** – Parteibezeichnung, Forderungsindividualisierung, Zinsen und Nebenforderungen (§ 690 ZPO) – und prüft die Zustellbarkeit. Ein dritter Strang plant die **Eskalation** entlang der Fristen: Widerspruch (§ 694 ZPO), Vollstreckungsbescheid (§ 699 ZPO) und Einspruch (§ 700 ZPO). Die Synthese gleicht die gewählte Strategie mit der Verjährungslage ab und empfiehlt Mahnverfahren oder sofortige Klage.

## Ablauf

### 1. Zulässigkeit ([§ 688 ZPO](https://www.gesetze-im-internet.de/zpo/__688.html))

- Nur **Ansprüche auf Zahlung einer bestimmten Geldsumme in EUR** sind mahnfähig.
- Ausgeschlossen u. a. bei Gegenleistung, die noch nicht erbracht ist (§ 688 Abs. 2 ZPO), bei unzulässiger Verbraucherkredit-Zinshöhe und wenn die Zustellung im Ausland oder öffentlich erfolgen müsste.
- Sachliche Zuständigkeit: ausschließlich das zentrale **Mahngericht** (Automatisiertes Mahnverfahren), bestimmt nach dem Wohnsitz des Antragstellers.

### 2. Mahnantrag und Mahnbescheid ([§ 690 ZPO](https://www.gesetze-im-internet.de/zpo/__690.html))

- Mussinhalt des Antrags: Parteien und Vertreter, Gericht, **Bezeichnung des Anspruchs unter Angabe der verlangten Leistung**, Hauptforderung und Nebenforderungen getrennt, Erklärung über Gegenleistung.
- Die Forderung muss **individualisiert** (nicht schlüssig begründet) sein: Der Schuldner muss erkennen können, welcher Anspruch geltend gemacht wird, sonst tritt keine Verjährungshemmung ein.
- Das Gericht erlässt ohne Prüfung der Begründetheit den **Mahnbescheid** und stellt ihn von Amts wegen zu. Die **Zustellung** ist der für die Verjährungshemmung maßgebliche Zeitpunkt.

### 3. Widerspruch ([§ 694 ZPO](https://www.gesetze-im-internet.de/zpo/__694.html))

- Der Schuldner kann gegen den Mahnbescheid **Widerspruch** einlegen, solange der Vollstreckungsbescheid noch nicht verfügt ist – regelmäßig binnen **zwei Wochen** ab Zustellung (Frist für die spätere Vollstreckungsbescheid-Beantragung).
- Der Widerspruch muss nicht begründet werden; er führt nicht zur Abweisung, sondern leitet bei entsprechendem Antrag in das **streitige Verfahren** über (Abgabe an das Prozessgericht).

### 4. Vollstreckungsbescheid ([§ 699 ZPO](https://www.gesetze-im-internet.de/zpo/__699.html))

- Legt der Schuldner nicht rechtzeitig Widerspruch ein, erlässt das Gericht auf Antrag den **Vollstreckungsbescheid**.
- Der Antrag ist erst nach Ablauf der Widerspruchsfrist, aber **nicht später als sechs Monate** nach Zustellung des Mahnbescheids zulässig.
- Der Vollstreckungsbescheid ist ein vollstreckbarer Titel (§ 794 Abs. 1 Nr. 4 ZPO), für vorläufig vollstreckbar erklärt.

### 5. Einspruch ([§ 700 ZPO](https://www.gesetze-im-internet.de/zpo/__700.html))

- Gegen den Vollstreckungsbescheid ist der **Einspruch** statthaft; er steht einem Versäumnisurteil gleich.
- Die **Einspruchsfrist** beträgt zwei Wochen ab Zustellung; nach Einspruch wird der Rechtsstreit an das im Mahnbescheid bezeichnete Prozessgericht abgegeben und streitig fortgeführt.

### 6. Verjährungshemmung und Strategie

- Die Zustellung des Mahnbescheids hemmt die **Verjährung** (§ 204 Abs. 1 Nr. 3 BGB); kurz vor Jahresende ist das Mahnverfahren das schnellste Hemmungsmittel.
- Wird der Anspruch im Antrag nicht ausreichend individualisiert, tritt **keine Hemmung** ein – häufigster Fehler bei Sammel- oder Saldoforderungen.
- Ist mit Widerspruch sicher zu rechnen, kann die direkte Klage günstiger sein (kein doppelter Aktenlauf).

## Risiken / typische Fehler

- **Verjährung** verkannt: Antrag zu spät eingereicht oder Forderung nicht individualisiert, sodass die Hemmung nicht eintritt.
- **Zustellung** unbeachtet: Maßgeblich für die Hemmung ist die Zustellung des Mahnbescheids, nicht die Antragstellung – bei demnächstiger Zustellung greift § 167 ZPO.
- **Widerspruchsfrist** und **Einspruchsfrist** verwechselt: Beide betragen zwei Wochen, knüpfen aber an unterschiedliche Bescheide an.
- **Sechs-Monats-Frist** des § 699 ZPO versäumt: Der Mahnbescheid verfällt, die Hemmung endet sechs Monate nach der letzten Verfahrenshandlung.

## Ausgabeformat

```
MAHNVERFAHREN — <Forderung> — <Datum>

I.    Zulässigkeit § 688        bezifferte Geldforderung EUR: <…> [ja/nein]
                                Gegenleistung erbracht? [ja/nein]
II.   Mahnantrag § 690          Gläubiger / Schuldner: <…>
                                Hauptforderung: <EUR>  Nebenforderungen: <…>
                                Individualisierung: <Anspruchsbezeichnung>
III.  Mahnbescheid              Zustelldatum (Hemmung): <…>
IV.   Reaktion Schuldner
      - Widerspruch § 694       [eingelegt am <…> → streitiges Verfahren]
      - kein Widerspruch        → Vollstreckungsbescheid § 699
V.    Vollstreckungsbescheid    Antrag binnen 6 Monaten: [ja/nein]
      Einspruch § 700           [Frist 2 Wochen — eingelegt? ja/nein]
VI.   Verjährungshemmung        Beginn / Ende der Hemmung: <…>

Empfehlung: Mahnverfahren / sofortige Klage — <Begründung>
```

## Quellen

### Statute

- [§ 688 ZPO](https://www.gesetze-im-internet.de/zpo/__688.html) (Zulässigkeit), [§ 690 ZPO](https://www.gesetze-im-internet.de/zpo/__690.html) (Mahnantrag/Mahnbescheid)
- [§ 694 ZPO](https://www.gesetze-im-internet.de/zpo/__694.html) (Widerspruch), [§ 699 ZPO](https://www.gesetze-im-internet.de/zpo/__699.html) (Vollstreckungsbescheid), [§ 700 ZPO](https://www.gesetze-im-internet.de/zpo/__700.html) (Einspruch)
- [§ 167 ZPO](https://www.gesetze-im-internet.de/zpo/__167.html) (Rückwirkung der Zustellung), [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html) (Vollstreckungstitel)
- [§ 204 BGB](https://www.gesetze-im-internet.de/bgb/__204.html) (Hemmung durch Rechtsverfolgung)

### Kommentare

- Schüler, in: Musielak/Voit, ZPO, 22. Aufl. 2025, §§ 688 ff. Rn. 1 ff.
- Seibel, in: Zöller, ZPO, 36. Aufl. 2025, § 690 Rn. 1 ff.

### Rechtsprechung

- Zur Individualisierung des Anspruchs als Voraussetzung der Verjährungshemmung besteht gefestigte BGH-Rechtsprechung (Aktenzeichen vor Zitat gesondert verifizieren) `[unverifiziert – prüfen]`
