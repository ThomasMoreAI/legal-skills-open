---
name: brao-pflichtenpruefung-borghei
title: /berufsrecht-anwaltschaft:brao-pflichtenpruefung
description: Checkliste anwaltlicher Grundpflichten vor Mandatsannahme und im laufenden Mandat – Verschwiegenheit § 43a II BRAO + § 2 BORA + § 203 StGB, Interessenkollision § 43a IV BRAO + § 3 BORA + § 356 StGB (mit Sozietätszurechnung), Sachlichkeit § 43a III/§ 44, Werbung § 43b/§§ 6 ff. BORA, Auslagerung/KI § 43e, Vergütung § 49b, Fremdgeld § 43a V, GwG-Hinweispflichten § 50 BRAO. Use when ein Anwalt vor Mandatsannahme die berufsrechtliche Zulässigkeit prüfen muss, eine Sozietät einen Konflikt-Check braucht, ein RAK-Aufsichtsverfahren droht oder KI-/Cloud-Auslagerung berufsrechtlich abzusichern ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/berufsrecht-anwaltschaft/skills/brao-pflichtenpruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /berufsrecht-anwaltschaft:brao-pflichtenpruefung

## Zweck

Der Skill prüft die zentralen Grundpflichten der BRAO entlang einer festen Reihenfolge — Verschwiegenheit zuerst, Interessenkollision zweitens, dann die konkreten Pflichtenkomplexe (Werbung, Auslagerung, Vergütung, Fremdgeld). Er ist sowohl Mandatsannahme-Checkliste als auch Verteidigungsraster, wenn ein Rüge- oder anwaltsgerichtliches Verfahren droht. Der Skill zeigt für jede Pflicht die strafrechtlichen Reflexe (§§ 203, 356 StGB) und die verfahrensrechtliche Folgenseite (§§ 73 ff., §§ 113 ff. BRAO).

## Eingaben

- Kanzleistruktur (Einzelanwalt, Sozietät, PartG mbB, RA-GmbH; Standort)
- Mandatsbeschreibung (Gegner, Sachverhalt, Vorbefassung in der Sozietät?)
- Frühere Mandate, die berührt sein könnten (Sozietätsdatenbank!)
- Drittanbieter im Workflow (Cloud, KI-Tools, externe Schreibkraft, Aktenscannen) — Vertragsstatus, AVV vorhanden?
- Honorarmodell (Stundensatz, Pauschal, Vergütungsvereinbarung, Erfolgshonorar erwogen?)
- Werbung/Außenauftritt (Website, Social Media, Akquise-Schreiben)
- Anlass der Prüfung: Mandatsanbahnung / laufendes Mandat / Rüge-Verfahren / Aufsichtsanhörung RAK

## Sub-Agent-Architektur

Researcher liefert BRAO-/BORA-Statute, BGH-Anwaltssenat-Rspr. zu Verschwiegenheit, Interessenkollision, Werbung und Auslagerung, BVerfG zu Art. 12 GG-Werbung, sowie Standardkommentare (Henssler/Prütting, Feuerich/Weyland, Kleine-Cosack, Hartung/Scharmer). Drafter prüft die sechs Pflichtenkomplexe in Gutachtenstil mit Sozietäts-zurechnung und schreibt Mandatsannahme- oder -ablehnungsvermerk. Reviewer setzt Verschwiegenheit (§ 203 StGB) und Interessenkollision (§ 43a IV BRAO + § 3 BORA) als zwingende Pflichtpunkte 1 und 2 — Lücken sind Blocker.

## Ablauf

### 1. Verschwiegenheit § 43a Abs. 2 BRAO — § 2 BORA — § 203 StGB

Verschwiegenheit ist die zentrale Grundpflicht des Rechtsanwalts. Sie umfasst alles, was in Ausübung des Berufs bekannt geworden ist, gilt zeitlich **unbegrenzt** (auch nach Mandatsende, § 43a Abs. 2 S. 1 BRAO) und ist sachlich nicht auf den Mandanten beschränkt. Verletzung ist strafbar nach § 203 Abs. 1 Nr. 3 StGB (Geldstrafe oder Freiheitsstrafe bis 1 Jahr).

