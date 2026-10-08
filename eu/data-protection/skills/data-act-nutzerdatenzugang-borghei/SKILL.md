---
name: data-act-nutzerdatenzugang-borghei
title: /datenwirtschaftsrecht:data-act-nutzerdatenzugang
description: Zugangsanspruch des Nutzers nach der EU-Datenverordnung – Konzeptionspflicht Art. 3 Abs. 1 und vorvertragliche Informationspflichten Art. 3 Abs. 2, 3, Bereitstellung an den Nutzer Art. 4 Abs. 1, Weitergabe an Dritte auf Verlangen des Nutzers Art. 5 mit Torwächtersperre Art. 5 Abs. 3, Pflichten des Dritten Art. 6, Schutz von Geschäftsgeheimnissen Art. 4 Abs. 6–8 und Art. 5 Abs. 9–11, technische Schutzmaßnahmen Art. 11, Beschwerde bei der Bundesnetzagentur Art. 38 iVm §§ 2, 6 DADG. Use when ein Nutzer Zugang zu Produktdaten verlangt oder ein Dateninhaber ein Zugangsverlangen beantworten, beschränken oder ablehnen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenwirtschaftsrecht/skills/data-act-nutzerdatenzugang
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: de
---

# /datenwirtschaftsrecht:data-act-nutzerdatenzugang

## Zweck

Der Skill bearbeitet das Zugangsverlangen selbst: er prüft, welche Daten „ohne Weiteres verfügbar" sind, in welcher Qualität und Frist sie bereitzustellen sind, wie Geschäftsgeheimnisse geschützt werden, ohne den Anspruch leerlaufen zu lassen, und wann eine Verweigerung tragfähig ist. Er entwirft die Antwort des Dateninhabers oder das Verlangen des Nutzers und benennt den Rechtsweg.

## Eingaben

- Wortlaut und Datum des Zugangsverlangens, Absender und dessen Rolle
- Datenkatalog: welche Daten das Produkt erzeugt, welche der Dateninhaber tatsächlich vorhält
- Ob ein Dritter benannt ist, und ob dieser Torwächter nach VO (EU) 2022/1925 ist
- Vorhandene Schnittstellen: API, Portal, Direktzugriff am Gerät
- Als Geschäftsgeheimnis gekennzeichnete Datenfelder samt Schutzmaßnahmen
- Sicherheitsrelevanz der Daten iSd Art. 4 Abs. 2
- Ob personenbezogene Daten Dritter enthalten sind

## Sub-Agent-Architektur

Der Researcher liefert Normtext, Erwägungsgründe und Behördenverlautbarungen. Der Drafter trennt den Datenbestand in „ohne Weiteres verfügbar", „abgeleitet" und „gesperrt" und entwirft Antwortschreiben oder Verlangen. Der Reviewer kontrolliert, dass keine Verweigerung ohne Rechtsgrundlage ausgesprochen, keine Mitteilungspflicht an die Bundesnetzagentur übergangen und kein Geschäftsgeheimnisschutz behauptet wird, für den die Kennzeichnung nach Art. 4 Abs. 6 fehlt.

## Ablauf

### 1. Datenkatalog bilden — „ohne Weiteres verfügbar" ist der Schlüsselbegriff

Der Anspruch aus Art. 4 Abs. 1 erfasst **ohne Weiteres verfügbare Daten** einschließlich der zur Auslegung und Nutzung erforderlichen **Metadaten**. Das sind Produktdaten und verbundene Dienstdaten, die der Dateninhaber rechtmäßig erlangt oder rechtmäßig erlangen kann, ohne unverhältnismäßigen Aufwand über einen einfachen Vorgang hinaus.

| Kategorie | Erfasst? |
|---|---|
| Rohdaten aus Sensorik, Zustands- und Nutzungsdaten | ja |
| Für Auslegung nötige Metadaten | ja |
| Daten, die erst durch komplexe Aufbereitung entstehen | regelmäßig nein — Begründung erforderlich |
| Stark abgeleitete oder rückgeschlossene Daten (inferred / derived) | nein |
| Daten aus Tests noch nicht in Verkehr gebrachter Produkte (Art. 5 Abs. 2) | für die Drittweitergabe nein, außer vertraglich gestattet |

Die Einordnung ist datenfeldweise zu dokumentieren. Eine pauschale Behauptung „alles ist abgeleitet" trägt nicht.

### 2. Konzeptionspflicht und vorvertragliche Information prüfen (Art. 3)

