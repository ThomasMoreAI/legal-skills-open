---
name: vergleich-abfindung-borghei
title: /vertragsrecht:vergleich-abfindung
description: Gestaltung und Prüfung von Vergleichen und Abfindungsvereinbarungen – Vergleich § 779 BGB mit gegenseitigem Nachgeben und Unwirksamkeit bei Sachverhaltsirrtum, Erledigungs- und Abgeltungsklausel, Erlassvertrag § 397 BGB, Widerrufsvorbehalt, Prozessvergleich als Vollstreckungstitel § 794 Abs. 1 Nr. 1 ZPO und Anwaltsvergleich § 796a ZPO. Use when ein Rechtsstreit oder eine streitige Forderung durch Vergleich beendet werden soll und der Umfang der Abgeltung, die Vollstreckbarkeit und die Widerrufsmöglichkeit zu regeln sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/vergleich-abfindung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:vergleich-abfindung

## Zweck

Ein Vergleich ist nur so gut wie seine **Abgeltungsklausel** und seine **Vollstreckbarkeit**. Zu eng formuliert, lässt er Nachforderungen zu; zu weit formuliert, erledigt er unbeabsichtigt Ansprüche, an die niemand gedacht hat. Dieser Skill prüft die Vergleichsvoraussetzungen des [§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html), gestaltet die Erledigungsklausel im gewollten Umfang und wählt die richtige Titelform.

## Eingaben

- Streitgegenstand: Ansprüche, Beträge, Rechtsgründe, Streitstand (außergerichtlich, rechtshängig, Instanz)
- Verhandlungsergebnis: Zahlungsbetrag, Fälligkeit, Ratenzahlung, Gegenleistungen (Rückgabe, Unterlassung, Zeugnis)
- Gewollter Abgeltungsumfang: nur der Streitgegenstand, alle Ansprüche aus dem Rechtsverhältnis, alle wechselseitigen Ansprüche überhaupt
- Bekannte, aber ausdrücklich auszunehmende Ansprüche (Betriebsrente, gewerbliche Schutzrechte, Ansprüche Dritter)
- Bedürfnis nach Vollstreckungstitel und Widerrufsmöglichkeit (Gremienvorbehalt, Aufsichtsrat, Versicherer)
- Kostenregelung; steuerliche Behandlung und Umsatzsteuer

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 779, 397 BGB, §§ 794, 796a, 98 ZPO mit URL und Kommentarstellen zur Auslegung von Abgeltungsklauseln.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Vergleichsvoraussetzungen → Abgeltungsumfang → Titelform → Widerruf und entwirft den Vergleichstext.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Bestimmtheit des Vollstreckungsinhalts, Reichweite der Abgeltungsklausel gegen die Mandanteninteressen, Widerrufsfrist und Kostenregelung.

## Ablauf

### 1. Vergleichsvoraussetzungen ([§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html))

Ein Vergleich ist ein Vertrag, durch den der Streit oder die Ungewissheit der Parteien über ein Rechtsverhältnis im Wege **gegenseitigen Nachgebens** beseitigt wird. Dem Streit steht die **Ungewissheit über die Verwirklichung eines Anspruchs** gleich (§ 779 Abs. 2 BGB).

