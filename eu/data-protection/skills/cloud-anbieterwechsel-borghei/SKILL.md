---
name: cloud-anbieterwechsel-borghei
title: /datenwirtschaftsrecht:cloud-anbieterwechsel
description: Anbieterwechsel bei Datenverarbeitungsdiensten nach Kapitel VI der EU-Datenverordnung – Beseitigung von Wechselhindernissen Art. 23, Funktionsäquivalenz Art. 24, zwingender Klauselkatalog des Wechselvertrags Art. 25 mit maximaler Kündigungsfrist von zwei Monaten, Übergangsfrist von höchstens 30 Kalendertagen und Mindestabrufzeit von 30 Kalendertagen, Informationspflichten Art. 26, Treu und Glauben Art. 27, Transparenz Art. 28, schrittweise Abschaffung der Wechselentgelte Art. 29 (entgeltfrei ab 12.01.2027), technische Aspekte Art. 30, Ausnahmen für maßgeschneiderte und Testdienste Art. 31 sowie Schutz vor unrechtmäßigem staatlichem Zugang Art. 32. Use when ein Cloud-, SaaS-, PaaS- oder IaaS-Vertrag auf Wechselkonformität zu prüfen, ein Exit zu planen oder ein Wechselhindernis anzugreifen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenwirtschaftsrecht/skills/cloud-anbieterwechsel
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: de
---

# /datenwirtschaftsrecht:cloud-anbieterwechsel

## Zweck

Der Skill prüft Verträge über Datenverarbeitungsdienste an den zwingenden Wechselvorgaben des Kapitels VI der Datenverordnung, entwirft den Exit-Fahrplan mit den drei maßgeblichen Fristen und benennt die Hebel gegen faktische Lock-in-Praktiken. Er trennt dabei sauber, was der Anbieter **vertraglich** schuldet (Art. 25), was er **technisch** schuldet (Art. 24, 30) und was er **nicht mehr berechnen** darf (Art. 29).

## Eingaben

- Vertragsart: IaaS, PaaS, SaaS; Dienstart und ob ein funktionsäquivalenter Dienst am Markt existiert
- Vertragsdatum, Laufzeit, Kündigungsregelung, vereinbarte Exit-Klauseln
- Aktuelle Entgeltstruktur: Standarddienstentgelte, Egress-Gebühren, Wechsel- und Kündigungsentgelte
- Datenbestand: exportierbare Daten, digitale Vermögenswerte, anbieterspezifische Datenkategorien
- Zielumgebung: anderer Anbieter, eigene IKT-Infrastruktur, Parallelbetrieb
- Ob der Dienst maßgeschneidert oder als Test-/Bewertungsversion erbracht wird (Art. 31)
- Regulatorische Zusatzanforderungen, insbesondere DORA für Finanzunternehmen

## Sub-Agent-Architektur

Der Researcher beschafft Normtext, Erwägungsgründe und Verlautbarungen der Bundesnetzagentur sowie – bei Finanzunternehmen – die einschlägigen DORA-Vorgaben. Der Drafter gleicht den Vertrag Klausel für Klausel gegen den Katalog des Art. 25 Abs. 2 ab und entwirft die fehlenden Klauseln. Der Reviewer prüft die Fristenkette, die Entgeltlage nach Art. 29 und ob eine Ausnahme nach Art. 31 tatsächlich vorliegt oder nur behauptet wird.

## Ablauf

### 1. Anwendbarkeit klären

Kapitel VI gilt für **Datenverarbeitungsdienste** — digitale Dienste, die eine bedarfsgesteuerte Verwaltung und einen breiten Fernzugang zu einem skalierbaren und elastischen Pool gemeinsam nutzbarer Rechenressourcen ermöglichen. Erfasst sind IaaS, PaaS und SaaS.

Ausnahmen nach **Art. 31**:

- **Abs. 1** — für Dienste, deren zentrale Funktionen ganz überwiegend auf die spezifischen Bedürfnisse eines **einzelnen Kunden** zugeschnitten oder deren Komponenten sämtlich für diesen entwickelt wurden **und** die nicht im größeren kommerziellen Maßstab über den Dienstleistungskatalog angeboten werden, gelten Art. 23 Buchst. d, Art. 29 und Art. 30 Abs. 1, 3 nicht.
- **Abs. 2** — für nicht als Vollversion, sondern zu Test- und Bewertungszwecken und zeitlich begrenzt bereitgestellte Dienste gelten die Pflichten des Kapitels nicht.
- **Abs. 3** — der Anbieter muss den potenziellen Kunden **vor Vertragsschluss** über die nicht geltenden Pflichten unterrichten. Unterbleibt diese Unterrichtung, ist die Berufung auf die Ausnahme angreifbar.

