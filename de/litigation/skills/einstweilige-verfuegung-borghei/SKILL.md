---
name: einstweilige-verfuegung-borghei
title: /prozessrecht:einstweilige-verfuegung
description: Antrag auf einstweilige Verfügung im einstweiligen Rechtsschutz – Sicherungsverfügung § 935 ZPO, Regelungsverfügung § 940 ZPO, Verfügungsanspruch und Verfügungsgrund, Glaubhaftmachung § 920 ZPO, entsprechende Anwendung der Arrestvorschriften § 936 ZPO, Dringlichkeit. Use when ein Anspruch eilig gesichert oder ein Zustand vorläufig geregelt werden soll, bevor das Hauptsacheverfahren entscheidet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/einstweilige-verfuegung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:einstweilige-verfuegung

## Zweck

Die einstweilige Verfügung sichert vorläufig einen Individualanspruch (kein Geldanspruch – dafür der Arrest), wenn das reguläre Hauptsacheverfahren zu langsam wäre. Sie steht und fällt mit zwei Voraussetzungen: dem **Verfügungsanspruch** (dem materiellen Recht) und dem **Verfügungsgrund** (der Dringlichkeit). Beide müssen nur **glaubhaft gemacht**, nicht voll bewiesen werden. Dieser Skill ordnet das Begehren in Sicherungs- oder Regelungsverfügung ein, prüft die Dringlichkeit und stellt den Antrag zusammen.

## Eingaben

- **Anspruch** (Unterlassung, Vornahme, Sicherung — materielle Anspruchsgrundlage)
- **Bedrohungslage** (drohende Veränderung des Status quo, wesentliche Nachteile, Gewalt)
- **Zeitablauf** (wann wurde der Verstoß bekannt? Selbstwiderlegung der Dringlichkeit?)
- **Glaubhaftmachungsmittel** (eidesstattliche Versicherung, Urkunden, präsente Beweismittel)
- **Gegner** (Name, Anschrift, Vollstreckbarkeit)
- **Ziel** (Sicherung eines bestehenden Zustands oder Regelung eines streitigen Verhältnisses)

## Sub-Agent-Architektur

Die Prüfung wird in drei gedankliche Prüfstränge zerlegt, die parallel laufen und zusammengeführt werden. Ein erster Strang klärt den **Verfügungsanspruch** – das materielle Recht, das gesichert werden soll, und seine Schlüssigkeit. Ein zweiter Strang prüft den **Verfügungsgrund** – die Dringlichkeit nach § 935 ZPO (drohende Vereitelung) oder § 940 ZPO (Regelungsbedürfnis) sowie eine etwaige Selbstwiderlegung durch Zuwarten. Ein dritter Strang stellt die **Glaubhaftmachung** zusammen (§ 920 Abs. 2 ZPO über § 936 ZPO) und wählt das Verfahren (mit/ohne mündliche Verhandlung, Beschluss- oder Urteilsverfügung). Die Synthese formuliert den bestimmten Verfügungsantrag und prüft, ob er hinter dem Hauptsacheziel zurückbleibt (Verbot der Vorwegnahme).

## Ablauf

### 1. Verfügungsanspruch

- Der zu sichernde **Individualanspruch** (z. B. Unterlassung aus § 1004 BGB, wettbewerbsrechtlicher Unterlassungsanspruch, Herausgabe) muss schlüssig dargelegt sein.
- Keine Geldforderung: Für die Sicherung von Geldforderungen ist der dingliche Arrest einschlägig, nicht die Verfügung.

### 2. Sicherungsverfügung ([§ 935 ZPO](https://www.gesetze-im-internet.de/zpo/__935.html))

- Zulässig, wenn zu besorgen ist, dass durch eine **Veränderung des bestehenden Zustands** die Verwirklichung des Rechts vereitelt oder wesentlich erschwert werden könnte.
- Typischer Fall: Sicherung eines bestehenden Besitz- oder Zustandsverhältnisses, Beweismittelsicherung, Verbot der Weiterveräußerung.

### 3. Regelungsverfügung ([§ 940 ZPO](https://www.gesetze-im-internet.de/zpo/__940.html))

- Zulässig zur **einstweiligen Regelung eines streitigen Rechtsverhältnisses**, wenn dies nötig erscheint, um wesentliche Nachteile abzuwenden oder drohende Gewalt zu verhindern.
- Typischer Fall: vorläufige Nutzungsregelung, Wettbewerbsverbote, Presse-/Äußerungssachen, gesellschaftsrechtliche Streitigkeiten.

### 4. Verfügungsgrund / Dringlichkeit

- Der **Verfügungsgrund** ist die Eilbedürftigkeit; er fehlt, wenn der Antragsteller nach Kenntnis des Verstoßes zu lange zuwartet (**Selbstwiderlegung der Dringlichkeit** – je nach OLG-Praxis Wochen bis wenige Monate).
- In bestimmten Bereichen (Wettbewerbsrecht, § 12 Abs. 1 UWG) wird die Dringlichkeit vermutet, ist aber widerlegbar.

