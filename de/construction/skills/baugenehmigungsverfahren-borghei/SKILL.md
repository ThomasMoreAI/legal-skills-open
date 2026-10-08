---
name: baugenehmigungsverfahren-borghei
title: /baurecht:baugenehmigungsverfahren
description: 'Prüfung der Baugenehmigung: bauplanungsrechtliche Zulässigkeit (§§ 30–35 BauGB; faktisches Gebiet § 34 II BauGB iVm BauNVO; Außenbereich § 35; Befreiung § 31 II), bauordnungsrechtliche Zulässigkeit (Landes-BauO – Abstandsflächen, Brandschutz, Stellplätze), Einvernehmen der Gemeinde § 36 BauGB, Verfahrensart (volles Verfahren / vereinfachtes Verfahren / Genehmigungsfreistellung), Rechtsbehelfe (Verpflichtungs-/Anfechtungsklage § 42 VwGO, Untätigkeitsklage § 75 VwGO, Bauvoranfrage). Use when ein Bauvorhaben planungs- und ordnungsrechtlich vorgeprüft, ein Bauantrag begleitet oder ein ablehnender Bescheid / fehlendes Einvernehmen angegriffen werden soll.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/baurecht/skills/baugenehmigungsverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: construction
language: de
---

# /baurecht:baugenehmigungsverfahren

## Zweck

Der Skill prüft die Genehmigungsfähigkeit eines Bauvorhabens in beiden Säulen (Bauplanungs- und Bauordnungsrecht), ordnet die Verfahrensart der einschlägigen Landes-BauO zu und bereitet die Rechtsbehelfsstrategie vor (Verpflichtungsklage bei Versagung; Anfechtungsklage gegen belastende Auflagen; § 75 VwGO bei Untätigkeit der Bauaufsicht). Er adressiert ausdrücklich das Einvernehmenserfordernis der Gemeinde (§ 36 BauGB).

## Eingaben

- Bundesland (entscheidend für LBO)
- Lage des Grundstücks (B-Plan vorhanden? Innenbereich? Außenbereich?), Auszug aus B-Plan / FNP
- Vorhaben (Nutzungsart, Maß: GRZ/GFZ/BMZ; Höhe; Anzahl Stellplätze)
- Bisheriger Verfahrensstand (Bauvoranfrage gestellt? Bauantrag eingereicht? Bescheid liegt vor?)
- Position des Mandanten: Bauherr (Vorhabenträger) oder Behörde / Gemeinde
- Fristen (Datum der Antragstellung, Datum eines etwaigen Bescheids)

## Sub-Agent-Architektur

Researcher liefert die einschlägigen §§ BauGB / BauNVO / der jeweiligen LBO, BVerwG 4.-Senat-Rechtsprechung (Einfügen, Rücksichtnahme, Außenbereich) und Kommentarstellen (Battis/Krautzberger/Löhr; Ernst/Zinkahn/Bielenberg; Jäde/Dirnberger; LBO-Kommentar). Drafter prüft im Gutachtenstil die materielle Zulässigkeit, ordnet die Verfahrensart zu und entwirft den Schriftsatz (Verpflichtungs- oder Anfechtungsklage; § 75 VwGO Untätigkeitsklage). Reviewer prüft Frist-Kalender (§§ 74, 75 VwGO), Einvernehmen, drittschützende Normen (wenn Nachbarklage droht) und ordnet Sofortvollzug § 212a BauGB ein.

## Ablauf

### 1. Vorhabenbegriff § 29 BauGB

Vorhaben = Errichtung, Änderung, Nutzungsänderung baulicher Anlagen. Vorprüfung: Liegt überhaupt ein „Vorhaben" im Sinne des § 29 BauGB vor (nicht bei Maßnahmen ohne städtebauliche Relevanz)?

### 2. Bauplanungsrechtliche Zulässigkeit

Verzweigung nach Lage:

**a) Qualifizierter B-Plan (§ 30 I BauGB)**

Zulässig, wenn das Vorhaben den Festsetzungen entspricht. Andernfalls Befreiung § 31 II BauGB (Grundzüge der Planung nicht berührt + öffentliches Interesse / Härte / städtebaulich vertretbar + nachbarliche Interessen).

**b) Faktischer Innenbereich (§ 34 BauGB)**

