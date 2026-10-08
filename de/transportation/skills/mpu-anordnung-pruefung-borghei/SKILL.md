---
name: mpu-anordnung-pruefung-borghei
title: /verkehrsrecht:mpu-anordnung-pruefung
description: Rechtmäßigkeitsprüfung einer MPU-Anordnung der Fahrerlaubnisbehörde – Trigger §§ 11, 13, 14 FeV (Alkohol ab 1,6 ‰; BTM; wiederholte Auffälligkeit), formelle und materielle Anforderungen, Schluss auf Nichteignung § 11 VIII FeV, Rechtsschutz Widerspruch/Klage § 74 VwGO und Eilantrag § 80 V VwGO. Use when ein Mandant eine MPU-Anordnung oder einen Entziehungsbescheid erhalten hat oder im Wiedererteilungsverfahren steht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verkehrsrecht/skills/mpu-anordnung-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
---

# /verkehrsrecht:mpu-anordnung-pruefung

## Zweck

Der Skill prüft, ob die Anordnung einer Medizinisch-Psychologischen Untersuchung (MPU) durch die Fahrerlaubnisbehörde nach §§ 11, 13, 14 FeV rechtmäßig ist, und entwirft Widerspruchs- bzw. Klagebegründung sowie Eilantrag nach § 80 V VwGO bei Sofortvollzug einer Fahrerlaubnisentziehung. Er klärt insbesondere die Triggerschwelle (Alkohol ab 1,6 ‰; ab 1,1 ‰ mit zusätzlichen Ausfallerscheinungen; BTM-Konsum) und die formellen Anforderungen an die Anordnung (Bestimmtheit, Anhörung, Frist).

## Eingaben

- Anlasstat (BAK, ggf. Drogenfund, wiederholte Verstöße, Punktestand)
- Strafrechtliche Vorgeschichte (§§ 315c, 316 StGB; § 69 StGB-Entziehung; Sperrfrist § 69a StGB)
- Anordnungsbescheid (Inhalt, Frist, Begründung, Sofortvollzug?)
- Position des Mandanten: Erstbetroffener / Wiedererteilung / Anhängiger Entziehungsbescheid

## Sub-Agent-Architektur

Researcher liefert FeV-Statute, StVG, VwGO, BVerwG- und OVG-Rechtsprechung zur MPU-Anordnung sowie Hentschel/König/Dauer-Belegstellen. Drafter prüft formelle und materielle Rechtmäßigkeit in Gutachtenstil und entwirft Widerspruch, Klage und ggf. Eilantrag. Reviewer prüft Klagefrist § 74 VwGO, Antragsfrist § 80 III VwGO, Hinweispflicht § 11 VIII FeV.

## Ablauf

### 1. Ermächtigungsgrundlage identifizieren

| Trigger | Norm | Charakter |
|---|---|---|
| BAK ≥ 1,6 ‰ (oder Atemalkohol ≥ 0,8 mg/l) | § 13 S. 1 Nr. 2 lit. c FeV | **gebunden** |
| Wiederholte Trunkenheitsfahrten | § 13 S. 1 Nr. 2 lit. b FeV | gebunden |
| Alkohol-Trunkenheit unter 1,6 ‰ mit zusätzlichen Tatsachen | § 13 S. 1 Nr. 2 lit. a FeV | Ermessen (Tatsachen erforderlich) |
| Cannabis-Mehrkonsum / harte Drogen | § 14 FeV | gebunden bzw. Ermessen je Variante |
| Sonstige Eignungszweifel | § 11 Abs. 3 FeV | Ermessen |

Die Reichweite der einzelnen Trigger ist im Detail verwaltungsgerichtlich entwickelt; BVerwG-Rspr. zu § 13 S. 1 Nr. 2 lit. a FeV verlangt **konkrete** Tatsachen, nicht bloße Vermutungen `[unverifiziert – prüfen in juris]`.

### 2. Formelle Rechtmäßigkeit

- Zuständigkeit (örtlich/sachlich) der Fahrerlaubnisbehörde.
- **Anhörung § 28 VwVfG** vor Erlass der Anordnung (im Anordnungsstadium häufig nicht zwingend, im Entziehungsstadium aber regelmäßig erforderlich).
- **Bestimmtheit § 37 VwVfG**: Fragestellung des Gutachtenauftrags muss klar formuliert sein (welche Eignungszweifel sind zu klären?).
- **Begründung § 39 VwVfG**.
- **Frist** zur Vorlage des Gutachtens angemessen (idR mind. 2–3 Monate, `[unverifiziert – konkret zu prüfen]`).
- **Hinweis nach § 11 Abs. 8 S. 2 FeV** auf die Folgen der Nichtbeibringung (Schluss auf Nichteignung). Fehlt der Hinweis, ist der Schluss auf Nichteignung später regelmäßig nicht zulässig.

