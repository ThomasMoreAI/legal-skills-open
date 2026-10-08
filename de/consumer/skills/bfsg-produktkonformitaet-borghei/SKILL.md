---
name: bfsg-produktkonformitaet-borghei
title: /barrierefreiheit-bfsg:bfsg-produktkonformitaet
description: Produktkonformität nach dem BFSG – Herstellerpflichten § 6 mit technischer Dokumentation nach Anlage 2, Konformitätsbewertungsverfahren, EU-Konformitätserklärung § 18 und CE-Kennzeichnung § 19, Kennzeichnungs- und Informationspflichten § 7, Bevollmächtigter § 8, Einführerpflichten §§ 9, 10, Händlerpflichten § 11, Rollenwechsel § 12, Wirtschaftsakteursangabe § 13, Konformitätsvermutung durch harmonisierte Normen § 4 und technische Spezifikationen § 5, Ausnahmen §§ 16, 17 nebst Anlage 4, Marktüberwachung §§ 20–27 mit Anhörungsfrist von mindestens zehn Tagen nach § 22 Abs. 2 sowie Bußgelder bis 100.000 EUR nach § 37. Use when ein erfasstes Produkt in Verkehr gebracht, eingeführt oder vertrieben wird oder eine Marktüberwachungsbehörde beanstandet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/barrierefreiheit-bfsg/skills/bfsg-produktkonformitaet
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /barrierefreiheit-bfsg:bfsg-produktkonformitaet

## Zweck

Der Skill führt die Produktseite des BFSG von der Konformitätsplanung bis zur behördlichen Beanstandung. Er ordnet dem Mandanten seine Rolle in der Lieferkette zu, arbeitet die jeweiligen Pflichtenkataloge ab, prüft die beiden Ausnahmetatbestände in ihrer richtigen Reihenfolge und entwirft die Reaktion auf ein Marktüberwachungsverfahren.

## Eingaben

- Produkt und Zuordnung zum Katalog des § 1 Abs. 2 BFSG
- Rolle: Hersteller, Bevollmächtigter, Einführer, Händler — und ob eine Rolle nach § 12 BFSG wechselt
- Datum des Inverkehrbringens; bei Serienfertigung: Änderungen an Entwurf oder Merkmalen
- Vorhandene technische Dokumentation, EU-Konformitätserklärung, CE-Kennzeichnung
- Herangezogene harmonisierte Normen oder technische Spezifikationen
- Etwaige Beurteilungen nach § 16 (grundlegende Veränderung) oder § 17 (unverhältnismäßige Belastung)
- Bei behördlichem Verfahren: Schreiben der Marktüberwachungsbehörde, Fristsetzung, Anhörung

## Sub-Agent-Architektur

Der Researcher beschafft BFSG, BFSGV, Anlagen 1 bis 4, die Richtlinie (EU) 2019/882 samt Anhang I, die VO (EU) 2019/1020 und die von der Bundesfachstelle für Barrierefreiheit nach § 3 Abs. 2 BFSGV veröffentlichten Standards und Konformitätstabellen. Der Drafter erstellt die Pflichtenmatrix und den Entwurf gegenüber der Behörde. Der Reviewer prüft die Vollständigkeit der Dokumentation, die Reihenfolge der Ausnahmeprüfung und die Einhaltung der Anhörungsfrist.

## Ablauf

### 1. Rolle in der Lieferkette bestimmen (§§ 6 bis 13 BFSG)

