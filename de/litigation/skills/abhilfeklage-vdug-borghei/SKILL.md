---
name: abhilfeklage-vdug-borghei
title: /verbandsklage-vdug:abhilfeklage-vdug
description: Abhilfeklage nach §§ 14 ff. VDuG – Leistung an die betroffenen Verbraucher oder Zahlung eines kollektiven Gesamtbetrags § 14, Gleichartigkeitserfordernis § 15 Abs. 1 (derselbe oder im Wesentlichen vergleichbarer Sachverhalt und im Wesentlichen gleiche Tatsachen- und Rechtsfragen) nebst Angaben zur Anspruchshöhe oder Berechnungsmethode § 15 Abs. 2, Abhilfegrundurteil § 16 mit Anspruchsvoraussetzungen und Berechtigungsnachweisen in der Urteilsformel, Vergleichsvorschlag § 17, Abhilfeendurteil § 18 mit Anordnung des Umsetzungsverfahrens, vorläufiger Kostenfestsetzung und zulassungsfreier Revision, Schätzung des kollektiven Gesamtbetrags § 19 iVm § 287 ZPO, Kosten § 20 und Erhöhung § 21. Use when eine Abhilfeklage zu erheben, zu verteidigen oder ein Abhilfegrundurteil umzusetzen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verbandsklage-vdug/skills/abhilfeklage-vdug
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /verbandsklage-vdug:abhilfeklage-vdug

## Zweck

Der Skill führt die Abhilfeklage durch ihre drei Stufen: Zulässigkeit der Gleichartigkeit, Abhilfegrundurteil dem Grunde nach, Abhilfeendurteil mit Anordnung des Umsetzungsverfahrens. Er behandelt die Frage, an der die Klage in der Praxis am häufigsten scheitert — die **Gleichartigkeit** nach § 15 Abs. 1 — und die Frage, die den wirtschaftlichen Ausgang bestimmt: die Bemessung des **kollektiven Gesamtbetrags**.

## Eingaben

- Lebenssachverhalt und beanstandetes Verhalten (Klausel, Preisanpassung, Produktmangel, Datenschutzverstoß)
- Anspruchsgrundlage je Verbraucher und die tatsächlichen Unterschiede zwischen den Betroffenen
- Angestrebte Leistung: Zahlung an namentlich benannte Verbraucher, kollektiver Gesamtbetrag oder andere Leistung
- Berechnungsmethode für den Einzelanspruch; verfügbare Datenbasis beim Unternehmer
- Verfahrensstand: Klageschrift, mündliche Verhandlung, Grundurteil, Endurteil
- Wirtschaftliche Eckdaten des Unternehmers für Kosten- und Vergleichsplanung

## Sub-Agent-Architektur

Der Researcher beschafft VDuG, ZPO (insbesondere § 287), die Anspruchsgrundlagen des materiellen Rechts und die junge obergerichtliche Rechtsprechung. Der Drafter formuliert Klageantrag, Gleichartigkeitsdarlegung und Berechnungsmethode oder — auf Beklagtenseite — die Individualisierungsrüge. Der Reviewer prüft, ob die Urteilsformel nach § 16 Abs. 2 vollstreckungs- und umsetzungstauglich ist und ob die Revisionsfrist gewahrt wird.

## Ablauf

### 1. Klageziel bestimmen ([§ 14 VDuG](https://www.gesetze-im-internet.de/vdug/__14.html))

Mit der Abhilfeklage begehrt die klageberechtigte Stelle die **Verurteilung des Unternehmers zu einer Leistung an die betroffenen Verbraucher**. Als Leistung kann auch die **Zahlung eines kollektiven Gesamtbetrags** begehrt werden.

Drei Antragsvarianten mit unterschiedlichen Folgen:

| Antrag | Urteil | Umsetzungsverfahren |
|---|---|---|
| Zahlung an **namentlich benannte** Verbraucher | **Urteil** (§ 16 Abs. 1 S. 2) | nicht erforderlich |
| **Kollektiver Gesamtbetrag** | **Abhilfegrundurteil** (§ 16 Abs. 1 S. 1), dann Abhilfeendurteil | erforderlich |
| **Andere Leistung als Zahlung** | **Abhilfegrundurteil**, dann Abhilfeendurteil | erforderlich |