### 3. Materielle Rechtmäßigkeit

- Liegen die tatbestandlichen Voraussetzungen des einschlägigen FeV-Trigers vor?
- Bei gebundenen Anordnungen: Tatsachenfeststellung der Behörde tragfähig (z. B. amtsärztliches Attest, BAK-Messung)?
- Bei Ermessensanordnungen: Ermessensausübung erkennbar und nicht ermessensfehlerhaft (§ 40 VwVfG)?
- **Verhältnismäßigkeit**: Ist die MPU das mildeste geeignete Mittel?

### 4. Folge bei Nichtbeibringung

Verweigert der Betroffene die MPU oder legt er das Gutachten nicht fristgerecht vor, **darf** die Behörde nach § 11 Abs. 8 S. 1 FeV auf die Nichteignung **schließen** — Voraussetzung: rechtmäßige Anordnung und ordnungsgemäßer Hinweis nach § 11 Abs. 8 S. 2 FeV. Das BVerwG verlangt, dass die Anordnung selbst rechtmäßig war (BVerwG-Linie, `[unverifiziert – prüfen in juris]`).

### 5. Rechtsschutz

- **Widerspruch** (soweit landesrechtlich vorgesehen, § 68 VwGO i. V. m. Landesrecht).
- **Klage** vor dem Verwaltungsgericht, § 42 II VwGO. **Frist § 74 VwGO: 1 Monat** ab Bekanntgabe.
- **Eilantrag § 80 V VwGO** bei Sofortvollzug der Fahrerlaubnisentziehung (§ 80 II Nr. 4 VwGO; Begründungsanforderungen § 80 III VwGO).
- **Beschwerde § 146 VwGO** gegen Eilbeschluss.

### 6. Wiedererteilung