Nach **Art. 24** gelten die Pflichten nur für Dienste, Verträge und Geschäftsgepflogenheiten, die der **ursprüngliche Anbieter** angeboten hat — nicht für Fremdleistungen im Ökosystem.

### 2. Wechselhindernisse identifizieren (Art. 23)

Anbieter dürfen keine vorkommerziellen, gewerblichen, technischen, vertraglichen oder organisatorischen Hindernisse aufzwingen und müssen bestehende beseitigen, wenn sie Kunden daran hindern,

- a) den Vertrag nach Ablauf der maximalen Kündigungsfrist und nach erfolgreichem Wechsel zu **kündigen**;
- b) **neue Verträge** mit einem anderen Anbieter derselben Dienstart zu schließen;
- c) exportierbare Daten und digitale Vermögenswerte zu einem anderen Anbieter oder in die **eigene IKT-Infrastruktur** zu übertragen — auch nach Inanspruchnahme eines unentgeltlichen Angebots;
- d) nach Art. 24 die **Funktionsäquivalenz** in der Umgebung eines anderen Anbieters derselben Dienstart zu erreichen;
- e) die Dienste nach Art. 30 Abs. 1 von anderen Diensten desselben Anbieters zu **trennen**, soweit technisch durchführbar.

Typische Hindernisse in der Praxis: prohibitive Egress-Entgelte, proprietäre Exportformate ohne Dokumentation, Bindung von Rabatten an Mindestabnahmen über den Wechselzeitpunkt hinaus, Verweigerung der Herausgabe von Konfigurations- und Metadaten, Supportverweigerung während des Wechsels.

### 3. Vertragsklauseln gegen Art. 25 Abs. 2 abgleichen

Der Wechselvertrag ist **schriftlich** zu schließen und dem Kunden vor Unterzeichnung so bereitzustellen, dass er ihn speichern und reproduzieren kann (Art. 25 Abs. 1). Er muss mindestens enthalten:

| Buchst. | Zwingender Inhalt |
|---|---|
| a | Wechselrecht des Kunden; Übertragung aller exportierbaren Daten und digitalen Vermögenswerte unverzüglich, spätestens nach Ablauf einer **verbindlichen Übergangsfrist von höchstens 30 Kalendertagen** ab Ablauf der maximalen Kündigungsfrist; dabei angemessene Unterstützung, Sorgfalt zur Aufrechterhaltung des Geschäftsbetriebs, Risikoaufklärung und hohes Sicherheitsniveau |
| b | Pflicht zur Unterstützung der **Ausstiegsstrategie** des Kunden einschließlich Bereitstellung aller einschlägigen Informationen |
| c | Klausel zur Vertragsbeendigung und Unterrichtung des Kunden — nach erfolgreichem Wechsel oder nach Ablauf der maximalen Kündigungsfrist bei Löschungswunsch |
| d | **Maximale Kündigungsfrist für die Einleitung des Wechsels: höchstens zwei Monate** |
| e | Erschöpfende Auflistung aller übertragbaren Daten- und Vermögenswertkategorien, mindestens aller exportierbaren Daten |
| f | Erschöpfende Liste der anbieterspezifischen, von der Übertragung ausgenommenen Datenkategorien — nur bei Gefahr der Verletzung von Geschäftsgeheimnissen des Anbieters und nur, soweit der Wechsel dadurch nicht behindert oder verzögert wird |
| g | **Mindestfrist für den Datenabruf von mindestens 30 Kalendertagen** ab Ablauf des Übergangszeitraums |
| h | Garantie der vollständigen Löschung aller exportierbaren Daten und digitalen Vermögenswerte nach Ablauf der Abruffrist |

Die Fristenkette lautet damit: **Wechselverlangen → maximal 2 Monate Kündigungsfrist → maximal 30 Kalendertage Übergangsfrist → mindestens 30 Kalendertage Abrufzeitraum → Löschung.**

### 4. Entgelte prüfen (Art. 29)

| Zeitraum | Zulässig |
|---|---|
| 11.01.2024 bis 11.01.2027 | **ermäßigte Wechselentgelte**, die die dem Anbieter unmittelbar durch den Wechsel entstehenden Kosten nicht übersteigen dürfen (Abs. 2, 3) |
| **ab 12.01.2027** | **keine Wechselentgelte** mehr (Abs. 1) |