- § 34 II BauGB: Wenn die nähere Umgebung einem der Baugebiete der BauNVO (§§ 2–11) entspricht, richtet sich die Zulässigkeit der Art der Nutzung allein nach den entsprechenden Vorschriften der BauNVO (faktisches Baugebiet); ergänzend § 15 BauNVO (Gebietsverträglichkeit / Rücksichtnahmegebot).
- § 34 I BauGB: Sonst muss sich das Vorhaben nach Art, Maß, Bauweise und überbaubarer Grundstücksfläche **einfügen** und das Ortsbild nicht beeinträchtigen. Maßstab „Einfügen": BVerwG, Urt. v. 26.05.1978 – 4 C 9.77, BVerwGE 55, 369 (Krabbenkamp) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=26.05.1978&Aktenzeichen=4+C+9.77).
- § 34 I 2 BauGB: Rücksichtnahmegebot („gesunde Wohn- und Arbeitsverhältnisse"; „nicht stören").

**c) Außenbereich (§ 35 BauGB)**

- § 35 I BauGB: **privilegierte Vorhaben** (Landwirtschaft, ortsgebundene gewerbliche Nutzung, öffentliche Versorgung, Windenergie etc.) – zulässig, sofern öffentliche Belange nicht entgegenstehen.
- § 35 II BauGB: **sonstige Vorhaben** – nur zulässig, wenn öffentliche Belange nicht beeinträchtigt werden. § 35 III BauGB konkretisiert die öffentlichen Belange (Flächennutzungsplan-Darstellung, Naturschutz, Außenbereich-Schutz, schädliche Umwelteinwirkungen u. a.).

### 3. Einvernehmen der Gemeinde § 36 BauGB

Bei Vorhaben nach §§ 31, 33, 34, 35 BauGB ist das Einvernehmen der Gemeinde erforderlich. Verweigerung muss aus städtebaulichen Gründen erfolgen; rechtswidrig verweigertes Einvernehmen kann nach Landesrecht **ersetzt** werden. Die Klage geht dann gegen den Landkreis / die Bauaufsicht, nicht gegen die Gemeinde direkt (h.M.; vgl. BVerwG-Rspr. `[unverifiziert]`).

### 4. Bauordnungsrechtliche Zulässigkeit (Landes-BauO)

Je nach Bundesland zu prüfen, idR:

- **Abstandsflächen** (BayBO Art. 6; BauO NRW § 6; LBO BW § 5 etc.) – drittschützend
- **Brandschutz** (LBO-Vorschriften)
- **Standsicherheit** (statische Anforderungen)
- **Stellplatzpflicht** (§ 12 BauNVO + LBO-Stellplatzvorschriften)
- **Erschließung** (Zufahrt, Versorgung)

> **Researcher-Hinweis**: Genauer Paragrafenstand variiert je LBO – Researcher zitiert die im Mandatsfall einschlägige LBO mit Norm und Landesrechts-URL.

### 5. Verfahrensart

Je LBO unterschiedlich, im Grundsatz:

- **Volles Baugenehmigungsverfahren** – umfassende Prüfung
- **Vereinfachtes Verfahren** – beschränkter Prüfungsumfang (idR Bauplanungsrecht + ausgewählte LBO-Vorgaben)
- **Genehmigungsfreistellung** – im Geltungsbereich eines qualifizierten B-Plans bei Wohngebäuden; Bauvorlagen einzureichen, Gemeinde kann ins Verfahren überleiten
- **Bauanzeige / verfahrensfreies Vorhaben** – bestimmte Nebenanlagen, kleine Vorhaben

Bauvoranfrage / Vorbescheid: rechtliches Sicherungsinstrument für einzelne Teilfragen (Bauplanungsrecht und/oder Bauordnungsrecht) vor Vollantrag; Bindungswirkung für die Bauaufsicht idR 3 Jahre (LBO-spezifisch).

### 6. Rechtsbehelfe

| Konstellation | Rechtsbehelf | Frist |
|---|---|---|
| Versagung BauG | **Verpflichtungsklage** § 42 I 2. Alt. VwGO | § 74 II VwGO, 1 Monat ab Bekanntgabe |
| Belastende Auflage einer BauG | **Anfechtungsklage** § 42 I 1. Alt. VwGO | § 74 I VwGO, 1 Monat |
| Bauaufsicht entscheidet nicht | **Untätigkeitsklage** § 75 VwGO | frühestens 3 Monate nach Antrag, sofern kein zureichender Grund |
| BauG-Empfänger gegen Sofortvollzug einer belastenden Nebenbestimmung | § 80 V VwGO | innerhalb der Klagefrist |
| Eilbedürfnis bei Versagung | § 123 VwGO | – |

