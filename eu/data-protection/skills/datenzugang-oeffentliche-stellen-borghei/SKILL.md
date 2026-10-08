---
name: datenzugang-oeffentliche-stellen-borghei
title: /datenwirtschaftsrecht:datenzugang-oeffentliche-stellen
description: Datenzugang öffentlicher Stellen und Datenintermediäre – Bereitstellungspflicht wegen außergewöhnlicher Notwendigkeit Art. 14 Data Act, enge Voraussetzungen Art. 15 mit Bereichsausnahme für Kleinst- und Kleinunternehmen Art. 15 Abs. 2, Anforderungen an das Verlangen Art. 17, Erfüllung und Ablehnung Art. 18 mit 5 Arbeitstagen im öffentlichen Notstand und 30 Arbeitstagen im Übrigen, Zweckbindung und Löschpflicht der Behörde Art. 19, Ausgleich Art. 20 (unentgeltlich im Notstand, faire Gegenleistung mit Marge im Übrigen), Weitergabe an Forschung Art. 21; daneben Datenvermittlungsdienste und Datenaltruismus nach der VO (EU) 2022/868 und dem DGG. Use when eine Behörde Unternehmensdaten anfordert oder ein Datenintermediär bzw. eine altruistische Organisation registriert werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenwirtschaftsrecht/skills/datenzugang-oeffentliche-stellen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: de
---

# /datenwirtschaftsrecht:datenzugang-oeffentliche-stellen

## Zweck

Der Skill bearbeitet die B2G-Seite der Datenwirtschaft: Er prüft ein behördliches Datenverlangen an den engen Voraussetzungen des Art. 15, arbeitet die Formanforderungen des Art. 17 ab, bestimmt die Ablehnungsgründe und -fristen des Art. 18 und rechnet den Ausgleichsanspruch nach Art. 20. Ergänzend ordnet er Datenvermittlungsdienste und Datenaltruismus dem Regime des Daten-Governance-Rechtsakts und des DGG zu.

## Eingaben

- Wortlaut des behördlichen Verlangens mit Datum des Eingangs
- Anfragende Stelle und die Rechtsvorschrift, die ihr die Aufgabe zuweist
- Behauptete Notwendigkeit: öffentlicher Notstand oder sonstiger Fall
- Datenkatalog: welche Daten verlangt werden, ob personenbezogen, ob Geschäftsgeheimnisse enthalten
- Größenklasse des Dateninhabers nach Empfehlung 2003/361/EG
- Ob dieselben Daten bereits an eine andere Stelle geliefert wurden
- Bei Intermediären: Geschäftsmodell, Trennung der Vermittlungstätigkeit, Registrierungsstand

## Sub-Agent-Architektur

Der Researcher beschafft Normtext, Erwägungsgründe, das DADG und das DGG sowie die Registerpraxis der Bundesnetzagentur. Der Drafter prüft das Verlangen Punkt für Punkt gegen Art. 17 Abs. 1 Buchst. a bis j und entwirft Erfüllung, Änderungsantrag oder Ablehnung. Der Reviewer kontrolliert die Fristen des Art. 18 Abs. 2, die Anonymisierungspflicht des Art. 18 Abs. 4 und die Ausgleichsberechnung nach Art. 20; er verhindert insbesondere, dass ein Notstandsverlangen und ein Regelverlangen gleich behandelt werden.

## Ablauf

### 1. Verlangen einordnen (Art. 14, Art. 15)

Nach Art. 14 besteht die Bereitstellungspflicht nur, wenn die anfragende Stelle die **außergewöhnliche Notwendigkeit** nach Art. 15 **nachweist**. Zwei Fallgruppen:

| Fallgruppe | Voraussetzungen |
|---|---|
| **Art. 15 Abs. 1 Buchst. a** — öffentlicher Notstand | Die Daten sind zur Bewältigung erforderlich **und** die Stelle kann sie unter gleichwertigen Bedingungen nicht rechtzeitig und wirksam anderweitig beschaffen |
| **Art. 15 Abs. 1 Buchst. b** — sonstige Fälle, **nur nicht personenbezogene Daten** | (i) Die Stelle wird auf Grundlage von Unionsrecht oder nationalem Recht tätig und hat spezifische Daten ermittelt, deren Fehlen sie an der Erfüllung einer **rechtlich ausdrücklich vorgesehenen** Aufgabe im öffentlichen Interesse hindert, und (ii) sie hat **alle anderen Mittel ausgeschöpft** — einschließlich des Erwerbs zu Markttarifen, der Inanspruchnahme bestehender Bereitstellungspflichten und des Erlasses neuer Rechtsvorschriften |

