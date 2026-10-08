---
name: betreuerbestellung-borghei
title: /betreuungsrecht:betreuerbestellung
description: Prüfung der Voraussetzungen einer rechtlichen Betreuung nach der Reform 2023. Erforderlichkeit und Vorrang anderer Hilfen § 1814 BGB, Bestimmung der Aufgabenbereiche § 1815 BGB, Betreuerauswahl § 1816 BGB. Use when geprüft wird, ob eine Betreuung erforderlich ist, welche Aufgabenbereiche zu bestimmen sind und wer als Betreuer auszuwählen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/betreuungsrecht/skills/betreuerbestellung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /betreuungsrecht:betreuerbestellung

## Zweck

Die Betreuungsrechtsreform 2023 stellt den Erforderlichkeitsgrundsatz und die Selbstbestimmung der betroffenen Person in den Mittelpunkt. Eine Betreuung darf nur angeordnet werden, soweit sie wirklich erforderlich ist und keine vorrangigen Hilfen genügen. Dieser Skill prüft die Voraussetzungen der Bestellung, die Bestimmung der Aufgabenbereiche und die Auswahl des Betreuers.

## Eingaben

- Krankheit oder Behinderung der betroffenen Person (ärztliches Zeugnis/Gutachten)
- Konkrete Angelegenheiten, die nicht selbst besorgt werden können
- Bestehende Vorsorgevollmacht oder andere Hilfen (sozialrechtlich, familiär)
- Geäußerter Wille der betroffenen Person (auch entgegenstehender)
- Vorschläge zur Person des Betreuers, Eignung und Bindungen
- Dringlichkeit (ggf. einstweilige Anordnung)

## Sub-Agent-Architektur

Der **Researcher** bestätigt §§ 1814–1816 BGB in der seit 2023 geltenden Fassung über gesetze-im-internet.de und ordnet flankierende Normen (Verfahrensrecht FamFG) ein; ungesicherte Aktenzeichen werden als `[unverifiziert – prüfen]` markiert. Der **Drafter** prüft stufenweise Erforderlichkeit, Vorrang anderer Hilfen, Zuschnitt der Aufgabenbereiche und Betreuerauswahl. Der **Reviewer** kontrolliert, ob der Erforderlichkeitsgrundsatz konsequent durchgehalten wurde, ob der Wille der Person beachtet ist und ob keine Tatsachen oder Gutachten erfunden wurden.

## Ablauf

### 1. Grundvoraussetzungen (§ 1814 BGB)

