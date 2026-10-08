---
name: gwg-risikoanalyse-borghei
title: /geldwaesche-aml-kyc:gwg-risikoanalyse
description: Aufbau und Aktualisierung der institutsspezifischen Risikoanalyse nach § 5 GwG – Risikokategorien (Kunde / Produkt / Vertriebsweg / Geografie), Berücksichtigung Supranationale und Nationale Risk Assessment, Risikoklassen und Ableitung des Pflichtenniveaus §§ 10–17 GwG. Use when ein Verpflichteter iSv § 2 GwG die Risikoanalyse erstmals erstellen, jährlich fortschreiben oder anlassbezogen anpassen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/geldwaesche-aml-kyc/skills/gwg-risikoanalyse
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /geldwaesche-aml-kyc:gwg-risikoanalyse

## Zweck

Der Skill erzeugt das Grundgerüst einer **dokumentierten** Risikoanalyse nach § 5 GwG, ordnet Risikofaktoren den vier Pflichtkategorien (Kunde, Produkt / Dienstleistung, Vertriebsweg, geografisches Risiko) zu und leitet daraus das Sorgfaltspflichtenniveau (§§ 10, 14, 15 GwG) ab. Er stellt sicher, dass die Analyse die Supranationale Risikoanalyse der EU-Kommission und die Nationale Risikoanalyse des BMF berücksichtigt und mindestens jährlich oder anlassbezogen aktualisiert wird.

> **⚠️ Aktualität (Stand 2026-07):** **Rechtsgrundlage der Risikoanalyse ist weiterhin § 5 GwG.** Das EU-AML-Paket löst das GwG nicht heute, sondern zum 10.07.2027 ab — der Übergang gehört jedoch bereits jetzt in die Analyse und in den Aktualisierungsanlass:
>
> - **AMLA** (VO (EU) 2024/1620) ist seit dem **01.07.2025 in Frankfurt am Main operativ**. Sie wird ausgewählte Verpflichtete **unmittelbar** beaufsichtigen und koordiniert im Übrigen die nationalen Aufsichtsbehörden.
> - **AMLR** (VO (EU) 2024/1624) gilt ab **10.07.2027** als unmittelbar anwendbares **Single Rulebook** — ohne nationales Umsetzungsgesetz.
> - **AMLD6** (RL (EU) 2024/1640): Umsetzungsfrist für **Art. 11–13, 15** (Register wirtschaftlich Berechtigter) am **10.07.2026 abgelaufen**; allgemeine Umsetzungsfrist **10.07.2027**.
> - Der Großteil der **AMLA-Level-2-/Level-3-Maßnahmen** war zum **10.07.2026** fällig; rund **23 RTS/ITS und Leitlinien** stehen noch aus — darunter Konkretisierungen zu Risikobewertung und Risikofaktoren.
> - **EU-weite Bargeldobergrenze 10.000 EUR**, Mitgliedstaaten dürfen niedrigere Grenzen setzen — relevant für die Risikokategorie „Produkt/Dienstleistung" bei bargeldintensivem Geschäft. `[unverifiziert - prüfen]`
>
> **Konsequenz für diesen Skill:** Der bevorstehende AMLR-Wechsel ist ein **anlassbezogener Aktualisierungsgrund** iSd § 5 II GwG. Die Analyse ist so zu strukturieren, dass sie zum 10.07.2027 auf die AMLR umgehängt werden kann (siehe Schritt 7a).

## Eingaben

- Verpflichteten-Typ nach § 2 GwG (Kreditinstitut, Finanzdienstleister, Versicherer, Vermögensverwalter, RA / StB / Notar, Güterhändler ab Schwelle, Immobilienmakler, Edelmetall- / Kunsthändler, Glücksspielanbieter, Krypto-Verwahrer)
- Geschäftsmodell (Produktportfolio, Kundengruppen, Vertriebskanäle, geografische Reichweite)
- bestehende Risikoanalyse (falls vorhanden, mit Datum und letzter Aktualisierung)
- aufsichtsrechtlicher Rahmen (BaFin / Zoll / Landesaufsicht)
- besondere Vorfälle seit letzter Analyse (Verdachtsmeldungen, Prüfungsfeststellungen, Sanktionsverfahren)

## Sub-Agent-Architektur

