---
name: arrest-borghei
title: /prozessrecht:arrest
description: Antrag auf Arrest zur Sicherung von Geldforderungen – dinglicher Arrest § 916 ZPO, Arrestgrund § 917 ZPO, persönlicher Arrest § 918 ZPO, Arrestgesuch und Glaubhaftmachung § 920 ZPO, Vollziehung § 929 ZPO. Use when eine Geldforderung gegen einen Schuldner vorläufig gesichert werden soll, bei dem die spätere Zwangsvollstreckung vereitelt oder erschwert zu werden droht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/arrest
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:arrest

## Zweck

Der Arrest ist das Gegenstück zur einstweiligen Verfügung für **Geldforderungen**: Er sichert die künftige Zwangsvollstreckung, indem er das Vermögen des Schuldners vorläufig blockiert (Pfändung, Sicherungshypothek) oder – als persönlicher Arrest – seine Person in Haft nimmt. Voraussetzung sind ein **Arrestanspruch** (die Geldforderung) und ein **Arrestgrund** (die Gefährdung der Vollstreckung). Beide sind nur **glaubhaft zu machen**. Dieser Skill prüft Anspruch und Grund, wählt dinglichen oder persönlichen Arrest und stellt das Arrestgesuch zusammen.

## Eingaben

- **Geldforderung** (Grund, Höhe, Fälligkeit, auch künftige/bedingte Forderung)
- **Gefährdungslage** (Vermögensverschiebung, Auslandsflucht, Beiseiteschaffen von Vermögen)
- **Schuldnerverhalten** (Insolvenzanzeichen, Verkauf von Vermögenswerten, Wohnsitzverlegung)
- **Glaubhaftmachungsmittel** (eidesstattliche Versicherung, Urkunden, Auskünfte)
- **Vollstreckungsobjekte** (bekannte Konten, Grundstücke, bewegliche Sachen)
- **Eilbedürftigkeit** (Zeit bis zur drohenden Vereitelung)

## Sub-Agent-Architektur

Die Bearbeitung wird in drei gedankliche Prüfstränge zerlegt, die zusammengeführt werden. Ein erster Strang prüft den **Arrestanspruch** – ob eine sicherbare Geldforderung oder ein in eine solche übergehender Anspruch besteht (§ 916 ZPO). Ein zweiter Strang prüft den **Arrestgrund** – die konkrete Gefährdung der Vollstreckung beim dinglichen Arrest (§ 917 ZPO) bzw. die strengeren Voraussetzungen des persönlichen Arrests (§ 918 ZPO). Ein dritter Strang stellt das **Arrestgesuch** mit Glaubhaftmachung zusammen (§ 920 ZPO), bestimmt die Höhe der Lösungssumme und plant die **Vollziehung** binnen Monatsfrist (§ 929 ZPO). Die Synthese wägt dinglichen gegen persönlichen Arrest ab und benennt das Schadensersatzrisiko.

## Ablauf

### 1. Arrestanspruch ([§ 916 ZPO](https://www.gesetze-im-internet.de/zpo/__916.html))

- Der Arrest dient der Sicherung der Zwangsvollstreckung wegen einer **Geldforderung** oder eines Anspruchs, der in eine Geldforderung übergehen kann.
- Auch **künftige oder bedingte** Forderungen sind sicherbar (§ 916 Abs. 2 ZPO).
- Die Forderung selbst muss schlüssig dargelegt und glaubhaft gemacht sein.

### 2. Dinglicher Arrest – Arrestgrund ([§ 917 ZPO](https://www.gesetze-im-internet.de/zpo/__917.html))

- Der dingliche Arrest findet statt, wenn zu besorgen ist, dass ohne ihn die **Vollstreckung des Urteils vereitelt oder wesentlich erschwert** würde.
- Anhaltspunkte: Vermögensverschiebung, Beiseiteschaffen von Werten, Veräußerung des wesentlichen Vermögens, drohender Wegzug. Die **Auslandsvollstreckung** allein begründet seit § 917 Abs. 2 ZPO im EU-Raum keinen Arrestgrund mehr.
- Bloße Zahlungsunfähigkeit oder schlechte Vermögenslage genügt **nicht**; erforderlich ist ein gezieltes vollstreckungsvereitelndes Verhalten.

### 3. Persönlicher Arrest ([§ 918 ZPO](https://www.gesetze-im-internet.de/zpo/__918.html))

- Der persönliche Arrest (Haft oder Beschränkung der Bewegungsfreiheit) ist **nur** zulässig, wenn er erforderlich ist, um die gefährdete Vollstreckung in das Vermögen zu sichern, und der dingliche Arrest nicht ausreicht.
- Ultima Ratio: Wegen des Grundrechtseingriffs (Art. 2, 104 GG) eng auszulegen; kommt praktisch nur bei drohender Flucht ins Ausland in Betracht.

### 4. Arrestgesuch und Glaubhaftmachung ([§ 920 ZPO](https://www.gesetze-im-internet.de/zpo/__920.html))

