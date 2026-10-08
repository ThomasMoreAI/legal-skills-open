---
name: schiedsverfahren-fuehrung-borghei
title: /schiedsverfahren-adr:schiedsverfahren-fuehrung
description: Führung eines Schiedsverfahrens nach dem Zehnten Buch der ZPO – Zusammensetzung § 1034 (drei Schiedsrichter als Auffangregel, gerichtliche Ersatzbestellung bei Übergewicht binnen zwei Wochen), Bestellung § 1035, Offenlegungspflicht und Ablehnung §§ 1036, 1037 mit Zweiwochen- und Monatsfrist, Verfahrensgrundsätze § 1042 (Gleichbehandlung, rechtliches Gehör, Anwaltszulassung), Schiedsort § 1043, Klage und Klagebeantwortung § 1046, Säumnis § 1048, Sachverständige § 1049, gerichtliche Unterstützung bei der Beweisaufnahme § 1050, einstweiliger Rechtsschutz §§ 1033, 1041, Rechtswahl § 1051, Vergleich § 1053, Form und Inhalt des Schiedsspruchs § 1054, Wirkung § 1055, Beendigung § 1056, Kosten § 1057, Berichtigung § 1058 sowie das Zusammenspiel mit der DIS-Schiedsgerichtsordnung 2018. Use when ein Schiedsverfahren einzuleiten, zu verteidigen oder verfahrensrechtlich zu steuern ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/schiedsverfahren-adr/skills/schiedsverfahren-fuehrung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: arbitration
language: de
---

# /schiedsverfahren-adr:schiedsverfahren-fuehrung

## Zweck

Der Skill steuert das Schiedsverfahren von der Konstituierung des Schiedsgerichts bis zum Kostenschiedsspruch. Sein Schwerpunkt liegt auf den Punkten, die später zum Aufhebungsgrund werden: Bildung des Schiedsgerichts, rechtliches Gehör, Beweisaufnahme und die formalen Anforderungen an den Schiedsspruch. Er entwirft Schiedsklage, Klagebeantwortung, Ablehnungsgesuch und Verfahrensanträge.

## Eingaben

- Schiedsvereinbarung und in Bezug genommene Verfahrensordnung
- Schiedsort und Verfahrenssprache; auf die Hauptsache anwendbares Recht
- Verfahrensstand: Schiedsklage zugestellt, Schiedsgericht gebildet, Verfahrenskonferenz, Beweisaufnahme
- Personen der Schiedsrichter und deren Offenlegungserklärungen
- Streitwert und Kostenvorschusslage
- Eilbedürfnis: Sicherungsbedarf, drohende Vermögensverschiebung
- Bei Beweisaufnahme: benötigte Zeugen, Urkunden Dritter, Zwangsmittelbedarf

## Sub-Agent-Architektur

Der Researcher beschafft die Normen des Zehnten Buchs, die konkrete Verfahrensordnung und die Rechtsprechung zu Gehörsverstößen und Ablehnungsgründen. Der Drafter entwirft Schriftsätze und Verfahrensanträge. Der Reviewer kontrolliert die Fristenkette der §§ 1034, 1037, 1040, prüft jeden Verfahrensschritt darauf, ob er einen Aufhebungsgrund nach § 1059 Abs. 2 erzeugt, und stellt sicher, dass Rügen rechtzeitig protokolliert werden.

> **Hinweis zum Rechtsstand.** Das Zehnte Buch der ZPO ist Gegenstand des Gesetzes vom 20.05.2026 (BGBl. 2026 I Nr. 152); die Änderungen sind auf gesetze-im-internet.de textlich nachgewiesen, dokumentarisch aber noch nicht abschließend eingearbeitet. Der konsolidierte Stand ist gegen das Bundesgesetzblatt abzugleichen `[unverifiziert – prüfen]`.

## Ablauf

### 1. Schiedsgericht konstituieren ([§ 1034 ZPO](https://www.gesetze-im-internet.de/zpo/__1034.html), [§ 1035 ZPO](https://www.gesetze-im-internet.de/zpo/__1035.html))