Flankierend: Vor Vertragsschluss ist eindeutig über Standarddienstentgelte, Sanktionen bei vorzeitiger Kündigung und die während der Übergangszeit möglichen ermäßigten Wechselentgelte zu unterrichten (Abs. 4). Dienste, bei denen der Wechsel besonders kompliziert, kostspielig oder ohne erhebliche Eingriffe unmöglich ist, sind zu benennen (Abs. 5); die Informationen sind auf der Website oder anderweitig leicht zugänglich zu veröffentlichen (Abs. 6).

Zu unterscheiden ist zwischen **Wechselentgelten** (fallen weg) und **Standarddienstentgelten** für die laufende Nutzung (bleiben zulässig). Als Wechselentgelt getarnte Egress-Gebühren sind der Kern des Streits.

### 5. Technische Ebene (Art. 30, Art. 34, Art. 35)

Für Dienste betreffend skalierbare und elastische Rechenressourcen, die nur Infrastrukturelemente bereitstellen, schuldet der Anbieter nach Art. 30 Abs. 1 die **Funktionsäquivalenz** in der Zielumgebung. Für andere Dienstarten sind offene Schnittstellen und – soweit einschlägig – die Kompatibilität mit offenen Interoperabilitätsspezifikationen oder harmonisierten Normen bereitzustellen. Art. 34 und Art. 35 flankieren die Interoperabilität bei paralleler Nutzung.

### 6. Staatlicher Zugang im internationalen Umfeld (Art. 32)

Anbieter haben alle angemessenen technischen, organisatorischen und rechtlichen Maßnahmen zu treffen, um den staatlichen Zugang zu und die Übermittlung von in der Union gespeicherten nicht personenbezogenen Daten durch Drittstaaten zu verhindern, soweit dies dem Unionsrecht oder dem nationalen Recht widerspricht. Für personenbezogene Daten bleibt Kapitel V DSGVO maßgeblich (`/datenschutzrecht:avv-pruefung`).

### 7. Durchsetzung

