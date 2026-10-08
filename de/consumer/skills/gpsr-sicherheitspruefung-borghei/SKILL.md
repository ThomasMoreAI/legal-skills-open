---
name: gpsr-sicherheitspruefung-borghei
title: /produktrecht:gpsr-sicherheitspruefung
description: Pflichtenkatalog für Hersteller, Importeur, Fulfillment-Dienstleister und Online-Marktplätze nach GPSR (VO (EU) 2023/988, anwendbar ab 13.12.2024) mit Risikobewertung, technischer Dokumentation, Vorfallsmeldung über Safety Business Gateway und Rückrufpflicht – einschließlich Abgrenzung zu sektoraler Harmonisierung und ProdSG-Übergang. Use when ein Verbraucherprodukt neu in den EU-Markt gebracht wird oder ein Sicherheitsproblem die GPSR-Pflichten auslöst.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/produktrecht/skills/gpsr-sicherheitspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /produktrecht:gpsr-sicherheitspruefung

## Zweck

Der Skill prüft die Pflichtenlage nach der **General Product Safety Regulation** (VO (EU) 2023/988, **GPSR**, anwendbar ab **13.12.2024**) für Hersteller, Importeure, Fulfillment-Dienstleister und Online-Marktplätze. Er klärt den Anwendungsbereich gegenüber sektoraler Harmonisierung, strukturiert die Risikobewertung und technische Dokumentation und adressiert Vorfallsmeldungen über das Safety Business Gateway sowie die Rückrufpflicht.

## Eingaben

- Produkt (Bezeichnung, Funktion, Zielnutzer — insbesondere Verbraucher iSv Art. 3 Nr. 1 GPSR)
- Rolle des Mandanten (Hersteller Art. 9, Importeur Art. 11, Fulfillment Art. 12, Online-Marktplatz Art. 22, Händler Art. 13)
- Sitz des Herstellers (innerhalb / außerhalb der EU — Pflicht zur verantwortlichen Wirtschaftsakteur-Bestellung nach Art. 16 MarktüberwachungsVO 2019/1020)
- einschlägige sektorale Harmonisierungsregeln (MaschinenVO 2023/1230, SpielzeugRL 2009/48/EG, NSpRG 2014/35/EU, EMV-RL 2014/30/EU, RED 2014/53/EU, Bauprodukten-VO 305/2011)
- Anlass: Erstinverkehrbringen / Bestandsprodukt / konkretes Sicherheitsproblem / Marktaufsichtsanfrage

## Sub-Agent-Architektur

Researcher liefert GPSR-Statute, EUR-Lex-Links, sektorale Harmonisierungsregeln, ProdSG-Übergang, Klindt-Kommentar (jetzt GPSR-Kommentar). Drafter erstellt strukturierten Pflichtenkatalog je Rolle mit Risikobewertungsraster. Reviewer prüft Vollständigkeit der technischen Dokumentation, Vorfallsmeldepflicht „unverzüglich" und Abgrenzung zur sektoralen lex specialis.

## Ablauf

### 1. Anwendungsbereich

GPSR gilt für **Verbraucherprodukte**, die in der Union in Verkehr gebracht oder bereitgestellt werden, **soweit** keine speziellen Sicherheitsanforderungen in harmonisierten Unionsrechtsakten dasselbe Schutzziel regeln (Art. 2 II GPSR). Bei sektoraler Harmonisierung gilt **GPSR ergänzend**, soweit Aspekte (Risiken, Pflichten) nicht abschließend geregelt sind (Art. 2 I lit. b GPSR).

Beispiele:

| Produkt | Vorrangiger Akt | GPSR-Ergänzung |
|---|---|---|
| Maschine | MaschinenVO (EU) 2023/1230 (ab 20.01.2027); bis dahin MaschinenRL 2006/42/EG iVm 9. ProdSV | nur Aspekte, die dort nicht geregelt |
| Spielzeug | SpielzeugRL 2009/48/EG iVm 2. ProdSV | ergänzend |
| Niederspannungsgerät | NSpRL 2014/35/EU iVm 1. ProdSV | ergänzend |
| Funkanlage | RED 2014/53/EU iVm FuAG | ergänzend |
| reiner Verbraucher-Sensor ohne sektorale Regelung | (kein vorrangiger Akt) | GPSR voll |

### 2. Pflichten des Herstellers (Art. 9 GPSR)