Erlaubte Durchbrechungen:

- Einwilligung des Mandanten (ausdrücklich, informiert)
- Wahrnehmung berechtigter Interessen des Anwalts (§ 2 Abs. 3 BORA, eng auszulegen — z. B. Honorarklage, Verteidigung gegen Vorwürfe)
- Gesetzliche Offenbarungspflichten (z. B. Geldwäsche § 43 GwG iVm § 2 GwG, §§ 138, 139 StGB-Anzeigepflichten in engem Rahmen)

Datenpannen-Schutz: Anwalt schuldet **organisatorische Sicherung** (verschlossene Akten, IT-Sicherheit, Need-to-know in Sozietät).

### 2. Interessenkollision § 43a Abs. 4 BRAO — § 3 BORA — § 356 StGB

Es ist verboten, **widerstreitende Interessen** zu vertreten. Maßstab:

- **„Dieselbe Rechtssache"** = derselbe Sachverhalt mit innerem Zusammenhang, auch wenn formal getrennte Aktenzeichen.
- **Vorbefassung** — auch nur beratend, auch nur außergerichtlich, auch nur durch einen anderen Berufskollegen der Sozietät — sperrt.
- **Sozietätszurechnung § 3 BORA**: Was ein Sozietätsmitglied weiß / vertreten hat, ist allen zugerechnet. Auch nach Ausscheiden bleibt die Sperre für den Ausgeschiedenen und für die Sozietät bestehen, wenn er „in derselben Rechtssache" tätig war.
- **Einwilligung beider Mandanten** kann den Konflikt heilen, wenn objektiv keine Gefährdung besteht (§ 3 Abs. 2 BORA, Streit über Reichweite — h.M. eng auszulegen).

Verstoß strafrechtlich: § 356 StGB (Parteiverrat — Freiheitsstrafe drei Monate bis fünf Jahre).

### 3. Sachlichkeitsgebot § 43a Abs. 3 BRAO — § 44 BRAO

Der Anwalt darf sich nicht unsachlich verhalten. Unsachlich sind insbesondere bewusste Unwahrheiten, herabwürdigende Äußerungen ohne Sachbezug. Streit über Reichweite (BVerfG: weite Meinungsfreiheit Art. 5 GG für berufliche Äußerungen `[unverifiziert – prüfen]`).

### 4. Werbung § 43b BRAO — §§ 6 ff. BORA

Sachliche Information über die berufliche Tätigkeit ist zulässig. Verboten ist Werbung, die auf Erteilung eines Auftrags im Einzelfall gerichtet ist. § 6 BORA konkretisiert: keine reklamehafte Werbung, keine vergleichende Werbung mit Berufskollegen, keine Erfolgs- und Umsatzangaben (§ 7 BORA) ohne dokumentierte Grundlage.

BVerfG hat das Werberecht mehrfach grundrechtskonform gelockert (Art. 12 GG `[unverifiziert – prüfen]`).

### 5. Auslagerung § 43e BRAO — Brücke zur KI-/Cloud-Compliance

Auslagerung an Dritte (IT-Dienstleister, Cloud, KI-Tools, externe Schreibkraft) verlangt:

- **Schriftliche Vereinbarung** über Verschwiegenheit (§ 43e Abs. 2 Nr. 1 BRAO)
- **Sorgfältige Auswahl und Kontrolle** des Dienstleisters (§ 43e Abs. 2 Nr. 2 BRAO)
- **Verpflichtung der Hilfspersonen** zur Verschwiegenheit nach § 203 Abs. 4 StGB
- **AVV (Art. 28 DSGVO)** parallel
- **Information des Mandanten**, wenn besondere Risiken (z. B. Cloud-Speicherung außerhalb EU, generative KI mit Trainings-Risiko)

