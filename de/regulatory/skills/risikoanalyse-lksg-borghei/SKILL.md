---
name: risikoanalyse-lksg-borghei
title: /lieferkettengesetz:risikoanalyse-lksg
description: Risikoanalyse nach § 5 LkSG – Identifikation menschenrechtlicher und umweltbezogener Risiken im eigenen Geschäftsbereich und bei unmittelbaren Zulieferern; anlassbezogene Erweiterung auf mittelbare Zulieferer (§ 9 LkSG). Use when ein Unternehmen die jährliche Risikoanalyse aufsetzt oder ein anlassbezogenes Risiko bei einem mittelbaren Zulieferer eingegangen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/lieferkettengesetz/skills/risikoanalyse-lksg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /lieferkettengesetz:risikoanalyse-lksg

## Zweck

Die Risikoanalyse ist der Anker des LkSG. Eine unzureichende Risikoanalyse macht die nachfolgenden Pflichten (Prävention, Abhilfe, Beschwerdeverfahren) angreifbar — und führt regelmäßig zu BAFA-Anfragen mit Bußgeldrisiko nach **§ 24 LkSG**: bis zu **800.000 EUR** (Abs. 2 Satz 1 Nr. 1) für Pflichtverletzungen wie Abhilfemaßnahme nicht ergriffen, **500.000 EUR** für Risikoanalyse-Verletzung (Nr. 2), **100.000 EUR** in den übrigen Fällen. Bei juristischen Personen mit durchschnittlichem Jahresumsatz **> 400 Mio. EUR** kann eine Geldbuße nach § 24 Abs. 3 LkSG bis zu **2 % des weltweiten durchschnittlichen Jahresumsatzes** verhängt werden — beschränkt auf Verstöße gegen Abhilfepflichten (Abs. 1 Nr. 6, Nr. 7 lit. a).

> **⚠️ Aktualität (Stand 2026-07) — die Risikoanalyse gilt unverändert fort; nur die Berichtseinreichung ist entfallen:** Das **BAFA** hat die Prüfung von Unternehmensberichten nach **§§ 12, 13 LkSG mit Wirkung zum 03.09.2025 vollständig eingestellt**; der Einreichungszugang **ist geschlossen**. Grundlage ist ein **Kabinettsbeschluss vom 03.09.2025 nebst Weisung an das BAFA**, mit der die Bundesregierung nach eigener Formulierung „der Gesetzesnovelle vorgreift".
>
> **Wichtige Abgrenzung:** Es handelt sich um eine **exekutive Weisung, nicht um eine Gesetzesaufhebung**. Die §§ 12, 13 LkSG stehen formal weiter im Gesetz; sie werden lediglich nicht mehr vollzogen und können mangels Einreichungsweg auch nicht erfüllt werden. Die geplante Novelle war zum Stand 07/2026 **nicht als verkündetes Gesetz nachweisbar** — Inkrafttretensstand `[unverifiziert - prüfen]`.
>
> **Für diese Skill entscheidend:** Die **Risikoanalyse nach § 5 LkSG** ist von alledem **nicht betroffen**. Sie besteht ebenso fort wie die anlassbezogene Prüfung mittelbarer Zulieferer (§ 9), die Präventions- und Abhilfemaßnahmen (§§ 6, 7), das Beschwerdeverfahren (§ 8), die interne **Dokumentation (§ 10)** sowie die behördliche **Kontrolle und Anordnungsbefugnis (§§ 14, 15)**. Der Wegfall der Berichtseinreichung ist **kein** Grund, die Risikoanalyse auszusetzen — im Gegenteil: sie ist nun der zentrale Nachweis gegenüber dem BAFA im Kontrollverfahren. Ordnungswidrigkeiten sollen künftig auf besonders schwere Verstöße konzentriert werden.
>
> **CSDDD-Ausblick:** Nach **Omnibus I** (Änderungs-RL (EU) 2026/470, in Kraft 18.03.2026) liegt die CSDDD-Schwelle bei **> 5.000 Beschäftigten UND > 1,5 Mrd. EUR Nettoumsatz**; Umsetzungsfrist **26.07.2028**, materielle Pflichten ab **26.07.2029**. Die alte Phasierung (6.000 / 900 Mio. EUR, 2027/2028) ist überholt.

## Eingaben