Researcher liefert § 5 GwG mit Bezug zu § 4 (risikobasierter Ansatz) und § 6 (interne Sicherungsmaßnahmen), Supranationale + Nationale Risikoanalyse, BaFin- und FIU-Auslegungshinweise sowie Kommentarstellen. Drafter erstellt das Risikoanalyse-Dokument mit Methodik, Risikofaktoren-Matrix, Risikoklassen und Ableitung des Pflichtenniveaus. Reviewer prüft Vollständigkeit der vier Kategorien, Dokumentationsdichte, Aktualisierungsturnus und Anbindung an § 6 GwG-Sicherungsmaßnahmen.

## Ablauf

### 1. Verpflichteten-Eigenschaft

Vor Beginn klären, **welche** Nummer des § 2 I GwG einschlägig ist — der Pflichtenumfang variiert (z. B. § 2 I Nr. 1: Kreditinstitute; Nr. 10: RA / StB / Notare nur bei Katalogtätigkeiten; Nr. 14: Güterhändler erst ab Bargeldschwelle iSv § 4 V GwG). Bei mehrfacher Einstufung gilt das jeweils strengere Pflichtenregime.

### 2. Methodik der Risikoanalyse (§ 5 GwG)

Die Risikoanalyse muss schriftlich vorliegen, **nachvollziehbar** sein, und die Methodenwahl dokumentieren. Üblich:

- qualitative Bewertung pro Risikofaktor (niedrig / normal / hoch)
- quantitative Gewichtung (z. B. Scorecard)
- aggregierte Risikoklasse je Geschäftsbeziehung / Transaktion

Maßstab und Mindestinhalt: Herzog, GwG, X. Aufl. Jahr, § 5 Rn. 1 ff. `[unverifiziert – Auflage prüfen]`; BaFin, Auslegungs- und Anwendungshinweise zum GwG, Allgemeiner Teil.

### 3. Externe Quellen einbeziehen

- **Supranationale Risikoanalyse** der EU-Kommission (Art. 6 RL (EU) 2015/849, alle zwei Jahre)
- **Nationale Risikoanalyse (NRA)** des BMF (zuletzt aktualisiert; konkrete Ausgabe `[unverifiziert – Stand prüfen]`)
- **Sektorale Risikoanalysen** der zuständigen Aufsicht (BaFin für Banken / Versicherer / FDI; Landes-RAK / StBK / Notarkammer; Zoll-FIU; Glücksspielbehörde)
- **EU-Liste der Hochrisikoländer** (delegierte VO der KOM nach Art. 9 RL 2015/849)
- **FATF-Empfehlungen** und FATF-Länderlisten

### 4. Vier Risikokategorien (§ 5 I GwG)

| Kategorie | Beispielindikatoren (nicht abschließend) |
|---|---|
| **Kunde** | natürliche / juristische Person; Branche; PEP-Eigenschaft § 1 XII GwG; Nominee-Strukturen; bargeldintensives Geschäft; Bestandskunde vs. Neukunde |
| **Produkt / Dienstleistung** | Produkte mit Anonymitätspotenzial (Inhaberinstrumente, E-Geld, Krypto), grenzüberschreitende Zahlungen, Korrespondenzbank-Beziehungen, Trade Finance |
| **Vertriebsweg** | Präsenz-Onboarding vs. Fernidentifizierung (Videoident, eID); Vermittler / Tippgeber; nicht regulierte Intermediäre |
| **Geografisches Risiko** | EU-Hochrisikoländer-Liste; FATF-Listen; Offshore-Zentren; Sanktionsländer (UN, EU, OFAC); Korruptionsindex (TI CPI) |

### 5. Risikoklassen und Pflichtenniveau

| Risikoklasse | Pflichtenniveau | Norm |
|---|---|---|
| niedrig (mit nachgewiesener Begründung) | vereinfachte Sorgfalt | § 14 GwG |
| normal | allgemeine Sorgfalt | § 10 GwG |
| hoch (PEP, Hochrisikoland, komplexe Struktur, ungewöhnliches Transaktionsverhalten) | verstärkte Sorgfalt | § 15 GwG |

Die Zuordnung darf nicht pauschal sein — jede Klasse ist auf den konkreten Geschäftsvorgang anzuwenden.

