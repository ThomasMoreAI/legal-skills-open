---
name: vollstreckbarerklaerung-schiedsspruch-borghei
title: /schiedsverfahren-adr:vollstreckbarerklaerung-schiedsspruch
description: Vollstreckbarerklärung von Schiedssprüchen – inländische Schiedssprüche § 1060 ZPO mit Ablehnung unter Aufhebung bei Gründen nach § 1059 Abs. 2 und Präklusion nach Fristablauf § 1060 Abs. 2 S. 3, ausländische Schiedssprüche § 1061 ZPO iVm dem New Yorker Übereinkommen von 1958 mit den Versagungsgründen des Art. V, Meistbegünstigung nach Art. VII, Vorlagepflichten § 1064 und vorläufige Vollstreckbarkeit Abs. 2, OLG-Zuständigkeit § 1062 einschließlich Auffangzuständigkeit des Kammergerichts, Verfahren § 1063 mit zwingender mündlicher Verhandlung bei möglichen Aufhebungsgründen und Sicherungsanordnung Abs. 3, Rechtsbeschwerde § 1065 sowie die anschließende Zwangsvollstreckung nach dem Achten Buch der ZPO. Use when aus einem Schiedsspruch vollstreckt werden soll oder die Vollstreckbarerklärung abzuwehren ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/schiedsverfahren-adr/skills/vollstreckbarerklaerung-schiedsspruch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: arbitration
language: de
---

# /schiedsverfahren-adr:vollstreckbarerklaerung-schiedsspruch

## Zweck

Der Skill führt vom Schiedsspruch zum vollstreckbaren Titel. Er trennt die beiden Regime — inländische Schiedssprüche nach § 1060 ZPO, ausländische nach § 1061 ZPO iVm dem New Yorker Übereinkommen —, ordnet die Versagungsgründe zu, prüft Präklusion und Beweislast und entwirft Antrag oder Abwehr. Er schließt mit der Anschlussfrage, wie aus dem Beschluss tatsächlich vollstreckt wird.

## Eingaben

- Schiedsspruch im Original oder in beglaubigter Abschrift; Sprache und Übersetzungsstand
- Schiedsort (bestimmt in- oder ausländische Herkunft) und Datum des Empfangs
- Schiedsvereinbarung im Original oder in beglaubigter Abschrift
- Ob ein Aufhebungsverfahren im Herkunftsstaat anhängig oder abgeschlossen ist
- Sitz oder gewöhnlicher Aufenthalt des Antragsgegners; belegenes Vermögen im Inland
- Vollstreckungsziel: Geldforderung, Handlung, Duldung, Unterlassung
- Ob bereits Sicherungsmaßnahmen erforderlich sind

## Sub-Agent-Architektur

Der Researcher beschafft §§ 1060 bis 1065 ZPO, den Text des New Yorker Übereinkommens, etwaige bilaterale Staatsverträge und die Rechtsprechung zum ordre public international. Der Drafter erstellt Antrag oder Erwiderung samt Anlagenkatalog. Der Reviewer prüft die Vollständigkeit der vorzulegenden Urkunden, die Zuständigkeit nach § 1062 und – bei der Abwehr – ob die Versagungsgründe nicht bereits präkludiert sind.

> **Hinweis zum Rechtsstand.** Das Zehnte Buch der ZPO ist Gegenstand des Gesetzes vom 20.05.2026 (BGBl. 2026 I Nr. 152); die Änderungen sind auf gesetze-im-internet.de textlich nachgewiesen, dokumentarisch aber noch nicht abschließend eingearbeitet. Der konsolidierte Stand ist gegen das Bundesgesetzblatt abzugleichen `[unverifiziert – prüfen]`.

## Ablauf

### 1. Herkunft des Schiedsspruchs bestimmen

**Dieser Schritt entscheidet über das gesamte Prüfprogramm.**

