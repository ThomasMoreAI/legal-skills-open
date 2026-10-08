---
name: nachhaltigkeitsbericht-pruefung-borghei
title: /csrd:nachhaltigkeitsbericht-pruefung
description: Vorbereitung und Durchführung der externen Prüfung der Nachhaltigkeitsberichterstattung nach CSRD-RL (EU) 2022/2464 – Prüferbestellung, Prüfungsumfang (limited assurance), ESRS-Konformität und Verbindung zum Lagebericht (§ 289b HGB). Use when ein CSRD-pflichtiges Unternehmen die Prüfung seines Nachhaltigkeitsberichts beauftragt oder den Prüfungsumfang klären muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/csrd/skills/nachhaltigkeitsbericht-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /csrd:nachhaltigkeitsbericht-pruefung

## Zweck

Die CSRD führt erstmals eine **verpflichtende externe Prüfung** der Nachhaltigkeitsberichterstattung ein. Diese Skill klärt, **wer prüft, mit welchem Sicherheitsniveau und in welcher Tiefe**. Geprüft wird zunächst mit **limited assurance** (begrenzte Sicherheit); ein späterer Übergang zu reasonable assurance ist angelegt. Ein unzureichend vorbereiteter Bericht führt zu eingeschränkten Prüfungsvermerken — mit unmittelbarer Außenwirkung gegenüber Kapitalmarkt und Aufsicht.

> **⚠️ Aktualität (Stand 2026-07) — erst Prüfungspflicht klären, dann Prüfer beauftragen:** Das **Omnibus-I-Paket** ist abgeschlossen: Die **Änderungs-RL (EU) 2026/470** wurde am **26.02.2026** im Amtsblatt veröffentlicht und ist am **18.03.2026** in Kraft getreten; sie ersetzt die Stop-the-Clock-RL (EU) 2025/794. Umsetzungsfrist **19.03.2027**.
>
> - **Der Anwendungsbereich ist verengt:** berichts- und damit prüfungspflichtig sind nur noch Unternehmen mit **> 1.000 Beschäftigten UND > 450 Mio. EUR Nettoumsatz** (kumulativ). Die vom EP vorgeschlagene 1.750-Schwelle wurde **abgelehnt**. Die Wellen-Systematik (Wave 1/2/3) ist als Maßstab überholt.
> - **Wave-1-Rückfall:** Wer für das **Geschäftsjahr 2024** berichtet und geprüft hat, aber unter den neuen Schwellen liegt, ist für **GJ 2025 und GJ 2026 nicht berichts- und nicht prüfungspflichtig** (vorbehaltlich nationaler Umsetzung). Ein bereits erteilter Prüfungsauftrag ist daraufhin zu überprüfen und ggf. zu kündigen oder auf eine freiwillige Leistung umzustellen.
> - **Vorschaltfrage vor jeder Beauftragung:** Besteht nach neuem Recht überhaupt eine Prüfungspflicht? Siehe `/csrd:esrs-berichtspflicht`. Eine freiwillige Prüfung ist zulässig, aber ausdrücklich als solche zu bezeichnen — ein Vermerk, der eine gesetzliche Pflichtprüfung suggeriert, ist irreführend.
> - **Sicherheitsniveau:** Die Prüfung bleibt bei **limited assurance**; der ursprünglich angelegte Übergang zu reasonable assurance ist im Zuge der Vereinfachung nicht weiterverfolgt worden `[unverifiziert - prüfen]`.
> - **ESRS-Überarbeitung läuft noch** — Prüfungsgegenstand und Datenpunktumfang stehen nicht abschließend fest `[unverifiziert - prüfen]`.
> - **Deutschland:** Das **CSRD-Umsetzungsgesetz** ist weiterhin nicht in Kraft (Regierungsentwurf 03.09.2025, Anhörung im Rechtsausschuss 13.04.2026); **§ 324i HGB-E** ist Entwurfsrecht `[unverifiziert - prüfen]`.

## Eingaben