- **Anzahl**: Parteivereinbarung; fehlt sie, sind es **drei** Schiedsrichter (§ 1034 Abs. 1 S. 2).
- **Übergewicht**: Gibt die Schiedsvereinbarung einer Partei bei der Zusammensetzung ein die andere benachteiligendes Übergewicht, kann diese binnen **zwei Wochen** ab Kenntnis der Zusammensetzung die abweichende gerichtliche Bestellung beantragen (§ 1034 Abs. 2).
- **Bestellung** (§ 1035): Parteivereinbarung geht vor. Fehlt sie, bestellt bei drei Schiedsrichtern **jede Partei einen**, diese beiden den **Vorsitzenden**; bei Untätigkeit einer Partei über einen Monat nach Aufforderung bestellt auf Antrag das Gericht. Bei einem Einzelschiedsrichter bestellt das Gericht, wenn keine Einigung zustande kommt. Die Bestellung durch eine Partei ist bindend, sobald die Mitteilung der anderen Partei zugeht (§ 1035 Abs. 2).
- Zuständig für gerichtliche Bestellungen ist das **OLG** ([§ 1062 Abs. 1 Nr. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__1062.html)).

### 2. Unabhängigkeit sichern ([§ 1036 ZPO](https://www.gesetze-im-internet.de/zpo/__1036.html), [§ 1037 ZPO](https://www.gesetze-im-internet.de/zpo/__1037.html))

- **Offenlegungspflicht (§ 1036 Abs. 1)**: Wer ein Schiedsrichteramt angetragen bekommt, hat **alle** Umstände offenzulegen, die Zweifel an Unparteilichkeit oder Unabhängigkeit wecken können — und zwar fortlaufend bis zum Verfahrensende.
- **Ablehnungsgründe (§ 1036 Abs. 2)**: berechtigte Zweifel an Unparteilichkeit oder Unabhängigkeit oder Nichterfüllung vereinbarter Voraussetzungen. Den selbst bestellten Schiedsrichter kann eine Partei nur aus **nachträglich bekannt gewordenen** Gründen ablehnen.
- **Verfahren (§ 1037)**: Ohne abweichende Vereinbarung sind die Gründe binnen **zwei Wochen** ab Kenntnis schriftlich dem Schiedsgericht darzulegen; tritt der Schiedsrichter nicht zurück und stimmt die Gegenseite nicht zu, entscheidet das Schiedsgericht. Bleibt die Ablehnung erfolglos, kann binnen **eines Monats** ab Kenntnis der Entscheidung die gerichtliche Entscheidung beantragt werden (§ 1037 Abs. 3); das Verfahren darf fortgesetzt werden.

Als Auslegungshilfe für Offenlegung und Ablehnung dienen in der internationalen Praxis die IBA Guidelines on Conflicts of Interest; sie sind **kein** geltendes Recht und nur als Orientierung zu zitieren `[unverifiziert – prüfen]` hinsichtlich der jeweils aktuellen Fassung.

### 3. Verfahrensgrundsätze einhalten ([§ 1042 ZPO](https://www.gesetze-im-internet.de/zpo/__1042.html))

Zwingend sind:

- **Gleichbehandlung** der Parteien (Abs. 1 S. 1);
- **rechtliches Gehör** (Abs. 1 S. 2);
- **keine Ausschließung von Rechtsanwälten** als Bevollmächtigte (Abs. 2).

Im Übrigen können die Parteien das Verfahren selbst oder durch Bezugnahme auf eine Verfahrensordnung regeln (Abs. 3); fehlt beides, bestimmt das Schiedsgericht die Regeln nach freiem Ermessen und entscheidet über Zulässigkeit, Durchführung und Würdigung der Beweisaufnahme (Abs. 4).

**Jeder Verstoß gegen Abs. 1 ist ein potenzieller Aufhebungsgrund nach § 1059 Abs. 2 Nr. 1 Buchst. b oder Nr. 2 Buchst. b.** Gehörsverstöße sind deshalb **sofort und protokolliert** zu rügen; wer schweigt, verliert den Einwand regelmäßig.

