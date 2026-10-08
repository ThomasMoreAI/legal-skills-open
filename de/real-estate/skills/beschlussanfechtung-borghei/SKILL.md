---
name: beschlussanfechtung-borghei
title: /wohnungseigentumsrecht:beschlussanfechtung
description: Prüfung der Erfolgsaussicht einer WEG-Beschlussanfechtung nach der WEMoG-Reform – Anfechtungsklage gegen die Gemeinschaft der Wohnungseigentümer § 44 Abs. 2 WEG, Monatsfrist § 45 WEG, Nichtigkeit und Anfechtbarkeit § 23 Abs. 4 WEG, Maßstab der ordnungsmäßigen Verwaltung § 19 WEG. Use when ein Wohnungseigentümer einen Beschluss der Eigentümerversammlung anfechten will oder die Erfolgsaussicht einer Anfechtungsklage geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wohnungseigentumsrecht/skills/beschlussanfechtung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /wohnungseigentumsrecht:beschlussanfechtung

## Zweck

Dieser Skill prüft die **Erfolgsaussicht** einer Beschlussanfechtung nach dem Wohnungseigentumsmodernisierungsgesetz (**WEMoG**, in Kraft seit 01.12.2020). Die Reform hat das Beschlussklagerecht grundlegend umgestaltet: Beschlussklagen sind nach [§ 44 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) seither **gegen die Gemeinschaft der Wohnungseigentümer** zu richten — nicht mehr gegen die übrigen Eigentümer. Geprüft werden Nichtigkeit und Anfechtbarkeit, die Wahrung der Fristen sowie der materielle Maßstab der ordnungsmäßigen Verwaltung.

## Eingaben

- der angefochtene **Beschluss** (Wortlaut, Beschlussart)
- das **Versammlungsprotokoll** (Beschlussfassung, Stimmverhältnis)
- die **Einladung** zur Eigentümerversammlung (Tagesordnung, Ankündigung)
- das **Beschlussdatum** (für die Fristberechnung)
- ggf. Verwaltervertrag, Gemeinschaftsordnung, frühere Beschlüsse

## Sub-Agent-Architektur

- **Researcher** (`../../agents/researcher.md`) liefert die einschlägigen WEG-Normen in der **post-WEMoG-Fassung** sowie verifizierte BGH-Rechtsprechung zur Beschlussanfechtung.
- **Drafter** (`../../agents/drafter.md`) erstellt das Prüfungsergebnis und — bei Erfolgsaussicht — den Entwurf der Anfechtungsklage gegen die Gemeinschaft der Wohnungseigentümer.
- **Reviewer** (`../../agents/reviewer.md`) kontrolliert Fristwahrung, richtigen Beklagten und die Trennung von Nichtigkeit und Anfechtbarkeit.

## Ablauf

### 1. Beschluss und Beschlussart erfassen

Wortlaut des Beschlusses und Beschlussgegenstand festhalten. Beschlussart bestimmen (z. B. Sonderumlage, Jahresabrechnung/Nachschüsse, Verwalterbestellung, bauliche Maßnahme). Die Beschlussart steuert Prüfungsmaßstab und die Frage einer möglichen Teilanfechtung.

### 2. Nichtigkeit oder Anfechtbarkeit (§ 23 Abs. 4 WEG)

Erste Weichenstellung nach [§ 23 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html):

| Kategorie | Voraussetzung | Folge |
|---|---|---|
| **Nichtigkeit** | Verstoß gegen eine **unabdingbare Rechtsvorschrift** (Satz 1) | Beschluss von Anfang an unwirksam — **fristunabhängig** feststellbar |
| **Anfechtbarkeit** | jeder sonstige Rechtsverstoß (Satz 2) | Beschluss bleibt wirksam, bis er **fristgerecht** angefochten und für ungültig erklärt wird |

Die Abgrenzung ist zentral: Ein **nichtiger** Beschluss kann auch nach Ablauf der Anfechtungsfrist mit der Nichtigkeitsklage angegriffen werden; ein nur **anfechtbarer** Beschluss erwächst nach Fristablauf in Bestandskraft.

### 3. Fristen (§ 45 WEG) und richtiger Beklagter (§ 44 Abs. 2 WEG)

Bei Anfechtbarkeit ist die **Anfechtungsfrist** strikt zu wahren. [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html) enthält **zwei materielle Ausschlussfristen**:

- **Klagefrist:** Die Anfechtungsklage ist **binnen eines Monats** nach Beschlussfassung zu **erheben**.
- **Begründungsfrist:** Die Klage ist **binnen zweier Monate** nach Beschlussfassung zu **begründen**.

Beide Fristen sind keine bloßen Ordnungsfristen, sondern materielle Ausschlussfristen — versäumte Anfechtungsfrist heilt den Rechtsverstoß und führt zur Bestandskraft des anfechtbaren Beschlusses.

**Richtiger Beklagter:** Nach [§ 44 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) ist die Beschlussklage **gegen die Gemeinschaft der Wohnungseigentümer** zu richten (post-WEMoG). Eine gegen die übrigen Eigentümer gerichtete Klage adressiert den falschen Beklagten und ist abzuweisen.

### 4. Formelle Anfechtungsgründe (Einberufung/Ankündigung, § 23 Abs. 2 WEG)