Im Widerspruchsverfahren (soweit landesrechtlich noch vorgesehen) Fristen entsprechend.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 29 BauGB](https://www.gesetze-im-internet.de/bbaug/__29.html) (Vorhabenbegriff)
- [§ 30 BauGB](https://www.gesetze-im-internet.de/bbaug/__30.html) (B-Plan-Gebiet)
- [§ 31 BauGB](https://www.gesetze-im-internet.de/bbaug/__31.html) (Ausnahme/Befreiung)
- [§ 33 BauGB](https://www.gesetze-im-internet.de/bbaug/__33.html) (Vorhaben während Planaufstellung)
- [§ 34 BauGB](https://www.gesetze-im-internet.de/bbaug/__34.html) (Innenbereich)
- [§ 35 BauGB](https://www.gesetze-im-internet.de/bbaug/__35.html) (Außenbereich)
- [§ 36 BauGB](https://www.gesetze-im-internet.de/bbaug/__36.html) (Einvernehmen der Gemeinde)
- [§ 212a BauGB](https://www.gesetze-im-internet.de/bbaug/__212a.html) (Sofortvollzug der Baugenehmigung)
- [BauNVO](https://www.gesetze-im-internet.de/baunvo/) (insb. §§ 2–11 Gebietsarten; § 12 Stellplätze; § 15 Gebietsverträglichkeit; § 16 Maß; § 23 überbaubare Fläche)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 75 VwGO](https://www.gesetze-im-internet.de/vwgo/__75.html), [§ 80 V VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html)
- LBO des einschlägigen Landes (BayBO / BauO NRW / LBO BW / HBauO / NBauO / LBauO RP / SächsBO / BbgBO / …) – Landesrechts-URL

### Kommentare

- Battis, in: Battis/Krautzberger/Löhr, BauGB, 15. Aufl. 2022, §§ 29, 34, 35 Rn. 1 ff.
- Söfker, in: Ernst/Zinkahn/Bielenberg/Krautzberger, BauGB (Loseblatt), § 34 Rn. 1 ff., § 35 Rn. 1 ff.
- Jäde, in: Jäde/Dirnberger, BauGB/BauNVO, 9. Aufl. 2022, § 34 BauGB Rn. 1 ff.
- Fickert/Fieseler, BauNVO, 13. Aufl. 2019, § 15 Rn. 1 ff.
- LBO-Kommentar des betroffenen Landes (z. B. Simon/Busse, BayBO – Art. 6 Abstandsflächen Rn. 1 ff.)
- Stüer, Bau- und Fachplanungsrecht, 6. Aufl. 2023, Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/BeckOnline]`)

1. BVerwG, Urt. v. 26.05.1978 – 4 C 9.77, BVerwGE 55, 369 („Krabbenkamp"; Einfügen § 34 BauGB)
2. BVerwG, Urt. v. 25.02.1977 – IV C 22.75, BVerwGE 52, 122 (Rücksichtnahmegebot)
3. BVerwG, Urt. v. 23.09.1999 – 4 C 6.98, BVerwGE 109, 314 (Rücksichtnahmegebot, Konkretisierung)
4. BVerwG, Urt. v. 16.03.1995 – 4 C 3.94 (Außenbereich, öffentliche Belange)
5. BVerwG-Linie zu rechtswidrig verweigertem Einvernehmen § 36 BauGB

## Ausgabeformat

```
GUTACHTEN — Baugenehmigung
Vorhaben: <Beschreibung>   Grundstück: <Lage, Bundesland>
Mandant: <Vorhabenträger / Gemeinde / Behörde>

I. Sachverhalt (knapp, mit B-Plan-Auszug / Innen-Außenbereich)

II. Frage(n)

III. Kurzantwort
     - Bauplanungsrechtliche Zulässigkeit: [§ 30 / § 34 / § 35 BauGB – Ergebnis]
     - Bauordnungsrechtliche Zulässigkeit: [LBO – Ergebnis]
     - Einvernehmen Gemeinde: [erteilt / verweigert – rechtmäßig?]
     - Verfahrensart: [volles / vereinfachtes Verfahren / Freistellung]
     - Empfehlung: [Bauvoranfrage / Vollantrag / Verpflichtungsklage / Untätigkeitsklage]

IV. Rechtliche Bewertung
    1. Vorhaben § 29 BauGB
    2. Bauplanungsrechtliche Zulässigkeit
       a) § 30 / § 34 / § 35 BauGB
       b) BauNVO (Art / Maß / Gebietsverträglichkeit)
       c) Befreiung § 31 II BauGB?
    3. Einvernehmen § 36 BauGB
    4. Bauordnungsrechtliche Zulässigkeit nach LBO <Land>
       a) Abstandsflächen
       b) Brandschutz / Standsicherheit
       c) Stellplätze
    5. Verfahrensart nach LBO
    6. Rechtsbehelfsstrategie
       – Verpflichtungs- / Anfechtungsklage § 42 VwGO
       – Untätigkeitsklage § 75 VwGO
       – Eilrechtsschutz § 123 VwGO

V. Schriftsatzentwurf (Antrag, Anträge, Begründung)

VI. Fristen-Box
    – Klagefrist § 74 VwGO (1 Monat ab Bekanntgabe)
    – Untätigkeitsklage § 75 VwGO (3 Monate)
    – Bauvorbescheid Bindung (idR 3 Jahre, LBO-spezifisch)

VII. Risiken / offene Punkte
     <Einstufung mit Begründung>

VIII. Quellenverzeichnis
```

## Beispiel (verkürzt, Gutachtenstil)

**Sachverhalt.** M will im Ortsteil X (Nordrhein-Westfalen) im faktischen Mischgebiet eine Gewerbeeinheit als Erweiterung ihres Bestandshauses errichten. Die Gemeinde verweigert das Einvernehmen unter Verweis auf „Wahrung des Wohncharakters". Ein qualifizierter B-Plan existiert nicht.

**I. § 29 BauGB.** Errichtung eines neuen Bauteils – Vorhaben (+).

**II. § 34 II BauGB iVm § 6 BauNVO (Mischgebiet).** Die nähere Umgebung entspricht einem MI. Art der Nutzung: Gewerbebetriebe, die das Wohnen nicht wesentlich stören, sind in MI allgemein zulässig (§ 6 II Nr. 4 BauNVO). Zu prüfen ist die konkrete Störungsintensität (Lärm, Verkehr) am Maßstab der TA Lärm und des Rücksichtnahmegebots § 15 I 2 BauNVO.

**III. Maß.** GRZ/GFZ in der näheren Umgebung als Maßstab; einzufügen iSv § 34 I BauGB.

**IV. § 36 BauGB.** Das Einvernehmen darf nur aus städtebaulichen Gründen verweigert werden. „Wahrung des Wohncharakters" ist im faktischen Mischgebiet kein tragfähiger Grund, soweit das Gebiet typenrein als MI einzustufen ist. Empfehlung: Aufforderung an Bauaufsicht zur Ersetzung des Einvernehmens (LBO NRW); hilfsweise Untätigkeitsklage nach Ablauf von drei Monaten (§ 75 VwGO).

**V. LBO NRW.** Abstandsflächen § 6 BauO NRW, Stellplätze, Brandschutz – zu prüfen anhand der konkreten Baupläne.

## Risiken / typische Fehler

- **„Faktisches Baugebiet" pauschal annehmen**, ohne die nähere Umgebung tatsächlich städtebaulich zu prüfen → BVerwG-Linie verfehlt.
- **Einvernehmen § 36 BauGB übersehen** – BauG ohne Einvernehmen rechtswidrig.
- **§ 212a BauGB unterschlagen** – die erteilte BauG ist kraft Gesetzes sofort vollziehbar; für Drittanfechtung ist Antrag § 80 V iVm § 80a VwGO erforderlich.
- **Sammelsurium aus LBO der falschen Bundesländer** zitiert; LBO ist immer landesgebunden.
- **Verpflichtungs- vs. Anfechtungsklage verwechseln**: BauG-Versagung → Verpflichtung; belastende Nebenbestimmung → Anfechtung.
- **§ 75 VwGO** (Untätigkeit) zu früh oder zu spät erhoben – 3-Monats-Hürde + zureichender Grund prüfen.
- **Bauvoranfrage als „Persilschein" missverstehen** – Bindung nur für die ausdrücklich gestellten Fragen.
