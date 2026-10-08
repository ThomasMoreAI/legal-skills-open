---
name: fao-fortbildungsnachweis-borghei
title: /berufsrecht-anwaltschaft:fao-fortbildungsnachweis
description: Nachweis der Fortbildungspflicht nach § 15 FAO (15 Zeitstunden pro Jahr je Fachgebiet, kumulativ bei Mehrfach-Fachanwaltschaft) und Verteidigung gegen Widerruf der Fachanwaltsbezeichnung nach § 25 FAO. Use when die RAK einen Stichproben-Nachweis fordert, ein Fachanwalt die Vollständigkeit seiner Fortbildung prüfen will, oder ein Widerrufsbescheid wegen unterlassener Fortbildung anzufechten ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/berufsrecht-anwaltschaft/skills/fao-fortbildungsnachweis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /berufsrecht-anwaltschaft:fao-fortbildungsnachweis

## Zweck

Der Skill prüft, ob ein Fachanwalt die Fortbildungspflicht des § 15 FAO erfüllt hat, listet anerkennungsfähige und nicht anerkennungsfähige Formate auf und entwirft die Stellungnahme an die zuständige Rechtsanwaltskammer (RAK) bzw. die Klagebegründung gegen einen Widerrufsbescheid nach § 25 FAO. Er erfasst die kumulative Pflicht bei Mehrfach-Fachanwaltschaft und die Grenzen des § 15 Abs. 4 FAO zum Selbststudium.

## Eingaben

- Fachanwaltsbezeichnung(en) des Mandanten (z. B. Arbeitsrecht, Steuerrecht, …)
- Kalenderjahr / Berichtszeitraum (i.d.R. Kalenderjahr)
- Aufstellung der absolvierten Fortbildung mit Format, Stundenumfang, Veranstalter, Bescheinigung
- Eigene Lehr-/Dozenten- oder Publikationstätigkeit (§ 15 Abs. 3 FAO)
- Stand des RAK-Verfahrens (Stichproben-Anforderung, Anhörung, Widerrufsbescheid)
- ggf. Anhörungsfrist / Klagefrist VwGO iVm § 112c BRAO

## Sub-Agent-Architektur

Researcher liefert FAO-Normen, BGH-Anwaltssenat-Rspr. zu anerkennungsfähigen Formaten und § 25 FAO-Widerruf, Standardkommentar Offermann-Burckart sowie BRAK-Mitteilungen zur Anerkennungspraxis (Online-Veranstaltungen seit 2020 — Übergangs-/Dauerpraxis `[unverifiziert]`). Drafter erstellt Nachweis-Aufstellung und Stellungnahme an RAK bzw. Klagebegründung. Reviewer prüft Stundenrechnung (kumulativ je Fachgebiet), Bescheinigungs-Vollständigkeit, Selbststudium-Grenze § 15 Abs. 4 FAO und Anfechtungsfristen.

## Ablauf

### 1. Pflichtumfang § 15 Abs. 1 FAO

**15 Zeitstunden pro Kalenderjahr je Fachgebiet.** Bei Mehrfach-Fachanwaltschaft kumulativ — wer Fachanwalt für Arbeits- **und** Steuerrecht ist, schuldet 30 Stunden pro Jahr, aufgeteilt nach Fachgebieten (BGH-Anwaltssenat-Linie `[unverifiziert]`). Eine fachgebietsübergreifende Veranstaltung kann anteilig auf mehrere Fachgebiete angerechnet werden, wenn der Inhalt jeweils einschlägig ist und die Aufteilung in der Bescheinigung ausgewiesen ist.

### 2. Anerkennungsfähige Formate § 15 Abs. 2–3 FAO

- **Hörende Teilnahme** an Lehrgängen / Fortbildungsveranstaltungen mit Teilnahmebescheinigung (Abs. 2)
- **Dozierende Tätigkeit** (Abs. 3) — Vorbereitung und Vortrag werden anerkannt; in der Praxis: Vortragsstunde + angemessene Vorbereitungsstunden (Faustregel: 1 Vortragsstunde = 2–3 Vorbereitungsstunden, einzelfallabhängig)
- **Wissenschaftliche Publikation** (Abs. 3) — einschlägige Aufsätze; Anrechnung nach Umfang und Tiefe (RAK-Praxis variabel `[unverifiziert]`)
- **Selbststudium § 15 Abs. 4 FAO** — maximal die Hälfte der Pflichtstunden (also bis zu 7,5 Std./Fachgebiet), mit Lernerfolgskontrolle

**Nicht anerkennungsfähig** sind reine Werbeveranstaltungen, Verkaufsschulungen, allgemeine Kanzleimanagement-Schulungen ohne fachlichen Schwerpunkt.