Zwei Begrenzungen, die in der Verteidigung an erster Stelle stehen:

- Die außergewöhnliche Notwendigkeit ist **zeitlich befristet und im Umfang begrenzt** (Art. 15 Abs. 1 Halbs. 1).
- **Art. 15 Abs. 2**: Die Fallgruppe des Buchst. b gilt **nicht für Kleinst- und Kleinunternehmen**. Ein solches Unternehmen ist nur im echten Notstandsfall verpflichtet.

Die **Nachweislast** für das Vorliegen der Voraussetzungen trägt die anfragende Stelle (Art. 15 Abs. 3).

### 2. Formanforderungen des Verlangens prüfen (Art. 17)

Das Verlangen muss schriftlich, klar, prägnant, einfach und für den Dateninhaber verständlich abgefasst sein (Art. 17 Abs. 2) und nach Art. 17 Abs. 1 enthalten:

| Buchst. | Erforderliche Angabe |
|---|---|
| a | welche Daten und Metadaten benötigt werden |
| b | Nachweis der Voraussetzungen des Art. 15 |
| c | Zweck, beabsichtigte Nutzung, Dauer der Nutzung, ggf. Umgang mit personenbezogenen Daten |
| d | nach Möglichkeit der voraussichtliche Löschzeitpunkt bei allen Zugangsberechtigten |
| e | Begründung der Auswahl gerade dieses Dateninhabers |
| f | alle weiteren Stellen und Dritten, an die weitergegeben werden soll |
| g | bei personenbezogenen Daten: technische und organisatorische Maßnahmen, etwa Pseudonymisierung, und ob der Dateninhaber vorher anonymisieren kann |
| h | die Rechtsvorschrift, die der Stelle die Aufgabe zuweist |
| i | die Frist zur Bereitstellung sowie die Frist des Art. 18 Abs. 2 für Ablehnung oder Änderungsantrag |
| j | Bemühen, eine Haftung des Dateninhabers wegen Verstoßes gegen Unionsrecht oder nationales Recht zu vermeiden |

Fehlt eine dieser Angaben, ist das Verlangen nach **Art. 18 Abs. 2 Buchst. c** ablehnungsfähig. Die Prüfung ist buchstabenweise zu dokumentieren.

### 3. Erfüllen, ändern oder ablehnen (Art. 18)

Grundsatz: Bereitstellung **unverzüglich** unter Berücksichtigung der erforderlichen technischen, organisatorischen und rechtlichen Maßnahmen (Art. 18 Abs. 1).

**Fristen für Ablehnung oder Änderungsantrag (Art. 18 Abs. 2):**

| Fall | Frist ab Eingang |
|---|---|
| Daten zur Bewältigung eines öffentlichen Notstands | unverzüglich, jedenfalls binnen **5 Arbeitstagen** |
| sonstige außergewöhnliche Notwendigkeit | unverzüglich, jedenfalls binnen **30 Arbeitstagen** |

**Ablehnungsgründe (abschließend):**

- a) der Dateninhaber hat **keine Kontrolle** über die verlangten Daten;
- b) ein **ähnliches Verlangen zu demselben Zweck** wurde bereits von einer anderen Stelle gestellt und über die Löschung nach Art. 19 Abs. 1 Buchst. c wurde nicht unterrichtet — in diesem Fall ist die zuvor anfragende Stelle zu benennen (Art. 18 Abs. 3);
- c) das Verlangen **erfüllt die Voraussetzungen des Art. 17 Abs. 1 und 2 nicht**.

