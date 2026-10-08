---
name: raeumungsklage-borghei
title: /mietrecht:raeumungsklage
description: Räumungsklage und Zwangsräumung im Wohnraum- und Gewerberaummietrecht – Rückgabeanspruch § 546 BGB und Herausgabeanspruch § 985 BGB, Nutzungsentschädigung § 546a BGB, Verbindung mit der Zahlungsklage, Klage auf künftige Räumung § 259 ZPO, Zuständigkeit § 23 Nr. 2a GVG und § 29a ZPO, Räumungsfrist § 721 ZPO und Vollstreckungsschutz § 765a ZPO, Sicherungsanordnung § 283a ZPO, einstweilige Räumungsverfügung § 940a ZPO, Berliner Räumung § 885a ZPO. Use when eine Räumungsklage vorbereitet, erhoben oder abgewehrt wird oder eine Zwangsräumung ansteht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/raeumungsklage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:raeumungsklage

## Zweck

Die Räumungsklage ist der Ort, an dem materielle Fehler der Kündigung sichtbar werden — und an dem Verfahrensfehler das materiell Richtige scheitern lassen. Diese Skill baut den Räumungsanspruch von der Anspruchsgrundlage über die Antragsfassung bis zur Vollstreckung auf, verbindet ihn mit der Zahlungsklage und behandelt die Verteidigungslinien des Mieters: Räumungsfrist, Vollstreckungsschutz und Sozialklausel.

## Eingaben

- **Beendigungstatbestand**: Kündigung (fristlos / ordentlich), Zeitablauf, Aufhebungsvertrag — mit Datum und Zugangsnachweis
- **Mietvertrag**, Parteien, genaue Bezeichnung der Mieträume (Lage im Haus, Nebenräume, Stellplatz)
- **Zahlungsrückstand** und laufende Nutzungsentschädigung
- Ob **Untermieter, Angehörige oder Dritte** in der Wohnung wohnen
- **Widerspruch** des Mieters nach §§ 574 ff. BGB, geltend gemachte Härtegründe
- Vermögenslage des Mieters (für § 283a ZPO), Titel- und Vollstreckungsstand

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Anspruchs-Prüfer** klärt zuerst, ob das Mietverhältnis wirksam beendet ist — ohne Beendigung ist die Klage unschlüssig. Ein **Antrags-Architekt** formuliert Räumungs-, Zahlungs- und Hilfsanträge und achtet auf die Vollstreckungsfähigkeit der Bezeichnung. Ein **Passivlegitimations-Prüfer** ermittelt alle Mitbesitzer und stellt sicher, dass gegen jeden ein Titel erwirkt wird. Ein **Eilrechtsschutz-Prüfer** bewertet Sicherungsanordnung und einstweilige Räumungsverfügung. Ein **Vollstreckungs-Prüfer** plant Räumungsfrist, Berliner Räumung und Vollstreckungsschutz.

## Ablauf

### 1. Anspruchsgrundlagen ([§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html), [§ 985 BGB](https://www.gesetze-im-internet.de/bgb/__985.html))

**Vertraglicher Rückgabeanspruch (§ 546 Abs. 1 BGB):** Der Mieter ist nach Beendigung des Mietverhältnisses verpflichtet, die Mietsache zurückzugeben. Er ist der vorrangige und sicherste Anspruch, weil er kein Eigentum des Klägers voraussetzt. Nach **§ 546 Abs. 2 BGB** kann der Vermieter die Rückgabe auch von einem **Dritten** verlangen, dem der Mieter den Gebrauch überlassen hat.

**Dinglicher Herausgabeanspruch (§ 985 BGB):** Nur für den **Eigentümer**; er greift, wenn kein Besitzrecht nach § 986 BGB mehr besteht. In der kanonischen Reihenfolge Vertrag → dinglich wird er hilfsweise geltend gemacht, insbesondere gegen Dritte ohne Vertragsbeziehung.

**Nutzungsentschädigung (§ 546a BGB):** Gibt der Mieter die Sache nicht zurück, kann der Vermieter für die Dauer der Vorenthaltung die **vereinbarte Miete oder die ortsübliche Vergleichsmiete** verlangen — je nachdem, welche höher ist. Weitergehender Schadensersatz bleibt unberührt (Abs. 2).

### 2. Passivlegitimation — alle Mitbesitzer

Ein Räumungstitel wirkt nur gegen die im Titel benannten Personen. Zu verklagen sind daher **alle Mitmieter** und alle Personen, die **selbständigen Mitbesitz** haben — insbesondere der **Ehegatte oder eingetragene Lebenspartner**, auch wenn er den Mietvertrag nicht unterschrieben hat, sowie **Untermieter** (§ 546 Abs. 2 BGB). Kinder und Besucher haben keinen selbständigen Mitbesitz. Wer den Ehegatten vergisst, steht am Räumungstag vor der Tür: § 940a Abs. 2 ZPO hilft nur eingeschränkt.

