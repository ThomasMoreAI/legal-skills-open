---
name: krypto-marktmissbrauch-borghei
title: /krypto-mikar:krypto-marktmissbrauch
description: Marktmissbrauch bei Kryptowerten – Geltungsbereich der Vorschriften über Marktmissbrauch Art. 86 VO (EU) 2023/1114, Begriff der Insiderinformation Art. 87, Pflicht zur Offenlegung von Insiderinformationen Art. 88 nebst zulässigem Aufschub, Verbot von Insidergeschäften Art. 89, Verbot der unrechtmäßigen Offenlegung Art. 90, Verbot der Marktmanipulation Art. 91 mit den Fallgruppen falscher Signale, Kursbeeinflussung und irreführender Handlungen, Pflicht zur Vorbeugung und Aufdeckung Art. 92 mit Systemen zur Erkennung und Meldung verdächtiger Aufträge, Verfolgung durch die BaFin §§ 31 bis 36 KMAG einschließlich Verschwiegenheit § 32, Anzeige straftatbegründender Tatsachen § 33, Handelsaussetzung § 34 und Übermittlung von Insiderinformationen § 36 sowie Straf- und Bußgeldvorschriften §§ 46, 47 KMAG. Use when ein Verdacht auf Insiderhandel oder Marktmanipulation besteht, ein Meldesystem aufzubauen oder eine Ad-hoc-Entscheidung zu treffen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/krypto-mikar/skills/krypto-marktmissbrauch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /krypto-mikar:krypto-marktmissbrauch

## Zweck

Der Skill überträgt das aus dem Wertpapierrecht bekannte Marktmissbrauchsregime auf Kryptowerte — mit den Abweichungen, die MiCAR und KMAG vorsehen. Er beantwortet die drei operativen Fragen: Liegt eine Insiderinformation vor, ist sie offenzulegen oder darf der Aufschub greifen, und welche Systeme schuldet ein Betreiber zur Erkennung verdächtiger Aufträge.

## Eingaben

- Betroffene Kryptowerte und deren Handelszulassung
- Rolle des Mandanten: Emittent, Anbieter, Betreiber einer Handelsplattform, Anbieter von Kryptowerte-Dienstleistungen, Person mit Führungsaufgaben
- Sachverhalt: Information, Zeitpunkt der Entstehung, Kreis der Wissenden, geplante oder erfolgte Transaktionen
- Bestehende Compliance-Systeme: Insiderverzeichnis, Handelsüberwachung, Meldeprozesse
- Ob bereits eine Offenlegung erfolgt ist oder ein Aufschub beschlossen wurde
- Ob die BaFin bereits Auskunft verlangt oder Maßnahmen angekündigt hat

## Sub-Agent-Architektur

Der Researcher beschafft MiCAR Titel VI, das KMAG und — als Auslegungshilfe — die Praxis zur Marktmissbrauchsverordnung. Der Drafter nimmt die Subsumtion vor und entwirft Offenlegung, Aufschubdokumentation oder Verdachtsmeldung. Der Reviewer prüft, ob die MAR-Praxis nicht unbesehen übertragen wurde und ob die Aufschubvoraussetzungen dokumentiert sind.

## Ablauf

### 1. Geltungsbereich bestimmen (Art. 86 MiCAR)

Die Vorschriften über Marktmissbrauch gelten für Handlungen jeder Person in Bezug auf Kryptowerte, die **zum Handel zugelassen** sind oder für die ein **Antrag auf Zulassung zum Handel** gestellt wurde. Erfasst sind Geschäfte, Aufträge und Handlungen — unabhängig davon, ob sie auf einer Handelsplattform ausgeführt werden.

**Abgrenzung, die zu Beginn zu treffen ist:** Ist der Kryptowert ein **Finanzinstrument**, gilt die **Marktmissbrauchsverordnung (MAR)** und nicht Titel VI der MiCAR (`/kapitalmarktrecht:wphg-marktmissbrauch`). Beide Regime sind ähnlich strukturiert, aber nicht deckungsgleich; eine unbesehene Übertragung der MAR-Praxis — etwa zu Aufschubgründen oder Insiderverzeichnissen — ist zu vermeiden und im Einzelfall zu begründen.

### 2. Insiderinformation prüfen (Art. 87 MiCAR)

Eine Insiderinformation ist eine **nicht öffentlich bekannte, präzise Information**, die direkt oder indirekt einen oder mehrere Kryptowerte oder deren Emittenten betrifft und die, wenn sie öffentlich bekannt würde, geeignet wäre, den **Kurs erheblich zu beeinflussen**.

Prüfschema:

