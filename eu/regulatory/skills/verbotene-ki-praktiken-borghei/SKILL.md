---
name: verbotene-ki-praktiken-borghei
title: /ki-vo-compliance:verbotene-ki-praktiken
description: Prüfung der verbotenen KI-Praktiken nach Art. 5 KI-VO – manipulative und ausnutzende Systeme, Social Scoring, biometrische Echtzeit-Fernidentifizierung, Ausnahmen und Bußgeldrisiko Art. 99 KI-VO. Use when ein Unternehmen oder eine Behörde prüfen muss, ob ein geplantes oder eingesetztes KI-System unter die Verbotstatbestände der KI-VO fällt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-vo-compliance/skills/verbotene-ki-praktiken
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /ki-vo-compliance:verbotene-ki-praktiken

## Zweck

**Art. 5 KI-VO** ([VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689)) listet die KI-Praktiken, die als mit den europäischen Grundrechten unvereinbar **vollständig verboten** sind. Diese Verbote gelten seit dem 2. Februar 2025. Verstöße bilden die höchste Bußgeldstufe der Verordnung. Dieser Skill prüft, ob ein System einen Verbotstatbestand erfüllt und ob eine eng auszulegende Ausnahme greift.

> **⚠️ Aktualität (Stand 2026-07): Zwei neue Verbotstatbestände ab 02.12.2026.** Der **Digital Omnibus on AI** (Europäisches Parlament **16.06.2026**, Rat **29.06.2026**) hat den Katalog des Art. 5 KI-VO um **zwei** Praktiken erweitert, die **ab dem 02.12.2026** verboten sind:
>
> | Neuer Verbotstatbestand | Geltung |
> |---|---|
> | **Nicht einvernehmliche intime Bildaufnahmen (NCII)** — KI-gestützte Erzeugung/Verbreitung intimer Darstellungen ohne Einwilligung der abgebildeten Person | **02.12.2026** |
> | **Darstellungen sexuellen Kindesmissbrauchs (CSAM)** | **02.12.2026** |
>
> **Die bestehenden Verbote des Art. 5 gelten unverändert seit dem 02.02.2025** und werden durch den Digital Omnibus **weder verschoben noch inhaltlich geändert**. Die Neuerungen treten neben den bisherigen Katalog; die Buchstabenzuordnung der bestehenden Tatbestände bleibt bestehen. Amtsblatt-Fundstelle der Änderungsverordnung `[unverifiziert - prüfen]`.
>
> **Aufsicht erweitert:** Die Zuständigkeit des **KI-Büros** erstreckt sich nunmehr auch auf KI-*Systeme*, die auf GPAI-Modellen aufsetzen, welche **innerhalb desselben Unternehmens** wie der Modellanbieter entwickelt wurden. Konzernintern gebaute Anwendungen fallen damit nicht mehr allein in die nationale Marktüberwachung.
>
> **Nationale Zuständigkeit in Deutschland:** Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit nach dem KI-MIG), **nicht** die Datenschutzaufsicht oder die/der BfDI. Für biometrische Systeme in Strafverfolgung, Grenzkontrolle, Justiz und demokratischen Prozessen ist die unabhängige **KI-Marktüberwachungskammer (UKIM)** zuständig. Das **KI-MIG** hat den Bundestag am **11.06.2026** und den Bundesrat am **10.07.2026** passiert, war zum **21.07.2026 aber noch nicht im BGBl. verkündet** — eine BGBl.-Fundstelle existiert daher nicht und darf nicht zitiert werden. `[unverifiziert - prüfen]`

## Eingaben

- Funktion und Zweck des KI-Systems
- Adressatenkreis (allgemeine Öffentlichkeit, Beschäftigte, vulnerable Gruppen)
- Einsatzkontext (öffentlich zugänglicher Raum, Strafverfolgung, privat, behördlich)
- Verwendete Techniken (Manipulation, biometrische Erfassung, Bewertung von Sozialverhalten)
- Rolle des Mandanten (Anbieter, Betreiber)

## Sub-Agent-Architektur

Drei gedankliche Rollen prüfen das System. Ein **Tatbestands-Prüfer** ordnet die Funktion den acht Verbotskategorien des Art. 5 KI-VO zu und arbeitet die jeweiligen Tatbestandsmerkmale heraus. Ein **Ausnahme-Analyst** prüft spiegelbildlich die eng gefassten Ausnahmen, insbesondere bei der biometrischen Echtzeit-Fernidentifizierung zu Strafverfolgungszwecken. Ein **Sanktions-Bewerter** beziffert das Bußgeldrisiko nach Art. 99 KI-VO und grenzt zur Hochrisiko-Einstufung ab. Der Tatbestands-Prüfer übergibt jeden bejahten Verbotstatbestand an den Ausnahme-Analysten, bevor das Endergebnis steht.