Die Wahl entscheidet über Verfahrensdauer, Kostenlast und darüber, ob ein Sachwalter bestellt wird (`/verbandsklage-vdug:anmeldung-umsetzungsverfahren`).

### 2. Gleichartigkeit prüfen ([§ 15 Abs. 1 VDuG](https://www.gesetze-im-internet.de/vdug/__15.html)) — die zentrale Hürde

Die Abhilfeklage ist **nur zulässig**, wenn die betroffenen Verbraucheransprüche **im Wesentlichen gleichartig** sind. Das ist der Fall, wenn **kumulativ**

1. die Ansprüche **auf demselben Sachverhalt oder auf einer Reihe im Wesentlichen vergleichbarer Sachverhalte** beruhen **und**
2. für die Ansprüche die **im Wesentlichen gleichen Tatsachen- und Rechtsfragen entscheidungserheblich** sind.

Die typische Verteidigung ist die **Individualisierungsrüge**: individuelle Kenntnis, individuelle Kausalität, individuelle Mitverschuldensanteile, unterschiedliche Vertragsgenerationen, abweichende Tarife oder Verjährungsstände machten die Ansprüche ungleichartig. Der Kläger begegnet ihr durch **Gruppenbildung** — Bildung homogener Verbrauchergruppen mit je eigener Berechnungsmethode — statt durch Behauptung pauschaler Gleichheit.

**§ 15 Abs. 2** verlangt in der Klageschrift:

- **Angaben zur Gleichartigkeit** der betroffenen Ansprüche;
- bei Antrag auf kollektiven Gesamtbetrag zusätzlich die **Höhe des einzelnen Verbraucheranspruchs**, wenn alle Ansprüche gleich hoch sind;
- andernfalls **soll** die **Methode** angegeben werden, nach der sich die Einzelbeträge berechnen lassen.

Die Berechnungsmethode ist damit ein Zulässigkeits- und zugleich ein Vollstreckungsthema: Sie wandert in die Urteilsformel des § 16 Abs. 2.

### 3. Abhilfegrundurteil ([§ 16 VDuG](https://www.gesetze-im-internet.de/vdug/__16.html))

Hält das Gericht eine auf kollektiven Gesamtbetrag oder auf eine andere Leistung als Zahlung gerichtete Abhilfeklage **dem Grunde nach** für begründet, erlässt es ein **Abhilfegrundurteil**. Bei Leistung an namentlich benannte Verbraucher entscheidet es im Fall der Verurteilung zur Zahlung durch **Urteil**. Unzulässige oder unbegründete Klagen weist es durch Urteil ab.

**Die Urteilsformel des Abhilfegrundurteils enthält zwingend (Abs. 2):**

1. die **konkreten Voraussetzungen**, nach denen sich die Anspruchsberechtigung der betroffenen Verbraucher bestimmt, **und**
2. die von **jedem einzelnen Verbraucher im Umsetzungsverfahren zu erbringenden Berechtigungsnachweise**.

Bei kollektivem Gesamtbetrag zusätzlich: der **Betrag je berechtigtem Verbraucher** oder — bei unterschiedlichen Beträgen — die **Berechnungsmethode**.

**Praxisfolge:** Wer als Kläger die Berechtigungsnachweise nicht durchdacht beantragt, erhält eine Urteilsformel, an der das Umsetzungsverfahren später scheitert. Wer als Beklagter hier nicht mitgestaltet, trägt später den Aufwand einer unpraktikablen Nachweislage.

### 4. Vergleichsvorschlag ([§ 17 VDuG](https://www.gesetze-im-internet.de/vdug/__17.html))

Nach dem Abhilfegrundurteil eröffnet § 17 die Möglichkeit eines **Vergleichsvorschlags**; kommt kein Vergleich zustande, wird das Abhilfeverfahren fortgesetzt. Für das Unternehmen ist dies der wirtschaftlich wichtigste Zeitpunkt: Der Haftungsgrund steht dann fest, die Höhe noch nicht.

### 5. Abhilfeendurteil ([§ 18 VDuG](https://www.gesetze-im-internet.de/vdug/__18.html))

Die Urteilsformel enthält (Abs. 1):

