---
name: ki-transparenzpflichten-borghei
title: /ki-vo-compliance:ki-transparenzpflichten
description: Prüfung der Transparenzpflichten nach Art. 50 KI-VO – Offenlegung der KI-Interaktion, Kennzeichnung synthetischer Inhalte und Deepfakes, Information bei Emotionserkennung und biometrischer Kategorisierung samt Bußgeldrisiko Art. 99 KI-VO. Use when ein Anbieter oder Betreiber eines KI-Systems prüfen muss, ob und wie er Nutzer über KI-Einsatz oder KI-generierte Inhalte informieren und kennzeichnen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-vo-compliance/skills/ki-transparenzpflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /ki-vo-compliance:ki-transparenzpflichten

## Zweck

**Art. 50 KI-VO** ([VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689)) auferlegt Anbietern und Betreibern bestimmter KI-Systeme **Transparenz- und Kennzeichnungspflichten**, um Täuschung, Desinformation und Manipulation im Informationsökosystem zu begrenzen. Die Pflichten gelten ab dem 2. August 2026 und treffen auch Systeme, die nicht hochrisiko-eingestuft sind. Dieser Skill ordnet einem System die einschlägige Transparenzpflicht zu und prüft die Art der Kennzeichnung.

> **⚠️ Aktualität (Stand 2026-07): Art. 50 gilt ab dem 02.08.2026 — die Pflichten sind NICHT verschoben.**
>
> Der **Digital Omnibus on AI** (Europäisches Parlament **16.06.2026**, Rat **29.06.2026**) hat die Transparenzpflichten des Art. 50 KI-VO **ausdrücklich von der Verschiebung ausgenommen**. Sie gelten unverändert **ab dem 02.08.2026**, wie ursprünglich vorgesehen.
>
> **Dies ist der in der Praxis am häufigsten übersehene Punkt der KI-VO.** Verschoben wurden allein die **Hochrisiko**-Pflichten — Anhang III auf den **02.12.2027**, Anhang I auf den **02.08.2028**. Diese Verschiebung wird in der Beratung verbreitet als pauschaler Aufschub der KI-VO gelesen. Sie ist es nicht: Art. 50 trifft Chatbots, Bildgeneratoren und Deepfake-Anwendungen **unabhängig von jeder Hochrisiko-Einstufung** und **unabhängig von jeder Verschiebung**.
>
> | Regelungsbereich | Geltung |
> |---|---|
> | Verbote Art. 5, KI-Kompetenz Art. 4 | 02.02.2025 (gilt) |
> | GPAI Art. 51–55 | 02.08.2025 (gilt) — nicht verschoben |
> | **Transparenz Art. 50** | **02.08.2026 — bleibt, nicht verschoben** |
> | Hochrisiko Anhang III (Art. 6 Abs. 2) | 02.12.2027 (verschoben) |
> | Hochrisiko Anhang I (Art. 6 Abs. 1) | 02.08.2028 (verschoben) |
> | Neue Verbote (NCII, CSAM) | 02.12.2026 |
>
> **Nationale Zuständigkeit in Deutschland:** Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit nach dem KI-MIG), **nicht** die Datenschutzaufsicht oder die/der BfDI. Das **KI-MIG** hat den Bundestag am **11.06.2026** und den Bundesrat am **10.07.2026** passiert, war zum **21.07.2026 aber noch nicht im BGBl. verkündet** — eine BGBl.-Fundstelle existiert daher nicht und darf nicht zitiert werden. `[unverifiziert - prüfen]`
>
> Amtsblatt-Fundstelle der Änderungsverordnung `[unverifiziert - prüfen]`.

## Eingaben

- Funktion des Systems (Interaktion mit Menschen, Inhaltserzeugung, Emotionserkennung)
- Rolle des Mandanten (Anbieter / Betreiber — Art. 3 KI-VO)
- Art der erzeugten Inhalte (Bild, Audio, Video, Text; synthetisch oder Deepfake)
- Einsatzkontext (Kundendialog, redaktioneller Inhalt, Kunst/Satire)
- Bereits vorhandene Kennzeichnung/Hinweise

## Sub-Agent-Architektur

Drei gedankliche Rollen teilen die Prüfung. Ein **Pflichten-Zuordner** ordnet die Funktion einer der vier Säulen des Art. 50 KI-VO zu (Interaktionsoffenlegung, Markierung synthetischer Inhalte, Emotionserkennung, Deepfake-Offenlegung) und bestimmt, ob Anbieter- oder Betreiberpflicht greift. Ein **Kennzeichnungs-Designer** legt fest, wie die Markierung technisch (maschinenlesbar) und gegenüber dem Menschen erfolgen muss und welche Ausnahmen gelten. Ein **Sanktions-Bewerter** beziffert das Bußgeldrisiko nach Art. 99 KI-VO. Der Pflichten-Zuordner übergibt jede bejahte Pflicht an den Kennzeichnungs-Designer.

## Ablauf

### 1. Offenlegung der KI-Interaktion (Art. 50 Abs. 1 KI-VO)

**Anbieter** müssen KI-Systeme, die für die **direkte Interaktion mit natürlichen Personen** bestimmt sind (z. B. Chatbots), so gestalten, dass die betroffene Person informiert ist, dass sie mit einem KI-System interagiert — es sei denn, dies ist aus den Umständen offensichtlich.

### 2. Kennzeichnung synthetischer Inhalte (Art. 50 Abs. 2 KI-VO)

**Anbieter** von Systemen, die synthetische **Bild-, Audio-, Video- oder Textinhalte** erzeugen oder manipulieren, müssen die Ausgabe in einem **maschinenlesbaren Format** markieren und als künstlich erzeugt/manipuliert erkennbar machen (z. B. Wasserzeichen, Metadaten).