- Geschäftsbereich (Branchen, Geographie, Produkte/Dienstleistungen)
- Direkte Zulieferer (Liste, Länder, Risikoprofile)
- Bekannte Vorfälle / Beschwerden / NGO-Berichte
- Ergebnis der vorherigen Risikoanalyse
- CSDDD-Anwendungszeitraum (für Vorbereitung)

## Ablauf

### 1. Geltungsbereich (§ 1 LkSG)

- Hauptverwaltung in DE und **≥ 1.000 Beschäftigte** im Inland (seit 2024)
- Konzernzurechnung: Beschäftigte verbundener Unternehmen in DE werden berücksichtigt (§ 1 Abs. 3 LkSG)

### 2. Geschützte Rechtspositionen (§ 2 LkSG)

- **Menschenrechtliche Risiken** § 2 Abs. 2 (Verbot Kinderarbeit, Zwangsarbeit, Diskriminierung, unzureichende Arbeitssicherheit, Vorenthalten angemessenen Lohns, Verstoß gegen Vereinigungsfreiheit, Folter, rechtswidrige Landnahme, Einsatz von Sicherheitskräften mit Übergriff)
- **Umweltbezogene Risiken** § 2 Abs. 3 (Minamata-Übereinkommen Quecksilber, Stockholmer Konvention POPs, Basler Konvention Abfälle)

### 3. Risikoanalyse-Stufen (§ 5 LkSG)

**Stufe 1 – eigener Geschäftsbereich:**

- Standorte, Tochterunternehmen
- Beschäftigte, Subunternehmer auf dem Werksgelände

**Stufe 2 – unmittelbare Zulieferer:**

- Vertragliche Direktbeziehung
- Risikobewertung mind. **jährlich** und **anlassbezogen**

**Stufe 3 – mittelbare Zulieferer (§ 9 LkSG):**

- Nur **anlassbezogen** bei "substantiierter Kenntnis" eines möglichen Verstoßes
- Trigger: NGO-Bericht, Medienbericht, interne Hinweise, Audit-Findings

### 4. Methodik der Risikobewertung

Pro Risiko bewerten:

1. **Schweregrad** – wie gravierend ist der mögliche Verstoß?
2. **Umkehrbarkeit** – wie umkehrbar ist der Schaden?
3. **Wahrscheinlichkeit** – wie wahrscheinlich tritt er ein?
4. **Beitragsleistung** – verursacht / trägt bei / steht in unmittelbarer Geschäftsbeziehung?
5. **Einflussvermögen** – wie viel Einfluss hat das Unternehmen?

### 5. Priorisierung (§ 5 Abs. 2 LkSG)

Risiken werden nach Angemessenheits-Kriterien priorisiert:

- Art und Umfang der Geschäftstätigkeit
- Einflussvermögen
- typische Schwere und Umkehrbarkeit
- Wahrscheinlichkeit
- Art des Verursachungsbeitrags

### 6. Dokumentation (§ 10 LkSG)

- **Dokumentationspflicht** intern (§ 10 Abs. 1) — **gilt unverändert fort** und ist der maßgebliche Nachweis im BAFA-Kontrollverfahren nach §§ 14, 15 LkSG.
- Aufbewahrung **7 Jahre**.
- **Berichtspflicht (§§ 12, 13 LkSG):** Das **BAFA** nimmt seit dem **03.09.2025 keine Berichte mehr entgegen und prüft keine mehr**; der Einreichungszugang ist geschlossen. Eine Einreichung ist weder möglich noch gefordert — Mandanten ist **nicht** dazu zu raten.
- **Beratungsfolge:** Berichtsinhalte als **interne Dokumentation nach § 10 LkSG** vorhalten. Ein bereits erstellter Bericht ist nicht wertlos, sondern wird zur Dokumentationsgrundlage.
- **Nicht als Aufhebung darstellen:** Es handelt sich um eine exekutive Weisung, nicht um eine Gesetzesaufhebung; zwischen *nicht vollzogen* und *aufgehoben* ist zu unterscheiden `[unverifiziert - prüfen]`. Einzelheiten in `/lieferkettengesetz:bafa-bericht-lksg`.

### 7. CSDDD-Ausblick (Richtlinie (EU) 2024/1760)

- Förmlich angenommen **24.05.2024**, geändert durch die **Änderungs-RL (EU) 2026/470 (Omnibus I)**, Amtsblatt **26.02.2026**, in Kraft **18.03.2026**.

**Geltender Stand nach Omnibus I:**