### 3. Online-Veranstaltungen

Seit 2020 hat sich die Anerkennung von Online-Lehrgängen mit interaktivem Element fest etabliert; reine Aufzeichnungen ohne Interaktionsmöglichkeit fallen unter § 15 Abs. 4 FAO (Selbststudium) mit Halbierungs-Grenze `[unverifiziert – prüfen in BRAK-Mitteilungen und juris]`. Bescheinigung muss Veranstaltungsformat, Stundenzahl und Anwesenheits-/Lernerfolgskontrolle ausweisen.

### 4. Nachweis ggü. RAK

Die Pflicht zur **unaufgeforderten** Vorlage besteht nicht (h.M.); die RAK fordert Nachweise stichprobenartig oder anlassbezogen ein. Bei Anforderung:

- Aufstellung aller Veranstaltungen pro Fachgebiet
- Bescheinigungen im Original / Kopie
- Bei dozierender Tätigkeit: Veranstaltungs-Programm + ggf. Manuskript
- Bei Publikation: Belegexemplar
- Frist setzt RAK üblicherweise 4 Wochen — verlängerbar

### 5. Folgen unzureichender Fortbildung — § 25 FAO

Bei nicht erfüllter Pflicht **kann** die RAK die Fachanwaltsbezeichnung **widerrufen** (§ 25 Abs. 1 FAO; gebundene Entscheidung mit eingeschränktem Ermessen `[unverifiziert]`). Verhältnismäßigkeitsprüfung ist Pflicht — Nachholung im laufenden Jahr kann den Widerruf abwenden, wenn die RAK die Möglichkeit einräumt.

Verfahrensrechtlich:

- Anhörung (§ 28 VwVfG iVm § 32 BRAO)
- Widerrufsbescheid als Verwaltungsakt
- **Klage zum Anwaltsgerichtshof** (§ 112c BRAO iVm VwGO; einmonatige Klagefrist § 74 VwGO)
- Aufschiebende Wirkung der Klage (§ 80 Abs. 1 VwGO) — i.d.R. gegeben, soweit kein Sofortvollzug

### 6. Erneute Verleihung nach Widerruf

Nach Widerruf ist eine erneute Verleihung möglich, sobald die Voraussetzungen (insb. erneute praktische Erfahrungen § 5 FAO und Lehrgang § 4 FAO ggf. ergänzt) wieder vorliegen. Hohe Hürde, daher Widerrufsverteidigung ernst nehmen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute / Satzung