**Art. 18 Abs. 4**: Enthalten die verlangten Daten personenbezogene Daten, sind sie vom Dateninhaber **ordnungsgemäß zu anonymisieren**, es sei denn, die Erfüllung erfordert gerade die Offenlegung personenbezogener Daten. Die Anonymisierung ist der Regelfall, nicht die Ausnahme.

### 4. Pflichten der empfangenden Stelle prüfen (Art. 19)

Die Behörde darf die Daten nicht zweckwidrig nutzen, muss technische und organisatorische Maßnahmen zur Wahrung von Vertraulichkeit, Integrität und Übermittlungssicherheit getroffen haben und die Daten **löschen**, sobald sie für den angegebenen Zweck nicht mehr erforderlich sind; die Löschung ist dem Dateninhaber unverzüglich mitzuteilen (Art. 19 Abs. 1).

**Art. 19 Abs. 2** verbietet ihr und Dritten, die Daten oder daraus gewonnene Erkenntnisse über wirtschaftliche Lage, Vermögenswerte oder Produktions- und Betriebsmethoden zu nutzen, um ein **konkurrierendes** vernetztes Produkt oder einen konkurrierenden verbundenen Dienst zu entwickeln oder zu verbessern, oder sie hierzu weiterzugeben.

**Art. 19 Abs. 3**: Geschäftsgeheimnisse sind nur offenzulegen, soweit dies für den Zweck des Verlangens **unerlässlich** ist; der Geheimnisinhaber kennzeichnet sie und kann Schutzmaßnahmen verlangen.

### 5. Ausgleich berechnen (Art. 20)

| Fall | Ausgleich |
|---|---|
| Öffentlicher Notstand, Art. 15 Abs. 1 Buchst. a, Dateninhaber ist **kein** Kleinst- oder Kleinunternehmen | **unentgeltlich**; auf Ersuchen öffentliche Anerkennung des Beitrags |
| Sonstige Fälle, Art. 15 Abs. 1 Buchst. b | **faire Gegenleistung**, die mindestens die technischen und organisatorischen Kosten deckt — gegebenenfalls einschließlich der Kosten für Anonymisierung, Pseudonymisierung, Aggregation und technische Anpassung — **zuzüglich einer angemessenen Marge** |

Auf Verlangen der Stelle sind die Berechnungsgrundlagen offenzulegen. Kleinst- und Kleinunternehmen sind auch im Notstandsfall nicht auf die Unentgeltlichkeit festgelegt.

### 6. Weitergabe an Forschung (Art. 21)