| Punkt | Wert |
|---|---|
| Anwendungsschwelle | **> 5.000 Beschäftigte UND > 1,5 Mrd. EUR Nettoumsatz** (kumulativ) |
| Umsetzungsfrist der Mitgliedstaaten | **26.07.2028** |
| Materielle Sorgfaltspflichten | ab **26.07.2029** |

**Überholt und nicht mehr zu verwenden:** die frühere Phasierung mit **Phase 1 (26.07.2027, > 6.000 Beschäftigte / > 1,5 Mrd. EUR)** und **Phase 2 (26.07.2028, > 900 Mio. EUR)** sowie die „Stop-the-Clock"-RL (EU) 2025/794.

- **Praxisfolge — Schwellenprüfung neu durchführen:** Ein großer Teil der bislang adressierten Unternehmen fällt aus dem CSDDD-Anwendungsbereich **heraus**. Die LkSG-Schwelle (**≥ 1.000 Beschäftigte im Inland**) sagt über die CSDDD-Betroffenheit **nichts** aus; wer LkSG-pflichtig ist, ist typischerweise gerade **nicht** CSDDD-pflichtig. Betroffenheit ist eigenständig und kumulativ zu prüfen.
- **Sorgfaltspflichten auf die gesamte „Chain of Activities"** (Upstream + Teile Downstream).
- Klimaplan-Pflicht (Art. 22 CSDDD); zivilrechtliche Haftung (Art. 29 CSDDD) — Ausgestaltung nach Omnibus I `[unverifiziert - prüfen]`.
- **Wertschöpfungsketten-Cap:** Datenanfragen an kleinere Geschäftspartner sind auf die gesetzliche Obergrenze begrenzt; diese dürfen weitergehende Anfragen zurückweisen. Lieferantenfragebögen und Self-Assessments sind entsprechend zu dimensionieren.
- Mapping der bestehenden LkSG-Kontrollen auf **Art. 8–11 CSDDD** empfohlen `[unverifiziert - prüfen]`.

## Quellen

### Statute