Nach Ablauf der strafrechtlichen Sperrfrist (§ 69a StGB) bzw. nach Eintritt der Bestandskraft der Entziehung erfolgt Wiedererteilung auf Antrag (§ 20 FeV). Die Behörde darf hier erneut MPU verlangen, wenn die ursprünglichen Eignungszweifel fortbestehen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 11 FeV](https://www.gesetze-im-internet.de/fev_2010/__11.html) (Eignung; Abs. 8 Schluss auf Nichteignung)
- [§ 13 FeV](https://www.gesetze-im-internet.de/fev_2010/__13.html) (Alkohol)
- [§ 14 FeV](https://www.gesetze-im-internet.de/fev_2010/__14.html) (BTM/Medikamente)
- [§ 20 FeV](https://www.gesetze-im-internet.de/fev_2010/__20.html) (Wiedererteilung)
- [§ 46 FeV](https://www.gesetze-im-internet.de/fev_2010/__46.html) (Entziehung)
- [§ 3 StVG](https://www.gesetze-im-internet.de/stvg/__3.html) (Entziehung)
- [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html) (Anhörung)
- [§ 37 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__37.html) (Bestimmtheit)
- [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html) (Begründung)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html); [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html) (Klagefrist 1 Monat); [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html) (Sofortvollzug, eA)
- [§ 69 StGB](https://www.gesetze-im-internet.de/stgb/__69.html); [§ 69a StGB](https://www.gesetze-im-internet.de/stgb/__69a.html) (strafgerichtliche Entziehung, Sperrfrist)

### Kommentare

- Dauer, in: Hentschel/König/Dauer, Straßenverkehrsrecht, 47. Aufl. 2023, § 13 FeV Rn. 1 ff., § 11 FeV Rn. 40 ff. (Schluss auf Nichteignung)
- Jahnke, in: Burmann/Heß/Hühnermann/Jahnke, Straßenverkehrsrecht, 28. Aufl. 2024, § 11 FeV Rn. 1 ff.
- Schubert/Schneider/Eisenmenger/Stephan, Begutachtungsleitlinien zur Kraftfahreignung (BAST), Stand 2022 (Standardwerk für medizinische Bewertung — keine Rechtsquelle, aber Verwaltungsleitlinie).

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BVerwG, Urt. v. 17.11.2016 – 3 C 20/15 (Anforderungen an MPU-Anordnung nach Trunkenheitsfahrt)
2. BVerwG, Urt. v. 09.06.2005 – 3 C 25/04, BVerwGE 123, 357 (Schluss auf Nichteignung § 11 VIII FeV)
3. OVG NRW, Beschl. v. 29.07.2009 – 16 B 895/09 (Eilrechtsschutz Fahrerlaubnisentziehung)
4. BVerwG, Urt. v. 11.04.2019 – 3 C 14/17 (Cannabis-Mehrkonsum, § 14 FeV)

## Ausgabeformat

```
GUTACHTEN — Rechtmäßigkeit der MPU-Anordnung
Bescheid: <Behörde, Az., Datum>

I.   Sachverhalt
II.  Frage(n)
III. Kurzantwort
     – Anordnung rechtmäßig: [ja / nein / teilweise]
     – Empfohlene Strategie: [Beibringung / Widerspruch / Klage / Eilantrag]

IV.  Rechtliche Bewertung
     1. Ermächtigungsgrundlage
        a) § 13 / § 14 / § 11 III FeV
        b) Tatbestand erfüllt?
     2. Formelle Rechtmäßigkeit
        a) Zuständigkeit
        b) Anhörung § 28 VwVfG
        c) Bestimmtheit § 37 VwVfG (Gutachtenfragestellung)
        d) Frist
        e) Hinweis § 11 VIII S. 2 FeV
     3. Materielle Rechtmäßigkeit
        a) Tatbestandsvoraussetzungen
        b) Ermessen (soweit eröffnet)
        c) Verhältnismäßigkeit
     4. Folgen bei Nichtbeibringung (§ 11 VIII FeV)
     5. Rechtsschutz
        a) Widerspruch / Klage § 74 VwGO
        b) Eilrechtsschutz § 80 V VwGO bei Sofortvollzug

V.   Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VI.  Entwurf Widerspruchs-/Klagebegründung

VII. Fristenkalender
     – Klagefrist § 74 VwGO: <Datum>
     – Antragsfrist § 80 III VwGO: parallel zur Klage zu stellen

VIII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Kurzantwort.** Die MPU-Anordnung der Fahrerlaubnisbehörde vom <Datum> ist nach § 13 S. 1 Nr. 2 lit. c FeV dem Grunde nach gerechtfertigt, weil die festgestellte BAK von 1,7 ‰ den Schwellenwert von 1,6 ‰ überschreitet und § 13 S. 1 Nr. 2 lit. c FeV insoweit gebundene Behördenentscheidung ist. Formell bestehen jedoch erhebliche Zweifel an der Bestimmtheit der Fragestellung im Sinne von § 37 VwVfG.
>
> **IV.2.c) Bestimmtheit.** Die Behörde hat die Fragestellung des Gutachtens auf „die Klärung der Fahreignung" beschränkt, ohne die zu klärenden Eignungszweifel zu konkretisieren. Nach BVerwG-Linie (BVerwG, Urt. v. 17.11.2016 – 3 C 20/15 `[unverifiziert – prüfen]`) muss der Begutachtungsauftrag die konkreten tatsächlichen Anknüpfungstatsachen benennen, damit der Begutachtungsgegenstand für Betroffenen und Gutachter eindeutig ist. Daran fehlt es.

## Risiken / typische Fehler

- **Beibringungs-Frist verstreichen lassen** und damit Schluss auf Nichteignung nach § 11 VIII FeV provozieren — auch wenn die Anordnung angreifbar ist.
- **Klagefrist § 74 VwGO** (1 Monat) übersehen — bei Sofortvollzug Eilantrag § 80 V VwGO parallel.
- **Hinweis § 11 VIII S. 2 FeV** nicht in der Anordnung enthalten → Schluss auf Nichteignung unzulässig.
- **Verwechselung Anordnung und Entziehungsbescheid:** Die MPU-**Anordnung** selbst ist verwaltungsgerichtlich grds. nicht selbstständig anfechtbar, sondern erst die darauf gestützte Entziehung (st. Rspr., `[unverifiziert – prüfen]`).
- **Wiedererteilungsverfahren** mit Entziehungsverfahren verwechseln — anderer Prüfungsmaßstab (Wegfall der Eignungsmängel positiv darzulegen).
- **Behauptung „MPU ist schikanös"** ohne tatbestandsbezogene Subsumtion — kein zulässiges Argument.