### 3. Verbindung mit der Zahlungsklage

Räumungs- und Zahlungsantrag werden nach [§ 260 ZPO](https://www.gesetze-im-internet.de/zpo/__260.html) in einer Klage verbunden. Beantragt wird typischerweise: Räumung und Herausgabe, Zahlung des rückständigen Betrags nebst Verzugszinsen (§§ 288, 247 BGB) und — als **Klage auf künftige Leistung** — die laufende Nutzungsentschädigung bis zur Räumung. Der **Streitwert** setzt sich aus dem Jahresbetrag der Nettomiete für den Räumungsantrag ([§ 41 Abs. 2 GKG](https://www.gesetze-im-internet.de/gkg_2004/__41.html)) und dem Zahlungsbetrag zusammen; Nebenforderungen bleiben außer Ansatz.

### 4. Klage auf künftige Räumung ([§ 259 ZPO](https://www.gesetze-im-internet.de/zpo/__259.html))

Klage auf **künftige Leistung** kann erhoben werden, wenn den Umständen nach die Besorgnis gerechtfertigt ist, dass der Schuldner sich der rechtzeitigen Leistung entziehen werde. Das erlaubt es, die Räumungsklage **vor Ablauf der Kündigungsfrist** zu erheben und den Zeitverlust bis zum Titel zu verkürzen — praktisch bedeutsam bei langen Fristen des § 573c BGB. Die Besorgnis ist konkret darzulegen (etwa ausdrückliche Weigerung, fortdauernder Zahlungsverzug); die bloße Möglichkeit der Nichtleistung genügt nicht.

### 5. Zuständigkeit und Verfahren

Sachlich ist stets das **Amtsgericht** zuständig, unabhängig vom Streitwert, wenn es um Wohnraum geht ([§ 23 Nr. 2a GVG](https://www.gesetze-im-internet.de/gvg/__23.html)). Örtlich ist der **ausschließliche Gerichtsstand der Belegenheit** nach [§ 29a ZPO](https://www.gesetze-im-internet.de/zpo/__29a.html) maßgeblich. Räumungssachen sind nach [§ 272 Abs. 4 ZPO](https://www.gesetze-im-internet.de/zpo/__272.html) **vorrangig zu terminieren**. Die Mieträume sind im Antrag so genau zu bezeichnen, dass der Gerichtsvollzieher sie ohne weitere Ermittlung auffinden kann — Straße, Hausnummer, Geschoss, Lage auf dem Geschoss, Nebenräume, Keller, Stellplatz.

### 6. Sicherungsanordnung ([§ 283a ZPO](https://www.gesetze-im-internet.de/zpo/__283a.html))

Auf Antrag des Klägers kann das Gericht anordnen, dass der Beklagte wegen der nach Rechtshängigkeit fällig werdenden Geldforderungen **Sicherheit leistet**, wenn die Klage hohe Aussicht auf Erfolg hat und die Anordnung nach Abwägung der beiderseitigen Interessen zur Abwendung besonderer Nachteile für den Kläger gerechtfertigt ist. Kommt der Beklagte der Anordnung nicht nach, eröffnet das den Weg zur **einstweiligen Räumungsverfügung** nach § 940a Abs. 3 ZPO. Die Sicherungsanordnung ist das schärfste Mittel gegen den bewussten Prozessverschlepper.

### 7. Einstweilige Räumungsverfügung ([§ 940a ZPO](https://www.gesetze-im-internet.de/zpo/__940a.html))

Die Räumung von Wohnraum darf durch einstweilige Verfügung **nur** angeordnet werden

- wegen **verbotener Eigenmacht** oder bei **konkreter Gefahr für Leib oder Leben** (Abs. 1),
- gegen einen **Dritten**, der ohne Kenntnis des Vermieters Besitz erlangt hat, wenn gegen den Mieter ein Räumungstitel vorliegt (Abs. 2),
- wenn der Schuldner einer **Sicherungsanordnung** nach § 283a ZPO nicht nachkommt (Abs. 3).

Außerhalb dieser Fälle ist der Eilrechtsschutz gesperrt — die Vorschrift ist Ausdruck des besonderen Bestandsschutzes der Wohnung.

### 8. Räumungsfrist und Vollstreckungsschutz ([§ 721 ZPO](https://www.gesetze-im-internet.de/zpo/__721.html), [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html))

Wird auf Räumung von Wohnraum erkannt, kann das Gericht dem Schuldner **von Amts wegen oder auf Antrag** eine den Umständen nach angemessene **Räumungsfrist** gewähren (§ 721 Abs. 1 ZPO). Die Frist darf insgesamt **ein Jahr** nicht übersteigen (Abs. 5); der Antrag ist vor Schluss der mündlichen Verhandlung zu stellen, bei nachträglichem Antrag gilt § 721 Abs. 2 ZPO. Im Vollstreckungsverfahren kann das Vollstreckungsgericht die Räumung nach **§ 765a ZPO** einstweilen einstellen, wenn sie eine mit den guten Sitten nicht zu vereinbarende **Härte** bedeutet — praktisch bei akuter Suizidgefahr, schwerer Erkrankung oder unmittelbar bevorstehender Entbindung. Bei Zeitmietverträgen tritt § 794a ZPO an die Stelle des § 721 ZPO. Materiellrechtlich flankierend: `/mietrecht:sozialklausel-widerspruch`.

### 9. Vollstreckung und Berliner Räumung ([§ 885 ZPO](https://www.gesetze-im-internet.de/zpo/__885.html), [§ 885a ZPO](https://www.gesetze-im-internet.de/zpo/__885a.html))

Die Räumung erfolgt durch den **Gerichtsvollzieher**: Besitzeinweisung des Gläubigers, Wegschaffung und Verwahrung der beweglichen Sachen (§ 885 ZPO). Bei der **Berliner Räumung** nach § 885a ZPO beschränkt der Gläubiger den Vollstreckungsauftrag auf die **Herausgabe der Wohnung**; der Gerichtsvollzieher setzt den Gläubiger nur in den Besitz ein, ohne die Gegenstände abzutransportieren. Der Gläubiger erwirbt an den zurückgelassenen Sachen ein **Vermieterpfandrecht**-ähnliches Verwertungsrecht nach Maßgabe des § 885a Abs. 2–4 ZPO und haftet nur für Vorsatz und grobe Fahrlässigkeit. Das senkt den Kostenvorschuss erheblich, verlagert aber Aufbewahrungs- und Verwertungsrisiken auf den Gläubiger.

## Quellen

### Statute

- [§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html), [§ 546a BGB](https://www.gesetze-im-internet.de/bgb/__546a.html), [§ 985 BGB](https://www.gesetze-im-internet.de/bgb/__985.html), [§ 986 BGB](https://www.gesetze-im-internet.de/bgb/__986.html), [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html)
- [§ 259 ZPO](https://www.gesetze-im-internet.de/zpo/__259.html), [§ 260 ZPO](https://www.gesetze-im-internet.de/zpo/__260.html), [§ 272 ZPO](https://www.gesetze-im-internet.de/zpo/__272.html), [§ 283a ZPO](https://www.gesetze-im-internet.de/zpo/__283a.html), [§ 29a ZPO](https://www.gesetze-im-internet.de/zpo/__29a.html)
- [§ 721 ZPO](https://www.gesetze-im-internet.de/zpo/__721.html), [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html), [§ 794a ZPO](https://www.gesetze-im-internet.de/zpo/__794a.html), [§ 885 ZPO](https://www.gesetze-im-internet.de/zpo/__885.html), [§ 885a ZPO](https://www.gesetze-im-internet.de/zpo/__885a.html), [§ 940a ZPO](https://www.gesetze-im-internet.de/zpo/__940a.html)
- [§ 23 GVG](https://www.gesetze-im-internet.de/gvg/__23.html), [§ 41 GKG](https://www.gesetze-im-internet.de/gkg_2004/__41.html)

### Kommentare

- Streyl, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 546 BGB Rn. 1 ff.
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 546 Rn. 1 ff.; § 546a Rn. 1 ff.
- Lackmann, in: Musielak/Voit, ZPO, aktuelle Auflage, § 885a Rn. 1 ff.
- Herget, in: Zöller, ZPO, aktuelle Auflage, § 940a Rn. 1 ff.; § 721 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 13.10.2021 – VIII ZR 91/20 (Schonfristzahlung beseitigt die hilfsweise ordentliche Kündigung nicht — für die Schlüssigkeit der Räumungsklage entscheidend) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-10-13&Aktenzeichen=VIII%20ZR%2091/20
- Zur Notwendigkeit eines Titels gegen den mitbesitzenden Ehegatten ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zu den Anforderungen an § 765a ZPO bei Suizidgefahr ist die einschlägige BGH- und BVerfG-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Klageanträge

```
Namens und in Vollmacht der Klägerin erhebe ich Klage und beantrage:

1. Die Beklagten werden als Gesamtschuldner verurteilt, die im Anwesen
   <Straße, Hausnummer, PLZ Ort> im <…> Obergeschoss <rechts/links>
   gelegene Wohnung, bestehend aus <…> Zimmern, Küche, Bad, Flur, nebst
   Kellerraum Nr. <…> und Stellplatz Nr. <…> zu räumen und geräumt an die
   Klägerin herauszugeben.

2. Die Beklagten werden als Gesamtschuldner verurteilt, an die Klägerin
   <Betrag> EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem
   jeweiligen Basiszinssatz seit <Datum> zu zahlen.

3. Die Beklagten werden als Gesamtschuldner verurteilt, an die Klägerin ab
   dem <Datum> bis zur Räumung eine monatliche Nutzungsentschädigung in
   Höhe von <Betrag> EUR, jeweils fällig am dritten Werktag eines Monats,
   zu zahlen (§ 546a Abs. 1 BGB, § 259 ZPO).

Für den Fall, dass die Beklagten die Räumung verzögern, wird bereits jetzt
beantragt, gemäß § 283a ZPO anzuordnen, dass die Beklagten wegen der nach
Rechtshängigkeit fällig werdenden Geldforderungen Sicherheit leisten.

Es wird gebeten, den Rechtsstreit gemäß § 272 Abs. 4 ZPO vorrangig zu
terminieren.
```

## Ausgabeformat

```
RÄUMUNGSKLAGE — <Vorbereitung / Abwehr> — <Mandat-ID> — <Datum>

I.    Beendigungstatbestand              [fristlos § 543 / ordentlich § 573 /
                                          Zeitablauf / Aufhebung]
      Wirksamkeit                        [✅ / ⚠️ / ❌]
II.   Anspruchsgrundlage                 [§ 546 Abs. 1 / § 546 Abs. 2 / § 985 hilfsweise]
III.  Passivlegitimation                 <alle Mitmieter, Ehegatte, Untermieter>
      Titel gegen alle Mitbesitzer       [✅ / ❌ Lücke: <Person>]
IV.   Anträge
      - Räumung und Herausgabe           [gefasst]
      - Zahlung Rückstand                <Betrag> + Zinsen §§ 288, 247 BGB
      - Künftige Nutzungsentschädigung   <Betrag>/Monat (§ 546a, § 259 ZPO)
V.    Zuständigkeit                      AG <Ort> (§ 23 Nr. 2a GVG, § 29a ZPO)
      Streitwert                         <Betrag> (§ 41 Abs. 2 GKG + Zahlungsantrag)
VI.   Sicherungsanordnung § 283a ZPO     [beantragt / nicht veranlasst]
VII.  Eilrechtsschutz § 940a ZPO         [Abs. 1 / Abs. 2 / Abs. 3 / gesperrt]
VIII. Verteidigung des Mieters
      - Widerspruch §§ 574 ff. BGB       [erhoben / nicht erhoben]
      - Räumungsfrist § 721 ZPO          [beantragt — bis <Datum>, max. 1 Jahr]
      - Vollstreckungsschutz § 765a ZPO  [kein Anhalt / Antrag zu erwarten]
IX.   Vollstreckung                      [§ 885 ZPO vollständig / § 885a ZPO Berliner Räumung]
      Kostenvorschuss GV                 <Betrag>

Ergebnis: <schlüssig / nachzubessern>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Nicht gegen alle Mitbesitzer geklagt** — insbesondere der mitbesitzende Ehegatte fehlt; der Titel ist dann am Räumungstag wertlos.
- **Mieträume ungenau bezeichnet** — der Gerichtsvollzieher kann nicht vollstrecken; Geschoss, Lage, Neben- und Kellerräume gehören in den Antrag.
- **Räumungsantrag ohne Zahlungsantrag** — die laufende Nutzungsentschädigung nach § 546a BGB wird nicht tituliert und muss später erneut eingeklagt werden.
- **§ 940a ZPO überschätzt** — der Eilrechtsschutz gegen Wohnraummieter ist auf drei enge Fälle beschränkt; ein Antrag außerhalb davon ist von vornherein aussichtslos.
- **Räumungsfrist unterschätzt** — § 721 ZPO erlaubt bis zu einem Jahr; das ist in der Fristen- und Kostenplanung abzubilden.
- **Berliner Räumung ohne Prüfung gewählt** — sie senkt den Vorschuss, verlagert aber Verwahrungs- und Verwertungspflichten samt Haftung auf den Gläubiger.
- **Widerspruch nach §§ 574 ff. BGB übersehen** — ein durchgreifender Härtefall führt zur Fortsetzung des Mietverhältnisses trotz wirksamer Kündigung.
- **Schonfristzahlung im laufenden Prozess** — sie erledigt nur die fristlose Kündigung; auf die hilfsweise ordentliche Kündigung ist rechtzeitig umzustellen.