- **Allgemeine Sicherheitsanforderung** Art. 5 GPSR: nur sichere Produkte in Verkehr bringen
- **Risikoanalyse** Art. 9 II GPSR mit Bewertung anhand der Indikatoren des Art. 6 GPSR (Eigenschaften, Wechselwirkung mit anderen Produkten, Aufmachung, Verbrauchergruppen, Cybersicherheit als neuer Faktor)
- **Technische Dokumentation** Art. 9 V GPSR: Beschreibung des Produkts, Risikoanalyse, ergriffene Risikominderungsmaßnahmen, ggf. Prüfberichte, **10 Jahre** aufzubewahren
- **Identifizierbarkeit** Art. 9 VI: Typen-, Chargen- oder Seriennummer am Produkt
- **Kennzeichnung des Herstellers** Art. 9 VII: Name, eingetragener Handelsname / Marke, Postanschrift, elektronische Kontaktadresse
- **Gebrauchs- und Sicherheitshinweise** Art. 9 VII in der Sprache des Mitgliedstaats
- **Reaktionspflicht bei Verdacht der Unsicherheit** Art. 9 IX–XI: Untersuchung, Korrekturmaßnahmen, Information der Marktaufsicht und der Verbraucher
- **Vorfallsmeldung** Art. 20 GPSR über das **Safety Business Gateway** **unverzüglich** nach Kenntnis eines Unfalls, der durch das Produkt verursacht wurde
- **Rückrufpflicht** Art. 36 GPSR bei Sicherheitsrisiko

### 3. Pflichten des Importeurs (Art. 11 GPSR)

- Inverkehrbringen nur sicherer Produkte
- Eigenständige Überprüfung der Hersteller-Pflichten (Risikoanalyse, technische Dokumentation, Kennzeichnung)
- **Anbringung der eigenen Kennzeichnung** (Name, Anschrift, elektronische Adresse) — zusätzlich zum Hersteller
- Aufbewahrung der technischen Dokumentation **10 Jahre**
- Mitwirkung bei Korrekturmaßnahmen und Vorfallsmeldungen

### 4. Pflichten des Fulfillment-Dienstleisters (Art. 12 GPSR)

Fulfillment iSv Art. 3 Nr. 11 GPSR (Lager, Verpackung, Adressierung, Versand). Pflicht: Sicherstellung, dass die Lager- und Versandbedingungen die Konformität nicht beeinträchtigen; Kooperationspflicht mit Marktaufsicht.

### 5. Pflichten der Online-Marktplätze (Art. 22 GPSR)

- Einrichtung einer **zentralen Kontaktstelle** für Marktüberwachungsbehörden
- Registrierung im **Safety Gate Portal**
- **Notice-and-Action-Mechanismus** für unsichere Angebote
- Entfernung gefährlicher Angebote nach Aufforderung der Marktaufsicht **innerhalb von 2 Werktagen**
- Information betroffener Verbraucher bei Rückruf

### 6. Sanktionen und Marktaufsicht

- Sanktionen nach Art. 44 GPSR im nationalen Recht zu konkretisieren — in DE über das **GPSR-Durchführungsgesetz** (Stand 2024/2025 in Vorbereitung, das ProdSG wird für nicht-harmonisierte Verbraucherprodukte abgelöst) `[unverifiziert – nationalen Umsetzungsstand prüfen]`
- Marktaufsicht in DE: Länder (zuständige Behörden), BAuA (Koordinierung), sektoral z. B. BNetzA, BVL
- Anordnungsbefugnisse nach Art. 36 GPSR iVm MarktüberwachungsVO 2019/1020 (Information, Warnung, Verkaufsverbot, Rückruf, Vernichtung)

### 7. ProdSG-Übergang

Für nicht-harmonisierte Verbraucherprodukte hat das **ProdSG** (Geltungsbereich Verbraucherprodukte, nicht-Wirtschaftstätigkeit) bis 12.12.2024 gegolten. Ab 13.12.2024 gilt unmittelbar die GPSR. Sektorale ProdSV (1. ProdSV NSpRG, 9. ProdSV Maschinen etc.) bleiben kraft Inkorporation in nationales Recht in Kraft.

Übergangsfragen: Produkte, die vor 13.12.2024 unter ProdSG-Regime in Verkehr gebracht wurden, behalten ihre rechtmäßige Inverkehrbringung; Pflichten nach Inverkehrbringen (Beobachtung, Rückruf) richten sich ab 13.12.2024 nach GPSR.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute (EU + national)

