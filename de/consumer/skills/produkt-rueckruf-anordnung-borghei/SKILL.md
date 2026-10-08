---
name: produkt-rueckruf-anordnung-borghei
title: /produktrecht:produkt-rueckruf-anordnung
description: Zivilrechtliche Rückrufpflicht des Herstellers aus § 823 I BGB (Produktbeobachtung, BGH „Pflegebetten") und öffentlich-rechtliche Anordnung der Marktaufsicht nach Art. 36 GPSR / sektoralen ProdSV mit Maßnahmenstufung (Warnung → Empfehlung → Reparatur → Rückruf → Vernichtung), Anhörung § 28 VwVfG, Sofortvollzug und Rechtsbehelf VwGO. Use when ein Hersteller die Rückruferforderlichkeit prüfen muss oder eine Marktaufsichtsbehörde eine Rückrufanordnung erlassen oder ihn der Adressat einer solchen Anordnung anfechten will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/produktrecht/skills/produkt-rueckruf-anordnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /produktrecht:produkt-rueckruf-anordnung

## Zweck

Der Skill prüft die **doppelte Rückrufdimension**: einerseits die zivilrechtliche Pflicht des Herstellers zu Rückrufmaßnahmen aus seiner Produktbeobachtungs-Verkehrssicherungspflicht (§ 823 I BGB, BGH „Pflegebetten"), andererseits die öffentlich-rechtliche Anordnung der Marktaufsichtsbehörde nach Art. 36 GPSR und sektoralen Verordnungen. Er strukturiert die Maßnahmenstufung nach Verhältnismäßigkeit und unterstützt sowohl bei der Erstellung einer Rückruf-Kommunikation als auch beim Vorgehen gegen eine behördliche Anordnung.

## Eingaben

- Sicherheitsproblem (Schadensbild, betroffene Charge, Häufigkeit, Risikogruppe)
- Position des Mandanten: Hersteller / Importeur / Händler / Marktaufsichtsbehörde / Adressat einer Anordnung
- Bisherige Maßnahmen (interne Risikobewertung, Vorfallsmeldungen, Information der Vertriebspartner)
- Stand des Verfahrens (interne Prüfung / behördliche Anhörung § 28 VwVfG / Anordnung erlassen / Sofortvollzug angeordnet)
- ggf. parallele Vorfallsmeldung Art. 20 GPSR über Safety Business Gateway

## Sub-Agent-Architektur

Researcher liefert § 823 BGB, BGH „Pflegebetten", Art. 36 und Art. 20 GPSR, sektorale ProdSV, VwVfG und VwGO. Drafter erstellt Maßnahmenplan, Rückruf-Bekanntmachung an Verbraucher und ggf. Stellungnahme zur Behördenanhörung oder Widerspruchsbegründung. Reviewer prüft Verhältnismäßigkeit, Anhörung, Verjährungs- und Klagefristen sowie Vollständigkeit der Safety-Business-Gateway-Meldung.

## Ablauf

### 1. Zivilrechtliche Rückrufpflicht (§ 823 I BGB)

Verkehrssicherungspflicht **Produktbeobachtung** (BGH, **„Pflegebetten"** – Urt. v. 16.12.2008 – VI ZR 170/07 `[unverifiziert – prüfen in juris]`): Der Hersteller muss sein Produkt nach Inverkehrbringen beobachten und auf später erkannte Risiken reagieren. Die Reaktion ist nach **Gefährdungsstärke** zu skalieren:

| Stufe | Maßnahme | Auslöser |
|---|---|---|
| 1 | **Warnung** an Verbraucher / Vertriebspartner | erhöhtes, aber begrenztes Risiko, das durch Hinweis abgewendet werden kann |
| 2 | **Gebrauchs-Empfehlung** (Ausbau, Nichtnutzung einzelner Funktionen) | Risiko abgrenzbar auf bestimmte Gebrauchssituationen |
| 3 | **Reparatur / Nachrüstung** | technisch korrigierbares Risiko |
| 4 | **Rückruf** (Aufforderung zur Rückgabe gegen Erstattung / Tausch) | Risiko nicht durch Hinweise oder Reparatur am verbliebenen Bestand neutralisierbar |
| 5 | **Vernichtung** | irreparable Gefahr für Leib und Leben |

Maßstab: BGH NJW 2009, 1080 `[unverifiziert]`; Wagner, in: MüKoBGB, § 823 Rn. 800 ff.

Ein **Verstoß** gegen die Stufung haftet schadensbegründend nach § 823 I BGB (Personenschäden), auch wenn der Erstinverkehrbringungs-Zeitpunkt fehlerfrei war (Produktbeobachtungsfehler — **nicht** über ProdHaftG erfasst).

### 2. Öffentlich-rechtliche Rückrufanordnung

#### a) GPSR Art. 36

Marktaufsichtsbehörden können nach Art. 36 GPSR iVm Art. 16 MarktüberwachungsVO 2019/1020 alle erforderlichen Korrekturmaßnahmen anordnen, einschließlich Verkaufsverbot, Rücknahme aus dem Markt, Rückruf und Vernichtung. Voraussetzung: das Produkt stellt ein **ernstes Risiko** (Art. 3 Nr. 19 GPSR) oder ein sonstiges Risiko dar, das ohne Maßnahme nicht beherrschbar ist.

#### b) Sektorale Verordnungen

Bei harmonisierten Produkten zusätzlich sektorale Anordnungsbefugnisse, z. B. § 7 9. ProdSV (Maschinen) iVm MaschinenRL; FuAG für Funkanlagen; Bauprodukten-VO 305/2011.

#### c) ProdSG-Übergang

Für Altanordnungen aus der Zeit bis 12.12.2024 gelten die §§ 26 ff. ProdSG fort, soweit das nationale GPSR-Durchführungsgesetz keine Aufhebung vorsieht `[unverifiziert – nationalen Umsetzungsstand prüfen]`.

### 3. Verfahren

- **Anhörung** nach § 28 VwVfG vor Erlass des belastenden Verwaltungsakts (außer bei Gefahr im Verzug § 28 II Nr. 1 VwVfG)
- **Begründung** § 39 VwVfG
- **Verhältnismäßigkeit** Art. 20 III GG, § 18 GPSR-Durchführungsgesetz (sobald in Kraft) — mildestes geeignetes Mittel; Stufung 1→5 ist Ausdruck der Verhältnismäßigkeit
- **Sofortvollzug** § 80 II Nr. 4 VwGO im überwiegenden öffentlichen Interesse; Begründung muss konkret das besondere Vollziehungsinteresse darlegen
- **Rechtsbehelf** Widerspruch / Anfechtungsklage VwGO; **Frist 1 Monat** ab Bekanntgabe (§§ 70, 74 VwGO); Eilrechtsschutz § 80 V VwGO bei Sofortvollzug
- **Grundrechtsbezug** Art. 12 I, Art. 14 I GG (Berufs- und Eigentumsfreiheit des Herstellers / Händlers)

### 4. Safety Business Gateway und Safety Gate

- Vorfallsmeldung an die Marktaufsicht über das **Safety Business Gateway** Art. 20 GPSR — **unverzüglich** nach Kenntnis
- bei grenzüberschreitender Bedeutung: behördeninterne Weitergabe an das **Safety Gate** (vormals RAPEX) Art. 26 GPSR
- öffentlich zugängliche Datenbank Art. 34 GPSR (Verbraucherinformation)

### 5. Rückruf-Kommunikation

Inhalt einer Verbraucher-gerichteten Rückrufanzeige (Art. 36 IV GPSR; § 26 ProdSG übergangsweise):

- klare Bezeichnung des Produkts (Marke, Modell, Charge / Seriennummer)
- konkrete Beschreibung des Risikos in laienverständlicher Sprache
- klare Handlungsanweisung („Nutzung sofort einstellen", „Rückgabe an Verkaufsstelle gegen Erstattung")
- Kontaktstelle (Telefon, E-Mail, Web-Formular)
- keine relativierende oder werblich beruhigende Sprache („vorsorglicher Rückruf" nur wenn sachlich zutreffend)

### 6. Verzahnung mit anderen Pflichten

- **§ 1 ProdHaftG**: ein **erfolgter** Rückruf beseitigt nicht den Schadensersatzanspruch für bereits eingetretene Schäden, aber begrenzt Folgeschäden und Mitverschulden § 6 ProdHaftG
- **§ 823 I BGB**: rechtzeitiger Rückruf entlastet den Hersteller von Vorwurf des Produktbeobachtungsfehlers
- **Strafrecht**: BGH, **„Lederspray"** (Urt. v. 06.07.1990 – 2 StR 549/89, BGHSt 37, 106) `[unverifiziert – prüfen]` — Geschäftsleitung kann sich bei unterbliebenem Rückruf strafrechtlich wegen Körperverletzung (durch Unterlassen) verantworten
- **Versicherung**: Rückrufkosten oft nur über separate Rückrufkostenversicherung gedeckt (nicht in jeder Produkthaftpflicht enthalten)

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html)
- [§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)
- [VO (EU) 2023/988 (GPSR), Art. 20, 22, 26, 34, 36](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R0988)
- [VO (EU) 2019/1020 (MarktüberwachungsVO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R1020)
- [§ 26 ProdSG](https://www.gesetze-im-internet.de/prodsg_2021/__26.html) (Übergang)
- [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html) (Anhörung)
- [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html) (Begründung)
- [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html) (Sofortvollzug)
- [§§ 70, 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html) (Rechtsbehelfsfristen)
- [Art. 12 GG](https://www.gesetze-im-internet.de/gg/art_12.html), [Art. 14 GG](https://www.gesetze-im-internet.de/gg/art_14.html)

### Kommentare

- Wagner, in: MüKoBGB, 9. Aufl. 2024, § 823 Rn. 800 ff. (Produktbeobachtung, Rückrufpflicht)
- Klindt, GPSR-Kommentar, 1. Aufl. 2024 ff., Art. 36 `[unverifiziert – Verlag/Aufl. prüfen]`
- Wilrich, Produktsicherheitsrecht, 2. Aufl. 2024, Rückruf-Kapitel `[unverifiziert – Aufl./Jahr prüfen]`
- Kopp/Ramsauer, VwVfG, 24. Aufl. 2023, § 28 Rn. 1 ff. (Anhörung)
- Schoch/Schneider, VwGO, Stand 2024, § 80 Rn. 1 ff. (Sofortvollzug)

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BGH, Urt. v. 16.12.2008 – VI ZR 170/07, NJW 2009, 1080 („Pflegebetten", zivilrechtliche Rückrufpflicht und Reaktionsstufung)
2. BGH, Urt. v. 06.07.1990 – 2 StR 549/89, BGHSt 37, 106 („Lederspray", strafrechtliche Rückrufpflicht der Geschäftsleitung)
3. BVerwG, Urt. v. 26.10.2017 – 7 C 21.15 (Marktaufsichtsanordnung nach ProdSG; auf GPSR-Anordnungen übertragbar) `[unverifiziert]`
4. EuGH, Urt. v. 05.03.2015 – C-503/13, C-504/13, ECLI:EU:C:2015:148 (Boston Scientific, präventive Maßnahmen bei potenziellen Risiken)

## Ausgabeformat

```
RÜCKRUF-PRÜFUNG
Mandat: <Hersteller / Importeur / Marktaufsicht / Adressat>
Produkt: <Bezeichnung, Charge>

I. Sachverhalt und Risikobewertung
   – Schadensbild und Häufigkeit
   – betroffene Charge / Gesamtbestand
   – Risikogruppe

II. Zivilrechtliche Rückrufpflicht (§ 823 I BGB)
    1. Produktbeobachtungspflicht (BGH „Pflegebetten")
    2. Maßnahmenstufung
       ☐ Warnung  ☐ Empfehlung  ☐ Reparatur  ☐ Rückruf  ☐ Vernichtung
    3. Begründung der gewählten Stufe (Verhältnismäßigkeit / Effektivität)

III. Öffentlich-rechtliche Anordnung (Art. 36 GPSR + sektoral)
     1. Rechtsgrundlage
     2. Anhörung § 28 VwVfG
     3. Begründung § 39 VwVfG
     4. Verhältnismäßigkeit Art. 20 III GG
     5. ggf. Sofortvollzug § 80 II Nr. 4 VwGO
     6. Rechtsbehelf §§ 70, 74 VwGO (1 Monat)

IV. Meldungen
    – Safety Business Gateway Art. 20 GPSR (unverzüglich)
    – Information Versicherer (Produkthaftpflicht / Rückrufkosten)

V. Entwurf der Rückruf-Bekanntmachung (laienverständlich)

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Maßnahmenstufe unterdimensioniert.** Wenn das Risiko Leib und Leben betrifft, genügt eine bloße Warnung idR nicht (BGH „Pflegebetten" `[unverifiziert]`).
- **„Vorsorglicher Rückruf" als Etikett.** Wenn das Risiko tatsächlich erheblich ist, ist die Verharmlosung haftungsrelevant; sachlich-klare Sprache.
- **Anhörung § 28 VwVfG übersprungen** ohne tragenden Gefahr-im-Verzug-Grund — Anordnung formell rechtswidrig.
- **Sofortvollzugs-Begründung pauschal.** Nach § 80 III VwGO muss das besondere Vollziehungsinteresse einzelfallbezogen dargelegt werden.
- **Klagefrist § 74 VwGO** (1 Monat ab Bekanntgabe) versäumt — Anordnung bestandskräftig.
- **Safety-Business-Gateway-Meldung verspätet** — eigenständiger Pflichtenverstoß Art. 20 GPSR, unabhängig von der Rückrufentscheidung.
- **Rückrufkostenversicherung nicht geprüft** — Standardprodukthaftpflicht deckt die Rückrufkosten in der Regel nicht.
- **Parallele Strafbarkeit der Geschäftsleitung** („Lederspray"-Linie `[unverifiziert]`) bei unterbliebenem Rückruf nicht adressiert.