Für KI-Tools: Prompts mit Mandatsbezug enthalten geschützte Geheimnisse iSv § 203 StGB. Ohne § 43e-konforme Vereinbarung und ohne § 203 IV StGB-Verpflichtung → **Strafbarkeitsrisiko**. Brücke zum geplanten `ki-governance`-Skill.

### 6. Vergütung § 49b BRAO — RVG

- Gebühren des RVG sind grundsätzlich bindend; Unterschreitung außerhalb gerichtlicher Verfahren in Grenzen erlaubt (§ 49b Abs. 1 BRAO, § 4 RVG).
- **Erfolgshonorar-Verbot** § 49b Abs. 2 BRAO. Ausnahmen § 4a RVG: (i) Mandant würde aus wirtschaftlichen Gründen sonst von der Rechtsverfolgung absehen, (ii) Inkassodienstleistungen, (iii) Auslandsfälle, jeweils eng ausgelegt.
- Honorarvereinbarung in Textform, deutlich abgesetzt vom Mandatsvertrag (§ 3a RVG).
- **Fremdgeld § 43a Abs. 5 BRAO**: getrenntes Anderkonto, unverzügliche Auskehr, unter Berücksichtigung von Aufrechnungsrechten nur sehr eingeschränkt.

### 7. GwG-Hinweispflichten § 50 BRAO

Bei katalogmäßiger Tätigkeit nach § 2 GwG (z. B. Immobilientransaktionen, Gesellschaftsgründungen mit Mittelfluss) gelten Identifizierungs- und Aufzeichnungspflichten. § 43e BRAO regelt die berufsrechtliche Flankierung; § 50 BRAO setzt das in Kammerrecht um. Verstoß: berufsrechtliche Maßnahmen + GwG-Bußgelder.

### 8. Verfahrensrechtliche Folgenseite