- [LkSG (Lieferkettensorgfaltspflichtengesetz)](https://www.gesetze-im-internet.de/lksg/) — Volltext, §§ 1–24
- [§ 5 LkSG](https://www.gesetze-im-internet.de/lksg/__5.html), [§ 9 LkSG](https://www.gesetze-im-internet.de/lksg/__9.html), [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [§ 12 LkSG](https://www.gesetze-im-internet.de/lksg/__12.html), [§ 13 LkSG](https://www.gesetze-im-internet.de/lksg/__13.html) — formal in Kraft, seit 03.09.2025 **nicht mehr vollzogen** (Kabinettsbeschluss + Weisung an das BAFA); Einreichungszugang geschlossen `[unverifiziert - prüfen]`
- [§ 14 LkSG](https://www.gesetze-im-internet.de/lksg/__14.html), [§ 15 LkSG](https://www.gesetze-im-internet.de/lksg/__15.html) — behördliche Kontrolle und Anordnungen, unverändert in Kraft
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/eli/dir/2024/1760/oj) · **Änderungs-RL (EU) 2026/470 (Omnibus I)**, Amtsblatt 26.02.2026, in Kraft 18.03.2026 — Schwelle > 5.000 Beschäftigte und > 1,5 Mrd. EUR; ELI-Fundstelle `[unverifiziert - prüfen]`
- UN-Leitprinzipien für Wirtschaft und Menschenrechte (UNGPs)
- ILO-Kernarbeitsnormen

### BAFA

- [BAFA – Lieferkettengesetz](https://www.bafa.de/DE/Lieferketten/ueberblick_node.html) — Kontrolle, Anordnungen, Bußgeldverfahren; **Berichtsprüfung nach §§ 12, 13 LkSG zum 03.09.2025 eingestellt, Einreichungsportal geschlossen**
- BAFA-Handreichungen zur Risikoanalyse (aktuelle Fassung)

### Sekundärliteratur

- Grabosch, LkSG, 1. Aufl. 2023
- Hembach, in: Beck'scher Online-Kommentar LkSG (aktualisiert)

## Ausgabeformat

```
LkSG-RISIKOANALYSE — <Berichtsjahr> — <Datum>

I.    Geltungsbereich                [Ja / Nein — Beschäftigtenzahl]
II.   Methodik
      Schwere | Umkehrbarkeit | Wahrscheinlichkeit | Beitragsleistung | Einfluss
III.  Stufe 1 — eigener Geschäftsbereich
      Identifizierte Risiken: <Liste>
      Bewertung: <Priorisierung>
IV.   Stufe 2 — unmittelbare Zulieferer
      Top-N nach Risikoexposition: <…>
      Methodik: <Self-Assessment / Audit / Datenanbieter>
V.    Stufe 3 — mittelbare Zulieferer
      Substantiierte Kenntnis: [keine / Ja — Quelle: …]
      Vertiefte Prüfung: <…>
VI.   Priorisierte Risiken (Top 5)   <…>
VII.  Folgemaßnahmen
      - Prävention § 6              <…>
      - Abhilfe § 7                  <…>
      - Vertragliche Verankerung     <…>
VIII. Dokumentation § 10 LkSG (interne Nachweisführung, 7 Jahre)
      Hinweis: KEINE BAFA-Einreichung — §§ 12, 13 LkSG seit 03.09.2025
      nicht mehr vollzogen, Zugang geschlossen ([unverifiziert - prüfen])
      Vorbereitung auf BAFA-Kontrolle §§ 14, 15 LkSG: <…>
IX.   CSDDD-Schwellenprüfung (neu)
      > 5.000 Beschäftigte? [Ja/Nein]  > 1,5 Mrd. EUR? [Ja/Nein]
      Kumulativ erfüllt: [Ja/Nein]  — materielle Pflichten ab 26.07.2029

Risiko-Restrisiko: <…>
Wiedervorlage: jährlich + ad-hoc
```

## Risiken / typische Fehler

- **Stufenfolge ignoriert** — direkter Sprung auf mittelbare Zulieferer ohne substantiierten Anlass.
- **Self-Assessment ohne Verifizierung** — BAFA verlangt belastbare Methodik.
- **CSDDD-Vorbereitung vergessen** — Übergangsfristen sind kurz für eine valide Datenbasis.
- **Dokumentation lückenhaft** — Pflicht ist beweispflichtig in BAFA-Verfahren.
- **Beschwerden ignoriert** — eine eingehende Beschwerde ist regelmäßig „substantiierte Kenntnis" i.S.v. § 9 LkSG.
- **Klimaschutz / Umwelt eng ausgelegt** — LkSG erfasst Quecksilber/POPs/Abfall, CSDDD wird breiter (Pariser Klimaabkommen).
- **Mandant plant gegen aufgehobenes Recht (CSDDD-Phasierung)** — Vorbereitung auf „Phase 1 ab 26.07.2027 / > 6.000 Beschäftigte" oder „Phase 2 / > 900 Mio. EUR". Diese Phasierung ist durch **Omnibus I** (RL (EU) 2026/470, in Kraft 18.03.2026) **überholt**: Schwelle **> 5.000 Beschäftigte UND > 1,5 Mrd. EUR**, materielle Pflichten erst ab **26.07.2029**. Wer nach altem Stand plant, baut ein Programm für eine Pflicht auf, die den Mandanten nicht trifft.
- **Risikoanalyse wegen des BAFA-Berichtsstopps ausgesetzt** — der gefährlichste Umkehrschluss. **§ 5 LkSG gilt unverändert fort**; eingestellt ist nur die Berichtsprüfung nach §§ 12, 13 LkSG (03.09.2025). Die Risikoanalyse ist jetzt sogar der zentrale Nachweis im Kontrollverfahren nach §§ 14, 15 LkSG.
- **„Nicht vollzogen" mit „aufgehoben" verwechselt** — die §§ 12, 13 LkSG stehen formal weiter im Gesetz; Grundlage des Stopps ist eine **exekutive Weisung**, keine Gesetzesaufhebung. Die Novelle war zum Stand 07/2026 nicht als verkündetes Gesetz nachweisbar `[unverifiziert - prüfen]`.
- **Bericht dennoch eingereicht** — der BAFA-Einreichungszugang ist geschlossen; eine Einreichung ist weder möglich noch geschuldet. Berichtsinhalte gehören in die Dokumentation nach § 10 LkSG.
- **LkSG-Schwelle als CSDDD-Indikator verwendet** — ≥ 1.000 Beschäftigte im Inland (LkSG) sagt über die CSDDD-Betroffenheit nichts aus; die Prüfung ist eigenständig und kumulativ vorzunehmen.