## Ablauf

### 1. Verbotskategorien (Art. 5 Abs. 1 KI-VO)

a) **Unterschwellige/manipulative Beeinflussung**, die das Verhalten wesentlich verändert und Schaden verursacht
b) **Ausnutzung von Vulnerabilität** (Alter, Behinderung, soziale/wirtschaftliche Lage) mit Schadensfolge
c) **Social Scoring** — Bewertung/Klassifizierung anhand sozialen Verhaltens oder persönlicher Merkmale mit ungerechtfertigter Schlechterstellung in nicht zusammenhängenden Kontexten
d) **Prädiktive Strafverfolgung** allein auf Profiling/Persönlichkeitsmerkmalen
e) **Ungezieltes Scraping** von Gesichtsbildern zum Aufbau von Gesichtserkennungsdatenbanken
f) **Emotionserkennung** am Arbeitsplatz und in Bildungseinrichtungen (außer medizinisch/sicherheitsbezogen)
g) **Biometrische Kategorisierung** zur Ableitung sensibler Merkmale (z. B. ethnische Herkunft, politische Meinung, sexuelle Orientierung)
h) **Biometrische Echtzeit-Fernidentifizierung** in öffentlich zugänglichen Räumen zu Strafverfolgungszwecken

Die Tatbestände a) bis h) gelten **seit dem 02.02.2025** und sind unverändert.

### 1a. Neue Verbotstatbestände ab 02.12.2026 (Digital Omnibus on AI)

Ergänzend — und **erst ab dem 02.12.2026** — verboten:

- **Nicht einvernehmliche intime Bildaufnahmen (NCII).** Erfasst sind KI-Systeme, die intime oder sexualisierte Darstellungen realer Personen ohne deren Einwilligung erzeugen oder manipulieren („Nudify"-Anwendungen, Deepfake-Pornografie). Betroffen sind Anbieter generativer Bild- und Videomodelle mit entsprechender Funktionalität ebenso wie Betreiber, die solche Systeme bereitstellen.
- **Darstellungen sexuellen Kindesmissbrauchs (CSAM).** KI-gestützte Erzeugung entsprechender Inhalte ist unabhängig davon verboten, ob reale Personen abgebildet sind.

**Prüfhinweise:**

1. **Zeitliche Anwendung beachten.** Vor dem 02.12.2026 sind diese Praktiken nicht nach Art. 5 KI-VO verboten. Sie sind jedoch bereits jetzt regelmäßig nach **nationalem Straf- und Persönlichkeitsrecht** unzulässig (u. a. §§ 184b, 201a StGB, allgemeines Persönlichkeitsrecht, DSGVO) — die Aussage „derzeit noch erlaubt" ist im Mandat **falsch**.
2. **Vorlaufpflicht der Anbieter.** Generative Modelle sind bis zum Stichtag durch Filter, Prompt- und Ausgabekontrollen sowie Missbrauchsmeldewege abzusichern; die Umstellung ist nicht kurzfristig leistbar.
3. **Abgrenzung zu Art. 50.** Die Kennzeichnungspflicht für Deepfakes (Art. 50 Abs. 4, ab 02.08.2026) macht einen verbotenen Inhalt **nicht zulässig** — eine gekennzeichnete NCII-Darstellung bleibt ab 02.12.2026 verboten.

Fundstelle der Änderungsverordnung im Amtsblatt `[unverifiziert - prüfen]`.

### 2. Ausnahmen bei biometrischer Echtzeit-Fernidentifizierung (Art. 5 Abs. 1 lit. h KI-VO)

Nur **drei** eng begrenzte Zwecke kommen in Betracht:

- gezielte Suche nach Opfern von Entführung, Menschenhandel, sexueller Ausbeutung sowie vermissten Personen
- Abwendung einer konkreten, erheblichen und unmittelbaren Gefahr für Leib/Leben oder eines Terroranschlags
- Lokalisierung/Identifizierung eines einer schweren Straftat Verdächtigen

Voraussetzung: vorherige **richterliche oder behördliche Genehmigung** (Art. 5 Abs. 3 KI-VO), Verhältnismäßigkeit, nationale Ermächtigungsgrundlage.

### 3. Abgrenzung zur Hochrisiko-Einstufung

Greift kein Verbot, ist die Hochrisiko-Prüfung nach Art. 6 i.V.m. Anhang III KI-VO der nächste Schritt — ein System kann zulässig, aber hochreguliert sein.

### 4. Sanktionen (Art. 99 KI-VO)

Verstöße gegen die Verbote nach Art. 5 KI-VO werden mit Geldbußen bis **35 Mio. EUR oder 7 % des weltweiten Jahresumsatzes** geahndet — die höchste Stufe.

## Risiken

- **Manipulation** — vermeintlich harmlose Personalisierung kann als unterschwellige Beeinflussung nach Art. 5 KI-VO verboten sein.
- **Social Scoring** durch die Hintertür — übergreifende Reputations- oder Bonitätssysteme können den Verbotstatbestand erfüllen.
- **Scheinausnahme** — die Ausnahmen zur biometrischen Echtzeit-Fernidentifizierung sind eng; eine fehlende Genehmigung nach Art. 5 Abs. 3 KI-VO macht den Einsatz verboten.
- **Bußgeldrisiko** — bis 35 Mio. EUR / 7 % nach Art. 99 KI-VO; Verbote gelten bereits seit Februar 2025.
- **Neue Verbote NCII und CSAM übersehen** — der Katalog des Art. 5 ist durch den Digital Omnibus on AI erweitert worden; die beiden Tatbestände greifen **ab 02.12.2026**. Prüfungen, die nur die acht Tatbestände von 2025 abarbeiten, sind unvollständig. Betroffen sind insbesondere Anbieter generativer Bild- und Videomodelle.
- **„Bis 02.12.2026 erlaubt" als Freibrief missverstanden** — NCII- und CSAM-Erzeugung ist bereits heute nach nationalem Straf- und Persönlichkeitsrecht sanktionsbewehrt. Die KI-VO ergänzt nur eine weitere, besonders scharfe Sanktionsebene.
- **Nationale Zuständigkeit falsch adressiert** — Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit, KI-MIG), **nicht** die Datenschutzaufsicht oder die/der BfDI; für Biometrie in Strafverfolgung, Grenzkontrolle, Justiz und demokratischen Prozessen die unabhängige **KI-Marktüberwachungskammer (UKIM)**. Das KI-MIG war zum 21.07.2026 **noch nicht im BGBl. verkündet**; eine BGBl.-Fundstelle darf nicht angegeben werden. `[unverifiziert - prüfen]`
- **Konzerninterne GPAI-Anwendungen falsch zugeordnet** — setzt ein KI-System auf einem GPAI-Modell desselben Unternehmens auf, ist die Aufsicht des **KI-Büros** eröffnet; die Annahme rein nationaler Zuständigkeit trägt nicht.