- [§ 43c BRAO](https://www.gesetze-im-internet.de/brao/__43c.html) (Führung der Fachanwaltsbezeichnung)
- [§ 2 FAO](https://www.brak.de/fuer-anwaelte/berufsrecht/fao/) (Fachgebiete)
- [§ 4 FAO](https://www.brak.de/fuer-anwaelte/berufsrecht/fao/) (Erwerb)
- [§ 5 FAO](https://www.brak.de/fuer-anwaelte/berufsrecht/fao/) (besondere praktische Erfahrungen)
- [§ 14 FAO](https://www.brak.de/fuer-anwaelte/berufsrecht/fao/) (Lehrgang)
- [§ 15 FAO](https://www.brak.de/fuer-anwaelte/berufsrecht/fao/) (Fortbildungspflicht)
- [§ 25 FAO](https://www.brak.de/fuer-anwaelte/berufsrecht/fao/) (Widerruf Fachanwaltsbezeichnung)
- [§ 112c BRAO](https://www.gesetze-im-internet.de/brao/__112c.html) (Verfahren am AGH, VwGO-Verweisung)
- [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html) (Klagefrist 1 Monat)

### Kommentare

- Offermann-Burckart, Fachanwalt werden und bleiben, 5. Aufl. 2023, § 15 FAO Rn. 1 ff., § 25 FAO Rn. 1 ff.
- Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 43c Rn. 1 ff.; § 15 FAO Rn. 1 ff.
- Träger, in: Feuerich/Weyland, BRAO, 11. Aufl. 2024, § 43c BRAO Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online/BRAK-Mitteilungen]`)

1. BGH-Anwaltssenat, Beschl. v. … – AnwZ (Brfg) …/…, NJW JJJJ, S. (Anerkennung dozierender Tätigkeit nach § 15 Abs. 3 FAO)
2. BGH-Anwaltssenat, Beschl. v. … – AnwZ (Brfg) …/…, BRAK-Mitt. JJJJ, S. (Widerruf § 25 FAO bei Unterschreitung)
3. AGH Berlin / München, Urt. … (Verhältnismäßigkeit des Widerrufs)
4. BVerfG, Beschl. v. … – 1 BvR …, NJW JJJJ, S. (Art. 12 GG / Fachanwaltsbezeichnung)

## Ausgabeformat

```
NACHWEIS / STELLUNGNAHME — § 15 FAO
Fachanwaltsbezeichnung(en): <…>     Berichtsjahr: <JJJJ>
RAK: <…>                            Datum: <TT.MM.JJJJ>

I. Sachverhalt
   - Fachanwaltsbezeichnungen, Verleihungsdatum
   - Anlass der Prüfung (Stichprobe / Anhörung / Widerrufsbescheid)

II. Pflichtumfang § 15 FAO
    – 15 Std. × Anzahl Fachgebiete = <X> Std./Jahr

III. Aufstellung der Fortbildung (je Fachgebiet)
     Fachgebiet 1: <Bezeichnung>
       Datum | Format | Veranstalter | Stunden | Bescheinigung
       ...
     Summe: <X> Std.
     Fachgebiet 2: <…>

IV. Subsumtion
    – Hörende Teilnahme (Abs. 2): <…>
    – Dozierende Tätigkeit (Abs. 3): <…>
    – Publikation (Abs. 3): <…>
    – Selbststudium (Abs. 4, Halbierungs-Grenze): <…>

V. Ergebnis
   – Pflicht erfüllt / teilweise erfüllt / nicht erfüllt
   – Bei Lücke: Nachholmöglichkeit im Berichts- oder Folgejahr

VI. Bei Widerrufsbescheid § 25 FAO:
    – Anfechtung zum AGH (§ 112c BRAO, § 74 VwGO — 1 Monat)
    – Aufschiebende Wirkung § 80 VwGO
    – Verhältnismäßigkeitsargumente, Nachholangebot

VII. Risikoeinstufung
     🟢 / 🟡 / 🔴 mit Begründung

VIII. Quellenverzeichnis
```

## Beispiel (Auszug Gutachtenstil)

**Sachverhalt:** Mandant ist Fachanwalt für Arbeitsrecht und für Steuerrecht. Im Berichtsjahr 2024 hat er 12 Stunden Präsenzlehrgang Arbeitsrecht, 8 Stunden Online-Veranstaltung Arbeitsrecht (mit Lernerfolgskontrolle), zwei Aufsätze (je 20 Manuskriptseiten) im Arbeitsrecht sowie 9 Stunden Präsenzlehrgang Steuerrecht absolviert.

**Bewertung:** Im **Arbeitsrecht** liegen aus hörender Teilnahme 12 + 8 = 20 Stunden vor; die Pflicht von 15 Stunden ist erfüllt (§ 15 Abs. 1, 2 FAO). Die zwei Aufsätze nach § 15 Abs. 3 FAO sind nicht mehr stundenwirksam erforderlich, sollten aber zum Nachweis vorgelegt werden, da die RAK in Zweifelsfällen die Anrechnung der Online-Stunden prüft. Im **Steuerrecht** liegen nur 9 Stunden vor — **Unterschreitung um 6 Stunden**. Der Mandant muss diese Stunden im Berichtsjahr noch nachholen oder — wenn das nicht mehr möglich ist — die RAK um eine Nachholfrist im Folgejahr bitten und auf Verhältnismäßigkeit (§ 25 FAO) abstellen. Bei Widerruf wäre die Klage zum AGH binnen 1 Monat (§ 112c BRAO iVm § 74 VwGO) zu erheben.

**Ergebnis:** 🟡 — Pflicht im Arbeitsrecht erfüllt, im Steuerrecht Lücke; Nachholung priorisieren, ggf. RAK-Stellungnahme.

## Risiken / typische Fehler

- **Kumulative Pflicht bei Mehrfach-Fachanwaltschaft übersehen** — 15 Std. **je** Fachgebiet, nicht 15 Std. insgesamt.
- **Online-Veranstaltungen ohne Lernerfolgskontrolle** als Präsenz-Äquivalent gewertet — fallen unter § 15 Abs. 4 FAO mit Halbierungs-Grenze.
- **Selbststudium-Stunden über die Hälfte hinaus** angesetzt — § 15 Abs. 4 FAO begrenzt.
- **Bescheinigung ohne Veranstalter-Angabe / Stundenzahl / Datum** — von RAK nicht akzeptiert.
- **Dozierende Tätigkeit ohne dokumentierte Vorbereitung** — Vorbereitungsstunden ggf. nicht anerkannt.
- **Anhörungs-/Klagefrist § 74 VwGO (1 Monat) verstrichen** — Widerrufsbescheid bestandskräftig, Fachanwaltsbezeichnung verloren.
- **Werbung mit verlorener Fachanwaltsbezeichnung** nach Widerruf — Verstoß gegen § 43b BRAO + § 6 BORA + § 5 UWG.