- Das Gesuch hat die **Bezeichnung des Anspruchs** unter Angabe des Geldbetrags und die **Bezeichnung des Arrestgrundes** zu enthalten (§ 920 Abs. 1 ZPO).
- Arrestanspruch und Arrestgrund sind **glaubhaft zu machen** (§ 920 Abs. 2 ZPO) – eidesstattliche Versicherung, Urkunden, präsente Beweismittel.
- Zuständig ist das Gericht der Hauptsache oder das Amtsgericht der belegenen Sache (§ 919 ZPO).

### 5. Arrestbefehl und Lösungssumme

- Das Gericht setzt im Arrestbefehl einen Geldbetrag fest, durch dessen **Hinterlegung** der Schuldner die Vollziehung abwenden und einen vollzogenen Arrest aufheben kann (§ 923 ZPO – Lösungssumme).
- Bei Dringlichkeit Entscheidung durch Beschluss ohne mündliche Verhandlung; sonst durch Endurteil (§ 922 ZPO).

### 6. Vollziehung ([§ 929 ZPO](https://www.gesetze-im-internet.de/zpo/__929.html))

- Die Vollziehung erfolgt durch **Pfändung** beweglicher Sachen/Forderungen oder Eintragung einer **Arresthypothek** (§§ 930, 932 ZPO).
- **Vollziehungsfrist**: Der Arrest ist binnen **eines Monats** ab Verkündung/Zustellung zu vollziehen (§ 929 Abs. 2 ZPO); die Vollziehung darf bereits vor Zustellung an den Schuldner beginnen (§ 929 Abs. 3 ZPO).

### 7. Rechtsbehelfe und Risiko

- Der Schuldner kann **Widerspruch** (§ 924 ZPO), Antrag auf Anordnung der Klageerhebung (§ 926 ZPO) oder Aufhebung wegen veränderter Umstände (§ 927 ZPO) stellen.
- **Schadensersatzrisiko** nach § 945 ZPO bei von Anfang an ungerechtfertigtem Arrest.

## Risiken / typische Fehler

- **Arrestgrund** zu schwach: bloße Zahlungsunfähigkeit statt gezielter Vollstreckungsvereitelung dargelegt – das Gesuch wird zurückgewiesen.
- **Glaubhaftmachung** fehlt: Anspruch oder Grund nur behauptet, keine eidesstattliche Versicherung oder Urkunde vorgelegt.
- **Vollziehungsfrist** des § 929 ZPO versäumt: Der erwirkte Arrest wird nicht binnen Monatsfrist vollzogen und damit wirkungslos.
- **persönlicher Arrest** vorschnell beantragt, obwohl der dingliche Arrest ausreicht – unverhältnismäßiger Grundrechtseingriff, Zurückweisung.

## Ausgabeformat

```
ARREST — <Geldforderung> — <Datum>

I.    Arrestanspruch § 916       Forderung EUR: <…>  [schlüssig/glaubhaft? ja/nein]
                                 künftig/bedingt? [ja/nein]
II.   Arrestgrund
      - dinglich § 917           Vollstreckungsvereitelung droht? [ja/nein — Indiz]
      - persönlich § 918         erforderlich + dinglich unzureichend? [ja/nein]
III.  Arrestgesuch § 920         Anspruchsbezeichnung / Arrestgrund
      Glaubhaftmachung           Mittel: <eidesstattl. Versicherung/Urkunden>
IV.   Arrestbefehl § 922/§ 923   Lösungssumme: <EUR>
V.    Vollziehung § 929          Frist 1 Monat — Art: Pfändung/Arresthypothek
VI.   Rechtsbehelfe/Risiko       Widerspruch § 924 / Schadensersatz § 945

Empfehlung: dinglicher / persönlicher Arrest — <Begründung>
```

## Quellen

### Statute

- [§ 916 ZPO](https://www.gesetze-im-internet.de/zpo/__916.html) (Arrestanspruch), [§ 917 ZPO](https://www.gesetze-im-internet.de/zpo/__917.html) (Arrestgrund dinglich), [§ 918 ZPO](https://www.gesetze-im-internet.de/zpo/__918.html) (persönlicher Arrest)
- [§ 920 ZPO](https://www.gesetze-im-internet.de/zpo/__920.html) (Arrestgesuch/Glaubhaftmachung), [§ 922 ZPO](https://www.gesetze-im-internet.de/zpo/__922.html), [§ 923 ZPO](https://www.gesetze-im-internet.de/zpo/__923.html) (Lösungssumme)
- [§ 929 ZPO](https://www.gesetze-im-internet.de/zpo/__929.html) (Vollziehungsfrist), [§ 930 ZPO](https://www.gesetze-im-internet.de/zpo/__930.html), [§ 932 ZPO](https://www.gesetze-im-internet.de/zpo/__932.html), [§ 945 ZPO](https://www.gesetze-im-internet.de/zpo/__945.html) (Schadensersatz)

### Kommentare

- Drescher, in: Musielak/Voit, ZPO, 22. Aufl. 2025, §§ 916 ff. Rn. 1 ff.
- Vollkommer, in: Zöller, ZPO, 36. Aufl. 2025, § 917 Rn. 1 ff.

### Rechtsprechung

- Zur Auslegung des Arrestgrundes (gezielte Vollstreckungsvereitelung, nicht bloße Zahlungsunfähigkeit) besteht gefestigte Rechtsprechung (Aktenzeichen vor Zitat verifizieren) `[unverifiziert – prüfen]`