Die empfangende Stelle darf die Daten unter den Voraussetzungen des Art. 21 an Einzelpersonen oder Organisationen weitergeben, die wissenschaftliche Forschung oder Analytik im Einklang mit dem Zweck des Verlangens betreiben, oder an amtliche Statistikstellen. Die Empfänger handeln gemeinnützig oder im Rahmen einer im Unionsrecht oder nationalen Recht anerkannten Aufgabe im öffentlichen Interesse; die Weitergabe ist dem Dateninhaber mitzuteilen. Nach [§ 2 Abs. 2 Nr. 7 DADG](https://www.gesetze-im-internet.de/dadg/__2.html) fördert die Bundesnetzagentur diese Weitergabe.

### 7. Datenvermittlungsdienste und Datenaltruismus (VO (EU) 2022/868, DGG)

Der **Daten-Governance-Rechtsakt** regelt daneben:

- **Kapitel II** — Weiterverwendung geschützter Daten öffentlicher Stellen (Daten, die Geschäftsgeheimnissen, dem Statistikgeheimnis, Rechten Dritter oder dem Datenschutz unterliegen). Abzugrenzen vom Open-Data-Regime des [DNG](https://www.gesetze-im-internet.de/dng/).
- **Kapitel III** — **Datenvermittlungsdienste**: Anzeigepflicht, strenge Neutralitäts- und Trennungsanforderungen; die Vermittlungstätigkeit darf nicht mit eigener Datennutzung vermischt werden. Durchsetzung nach [§ 7 DGG](https://www.gesetze-im-internet.de/dgg/__7.html).
- **Kapitel IV** — **Datenaltruismus**: Eintragung als anerkannte datenaltruistische Organisation, Transparenz- und Berichtspflichten. Durchsetzung nach [§ 8 DGG](https://www.gesetze-im-internet.de/dgg/__8.html).

Zuständig ist auch hier die **Bundesnetzagentur** ([§ 2 DGG](https://www.gesetze-im-internet.de/dgg/__2.html)); Bußgelder folgen aus [§ 10 DGG](https://www.gesetze-im-internet.de/dgg/__10.html).

## Deterministische Berechnung

Die Fristen des Art. 18 Abs. 2 sind **Arbeitstagsfristen** und werden nach der VO (EWG, Euratom) Nr. 1182/71 berechnet: Der Tag des Eingangs zählt nicht mit (Art. 3 Abs. 1), Samstage, Sonntage und Feiertage sind keine Arbeitstage (Art. 2 Abs. 2). Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) kennt **keine** Einheit „Arbeitstage"; er liefert die Feiertage des jeweiligen Landes, die Arbeitstage sind anhand dieser Liste von Hand auszuzählen:

```bash
# Grundlage für die Auszählung von 5 (Notstand) bzw. 30 (Regelfall) Arbeitstagen
# ab Eingang des Verlangens am 09.03.2026 in Bayern
python -m scripts.legal_calc.cli feiertage --jahr 2026 --land BY
```

`--json` liefert die Feiertagsliste maschinenlesbar. Ob ein „öffentlicher Notstand" vorliegt, ist eine juristische Wertung und gesondert zu begründen.

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/2854, Art. 14, 15, 16, 17, 18, 19, 20, 21, 22, 38, 50 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- [§ 2 DADG](https://www.gesetze-im-internet.de/dadg/__2.html), [§ 6 DADG](https://www.gesetze-im-internet.de/dadg/__6.html), [§ 15 DADG](https://www.gesetze-im-internet.de/dadg/__15.html)
- Verordnung (EU) 2022/868 (Daten-Governance-Rechtsakt), Kapitel II bis IV — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/868/oj)
- [DGG](https://www.gesetze-im-internet.de/dgg/) – [§ 2](https://www.gesetze-im-internet.de/dgg/__2.html), [§ 7](https://www.gesetze-im-internet.de/dgg/__7.html), [§ 8](https://www.gesetze-im-internet.de/dgg/__8.html), [§ 10](https://www.gesetze-im-internet.de/dgg/__10.html)
- [DNG](https://www.gesetze-im-internet.de/dng/) (Nutzung von Daten des öffentlichen Sektors)
- [GeschGehG § 2](https://www.gesetze-im-internet.de/geschgehg/__2.html)

### Kommentare und Literatur

- Hennemann/Steinrötter, Data Act – Handkommentar, Art. 14 ff.
- Specht-Riemenschneider/Hennemann, Data Act, Kommentar, Art. 15, Art. 20.
- Richter, Datenzugang für den Staat, Beiträge in DVBl/ZD 2024/2025 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`
- Zum DGA: Hennemann/von Ditfurth, in: Datenrecht, Kap. Datenvermittlungsdienste.

### Rechtsprechung

Zu Kapitel V des Data Act und zum DGA liegt keine gefestigte Rechtsprechung vor. Für die verwaltungsrechtliche Flankierung – Anhörung, Begründung, Verhältnismäßigkeit – ist auf die allgemeine Rechtsprechung zu §§ 28, 39, 40 VwVfG zurückzugreifen; jede konkrete Entscheidung ist vor Verwendung zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
BEHÖRDLICHES DATENVERLANGEN — <Mandant> — <Datum>

I.   Verlangen
     Eingang:                 <Datum>   Anfragende Stelle: <…>
     Fallgruppe:              [Art. 15 Abs. 1 lit. a Notstand / lit. b Regelfall]
     Größenklasse Mandant:    <…>   Art. 15 Abs. 2 einschlägig: [ja — lit. b entfällt / nein]

II.  Formprüfung Art. 17 Abs. 1
     lit. a … lit. j:         <je Buchstabe: erfüllt / fehlt>
     Sprachform Abs. 2:       [erfüllt / nicht erfüllt]
     Ergebnis:                [vollständig / ablehnungsfähig nach Art. 18 Abs. 2 lit. c]

III. Materielle Prüfung Art. 15
     Erforderlichkeit:        <…>
     Ausschöpfung anderer Mittel (lit. b ii): <…>
     Zeitliche und Umfangsbegrenzung: <…>
     Nachweis durch die Stelle: [geführt / nicht geführt]

IV.  Reaktion und Frist
     Frist Art. 18 Abs. 2:    [5 Arbeitstage bis <Datum> / 30 Arbeitstage bis <Datum>]
     Empfehlung:              [Erfüllung / Änderungsantrag / Ablehnung nach lit. a/b/c]
     Anonymisierung Art. 18 Abs. 4: [geboten / ausnahmsweise entbehrlich — Begründung]
     Geschäftsgeheimnisse:    <Kennzeichnung / Unerlässlichkeit Art. 19 Abs. 3>

V.   Ausgleich Art. 20
     Grundlage:               [unentgeltlich Abs. 1 / faire Gegenleistung Abs. 2]
     Kostenpositionen:        <…>
     Angemessene Marge:       <…>
     Offenlegung der Berechnung: [zugesagt / erfolgt]

VI.  Nachsorge
     Zweckbindung und Löschpflicht der Stelle (Art. 19 Abs. 1)
     Wettbewerbsverbot (Art. 19 Abs. 2)
     Weitergabe an Forschung (Art. 21): [angekündigt / nein]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Änderungsantrag nach Art. 18 Abs. 2 (Gerüst)

```
An <Behörde>
Ihr Datenverlangen vom <Datum>, Az. <…>

Namens und in Vollmacht der <Mandantin> beantragen wir fristgerecht die
Änderung des Verlangens nach Artikel 18 Absatz 2 der Verordnung (EU)
2023/2854 und begründen dies wie folgt:

1. Das Verlangen genügt Artikel 17 Absatz 1 nicht, weil <lit. b / e / h>
   fehlt bzw. unvollständig ist.
2. Eine außergewöhnliche Notwendigkeit nach Artikel 15 Absatz 1
   Buchstabe b ist nicht nachgewiesen; insbesondere ist nicht dargelegt,
   dass alle anderen Mittel einschließlich des Erwerbs zu Markttarifen
   ausgeschöpft wurden.
3. Die verlangten Daten enthalten personenbezogene Daten; nach Artikel 18
   Absatz 4 ist eine Anonymisierung vorzunehmen. Wir bieten die
   Bereitstellung in anonymisierter Form an.
4. Für die Bereitstellung machen wir den Ausgleich nach Artikel 20
   Absatz 2 geltend; die Kostenaufstellung fügen wir bei.
```

## Risiken / typische Fehler

- **Notstands- und Regelfall gleich behandelt.** Fristen (5 gegen 30 Arbeitstage), Datenkategorien (auch personenbezogen gegen nur nicht personenbezogen) und Ausgleich (unentgeltlich gegen faire Gegenleistung mit Marge) unterscheiden sich vollständig.
- **Bereichsausnahme des Art. 15 Abs. 2 übersehen.** Kleinst- und Kleinunternehmen trifft die Fallgruppe des Buchst. b nicht.
- **Formprüfung nach Art. 17 übersprungen.** Ein unvollständiges Verlangen ist nach Art. 18 Abs. 2 Buchst. c ablehnungsfähig — das ist der praktisch wichtigste Verteidigungsansatz.
- **Ablehnungsfrist versäumt.** Nach Ablauf der 5 bzw. 30 Arbeitstage ist die Ablehnung präkludiert; Arbeitstage sind feiertagsabhängig zu rechnen.
- **Personenbezogene Daten ohne Anonymisierung geliefert.** Art. 18 Abs. 4 macht die Anonymisierung zum Regelfall.
- **Ausgleich nicht geltend gemacht.** Im Fall des Art. 15 Abs. 1 Buchst. b besteht ein Anspruch auf faire Gegenleistung einschließlich angemessener Marge.
- **DGA und Data Act vermengt.** Datenvermittlungsdienste und Datenaltruismus folgen der VO (EU) 2022/868 und dem DGG, nicht dem Data Act.
- **Rechtsprechung erfunden.** Zu Kapitel V existiert keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