### 5. Glaubhaftmachung ([§ 920 ZPO](https://www.gesetze-im-internet.de/zpo/__920.html) über [§ 936 ZPO](https://www.gesetze-im-internet.de/zpo/__936.html))

- Über § 936 ZPO gelten die Arrestvorschriften entsprechend: Verfügungsanspruch und Verfügungsgrund sind **glaubhaft zu machen** (§ 920 Abs. 2 ZPO).
- Mittel: **eidesstattliche Versicherung** (§ 294 ZPO), Urkunden, präsente Beweismittel. Vollbeweis ist nicht erforderlich, ein überwiegendes Wahrscheinlichkeitsmaß genügt.

### 6. Verfahren und Entscheidung

- Bei **Dringlichkeit** kann das Gericht ohne mündliche Verhandlung durch Beschluss entscheiden (§ 937 Abs. 2 ZPO); andernfalls durch Urteil nach mündlicher Verhandlung.
- Rechtsbehelfe des Gegners: **Widerspruch** (§ 924 ZPO), Antrag auf Anordnung der Klageerhebung (§ 926 ZPO), Aufhebung wegen veränderter Umstände (§ 927 ZPO).
- **Vollziehungsfrist**: Die Verfügung ist binnen eines Monats zu vollziehen (§ 929 Abs. 2 ZPO über § 936 ZPO).

### 7. Grenzen

- Grundsatz: keine **Vorwegnahme der Hauptsache**; bei Leistungsverfügungen (z. B. Unterhalt) ausnahmsweise zulässig, wenn der Antragsteller sonst irreparable Nachteile erleidet.
- Schadensersatzrisiko nach § 945 ZPO, wenn sich die Verfügung als von Anfang an ungerechtfertigt erweist.

## Risiken / typische Fehler

- **Dringlichkeit** durch Zuwarten selbst widerlegt: Der Verfügungsgrund entfällt, weil zwischen Kenntnis und Antrag zu viel Zeit verstrichen ist.
- **Glaubhaftmachung** unzureichend: bloße Behauptung ohne eidesstattliche Versicherung oder präsente Mittel – Antrag wird zurückgewiesen.
- **Vorwegnahme** der Hauptsache: Der Antrag geht über reine Sicherung hinaus und nimmt das Endergebnis vorweg, ohne dass eine Ausnahme vorliegt.
- **Vollziehungsfrist** des § 929 ZPO versäumt: Die erwirkte Verfügung wird nicht binnen Monatsfrist vollzogen und damit wirkungslos.

## Ausgabeformat

```
EINSTWEILIGE VERFÜGUNG — <Begehren> — <Datum>

I.    Verfügungsanspruch        Anspruchsgrundlage: <…>  [schlüssig? ja/nein]
II.   Verfügungsart
      - Sicherungsverfügung § 935 [Veränderung des Status quo droht? ja/nein]
      - Regelungsverfügung § 940  [wesentliche Nachteile/Gewalt? ja/nein]
III.  Verfügungsgrund / Dringlichkeit
      Kenntnis am <…> / Antrag am <…>  [Selbstwiderlegung? ja/nein]
IV.   Glaubhaftmachung § 920/§ 936  Mittel: <eidesstattl. Versicherung/Urkunden>
V.    Verfahren                  [Beschluss ohne mV / Urteil nach mV]
      Vollziehungsfrist § 929    1 Monat ab Zustellung
VI.   Antrag (bestimmt)          <Unterlassung/Vornahme — Wortlaut>
                                 [Vorwegnahme der Hauptsache? ja/nein]

Empfehlung: <…>  / Risiko § 945 ZPO: <…>
```

## Quellen

### Statute

- [§ 935 ZPO](https://www.gesetze-im-internet.de/zpo/__935.html) (Sicherungsverfügung), [§ 940 ZPO](https://www.gesetze-im-internet.de/zpo/__940.html) (Regelungsverfügung)
- [§ 936 ZPO](https://www.gesetze-im-internet.de/zpo/__936.html) (entsprechende Anwendung der Arrestvorschriften), [§ 920 ZPO](https://www.gesetze-im-internet.de/zpo/__920.html) (Glaubhaftmachung)
- [§ 929 ZPO](https://www.gesetze-im-internet.de/zpo/__929.html) (Vollziehungsfrist), [§ 924 ZPO](https://www.gesetze-im-internet.de/zpo/__924.html) (Widerspruch), [§ 945 ZPO](https://www.gesetze-im-internet.de/zpo/__945.html) (Schadensersatz)
- [§ 12 UWG](https://www.gesetze-im-internet.de/uwg_2004/__12.html) (Dringlichkeitsvermutung im Wettbewerbsrecht)

### Kommentare

- Drescher, in: Musielak/Voit, ZPO, 22. Aufl. 2025, §§ 935 ff. Rn. 1 ff.
- Vollkommer, in: Zöller, ZPO, 36. Aufl. 2025, § 940 Rn. 1 ff.

### Rechtsprechung

- Zur Selbstwiderlegung der Dringlichkeit durch Zuwarten besteht gefestigte OLG-Rechtsprechung (Aktenzeichen je nach OLG vor Zitat verifizieren) `[unverifiziert – prüfen]`