## Ausgabeformat

```
VERBOTENE KI-PRAKTIKEN — PRÜFUNG — <System> — <Datum>

I.   Funktion / Zweck                          [Beschreibung]
II.  Einschlägige Kategorie (Art. 5 KI-VO)     [lit. a–h / NCII / CSAM / keine]
     Tatbestandsmerkmale                       [erfüllt? <…>]
     Geltung ab                                [02.02.2025 / 02.12.2026]
III. Ausnahme (Art. 5 Abs. 1 lit. h / Abs. 3 KI-VO)  [greift? / Genehmigung?]
IV.  Ergebnis                                  [VERBOTEN / nicht verboten]
V.   Falls nicht verboten: Hochrisiko-Check (Art. 6, Anhang III)  [erforderlich?]
VI.  Bußgeldrisiko (Art. 99 KI-VO)             [bis 35 Mio. EUR / 7 %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2024/1689 (KI-VO / EU AI Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Volltext mit Anhängen
- Art. 5 KI-VO (verbotene Praktiken), Art. 6 KI-VO und Anhang III (Hochrisiko), Art. 99 KI-VO (Sanktionen)
- **Digital Omnibus on AI** — Änderungsverordnung zur KI-VO (EP 16.06.2026, Rat 29.06.2026); neue Verbote NCII und CSAM ab 02.12.2026. Amtsblatt-Fundstelle `[unverifiziert - prüfen]`
- **KI-MIG** (KI-Marktüberwachungs- und Innovationsförderungsgesetz) — Bundestag 11.06.2026, Bundesrat 10.07.2026, **zum 21.07.2026 nicht im BGBl. verkündet**; Zuständigkeit BNetzA / UKIM `[unverifiziert - prüfen]`

### Leitlinien

- EU-Kommission, Leitlinien zur Anwendung der Verbote gemäß Art. 5 KI-VO (Februar 2025) — **erfassen die Tatbestände NCII und CSAM noch nicht**

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- BeckOK KI-VO (Online)