| Schiedsort | Regime | Versagungsgründe |
|---|---|---|
| **Deutschland** | [§ 1060 ZPO](https://www.gesetze-im-internet.de/zpo/__1060.html) | § 1059 Abs. 2 ZPO |
| **Ausland** | [§ 1061 ZPO](https://www.gesetze-im-internet.de/zpo/__1061.html) iVm dem Übereinkommen vom 10.06.1958 über die Anerkennung und Vollstreckung ausländischer Schiedssprüche (New Yorker Übereinkommen, BGBl. 1961 II S. 121) | Art. V NYÜ |

Maßgeblich ist der **rechtliche Schiedsort** nach § 1043 Abs. 1 ZPO, nicht der Ort der Verhandlungen oder der Unterzeichnung. Vorschriften anderer Staatsverträge über die Anerkennung und Vollstreckung bleiben nach § 1061 Abs. 1 S. 2 ZPO unberührt.

### 2. Inländische Schiedssprüche ([§ 1060 ZPO](https://www.gesetze-im-internet.de/zpo/__1060.html))

- **Abs. 1** — Die Zwangsvollstreckung findet statt, wenn der Schiedsspruch **für vollstreckbar erklärt** ist. Die Wirkung eines rechtskräftigen Urteils nach § 1055 ZPO genügt dafür nicht.
- **Abs. 2 S. 1** — Der Antrag ist **unter Aufhebung des Schiedsspruchs** abzulehnen, wenn ein Aufhebungsgrund nach § 1059 Abs. 2 vorliegt.
- **Abs. 2 S. 2** — Aufhebungsgründe sind nicht zu berücksichtigen, soweit ein darauf gestützter Aufhebungsantrag bei Zustellung des Vollstreckbarerklärungsantrags bereits **rechtskräftig abgewiesen** ist.
- **Abs. 2 S. 3** — Gründe nach § 1059 Abs. 2 **Nr. 1** sind auch dann nicht zu berücksichtigen, wenn die Fristen des § 1059 Abs. 3 abgelaufen sind, ohne dass ein Aufhebungsantrag gestellt wurde.

Daraus folgt die zentrale Weichenstellung für die Abwehr: **Die Gründe der Nr. 1 müssen innerhalb der Dreimonatsfrist des § 1059 Abs. 3 ZPO durch Aufhebungsantrag geltend gemacht werden**, sonst sind sie auch als Verteidigung verloren. Die Gründe der Nr. 2 — fehlende Schiedsfähigkeit und ordre public — sind von Amts wegen zu prüfen und nicht präkludierbar (`/schiedsverfahren-adr:aufhebungsantrag-1059`).

### 3. Ausländische Schiedssprüche ([§ 1061 ZPO](https://www.gesetze-im-internet.de/zpo/__1061.html), NYÜ)

Das Übereinkommen kehrt die Beweislast um: Der Antragsteller legt die Urkunden vor; die **Versagungsgründe des Art. V Abs. 1 NYÜ hat der Antragsgegner darzulegen und zu beweisen**. Nur die Gründe des Art. V Abs. 2 prüft das Gericht von Amts wegen.

**Art. V Abs. 1 NYÜ — auf Einwand des Antragsgegners:**

| lit. | Versagungsgrund |
|---|---|
| a | Parteiunfähigkeit oder Ungültigkeit der Schiedsvereinbarung nach dem gewählten Recht, hilfsweise nach dem Recht des Schiedsortes |
| b | Fehlende ordnungsgemäße Unterrichtung über Schiedsrichterbestellung oder Verfahren; Unmöglichkeit, Angriffs- und Verteidigungsmittel geltend zu machen |
| c | Überschreitung der Grenzen der Schiedsvereinbarung — mit der Möglichkeit der **Teilanerkennung** des abtrennbaren Teils |
| d | Bildung des Schiedsgerichts oder Verfahren entsprachen nicht der Parteivereinbarung oder, hilfsweise, dem Recht des Schiedsortes |
| e | Der Schiedsspruch ist für die Parteien **noch nicht verbindlich** oder wurde im Herkunftsstaat **aufgehoben oder ausgesetzt** |

**Art. V Abs. 2 NYÜ — von Amts wegen:**

- a) Der Streitgegenstand ist nach dem Recht des Vollstreckungsstaates **nicht schiedsfähig**;
- b) Anerkennung oder Vollstreckung würde der **öffentlichen Ordnung** des Vollstreckungsstaates widersprechen (**ordre public international** — noch enger als der innerstaatliche Maßstab).