- Entwurf des Nachhaltigkeitsberichts (Lageberichtsabschnitt)
- Wesentlichkeitsanalyse mit Methodik und Schwellenwert-Begründung
- ESRS-Datenpunkte mit Datenherkunft und Kontrollen
- Bisheriger Abschlussprüfer / Prüfungsausschuss-Beschluss
- Vorjahres-Prüfungsvermerk (falls vorhanden)

## Sub-Agent-Architektur

Ein **Bestellungs-Agent** klärt die Prüferbestellung und Unabhängigkeit (Abschlussprüfer, anderer Wirtschaftsprüfer oder unabhängiger Erbringer von Bestätigungsleistungen). Ein **Scoping-Agent** legt den **Prüfungsumfang** fest: Prozess der Wesentlichkeitsanalyse, ESRS-Angaben, Digital-Tagging, Konformität mit den ESRS. Ein **Evidenz-Agent** prüft die **ESRS-Konformität** der einzelnen Datenpunkte gegen die zugrunde liegenden Nachweise und Kontrollen. Ein **Vermerks-Agent** formuliert den Prüfungsvermerk (limited assurance) und kennzeichnet jede ungeklärte Rechts- oder Datumsfrage mit `[unverifiziert - prüfen]`.

## Ablauf

### 0. Vorfrage: Besteht die Prüfungspflicht noch? (RL (EU) 2026/470)

- Schwellentest nach neuem Recht: **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz**, kumulativ, seit **18.03.2026**.
- Frühere Berichts- und Prüfungspraxis oder die Wellenzuordnung sind **kein** Nachweis fortbestehender Pflicht.
- **Wave-1-Rückfall** prüfen: Berichterstattung für GJ 2024 erfolgt, Schwellen nun nicht mehr erreicht → für **GJ 2025 und GJ 2026** keine Pflicht.
- Ergebnis: Pflichtprüfung / freiwillige Prüfung / keine Prüfung. Bestehende Prüfungsaufträge und Honorarvereinbarungen entsprechend anpassen.

### 1. Prüferbestellung und Unabhängigkeit

- Bestellung durch die Gesellschafter/Hauptversammlung; Vorbereitung durch den Prüfungsausschuss.
- Unabhängigkeit und Verbot bestimmter Nicht-Prüfungsleistungen beachten.
- Festlegung, ob der **Abschlussprüfer** zugleich die Nachhaltigkeitsprüfung übernimmt.

### 2. Prüfungsumfang (limited assurance)

Die Prüfung mit **limited assurance** umfasst:

- den **Prozess** der doppelten Wesentlichkeitsanalyse,
- die Einhaltung der **ESRS** bei den berichteten Angaben (**ESRS-Konformität**),
- die Vorgaben zum digitalen Auszeichnungsformat (Tagging),
- die Vollständigkeit gegenüber den taxonomiebezogenen Angaben (Art. 8 Taxonomie-VO).