| Merkmal | Prüfung |
|---|---|
| **präzise** | Umstände existieren oder werden vernünftigerweise eintreten; hinreichend spezifisch für einen Schluss auf die Kurswirkung; bei gestreckten Vorgängen kann auch ein **Zwischenschritt** präzise sein |
| **nicht öffentlich bekannt** | keine Verbreitung, die einem breiten Anlegerkreis Zugang eröffnet |
| **Kryptowertbezug** | direkt oder indirekt |
| **Kursrelevanz** | ein verständiger Anleger würde die Information als Teil seiner Anlageentscheidung nutzen |

### 3. Offenlegung und Aufschub (Art. 88 MiCAR)

Emittenten, Anbieter und Personen, die die Zulassung zum Handel beantragen, haben Insiderinformationen, die sie unmittelbar betreffen, **öffentlich bekannt zu geben** — so, dass ein schneller Zugang und eine vollständige, korrekte und rechtzeitige Bewertung möglich sind.

Ein **Aufschub** ist unter den in Art. 88 genannten Voraussetzungen zulässig; er verlangt regelmäßig ein berechtigtes Interesse, die fehlende Eignung zur Irreführung der Öffentlichkeit und die Sicherstellung der Vertraulichkeit. **Der Aufschubbeschluss ist zu dokumentieren** — Zeitpunkt, Gründe, Verantwortliche, Vertraulichkeitsmaßnahmen — und die zuständige Behörde ist nach Maßgabe des Art. 88 zu unterrichten. Die genauen Voraussetzungen und Mitteilungspflichten sind am Wortlaut zu prüfen `[unverifiziert – prüfen]`.