**Meistbegünstigung, Art. VII NYÜ:** Das Übereinkommen sperrt nicht die Anwendung anerkennungsfreundlicheren nationalen Rechts oder anderer Staatsverträge. Der Antragsteller kann sich auf die für ihn günstigere Regelung berufen — ein in der Praxis regelmäßig übersehener Hebel.

**Aufhebung im Ausland nach Vollstreckbarerklärung:** Nach § 1061 Abs. 3 ZPO kann die **Aufhebung der Vollstreckbarerklärung** beantragt werden, wenn der Schiedsspruch nach der Vollstreckbarerklärung im Ausland aufgehoben wird. Wird die Vollstreckbarerklärung abgelehnt, stellt das Gericht nach § 1061 Abs. 2 ZPO fest, dass der Schiedsspruch **im Inland nicht anzuerkennen** ist.

### 4. Zuständigkeit ([§ 1062 ZPO](https://www.gesetze-im-internet.de/zpo/__1062.html))

- **Abs. 1 Nr. 4** — Zuständig ist das in der Schiedsvereinbarung bezeichnete **Oberlandesgericht**, sonst das OLG des Schiedsortbezirks, für Aufhebung, Vollstreckbarerklärung und Aufhebung der Vollstreckbarerklärung.
- **Abs. 2** — Fehlt ein deutscher Schiedsort, ist das OLG zuständig, in dessen Bezirk der **Antragsgegner** Sitz oder gewöhnlichen Aufenthalt hat oder sich **Vermögen** des Antragsgegners bzw. der betroffene Gegenstand befindet; **hilfsweise das Kammergericht**.

Die Vermögensbelegenheit ist damit ein eigenständiger Zuständigkeitsanker — bei ausländischen Antragsgegnern der praktisch wichtigste.

### 5. Verfahren und Urkundenvorlage ([§ 1063 ZPO](https://www.gesetze-im-internet.de/zpo/__1063.html), [§ 1064 ZPO](https://www.gesetze-im-internet.de/zpo/__1064.html))

- **Form** (§ 1064 Abs. 1): Mit dem Antrag ist der **Schiedsspruch oder eine beglaubigte Abschrift** vorzulegen; die **Beglaubigung kann der für das gerichtliche Verfahren bevollmächtigte Rechtsanwalt** vornehmen. Das ist eine erhebliche Erleichterung gegenüber Art. IV NYÜ; sie gilt nach § 1064 Abs. 3 auch für ausländische Schiedssprüche, soweit Staatsverträge nichts anderes bestimmen — Ausdruck der Meistbegünstigung nach Art. VII NYÜ.
- **Verfahren** (§ 1063 Abs. 1): Entscheidung durch **Beschluss** nach Anhörung des Gegners.
- **Mündliche Verhandlung** (§ 1063 Abs. 2): **zwingend anzuordnen**, wenn die Aufhebung beantragt wird oder wenn bei einem Antrag auf Anerkennung oder Vollstreckbarerklärung Aufhebungsgründe nach § 1059 Abs. 2 **in Betracht kommen**.
- **Eilrechtsschutz** (§ 1063 Abs. 3): Der Vorsitzende des Zivilsenats kann **ohne vorherige Anhörung** des Gegners anordnen, dass der Antragsteller bis zur Entscheidung die Zwangsvollstreckung betreiben oder eine Maßnahme nach § 1041 ZPO vollziehen darf; die Vollstreckung darf **nicht über Sicherungsmaßnahmen hinausgehen**. Der Antragsgegner kann durch Sicherheitsleistung abwenden.
- **Vorläufige Vollstreckbarkeit** (§ 1064 Abs. 2): Der stattgebende Beschluss ist **für vorläufig vollstreckbar zu erklären**.
- **Rechtsmittel** (§ 1065 Abs. 1): **Rechtsbeschwerde** zum BGH gegen Entscheidungen nach § 1062 Abs. 1 Nr. 2 und Nr. 4; sie kann auch auf die Verletzung eines Staatsvertrags gestützt werden (Abs. 2).

### 6. Anschluss an die Zwangsvollstreckung