| Rolle | Kernpflichten |
|---|---|
| **Hersteller** ([§ 6](https://www.gesetze-im-internet.de/bfsg/__6.html)) | barrierefreie Gestaltung und Herstellung; technische Dokumentation nach Anlage 2; Konformitätsbewertungsverfahren; EU-Konformitätserklärung § 18; CE-Kennzeichnung § 19; fünf Jahre Aufbewahrung; Serienkonformität; Korrekturmaßnahmen, Rücknahme oder Rückruf nebst Behördeninformation |
| **Bevollmächtigter** ([§ 8](https://www.gesetze-im-internet.de/bfsg/__8.html)) | schriftliches Mandat; Aufbewahrung und Vorlage der Unterlagen; Zusammenarbeit mit der Behörde |
| **Einführer** ([§ 9 BFSG](https://www.gesetze-im-internet.de/bfsg/__9.html), [§ 10](https://www.gesetze-im-internet.de/bfsg/__10.html)) | Inverkehrbringen nur konformer Produkte; Prüfung von Verfahren, Dokumentation und Kennzeichnung; eigene Kennzeichnungs- und Informationspflichten; Korrekturmaßnahmen |
| **Händler** ([§ 11](https://www.gesetze-im-internet.de/bfsg/__11.html)) | Sorgfalt bei der Bereitstellung; Prüfung von CE-Kennzeichnung und Begleitunterlagen; keine Bereitstellung bei Kenntnis der Nichtkonformität; Korrekturmaßnahmen |
| **Rollenwechsel** ([§ 12](https://www.gesetze-im-internet.de/bfsg/__12.html)) | Einführer oder Händler gilt als **Hersteller**, wenn er ein Produkt unter eigenem Namen oder eigener Marke in Verkehr bringt oder ein bereits in Verkehr gebrachtes Produkt so verändert, dass die Konformität beeinträchtigt sein kann |

Nach [§ 13 BFSG](https://www.gesetze-im-internet.de/bfsg/__13.html) hat jeder Wirtschaftsakteur der Behörde auf Verlangen die vor- und nachgelagerten Wirtschaftsakteure zu benennen. Die Pflicht ist bußgeldbewehrt (§ 37 Abs. 1 Nr. 6 BFSG).

**§ 12 ist die praktisch wichtigste Falle:** Der Handel mit Eigenmarken macht den Händler zum Hersteller mit voller Dokumentations-, Erklärungs- und Kennzeichnungslast.

### 2. Barrierefreiheitsanforderungen bestimmen (§ 3 BFSG, BFSGV)

§ 3 Abs. 1 BFSG verlangt, dass Produkte barrierefrei sind — auffindbar, zugänglich und nutzbar für Menschen mit Behinderungen in der allgemein üblichen Weise, ohne besondere Erschwernis und grundsätzlich ohne fremde Hilfe. Die **konkreten** Anforderungen stehen in der [BFSGV](https://www.gesetze-im-internet.de/bfsgv/):

- [§ 4 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__4.html) — Bereitstellung von Informationen für Produkte
- [§ 5 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__5.html) — Produktverpackungen und Anleitungen
- [§ 6 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__6.html) — Benutzerschnittstelle und Funktionalität
- §§ 7 bis 10 BFSGV — branchenspezifische Anforderungen an Selbstbedienungsterminals, E-Book-Lesegeräte und Verbraucherendgeräte
- [§ 11 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__11.html) — Unterstützungsdienste
- §§ 20, 21 BFSGV — funktionale Leistungskriterien

Nach [§ 3 BFSGV](https://www.gesetze-im-internet.de/bfsgv/__3.html) ist der **Stand der Technik** zu beachten; Abweichung ist zulässig, wenn die Anforderungen auf andere Weise in gleichem Maße erfüllt werden. Die **Bundesfachstelle für Barrierefreiheit** veröffentlicht dazu Standardauflistungen und Konformitätstabellen (§ 3 Abs. 2 BFSGV) — sie sind der praktische Einstieg, aber keine Rechtsnorm.

### 3. Konformitätsvermutung nutzen (§§ 4, 5 BFSG)

- [§ 4 BFSG](https://www.gesetze-im-internet.de/bfsg/__4.html) — Konformitätsvermutung bei Übereinstimmung mit **harmonisierten Normen** oder Teilen davon, deren Fundstellen im Amtsblatt der EU veröffentlicht sind. Für digitale Elemente ist **EN 301 549** die einschlägige Referenz `[unverifiziert – prüfen]` hinsichtlich des jeweils im Amtsblatt gelisteten Fassungsstands.
- [§ 5 BFSG](https://www.gesetze-im-internet.de/bfsg/__5.html) — Konformitätsvermutung bei Übereinstimmung mit **technischen Spezifikationen** der Kommission, soweit harmonisierte Normen fehlen.

Die Vermutung reicht nur so weit, wie die Norm die Anforderung abdeckt. Ein pauschaler Verweis auf „EN 301 549" ohne Abgleich mit der konkreten Anforderung trägt nicht.

### 4. Konformitätsbewertung, Erklärung und Kennzeichnung (§§ 6, 18, 19 BFSG)

1. **Technische Dokumentation nach Anlage 2** erstellen und das dort vorgesehene Konformitätsbewertungsverfahren durchführen. Ein Prüfverfahren durch eine benannte Stelle ist nicht vorgesehen; die Konformitätsbewertung erfolgt in Eigenverantwortung des Herstellers.
2. **EU-Konformitätserklärung** nach [§ 18 BFSG](https://www.gesetze-im-internet.de/bfsg/__18.html) ausstellen: Aufbau nach dem Muster in Anhang III des Beschlusses Nr. 768/2008/EG, Elemente nach Anlage 2, **in deutscher Sprache**, auf dem neuesten Stand gehalten. Wurde von § 16 oder § 17 Gebrauch gemacht, muss die Erklärung **ausweisen, welche Anforderungen davon betroffen sind** (§ 18 Abs. 2 S. 2). Bei mehreren einschlägigen Unionsrechtsakten ist eine **einzige** Erklärung auszustellen (§ 18 Abs. 4).
3. **CE-Kennzeichnung** nach [§ 19 BFSG](https://www.gesetze-im-internet.de/bfsg/__19.html) anbringen: deutlich sichtbar, gut lesbar und dauerhaft auf dem Produkt oder der Datenplakette, sonst auf Verpackung und Begleitunterlagen; im Übrigen gelten die Grundsätze des Art. 30 VO (EG) Nr. 765/2008.
4. **Aufbewahrung** von Dokumentation und Erklärung **fünf Jahre** ab Inverkehrbringen (§ 6 Abs. 2 BFSG).
5. **Serienkonformität** durch geeignete Verfahren sicherstellen; Änderungen an Entwurf, Merkmalen oder an den herangezogenen Normen sind zu berücksichtigen (§ 6 Abs. 3 BFSG).

### 5. Ausnahmen in der richtigen Reihenfolge prüfen (§§ 16, 17 BFSG)

**Zuerst § 16 (grundlegende Veränderung), dann § 17 (unverhältnismäßige Belastung)** — beide sind Ausnahmen vom Umfang der Anforderungen, nicht vom Anwendungsbereich.

| | [§ 16 BFSG](https://www.gesetze-im-internet.de/bfsg/__16.html) | [§ 17 BFSG](https://www.gesetze-im-internet.de/bfsg/__17.html) |
|---|---|---|
| Tatbestand | Einhaltung erfordert eine wesentliche Änderung, die zu einer **grundlegenden Veränderung der Wesensmerkmale** führt | Einhaltung führt zu einer **unverhältnismäßigen Belastung** nach den Kriterien der **Anlage 4** |
| Beurteilung | durch den Wirtschaftsakteur selbst | durch den Wirtschaftsakteur selbst |
| Dokumentation | fünf Jahre ab letzter Bereitstellung bzw. Erbringung; Vorlage auf Verlangen | fünf Jahre; Vorlage auf Verlangen |
| Mitteilung | unverzüglich an die Marktüberwachungsbehörden aller betroffenen Mitgliedstaaten | unverzüglich an die zuständige Behörde |
| Erleichterung | Abs. 2 S. 1 und Abs. 3 gelten nicht für **Kleinstunternehmen, die mit Produkten befasst sind**; sie übermitteln auf Verlangen die maßgeblichen Fakten | Abs. 2 S. 1, 2 und Abs. 5 gelten nicht für Kleinstunternehmen, die mit Produkten befasst sind |
| Sperre | — | **§ 17 Abs. 4**: Wer für die Verbesserung der Barrierefreiheit **nichteigene öffentliche oder private Mittel** erhält, darf sich **nicht** auf die unverhältnismäßige Belastung berufen |

Für Dienstleistungserbringer ist die Beurteilung nach § 17 Abs. 3 BFSG **mindestens alle fünf Jahre** und stets bei Änderung der Dienstleistung oder auf behördliche Aufforderung zu wiederholen.

### 6. Marktüberwachungsverfahren führen (§§ 20 bis 27 BFSG)

- **Zuständigkeit** ([§ 20 BFSG](https://www.gesetze-im-internet.de/bfsg/__20.html)): Marktüberwachungsbehörden der **Länder** nach der gemeinsamen Marktüberwachungsstrategie.
- **Befugnisse** ([§ 21 BFSG](https://www.gesetze-im-internet.de/bfsg/__21.html)): entsprechend Art. 14 Abs. 4 Buchst. a, b, e, j VO (EU) 2019/1020; Betretensrechte nur zu den üblichen Betriebs- und Geschäftszeiten. Bei Berufung auf §§ 16, 17 prüft die Behörde, ob die Beurteilung durchgeführt wurde, ob die Kriterien der Anlage 4 ordnungsgemäß angewandt wurden und ob die übrigen Anforderungen eingehalten sind (§ 21 Abs. 3).
- **Verfahren bei Nichtkonformität** ([§ 22 BFSG](https://www.gesetze-im-internet.de/bfsg/__22.html)): Aufforderung zur Herstellung der Konformität innerhalb angemessener Frist; die **Anhörungsfrist nach § 28 VwVfG bzw. den Landesparallelvorschriften darf nicht weniger als zehn Tage betragen** (§ 22 Abs. 2 S. 2). Die Maßnahmen müssen sich auf **alle** unionsweit bereitgestellten betroffenen Produkte erstrecken (§ 22 Abs. 3). Bleibt der Wirtschaftsakteur untätig, folgen Beschränkung, Untersagung, Rücknahme oder Rückruf (§ 22 Abs. 4).
- **Formale Nichtkonformität** ([§ 23 BFSG](https://www.gesetze-im-internet.de/bfsg/__23.html)): fehlende oder fehlerhafte CE-Kennzeichnung, fehlende Erklärung oder Dokumentation.
- **Rechtsschutz**: Widerspruch und Anfechtungsklage nach §§ 68 ff., 42 VwGO; bei Anordnung des Sofortvollzugs Antrag nach § 80 Abs. 5 VwGO (`/verwaltungsrecht:vorlaeufiger-rechtsschutz-80`).

### 7. Bußgeldrisiko einordnen ([§ 37 BFSG](https://www.gesetze-im-internet.de/bfsg/__37.html))

| Tatbestand | Rahmen |
|---|---|
| § 37 Abs. 1 Nr. 1 (Inverkehrbringen nicht konformer Produkte), Nr. 7 (Bereitstellung durch den Händler), Nr. 8 (Erbringen nicht konformer Dienstleistungen), Nr. 9 und Nr. 10 (CE-Kennzeichnung) | bis **100.000 EUR** |
| übrige Fälle, insbesondere Informations-, Kennzeichnungs- und Auskunftspflichtverletzungen | bis **10.000 EUR** |

Ordnungswidrig handelt, wer vorsätzlich **oder fahrlässig** handelt.

## Deterministische Berechnung

Zu rechnen sind die Aufbewahrungsfrist des § 6 Abs. 2 BFSG, der Fünfjahresrhythmus der Beurteilungen nach §§ 16, 17 und die behördliche Anhörungsfrist. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Aufbewahrung § 6 Abs. 2 BFSG: 5 Jahre ab Inverkehrbringen am 01.10.2026
python -m scripts.legal_calc.cli frist --ereignis 01.10.2026 --menge 5 --einheit jahre --land BY

# Anhörung § 22 Abs. 2 S. 2 BFSG: mindestens 10 Tage ab Zugang am 12.03.2026
python -m scripts.legal_calc.cli frist --ereignis 12.03.2026 --menge 10 --einheit tage --land BY

# Widerspruchsfrist § 70 VwGO: 1 Monat ab Bekanntgabe
python -m scripts.legal_calc.cli frist --ereignis 20.04.2026 --menge 1 --einheit monate --land BY
```

## Quellen

### Statute

- [§ 3 BFSG](https://www.gesetze-im-internet.de/bfsg/__3.html), [§ 4](https://www.gesetze-im-internet.de/bfsg/__4.html), [§ 5](https://www.gesetze-im-internet.de/bfsg/__5.html), [§ 6](https://www.gesetze-im-internet.de/bfsg/__6.html), [§ 7](https://www.gesetze-im-internet.de/bfsg/__7.html), [§ 8](https://www.gesetze-im-internet.de/bfsg/__8.html), [§ 9](https://www.gesetze-im-internet.de/bfsg/__9.html), [§ 10](https://www.gesetze-im-internet.de/bfsg/__10.html), [§ 11](https://www.gesetze-im-internet.de/bfsg/__11.html), [§ 12](https://www.gesetze-im-internet.de/bfsg/__12.html), [§ 13](https://www.gesetze-im-internet.de/bfsg/__13.html), [§ 16](https://www.gesetze-im-internet.de/bfsg/__16.html), [§ 17](https://www.gesetze-im-internet.de/bfsg/__17.html), [§ 18](https://www.gesetze-im-internet.de/bfsg/__18.html), [§ 19](https://www.gesetze-im-internet.de/bfsg/__19.html), [§ 20](https://www.gesetze-im-internet.de/bfsg/__20.html), [§ 21](https://www.gesetze-im-internet.de/bfsg/__21.html), [§ 22](https://www.gesetze-im-internet.de/bfsg/__22.html), [§ 23](https://www.gesetze-im-internet.de/bfsg/__23.html), [§ 37](https://www.gesetze-im-internet.de/bfsg/__37.html); Anlagen 1 bis 4
- [BFSGV §§ 3 bis 11, 20, 21](https://www.gesetze-im-internet.de/bfsgv/)
- Richtlinie (EU) 2019/882, Anhang I und VI — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/882/oj)
- Verordnung (EU) 2019/1020 (Marktüberwachung), Art. 14, 16, 17, 22 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2019/1020/oj)
- Verordnung (EG) Nr. 765/2008, Art. 30; Beschluss Nr. 768/2008/EG, Anhang III
- [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html)

### Kommentare und Literatur

- Ritgen/Sellmann, BFSG, Kommentar, §§ 6, 16, 17, 22.
- Dörr/Natlacen, Barrierefreiheitsstärkungsgesetz, Praxishandbuch, Kap. Produktkonformität.
- Klindt, Produktsicherheitsrecht (zur Systematik des New Legislative Framework und zur CE-Kennzeichnung).
- Bundesfachstelle für Barrierefreiheit, Konformitätstabellen nach § 3 Abs. 2 BFSGV.

### Rechtsprechung

Zum BFSG liegt bislang keine gefestigte Rechtsprechung vor. Für Marktüberwachungsmaßnahmen ist auf die Judikatur zum ProdSG und zur VO (EU) 2019/1020 zurückzugreifen; jede Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
BFSG-PRODUKTKONFORMITÄT — <Produkt> — <Datum>

I.   Einordnung
     Produktkategorie § 1 Abs. 2: <Nr. …>
     Inverkehrbringen:            <Datum>
     Rolle:                       <Hersteller / Einführer / Händler / Bevollmächtigter>
     Rollenwechsel § 12:          [ja — Herstellerpflichten / nein]

II.  Anforderungen
     Einschlägige BFSGV-Normen:   <§§ …>
     Herangezogene harmonisierte Norm: <…>  Vermutungswirkung § 4: [ja / teilweise]
     Stand der Technik § 3 BFSGV: <…>

III. Konformitätsnachweis
     Technische Dokumentation Anlage 2: [vollständig / Lücken: …]
     Konformitätsbewertungsverfahren:   [durchgeführt / offen]
     EU-Konformitätserklärung § 18:     [vorhanden / fehlt]  Sprache: <…>
       Ausnahmen ausgewiesen (Abs. 2 S. 2): [ja / nein]
     CE-Kennzeichnung § 19:             [angebracht / fehlt / fehlerhaft]
     Aufbewahrung 5 Jahre bis:          <Datum>

IV.  Ausnahmen
     § 16 grundlegende Veränderung: [geprüft — Ergebnis / nicht geprüft]
     § 17 unverhältnismäßige Belastung nach Anlage 4: [geprüft — Ergebnis / nicht geprüft]
     Fördermittel erhalten (§ 17 Abs. 4): [ja — Berufung gesperrt / nein]
     Mitteilung an die Behörde:      [erfolgt am <Datum> / offen]

V.   Marktüberwachung
     Behörde:                     <Land>
     Verfahrensstand:             <…>
     Anhörungsfrist § 22 Abs. 2 S. 2: mindestens 10 Tage, endet am <Datum>
     Reichweite der Maßnahmen § 22 Abs. 3: <unionsweit betroffene Produkte>
     Rechtsschutz:                <Widerspruch bis <Datum> / § 80 Abs. 5 VwGO>

VI.  Bußgeldrisiko § 37
     Tatbestand:                  <…>   Rahmen: <100.000 EUR / 10.000 EUR>

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Rollenwechsel nach § 12 BFSG übersehen.** Eigenmarkenvertrieb macht Händler und Einführer zum Hersteller — mit voller Dokumentations-, Erklärungs- und Kennzeichnungslast.
- **Ausnahmen in falscher Reihenfolge oder als Bereichsausnahme geprüft.** §§ 16, 17 BFSG begrenzen den Umfang der Anforderungen, nicht den Anwendungsbereich; sie setzen eine dokumentierte Beurteilung und eine Mitteilung an die Behörde voraus.
- **§ 17 trotz Fördermitteln geltend gemacht.** § 17 Abs. 4 BFSG sperrt die Berufung, wenn nichteigene öffentliche oder private Mittel für die Barrierefreiheit bezogen wurden.
- **Konformitätserklärung ohne Ausweis der Ausnahmen.** § 18 Abs. 2 S. 2 BFSG verlangt die Angabe, welche Anforderungen betroffen sind.
- **Pauschalverweis auf EN 301 549.** Die Vermutungswirkung des § 4 BFSG reicht nur so weit, wie die im Amtsblatt gelistete Norm die konkrete Anforderung abdeckt.
- **Anhörungsfrist unter zehn Tagen akzeptiert.** § 22 Abs. 2 S. 2 BFSG setzt eine Untergrenze.
- **Korrekturmaßnahmen auf den deutschen Markt beschränkt.** § 22 Abs. 3 BFSG verlangt die Erstreckung auf alle unionsweit bereitgestellten Produkte.
- **Aufbewahrungsfrist versäumt.** Dokumentation und Erklärung sind fünf Jahre ab Inverkehrbringen vorzuhalten.
- **Rechtsprechung erfunden.** Zum BFSG existiert kaum Judikatur; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