Zuständig ist die **Bundesnetzagentur** ([§ 2 Abs. 1 DADG](https://www.gesetze-im-internet.de/dadg/__2.html)); Beschwerde nach Art. 38, Durchsetzung nach [§§ 6 bis 14 DADG](https://www.gesetze-im-internet.de/dadg/__6.html), Bußgeld nach [§ 15 DADG](https://www.gesetze-im-internet.de/dadg/__15.html) — unter anderem für die unterbliebene Mitteilung nach Art. 25 Abs. 4. Für **Finanzunternehmen** treten die Ausstiegsstrategie- und Kündigungsvorgaben der DORA hinzu (`/dora:ikt-drittparteienrisiko`); die strengere Anforderung setzt sich durch.

## Deterministische Berechnung

Die Fristenkette des Art. 25 ist kalendarisch und damit rechenbar. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik — die Bestimmung des Wechselverlangens und die Frage, wann der Wechsel „erfolgreich vollzogen" ist, bleiben juristische Eingaben:

```bash
# 1) Maximale Kündigungsfrist Art. 25 Abs. 2 Buchst. d: 2 Monate ab Wechselverlangen 01.03.2026
python -m scripts.legal_calc.cli frist --ereignis 01.03.2026 --menge 2 --einheit monate --land BY

# 2) Übergangsfrist Art. 25 Abs. 2 Buchst. a: höchstens 30 Kalendertage ab Ablauf der Kündigungsfrist
python -m scripts.legal_calc.cli frist --ereignis 01.05.2026 --menge 30 --einheit tage --land BY

# 3) Mindestabrufzeitraum Art. 25 Abs. 2 Buchst. g: mindestens 30 Kalendertage ab Ende des Übergangs
python -m scripts.legal_calc.cli frist --ereignis 31.05.2026 --menge 30 --einheit tage --land BY
```

`--json` liefert die Rechenschritte. Die 30-Tage-Fristen sind **Kalendertage**, keine Werktage.

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/2854, Art. 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 38, 50 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- [§ 2 DADG](https://www.gesetze-im-internet.de/dadg/__2.html), [§ 6 DADG](https://www.gesetze-im-internet.de/dadg/__6.html), [§ 15 DADG](https://www.gesetze-im-internet.de/dadg/__15.html)
- Verordnung (EU) 2022/2554 (DORA), Art. 28, 30 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- Richtlinie (EU) 2019/770 (digitale Inhalte und Dienstleistungen) — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/770/oj)

### Kommentare und Literatur

- Hennemann/Steinrötter, Data Act – Handkommentar, Art. 23 ff.
- Specht-Riemenschneider/Hennemann, Data Act, Kommentar, Art. 25, Art. 29.
- Schuster/Grützmacher, IT-Recht, Kap. Cloud-Verträge und Exit-Management.
- Beiträge zu Egress-Gebühren und Lock-in in CR und MMR 2024/2025 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zu Kapitel VI der Datenverordnung liegt keine Judikatur vor. Für die AGB-rechtliche Flankierung von Cloud-Verträgen ist die Rechtsprechung zu §§ 307 ff. BGB heranzuziehen; jede Entscheidung ist vor Verwendung zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
CLOUD-EXIT-PRÜFUNG — <Vertrag / Anbieter> — <Datum>

I.   Anwendbarkeit
     Dienstart:               <IaaS / PaaS / SaaS>
     Ausnahme Art. 31:        [Abs. 1 maßgeschneidert / Abs. 2 Testdienst / keine]
     Unterrichtung Abs. 3:    [erfolgt / fehlt — Ausnahme angreifbar]
     Zusatzregime:            [DORA / keines]

II.  Wechselhindernisse Art. 23
     Buchst. a–e:             <Feststellungen je Buchstabe>
     Faktische Hindernisse:   <Egress-Entgelte / Formate / Support / Rabattbindung>

III. Klauselabgleich Art. 25 Abs. 2
     Buchst. | gefordert | im Vertrag | Ergebnis
     a  Übergangsfrist ≤ 30 Kalendertage      | <…> | <konform / fehlt>
     b  Unterstützung der Ausstiegsstrategie  | <…> | <…>
     c  Beendigungs- und Unterrichtungsklausel| <…> | <…>
     d  Kündigungsfrist ≤ 2 Monate            | <…> | <…>
     e  Katalog exportierbarer Daten          | <…> | <…>
     f  Ausnahmeliste anbieterspezifischer Daten | <…> | <…>
     g  Abrufzeitraum ≥ 30 Kalendertage       | <…> | <…>
     h  Löschgarantie                          | <…> | <…>

IV.  Entgelte Art. 29
     Wechselentgelte:         <Betrag / Struktur>
     Zeitliche Einordnung:    [ermäßigt zulässig bis 11.01.2027 / unzulässig ab 12.01.2027]
     Als Wechselentgelt getarnte Egress-Kosten: [ja / nein]
     Vorvertragliche Information Abs. 4–6:     [vollständig / lückenhaft]

V.   Exit-Fahrplan
     Wechselverlangen:        <Datum>
     Kündigungsfrist endet:   <Datum>
     Übergangsfrist endet:    <Datum>
     Abrufzeitraum endet:     <Datum>
     Löschung geschuldet ab:  <Datum>

VI.  Durchsetzung
     Beschwerde Art. 38 iVm § 6 DADG | Bußgeldrisiko § 15 DADG | Zivilrechtliche Ansprüche

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Egress-Gebühren als Standarddienstentgelt durchgewinkt.** Entgelte, die wirtschaftlich den Wechsel verteuern, sind an Art. 29 zu messen; ab dem 12.01.2027 sind Wechselentgelte unzulässig.
- **Kündigungsfrist über zwei Monate akzeptiert.** Art. 25 Abs. 2 Buchst. d setzt eine Höchstgrenze, keine Regelfrist.
- **Übergangs- und Abruffrist verwechselt.** Die Übergangsfrist beträgt **höchstens** 30 Kalendertage, der Abrufzeitraum **mindestens** 30 Kalendertage — und er beginnt erst danach.
- **Werktage statt Kalendertage gerechnet.** Art. 25 spricht durchgehend von Kalendertagen.
- **Ausnahme nach Art. 31 behauptet, ohne die Unterrichtung nach Abs. 3 zu belegen.**
- **Ausnahmeliste nach Buchst. f überdehnt.** Sie rechtfertigt nur den Ausschluss anbieterspezifischer Datenkategorien und darf den Wechsel weder behindern noch verzögern.
- **Löschgarantie nach Buchst. h übersehen.** Sie ist zwingender Vertragsbestandteil, nicht Kulanz.
- **DORA-Anforderungen ignoriert.** Für Finanzunternehmen gelten zusätzliche Ausstiegs- und Kündigungsvorgaben; die strengere Anforderung setzt sich durch.
- **Rechtsprechung erfunden.** Zu Kapitel VI gibt es keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