Der Beschluss über die Vollstreckbarerklärung ist Vollstreckungstitel iSd [§ 794 Abs. 1 Nr. 4a ZPO](https://www.gesetze-im-internet.de/zpo/__794.html). Es folgen Klauselerteilung und Zustellung nach §§ 724 ff., 750 ZPO und sodann die Vollstreckungsmaßnahme — Pfändungs- und Überweisungsbeschluss nach §§ 829, 835 ZPO, Sachpfändung, Zwangsvollstreckung in Grundstücke. Vertiefung: `/zwangsvollstreckung:pfaendungs-ueberweisungsbeschluss` bzw. die einschlägige Skill des Plugins `zwangsvollstreckung`.

Materielle Einwendungen gegen den titulierten Anspruch, die **nach** dem für die Aufhebung maßgeblichen Zeitpunkt entstanden sind, sind mit der Vollstreckungsabwehrklage nach [§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html) geltend zu machen — nicht im Vollstreckbarerklärungsverfahren.

## Deterministische Berechnung

Die kritische Frist des Verfahrens liegt nicht hier, sondern im Aufhebungsrecht: Wer die Dreimonatsfrist des § 1059 Abs. 3 ZPO versäumt, verliert nach § 1060 Abs. 2 S. 3 ZPO die Gründe der Nr. 1. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# § 1059 Abs. 3 ZPO: 3 Monate ab Empfang des Schiedsspruchs — Präklusionsgrenze für § 1060 Abs. 2 S. 3
python -m scripts.legal_calc.cli frist --ereignis 20.11.2026 --menge 3 --einheit monate --land BE

# Rechtsbeschwerdefrist § 575 Abs. 1 ZPO: 1 Monat ab Zustellung des Beschlusses
python -m scripts.legal_calc.cli frist --ereignis 10.03.2027 --menge 1 --einheit monate --land BE

# Gerichtskosten der Vollstreckbarerklärung: Gebührensatz 2,0 nach KV GKG Nr. 1620
python -m scripts.legal_calc.cli gkg --wert 850000 --faktor 2.0
```

## Quellen

### Statute und Staatsverträge

- [§ 1055](https://www.gesetze-im-internet.de/zpo/__1055.html), [§ 1059](https://www.gesetze-im-internet.de/zpo/__1059.html), [§ 1060](https://www.gesetze-im-internet.de/zpo/__1060.html), [§ 1061](https://www.gesetze-im-internet.de/zpo/__1061.html), [§ 1062](https://www.gesetze-im-internet.de/zpo/__1062.html), [§ 1063](https://www.gesetze-im-internet.de/zpo/__1063.html), [§ 1064](https://www.gesetze-im-internet.de/zpo/__1064.html), [§ 1065 ZPO](https://www.gesetze-im-internet.de/zpo/__1065.html)
- [§ 767](https://www.gesetze-im-internet.de/zpo/__767.html), [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html), [§ 829 ZPO](https://www.gesetze-im-internet.de/zpo/__829.html), [§ 835 ZPO](https://www.gesetze-im-internet.de/zpo/__835.html)
- Übereinkommen vom 10.06.1958 über die Anerkennung und Vollstreckung ausländischer Schiedssprüche (New Yorker Übereinkommen), BGBl. 1961 II S. 121 — Art. II, III, IV, V, VII. Das Übereinkommen ist **nicht** auf gesetze-im-internet.de veröffentlicht; maßgeblich ist der Text im Bundesgesetzblatt.

### Kommentare

- Zöller/Geimer, ZPO, §§ 1060–1065 sowie Anhang zum NYÜ.
- Musielak/Voit, ZPO, § 1061 Rn. 1 ff.
- Stein/Jonas/Schlosser, ZPO, § 1061, Anhang NYÜ.
- Schwab/Walter, Schiedsgerichtsbarkeit, Kap. Anerkennung und Vollstreckung.
- Adolphsen, Internationale Schiedsgerichtsbarkeit (zum ordre public international).

### Rechtsprechung

Zur Auslegung des Art. V NYÜ, zum ordre public international und zur Meistbegünstigung nach Art. VII NYÜ besteht gefestigte Rechtsprechung des BGH und der Oberlandesgerichte. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf den Seiten des BGH zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
VOLLSTRECKBARERKLÄRUNG — <Mandat> — <Datum>

I.   Herkunft und Regime
     Schiedsort § 1043 Abs. 1:  <Ort, Staat>
     Regime:                    [§ 1060 ZPO — inländisch | § 1061 ZPO iVm NYÜ — ausländisch]
     Weitere Staatsverträge:    <…> (Art. VII NYÜ Meistbegünstigung geprüft: [ja / nein])

II.  Zuständigkeit
     § 1062 Abs. 1 Nr. 4:       OLG <…>
     § 1062 Abs. 2 (kein dt. Schiedsort): <Sitz / Vermögensbelegenheit / KG>

III. Antragsvoraussetzungen
     Vorlage § 1064 Abs. 1:     [Original / beglaubigte Abschrift — Beglaubigung durch RA]
     Übersetzung:               [erforderlich / vorhanden]
     Schiedsvereinbarung:       [vorgelegt / nicht erforderlich nach § 1064 iVm Art. VII NYÜ]

IV.  Versagungsgründe
     Inländisch (§ 1059 Abs. 2 iVm § 1060 Abs. 2):
       Nr. 1 lit. a–d:          [präkludiert nach § 1060 Abs. 2 S. 3 / geltend gemacht]
       Nr. 2 lit. a, b:         [von Amts wegen — Feststellung]
     Ausländisch (Art. V NYÜ):
       Abs. 1 lit. a–e:         [Darlegungs- und Beweislast beim Antragsgegner — Befund]
       Abs. 2 lit. a, b:        [von Amts wegen — ordre public international]
     Aufhebung im Herkunftsstaat: [anhängig / erfolgt — Art. V Abs. 1 lit. e / nein]

V.   Verfahren
     Mündliche Verhandlung § 1063 Abs. 2: [zwingend / nicht erforderlich]
     Sicherungsanordnung § 1063 Abs. 3:   [beantragt / nicht erforderlich]
     Vorläufige Vollstreckbarkeit § 1064 Abs. 2: von Amts wegen
     Rechtsbeschwerde § 1065:             Frist bis <Datum>

VI.  Anschlussvollstreckung
     Titel § 794 Abs. 1 Nr. 4a ZPO → Klausel §§ 724 ff. → Zustellung § 750 → Maßnahme <…>
     Materielle Einwendungen:   § 767 ZPO, nicht im Vollstreckbarerklärungsverfahren

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **§ 1055 ZPO mit Vollstreckbarkeit verwechselt.** Der Schiedsspruch wirkt wie ein rechtskräftiges Urteil, ist aber erst nach Vollstreckbarerklärung Vollstreckungstitel.
- **Falsches Regime gewählt.** Die Herkunft richtet sich nach dem rechtlichen Schiedsort, nicht nach Verhandlungs- oder Unterzeichnungsort.
- **Aufhebungsgründe der Nr. 1 nicht fristgerecht geltend gemacht.** § 1060 Abs. 2 S. 3 ZPO präkludiert sie nach Ablauf der Dreimonatsfrist des § 1059 Abs. 3 ZPO auch als Verteidigung.
- **Beweislast bei Art. V NYÜ verkannt.** Abs. 1 trägt der Antragsgegner; nur Abs. 2 prüft das Gericht von Amts wegen.
- **Meistbegünstigung nach Art. VII NYÜ übersehen.** Anerkennungsfreundlicheres nationales Recht — etwa die Beglaubigung durch den Rechtsanwalt nach § 1064 Abs. 1 S. 2 ZPO — bleibt anwendbar.
- **Ordre public international mit innerstaatlichem ordre public gleichgesetzt.** Der Maßstab bei ausländischen Schiedssprüchen ist enger.
- **Zuständigkeitsanker der Vermögensbelegenheit übersehen** (§ 1062 Abs. 2 ZPO), obwohl der Antragsgegner keinen inländischen Sitz hat.
- **Mündliche Verhandlung für entbehrlich gehalten**, obwohl Aufhebungsgründe in Betracht kommen (§ 1063 Abs. 2 ZPO).
- **Materielle Einwendungen im Vollstreckbarerklärungsverfahren vorgetragen** statt über § 767 ZPO.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