### 6. Anbindung an § 6 GwG (interne Sicherungsmaßnahmen)

Die Risikoanalyse muss in konkrete Sicherungsmaßnahmen münden: Verfahren zur Kundenannahme, Monitoring, Mitarbeiterzuverlässigkeit, Schulung, GW-Beauftragter (§ 7 GwG, bei Kreditinstituten + Stellvertreter, MaRisk AT 4.4.3). Ohne diese Anbindung ist die Risikoanalyse formal unvollständig.

### 7. Aktualisierung

Mindestens **jährlich** und **anlassbezogen** (neue Produkte, neue Märkte, geänderte Aufsichtsleitlinien, neue NRA / SNRA, sichtbare Veränderung des Bedrohungsbildes). Aktualisierungen sind zu dokumentieren mit Datum, Anlass und Verantwortlichem.

### 7a. Vorbereitung auf AMLR, AMLA und AMLD6

Der Übergang auf das EU-AML-Paket ist kein künftiges Thema, sondern ein **anlassbezogener Aktualisierungsgrund** nach § 5 II GwG. Vier Arbeitsstränge gehören in die Analyse und in den Maßnahmenplan:

**a) Gap-Mapping der bestehenden GwG-Verfahren auf die AMLR (Stichtag 10.07.2027).** Jede in der Risikoanalyse verankerte Pflicht wird auf die entsprechende AMLR-Vorschrift abgebildet und eingeordnet als **deckungsgleich**, **verschärft** (Prozess- und IT-Vorlauf einplanen) oder **entfallend/abweichend**. Wichtig: Die AMLR ist **vollharmonisierend** — nationale Zusatzanforderungen, die heute selbstverständlich sind, lassen sich nicht ohne Weiteres fortschreiben. Das Mapping ist zu dokumentieren und mit Zuständigkeiten und Terminen zu versehen.

**b) UBO-Daten an der 25-%-Schwelle ausrichten.** Die Umsetzungsfrist der Register-Vorschriften (AMLD6 Art. 11–13, 15) ist am **10.07.2026 abgelaufen**. Die Analyse muss die Datenqualität zu wirtschaftlich Berechtigten als eigenen Risikofaktor der Kategorie „Kunde" abbilden — insbesondere bei mehrstufigen und grenzüberschreitenden Beteiligungsketten.

**c) AMLA-Level-2-Pipeline überwachen.** Rund 23 technische Standards und Leitlinien sind noch offen; sie konkretisieren gerade die Risikobewertung. In der Risikoanalyse ist ein **Verantwortlicher für das Monitoring** zu benennen, und Festlegungen, die von noch ausstehenden Standards abhängen, sind als **vorläufig** zu kennzeichnen.

