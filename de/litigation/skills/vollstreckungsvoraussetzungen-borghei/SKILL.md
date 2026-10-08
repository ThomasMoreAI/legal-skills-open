---
name: vollstreckungsvoraussetzungen-borghei
title: /zwangsvollstreckung:vollstreckungsvoraussetzungen
description: 'Die allgemeinen Voraussetzungen jeder Zwangsvollstreckung – Titel §§ 704, 794 ZPO, Vollstreckungsklausel §§ 724–726 ZPO, Zustellung § 750 ZPO als Trias, vollstreckbare Ausfertigung, Rechtsnachfolgeklausel § 727 ZPO, besondere Voraussetzungen §§ 751, 756 ZPO, sowie die Zuordnung der Rechtsbehelfe: Erinnerung § 766 ZPO, Klauselerinnerung § 732 ZPO, Klauselgegenklage § 768 ZPO, Vollstreckungsschutz § 765a ZPO und sofortige Beschwerde § 793 ZPO. Use when geprüft wird, ob aus einem Titel vollstreckt werden darf, eine Klausel erteilt oder angegriffen werden soll oder ein Schuldner sich gegen eine laufende Vollstreckung wehrt.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/zwangsvollstreckung/skills/vollstreckungsvoraussetzungen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /zwangsvollstreckung:vollstreckungsvoraussetzungen

## Zweck

Jede Zwangsvollstreckung steht auf drei Beinen: **Titel, Klausel, Zustellung**. Fehlt eines, ist die Vollstreckung fehlerhaft — und zwar unabhängig davon, ob der Anspruch materiell besteht. Diese Trennung von formeller und materieller Ebene ist zugleich die Landkarte der Rechtsbehelfe: Jeder Angriff gehört zu genau einer Ebene, und der falsch gewählte Rechtsbehelf geht als unzulässig verloren. Dieser Skill prüft die Trias vor Vollstreckungsbeginn und ordnet auf Schuldnerseite jeden Einwand dem richtigen Rechtsbehelf zu.

## Eingaben

- **Titel**: Art (Urteil, Vollstreckungsbescheid, Prozessvergleich, notarielle Urkunde, Kostenfestsetzungsbeschluss, einstweilige Verfügung), Gericht/Notar, Datum, Aktenzeichen
- **Tenor im Wortlaut** — insbesondere Bestimmtheit von Leistung, Zeit und Person
- **Rechtskraft** bzw. vorläufige Vollstreckbarkeit und etwaige **Sicherheitsleistung**
- **Klausel**: erteilt am, durch wen, einfache oder qualifizierte Klausel, Rechtsnachfolge
- **Zustellung**: Datum, Art (Zustellungsurkunde, Empfangsbekenntnis, Parteibetrieb), Nachweis
- Identität von **Gläubiger und Schuldner** mit den im Titel Genannten
- Auf Schuldnerseite: der konkrete **Einwand** (Erfüllung, Stundung, Aufrechnung, Formfehler, Härte)
- Vollstreckungsart und Stand des Verfahrens; drohende Termine

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft die ZPO-Normen des 8. Buchs mit URL sowie Kommentarstellen (Zöller, Musielak/Voit, Stein/Jonas) und die BGH-Linien zur Bestimmtheit des Titels.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Klauselantrag, Vollstreckungsauftrag oder Rechtsbehelfsschriftsatz.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft die Trias, die Zuordnung des Rechtsbehelfs und die Fristen.

## Ablauf

### 1. Titel ([§ 704 ZPO](https://www.gesetze-im-internet.de/zpo/__704.html), [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html))

Vollstreckt wird aus **Endurteilen**, die rechtskräftig oder für vorläufig vollstreckbar erklärt sind (§ 704 ZPO). Daneben stehen die Titel des § 794 Abs. 1 ZPO:

- **Prozessvergleiche** (Nr. 1) und Vergleiche vor Gütestellen,
- **Kostenfestsetzungsbeschlüsse** (Nr. 2),
- **Vollstreckungsbescheide** (Nr. 4) aus dem Mahnverfahren — Querverweis: `/prozessrecht:mahnverfahren`,
- **notarielle Urkunden mit Unterwerfungserklärung** (Nr. 5) — der praktisch wichtigste Titel ohne Gerichtsverfahren, insbesondere die Grundschuldbestellungsurkunde; Querverweis: `/immobilien-grundbuchrecht:grundschuld-sicherungsrecht`.

Prüfpunkte am Titel selbst:

- **Bestimmtheit**: Der Tenor muss Inhalt und Umfang der Leistung so genau bezeichnen, dass das Vollstreckungsorgan ohne eigene Sachprüfung handeln kann. Ein unbestimmter Tenor ist nicht vollstreckungsfähig; ein Zahlungstitel muss den Betrag beziffern oder rechnerisch eindeutig bestimmbar machen.
- **Parteiidentität**: Gläubiger und Schuldner müssen mit den im Titel Genannten übereinstimmen — sonst ist eine Rechtsnachfolgeklausel erforderlich.
- **Vorläufige Vollstreckbarkeit gegen Sicherheitsleistung**: Die Sicherheit ist **vor** Vollstreckungsbeginn zu leisten und nachzuweisen ([§ 751 Abs. 2 ZPO](https://www.gesetze-im-internet.de/zpo/__751.html)).

### 2. Vollstreckungsklausel ([§ 724 ZPO](https://www.gesetze-im-internet.de/zpo/__724.html), [§ 725 ZPO](https://www.gesetze-im-internet.de/zpo/__725.html), [§ 726 ZPO](https://www.gesetze-im-internet.de/zpo/__726.html))

Die Zwangsvollstreckung erfolgt aufgrund einer **vollstreckbaren Ausfertigung** des Titels (§ 724 Abs. 1 ZPO). Die Klausel lautet: "Vorstehende Ausfertigung wird dem … zum Zwecke der Zwangsvollstreckung erteilt" (§ 725 ZPO). Sie wird erteilt vom **Urkundsbeamten der Geschäftsstelle** des Prozessgerichts erster Instanz, bei notariellen Urkunden vom **Notar**.

- **Einfache Klausel** (§ 724 ZPO): Regelfall, keine besondere Prüfung.
- **Qualifizierte Klausel** (§ 726 ZPO): Hängt die Vollstreckung vom Eintritt einer vom Gläubiger zu beweisenden **Tatsache** ab, wird die Klausel nur erteilt, wenn der Beweis durch öffentliche oder öffentlich beglaubigte Urkunden geführt ist. Ausgenommen sind Zug-um-Zug-Titel, deren Gegenleistung nach [§ 756 ZPO](https://www.gesetze-im-internet.de/zpo/__756.html) erst der Gerichtsvollzieher prüft.
- **Weitere vollstreckbare Ausfertigung** ([§ 733 ZPO](https://www.gesetze-im-internet.de/zpo/__733.html)) nur nach Anhörung des Schuldners.

### 3. Rechtsnachfolgeklausel ([§ 727 ZPO](https://www.gesetze-im-internet.de/zpo/__727.html))

Für und gegen den **Rechtsnachfolger** der im Titel bezeichneten Partei sowie gegen den Besitzer der streitbefangenen Sache wird die Klausel erteilt, wenn die Rechtsnachfolge **offenkundig** oder durch **öffentliche oder öffentlich beglaubigte Urkunden** nachgewiesen ist. Typische Fälle: Erbfolge (Erbschein), Abtretung der titulierten Forderung (beglaubigte Abtretungsurkunde), Verschmelzung (Handelsregisterauszug), Erwerb einer Grundschuld. Wird der Nachweis nicht in dieser Form erbracht, ist der Gläubiger auf die **Klage auf Erteilung der Vollstreckungsklausel** ([§ 731 ZPO](https://www.gesetze-im-internet.de/zpo/__731.html)) verwiesen. Der Schuldner greift die Klausel mit der **Klauselerinnerung** (§ 732 ZPO) oder — wenn er die Rechtsnachfolge materiell bestreitet — mit der **Klauselgegenklage** ([§ 768 ZPO](https://www.gesetze-im-internet.de/zpo/__768.html)) an.

### 4. Zustellung ([§ 750 ZPO](https://www.gesetze-im-internet.de/zpo/__750.html))

Die Zwangsvollstreckung darf nur beginnen, wenn die Personen, für und gegen die sie stattfinden soll, in dem Titel oder in der Klausel **namentlich bezeichnet** sind und das Urteil bereits **zugestellt** ist oder gleichzeitig zugestellt wird. Für die qualifizierte und die Rechtsnachfolgeklausel gilt zusätzlich § 750 Abs. 2 ZPO: Klausel und die zu ihrer Erteilung vorgelegten Urkunden sind **mindestens zwei Wochen vor** Vollstreckungsbeginn zuzustellen. Diese Zwei-Wochen-Frist ist der am häufigsten übersehene Formfehler der Praxis.

Weitere Voraussetzungen: Bei einer **Kalenderzeit-** oder **Sicherheitsleistungsbedingung** greift § 751 ZPO; bei Zug-um-Zug-Titeln muss der Gerichtsvollzieher die Gegenleistung angeboten haben (§ 756 ZPO).

### 5. Rechtsbehelfe: die Zuordnung nach Ebenen

Der praktisch entscheidende Schritt. Jeder Einwand gehört zu genau einer Ebene:

| Einwand | Rechtsbehelf | Zuständigkeit |
|---|---|---|
| Fehler in der **Art und Weise** der Vollstreckung (Verfahrensfehler des Vollstreckungsorgans, unpfändbare Sache gepfändet, Zustellung fehlt) | **Erinnerung** [§ 766 ZPO](https://www.gesetze-im-internet.de/zpo/__766.html) | Vollstreckungsgericht |
| Fehler bei der **Klauselerteilung** (formelle Voraussetzungen nicht erfüllt, Nachweis nicht in der Form des § 726/§ 727 ZPO) | **Klauselerinnerung** [§ 732 ZPO](https://www.gesetze-im-internet.de/zpo/__732.html) | Erteilendes Gericht |
| **Materielle** Einwendungen gegen den titulierten Anspruch (Erfüllung, Stundung, Aufrechnung, Erlass) | **Vollstreckungsabwehrklage** [§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html) | Prozessgericht erster Instanz |
| Materielle Einwendungen gegen die **Rechtsnachfolge** | **Klauselgegenklage** [§ 768 ZPO](https://www.gesetze-im-internet.de/zpo/__768.html) | Prozessgericht |
| Die Veräußerung **hinderndes Recht eines Dritten** | **Drittwiderspruchsklage** [§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html) | Prozessgericht |
| **Sittenwidrige Härte** der Maßnahme | **Vollstreckungsschutz** [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html) | Vollstreckungsgericht |
| Entscheidung des Vollstreckungsgerichts ohne mündliche Verhandlung | **Sofortige Beschwerde** [§ 793 ZPO](https://www.gesetze-im-internet.de/zpo/__793.html), Frist zwei Wochen | Beschwerdegericht |

Zur Vollstreckungsabwehrklage und zur Präklusion nach § 767 Abs. 2 ZPO im Einzelnen: `/prozessrecht:vollstreckungsabwehrklage` — dort auch die Drittwiderspruchsklage. Bei **notariellen Urkunden** gilt die Besonderheit des [§ 797 Abs. 4 ZPO](https://www.gesetze-im-internet.de/zpo/__797.html): Die Präklusion des § 767 Abs. 2 ZPO greift nicht, weil es keine mündliche Verhandlung gab.

### 6. Vollstreckungsschutz ([§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html))

Auf Antrag des Schuldners hebt das Vollstreckungsgericht eine Maßnahme auf, untersagt sie oder stellt sie einstweilen ein, wenn sie unter voller Würdigung des Schutzbedürfnisses des Gläubigers wegen ganz besonderer Umstände eine **Härte** bedeutet, die mit den guten Sitten nicht vereinbar ist. Das ist eine **eng auszulegende Ausnahmevorschrift**, keine allgemeine Billigkeitsklausel. Anerkannte Fallgruppen betreffen vor allem konkrete Suizidgefahr, schwere Erkrankung und die Räumung ohne Anschlussunterkunft. Der Antrag ist **grundsätzlich vor** der Maßnahme zu stellen (§ 765a Abs. 3 ZPO); bei der Räumung ist zusätzlich die Räumungsfrist nach [§ 721 ZPO](https://www.gesetze-im-internet.de/zpo/__721.html) zu prüfen. Der Antrag hat **keine aufschiebende Wirkung** — die einstweilige Einstellung ist gesondert zu beantragen.

### 7. Vollstreckungsauftrag und Wahl des Zugriffs

Steht die Trias, folgt die Wahl des Zugriffs nach Erfolgsaussicht:

1. **Forderungspfändung** (Konto, Arbeitseinkommen, Ansprüche gegen Dritte) — schnellster Zugriff; `/zwangsvollstreckung:forderungspfaendung`.
2. **Sachpfändung und Vermögensauskunft** — bei unbekannter Vermögenslage regelmäßig der erste Schritt; `/zwangsvollstreckung:sachpfaendung-vermoegensauskunft`.
3. **Immobiliarvollstreckung** (Zwangshypothek, Zwangsversteigerung, Zwangsverwaltung) — bei Grundbesitz; `/zwangsvollstreckung:immobiliarvollstreckung-zvg`.

Der Auftrag an den Gerichtsvollzieher erfolgt über das amtliche Formular (Zwangsvollstreckungsformular-Verordnung); der Antrag beim Vollstreckungsgericht ebenfalls formulargebunden.

## Deterministische Berechnung

Die Zwei-Wochen-Frist des § 750 Abs. 2 ZPO und die Beschwerdefrist des § 793 ZPO sind **Ereignisfristen** nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html); das Fristende verschiebt sich nach [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) auf den nächsten Werktag ([§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html)). Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — Zugang, Zustellung und Fristbeginn bleiben juristische Eingaben und sind gesondert nachzuweisen.

```bash
# § 750 Abs. 2 ZPO: Zustellung der Klausel am 15.01.2026, frühester Vollstreckungsbeginn
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY

# Sofortige Beschwerde § 793 ZPO: Zustellung des Beschlusses am 15.01.2026
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY

# Kosten eines Vollstreckungsabwehrverfahrens (Geschäftswert = Titelbetrag)
python -m scripts.legal_calc.cli rvg --wert 8500 --posten verfahren termin
```

`--json` liefert die Rechenschritte samt Normzitat maschinenlesbar. Die Titelsumme selbst — Hauptforderung, titulierte Zinsen, festgesetzte Kosten — ist dem Titel und dem Kostenfestsetzungsbeschluss zu entnehmen, nicht zu schätzen.

## Quellen

### Statute

- [§ 704 ZPO](https://www.gesetze-im-internet.de/zpo/__704.html), [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html), [§ 797 ZPO](https://www.gesetze-im-internet.de/zpo/__797.html)
- [§ 724 ZPO](https://www.gesetze-im-internet.de/zpo/__724.html), [§ 725 ZPO](https://www.gesetze-im-internet.de/zpo/__725.html), [§ 726 ZPO](https://www.gesetze-im-internet.de/zpo/__726.html), [§ 727 ZPO](https://www.gesetze-im-internet.de/zpo/__727.html), [§ 731 ZPO](https://www.gesetze-im-internet.de/zpo/__731.html), [§ 732 ZPO](https://www.gesetze-im-internet.de/zpo/__732.html), [§ 733 ZPO](https://www.gesetze-im-internet.de/zpo/__733.html)
- [§ 750 ZPO](https://www.gesetze-im-internet.de/zpo/__750.html), [§ 751 ZPO](https://www.gesetze-im-internet.de/zpo/__751.html), [§ 756 ZPO](https://www.gesetze-im-internet.de/zpo/__756.html), [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html), [§ 766 ZPO](https://www.gesetze-im-internet.de/zpo/__766.html)
- [§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html), [§ 768 ZPO](https://www.gesetze-im-internet.de/zpo/__768.html), [§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html), [§ 793 ZPO](https://www.gesetze-im-internet.de/zpo/__793.html), [§ 721 ZPO](https://www.gesetze-im-internet.de/zpo/__721.html), [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html)

### Kommentare

- Seibel, in: Zöller, ZPO, 35. Aufl. 2024, § 750 Rn. 1 ff.; § 765a Rn. 1 ff.
- Lackmann, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 724 Rn. 1 ff.; § 727 Rn. 1 ff.
- Münzberg, in: Stein/Jonas, ZPO, 23. Aufl., § 750 Rn. 1 ff.
- Kindl/Meller-Hannich, Gesamtes Recht der Zwangsvollstreckung, 4. Aufl. 2021, § 750 ZPO Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 30.03.2010 – XI ZR 200/09 (Vollstreckungsunterwerfung aus einer Sicherungsgrundschuld; §§ 727, 732 ZPO, §§ 305c, 307 BGB) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-03-30&Aktenzeichen=XI%20ZR%20200/09
- Zu den Anforderungen an die Bestimmtheit des Vollstreckungstitels ist die st. Rspr. des BGH heranzuziehen `[unverifiziert - prüfen]`.
- Zu den Fallgruppen des § 765a ZPO, insbesondere zur Suizidgefahr bei Räumung und Zwangsversteigerung, ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Klauselantrag, Erinnerung, Vollstreckungsschutz

```
An das Amtsgericht <Ort> — Geschäftsstelle —
In Sachen <Gläubiger> ./. <Schuldner>, Az. <…>

Antrag auf Erteilung einer Rechtsnachfolgeklausel (§ 727 ZPO)

Die Gläubigerin hat die titulierte Forderung mit Vertrag vom <Datum> an die
Antragstellerin abgetreten. Die Abtretung ist durch die beigefügte
öffentlich beglaubigte Urkunde des Notars <…> vom <Datum>, UR-Nr. <…>,
nachgewiesen.

Es wird beantragt, der Antragstellerin eine vollstreckbare Ausfertigung des
Urteils des <Gericht> vom <Datum>, Az. <…>, mit der Klausel nach § 727 ZPO
zu erteilen.

Es wird darauf hingewiesen, dass Klausel und Nachweisurkunden dem Schuldner
gemäß § 750 Abs. 2 ZPO mindestens zwei Wochen vor Beginn der
Zwangsvollstreckung zuzustellen sind.
```

```
An das Amtsgericht <Ort> — Vollstreckungsgericht —

Erinnerung nach § 766 ZPO und Antrag auf einstweilige Einstellung

Namens des Schuldners lege ich gegen die Pfändung vom <Datum>
(Gerichtsvollzieher <…>, DR II <…>) Erinnerung nach § 766 ZPO ein.

Begründung: Die Zwangsvollstreckung wurde begonnen, ohne dass die
Vollstreckungsklausel und die zu ihrer Erteilung vorgelegten Urkunden dem
Schuldner zuvor zugestellt worden sind. § 750 Abs. 2 ZPO verlangt die
Zustellung mindestens zwei Wochen vor Beginn der Zwangsvollstreckung. Die
Maßnahme ist daher aufzuheben.

Es wird beantragt,
  1. die Zwangsvollstreckung aus dem Titel <…> einstweilen ohne
     Sicherheitsleistung einzustellen (§ 766 Abs. 1 S. 2 i. V. m. § 732
     Abs. 2 ZPO),
  2. die Pfändung vom <Datum> aufzuheben.
```

```
Antrag auf Vollstreckungsschutz (§ 765a ZPO)

Die für den <Datum> angesetzte Maßnahme bedeutet für den Schuldner unter
voller Würdigung des Schutzbedürfnisses der Gläubigerin wegen ganz
besonderer Umstände eine mit den guten Sitten nicht zu vereinbarende Härte.
Zur Glaubhaftmachung wird das ärztliche Attest vom <Datum> vorgelegt.
Es wird beantragt, die Maßnahme aufzuheben, hilfsweise sie einstweilen
einzustellen und dem Schuldner eine Frist bis zum <Datum> zu gewähren.
```

## Ausgabeformat

```
VOLLSTRECKUNGSVORAUSSETZUNGEN — <Gläubiger- / Schuldnerperspektive> — <Datum>

I.    Titel (§§ 704, 794 ZPO)      Art: <…>  Gericht/Notar: <…>  Datum: <…>
      - Bestimmtheit des Tenors    [✅ / 🔴 nicht vollstreckungsfähig]
      - Rechtskraft / vorl. VStr.  [rechtskräftig / § 709 / § 708 ZPO]
      - Sicherheitsleistung § 751  [N/A / geleistet am <Datum>]
II.   Klausel (§§ 724–727 ZPO)     erteilt am <Datum> durch <…>
      - Art                        [einfach § 724 / qualifiziert § 726 /
                                    Rechtsnachfolge § 727]
      - Nachweisform               [öffentlich / beglaubigt / 🔴 unzureichend]
III.  Zustellung (§ 750 ZPO)       Titel zugestellt am <Datum>
      - § 750 Abs. 2 ZPO           Klausel + Urkunden am <Datum>,
                                   frühester Beginn: <Datum>  [✅ / 🔴]
IV.   Parteiidentität              [✅ / Rechtsnachfolge geklärt / ❌]
V.    Zug-um-Zug § 756 ZPO         [N/A / Angebot durch GV erforderlich]
VI.   Rechtsbehelf (Schuldner)     Einwand: <…>
      → zutreffend:                [§ 766 / § 732 / § 767 / § 768 / § 771 /
                                    § 765a / § 793 ZPO]
      Frist                        <Datum>   Aufschiebende Wirkung [nein]
VII.  Gewählter Zugriff            [Forderung / Sache + Auskunft / Immobilie]
      Querverweis                  /zwangsvollstreckung:<skill>
VIII. Fristen / Kosten             s. Deterministische Berechnung

Ergebnis: <vollstreckungsreif / Hindernis: … / Vollstreckung angreifbar>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Zwei-Wochen-Frist des § 750 Abs. 2 ZPO übersehen** — bei qualifizierter oder Rechtsnachfolgeklausel muss vor Vollstreckungsbeginn zugestellt werden; die Maßnahme ist sonst auf Erinnerung aufzuheben.
- **Falscher Rechtsbehelf gewählt** — materielle Einwendungen gehören zur Vollstreckungsabwehrklage § 767 ZPO, nicht zur Erinnerung § 766 ZPO; der Fehler kostet Zeit und Kosten, und die Maßnahme läuft weiter.
- **Titel nicht bestimmt genug** — ein Tenor, der dem Vollstreckungsorgan eine eigene Sachprüfung abverlangt, ist nicht vollstreckungsfähig; das fällt erst beim Gerichtsvollzieher auf.
- **Rechtsnachfolge nicht in der Form des § 727 ZPO nachgewiesen** — private Abtretungsurkunde genügt nicht; ohne beglaubigten Nachweis bleibt nur die Klage nach § 731 ZPO.
- **Sicherheitsleistung nicht vor Beginn nachgewiesen** — § 751 Abs. 2 ZPO verlangt den Nachweis vorab; die Vollstreckung ist sonst einzustellen.
- **§ 765a ZPO als allgemeine Billigkeitsklausel behandelt** — die Vorschrift ist eng auszulegen, der Antrag ist vorher zu stellen und hat keine aufschiebende Wirkung.
- **Beschwerdefrist § 793 ZPO versäumt** — zwei Wochen ab Zustellung; danach steht die Entscheidung des Vollstreckungsgerichts fest.