**[§ 36 KMAG](https://www.gesetze-im-internet.de/kmag/__36.html)** regelt die **Übermittlung von Insiderinformationen** an die BaFin nebst Verordnungsermächtigung.

### 4. Verbote (Art. 89, 90, 91 MiCAR)

| Norm | Verbot |
|---|---|
| **Art. 89** | **Insidergeschäfte** — Nutzung von Insiderinformationen beim Erwerb oder der Veräußerung von Kryptowerten, einschließlich Stornierung oder Änderung eines vor Kenntnis erteilten Auftrags; ebenso Empfehlung und Anstiftung |
| **Art. 90** | **unrechtmäßige Offenlegung** von Insiderinformationen außerhalb der normalen Ausübung von Beruf oder Aufgaben |
| **Art. 91** | **Marktmanipulation** |

Die Fallgruppen der **Marktmanipulation** nach Art. 91 umfassen insbesondere:

- Geschäfte oder Aufträge, die **falsche oder irreführende Signale** hinsichtlich Angebot, Nachfrage oder Kurs geben oder geben könnten;
- Geschäfte oder Aufträge, die den Kurs auf einem **anormalen oder künstlichen Niveau** sichern;
- Handlungen unter Vorspiegelung falscher Tatsachen oder sonstiger **Täuschungshandlungen**;
- **Verbreitung von Informationen**, die falsche oder irreführende Signale geben, einschließlich über Medien und soziale Netzwerke, wenn der Verbreitende daraus einen Vorteil zieht.

Im Kryptomarkt praktisch bedeutsam sind Wash Trading, Spoofing und Layering, koordinierte Pump-and-Dump-Kampagnen sowie Kursbeeinflussung durch Beiträge in sozialen Medien. Die Subsumtion erfolgt anhand der Fallgruppen des Art. 91, nicht anhand der Marktbezeichnung des Verhaltens.

### 5. Vorbeugung und Aufdeckung (Art. 92 MiCAR)

Personen, die berufsmäßig Geschäfte mit Kryptowerten vermitteln oder ausführen, sowie Betreiber von Handelsplattformen müssen über **wirksame Regelungen, Systeme und Verfahren** verfügen, um Marktmissbrauch **vorzubeugen und ihn aufzudecken**, und **verdächtige Aufträge und Geschäfte** unverzüglich der zuständigen Behörde zu **melden**.

Operativ heißt das: Handelsüberwachung mit definierten Szenarien, Eskalationswege, dokumentierte Prüfung jedes Alarms, Meldeformat und Fristenkontrolle, Schulung sowie ein **Insiderverzeichnis**, soweit vorgesehen. Der Aufbau ist zu dokumentieren — im Aufsichtsgespräch ist die **Systembeschreibung** der erste Prüfgegenstand.

### 6. Verfolgung durch die BaFin (§§ 31 bis 36 KMAG)

- **[§ 31 KMAG](https://www.gesetze-im-internet.de/kmag/__31.html)** — **Verfolgung von Marktmissbrauch**.
- **[§ 32 KMAG](https://www.gesetze-im-internet.de/kmag/__32.html)** — **Verschwiegenheitspflicht** bei Maßnahmen wegen eines Marktmissbrauchsverdachts; sie verbietet insbesondere die Information des Betroffenen und ist bei internen Untersuchungen zu beachten.
- **[§ 33 KMAG](https://www.gesetze-im-internet.de/kmag/__33.html)** — **Anzeige straftatbegründender Tatsachen**.
- **[§ 34 KMAG](https://www.gesetze-im-internet.de/kmag/__34.html)** — **Aussetzung des Handels** und Ausschluss von Kryptowerten.
- **[§ 35 KMAG](https://www.gesetze-im-internet.de/kmag/__35.html)** — Bekanntmachung marktrelevanter Informationen zum Handel.
- **[§ 36 KMAG](https://www.gesetze-im-internet.de/kmag/__36.html)** — Übermittlung von Insiderinformationen.

Hinzu treten die allgemeinen Befugnisse der **[§§ 4](https://www.gesetze-im-internet.de/kmag/__4.html), [20 KMAG](https://www.gesetze-im-internet.de/kmag/__20.html)** sowie die **sofortige Vollziehbarkeit** nach [§ 5 KMAG](https://www.gesetze-im-internet.de/kmag/__5.html).

### 7. Sanktionen (§§ 46, 47 KMAG; Art. 111 MiCAR)

- **[§ 46 KMAG](https://www.gesetze-im-internet.de/kmag/__46.html)** — **Strafvorschriften**; **[§ 47 KMAG](https://www.gesetze-im-internet.de/kmag/__47.html)** — **Bußgeldvorschriften**; **[§ 48 KMAG](https://www.gesetze-im-internet.de/kmag/__48.html)** — Ordnungsgelder. Tatbestände und Rahmen sind **am Wortlaut** zu bestimmen und nicht aus dem Wertpapierrecht zu übertragen `[unverifiziert – prüfen]`.
- **Art. 111 MiCAR** — verwaltungsrechtliche Sanktionen und andere Maßnahmen.
- Flankierend: **[§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html)** (Aufsichtspflichtverletzung) und **[§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html)** (Verbandsgeldbuße).

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Dokumentierte Aufschubdauer nach Art. 88 - Beginn und Ende festhalten
python -m scripts.legal_calc.cli frist --ereignis 04.05.2026 --menge 10 --einheit tage --land HE

# Verfolgungsverjährung einer Ordnungswidrigkeit nach § 47 KMAG iVm § 31 OWiG
python -m scripts.legal_calc.cli frist --ereignis 04.05.2026 --menge 3 --einheit jahre --land HE

# Rechtsbehelfsfrist gegen eine Maßnahme der BaFin (§ 5 KMAG: keine aufschiebende Wirkung)
python -m scripts.legal_calc.cli frist --ereignis 04.05.2026 --menge 1 --einheit monate --land HE
```

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/1114 (MiCAR), Art. 86, 87, 88, 89, 90, 91, 92, 111 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1114/oj)
- [KMAG](https://www.gesetze-im-internet.de/kmag/) – [§ 4](https://www.gesetze-im-internet.de/kmag/__4.html), [§ 5](https://www.gesetze-im-internet.de/kmag/__5.html), [§ 20](https://www.gesetze-im-internet.de/kmag/__20.html), [§ 31](https://www.gesetze-im-internet.de/kmag/__31.html), [§ 32](https://www.gesetze-im-internet.de/kmag/__32.html), [§ 33](https://www.gesetze-im-internet.de/kmag/__33.html), [§ 34](https://www.gesetze-im-internet.de/kmag/__34.html), [§ 35](https://www.gesetze-im-internet.de/kmag/__35.html), [§ 36](https://www.gesetze-im-internet.de/kmag/__36.html), [§ 46](https://www.gesetze-im-internet.de/kmag/__46.html), [§ 47](https://www.gesetze-im-internet.de/kmag/__47.html), [§ 48 KMAG](https://www.gesetze-im-internet.de/kmag/__48.html)
- Verordnung (EU) 596/2014 (MAR) zur Abgrenzung — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/596/oj); [WpHG](https://www.gesetze-im-internet.de/wphg/)
- [§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html), [§ 31 OWiG](https://www.gesetze-im-internet.de/owig_1968/__31.html), [§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html)

### Kommentare und Literatur

- Maume/Maute, MiCAR, Kommentar, Titel VI `[unverifiziert – prüfen]`
- Klöhn, MAR, Kommentar (als Auslegungshilfe, nicht als unmittelbare Quelle).
- BaFin, Hinweise zur Verdachtsmeldung und zur Handelsüberwachung.
- ESMA-Leitlinien zum Marktmissbrauch bei Kryptowerten `[unverifiziert – prüfen]`

### Rechtsprechung

Zu Titel VI der MiCAR und zu den §§ 31 ff. KMAG liegt **keine** Rechtsprechung vor. Zur Insiderinformation, zum Zwischenschritt bei gestreckten Sachverhalten und zur Marktmanipulation besteht **gefestigte** Rechtsprechung von EuGH und BGH zur MAR bzw. zum WpHG, die als **Auslegungshilfe** dienen kann — die Übertragung ist jeweils zu begründen. Jede konkrete Entscheidung ist vor Verwendung in curia.europa.eu, juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
KRYPTO-MARKTMISSBRAUCH — <Mandat> — <Datum>

I.   Geltungsbereich Art. 86
     Kryptowert:              <…>
     Zum Handel zugelassen / Antrag gestellt: [ja / nein]
     Abgrenzung:              [MiCAR Titel VI / MAR, weil Finanzinstrument]
     Rolle des Mandanten:     <Emittent / Anbieter / Plattformbetreiber / CASP / Führungsperson>

II.  Insiderinformation Art. 87
     Information:             <…>   Entstehungszeitpunkt: <…>
     präzise:                 [ja / nein — Zwischenschritt geprüft]
     nicht öffentlich bekannt:[ja / nein]
     Kursrelevanz:            [ja / nein — verständiger Anleger]
     Ergebnis:                [Insiderinformation / nicht]

III. Offenlegung Art. 88
     Offenlegungspflicht:     [ja / nein]
     Aufschub:                [beschlossen am <Datum> — Gründe, Vertraulichkeit, Verantwortliche
                               dokumentiert / nicht beschlossen]
     Mitteilung an die BaFin: [erfolgt / offen]   § 36 KMAG: <…>

IV.  Verbote
     Art. 89 Insidergeschäft: <Subsumtion, auch Stornierung/Änderung von Aufträgen>
     Art. 90 Offenlegung:     <…>
     Art. 91 Manipulation:    [falsche Signale / künstliches Kursniveau / Täuschung /
                               Informationsverbreitung]  <Fallgruppe benannt>

V.   Systeme Art. 92
     Überwachungsszenarien:   <…>
     Eskalation und Dokumentation: <…>
     Verdachtsmeldung:        [erstattet am <Datum> / zu erstatten]
     Insiderverzeichnis:      <…>

VI.  Aufsicht und Sanktionen
     §§ 31, 34 KMAG:          <Verfolgung, Handelsaussetzung>
     § 32 KMAG:               Verschwiegenheit — Betroffenen nicht informieren
     § 33 KMAG:               Anzeige straftatbegründender Tatsachen
     §§ 46, 47, 48 KMAG:      <Tatbestand und Rahmen am Wortlaut>
     §§ 130, 30 OWiG:         <Aufsichtspflicht, Verbandsgeldbuße>
     § 5 KMAG:                sofort vollziehbar

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **MAR-Praxis unbesehen übertragen.** Titel VI MiCAR ist eigenständig; Aufschubgründe, Verzeichnisse und Meldeformate sind am MiCAR- und KMAG-Wortlaut zu prüfen.
- **Regime verwechselt.** Ist der Kryptowert ein Finanzinstrument, gilt die MAR und nicht MiCAR.
- **Aufschub ohne Dokumentation.** Zeitpunkt, Gründe, Vertraulichkeitsmaßnahmen und Verantwortliche sind festzuhalten; ohne Dokumentation ist der Aufschub im Nachhinein nicht verteidigungsfähig.
- **Stornierung oder Änderung eines Auftrags nicht als Insidergeschäft erkannt** (Art. 89).
- **Marktmanipulation nach Marktjargon statt nach Fallgruppen subsumiert.** Wash Trading, Spoofing und Pump-and-Dump sind unter Art. 91 zu fassen, nicht umgekehrt.
- **Social-Media-Beiträge ausgeblendet.** Die Verbreitung irreführender Informationen ist eine eigene Fallgruppe des Art. 91.
- **Kein System nach Art. 92 aufgebaut** oder keines dokumentiert — die Systembeschreibung ist der erste Prüfgegenstand der Aufsicht.
- **Verschwiegenheitspflicht des § 32 KMAG verletzt**, indem der Betroffene über die Maßnahme informiert wird.
- **Sanktionsrahmen aus dem WpHG übernommen** statt aus §§ 46, 47 KMAG.
- **Rechtsprechung erfunden.** Zu Titel VI MiCAR gibt es keine; MAR-Judikatur ist nur Auslegungshilfe und stets zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