1. die **Anordnung des Umsetzungsverfahrens**,
2. die **vorläufige Festsetzung der Kosten** des Umsetzungsverfahrens,
3. die **Verurteilung des Unternehmers zur Zahlung dieser Kosten zu Händen des Sachwalters**,
4. die Entscheidung über die Verfahrenskosten.

Bei kollektivem Gesamtbetrag zusätzlich die **Verurteilung zur Zahlung dieses Betrags zu Händen des Sachwalters** (Abs. 2). Bei besonderen Umständen — insbesondere einer Vielzahl betroffener Ansprüche — kann das Gericht die **Widerspruchsfrist des § 28 Abs. 2 S. 1 angemessen verlängern** (Abs. 3).

**Abs. 4: Gegen Abhilfeendurteile findet die Revision statt; sie bedarf keiner Zulassung.** Das ist der praktisch wichtigste Rechtsmittelhinweis des Gebiets — eine zulassungsfreie Revision zum BGH.

### 6. Kollektiver Gesamtbetrag ([§ 19 VDuG](https://www.gesetze-im-internet.de/vdug/__19.html), [§ 20](https://www.gesetze-im-internet.de/vdug/__20.html), [§ 21 VDuG](https://www.gesetze-im-internet.de/vdug/__21.html))

- **§ 19 Abs. 1** — Das Gericht kann die Höhe des kollektiven Gesamtbetrags **unter Würdigung aller Umstände nach freier Überzeugung** bestimmen.
- **§ 19 Abs. 2** — **[§ 287 ZPO](https://www.gesetze-im-internet.de/zpo/__287.html) ist entsprechend anzuwenden.** Die Schätzung ist damit der Regelfall, nicht die Ausnahme; der Vortrag zur Schätzgrundlage entscheidet über die Größenordnung.
- **§ 20** — Kosten des Umsetzungsverfahrens.
- **§ 21** — **Erhöhung** des kollektiven Gesamtbetrags, wenn der Fonds nicht ausreicht; § 19 gilt entsprechend (Fußnote zu § 19). Für den Unternehmer bedeutet das: Der zunächst titulierte Betrag ist **keine Haftungsobergrenze**.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; Schätzgrundlage und Gruppenbildung bleiben juristische Eingaben:

```bash
# Revisionsfrist § 548 ZPO: 1 Monat ab Zustellung des Abhilfeendurteils
python -m scripts.legal_calc.cli frist --ereignis 20.05.2026 --menge 1 --einheit monate --land BY

# Anmeldefrist § 46 Abs. 1 VDuG: 3 Wochen ab Schluss der mündlichen Verhandlung, ohne § 193 BGB
python -m scripts.legal_calc.cli frist --ereignis 14.03.2026 --menge 3 --einheit wochen --land BY --kein-rollover

# Gerichtskosten: Streitwert nach § 48 Abs. 1 S. 3 GKG auf 300.000 EUR begrenzt
# (12 Mio. EUR Forderungsvolumen -> 300.000 EUR); Gebührensatz 4,0 nach KV GKG Nr. 1212
# (erster Rechtszug vor dem OLG)
python -m scripts.legal_calc.cli gkg --wert 300000 --faktor 4.0
```

## Quellen

### Statute

- [§ 14](https://www.gesetze-im-internet.de/vdug/__14.html), [§ 15](https://www.gesetze-im-internet.de/vdug/__15.html), [§ 16](https://www.gesetze-im-internet.de/vdug/__16.html), [§ 17](https://www.gesetze-im-internet.de/vdug/__17.html), [§ 18](https://www.gesetze-im-internet.de/vdug/__18.html), [§ 19](https://www.gesetze-im-internet.de/vdug/__19.html), [§ 20](https://www.gesetze-im-internet.de/vdug/__20.html), [§ 21](https://www.gesetze-im-internet.de/vdug/__21.html), [§ 28](https://www.gesetze-im-internet.de/vdug/__28.html), [§ 46 VDuG](https://www.gesetze-im-internet.de/vdug/__46.html)
- [§ 287 ZPO](https://www.gesetze-im-internet.de/zpo/__287.html), [§ 548 ZPO](https://www.gesetze-im-internet.de/zpo/__548.html)
- Richtlinie (EU) 2020/1828 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2020/1828/oj)

### Kommentare und Literatur

- Röthemeyer, VDuG, Kommentar, §§ 14–21.
- Nordholtz/Mekat, Musterfeststellungsklage und Verbandsklage, Kap. Abhilfeklage.
- Zöller/Greger, ZPO, § 287 (Schätzung).
- Beiträge zur Gleichartigkeit nach § 15 VDuG in NJW, ZIP und VuR 2024–2026 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zur Gleichartigkeit nach § 15 VDuG und zur Bemessung des kollektiven Gesamtbetrags liegt noch keine gefestigte höchstrichterliche Rechtsprechung vor. Für § 287 ZPO ist auf die allgemeine Schätzungsrechtsprechung zurückzugreifen; jede konkrete Entscheidung ist vor Verwendung zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
ABHILFEKLAGE — <Mandat> — <Datum>

I.   Klageziel § 14
     Antragsvariante:         [namentlich benannte Verbraucher / kollektiver Gesamtbetrag / andere Leistung]
     Folge:                   [Urteil ohne Umsetzungsverfahren / Grundurteil + Endurteil + Sachwalter]

II.  Gleichartigkeit § 15 Abs. 1
     Nr. 1 gemeinsamer Sachverhalt:        <Darlegung>
     Nr. 2 gleiche Tatsachen-/Rechtsfragen: <Darlegung>
     Individualisierungseinwände:          <Kenntnis / Kausalität / Tarifgenerationen / Verjährung>
     Gruppenbildung:                       <Gruppe 1 … n mit je eigener Methode>
     Ergebnis:                             [gleichartig / nicht gleichartig]

III. Angaben nach § 15 Abs. 2
     Einheitliche Anspruchshöhe: <Betrag / nein>
     Berechnungsmethode:         <Formel und Datenquelle>

IV.  Abhilfegrundurteil § 16 Abs. 2
     Anspruchsvoraussetzungen (Nr. 1):     <Formulierungsvorschlag>
     Berechtigungsnachweise (Nr. 2):       <konkret, praktikabel>
     Betrag je Verbraucher / Methode:      <…>

V.   Vergleich § 17
     Vergleichsfenster nach Grundurteil:   <Bewertung, Austrittsrisiko §§ 9, 10>

VI.  Abhilfeendurteil § 18
     Umsetzungsverfahren angeordnet:       [ja]
     Vorläufige Kosten (Nr. 2):            <Betrag>
     Kollektiver Gesamtbetrag (Abs. 2):    <Betrag>
     Widerspruchsfrist verlängert (Abs. 3):[ja auf <…> / nein]
     Revision Abs. 4:                      zulassungsfrei — Frist bis <Datum>

VII. Kollektiver Gesamtbetrag §§ 19, 21
     Schätzgrundlage (§ 287 ZPO):          <…>
     Erhöhungsrisiko § 21:                 <keine Haftungsobergrenze>

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Gleichartigkeit behauptet statt dargelegt.** § 15 Abs. 1 VDuG verlangt beide Merkmale kumulativ; die Antwort auf die Individualisierungsrüge ist Gruppenbildung, nicht Pauschalierung.
- **Berechnungsmethode erst im Umsetzungsverfahren entwickelt.** Sie gehört nach § 15 Abs. 2 in die Klageschrift und nach § 16 Abs. 2 in die Urteilsformel.
- **Berechtigungsnachweise unpraktikabel formuliert.** Sie binden jeden einzelnen Verbraucher im Umsetzungsverfahren; unerfüllbare Nachweise entwerten den Titel.
- **Revision für zulassungsbedürftig gehalten.** § 18 Abs. 4 VDuG gewährt sie **ohne Zulassung**.
- **Kollektiven Gesamtbetrag als Haftungsobergrenze behandelt.** § 21 VDuG erlaubt die Erhöhung.
- **§ 287 ZPO übersehen.** Nach § 19 Abs. 2 VDuG ist die Schätzung ausdrücklich eröffnet; wer keine Schätzgrundlage liefert, überlässt sie dem Gericht.
- **Antragsvariante ohne Blick auf das Umsetzungsverfahren gewählt.** Nur die Leistung an namentlich benannte Verbraucher vermeidet Sachwalter und Fonds.
- **Vergleichsfenster nach dem Grundurteil verstreichen lassen** (§ 17 VDuG).
- **Rechtsprechung erfunden.** Das VDuG ist jung; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
