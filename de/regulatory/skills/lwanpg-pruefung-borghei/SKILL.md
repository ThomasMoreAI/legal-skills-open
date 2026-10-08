---
name: lwanpg-pruefung-borghei
title: /agrarrecht:lwanpg-pruefung
description: Prüfung und Durchsetzung von Auseinandersetzungsansprüchen ehemaliger LPG-Mitglieder bzw. ihrer Erben gegen die LPG-Nachfolgegesellschaft nach §§ 44 ff. LwAnpG vor dem Landwirtschaftsgericht – Anspruchsgrundlagen, Ermittlung des Auseinandersetzungsguthabens, Verjährung § 51a LwAnpG, Klagebefugnis, Verfahren nach LwVG/FamFG. Use when ein Mandant (Mitglied oder Erbe) Ansprüche gegen die LPG-Nachfolgegesellschaft (e.G., GmbH, GbR) geltend macht, ein Bescheid der Nachfolgegesellschaft angefochten werden soll oder die Verjährung zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/agrarrecht/skills/lwanpg-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /agrarrecht:lwanpg-pruefung

## Zweck

Der Skill prüft Ansprüche ehemaliger LPG-Mitglieder bzw. ihrer Erben auf **Vermögensauseinandersetzung** nach den §§ 44 ff. des Landwirtschaftsanpassungsgesetzes (LwAnpG) gegen die Nachfolgegesellschaft (eingetragene Genossenschaft, GmbH, GbR oder Liquidatoren). Er adressiert die Ermittlung des Auseinandersetzungsguthabens, den **Auskunftsanspruch** nach § 49 LwAnpG, die **Verjährung** nach § 51a LwAnpG sowie das Verfahren vor dem **Landwirtschaftsgericht** (§ 9 LwVG i.V.m. FamFG). Praxisrelevant insbesondere in den ostdeutschen Bundesländern auch noch mehr als drei Jahrzehnte nach der Wiedervereinigung.

## Eingaben

- Identität des Anspruchsberechtigten (ehem. LPG-Mitglied, Erbe, Gesamtrechtsnachfolger) — Namensangaben als `[Mandant]` / `[Erblasser]` redigieren
- Identität der Nachfolgegesellschaft (e.G., GmbH, GbR, ggf. Liquidator)
- Datum des Ausscheidens des Mitglieds bzw. Stichtag der LPG-Umwandlung (§§ 23 ff. LwAnpG)
- Bisherige Zahlungen / Bescheide / Auskünfte der Nachfolgegesellschaft
- Beweismittel (LPG-Aufnahmevertrag, Inventarbeiträge, Tilgungspläne, Abschlussbilanz LPG)
- Bundesland (Sachsen, Sachsen-Anhalt, Thüringen, Brandenburg, Mecklenburg-Vorpommern, Berlin-Ost)

## Sub-Agent-Architektur

Researcher liefert die LwAnpG-Vorschriften (§§ 27 ff., 44 ff., 49, 51a, 64), das LwVG mit FamFG-Verweisung, BGH-Landwirtschaftssenat-Beschlüsse zur Auseinandersetzungshöhe und Verjährung sowie Schweizer/Düsing-Martinez-Kommentarstellen. Drafter erstellt im Urteilsstil eine Antragsschrift an das Landwirtschaftsgericht oder im Gutachtenstil ein Memo zur Verjährungslage. Reviewer prüft die Klagebefugnis, die Verjährung, die Zuständigkeit Landwirtschaftsgericht und die Beweislastverteilung.

## Ablauf

### 1. Anspruchsgrundlage

Zentrale Anspruchsgrundlage ist § 44 LwAnpG (Wertermittlung und Auseinandersetzungsguthaben des ausgeschiedenen Mitglieds). Ergänzend:

- **§ 28 LwAnpG** — Wahl der Rechtsform durch die LPG, Wirkungen der Umwandlung
- **§§ 36 ff. LwAnpG** — Auseinandersetzung bei Umwandlung in andere Rechtsform
- **§ 44 LwAnpG** — Auseinandersetzungsguthaben (Inventarbeitrag, Bodenanteil, Fonds-Anteil)
- **§ 44 Abs. 6 LwAnpG** — Ermittlung des Eigenkapitals iSd Abs. 1 auf Grundlage der nach Beendigung der Mitgliedschaft aufzustellenden ordentlichen Bilanz ([buzer.de](https://www.buzer.de/s1.htm?a=44&g=LwAnpG&dorg=1)). **Keine** Ratenzahlungs- oder Verzinsungsregelung — die Ratenzahlung steht in § 51a, die Fälligkeit in § 49.
- **§ 49 LwAnpG** — Auskunftsanspruch gegen die Nachfolgegesellschaft
- **§ 51a LwAnpG** — Ansprüche der **vor dem 16.03.1990** ausgeschiedenen Mitglieder und ihrer Erben; Auszahlung in **fünf gleichen Jahresraten**, Berechnung nach § 44 mit der Geltendmachung statt der Beendigung der Mitgliedschaft als Stichtag ([buzer.de](https://www.buzer.de/s1.htm?a=51a&g=LwAnpG&dorg=1)). **Keine Verjährungsvorschrift.**
- **§ 3b LwAnpG** — Verjährung: **zehn Jahre** für Ansprüche nach §§ 3a, 28 Abs. 2, 37 Abs. 2, 44 Abs. 1 sowie 51a Abs. 1 und 2; Beginn mit dem **Schluss des Jahres, in dem der Anspruch entstanden ist** ([buzer.de](https://www.buzer.de/s1.htm?a=3b&g=LwAnpG&dorg=1))

Bei Erben: § 1922 BGB iVm der jeweiligen LwAnpG-Vorschrift; Klagebefugnis ist gesondert zu prüfen.

### 2. Ermittlung des Auseinandersetzungsguthabens

Das Auseinandersetzungsguthaben setzt sich nach § 44 LwAnpG idR aus folgenden Bestandteilen zusammen:

1. **Inventarbeitrag** des Mitglieds (Sacheinlage bei Aufnahme, idR Tier- und Maschinenbeiträge)
2. **Bodenanteil** (eingebrachte oder zur Nutzung übernommene landwirtschaftliche Nutzfläche)
3. **Anteil am Fonds** der LPG zum Zeitpunkt des Ausscheidens (Wertermittlung anhand der LPG-Abschlussbilanz bzw. Übergangsbilanz)
4. abzüglich bereits geleisteter Zahlungen der Nachfolgegesellschaft

Maßstab für die Wertermittlung: Schweizer, LwAnpG-Kommentar, § 44 LwAnpG `[unverifiziert]`; BGH-Landwirtschaftssenat-Linie zur Bewertung der Übergangsbilanz und zu Verkehrswert vs. Bilanzwert `[unverifiziert – prüfen in juris]`.

### 3. Auskunftsanspruch § 49 LwAnpG

Das ausgeschiedene Mitglied (bzw. der Erbe) kann nach § 49 LwAnpG Auskunft über die Berechnungsgrundlagen verlangen, insbesondere Einsicht in die Übergangsbilanz und die LPG-Mitgliederliste. Praxisrelevant als **Stufenklage** (§ 254 ZPO entsprechend; vor dem Landwirtschaftsgericht über FamFG-Vorschriften), wenn die Nachfolgegesellschaft die Auskunft verweigert.

### 4. Verjährung § 3b LwAnpG

Die Sonderregel zur Verjährung steht in **§ 3b LwAnpG**, nicht in § 51a: Ansprüche nach §§ 3a, 28 Abs. 2, 37 Abs. 2, **44 Abs. 1** sowie 51a Abs. 1 und 2 verjähren in **zehn Jahren**; die Verjährung beginnt mit dem **Schluss des Jahres, in dem der Anspruch entstanden ist** ([buzer.de](https://www.buzer.de/s1.htm?a=3b&g=LwAnpG&dorg=1)). Die regelmäßige Verjährung des § 195 BGB greift nicht. Wegen der jahrzehntelangen Bearbeitungspraxis ist die individuelle Anknüpfung (Bescheidzustellung, Auskunftserteilung, Verhandlungsende § 203 BGB analog) sorgfältig zu prüfen.

### 5. Klagebefugnis und Aktivlegitimation

- **Mitglied**: Anspruchsberechtigt mit Ausscheiden aus der LPG (§ 44 LwAnpG).
- **Erbe**: Gesamtrechtsnachfolger nach § 1922 BGB. Bei Erbengemeinschaft Streitgenossenschaft (§ 62 ZPO bzw. FamFG-Pendant) — alle Erben müssen Antragsteller sein, sofern kein Teilungsbescheid vorliegt.
- **Pfändungsgläubiger / Insolvenzverwalter**: nach Pfändung bzw. Insolvenzeröffnung.

Passivlegitimiert ist die **Nachfolgegesellschaft** in der jeweiligen Rechtsform (e.G. / GmbH / GbR); im Liquidationsstadium der Liquidator. Bei zwischenzeitlicher Verschmelzung der Nachfolgegesellschaft: § 20 UmwG (Rechtsnachfolge).

### 6. Verfahren vor dem Landwirtschaftsgericht

Zuständigkeit: **Landwirtschaftsgericht beim Amtsgericht** (§ 1 i.V.m. § 9 LwVG); das Verfahren richtet sich nach dem FamFG (§ 1 LwVG iVm dem 8. Buch FamFG `[unverifiziert]`). Statt Klageschrift: **Antrag** mit bestimmter Forderung, Sachverhalt, Begründung und Beweismitteln. Beschwerde gegen den Beschluss des LwG zum **OLG-Landwirtschaftssenat** nach §§ 22 ff. GrdstVG iVm § 9 LwVG `[unverifiziert]`.

### 7. Vergleichsoptionen

Wegen der Beweislage (Übergangsbilanzen häufig schwer rekonstruierbar) ist eine Mediation oder ein Vergleich nach § 779 BGB praktisch oft sinnvoll. Eine Kapitalisierung des Auseinandersetzungsguthabens mit Verzinsung über 30+ Jahre ist regelmäßig streitanfällig.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [LwAnpG](https://www.gesetze-im-internet.de/lwanpg/) (insb. §§ 27 ff., 44 ff., 49, 51a, 64)
- [LwVG](https://www.gesetze-im-internet.de/lwvg/) (gerichtliches Verfahren in Landwirtschaftssachen)
- [FamFG](https://www.gesetze-im-internet.de/famfg/) (Verfahrensordnung)
- [§ 1922 BGB](https://www.gesetze-im-internet.de/bgb/__1922.html) (Erbfolge)
- [§ 254 ZPO](https://www.gesetze-im-internet.de/zpo/__254.html) (Stufenklage; entsprechend im LwG-Verfahren)
- [§ 20 UmwG](https://www.gesetze-im-internet.de/umwg_1995/__20.html) (Rechtsnachfolge bei Verschmelzung)

### Kommentare

- Schweizer, LwAnpG-Kommentar (zuletzt Stand `[unverifiziert]`)
- Schmidt-Räntsch, in: Düsing/Martinez, Agrarrecht, LwAnpG-Teil `[unverifiziert]`
- Bayer/Lange, LwAnpG (sofern aktuelle Auflage vorhanden) `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/openjur]`)

Hier stehen **keine konkreten Aktenzeichen**, weil der Verifikationsdurchlauf keine namentlich belegte BLw-Entscheidung zu diesen drei Punkten aus einer öffentlichen Primärquelle bestätigen konnte. Die Linien sind als Suchauftrag zu lesen, nicht als Zitat:

1. BGH-Landwirtschaftssenat (BLw-Senat) zur Ermittlung des Auseinandersetzungsguthabens und zur Übergangsbilanzbewertung — Standardlinie seit den 1990er-Jahren. `[unverifiziert – Az. in juris/openjur ermitteln]`
2. BGH-BLw zur Verjährung nach **§ 3b LwAnpG** (nicht § 51a) und zur Hemmung durch Verhandlungen. `[unverifiziert – Az. in juris/openjur ermitteln]`
3. OLG-Landwirtschaftssenate (insb. Dresden, Naumburg, Rostock, Jena) zur Stufenklage und zum Auskunftsanspruch § 49 LwAnpG. `[unverifiziert – Az. in juris/openjur ermitteln]`

## Ausgabeformat (Antragsschrift Landwirtschaftsgericht)

```
An das Amtsgericht — Landwirtschaftsgericht — <Ort>

In der Landwirtschaftssache

  [Antragsteller], <Anschrift>,
    – Antragsteller –
  Verfahrensbevollmächtigter: <Kanzlei>

  gegen

  [Nachfolgegesellschaft] e.G. / GmbH i.L., <Anschrift>,
    – Antragsgegnerin –

wegen Auseinandersetzungsguthaben nach §§ 44 ff. LwAnpG

beantragen wir,

  1. die Antragsgegnerin zu verpflichten, dem Antragsteller Auskunft
     über die Berechnungsgrundlagen seines Auseinandersetzungs-
     guthabens nach § 49 LwAnpG zu erteilen, insbesondere durch
     Vorlage der Übergangsbilanz zum <Stichtag>;

  2. die Antragsgegnerin zu verpflichten, an den Antragsteller den
     sich aus der Auskunft ergebenden Betrag zu zahlen, mindestens
     jedoch <Mindestbetrag> EUR nebst Zinsen.

Begründung

  I. Sachverhalt
     1. Mitgliedschaft Erblasser/Antragsteller
     2. Ausscheiden / Tod / Erbfolge
     3. Bisherige Zahlungen / Auskünfte

  II. Anspruchsgrundlage
      § 44 LwAnpG; § 49 LwAnpG; § 1922 BGB

  III. Anspruchshöhe (Stufe 1: Auskunft; Stufe 2: Zahlung)

  IV. Verjährung
      § 51a LwAnpG; ggf. Hemmung § 203 BGB

  V. Zuständigkeit
     § 1, § 9 LwVG i.V.m. FamFG

Beweismittel:
  – LPG-Aufnahmevertrag vom <Datum>, Anlage K1
  – Übergangsbilanz <Stichtag>, soweit vorhanden, Anlage K2
  – ...

[Kostenhinweis nach RVG / Honorarvereinbarung – nur im Mandantenbrief]
```

## Beispiel (Auszug Gutachten zur Verjährung)

> **IV. Verjährung, § 3b LwAnpG.** Der Auseinandersetzungsanspruch des Mandanten (§ 44 Abs. 1 LwAnpG) unterliegt nicht der regelmäßigen Verjährung des § 195 BGB, sondern der Sonderregelung des § 3b LwAnpG: zehn Jahre, beginnend mit dem Schluss des Jahres, in dem der Anspruch entstanden ist. Anknüpfungspunkt ist nach der Linie des BGH-Landwirtschaftssenats `[unverifiziert]` nicht das Ausscheiden des Mitglieds, sondern die Fälligkeit des Auseinandersetzungsguthabens nach Feststellung der Übergangsbilanz. Da die Antragsgegnerin bis heute keine prüffähige Auskunft nach § 49 LwAnpG erteilt hat, ist die Verjährung in Bezug auf den Hauptanspruch noch nicht eingetreten; jedenfalls war sie durch Verhandlungen (§ 203 BGB analog) gehemmt, solange die Antragsgegnerin Zahlungs- und Auskunftsbereitschaft signalisierte. **Empfehlung:** Verjährungseinrede vorsorglich antizipieren und in der Antragsschrift adressieren.

## Risiken / typische Fehler

- **Zivilkammer statt Landwirtschaftsgericht** angerufen — Verweisung kostet Zeit und Gebühren.
- **Erbengemeinschaft nicht vollständig** als Antragsteller aufgeführt — fehlende Aktivlegitimation.
- **Stufenklage nicht genutzt**, obwohl die Auskunft nach § 49 LwAnpG offen ist — vermeidbare Beweisnot.
- **Verjährungseinrede nicht antizipiert**, obwohl § 51a LwAnpG eine eigenständige Verjährungsregelung enthält.
- **Bewertung Übergangsbilanz** ohne Sachverständigengutachten (§ 30 FamFG / § 144 ZPO entsprechend) angreifbar.
- **Verschmelzung der Nachfolgegesellschaft übersehen** — Passivlegitimation falsch (§ 20 UmwG).
- **Konkrete EUR-Beträge** der Auseinandersetzung sind einzelfallabhängig — keine Pauschalformeln ohne Bilanzgrundlage.