Formelle Mängel der Beschlussfassung prüfen:

- **Einberufung:** Ladungsfrist, Ladungsform, Zuständigkeit des Einberufenden.
- **Ankündigung:** Nach [§ 23 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html) ist ein Beschluss nur wirksam, wenn der **Gegenstand bei der Einberufung bezeichnet** war. Ein nicht angekündigter Tagesordnungspunkt begründet regelmäßig die **Anfechtbarkeit** (nicht Nichtigkeit) des darüber gefassten Beschlusses.

### 5. Materielle Prüfung — ordnungsmäßige Verwaltung (§ 19 WEG)

Inhaltlich ist Maßstab die **ordnungsmäßige Verwaltung** nach [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html). Ein Beschluss ist anfechtbar, wenn er nicht ordnungsmäßiger Verwaltung entspricht (z. B. unverhältnismäßige Sonderumlage, sachfremde Erwägungen, Verstoß gegen den Gleichbehandlungsgrundsatz, Überschreitung des Ermessens der Eigentümer).

### 6. Teilanfechtung eines Beschlusses

Ein Beschluss kann auch **in Teilen** angefochten werden, wenn der angegriffene Teil abtrennbar ist und der Restbeschluss eigenständig Bestand haben kann. Auch nach der WEMoG-Reform bleibt die **Teilanfechtung** etwa eines Beschlusses über die Nachschüsse/Abrechnungsspitze möglich (BGH, Urt. v. 11.04.2025 – V ZR 96/24, NJW 2025, 1504 = NZM 2025, 351, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=11.04.2025&Aktenzeichen=V%20ZR%2096/24)). Praktisch relevant bei Jahresabrechnungen, deren einzelne Positionen separat angreifbar sind.

### 7. Ergebnis

Erfolgsaussicht zusammenfassen: Nichtigkeit oder Anfechtbarkeit, Fristwahrung, richtiger Beklagter, durchgreifender formeller/materieller Anfechtungsgrund, Reichweite (Voll- oder Teilanfechtung).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute (post-WEMoG, Stand seit 01.12.2020)

- [§ 44 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) (Beschlussklagen; Abs. 2: Klage gegen die Gemeinschaft der Wohnungseigentümer)
- [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html) (Anfechtungsfrist — ein Monat Klagefrist, zwei Monate Begründungsfrist)
- [§ 23 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html) (Abs. 2 Ankündigung, Abs. 4 Nichtigkeit/Anfechtbarkeit)
- [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (Maßstab der ordnungsmäßigen Verwaltung)

### Rechtsprechung

1. BGH, Urt. v. 11.04.2025 – V ZR 96/24, NJW 2025, 1504 = NZM 2025, 351 (Teilanfechtung eines Beschlusses über Nachschüsse/Abrechnungsspitze auch nach WEMoG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=11.04.2025&Aktenzeichen=V%20ZR%2096/24)

## Risiken / typische Fehler

- **Versäumte Anfechtungsfrist** → Die Monatsfrist des § 45 WEG ist eine materielle Ausschlussfrist; bei Fristablauf wird der anfechtbare Beschluss bestandskräftig. Frühzeitig Klage erheben.
- **falscher Beklagter** → Klage gegen die übrigen Eigentümer statt gegen die Gemeinschaft der Wohnungseigentümer (§ 44 Abs. 2 WEG, WEMoG-Änderung) führt zur Abweisung.
- **Nichtigkeit mit Anfechtbarkeit verwechselt** → Bei bloßer Anfechtbarkeit hilft keine fristunabhängige Nichtigkeitsklage; umgekehrt verfällt ein nichtiger Beschluss nicht durch Fristablauf.
- **Alte Rechtslage angewandt** → Vor der WEMoG-Reform geltende Numerierung und Beklagtenstellung nicht mehr verwenden; durchgängig die post-WEMoG-Fassung prüfen.
- **Vollanfechtung statt Teilanfechtung** → Bei abtrennbaren Positionen genügt eine Teilanfechtung; eine unnötige Vollanfechtung kann das Kosteninteresse verfehlen.

## Ausgabeformat

```
ERFOLGSAUSSICHT — WEG-BESCHLUSSANFECHTUNG (post-WEMoG)

1. Beschluss
   - Gegenstand / Beschlussart: <…>
   - Beschlussdatum: <…>

2. Nichtigkeit vs. Anfechtbarkeit (§ 23 Abs. 4 WEG)
   - Einordnung: [ ] nichtig  [ ] anfechtbar
   - Begründung: <…>

3. Fristen & Beklagter
   - Anfechtungsfrist (§ 45 WEG): Klage 1 Monat / Begründung 2 Monate — gewahrt? <…>
   - Beklagter (§ 44 Abs. 2 WEG): Gemeinschaft der Wohnungseigentümer

4. Formelle Anfechtungsgründe (§ 23 Abs. 2 WEG)
   - Einberufung / Ankündigung: <…>

5. Materielle Prüfung (§ 19 WEG)
   - ordnungsmäßige Verwaltung: <…>

6. Teilanfechtung
   - abtrennbarer Teil? Reichweite: <…>

7. Ergebnis
   - Erfolgsaussicht: <hoch / offen / gering> — <Begründung>
```