### 3. Emotionserkennung und biometrische Kategorisierung (Art. 50 Abs. 3 KI-VO)

**Betreiber** von Emotionserkennungs- oder biometrischen Kategorisierungssystemen müssen die betroffenen Personen über den Betrieb informieren (Verzahnung mit DSGVO-Pflichten).

### 4. Deepfake-Offenlegung (Art. 50 Abs. 4 KI-VO)

**Betreiber**, die mit einem KI-System **Deepfakes** (Bild, Audio, Video) erzeugen oder manipulieren, müssen offenlegen, dass die Inhalte künstlich erzeugt/manipuliert wurden. Für offensichtlich künstlerische, kreative oder satirische Werke gilt eine **abgeschwächte** Offenlegung, die die Darstellung nicht beeinträchtigt. Auch bei KI-erzeugten/-bearbeiteten Texten zur Information der Öffentlichkeit über Angelegenheiten von öffentlichem Interesse besteht eine Offenlegungspflicht.

### 5. Form und Zeitpunkt

Informationen sind **klar und unterscheidbar spätestens zum Zeitpunkt der ersten Interaktion/Exposition** bereitzustellen, barrierefrei. Markierungen müssen wirksam, interoperabel, robust und so weit technisch möglich sein.

### 6. Sanktionen (Art. 99 KI-VO)

Verstöße gegen Transparenzpflichten nach Art. 50 KI-VO können mit Geldbußen bis **15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** geahndet werden.

## Risiken

- **Kennzeichnung vergessen** — synthetische Inhalte ohne maschinenlesbare Markierung verstoßen gegen Art. 50 Abs. 2 KI-VO.
- **Deepfake nicht offengelegt** — fehlende Offenlegung nach Art. 50 Abs. 4 KI-VO; die Kunst-/Satire-Ausnahme ist eng und befreit nicht vollständig.
- **Chatbot ohne Hinweis** — fehlende Offenlegung der KI-Interaktion nach Art. 50 Abs. 1 KI-VO.
- **Verschiebung der Hochrisiko-Pflichten als Entwarnung für Art. 50 missverstanden** — BLOCKER und der in der Praxis häufigste Fehler. Der Digital Omnibus on AI hat **nur** die Hochrisiko-Pflichten verschoben (Anhang III → 02.12.2027, Anhang I → 02.08.2028) und Art. 50 **ausdrücklich ausgenommen**. Die Transparenzpflichten gelten **ab 02.08.2026**. Mandanten, die aus der Schlagzeile „KI-VO verschoben" auf einen Aufschub schließen, laufen ohne Kennzeichnung in die Anwendbarkeit.
- **Art. 50 an die Hochrisiko-Einstufung gekoppelt** — die Transparenzpflichten greifen **unabhängig** von Art. 6 und Anhang III. Ein Chatbot oder Bildgenerator ohne Hochrisiko-Bezug ist voll erfasst; die Prüfung „nicht hochrisiko, also nichts zu tun" ist falsch.
- **Umsetzungsvorlauf unterschätzt** — Wasserzeichen, C2PA-/Metadaten-Pipelines, UI-Hinweise und redaktionelle Freigabeprozesse sind technische Projekte. Wer sie erst zum Stichtag beginnt, ist am 02.08.2026 nicht konform.
- **Nationale Zuständigkeit falsch adressiert** — Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit, KI-MIG), **nicht** die Datenschutzaufsicht oder die/der BfDI. Das KI-MIG war zum 21.07.2026 **noch nicht im BGBl. verkündet**; eine BGBl.-Fundstelle darf nicht angegeben werden. `[unverifiziert - prüfen]`
- **Bußgeldrisiko** — bis 15 Mio. EUR / 3 % nach Art. 99 KI-VO; ab dem 02.08.2026 durchsetzbar.

## Ausgabeformat

```
KI-TRANSPARENZPFLICHTEN — PRÜFUNG — <System> — <Datum>

I.   Funktion                                   [Interaktion / Inhaltserzeugung / Emotion]
II.  Rolle (Art. 3 KI-VO)                        [Anbieter / Betreiber]
III. Einschlägige Pflicht (Art. 50 KI-VO)
     Abs. 1 KI-Interaktion                       [betroffen? <…>]
     Abs. 2 synthetische Inhalte                 [betroffen? Markierung <…>]
     Abs. 3 Emotionserkennung                    [betroffen? <…>]
     Abs. 4 Deepfake                             [betroffen? Offenlegung <…>]
IV.  Form / Zeitpunkt der Kennzeichnung          [<…>]
V.   Ausnahme (Kunst/Satire/offensichtlich)      [greift? <…>]
VI.  Bußgeldrisiko (Art. 99 KI-VO)               [bis 15 Mio. EUR / 3 %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2024/1689 (KI-VO / EU AI Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Volltext
- Art. 50 KI-VO (Transparenzpflichten), Art. 99 KI-VO (Sanktionen), Art. 113 KI-VO (Geltungsbeginn)
- **Digital Omnibus on AI** — Änderungsverordnung zur KI-VO (EP 16.06.2026, Rat 29.06.2026); **Art. 50 von der Verschiebung ausgenommen, Geltung bleibt 02.08.2026**. Amtsblatt-Fundstelle `[unverifiziert - prüfen]`
- **KI-MIG** (KI-Marktüberwachungs- und Innovationsförderungsgesetz) — Bundestag 11.06.2026, Bundesrat 10.07.2026, **zum 21.07.2026 nicht im BGBl. verkündet**; Marktüberwachung durch die BNetzA `[unverifiziert - prüfen]`

### Leitlinien

- EU-Kommission, Leitlinien zu Transparenzpflichten nach Art. 50 KI-VO (Entwurf)

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- BeckOK KI-VO (Online)