- [VO (EU) 2023/988 (GPSR)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R0988)
- [VO (EU) 2019/1020 (MarktüberwachungsVO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R1020)
- [VO (EU) 2023/1230 (MaschinenVO, ab 20.01.2027)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1230)
- [RL 2009/48/EG (SpielzeugRL)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32009L0048)
- [RL 2014/35/EU (NSpRL)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0035)
- [RL 2014/30/EU (EMV-RL)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0030)
- [RL 2014/53/EU (RED)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0053)
- [ProdSG](https://www.gesetze-im-internet.de/prodsg_2021/) (Übergangsregime)
- [1. ProdSV (NSpRG)](https://www.gesetze-im-internet.de/prodsv_1_2016/)
- [9. ProdSV (Maschinen)](https://www.gesetze-im-internet.de/prodsv_9/)

### Kommentare

- Klindt, GPSR-Kommentar (Nachfolger Klindt ProdSG), 1. Aufl. 2024 ff. `[unverifiziert – Verlag/Aufl. prüfen]`
- Wilrich, Produktsicherheitsrecht, 2. Aufl. 2024 `[unverifiziert – Aufl./Jahr prüfen]`
- Lenz, ProdHaftG, Kommentar, 2024 (auch zu GPSR-Schnittstelle) `[unverifiziert – Aufl. prüfen]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/curia.europa.eu]`)

1. EuGH, Urt. v. 30.04.2009 – C-132/08, Lidl Magyarország (sektoraler Vorrang gegenüber allgemeiner Produktsicherheits-RL)
2. EuGH, Urt. v. 05.03.2015 – C-503/13, C-504/13, ECLI:EU:C:2015:148 (Boston Scientific, Fehlerbegriff bei potenziellen Risiken)
3. nationale Marktaufsichtsrechtsprechung VGH/OVG zu ProdSG-Anordnungen (im Übergang auf GPSR fortgeltend)

## Ausgabeformat

```
GPSR-PRÜFUNG
Mandat: <Rolle: Hersteller / Importeur / Fulfillment / Marktplatz>
Produkt: <Bezeichnung, Funktion, Zielnutzer>

I. Anwendungsbereich
   1. Verbraucherprodukt iSv Art. 3 Nr. 1 GPSR?
   2. Sektorale Harmonisierung einschlägig?
      → <Akt> – Vorrang / ergänzende GPSR-Anwendung

II. Pflichten je Rolle
    A. Hersteller (Art. 9 GPSR)
       – Risikobewertung Art. 5, 6
       – Technische Dokumentation Art. 9 V (10 J)
       – Identifizierung / Kennzeichnung Art. 9 VI, VII
       – Gebrauchs- und Sicherheitshinweise
       – Reaktionspflicht Art. 9 IX–XI
       – Vorfallsmeldung Art. 20 (Safety Business Gateway)
       – Rückrufpflicht Art. 36
    B. Importeur (Art. 11) — eigene Kennzeichnung, 10-J-Aufbewahrung
    C. Fulfillment (Art. 12)
    D. Online-Marktplatz (Art. 22)
       – zentrale Kontaktstelle
       – Safety Gate Portal Registrierung
       – Notice-and-Action, 2-Werktage-Frist

III. ProdSG-Übergang (Altprodukte vor 13.12.2024)

IV. Sanktionen und Marktaufsicht

V. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VI. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Sektorale Harmonisierung übersehen.** Bei Maschinen, Spielzeug, NSpRG, EMV, RED, Bauprodukten gilt zuerst der spezielle Akt; GPSR nur ergänzend.
- **GPSR-Anwendungsdatum.** Die Verordnung gilt ab **13.12.2024** unmittelbar; nationales Umsetzungsgesetz für Sanktionen separat — Stand prüfen.
- **Importeur-Pflichten unterschätzt.** Der EU-Importeur ist gegenüber der Marktaufsicht erste Adresse, wenn der Hersteller außerhalb der EU sitzt; auch ohne Quasi-Hersteller-Status haftet er nach Art. 11 GPSR und § 4 II ProdHaftG.
- **Produkthaftungsrechtliche Folgeebene nach altem Stand beurteilt.** Für Produkte, die **ab dem 09.12.2026** in Verkehr gebracht werden, tritt an die Stelle des ProdHaftG 1989 das Umsetzungsrecht zur **RL (EU) 2024/2853**: Software, SaaS und KI sind Produkte, die 85-Mio.-EUR-Höchstgrenze entfällt, der Kreis der Haftungsadressaten ist erweitert. Der Verweis auf § 4 II ProdHaftG trägt nur für Altprodukte. Einzelheiten und Stichtagsprüfung im Skill `prodhaftg-herstellerhaftung`. `[unverifiziert - prüfen]`
- **„Safety Gate" vs. „Safety Business Gateway" verwechselt.** Safety Gate = Behörden-/Verbraucherportal (vormals RAPEX); Safety Business Gateway = Meldekanal für Wirtschaftsakteure.
- **Vorfallsmeldung Art. 20 verzögert.** „Unverzüglich" iSv § 121 BGB-Wertung; Zögern kann Bußgeld und § 823 BGB-Haftung auslösen.
- **Cybersicherheit als Sicherheitsfaktor übersehen.** Art. 6 lit. h GPSR erfasst auch IT-Risiken bei vernetzten Produkten.
- **Technische Dokumentation unvollständig.** Pflicht zur 10-Jahre-Aufbewahrung; bei Marktaufsichtsanfrage kurzfristig vorzulegen.