Das Niveau **limited assurance** verlangt eine Aussage in negativer Formulierung („keine Hinweise auf wesentliche Falschdarstellungen"); **reasonable assurance** (positive Aussage) ist als Ausbaustufe angelegt.

### 3. ESRS-Konformität der Angaben

- Datenpunkte gegen **ESRS 1** (allgemeine Anforderungen) und ESRS 2 sowie die wesentlichen themenbezogenen Standards abgleichen.
- Datenherkunft, Schätzverfahren und interne Kontrollen prüfen.
- Konsistenz zwischen Nachhaltigkeits- und Finanzberichterstattung.

### 4. Verbindung zum Lagebericht (§ 289b HGB)

- Der Nachhaltigkeitsbericht ist Teil des **Lageberichts** (**§ 289b HGB**); die Prüfung knüpft an diese Verortung an.
- Abgrenzung zur Lageberichtsprüfung nach den allgemeinen Vorschriften.
- Befund: gesonderter Prüfungsvermerk zur Nachhaltigkeitsberichterstattung.

### 5. Berichterstattung über die Prüfung

- Prüfungsvermerk mit Einschränkungen/Hinweisen, Verweis auf das Sicherheitsniveau.
- Kommunikation an Prüfungsausschuss und Aufsichtsorgan.

## Risiken / typische Fehler

- **Niveau verwechselt** — **limited assurance** als reasonable assurance dargestellt; die Aussageform unterscheidet sich grundlegend.
- **ESRS-Konformität nur formal** — **ESRS-Konformität** auf Vollständigkeit der Überschriften reduziert, ohne Datennachweis und Kontrollen.
- **Wesentlichkeitsprozess nicht prüffähig** — Methodik und Schwellenwert nicht dokumentiert; führt zu Einschränkung.
- **Prüferzulassung offen** — Zulassung/Unabhängigkeit nicht abschließend geklärt; Stand `[unverifiziert - prüfen]`.
- **Mandant plant gegen aufgehobenes Recht** — Prüfungsumfang und Betroffenheit nach der alten Wellen-Systematik oder der Stop-the-Clock-RL (EU) 2025/794 bestimmt. Maßgeblich ist die **Änderungs-RL (EU) 2026/470** (in Kraft 18.03.2026).
- **Prüfung ohne Prüfungspflicht beauftragt** — die Schwellenprüfung (**> 1.000 Beschäftigte UND > 450 Mio. EUR**) wurde nicht neu durchgeführt; Honorar und Haftungsrisiko entstehen ohne gesetzliche Grundlage.
- **Wave-1-Rückfall übersehen** — für GJ 2024 geprüft, für **GJ 2025/2026** nicht mehr pflichtig; bestehender Auftrag nicht angepasst.
- **Freiwillige Prüfung nicht als solche gekennzeichnet** — ein Vermerk, der eine gesetzliche Pflichtprüfung suggeriert, ist gegenüber Kapitalmarkt und Adressaten irreführend.
- **Prüfungsgegenstand als final behandelt** — die **ESRS-Überarbeitung** läuft noch; Datenpunktumfang `[unverifiziert - prüfen]`.
- **Lageberichtsverortung ignoriert** — Verbindung nach § 289b HGB nicht hergestellt, Prüfungsvermerk falsch adressiert.

## Quellen

### EU-Rechtsakte

- [RL (EU) 2022/2464 (CSRD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464) — Prüfungspflicht (geänderte Bilanz-RL 2013/34/EU, Art. 34)
- [Delegierte VO (EU) 2023/2772 (ESRS Set 1)](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj) — **Überarbeitung läuft** `[unverifiziert - prüfen]`
- **Änderungs-RL (EU) 2026/470 (Omnibus I)** — Amtsblatt 26.02.2026, in Kraft 18.03.2026, Umsetzungsfrist 19.03.2027; ersetzt die Stop-the-Clock-RL (EU) 2025/794. ELI-Fundstelle `[unverifiziert - prüfen]`

### Deutsches Recht / Standards

- [§ 289b HGB](https://www.gesetze-im-internet.de/hgb/__289b.html) · § 324i HGB-E (CSRD-UmsG, im Verfahren) `[unverifiziert - prüfen]`
- IDW-Verlautbarungen zur Prüfung der Nachhaltigkeitsberichterstattung (aktuelle Fassung)

## Ausgabeformat

```
PRÜFUNG NACHHALTIGKEITSBERICHT — <Unternehmen> — <Geschäftsjahr>

0.    Prüfungspflicht (RL (EU) 2026/470, in Kraft 18.03.2026)
      Beschäftigte > 1.000?  [Ja/Nein]   Nettoumsatz > 450 Mio. EUR? [Ja/Nein]
      Kumulativ erfüllt: [Ja/Nein]  → Pflichtprüfung / freiwillig / keine
      Wave-1-Rückfall GJ 2025/2026: [Ja/Nein]
I.    Prüferbestellung
      Prüfer / Unabhängigkeit / Prüfungsausschuss: <…>
II.   Prüfungsumfang
      Sicherheitsniveau: limited assurance
      Gegenstand: Wesentlichkeitsprozess / ESRS-Angaben / Tagging / Taxonomie
III.  ESRS-Konformität
      Datenpunkt | Standard | Nachweis | Befund
IV.   Verbindung Lagebericht (§ 289b HGB)
      <…>
V.    Prüfungsvermerk
      Einschränkungen / Hinweise: <…>
VI.   Offene Punkte
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: jährlich
```