**d) Auswahl zur direkten AMLA-Aufsicht prüfen.** Verpflichtete mit grenzüberschreitender Tätigkeit und erhöhtem Risikoprofil können unmittelbar der AMLA unterstellt werden. Die Selbsteinschätzung („Kommen wir in Betracht?") gehört in die Risikoanalyse; folgt daraus ein realistischer Kandidatenstatus, sind Dokumentationstiefe, Datenqualität und Ansprechstellen entsprechend zu heben. Auswahlkriterien und Zeitplan sind an der AMLA-Verordnung und den AMLA-Veröffentlichungen zu verifizieren. `[unverifiziert - prüfen]`

### 8. Bußgeldrisiko

Pflichtverletzung iSv § 5 GwG ist Ordnungswidrigkeit nach § 56 I Nr. 6 GwG `[unverifiziert – konkrete Nr. prüfen]`. Bußgeldrahmen bei vorsätzlichen Verstößen bis 1 Mio. EUR bzw. 10 % des jährlichen Gesamtumsatzes (§ 56 III GwG).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 4 GwG](https://www.gesetze-im-internet.de/gwg_2017/__4.html) (risikobasierter Ansatz)
- [§ 5 GwG](https://www.gesetze-im-internet.de/gwg_2017/__5.html) (Risikoanalyse)
- [§ 6 GwG](https://www.gesetze-im-internet.de/gwg_2017/__6.html) (interne Sicherungsmaßnahmen)
- [§ 7 GwG](https://www.gesetze-im-internet.de/gwg_2017/__7.html) (Geldwäschebeauftragter)
- [§§ 10, 14, 15 GwG](https://www.gesetze-im-internet.de/gwg_2017/__10.html) (Pflichtenniveau)
- [§ 56 GwG](https://www.gesetze-im-internet.de/gwg_2017/__56.html) (Bußgelder)
- [Art. 6, 7, 8 RL (EU) 2015/849](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L0849) (Risikobewertungspflichten)
- [VO (EU) 2024/1624 (AMLR — Single Rulebook)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1624) — unmittelbar anwendbar ab **10.07.2027**; Vorschriften zur Risikobewertung, zu Sorgfaltspflichten und zur EU-weiten Bargeldobergrenze von 10.000 EUR. Konkrete Artikelzuordnung am Verordnungstext verifizieren `[unverifiziert - prüfen]`
- [RL (EU) 2024/1640 (AMLD6)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1640) — Art. 11–13, 15 (Register wirtschaftlich Berechtigter) Umsetzungsfrist **10.07.2026**; allgemeine Umsetzungsfrist **10.07.2027**
- [VO (EU) 2024/1620 (AMLA-Verordnung)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1620) — AMLA seit **01.07.2025** in Frankfurt am Main operativ; direkte Aufsicht über ausgewählte Verpflichtete, Level-2-/Level-3-Rechtsetzung

### Verwaltungsvorschriften

- BaFin, Auslegungs- und Anwendungshinweise zum GwG, Allgemeiner Teil und Besonderer Teil Kreditinstitute
- FIU-Auslegungs- und Anwendungshinweise (für Nichtfinanzsektor)
- BMF, Nationale Risikoanalyse `[unverifiziert – aktuellen Stand prüfen]`
- EU-Kommission, Supranational Risk Assessment, COM(2022) 554 final `[unverifiziert – aktuelle Ausgabe prüfen]`
- MaRisk (AT 4.4.3 Compliance-Funktion, BT 5 GW-Prävention)

### Kommentare

- Herzog, GwG, X. Aufl. Jahr, § 5 Rn. 1 ff. `[unverifiziert – Auflage prüfen]`
- Bülte, GwG, § 5 Rn. 1 ff. `[unverifiziert]`
- Kreitmair, GwG, § 5 Rn. 1 ff. `[unverifiziert]`
- Quedenfeld, Handbuch Bekämpfung Geldwäsche und Wirtschaftskriminalität, X. Aufl., Kap. zu Risikomanagement `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

- Bußgeld-Rspr. zu § 56 GwG (Aufsichts- und Verwaltungsgerichte, vereinzelt KG / OLG) — konkrete Aktenzeichen sind im Modellwissen nicht zuverlässig erinnerbar; in juris mit Suchstring „GwG Risikoanalyse Bußgeld" recherchieren.

## Ausgabeformat

```
RISIKOANALYSE — § 5 GwG
Verpflichteter: <Firma / Kanzlei>, § 2 I Nr. <…> GwG
Stand: <Datum>   Verantwortlich: <Name GW-Beauftragter>
Letzte Aktualisierung: <Datum>   Nächste Wiedervorlage: <Datum + 12 Monate>

I.   Methodik
     - Bewertungslogik (qualitativ / quantitativ / Scorecard)
     - Berücksichtigte externe Quellen (SNRA, NRA, BaFin-AuA, FATF)

II.  Risikofaktoren
     1. Kunde
        - <Faktor> → Bewertung (niedrig / normal / hoch) → Begründung
     2. Produkt / Dienstleistung
     3. Vertriebsweg
     4. Geografisches Risiko

III. Risikoklassen und Pflichtenniveau
     - niedrig → § 14 GwG (vereinfachte Sorgfalt)
     - normal → § 10 GwG
     - hoch   → § 15 GwG (verstärkte Sorgfalt)

IV.  Interne Sicherungsmaßnahmen § 6 GwG
     - Kundenannahme, Monitoring, Mitarbeiterschulung, GW-Beauftragter

V.   Aktualisierungsregime
     - jährlich + anlassbezogen

V-a. Übergang EU-AML-Paket
     - Gap-Mapping GwG → AMLR (Stichtag 10.07.2027): <Stand, Verantwortlicher, Termin>
     - UBO-Datenqualität / 25-%-Schwelle (AMLD6 Art. 11–13, 15; Frist 10.07.2026): <…>
     - AMLA-Level-2-Pipeline (offene RTS/ITS/Leitlinien): <Monitoring-Verantwortlicher>
     - Kandidat für direkte AMLA-Aufsicht? <ja / nein / offen — Begründung>

VI.  Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Risikoklassen und Pflichtenniveau**
>
> Die Geschäftsbeziehung zu einer in Deutschland ansässigen mittelständischen GmbH ohne PEP-Bezug und ohne Hochrisikoland-Bezug fällt nach den unter II. zusammengetragenen Indikatoren in die Risikoklasse „normal". Anwendbar ist daher § 10 I GwG (allgemeine Sorgfaltspflichten: Identifizierung des Vertragspartners, Abklärung des wirtschaftlich Berechtigten gem. §§ 10 I Nr. 2, 11 V GwG, Klärung von Zweck und angestrebter Art der Geschäftsbeziehung, kontinuierliche Überwachung). Eine vereinfachte Sorgfalt nach § 14 GwG kommt nicht in Betracht, weil eine nachgewiesen niedrige Risikolage iSd § 14 I GwG nicht belegt ist; das pauschale Argument „inländischer Mittelstand" trägt nicht (vgl. Herzog, GwG, § 14 Rn. 12 ff. `[unverifiziert]`).

## Risiken / typische Fehler

- **Risikoanalyse als „Schubladendokument"** ohne Anbindung an konkrete Sicherungsmaßnahmen (§ 6 GwG) — formaler Verstoß, Bußgeldrisiko nach § 56 GwG.
- **Pauschale Einstufung „niedriges Risiko"** ohne Begründung der vereinfachten Sorgfalt § 14 GwG — Aufsicht und FIU-AuA verlangen Einzelfallbegründung.
- **PEP-Status unbeachtet** — § 1 XII GwG erfasst auch ausländische und nationale Amtsträger sowie Angehörige; ohne strukturierte PEP-Abfrage ist § 15 III GwG verletzt.
- **Keine Aktualisierung** seit > 12 Monaten oder trotz neuer NRA / EU-Hochrisikoliste — verletzt § 5 II GwG.
- **GW-Beauftragter ohne Stellvertreter** bei Verpflichteten mit entsprechender Pflicht (§ 7 GwG iVm Branchenspezifik) — MaRisk-Verstoß bei Kreditinstituten.
- **AMLR-/AMLA-Übergang ignoriert** — ab **10.07.2027** greifen die vollharmonisierten Pflichten der AMLR unmittelbar. Wer das Gap-Mapping erst 2027 beginnt, hat für IT- und Prozessanpassungen keinen Vorlauf mehr.
- **AMLR bereits heute als Prüfungsmaßstab verwendet** — bis zum 10.07.2027 ist **§ 5 GwG** die Rechtsgrundlage der Risikoanalyse. Eine auf die AMLR gestützte Analyse ist derzeit aufsichtsrechtlich unbrauchbar.
- **Auf ein nationales AMLR-Umsetzungsgesetz gewartet** — die AMLR ist eine **Verordnung** und gilt unmittelbar; nur die AMLD6 wird national umgesetzt.
- **Vollharmonisierung unterschätzt** — nationale Zusatzanforderungen aus dem GwG lassen sich unter der AMLR nicht ohne Weiteres fortschreiben. Das Gap-Mapping muss auch **entfallende** Pflichten ausweisen, nicht nur Lücken.
- **UBO-Datenqualität nicht als Risikofaktor abgebildet** — die AMLD6-Frist für die Register-Vorschriften (Art. 11–13, 15) ist am **10.07.2026** abgelaufen; lückenhafte Ketten oberhalb der **25-%-Schwelle** sind ein typischer Prüfungsbefund.
- **Noch offene AMLA-Level-2-Standards als final behandelt** — rund 23 RTS/ITS und Leitlinien stehen aus; darauf gestützte Festlegungen sind als vorläufig zu kennzeichnen und mit einem Monitoring-Verantwortlichen zu versehen.
- **Direkte AMLA-Aufsicht nicht selbst eingeschätzt** — die AMLA (seit 01.07.2025 in Frankfurt operativ) beaufsichtigt ausgewählte Verpflichtete unmittelbar; die Selbsteinschätzung gehört in die Risikoanalyse.
