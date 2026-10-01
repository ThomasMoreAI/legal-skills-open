---
name: domainrecht-borghei
title: /it-recht:domainrecht
description: Bewertung von Domainstreitigkeiten und Ansprüchen aus Namensrecht (§ 12 BGB), Kennzeichenrecht und geschäftlicher Bezeichnung (§§ 5, 15 MarkenG) sowie Markenrecht (§ 14 MarkenG), inklusive DENIC-Dispute-Eintrag und Domain-Grabbing. Use when ein Streit über eine Internet-Domain (Registrierung, Nutzung, Übertragung, Löschung) zu beurteilen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/domainrecht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /it-recht:domainrecht

## Zweck

Domainstreitigkeiten betreffen die Kollision einer registrierten Internet-Domain mit Namens-, Kennzeichen- oder Markenrechten Dritter. Dieser Skill ordnet den Sachverhalt den richtigen Anspruchsgrundlagen zu — **§ 12 BGB** (Namensrecht), **§ 5 MarkenG** und **§ 15 MarkenG** (geschäftliche Bezeichnung), **§ 14 MarkenG** (eingetragene Marke) — klärt die Priorität, bestimmt Unterlassungs-, Löschungs- und Übertragungsfolgen und bewertet den sichernden DENIC-Dispute-Eintrag.

## Eingaben

- Streitige Domain (Second-Level, TLD) und Registrierungsdatum
- Rolle des Mandanten (Domaininhaber / Anspruchsteller)
- Eigene Kennzeichenposition (eingetragene Marke, Unternehmenskennzeichen, bürgerlicher Name, Gebietskörperschaft)
- Prioritätszeitpunkte beider Seiten (Markenanmeldung / Namensführung / Domainregistrierung)
- Tatsächliche Nutzung der Domain (aktiver Inhalt, Branche, Verkaufsangebot)
- Gleichnamigkeit / berechtigtes eigenes Interesse des Inhabers?

## Sub-Agent-Architektur

Die Bearbeitung folgt drei Rollen. Ein **Rechtspositions-Agent** ermittelt, welche Kennzeichenrechte beim Anspruchsteller bestehen (Marke nach § 14 MarkenG, geschäftliche Bezeichnung nach §§ 5, 15 MarkenG, Namensrecht nach § 12 BGB) und prüft Branchen-/Warenähnlichkeit sowie Verwechslungsgefahr. Ein **Prioritäts-Agent** stellt die zeitliche Rangfolge fest, prüft Gleichnamigkeit und das Gerechtigkeitsprinzip der Priorität sowie etwaige Ausnahmen (überragende Bekanntheit, Recht der Gleichnamigen). Ein **Rechtsfolgen-Agent** bestimmt die durchsetzbaren Ansprüche — Unterlassung, Löschung/Verzicht (kein genereller Übertragungsanspruch nach BGH), DENIC-Dispute zur Sicherung — und bewertet Domain-Grabbing als Sonderfall. Die Rollen arbeiten sequenziell; ohne festgestellte Rechtsposition entsteht kein Anspruch. Aktenzeichen werden nur verifiziert zitiert, sonst mit `[unverifiziert – prüfen]` markiert (Zero-Fabrication).

## Ablauf

### 1. Kennzeichenposition feststellen

| Grundlage | Schutzgegenstand | Voraussetzung |
|---|---|---|
| **§ 12 BGB** | bürgerlicher Name, Firma, Vereins-/Gebietsname | Namensanmaßung / Zuordnungsverwirrung |
| **§ 5 MarkenG** | geschäftliche Bezeichnung (Unternehmenskennzeichen, Werktitel) | Benutzung im Geschäftsverkehr, Kennzeichnungskraft |
| **§ 15 MarkenG** | Schutz der geschäftlichen Bezeichnung | Verwechslungsgefahr / Bekanntheitsschutz |
| **§ 14 MarkenG** | eingetragene Marke | Identität/Ähnlichkeit + Waren-/Dienstleistungsähnlichkeit |

§ 12 BGB bleibt neben dem Kennzeichenschutz anwendbar, soweit Folgen begehrt werden, die das Markenrecht nicht trägt (z. B. Löschung der Registrierung als solche).

### 2. Verletzungsprüfung

- Verwechslungsgefahr: Zeichenähnlichkeit × Branchen-/Warennähe × Kennzeichnungskraft.
- Bei nur privater oder branchenfremder Nutzung: keine Verletzung der geschäftlichen Bezeichnung, aber u. U. Namensanmaßung nach § 12 BGB.

