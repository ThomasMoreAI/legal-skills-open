---
name: opportunitaetseinstellung-borghei
title: /strafrecht:opportunitaetseinstellung
description: Prüfung der Opportunitätseinstellung im Ermittlungs- und Hauptverfahren – Einstellung wegen Geringfügigkeit § 153 StPO, Einstellung gegen Auflagen und Weisungen § 153a StPO, Teileinstellung §§ 154, 154a StPO; Zustimmungserfordernisse, Auflagenkatalog, Rechtsfolgen. Use when eine Einstellung des Verfahrens aus Opportunitätsgründen zu prüfen, anzuregen oder zu verhandeln ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/opportunitaetseinstellung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:opportunitaetseinstellung

## Zweck

Nicht jedes Verfahren muss mit Urteil oder Strafbefehl enden. Das Opportunitätsprinzip durchbricht den Legalitätsgrundsatz (§ 152 Abs. 2 StPO) und erlaubt bei geringer Schuld eine sanktionslose oder auflagengebundene Erledigung — **ohne Eintragung im Führungszeugnis, ohne Schuldspruch**. Dieser Skill prüft, welche der Einstellungsnormen einschlägig ist, welche **Zustimmungen** (Gericht, Staatsanwaltschaft, Beschuldigter) erforderlich sind, welche Auflagen verhandelbar sind und welche Rechtsfolgen — insbesondere der **beschränkte Strafklageverbrauch** — eintreten.

## Eingaben

- Verfahrensstand (Ermittlungsverfahren / nach Anklage / Hauptverhandlung)
- Tatvorwurf und Norm (Vergehen oder Verbrechen?)
- bisheriges Strafmaßrisiko, Vorstrafen
- bereits angebotene/erwartete Auflagen (Geldbetrag, TOA, gemeinnützige Arbeit)
- bei mehreren Taten: Gewicht der Einzeltaten zueinander
- Haltung von StA und Gericht (Signale bekannt?)

## Sub-Agent-Architektur

Die Bearbeitung verteilt sich auf drei gedankliche Rollen, die nacheinander durchlaufen werden. Ein Subsumtions-Agent ordnet den Sachverhalt der passenden Norm zu und prüft, ob ein Vergehen vorliegt und die Schuld als gering einzustufen ist. Ein Zustimmungs-Agent klärt für die gewählte Norm exakt, wer zustimmen muss — Gericht, Staatsanwaltschaft und/oder Beschuldigter — und ob in der jeweiligen Verfahrensphase überhaupt noch eine Einstellung möglich ist. Ein Auflagen- und Folgen-Agent kalkuliert einen angemessenen Auflagenkatalog, die Erfüllungsfrist und die Rechtsfolgen einschließlich des Umfangs des Strafklageverbrauchs. Die Rollen sind reine Prosa-Arbeitsschritte, keine getrennten technischen Prozesse.

## Ablauf

### 1. Normwahl