### 4. Verfahrensablauf strukturieren

| Schritt | Norm | Praxispunkt |
|---|---|---|
| Schiedsort bestimmen | [§ 1043](https://www.gesetze-im-internet.de/zpo/__1043.html) | Parteivereinbarung, sonst Bestimmung durch das Schiedsgericht; Verhandlungen können anderswo stattfinden |
| Beginn des Verfahrens | [§ 1044](https://www.gesetze-im-internet.de/zpo/__1044.html) | Empfang des Antrags durch den Beklagten — maßgeblich für Verjährungshemmung nach § 204 Abs. 1 Nr. 11 BGB |
| Klage und Klagebeantwortung | [§ 1046](https://www.gesetze-im-internet.de/zpo/__1046.html) | Fristsetzung durch das Schiedsgericht; Zuständigkeitsrüge spätestens hier (§ 1040 Abs. 2) |
| Mündliche Verhandlung | [§ 1047 ZPO](https://www.gesetze-im-internet.de/zpo/__1047.html) | auf Antrag einer Partei zwingend, sofern nicht abbedungen |
| Säumnis | [§ 1048](https://www.gesetze-im-internet.de/zpo/__1048.html) | kein Versäumnisschiedsspruch nach Aktenlage ohne Prüfung; Fortsetzung des Verfahrens |
| Sachverständige | [§ 1049](https://www.gesetze-im-internet.de/zpo/__1049.html) | Bestellung durch das Schiedsgericht; Anhörungsrecht der Parteien |
| Gerichtliche Unterstützung | [§ 1050](https://www.gesetze-im-internet.de/zpo/__1050.html) | Antrag auf Unterstützung bei Beweisaufnahme und richterlichen Handlungen — **gilt auch bei ausländischem Schiedsort** (§ 1025 Abs. 2) |
| Anwendbares Recht | [§ 1051](https://www.gesetze-im-internet.de/zpo/__1051.html) | Rechtswahl der Parteien; Billigkeitsentscheidung nur bei ausdrücklicher Ermächtigung |
| Vergleich | [§ 1053](https://www.gesetze-im-internet.de/zpo/__1053.html) | Schiedsspruch mit vereinbartem Wortlaut — vollstreckbar wie ein Schiedsspruch |

### 5. Einstweiligen Rechtsschutz organisieren ([§ 1033](https://www.gesetze-im-internet.de/zpo/__1033.html), [§ 1041 ZPO](https://www.gesetze-im-internet.de/zpo/__1041.html))

Zwei parallele Wege, die sich nicht ausschließen:

- **§ 1033** — Die Schiedsvereinbarung hindert das **staatliche** Gericht nicht, vor oder nach Verfahrensbeginn vorläufige oder sichernde Maßnahmen anzuordnen (Arrest, einstweilige Verfügung; `/prozessrecht:einstweilige-verfuegung`). Diese Norm gilt nach § 1025 Abs. 2 auch bei ausländischem Schiedsort.
- **§ 1041 Abs. 1** — Das **Schiedsgericht** kann, wenn nichts anderes vereinbart ist, vorläufige oder sichernde Maßnahmen anordnen und Sicherheit verlangen. Solche Anordnungen sind **nicht unmittelbar vollstreckbar**: Nach § 1041 Abs. 2 lässt das staatliche Gericht die **Vollziehung** auf Antrag zu, sofern nicht bereits eine entsprechende Maßnahme bei einem Gericht beantragt wurde, und kann die Anordnung zur Vollziehung abweichend fassen. Zuständig ist das OLG (§ 1062 Abs. 1 Nr. 3).
- **§ 1041 Abs. 4** — Erweist sich die Anordnung als von Anfang an ungerechtfertigt, haftet die vollziehende Partei verschuldensunabhängig auf Schadensersatz; der Anspruch kann im anhängigen Schiedsverfahren geltend gemacht werden.

Vor Konstituierung des Schiedsgerichts ist der Weg über § 1033 der einzige praktikable — es sei denn, die Verfahrensordnung sieht einen Eilschiedsrichter vor.

### 6. Schiedsspruch und Kosten ([§ 1054](https://www.gesetze-im-internet.de/zpo/__1054.html), [§ 1055](https://www.gesetze-im-internet.de/zpo/__1055.html), [§ 1057](https://www.gesetze-im-internet.de/zpo/__1057.html), [§ 1058 ZPO](https://www.gesetze-im-internet.de/zpo/__1058.html))

**Formale Anforderungen des § 1054 — jede einzelne ist aufhebungsrelevant:**

1. **Schriftlich** erlassen und von den Schiedsrichtern **unterschrieben**; bei Mehrpersonenschiedsgerichten genügen die Unterschriften der **Mehrheit**, sofern der Grund für die fehlende Unterschrift angegeben wird (Abs. 1).
2. **Begründet**, es sei denn, die Parteien haben darauf verzichtet oder es handelt sich um einen Schiedsspruch mit vereinbartem Wortlaut (Abs. 2).
3. Angabe des **Tages des Erlasses** und des **Schiedsorts** nach § 1043 Abs. 1; der Spruch gilt als an diesem Tag und Ort erlassen (Abs. 3).
4. Übermittlung eines unterschriebenen Exemplars an **jede Partei** (Abs. 4).

Nach **§ 1055** hat der Schiedsspruch unter den Parteien die Wirkungen eines **rechtskräftigen gerichtlichen Urteils**. Die Zwangsvollstreckung setzt gleichwohl die Vollstreckbarerklärung voraus (`/schiedsverfahren-adr:vollstreckbarerklaerung-schiedsspruch`).

**Kosten (§ 1057):** Ohne abweichende Vereinbarung entscheidet das Schiedsgericht durch Schiedsspruch über die Kostenquote — einschließlich der zur zweckentsprechenden Rechtsverfolgung notwendigen Parteikosten — nach pflichtgemäßem Ermessen unter Berücksichtigung insbesondere des Verfahrensausgangs. Stehen die Kosten fest, entscheidet es auch über die Höhe; sonst ergeht ein gesonderter Kostenschiedsspruch (Abs. 2). **Anders als im staatlichen Verfahren gilt keine strikte Bindung an § 91 ZPO**, und die Erstattung ist nicht auf RVG-Sätze begrenzt.

**§ 1058** erlaubt Berichtigung, Auslegung und Ergänzung binnen eines Monats nach Empfang des Schiedsspruchs — und verlängert nach § 1059 Abs. 3 S. 3 die Aufhebungsfrist um höchstens einen Monat.

### 7. Institutionelle Verfahren

Wird die **DIS-Schiedsgerichtsordnung 2018** oder eine andere institutionelle Ordnung in Bezug genommen, verdrängt sie die dispositiven Regeln des Zehnten Buchs im Rahmen des § 1042 Abs. 3 — nicht jedoch die zwingenden Vorschriften. Institutionelle Fristen (Klageerwiderung, Verfahrenskonferenz, Erlass des Schiedsspruchs) sind gesondert zu erfassen und laufen neben den gesetzlichen Fristen. Der jeweils geltende Fassungsstand der Ordnung ist zu prüfen `[unverifiziert – prüfen]`.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; die Fristanknüpfung bleibt juristische Eingabe:

```bash
# § 1037 Abs. 2 ZPO: 2 Wochen ab Kenntnis des Ablehnungsgrundes am 05.03.2026
python -m scripts.legal_calc.cli frist --ereignis 05.03.2026 --menge 2 --einheit wochen --land BY

# § 1037 Abs. 3 ZPO: 1 Monat ab Kenntnis der ablehnenden Entscheidung
python -m scripts.legal_calc.cli frist --ereignis 02.04.2026 --menge 1 --einheit monate --land BY

# § 1035 Abs. 3 S. 3 ZPO: 1 Monat Untätigkeit nach Aufforderung zur Bestellung
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY

# § 1058 ZPO: 1 Monat für Berichtigungs-, Auslegungs- und Ergänzungsantrag
python -m scripts.legal_calc.cli frist --ereignis 20.11.2026 --menge 1 --einheit monate --land BY
```

## Quellen

### Statute

- [§ 1033](https://www.gesetze-im-internet.de/zpo/__1033.html), [§ 1034](https://www.gesetze-im-internet.de/zpo/__1034.html), [§ 1035](https://www.gesetze-im-internet.de/zpo/__1035.html), [§ 1036](https://www.gesetze-im-internet.de/zpo/__1036.html), [§ 1037](https://www.gesetze-im-internet.de/zpo/__1037.html), [§ 1040](https://www.gesetze-im-internet.de/zpo/__1040.html), [§ 1041](https://www.gesetze-im-internet.de/zpo/__1041.html), [§ 1042](https://www.gesetze-im-internet.de/zpo/__1042.html), [§ 1043](https://www.gesetze-im-internet.de/zpo/__1043.html), [§ 1044](https://www.gesetze-im-internet.de/zpo/__1044.html), [§ 1046](https://www.gesetze-im-internet.de/zpo/__1046.html), [§ 1047](https://www.gesetze-im-internet.de/zpo/__1047.html), [§ 1048](https://www.gesetze-im-internet.de/zpo/__1048.html), [§ 1049](https://www.gesetze-im-internet.de/zpo/__1049.html), [§ 1050](https://www.gesetze-im-internet.de/zpo/__1050.html), [§ 1051](https://www.gesetze-im-internet.de/zpo/__1051.html), [§ 1053](https://www.gesetze-im-internet.de/zpo/__1053.html), [§ 1054](https://www.gesetze-im-internet.de/zpo/__1054.html), [§ 1055](https://www.gesetze-im-internet.de/zpo/__1055.html), [§ 1056](https://www.gesetze-im-internet.de/zpo/__1056.html), [§ 1057](https://www.gesetze-im-internet.de/zpo/__1057.html), [§ 1058](https://www.gesetze-im-internet.de/zpo/__1058.html), [§ 1062 ZPO](https://www.gesetze-im-internet.de/zpo/__1062.html)
- [§ 204 BGB](https://www.gesetze-im-internet.de/bgb/__204.html) (Verjährungshemmung durch Beginn des schiedsrichterlichen Verfahrens)
- DIS-Schiedsgerichtsordnung 2018; ICC-Schiedsgerichtsordnung (Institutionenrecht) `[unverifiziert – prüfen]`
- IBA Guidelines on Conflicts of Interest in International Arbitration (soft law) `[unverifiziert – prüfen]`

### Kommentare

- Zöller/Geimer, ZPO, §§ 1034–1058.
- Musielak/Voit, ZPO, § 1042 Rn. 1 ff. (rechtliches Gehör), § 1054.
- Stein/Jonas/Schlosser, ZPO, Zehntes Buch.
- Schwab/Walter, Schiedsgerichtsbarkeit, Kap. Verfahren und Schiedsspruch.
- Salger/Trittmann, Internationale Schiedsverfahren, Praxishandbuch.

### Rechtsprechung

Zu Gehörsverstößen, zur Ablehnung von Schiedsrichtern und zu den Formanforderungen des § 1054 ZPO besteht gefestigte Rechtsprechung des BGH und der Oberlandesgerichte. Jede konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
SCHIEDSVERFAHREN — <Mandat> — <Datum>

I.   Rahmen
     Schiedsvereinbarung:     <Fundstelle im Vertrag>
     Verfahrensordnung:       <DIS 2018 / ICC / ad hoc>
     Schiedsort § 1043:       <Ort>   Sprache: <…>   Anwendbares Recht § 1051: <…>
     Verfahrensbeginn § 1044: <Datum>  → Verjährungshemmung § 204 Abs. 1 Nr. 11 BGB

II.  Schiedsgericht
     Anzahl:                  <vereinbart / drei nach § 1034 Abs. 1 S. 2>
     Bestellung § 1035:       <Stand>   Gerichtliche Bestellung erforderlich: [ja / nein]
     Übergewicht § 1034 Abs. 2: [ja — Frist 2 Wochen bis <Datum> / nein]
     Offenlegung § 1036 Abs. 1: [vollständig / Lücken: …]
     Ablehnung § 1037:        Frist 2 Wochen bis <Datum>; gerichtlich 1 Monat bis <Datum>

III. Verfahrensführung
     Gleichbehandlung / rechtliches Gehör § 1042 Abs. 1: <Feststellungen>
     Erhobene Rügen (protokolliert):  <…>
     Zuständigkeitsrüge § 1040 Abs. 2: [mit Klagebeantwortung erhoben / offen]
     Beweisaufnahme:          <…>   Unterstützung § 1050 erforderlich: [ja / nein]
     Mündliche Verhandlung § 1047: <Stand>

IV.  Einstweiliger Rechtsschutz
     § 1033 staatliches Gericht: [beantragt / geplant / nein]
     § 1041 Schiedsgericht:      [angeordnet — Vollziehung § 1041 Abs. 2 beim OLG / nein]
     Schadensersatzrisiko § 1041 Abs. 4: <…>

V.   Schiedsspruch
     § 1054 Abs. 1 Schriftform und Unterschriften: [erfüllt / Grund für fehlende Unterschrift angegeben?]
     Abs. 2 Begründung:        [vorhanden / wirksam abbedungen]
     Abs. 3 Tag und Schiedsort: [angegeben / fehlt]
     Abs. 4 Übermittlung:       [erfolgt am <Datum>]
     § 1057 Kosten:             <Quote / gesonderter Kostenschiedsspruch>
     § 1058 Berichtigung:       Frist 1 Monat bis <Datum>

VI.  Aufhebungsrisiko (Vorprüfung § 1059 Abs. 2)
     <je Nummer: Anhaltspunkte / keine>

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Gehörsverstoß nicht sofort gerügt.** Wer den Verstoß gegen § 1042 Abs. 1 ZPO hinnimmt und erst im Aufhebungsverfahren vorträgt, verliert den Einwand regelmäßig. Rügen gehören ins Protokoll.
- **Ablehnungsfristen versäumt.** § 1037 Abs. 2 ZPO gibt zwei Wochen ab Kenntnis, Abs. 3 einen Monat für den gerichtlichen Antrag.
- **Anordnung des Schiedsgerichts nach § 1041 ZPO für vollstreckbar gehalten.** Erforderlich ist die Zulassung der Vollziehung durch das OLG nach § 1041 Abs. 2 ZPO.
- **§ 1033 ZPO übersehen.** Der staatliche Eilrechtsschutz bleibt trotz Schiedsvereinbarung offen und ist vor Konstituierung des Schiedsgerichts oft der einzige Weg.
- **Schiedsspruch ohne Angabe von Tag und Schiedsort.** § 1054 Abs. 3 ZPO ist Wirksamkeitsvoraussetzung und bestimmt zugleich die Zuständigkeit nach § 1062 ZPO.
- **Fehlende Unterschrift ohne Begründung.** § 1054 Abs. 1 S. 2 ZPO verlangt die Angabe des Grundes.
- **Begründung ohne wirksamen Verzicht weggelassen.** § 1054 Abs. 2 ZPO lässt das nur bei Parteivereinbarung oder Schiedsspruch mit vereinbartem Wortlaut zu.
- **Kostenentscheidung an § 91 ZPO und RVG-Sätzen ausgerichtet.** § 1057 ZPO gibt dem Schiedsgericht pflichtgemäßes Ermessen und erfasst die notwendigen Parteikosten.
- **Verjährungshemmung falsch datiert.** Maßgeblich ist nach § 1044 ZPO der Empfang des Antrags durch den Beklagten.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