- **Gegenseitiges Nachgeben** ist konstitutiv: Gibt nur eine Seite nach, liegt kein Vergleich, sondern ein **Erlassvertrag** ([§ 397 BGB](https://www.gesetze-im-internet.de/bgb/__397.html)), ein Anerkenntnis oder ein Schuldversprechen vor. Das Nachgeben kann geringfügig sein (Ratenzahlung, Kostenverzicht), muss aber beiderseits vorliegen.
- **Unwirksamkeit bei Sachverhaltsirrtum (§ 779 Abs. 1 BGB):** Der Vergleich ist unwirksam, wenn der nach dem Inhalt des Vertrags als feststehend zugrunde gelegte Sachverhalt **der Wirklichkeit nicht entspricht** und der Streit oder die Ungewissheit bei Kenntnis der Sachlage **nicht entstanden sein würde**. Betroffen ist nur die gemeinsam als sicher vorausgesetzte Grundlage, nicht der streitig gebliebene Punkt — gerade dessen Ungewissheit ist ja Vergleichsgegenstand.
- **Form:** grundsätzlich formfrei; formbedürftig, wenn der Vergleichsinhalt eine formbedürftige Verpflichtung begründet (§ 311b BGB Grundstück, § 766 BGB Bürgschaft). Ein **Prozessvergleich** wahrt jede Form (§ 127a BGB).

### 2. Abgeltungs- und Erledigungsklausel

Die Abgeltungsklausel ist der wirtschaftlich wichtigste Satz jedes Vergleichs. Ihre Reichweite ist reine **Auslegungsfrage** — deshalb muss sie den gewollten Umfang ausdrücklich benennen. Drei Stufen:

**Stufe 1 — enge Erledigungsklausel (nur der Streitgegenstand):**

> „Mit Erfüllung dieser Vereinbarung sind sämtliche Ansprüche der Parteien **aus dem Vertrag vom [Datum]** erledigt."

**Stufe 2 — umfassende Abgeltungsklausel (gesamtes Rechtsverhältnis):**

> „Mit der Erfüllung dieser Vereinbarung sind sämtliche wechselseitigen Ansprüche der Parteien aus und im Zusammenhang mit [Rechtsverhältnis], gleich aus welchem Rechtsgrund, **bekannt oder unbekannt**, erledigt und abgegolten. Dies gilt auch für Ansprüche gegen verbundene Unternehmen sowie gegen Organmitglieder, Mitarbeiter und Erfüllungsgehilfen der Parteien."

**Stufe 3 — Ausnahmen (praktisch immer erforderlich):**

> „Von dieser Abgeltungsklausel ausgenommen sind: (a) Ansprüche aus dieser Vereinbarung selbst, (b) Ansprüche wegen vorsätzlicher oder arglistiger Pflichtverletzung, (c) Ansprüche wegen Verletzung des Lebens, des Körpers oder der Gesundheit, (d) [konkret benannte Ansprüche, z. B. Anwartschaften aus der betrieblichen Altersversorgung, gewerbliche Schutzrechte, Freistellungsansprüche gegenüber Dritten]."

**Deklaratorisches vs. konstitutives Negatives Schuldanerkenntnis:** Eine umfassende Abgeltungsklausel wirkt in der Regel als **konstitutives negatives Schuldanerkenntnis** (§ 397 Abs. 2 BGB) — sie vernichtet auch Ansprüche, die keiner der Parteien bekannt waren. Wer das nicht will, muss die Klausel auf bekannte Ansprüche beschränken. **Der Mandant ist über diese Wirkung ausdrücklich zu belehren.**

Zu klären ist ferner, ob die Abgeltung **Erfüllungswirkung erst mit Zahlung** entfaltet („mit Erfüllung dieser Vereinbarung") oder sofort mit Abschluss — die erste Variante schützt den Gläubiger vor dem Zahlungsausfall.

### 3. Widerrufsvorbehalt

Ein Widerrufsvorbehalt gibt einer Partei Zeit für Gremienbeschlüsse, Versicherungsdeckung oder Mandantenrücksprache. Er muss vier Punkte regeln: **Berechtigten, Frist, Form und Adressaten**.

> „Diese Vereinbarung kann von der [Partei] **bis zum [Datum], eingehend, schriftlich gegenüber [Gericht / Gegenseite / Prozessbevollmächtigte]** widerrufen werden. Wird der Widerruf fristgerecht erklärt, entfällt die Vereinbarung insgesamt; die Parteien stehen sodann, als wäre sie nicht geschlossen worden."

- Beim **Prozessvergleich** ist der Widerruf gegenüber dem **Gericht** zu erklären; die Frist muss so bemessen sein, dass der Widerruf bei Gericht **eingeht** — das Absenden genügt nicht.
- Wird nicht widerrufen, wird der Vergleich mit Fristablauf endgültig wirksam. **Eine Fristverlängerung setzt das Einverständnis beider Seiten voraus.**
- **Kein Verbraucherwiderrufsrecht:** Der Widerrufsvorbehalt im Vergleich ist rein vertraglich; er hat mit §§ 355 ff. BGB nichts zu tun.

### 4. Prozessvergleich ([§ 794 Abs. 1 Nr. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html))

Die Zwangsvollstreckung findet statt aus **Vergleichen, die zwischen den Parteien zur Beilegung des Rechtsstreits seinem ganzen Umfang nach oder in Betreff eines Teiles des Streitgegenstands vor einem deutschen Gericht abgeschlossen sind**. Der Prozessvergleich hat eine **Doppelnatur**: Er ist zugleich Prozesshandlung (beendet den Rechtsstreit) und materiell-rechtlicher Vertrag (§ 779 BGB).

Folgen der Doppelnatur:

- Ist der Vergleich **materiell unwirksam** (§ 779 Abs. 1 BGB, Anfechtung), entfällt auch die prozessbeendende Wirkung; der **alte Rechtsstreit lebt wieder auf** und ist auf Antrag fortzusetzen.
- Der Vergleich ist **Vollstreckungstitel** — er muss daher einen **bestimmten, vollstreckungsfähigen Inhalt** haben: bezifferter Betrag, konkretes Datum oder bestimmtes Ereignis für die Fälligkeit, bei Handlungspflichten eine konkret bezeichnete Handlung. „Die Beklagte zahlt einen angemessenen Betrag" ist kein Titel.
- Zur Vollstreckung bedarf es einer **vollstreckbaren Ausfertigung** (§ 795 iVm §§ 724 ff. ZPO).

**Alternativen für außergerichtliche Vergleiche:**

- **Anwaltsvergleich** ([§ 796a ZPO](https://www.gesetze-im-internet.de/zpo/__796a.html)): Ein von Rechtsanwälten im Namen der Parteien geschlossener Vergleich wird auf Antrag für vollstreckbar erklärt, wenn der Schuldner sich der sofortigen Zwangsvollstreckung unterworfen und der Vergleich bei einem Amtsgericht niedergelegt ist.
- **Notarielle Urkunde mit Unterwerfungserklärung** (§ 794 Abs. 1 Nr. 5 ZPO) — der Regelweg bei größeren Beträgen.
- **Vergleich vor einer Gütestelle** (§ 794 Abs. 1 Nr. 1 ZPO).

### 5. Zahlungsmodalitäten und Sicherung

- **Fälligkeit** taggenau bestimmen; bei Ratenzahlung eine **Verfallklausel** aufnehmen: „Gerät die Schuldnerin mit einer Rate ganz oder teilweise länger als [14] Tage in Rückstand, wird der gesamte noch offene Restbetrag sofort zur Zahlung fällig."
- **Erfüllungswirkung** an den Zahlungseingang knüpfen, nicht an die Absendung.
- **Sicherung** bei Ratenzahlung: Bürgschaft, Schuldanerkenntnis über den vollen streitigen Betrag mit Erlassvorbehalt bei vertragstreuem Verhalten (`/vertragsrecht:sicherheiten-gestaltung`).
- **Verjährung:** Der Vergleich begründet einen neuen Anspruch mit Regelverjährung nach §§ 195, 199 BGB; ein titulierter Anspruch verjährt in 30 Jahren (§ 197 Abs. 1 Nr. 3 BGB). Siehe `/vertragsrecht:verjaehrung-pruefung`.

### 6. Kosten und Steuern

- **Kostenregelung:** Ohne ausdrückliche Regelung gilt bei einem Prozessvergleich § 98 ZPO — die Kosten sind **gegeneinander aufgehoben** und die Gerichtskosten je zur Hälfte zu tragen. Weicht das vom Verhandlungsergebnis ab, ist ausdrücklich zu regeln: „Von den Kosten des Rechtsstreits und des Vergleichs trägt die Klägerin [X] %, die Beklagte [Y] %."
- **Einigungsgebühr:** Der Vergleich löst eine Einigungsgebühr nach VV 1000 ff. RVG aus; die Höhe hängt vom Gegenstandswert ab und kann mit dem deterministischen Gebührenrechner ermittelt werden, beim Prozessvergleich `python -m scripts.legal_calc.cli rvg --wert 10000 --posten verfahren termin einigung-anhaengig` (VV 1003, 1,0), beim außergerichtlichen Vergleich `python -m scripts.legal_calc.cli rvg --wert 10000 --posten geschaeft einigung` (VV 1000, 1,5) (siehe [`../../references/rechner.md`](../../references/rechner.md)). **Die maßgebliche Gebührentabelle ist gegen die aktuelle Anlage 2 zu § 13 RVG zu prüfen.**
- **Umsatzsteuer:** Ist die Zahlung Entgelt für eine Leistung, fällt Umsatzsteuer an; echter Schadensersatz ist nicht steuerbar. Im Vergleichstext ist stets zu regeln, ob der Betrag **brutto oder netto** gemeint ist.
- **Abfindungen im Arbeitsverhältnis** sind lohnsteuerpflichtig; die ermäßigte Besteuerung nach § 34 EStG ist gesondert zu prüfen (Detailprüfung: `/arbeitsrecht:aufhebungsvertrag`).

## Quellen

### Statute

- [§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html) (Vergleich), [§ 397 BGB](https://www.gesetze-im-internet.de/bgb/__397.html) (Erlass, negatives Schuldanerkenntnis)
- [§ 127a BGB](https://www.gesetze-im-internet.de/bgb/__127a.html) (gerichtlicher Vergleich wahrt die Form), [§ 311b BGB](https://www.gesetze-im-internet.de/bgb/__311b.html)
- [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html), [§ 795 ZPO](https://www.gesetze-im-internet.de/zpo/__795.html), [§ 796a ZPO](https://www.gesetze-im-internet.de/zpo/__796a.html), [§ 98 ZPO](https://www.gesetze-im-internet.de/zpo/__98.html)
- [§ 197 BGB](https://www.gesetze-im-internet.de/bgb/__197.html) (30-jährige Verjährung titulierter Ansprüche)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, § 779 Rn. 1 ff., § 397 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Habersack, in: MüKoBGB, 8. Aufl. 2020, § 779 Rn. 1 ff.
- Seiler, in: Thomas/Putzo, ZPO, 45. Aufl. 2024, § 794 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`

### Rechtsprechung

- BGH, Urt. v. 27.01.2016 – XII ZR 33/15 (Auslegung umfassender Abgeltungsklauseln) `[unverifiziert – prüfen]`
- BGH, Urt. v. 15.04.1964 – Ib ZR 201/62 (Doppelnatur des Prozessvergleichs, Wiederaufleben des Rechtsstreits) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen folgen aus dem Gesetzeswortlaut.

## Ausgabeformat

```
VERGLEICH / ABFINDUNG — <Streitgegenstand> — <Datum>

I.    Vergleichsvoraussetzungen (§ 779) [gegenseitiges Nachgeben ✅/❌ — sonst Erlass § 397]
        Sachverhaltsirrtum § 779 I:     [kein Anhaltspunkt / 🔴 Risiko: <…>]
II.   Wirtschaftlicher Inhalt          <Betrag, Fälligkeit, Raten, Gegenleistungen>
III.  Abgeltungsklausel                [eng / umfassend / mit Ausnahmen]
        Wirkung:                       [deklaratorisch / konstitutiv § 397 II]
        Ausgenommene Ansprüche:        <Liste>
IV.   Widerrufsvorbehalt               [Berechtigter, Frist bis <Datum>, Form, Adressat]
V.    Titelform                        [Prozessvergleich § 794 I Nr. 1 ZPO / Anwaltsvergleich § 796a
                                        / notarielle Urkunde § 794 I Nr. 5 / kein Titel]
        Vollstreckungsfähiger Inhalt:  [✅ bestimmt / 🔴 unbestimmt]
VI.   Sicherung / Verfallklausel       [✅ / ❌]
VII.  Kosten                           [§ 98 ZPO / abweichend: <Quote>]
        Einigungsgebühr VV 1000:       <Rechnerbeleg>
VIII. Steuern / Umsatzsteuer           [brutto / netto — Begründung]
IX.   Verjährung                       [§§ 195, 199 / § 197 I Nr. 3 bei Titel]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Abgeltungsklausel unbeabsichtigt zu weit** — eine Klausel „alle Ansprüche, bekannt oder unbekannt" vernichtet als konstitutives negatives Schuldanerkenntnis auch Ansprüche, an die niemand gedacht hat; Ausnahmen sind ausdrücklich zu benennen.
- **Vergleich ohne gegenseitiges Nachgeben** — dann liegt kein Vergleich nach § 779 BGB, sondern ein Erlass oder Anerkenntnis mit anderer Rechtsfolge und anderer Anfechtbarkeit vor.
- **Prozessvergleich ohne vollstreckungsfähigen Inhalt** — ein unbestimmter Betrag oder eine unbestimmte Handlungspflicht macht den Titel wertlos.
- **Widerrufsfrist auf Absendung statt Eingang bezogen** — der Widerruf muss innerhalb der Frist beim Gericht bzw. beim Adressaten **eingehen**.
- **Kostenregelung vergessen** — ohne ausdrückliche Regelung greift § 98 ZPO mit gegeneinander aufgehobenen Kosten, was oft nicht dem Verhandlungsergebnis entspricht.
- **Umsatzsteuer nicht geregelt** — im Zweifel wird ein vereinbarter Betrag als Bruttobetrag ausgelegt; bei steuerbaren Leistungen entsteht eine erhebliche Differenz.