- **Rüge § 74 BRAO** durch Kammervorstand. Anfechtung binnen **1 Monat** ab Zustellung.
- **Anwaltsgerichtliches Verfahren §§ 113 ff. BRAO**. Sanktionskatalog § 114: Warnung, Verweis, Geldbuße bis 50.000 €, Vertretungsverbot ein bis fünf Jahre, Ausschließung aus der Rechtsanwaltschaft.
- **Verfolgungsverjährung § 115 BRAO**: 5 Jahre, beginnt mit Beendigung der Pflichtverletzung (Dauerverstöße: Beendigung des Dauerverstands).
- Daneben: zivilrechtliche Haftung (§ 280 BGB iVm Mandatsvertrag), strafrechtliche Verfolgung (§§ 203, 356 StGB), wettbewerbsrechtliche Ansprüche (UWG bei Werbeverstößen).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 43 BRAO](https://www.gesetze-im-internet.de/brao/__43.html) (allgemeine Berufspflicht)
- [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) (Grundpflichten — Verschwiegenheit Abs. 2, Sachlichkeit Abs. 3, Interessenkollision Abs. 4, Fremdgeld Abs. 5)
- [§ 43b BRAO](https://www.gesetze-im-internet.de/brao/__43b.html) (Werbung)
- [§ 43e BRAO](https://www.gesetze-im-internet.de/brao/__43e.html) (Auslagerung)
- [§ 44 BRAO](https://www.gesetze-im-internet.de/brao/__44.html) (Sachlichkeit)
- [§§ 45, 46 BRAO](https://www.gesetze-im-internet.de/brao/__45.html) (Tätigkeitsverbote)
- [§ 49b BRAO](https://www.gesetze-im-internet.de/brao/__49b.html) (Vergütung, Erfolgshonorar)
- [§ 50 BRAO](https://www.gesetze-im-internet.de/brao/__50.html) (GwG-Hinweispflichten)
- [§ 73 BRAO](https://www.gesetze-im-internet.de/brao/__73.html) (Aufsicht durch Kammervorstand)
- [§ 74 BRAO](https://www.gesetze-im-internet.de/brao/__74.html) (Rüge, 1-Monatsfrist)
- [§ 113 BRAO](https://www.gesetze-im-internet.de/brao/__113.html) ff. (anwaltsgerichtliches Verfahren)
- [§ 114 BRAO](https://www.gesetze-im-internet.de/brao/__114.html) (Sanktionskatalog)
- [§ 115 BRAO](https://www.gesetze-im-internet.de/brao/__115.html) (5-Jahre-Verjährung)
- [§§ 2, 3, 6, 7, 14, 18, 30 BORA](https://www.brak.de/fuer-anwaelte/berufsrecht/bora/)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) (Verletzung von Privatgeheimnissen)
- [§ 356 StGB](https://www.gesetze-im-internet.de/stgb/__356.html) (Parteiverrat)
- [§ 53 Abs. 1 Nr. 3 StPO](https://www.gesetze-im-internet.de/stpo/__53.html) (Zeugnisverweigerung)
- [§ 97 StPO](https://www.gesetze-im-internet.de/stpo/__97.html) (Beschlagnahmeverbote)
- [§ 383 Abs. 1 Nr. 6 ZPO](https://www.gesetze-im-internet.de/zpo/__383.html) (Zeugnisverweigerung)
- [§§ 3a, 4, 4a RVG](https://www.gesetze-im-internet.de/rvg/__3a.html)

### Kommentare

- Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 43a Rn. 1 ff., § 43e Rn. 1 ff.
- Träger, in: Feuerich/Weyland, BRAO, 11. Aufl. 2024, § 43a Rn. 1 ff.
- Kleine-Cosack, BRAO, 9. Aufl. 2023, § 43a Rn. 1 ff.
- Hartung, in: Hartung/Scharmer, Anwaltsberufsrecht (BORA), 7. Aufl. 2024, § 3 BORA Rn. 1 ff.
- Fischer, StGB, 71. Aufl. 2024, § 203 Rn. 1 ff., § 356 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BVerfG, Beschl. v. 12.12.2007 – 1 BvR 1625/06, NJW 2008, 502 (anwaltliche Werbung)
2. BGH, Urt. v. 25.06.2020 – IX ZR 243/18, NJW 2020, 2614 (Reichweite Mandatsgeheimnis bei IT-Auslagerung)
3. BGH-Anwaltssenat, Beschl. v. … – AnwZ (Brfg) …/… (Interessenkollision, „dieselbe Rechtssache")
4. EuGH, Urt. v. 14.09.2010 – Rs. C-550/07 P, ECLI:EU:C:2010:512 (Akzo Nobel — Legal Privilege im EU-Kartellverfahren, nur für unabhängige Anwälte)
5. BGH, Urt. v. 13.05.2014 – VI ZR 192/13, NJW 2014, 2492 (anwaltliche Sorgfalts- und Aufklärungspflicht)

## Ausgabeformat

```
VERMERK — BRAO-Pflichtenprüfung
Kanzlei: <…>           Datum: <TT.MM.JJJJ>
Mandat:   <Bezeichnung anonymisiert>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
    – Mandatsannahme: [ja / ja mit Auflagen / nein]
    – Begründung in einem Satz

IV. Rechtliche Bewertung
    1. Verschwiegenheit § 43a II BRAO / § 2 BORA / § 203 StGB
       – Datenfluss, Auslagerung, Mandanteneinwilligung?
    2. Interessenkollision § 43a IV BRAO / § 3 BORA / § 356 StGB
       – Vorbefassung Sozietät? Konfliktdatenbank-Check
       – „Dieselbe Rechtssache"?
       – Einwilligungsoption?
    3. Sachlichkeit § 43a III / § 44 BRAO
    4. Werbung § 43b BRAO / §§ 6 ff. BORA
    5. Auslagerung § 43e BRAO
       – Drittanbieter, AVV, § 203 IV StGB-Verpflichtung
       – KI-Bezug
    6. Vergütung § 49b BRAO / §§ 3a, 4a RVG
       – Erfolgshonorar-Risiko?
       – Fremdgeld § 43a V BRAO
    7. GwG-Hinweispflichten § 50 BRAO

V. Verfahrensrechtliche Folgen bei Verstoß
   – Rüge § 74 BRAO (1 Monat Anfechtung)
   – Anwaltsgerichtliche Maßnahmen §§ 113 ff., § 114 BRAO
   – Verjährung 5 Jahre § 115 BRAO
   – Strafrechtliche Reflexe §§ 203, 356 StGB
   – Zivilrechtliche Haftung § 280 BGB

VI. Empfehlung
    – konkrete Handlungsschritte (Mandat annehmen / ablehnen / Auflagen)
    – Dokumentation (Konfliktcheck-Protokoll, Mandanteneinwilligung)

VII. Risikoeinstufung
     🟢 / 🟡 / 🔴 mit Begründung

VIII. Quellenverzeichnis
```

## Beispiel (Auszug Gutachtenstil)

**Frage:** Darf Kanzlei K die Verteidigung des Mandanten M übernehmen, wenn ein Sozietätspartner vor zwei Jahren die Gegnerin steuerlich beraten hat?

**Bewertung:** Es liegt eine vorbefasste Sozietät iSv § 43a Abs. 4 BRAO iVm § 3 BORA vor. Die steuerliche Beratung der Gegenseite und das jetzt anstehende Mandat sind in **derselben Rechtssache** verzahnt, wenn die damalig beratene Vermögensstruktur Gegenstand des aktuellen Streits ist. Die Vorbefassung eines Sozietätsmitglieds ist sämtlichen Sozietätsmitgliedern zuzurechnen (§ 3 BORA, h.M.: Henssler, in: Henssler/Prütting, 6. Aufl. 2024, § 3 BORA Rn. 12 `[unverifiziert]`). Eine wechselseitige Einwilligung beider Parteien könnte den Konflikt grundsätzlich heilen (§ 3 Abs. 2 BORA), kommt hier aber wegen offen widerstreitender Interessen praktisch nicht in Betracht. Folge: **Mandatsablehnung**, da andernfalls Verstoß gegen § 43a Abs. 4 BRAO und Strafbarkeitsrisiko nach § 356 StGB.

**Ergebnis:** 🔴 — Mandat ablehnen, Begründung dokumentieren (Konfliktcheck-Protokoll).

## Risiken / typische Fehler

- **Vorbefassung der Sozietät übersehen**, weil das damalige Mandat in einem anderen Aktenzeichen oder einem anderen Büro geführt wurde — § 3 BORA zurechnet beides.
- **Mandanteneinwilligung als Universal-Heilmittel** missverstehen — bei offen widerstreitenden Interessen wirkt sie nicht (§ 3 Abs. 2 BORA, h.M.).
- **KI-Auslagerung ohne § 43e-Vereinbarung und ohne § 203 Abs. 4 StGB-Verpflichtung** — strafbar nach § 203 Abs. 1 Nr. 3 StGB.
- **Erfolgshonorar zugesagt** außerhalb § 4a RVG — Vereinbarung nichtig, RVG-Sätze greifen, ggf. Rückforderung erfolgsbezogen gezahlter Beträge.
- **Werbeversprechen** („Wir setzen Ihren Anspruch durch") — Verstoß gegen § 43b BRAO + § 6 BORA, UWG-Abmahnung möglich.
- **Fremdgeld auf Geschäftskonto** statt Anderkonto — § 43a Abs. 5 BRAO-Verstoß, Anfangsverdacht Untreue § 266 StGB.
- **1-Monatsfrist § 74 BRAO** versäumt — Rüge wird bestandskräftig.
- **Verfolgungsverjährung 5 Jahre § 115 BRAO** bei Dauerverstößen (z. B. dauerhaft unzulässige Werbung) zu früh angenommen — beginnt mit Beendigung des Dauerverstands.