| Norm | Voraussetzung | Rechtsfolge |
|---|---|---|
| [§ 153 StPO](https://www.gesetze-im-internet.de/stpo/__153.html) | Vergehen, geringe Schuld, kein öffentliches Interesse | folgenlose Einstellung |
| [§ 153a StPO](https://www.gesetze-im-internet.de/stpo/__153a.html) | Vergehen, Schwere der Schuld steht nicht entgegen, öffentliches Interesse durch Auflage beseitigbar | Einstellung gegen Auflagen/Weisungen |
| [§ 154 StPO](https://www.gesetze-im-internet.de/stpo/__154.html) | Tat fällt neben anderer Strafe nicht beträchtlich ins Gewicht | Teileinstellung (ganze Tat) |
| [§ 154a StPO](https://www.gesetze-im-internet.de/stpo/__154a.html) | abtrennbarer Teil/Gesetzesverletzung fällt nicht beträchtlich ins Gewicht | Beschränkung der Verfolgung |

Verbrechen (§ 12 Abs. 1 StGB) sind von §§ 153, 153a StPO ausgeschlossen.

### 2. Zustimmungserfordernisse

- **§ 153 Abs. 1 StPO:** Im Ermittlungsverfahren Einstellung durch StA mit **Zustimmung des Gerichts**; bei Vergehen mit Mindeststrafe und geringen Folgen kann die Zustimmung entfallen. Nach Anklage: Einstellung durch das **Gericht mit Zustimmung von StA und Angeschuldigtem**.
- **§ 153a Abs. 1 StPO:** stets Zustimmung des **Gerichts** und des **Beschuldigten** (die Auflage ist freiwillig — niemand muss sich auf sie einlassen). Nach Anklage § 153a Abs. 2 StPO entsprechend durch das Gericht.
- **§§ 154, 154a StPO:** Einstellung/Beschränkung durch StA bzw. nach Anklage durch das Gericht **mit Zustimmung der StA**; eine Zustimmung des Beschuldigten ist nicht erforderlich.

### 3. Auflagen und Weisungen (§ 153a Abs. 1 S. 2 StPO)

Verhandelbarer Katalog, u. a.:

- Geldzahlung an gemeinnützige Einrichtung oder Staatskasse
- Schadenswiedergutmachung / Täter-Opfer-Ausgleich (§ 46a StGB)
- gemeinnützige Leistungen
- Unterhaltspflichten, Teilnahme an Aufbauseminar/Verkehrsunterricht
- Erfüllungsfrist: i. d. R. bis zu **sechs Monate**, einmalige Verlängerung um drei Monate möglich (§ 153a Abs. 1 S. 3, 4 StPO).

**Verteidigerziel:** Auflagenhöhe an wirtschaftlicher Leistungsfähigkeit ausrichten, Ratenzahlung vereinbaren, Geldauflage statt Schuldeingeständnis.

### 4. Rechtsfolgen

- **§ 153a StPO:** Nach Erfüllung der Auflagen **beschränkter Strafklageverbrauch** — die Tat kann nicht mehr als Vergehen verfolgt werden (§ 153a Abs. 1 S. 5 StPO), wohl aber als Verbrechen, wenn sich neue Umstände ergeben.
- **§ 153 StPO:** Einstellung ohne Auflage; bei gerichtlicher Einstellung nach Anklage tritt ebenfalls beschränkter Strafklageverbrauch ein.
- **§§ 154, 154a StPO:** vorläufige Erledigung; **Wiederaufnahme der Verfolgung** ist möglich (§ 154 Abs. 3–5, § 154a Abs. 3 StPO), kein endgültiger Strafklageverbrauch.
- Keine Eintragung im Bundeszentralregister, kein Schuldspruch — wichtig für Beamte, Ausländer, Berufsträger.

### 5. Strategische Bewertung

- Frühzeitig auf StA zugehen; § 153a StPO als „Verständigung light" anbieten.
- Bei mehreren Taten: §§ 154, 154a StPO nutzen, um Hauptvorwurf zu fokussieren und Nebenvorwürfe abzuräumen.
- Niemals Auflage akzeptieren, ohne Beweislage geprüft zu haben — eine schwache Beweislage rechtfertigt Freispruch statt Auflage.

## Quellen

### Statute

- [§ 153 StPO](https://www.gesetze-im-internet.de/stpo/__153.html), [§ 153a StPO](https://www.gesetze-im-internet.de/stpo/__153a.html), [§ 154 StPO](https://www.gesetze-im-internet.de/stpo/__154.html), [§ 154a StPO](https://www.gesetze-im-internet.de/stpo/__154a.html)
- § 152 Abs. 2 StPO (Legalitätsprinzip), § 12 StGB (Verbrechen/Vergehen), § 46a StGB (TOA)

### Kommentare

- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 153, § 153a Rn. 1 ff.
- Diemer, in: KK-StPO, 9. Aufl. 2023, § 153a Rn. 1 ff.
- Beulke, Strafprozessrecht, 15. Aufl. 2023, Rn. 334 ff.

### Rechtsprechung

- BVerfG, Beschl. v. 06.12.2021 – 2 BvR 860/21 (Reichweite § 153a) `[unverifiziert – prüfen]`
- BGH, Urt. v. 03.12.2013 – 1 StR 412/13 (Strafklageverbrauch § 153a) `[unverifiziert – prüfen]`

## Ausgabeformat

```
OPPORTUNITÄTSEINSTELLUNG — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Verfahrensstand            <Ermittlung / nach Anklage / HV>
II.   Normwahl                   [§ 153 / § 153a / § 154 / § 154a StPO]
      Vergehen?                   [✅ / ⚠️ Verbrechen → §§ 153/153a (–)]
      Schuld gering?              [✅ / ⚠️]
III.  Zustimmungen erforderlich
      Gericht:                    [ja / nein]
      Staatsanwaltschaft:         [ja / nein]
      Beschuldigter:              [ja / nein]
IV.   Auflagen (nur § 153a)
      Vorschlag:                  <Geldbetrag / TOA / …>
      Erfüllungsfrist:            <… Monate>
V.    Rechtsfolgen
      Strafklageverbrauch:        [beschränkt / keiner — Wiederaufnahme möglich]
      Registereintrag:            [keiner]

Empfehlung: <…>
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Auflage trotz schwacher Beweislage** — Mandant zahlt für ein Verfahren, das im Zweifel mit Freispruch geendet hätte.
- **Zustimmung übersehen** — Einstellung nach § 153a StPO ohne erforderliche gerichtliche Zustimmung ist unwirksam.
- **Strafklageverbrauch falsch eingeschätzt** — §§ 154, 154a StPO bewirken **keinen** endgültigen Verbrauch; Wiederaufnahme der Verfolgung bleibt möglich.
- **Verbrechen** fälschlich über § 153a StPO eingestellt — unzulässig.
- **Auflagenhöhe** ohne Blick auf wirtschaftliche Leistungsfähigkeit vereinbart → Erfüllung scheitert, Verfahren lebt wieder auf.