Nach Art. 3 Abs. 1 sind vernetzte Produkte und verbundene Dienste so zu konzipieren, dass die Daten **standardmäßig, einfach, sicher, unentgeltlich, in einem umfassenden, strukturierten, gängigen und maschinenlesbaren Format** und – soweit relevant und technisch durchführbar – **direkt** zugänglich sind. Diese Pflicht gilt nach Art. 50 nur für Produkte und Dienste, die **nach dem 12.09.2026** in Verkehr gebracht wurden.

Unabhängig davon bestehen die vorvertraglichen Informationspflichten:

- **Art. 3 Abs. 2** — vor Abschluss eines Kauf-, Miet- oder Leasingvertrags über das Produkt: Art, Format und geschätzter Umfang der Daten; ob kontinuierlich und in Echtzeit generiert wird; ob auf dem Gerät oder einem entfernten Server gespeichert wird und wie lange; wie zugegriffen, abgerufen und gelöscht werden kann.
- **Art. 3 Abs. 3** — vor Abschluss eines Vertrags über einen verbundenen Dienst: Art, Umfang und Häufigkeit der Erhebung, Zugriffsmodalitäten, geplante Eigennutzung durch den künftigen Dateninhaber und deren Zwecke.

Diese Informationen gehören in Produktinformation und Vertragsunterlagen, nicht in die Datenschutzerklärung.

### 3. Bereitstellung an den Nutzer (Art. 4 Abs. 1)

Soweit der Nutzer nicht direkt am Produkt zugreifen kann, hat der Dateninhaber bereitzustellen: **unverzüglich, einfach, sicher, unentgeltlich, in einem umfassenden, gängigen und maschinenlesbaren Format** und, falls relevant und technisch durchführbar, **in gleicher Qualität wie für den Dateninhaber, kontinuierlich und in Echtzeit**. Das Verlangen kann formlos elektronisch gestellt werden.

Flankierend:

- **Art. 4 Abs. 4** — Verbot, die Rechtsausübung unangemessen zu erschweren, ausdrücklich einschließlich manipulativer Oberflächengestaltung („dark patterns").
- **Art. 4 Abs. 5** — Identitätsprüfung nur im erforderlichen Maß; keine über das Nötige hinausgehende Protokollierung der Zugriffe.
- **Art. 4 Abs. 2** — vertragliche Beschränkungen sind zulässig, wenn die Verarbeitung gesetzliche Sicherheitsanforderungen des Produkts beeinträchtigen und zu schwerwiegenden Gesundheits- oder Sicherheitsfolgen führen könnte. Verweigert der Dateninhaber deshalb, **teilt er dies der nach Art. 37 benannten zuständigen Behörde mit** — in Deutschland der Bundesnetzagentur (§ 2 Abs. 1 DADG).

### 4. Weitergabe an Dritte (Art. 5, Art. 6)

Auf Verlangen des Nutzers stellt der Dateninhaber die Daten einem **Dritten** bereit — für den Nutzer unentgeltlich, in derselben Qualität, strukturiert, gängig und maschinenlesbar, soweit relevant kontinuierlich und in Echtzeit. Das Verhältnis Dateninhaber ↔ Dritter richtet sich nach Art. 8 und Art. 9; die Vergütung schuldet der Dritte, nicht der Nutzer (`/datenwirtschaftsrecht:data-act-vertragsklauseln`).

Grenzen:

- **Art. 5 Abs. 3** — ein benannter **Torwächter** ist kein zugelassener Dritter. Er darf Nutzer weder auffordern noch durch Anreize gewinnen, Daten weiterzugeben, und darf solche Daten nicht entgegennehmen. Verstöße sind nach § 15 Abs. 2 Nr. 9 DADG der schärfste Bußgeldtatbestand des deutschen Durchführungsrechts.
- **Art. 5 Abs. 5** — der Dritte darf keine Zwangsmittel einsetzen und keine Lücken der Schutzinfrastruktur ausnutzen.
- **Art. 5 Abs. 6** — der Dateninhaber darf die Daten nicht nutzen, um Einblicke in die wirtschaftliche Lage des Dritten zu gewinnen.
- **Art. 5 Abs. 7** — ist der Nutzer nicht die betroffene Person, ist eine Rechtsgrundlage nach Art. 6 DSGVO erforderlich.
- **Art. 6** — der Dritte darf die Daten nur zu den mit dem Nutzer vereinbarten Zwecken und Bedingungen verarbeiten; die Verletzung ist nach § 15 Abs. 3 DADG bußgeldbewehrt.

### 5. Geschäftsgeheimnisse — Verfahren statt Verweigerung (Art. 4 Abs. 6–8, Art. 5 Abs. 9–11)

Die Verordnung schützt Geschäftsgeheimnisse in drei Stufen:

1. **Kennzeichnung.** Der Dateninhaber oder der Geheimnisinhaber **ermittelt und kennzeichnet** – auch in den Metadaten – die als Geschäftsgeheimnis geschützten Daten. Ohne Kennzeichnung trägt die Verteidigung nicht.
2. **Schutzmaßnahmen.** Mit dem Nutzer bzw. Dritten sind angemessene technische und organisatorische Maßnahmen zu vereinbaren: Mustervertragsklauseln, Vertraulichkeitsvereinbarungen, strenge Zugangsprotokolle, technische Normen, Verhaltenskodizes.
3. **Aussetzung oder Verweigerung.** Kommt keine Einigung zustande oder werden vereinbarte Maßnahmen nicht umgesetzt bzw. untergraben, kann die Weitergabe ausgesetzt und im engen Ausnahmefall verweigert werden. Die Entscheidung ist zu begründen, dem Verlangenden mitzuteilen und der zuständigen Behörde anzuzeigen; die Nachweise sind vorzulegen.

Die zugehörigen Mitteilungs- und Nachweispflichten sind in § 15 Abs. 2 Nr. 4 und Nr. 5 DADG bußgeldbewehrt. Wer verweigert, ohne zu melden, riskiert die Sanktion zusätzlich zur materiellen Niederlage.

### 6. Technische Schutzmaßnahmen und Rechtsbehelfe

Nach **Art. 11** darf der Dateninhaber technische Schutzmaßnahmen einsetzen, um unbefugte Nutzung oder Offenlegung zu verhindern — sie dürfen den Zugangsanspruch jedoch nicht unterlaufen. Bei unbefugter Nutzung durch Nutzer oder Dritten sieht Art. 11 Abs. 2 Beseitigungs-, Vernichtungs- und Unterlassungsansprüche vor.

Rechtsbehelfe des Nutzers: Beschwerde bei der Bundesnetzagentur nach Art. 38 iVm [§ 2 DADG](https://www.gesetze-im-internet.de/dadg/__2.html), [§ 6 DADG](https://www.gesetze-im-internet.de/dadg/__6.html); Streitbeilegung nach Art. 10 vor einer nach § 5 DADG zugelassenen Stelle; gerichtlicher Rechtsbehelf nach Art. 39 — vor den ordentlichen Gerichten, soweit der Anspruch zivilrechtlich geltend gemacht wird.

## Deterministische Berechnung

Der Data Act arbeitet mit dem unbestimmten Begriff „unverzüglich" und stellt keine Tagesfrist auf. Zu rechnen sind daher nur selbst gesetzte oder vertraglich vereinbarte Fristen. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) unterstützt die Fristsetzung im Aufforderungsschreiben:

```bash
# Angemessene Frist zur Bereitstellung, gesetzt am 15.02.2026, 14 Tage
python -m scripts.legal_calc.cli frist --ereignis 15.02.2026 --menge 14 --einheit tage --land BY
```

Die Angemessenheit der Frist bleibt eine juristische Wertung und ist zu begründen.

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/2854, Art. 2, 3, 4, 5, 6, 7, 10, 11, 37, 38, 39, 43 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- [DADG § 2](https://www.gesetze-im-internet.de/dadg/__2.html), [§ 5](https://www.gesetze-im-internet.de/dadg/__5.html), [§ 6](https://www.gesetze-im-internet.de/dadg/__6.html), [§ 15](https://www.gesetze-im-internet.de/dadg/__15.html)
- Verordnung (EU) 2022/1925 (DMA), Art. 3 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/1925/oj)
- [GeschGehG § 2](https://www.gesetze-im-internet.de/geschgehg/__2.html), [§ 6](https://www.gesetze-im-internet.de/geschgehg/__6.html)
- [Art. 6 DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

### Kommentare und Literatur

- Hennemann/Steinrötter, Data Act – Handkommentar, Art. 3, Art. 4, Art. 5.
- Specht-Riemenschneider/Hennemann, Data Act, Kommentar, Art. 4 Rn. zum Begriff „ohne Weiteres verfügbar".
- Wiebe, in: Wiebe/Schur, Datenrecht, Kap. Zugangsansprüche.
- Zum Verhältnis Geschäftsgeheimnis / Zugangsanspruch: Beiträge in GRUR und ZD 2024/2025 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Höchstrichterliche Rechtsprechung zu Art. 3 bis 6 Data Act liegt bislang nicht vor. Zur Auslegung des Geschäftsgeheimnisbegriffs kann auf die Rechtsprechung zu § 2 GeschGehG zurückgegriffen werden; jede konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
DATA-ACT-ZUGANGSVERLANGEN — <Mandat> — <Datum>

I.   Verlangen
     Eingang:                 <Datum>  Absender: <Nutzer / Dritter im Namen des Nutzers>
     Rolle geprüft:           [Nutzer bestätigt / zweifelhaft — Nachweis angefordert]
     Torwächter:              [ja — Art. 5 Abs. 3 sperrt / nein]

II.  Datenkatalog
     Feld / Kategorie | ohne Weiteres verfügbar | abgeleitet | Geschäftsgeheimnis | Ergebnis
     <…>

III. Anspruchsgrundlage
     [Art. 4 Abs. 1 — Zugang für den Nutzer]
     [Art. 5 Abs. 1 — Weitergabe an Dritten]
     Format:                  <maschinenlesbar, gängig, strukturiert>
     Echtzeit / kontinuierlich: [ja / technisch nicht durchführbar — Begründung]

IV.  Grenzen und Einwendungen
     Art. 4 Abs. 2 Sicherheit: [einschlägig — Mitteilung an BNetzA am <Datum> / nein]
     Geschäftsgeheimnis:      Kennzeichnung [erfolgt / fehlt]; Maßnahmen [vereinbart / offen]
     Art. 5 Abs. 2 Testdaten: [einschlägig / nein]
     Art. 11 Schutzmaßnahmen: <…>

V.   Ergebnis
     Bereitstellung:          [vollständig / teilweise / ausgesetzt / verweigert]
     Begründung:              <…>
     Mitteilungspflichten:    <Art. 4 Abs. 2 / Abs. 8 / Art. 5 Abs. 11 — an BNetzA>

VI.  Rechtsbehelfe
     Beschwerde Art. 38 iVm § 6 DADG | Streitbeilegung Art. 10 | Klage Art. 39
     Bußgeldrisiko:           <§ 15 DADG — Tatbestand und Rahmen>

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Antwort auf ein Zugangsverlangen (Gerüst)

```
Sehr geehrte …,

wir bestätigen den Eingang Ihres Verlangens vom <Datum> nach Artikel 4
Absatz 1 der Verordnung (EU) 2023/2854.

1. Umfang
   Die nachstehenden Datenkategorien stellen wir Ihnen ab dem <Datum>
   über <Schnittstelle> im Format <…> bereit: <Aufzählung>.

2. Nicht erfasste Daten
   Die Felder <…> sind keine ohne Weiteres verfügbaren Daten, weil <…>.

3. Geschäftsgeheimnisse
   Die Felder <…> sind als Geschäftsgeheimnisse im Sinne des § 2 Nr. 1
   GeschGehG gekennzeichnet. Wir schlagen zur Wahrung der Vertraulichkeit
   folgende Maßnahmen nach Artikel 4 Absatz 6 vor: <…>.

4. Weiteres Vorgehen
   Für Rückfragen und zur Abstimmung der Maßnahmen stehen wir bis zum
   <Datum> zur Verfügung. Eine Ablehnung ist mit diesem Schreiben nicht
   verbunden.
```

## Risiken / typische Fehler

- **Zugang pauschal verweigert.** Art. 4 kennt keine allgemeine Verweigerung; zulässig sind nur die Sicherheitsausnahme des Abs. 2 und das Geschäftsgeheimnisverfahren des Abs. 6 ff. — beide mit Mitteilung an die Bundesnetzagentur.
- **Geschäftsgeheimnis ohne Kennzeichnung geltend gemacht.** Art. 4 Abs. 6 verlangt die vorherige Ermittlung und Kennzeichnung, auch in den Metadaten.
- **Alles zu „abgeleiteten Daten" erklärt.** Die Einordnung ist feldweise zu begründen; die Beweisnot trifft im Streitfall den Dateninhaber.
- **Entgelt vom Nutzer verlangt.** Der Zugang nach Art. 4 Abs. 1 und die Weitergabe nach Art. 5 Abs. 1 sind für den Nutzer unentgeltlich; eine Gegenleistung kommt nur im Verhältnis zum Dritten nach Art. 9 in Betracht.
- **Torwächtersperre übersehen.** Art. 5 Abs. 3 verbietet die Weitergabe an benannte Torwächter — mit dem höchsten Bußgeldrahmen des § 15 DADG.
- **Vorvertragliche Information in die Datenschutzerklärung gepackt.** Art. 3 Abs. 2, 3 verlangt eigenständige, klare und verständliche Angaben im Produkt- und Vertragskontext.
- **Identitätsprüfung als Zugangshürde missbraucht.** Art. 4 Abs. 5 begrenzt sie auf das Erforderliche; übermäßige Protokollierung ist unzulässig.
- **Rechtsprechung erfunden.** Zum Data Act existiert kaum Judikatur; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
