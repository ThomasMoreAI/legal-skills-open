---
name: notwendige-verteidigung-borghei
title: /strafrecht:notwendige-verteidigung
description: Prüfung der notwendigen Verteidigung – Fälle des § 140 StPO, Zeitpunkt der Pflichtverteidigerbestellung § 141 StPO, Zuständigkeit und Auswahlrecht § 142 StPO, Dauer und Aufhebung der Bestellung § 143 StPO. Use when zu klären ist, ob ein Fall notwendiger Verteidigung vorliegt und ein Pflichtverteidiger zu bestellen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/notwendige-verteidigung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:notwendige-verteidigung

## Zweck

In bestimmten Konstellationen darf das Strafverfahren nicht ohne Verteidiger geführt werden — die **notwendige Verteidigung**. Liegt ein Fall des [§ 140 StPO](https://www.gesetze-im-internet.de/stpo/__140.html) vor, ist dem Beschuldigten ein Pflichtverteidiger zu bestellen, notfalls gegen seinen Willen. Dieser Skill prüft, **ob** ein Fall notwendiger Verteidigung vorliegt, **wann** die Bestellung zu erfolgen hat und **wer** ausgewählt wird. Fehler hier führen zu revisiblen Verfahrensfehlern.

## Eingaben

- Tatvorwurf und einschlägige Norm (Verbrechen / Vergehen)
- Verfahrensstand (Ermittlungsverfahren, Anklage, Hauptverhandlung)
- Zuständiges Gericht (AG, LG, OLG)
- Bestehende Untersuchungshaft / Unterbringung?
- Persönliche Umstände (Sprache, Behinderung, Verständnisfähigkeit)
- Hat der Beschuldigte bereits einen Wahlverteidiger?
- Wunschverteidiger benannt?

## Sub-Agent-Architektur

Der **Researcher** ordnet den Sachverhalt den Tatbeständen des § 140 Abs. 1 und Abs. 2 StPO zu und verifiziert jede zitierte Norm gegen gesetze-im-internet.de; er erfindet keine Aktenzeichen. Der **Drafter** formuliert den Beiordnungsantrag bzw. die Stellungnahme, benennt den konkreten Fall der notwendigen Verteidigung und den richtigen Zeitpunkt. Der **Reviewer** prüft gegenläufig, ob ein Fall übersehen wurde, ob das Auswahlrecht des Beschuldigten gewahrt ist und ob die Frist zur Benennung eingehalten wird; unbestätigte Rechtsprechung markiert er mit `[unverifiziert – prüfen]`.

## Ablauf

### 1. Liegt ein Fall notwendiger Verteidigung vor? ([§ 140 StPO](https://www.gesetze-im-internet.de/stpo/__140.html))

**Fälle notwendiger Verteidigung** nach Abs. 1 (abschließender Katalog), u. a.:

- Hauptverhandlung erstinstanzlich am LG oder OLG (Abs. 1 Nr. 1)
- Vorwurf eines **Verbrechens** (Abs. 1 Nr. 2)
- drohendes Berufsverbot (Abs. 1 Nr. 3)
- Vollstreckung von Untersuchungshaft / einstweiliger Unterbringung (Abs. 1 Nr. 4, 5)
- Unterbringungsverfahren (Abs. 1 Nr. 6)
- Sicherungsverfahren, Verbot des bisherigen Verteidigers (Abs. 1 Nr. 7–11)

Nach **Abs. 2** zudem, wenn wegen Schwere der Tat, Schwierigkeit der Sach- oder Rechtslage oder ersichtlicher Unfähigkeit zur Selbstverteidigung die Mitwirkung eines Verteidigers geboten ist (**Auffangtatbestand**).

### 2. Zeitpunkt der Bestellung ([§ 141 StPO](https://www.gesetze-im-internet.de/stpo/__141.html))

- Bestellung **unverzüglich**, sobald der Beschuldigte über den Tatvorwurf vernommen wird oder ein Fall des § 140 bekannt wird.
- Bei Untersuchungshaft: spätestens mit Vorführung vor den Haftrichter.
- Vor der ersten Vernehmung kann der Beschuldigte die Bestellung beantragen.

### 3. Zuständigkeit und Auswahlrecht ([§ 142 StPO](https://www.gesetze-im-internet.de/stpo/__142.html))

- Zuständig im Ermittlungsverfahren: das nach § 142 StPO bestimmte Gericht (auf Antrag der StA).
- **Auswahlrecht**: Dem Beschuldigten ist Gelegenheit zu geben, **binnen einer zu bestimmenden Frist** einen Verteidiger zu bezeichnen. Der bezeichnete Verteidiger ist grundsätzlich zu bestellen, sofern kein wichtiger Grund entgegensteht.
- Übergeht das Gericht das Auswahlrecht, ist die Beiordnung fehlerhaft.

### 4. Dauer und Aufhebung der Bestellung ([§ 143 StPO](https://www.gesetze-im-internet.de/stpo/__143.html))

- Die Bestellung dauert grundsätzlich bis zum rechtskräftigen Abschluss des Verfahrens.
- **Aufhebung** der Bestellung, wenn ein Wahlverteidiger die Verteidigung übernimmt oder die Voraussetzungen des § 140 StPO endgültig entfallen.
- Auswechslung des Pflichtverteidigers nach [§ 143a StPO](https://www.gesetze-im-internet.de/stpo/__143a.html) (zerrüttetes Vertrauensverhältnis, fehlende Verteidigung).

### 5. Antrag / Stellungnahme formulieren

- Konkreten Fall des § 140 StPO benennen.
- Bei Abs. 2: Schwere/Schwierigkeit substantiiert darlegen.
- Wunschverteidiger ausdrücklich benennen (Auswahlrecht).
- Bei verspäteter Bestellung: **rückwirkende Bestellung** prüfen (str.; mit `[unverifiziert – prüfen]` kennzeichnen, wo keine gefestigte Rechtsprechung zitiert wird).

## Risiken

- **Übersehener Fall** notwendiger Verteidigung → Verfahrensfehler, in der Hauptverhandlung absoluter Revisionsgrund.
- **Fristversäumnis** bei der Benennung des Wunschverteidigers → Gericht bestellt nach eigener Auswahl.
- **Auswahlrecht** des Beschuldigten übergangen → fehlerhafte Beiordnung, Beschwerde.
- **Verspätete Bestellung**: rückwirkende Beiordnung ist umstritten; Vergütungsrisiko für den Verteidiger.

## Ausgabeformat

```
NOTWENDIGE VERTEIDIGUNG — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Fall notwendiger Verteidigung   [§ 140 StPO]
      Einschlägige Nr.:               <Abs. 1 Nr. X / Abs. 2>
      Begründung:                     <…>
II.   Zeitpunkt                       [§ 141 StPO]
      Bestellung fällig seit:         <…>  [🟢 erfolgt / 🔴 überfällig]
III.  Zuständigkeit & Auswahl         [§ 142 StPO]
      Wunschverteidiger:              <…>
      Benennungsfrist:                <…>
IV.   Dauer / Aufhebung               [§ 143 StPO]
      Status:                         <bestehend / Aufhebung beantragt>

Empfehlung: <…>
Nächster Schritt: <Beiordnungsantrag / Beschwerde>
```

## Quellen

- [§ 140 StPO](https://www.gesetze-im-internet.de/stpo/__140.html), [§ 141 StPO](https://www.gesetze-im-internet.de/stpo/__141.html), [§ 142 StPO](https://www.gesetze-im-internet.de/stpo/__142.html), [§ 143 StPO](https://www.gesetze-im-internet.de/stpo/__143.html), [§ 143a StPO](https://www.gesetze-im-internet.de/stpo/__143a.html)
- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 140 Rn. 1 ff.
- Rechtsprechung zur rückwirkenden Bestellung: `[unverifiziert – prüfen]`