### 3. Priorität und Gleichnamigkeit

- Grundsatz: Prioritätsälteres Recht setzt sich durch.
- Recht der Gleichnamigen: Bei berechtigtem eigenem Interesse kann der Erstregistrierende die Domain behalten (Ausnahme bei überragender Bekanntheit der Gegenseite).

### 4. Rechtsfolgen

- **Unterlassung** der kennzeichenverletzenden Nutzung.
- **Löschung / Verzicht** auf die Domain — aber **kein** allgemeiner Anspruch auf Übertragung (BGH).
- **DENIC-Dispute-Eintrag**: sperrt die Übertragung an Dritte und sichert dem Antragsteller die Anwartschaft auf die Domain bei Freiwerden.
- Schadensersatz / Auskunft bei Verschulden.

### 5. Domain-Grabbing

Registrierung ohne eigenes Interesse, allein um den Kennzeicheninhaber zu behindern oder die Domain teuer zu veräußern: sittenwidrige Behinderung (§ 826 BGB, § 4 Nr. 4 UWG) neben Kennzeichenansprüchen.

## Risiken / typische Fehler

- **Domain-Grabbing** übersehen — missbräuchliche Registrierung erfordert eigene Anspruchsbegründung (§ 826 BGB / UWG) neben § 12 BGB.
- **DENIC-Dispute** versäumt — ohne Eintrag kann der Inhaber die Domain während des Streits an Dritte übertragen und den Anspruch leerlaufen lassen.
- **Übertragung statt Löschung** verlangt — die Rechtsprechung gewährt regelmäßig nur Verzicht/Löschung, keinen Übertragungsanspruch; falscher Antrag scheitert.
- **Verwechslungsgefahr** fehlerhaft bejaht — bei fehlender Branchennähe greift § 15 MarkenG nicht; nur § 12 BGB kann tragen.

## Ausgabeformat

```
DOMAINRECHT — <Domain> — <Datum>

I.    Kennzeichenposition
      Anspruchsteller:            [§ 14 MarkenG / §§ 5,15 MarkenG / § 12 BGB]
      Inhaber-Interesse:          [keins / gleichnamig / branchenfremd]
II.   Verletzung
      Verwechslungsgefahr:        [✓ / ✗]   Begründung: <…>
III.  Priorität
      Älteres Recht:              [Anspruchsteller / Inhaber]
      Gleichnamigkeit:            [relevant / nein]
IV.   Rechtsfolgen
      Unterlassung:               [✓ / ✗]
      Löschung/Verzicht:          [✓ / ✗]   (kein Übertragungsanspruch)
      DENIC-Dispute:              [empfohlen / gesetzt]
V.    Domain-Grabbing:            [ja (§ 826 BGB / UWG) / nein]

Handlungsempfehlung:              <…>
```

## Quellen

- [§ 12 BGB](https://www.gesetze-im-internet.de/bgb/__12.html) (Namensrecht)
- [§ 5 MarkenG](https://www.gesetze-im-internet.de/markeng/__5.html), [§ 15 MarkenG](https://www.gesetze-im-internet.de/markeng/__15.html) (geschäftliche Bezeichnung)
- [§ 14 MarkenG](https://www.gesetze-im-internet.de/markeng/__14.html) (eingetragene Marke)
- [§ 826 BGB](https://www.gesetze-im-internet.de/bgb/__826.html), [§ 4 UWG](https://www.gesetze-im-internet.de/uwg_2004/__4.html) (Behinderung)
- DENIC-Domainbedingungen / DENIC-Dispute-Verfahren
- BGH, Urt. v. 22.11.2001 – I ZR 138/99, BGHZ 149, 191 = GRUR 2002, 622 – „shell.de" (Namensrecht vs. Domain), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2001-11-22&Aktenzeichen=I%20ZR%20138/99)
- BGH, Urt. v. 17.05.2001 – I ZR 251/99, BGHZ 148, 13 = GRUR 2001, 1038 – „ambiente.de" (Prüfungspflichten der DENIC nur bei offenkundiger Rechtsverletzung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2001-05-17&Aktenzeichen=I%20ZR%20251/99)
- BGH „afilias.de" (Haftung DENIC, Übertragung) `[unverifiziert – prüfen]` — Az und Datum nicht ermittelbar; dejure indexiert keine Entscheidungsnamen, Fundstelle in juris/Beck-Online prüfen
