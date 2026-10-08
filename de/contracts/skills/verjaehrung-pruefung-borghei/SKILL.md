---
name: verjaehrung-pruefung-borghei
title: /vertragsrecht:verjaehrung-pruefung
description: Vollständige Verjährungsprüfung im Zivilrecht – Regelverjährung § 195 BGB, kenntnisabhängiger Beginn und Höchstfristen § 199 BGB, Hemmung durch Verhandlungen § 203 BGB und durch Rechtsverfolgung § 204 BGB, Neubeginn durch Anerkenntnis § 212 BGB, Wirkung der Verjährungseinrede § 214 BGB sowie Hemmungsvereinbarung und Einredeverzicht nach § 202 BGB. Use when zu klären ist, ob ein Anspruch verjährt ist, bis wann verjährungshemmend gehandelt werden muss oder ob eine Verjährungsverzichtserklärung eingeholt werden sollte.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/verjaehrung-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:verjaehrung-pruefung

## Zweck

Die Verjährung ist der häufigste Grund, aus dem ein materiell bestehender Anspruch nicht mehr durchsetzbar ist — und der häufigste Haftungsfall in der anwaltlichen Berufspraxis. Dieser Skill bestimmt die einschlägige Frist, ihren Beginn nach der **Ultimo-Regel** des [§ 199 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__199.html), rechnet das Fristende **deterministisch** und benennt die Handlungsoptionen: Hemmung, Neubeginn, Hemmungsvereinbarung, Verjährungsverzicht.

## Eingaben

- Anspruch: Rechtsgrund, Gläubiger, Schuldner, Betrag
- **Entstehung** des Anspruchs (Fälligkeit — § 199 Abs. 1 Nr. 1 BGB)
- **Kenntnis** oder grob fahrlässige Unkenntnis des Gläubigers von den anspruchsbegründenden Umständen und der Person des Schuldners (§ 199 Abs. 1 Nr. 2 BGB) — mit Datum und Beleg
- Anspruchsart (für Sonderfristen: Kauf § 438 BGB, Werkvertrag § 634a BGB, Herausgabeanspruch § 197 BGB, Miete § 548 BGB, Schadensersatz wegen Verletzung von Leben, Körper, Gesundheit, Freiheit § 199 Abs. 2 BGB)
- Hemmungs- und Neubeginntatbestände: Verhandlungen (Beginn/Abbruch), Klageerhebung, Mahnbescheid, Anerkenntnis, Ratenzahlung, Sicherheitsleistung — jeweils mit Datum
- Vertragliche Verjährungsregelungen (Verkürzung, Verlängerung, AGB)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) ordnet dem Anspruch die zutreffende Frist zu, liefert die Statute mit URL und Kommentarstellen zu Kenntnisbegriff und Hemmungstatbeständen.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) rechnet mit dem deterministischen Rechner, stellt die Zeitachse auf und entwirft Hemmungsvereinbarung, Verjährungsverzicht oder Verjährungseinrede.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft jede Datumsangabe gegen die Eingaben, verifiziert das Rechenergebnis und markiert jeden nicht belegten Kenntniszeitpunkt als offene Tatsache.

## Ablauf

### 1. Anspruch und einschlägige Frist bestimmen ([§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html))

Die **regelmäßige Verjährungsfrist** beträgt **drei Jahre**. Vorrangig sind die Sonderfristen:

| Anspruch | Frist | Norm |
|---|---|---|
| Regelfall (vertraglich, deliktisch, bereicherungsrechtlich) | 3 Jahre | § 195 BGB |
| Kaufrechtliche Mängelansprüche | 2 Jahre ab Ablieferung (5 Jahre Bauwerk) | § 438 BGB |
| Werkvertragliche Mängelansprüche | 2 Jahre ab Abnahme (5 Jahre Bauwerk) | § 634a BGB |
| Herausgabeansprüche aus Eigentum, familien- und erbrechtliche Ansprüche, rechtskräftig festgestellte Ansprüche, Titel | 30 Jahre | [§ 197 BGB](https://www.gesetze-im-internet.de/bgb/__197.html) |
| Ansprüche auf Übertragung des Eigentums an einem Grundstück | 10 Jahre | [§ 196 BGB](https://www.gesetze-im-internet.de/bgb/__196.html) |
| Ersatzansprüche des Vermieters wegen Veränderungen der Mietsache | 6 Monate | § 548 BGB |

### 2. Verjährungsbeginn — kenntnisabhängig ([§ 199 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__199.html))

Die regelmäßige Verjährungsfrist beginnt mit dem **Schluss des Jahres**, in dem

1. der Anspruch **entstanden** ist (= erstmals fällig und klagbar) **und**
2. der Gläubiger von den anspruchsbegründenden Umständen und der Person des Schuldners **Kenntnis erlangt** hat oder ohne **grobe Fahrlässigkeit** hätte erlangen müssen.

**Berechnungsschema:**

```
Schritt 1: Entstehungsjahr E bestimmen (Fälligkeit).
Schritt 2: Kenntnisjahr K bestimmen (Kenntnis oder grob fahrlässige Unkenntnis).
Schritt 3: Maßgeblich ist das SPÄTERE der beiden Ereignisse.
Schritt 4: Ultimo-Regel — Fristbeginn ist der 31.12. dieses Jahres, 24:00 Uhr.
Schritt 5: + 3 Jahre  ->  Verjährungseintritt mit Ablauf des 31.12. des dritten Folgejahres.
Schritt 6: § 193 BGB wird NICHT angewendet — die Verjährung läuft auch an
           Samstagen, Sonntagen und Feiertagen ab.
```

**Kenntnis** bedeutet Kenntnis der Tatsachen, nicht der zutreffenden rechtlichen Würdigung. **Grobe Fahrlässigkeit** liegt vor, wenn sich die Kenntnis förmlich aufdrängte und der Gläubiger auf der Hand liegende Erkenntnisquellen nicht genutzt hat.

### 3. Kenntnisunabhängige Höchstfristen ([§ 199 Abs. 2–4 BGB](https://www.gesetze-im-internet.de/bgb/__199.html))

Unabhängig von Kenntnis oder grob fahrlässiger Unkenntnis verjähren:

- **Schadensersatzansprüche wegen Verletzung des Lebens, des Körpers, der Gesundheit oder der Freiheit** in **30 Jahren** ab der Begehung der Handlung, der Pflichtverletzung oder dem schädigenden Ereignis (§ 199 Abs. 2 BGB).
- **Sonstige Schadensersatzansprüche** in **10 Jahren** ab Entstehung, ohne Rücksicht darauf in **30 Jahren** ab dem schädigenden Ereignis — maßgeblich ist die **früher endende** Frist (§ 199 Abs. 3 BGB).
- **Andere Ansprüche** in **10 Jahren** ab Entstehung (§ 199 Abs. 4 BGB).

### 4. Hemmung durch Verhandlungen ([§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html))

Schweben zwischen Schuldner und Gläubiger **Verhandlungen** über den Anspruch oder die den Anspruch begründenden Umstände, ist die Verjährung gehemmt, bis der eine oder der andere Teil die Fortsetzung der Verhandlungen **verweigert**. Die Verjährung tritt frühestens **drei Monate nach dem Ende der Hemmung** ein (§ 203 S. 2 BGB — „Nachlauffrist").

- Der Begriff „Verhandlungen" ist weit: Jeder Meinungsaustausch über den Anspruch genügt, sofern der Schuldner nicht sofort und eindeutig ablehnt.
- Das **Ende** der Verhandlungen ist der neuralgische Punkt: „Einschlafenlassen" beendet die Hemmung zu dem Zeitpunkt, zu dem der nächste Schritt nach Treu und Glauben zu erwarten gewesen wäre. **Immer schriftlich dokumentieren, wann verhandelt wurde und wann abgebrochen wurde.**

### 5. Hemmung durch Rechtsverfolgung ([§ 204 BGB](https://www.gesetze-im-internet.de/bgb/__204.html))

Gehemmt wird die Verjährung u.a. durch

- Erhebung der **Klage** auf Leistung oder Feststellung (§ 204 Abs. 1 Nr. 1 BGB) — mit **Rückwirkung der Zustellung** auf den Eingang bei Gericht, wenn demnächst zugestellt wird ([§ 167 ZPO](https://www.gesetze-im-internet.de/zpo/__167.html));
- Zustellung des **Mahnbescheids** im Mahnverfahren (§ 204 Abs. 1 Nr. 3 BGB) — das schnellste Mittel kurz vor Fristablauf;
- Veranlassung der Bekanntgabe eines **Güteantrags** bei einer anerkannten Gütestelle (Nr. 4);
- Anmeldung im **Insolvenzverfahren** (Nr. 10); Beginn eines **schiedsrichterlichen Verfahrens** (Nr. 11);
- Zustellung der **Streitverkündung** (Nr. 6) und Antrag auf **selbständiges Beweisverfahren** (Nr. 7).

Die Hemmung endet **sechs Monate** nach rechtskräftiger Entscheidung oder anderweitiger Beendigung des Verfahrens (§ 204 Abs. 2 BGB). **Gerät ein Verfahren in Stillstand**, endet die Hemmung sechs Monate nach der letzten Verfahrenshandlung.

### 6. Neubeginn ([§ 212 BGB](https://www.gesetze-im-internet.de/bgb/__212.html))

Die Verjährung beginnt **erneut**, wenn

1. der Schuldner dem Gläubiger gegenüber den Anspruch durch **Abschlagszahlung, Zinszahlung, Sicherheitsleistung oder in anderer Weise anerkennt**, oder
2. eine gerichtliche oder behördliche **Vollstreckungshandlung** vorgenommen oder beantragt wird.

Anders als die Hemmung setzt der Neubeginn die volle Frist erneut in Lauf — hier ab dem Tag des Anerkenntnisses, **nicht** nach der Ultimo-Regel. Das **Anerkenntnis** im Sinne des § 212 BGB ist ein rein tatsächliches Verhalten, aus dem sich das Bewusstsein vom Bestehen der Schuld ergibt; eine rechtsgeschäftliche Erklärung ist nicht erforderlich. **Für den Schuldner ist das die größte Falle:** Eine Teilzahlung „ohne Anerkennung einer Rechtspflicht" schützt nur, wenn der Vorbehalt eindeutig und rechtzeitig erklärt ist.

### 7. Verjährungseinrede und Wirkung ([§ 214 BGB](https://www.gesetze-im-internet.de/bgb/__214.html))

Nach Eintritt der Verjährung ist der Schuldner **berechtigt, die Leistung zu verweigern**. Die Verjährung wirkt nicht von Amts wegen — sie ist eine **Einrede**, die im Prozess ausdrücklich erhoben werden muss. Das Zurückgeforderte kann nicht zurückverlangt werden, auch wenn in Unkenntnis der Verjährung geleistet wurde (§ 214 Abs. 2 BGB).

**Formulierungshilfe Verjährungseinrede:** „Namens und in Vollmacht der Beklagten erhebe ich hinsichtlich der Klageforderung die **Einrede der Verjährung**. Der Anspruch ist spätestens mit Ablauf des [Datum] nach §§ 195, 199 Abs. 1 BGB verjährt. Verjährungshemmende oder den Neubeginn auslösende Umstände nach §§ 203, 204, 212 BGB liegen nicht vor; insbesondere haben Verhandlungen im Sinne des § 203 BGB nicht stattgefunden."

### 8. Vereinbarungen über die Verjährung ([§ 202 BGB](https://www.gesetze-im-internet.de/bgb/__202.html))

Die Verjährung kann durch Rechtsgeschäft **erleichtert oder erschwert** werden, mit zwei Grenzen: keine Erleichterung bei **Haftung wegen Vorsatzes** im Voraus (§ 202 Abs. 1 BGB), keine Erschwerung über eine Verjährungsfrist von **30 Jahren ab dem gesetzlichen Verjährungsbeginn** hinaus (§ 202 Abs. 2 BGB). In AGB gelten zusätzlich §§ 307, 309 Nr. 8 BGB.

**Zwei Instrumente kurz vor Fristablauf:**

- **Hemmungsvereinbarung (Stillhalteabkommen):** „Die Parteien vereinbaren, dass die Verjährung sämtlicher wechselseitiger Ansprüche aus dem Vertrag vom [Datum] ab dem [Datum] bis zum [Datum] **gehemmt** ist. Die Hemmung wirkt wie eine Hemmung nach § 203 BGB; die Regelung des § 203 S. 2 BGB (Nachlauffrist von drei Monaten) bleibt unberührt." — Vorteil: keine Klage nötig, Verhandlungsklima bleibt erhalten.
- **Einredeverzicht:** „Die Schuldnerin verzichtet gegenüber der Gläubigerin hinsichtlich der Ansprüche aus [Bezeichnung] **befristet bis zum [Datum] auf die Erhebung der Einrede der Verjährung**, soweit diese im Zeitpunkt dieser Erklärung noch nicht eingetreten ist." — **Der Zusatz „soweit noch nicht eingetreten" ist entscheidend**; ein Verzicht auf bereits eingetretene Verjährung wird sonst als Verzicht auf eine bestehende Rechtsposition ausgelegt. Der Verzicht ist **befristet** zu erklären; ein unbefristeter Verzicht ist regelmäßig unerwünscht und im Zweifel auslegungsbedürftig.

Wenn beides nicht zu erreichen ist: **Mahnbescheid** nach § 204 Abs. 1 Nr. 3 BGB als schnellstes Hemmungsmittel.

## Deterministische Berechnung

Die rechtliche Wertung — **welche** Frist gilt, wann der Anspruch entstanden ist, wann Kenntnis vorlag — bleibt vorgelagerte Eingabe und muss belegt sein. Die Arithmetik übernimmt der deterministische Rechner (siehe [`../../references/rechner.md`](../../references/rechner.md)), ohne Modellaufruf:

```bash
python -m scripts.legal_calc.cli verjaehrung --entstehung 10.03.2023 --kenntnis 05.07.2023
```

Ausgabe:

```
Verjährungsberechnung (Regelverjährung 3 Jahre (Ultimo))
  Verjährung tritt ein mit Ablauf des 31.12.2026.
  Letzter Tag für verjährungshemmende Handlung: 31.12.2026.
  Schritte:
    - § 199 Abs. 1 BGB: maßgeblich ist das spätere Ereignis aus Entstehung
      (10.03.2023) und Kenntnis (05.07.2023) = 05.07.2023.
    - Ultimo-Regel: Frist beginnt mit Schluss des Jahres 2023 (31.12.2023).
    - § 195 BGB: 3 Jahre -> Verjährung mit Ablauf des 31.12.2026.
```

Für die kenntnisunabhängigen Höchstfristen des § 199 Abs. 2–4 BGB wird zusätzlich `--begehung` gesetzt; der Rechner gibt dann die **früher endende** Frist aus:

```bash
python -m scripts.legal_calc.cli verjaehrung --entstehung 10.05.2020 --kenntnis 01.01.2028 --begehung 10.05.2020
```

Für abgeleitete Fristen (Nachlauffrist § 203 S. 2 BGB, Sechs-Monats-Frist § 204 Abs. 2 BGB) den Fristenrechner verwenden:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY
```

**Grenzen:** Hemmung und Neubeginn nach §§ 203, 204, 212 BGB sind fallabhängig und **nicht** eingebaut — ein durch Anerkenntnis neu begonnener Lauf ist als angepasster `--entstehung`-Wert einzugeben. § 193 BGB wird auf den Verjährungsablauf nach h.M. **nicht** angewendet; der Rechner verschiebt daher nicht auf den nächsten Werktag. Jedes Ergebnis ist mit `--json` maschinenlesbar und enthält die Rechenschritte mit Normzitat.

## Quellen

### Statute

- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 196 BGB](https://www.gesetze-im-internet.de/bgb/__196.html), [§ 197 BGB](https://www.gesetze-im-internet.de/bgb/__197.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)
- [§ 202 BGB](https://www.gesetze-im-internet.de/bgb/__202.html), [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html), [§ 204 BGB](https://www.gesetze-im-internet.de/bgb/__204.html), [§ 212 BGB](https://www.gesetze-im-internet.de/bgb/__212.html), [§ 214 BGB](https://www.gesetze-im-internet.de/bgb/__214.html)
- [§ 438 BGB](https://www.gesetze-im-internet.de/bgb/__438.html), [§ 634a BGB](https://www.gesetze-im-internet.de/bgb/__634a.html)
- [§§ 187–193 BGB](https://www.gesetze-im-internet.de/bgb/__187.html) (Fristberechnung), [§ 167 ZPO](https://www.gesetze-im-internet.de/zpo/__167.html) (Rückwirkung der Zustellung)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 195, 199, 203, 204 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Grothe, in: MüKoBGB, 9. Aufl. 2021, § 199 Rn. 1 ff., § 203 Rn. 1 ff.
- Peters/Jacoby, in: Staudinger, BGB, Neubearb. 2019, § 199 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 26.10.2006 – VII ZR 194/05 (Verhandlungsbegriff § 203 BGB, „Einschlafenlassen") `[unverifiziert – prüfen]`
- BGH, Urt. v. 10.11.2009 – VI ZR 247/08 (grob fahrlässige Unkenntnis § 199 Abs. 1 Nr. 2 BGB) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen dieses Skills folgen unmittelbar aus dem Gesetzeswortlaut und dem Rechenergebnis des deterministischen Rechners.

## Ausgabeformat

```
VERJÄHRUNGSPRÜFUNG — <Anspruch> — <Datum>

I.    Anspruch / Rechtsgrund          <…>
II.   Einschlägige Frist              [§ 195 (3 J.) / § 438 / § 634a / § 197 (30 J.) / § 196]
III.  Entstehung (§ 199 I Nr. 1)      <TT.MM.JJJJ> — Beleg: <…>
IV.   Kenntnis (§ 199 I Nr. 2)        <TT.MM.JJJJ> — Beleg: <…>  [belegt / offene Tatsache]
V.    Fristbeginn (Ultimo-Regel)      31.12.<JJJJ>
VI.   Verjährungseintritt             <TT.MM.JJJJ>
        Rechner-Beleg:                <Ausgabe legal_calc verjaehrung>
VII.  Höchstfristen (§ 199 II–IV)     [10 J. / 30 J. — Ende <TT.MM.JJJJ> / nicht einschlägig]
VIII. Hemmung                         [§ 203 Verhandlungen <von>–<bis> + 3 Monate Nachlauf
                                       / § 204 Rechtsverfolgung — Ende + 6 Monate]
IX.   Neubeginn (§ 212)               [Anerkenntnis am <Datum> — neuer Lauf ab <Datum> / keiner]
X.    Ergebnis                        [🟢 nicht verjährt / 🟡 Frist läuft ab am <Datum> / 🔴 verjährt]
XI.   Handlungsempfehlung             [Mahnbescheid § 204 I Nr. 3 / Klage / Hemmungsvereinbarung
                                       / befristeter Einredeverzicht] — bis spätestens <TT.MM.JJJJ>

Wiedervorlage: <TT.MM.JJJJ>
Offene Tatsachen: <Liste — insbesondere Kenntniszeitpunkt>
```

## Risiken / typische Fehler

- **Ultimo-Regel übersehen** — die Frist beginnt nicht am Tag der Kenntnis, sondern mit Schluss des Kalenderjahres (§ 199 Abs. 1 BGB); wer taggenau ab Kenntnis rechnet, verkürzt sich die Frist um bis zu ein Jahr.
- **§ 193 BGB auf den Verjährungsablauf angewendet** — die Verjährung tritt nach h.M. auch an einem Samstag, Sonntag oder Feiertag ein; verjährungshemmende Handlungen müssen entsprechend früher erfolgen.
- **Ende der Verhandlungen nicht dokumentiert** — beim „Einschlafenlassen" nach § 203 BGB ist der Hemmungszeitraum später kaum beweisbar; die Dreimonats-Nachlauffrist läuft dann von einem streitigen Datum an.
- **Anerkenntnis nach § 212 BGB unbewusst abgegeben** — eine Abschlagszahlung oder Sicherheitsleistung setzt die volle Frist neu in Lauf; für den Schuldner ist stets ein eindeutiger Vorbehalt zu erklären.
- **Verzicht auf bereits eingetretene Verjährung erklärt** — der Einredeverzicht ist stets befristet und mit dem Zusatz zu versehen, dass die Verjährung im Zeitpunkt der Erklärung noch nicht eingetreten war.
- **Sonderfristen übersehen** — §§ 438, 634a BGB knüpfen an Ablieferung bzw. Abnahme an und laufen kenntnisunabhängig; die Ultimo-Regel des § 199 BGB gilt dort gerade nicht.
- **Kenntniszeitpunkt frei geschätzt** — er ist eine beweisbedürftige Tatsache und als Eingabe des Rechners zu belegen, nicht zu unterstellen.