[§ 1814 BGB](https://www.gesetze-im-internet.de/bgb/__1814.html): Das Betreuungsgericht bestellt einen Betreuer, wenn ein Volljähriger seine Angelegenheiten ganz oder teilweise rechtlich nicht besorgen kann und dies auf einer Krankheit oder Behinderung beruht.

- **Freier Wille (§ 1814 Abs. 2 BGB):** Gegen den freien Willen der Person darf kein Betreuer bestellt werden.
- **Erforderlichkeit (§ 1814 Abs. 3 BGB):** Die Betreuung ist nicht erforderlich, soweit die Angelegenheiten durch eine Bevollmächtigte oder durch andere Hilfen, bei denen kein gesetzlicher Vertreter bestellt wird, ebenso gut besorgt werden können.

### 2. Vorrang anderer Hilfen (Erforderlichkeitsgrundsatz)

Vor der Bestellung ist zu klären, ob mildere Mittel genügen:

- Wirksame **Vorsorgevollmacht** (siehe Skill vorsorgevollmacht-patientenverfuegung)
- Soziale Hilfen nach SGB (Pflege, Eingliederung, Teilhabe)
- Unterstützte Entscheidungsfindung, familiäre Hilfe
- Betreuung nur für die konkret nicht selbst besorgbaren Bereiche

### 3. Aufgabenbereiche (§ 1815 BGB)

[§ 1815 BGB](https://www.gesetze-im-internet.de/bgb/__1815.html): Das Gericht bestimmt die Aufgabenbereiche **einzeln und konkret**; eine pauschale „Allzuständigkeit" ist unzulässig. Besonders eingriffsintensive Befugnisse müssen ausdrücklich übertragen werden, u. a.:

- Entscheidung über eine freiheitsentziehende Unterbringung/Maßnahme
- Bestimmung des Aufenthalts/Wohnungsangelegenheiten
- Entscheidungen über Telekommunikation und Post
- Entgegennahme, Öffnen und Anhalten der Post

### 4. Betreuerauswahl (§ 1816 BGB)

[§ 1816 BGB](https://www.gesetze-im-internet.de/bgb/__1816.html): Auswahl nach Eignung und den **Wünschen der betroffenen Person**.

- Vorschlag der Person ist maßgeblich, sofern dem nicht das Wohl entgegensteht (§ 1816 Abs. 2 BGB)
- Vorrang ehrenamtlicher, der Person nahestehender Betreuer (§ 1816 Abs. 4, 5 BGB)
- Berücksichtigung von Bindungen, Interessenkonflikten und Belastung

### 5. Verfahren und Dauer

- Persönliche Anhörung und Sachverständigengutachten (FamFG)
- Befristung und Überprüfung von Amts wegen
- Einstweilige Anordnung nur bei Dringlichkeit

## Risiken / typische Fehler

- **Erforderlichkeit nicht geprüft** — eine Betreuung wird angeordnet, obwohl Vollmacht oder Sozialleistungen genügen; § 1814 Abs. 3 BGB verlangt den Vorrang anderer Hilfen.
- **Vorrang anderer Hilfen übergangen** — bestehende Vorsorgevollmacht macht die Betreuung insoweit entbehrlich.
- **Aufgabenbereiche zu weit gefasst** — pauschale Zuständigkeit verstößt gegen § 1815 BGB; eingriffsintensive Befugnisse müssen einzeln übertragen werden.
- **Freier Wille missachtet** — gegen den freien Willen der Person ist keine Bestellung zulässig (§ 1814 Abs. 2 BGB).
- **Betreuerauswahl ohne Wunschberücksichtigung** — der Vorschlag der Person nach § 1816 BGB wurde nicht beachtet; Interessenkonflikte ungeprüft; ungesicherte Aktenzeichen als `[unverifiziert – prüfen]` kennzeichnen.

## Quellen (Reform 2023)

- [§ 1814 BGB](https://www.gesetze-im-internet.de/bgb/__1814.html) (Voraussetzungen)
- [§ 1815 BGB](https://www.gesetze-im-internet.de/bgb/__1815.html) (Aufgabenbereiche)
- [§ 1816 BGB](https://www.gesetze-im-internet.de/bgb/__1816.html) (Betreuerauswahl)
- [§ 1821 BGB](https://www.gesetze-im-internet.de/bgb/__1821.html) (Pflichten, Wünsche der Person)
- [FamFG §§ 271 ff.](https://www.gesetze-im-internet.de/famfg/__271.html) (Betreuungsverfahren)
- BMJ-Informationen zur Betreuungsrechtsreform 2023

## Ausgabeformat

```
BETREUERBESTELLUNG — <betroffene Person> — <Datum>

I.    Voraussetzungen § 1814 BGB
      Krankheit/Behinderung:             <…>
      Freier Wille (Abs. 2):             [entgegenstehend? ja/nein]
      Erforderlichkeit (Abs. 3):         [erforderlich / entbehrlich]
II.   Vorrang anderer Hilfen
      Vorsorgevollmacht / Sozialhilfen:  [vorhanden → Umfang]
III.  Aufgabenbereiche § 1815 BGB
      Konkrete Bereiche:                 <Liste>
      Eingriffsintensive Befugnisse:     [ausdrücklich übertragen?]
IV.   Betreuerauswahl § 1816 BGB
      Wunsch der Person:                 <…>
      Eignung / Interessenkonflikt:      <…>

Empfehlung: <…>
```
