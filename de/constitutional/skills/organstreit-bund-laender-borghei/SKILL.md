---
name: organstreit-bund-laender-borghei
title: /verfassungsrecht:organstreit-bund-laender
description: Abgrenzung Organstreit (Art. 93 I Nr. 1 GG, §§ 63 ff. BVerfGG), Bund-Länder-Streit (Art. 93 I Nr. 3 GG, §§ 68 ff. BVerfGG) und abstrakte Normenkontrolle (Art. 93 I Nr. 2 GG, §§ 76 ff. BVerfGG) inkl. Antragsberechtigung, Antragsgegenstand und Frist. Use when ein Verfassungsorgan, eine Bundes- oder Landesregierung oder ein Bundestagsdrittel eine Kompetenz- oder Verfahrensfrage vor das BVerfG bringen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verfassungsrecht/skills/organstreit-bund-laender
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: constitutional
language: de
---

# /verfassungsrecht:organstreit-bund-laender

## Zweck

Die drei objektiven Verfahren — Organstreit, Bund-Länder-Streit, abstrakte Normenkontrolle — sehen ähnlich aus, haben aber unterschiedliche Antragsberechtigte, Antragsgegenstände und Fristen. Vor jeder weiteren Prüfung steht daher die **Verfahrenswahl**. Dieser Skill trennt die drei Verfahren sauber und führt die jeweilige Zulässigkeitsprüfung durch.

## Eingaben

- Antragsteller (Verfassungsorgan / Teil eines Verfassungsorgans / Bundesregierung / Landesregierung / Bundestagsdrittel)
- gerügte Maßnahme (Akt eines Verfassungsorgans / Bundesrecht / Landesrecht / Unterlassen)
- behauptete Verletzung (verfassungsrechtliche Kompetenz / Recht aus dem GG / Vereinbarkeit einer Norm mit dem GG)
- Zeitpunkt der Kenntniserlangung

## Sub-Agent-Architektur

Researcher liefert GG, BVerfGG und BVerfG-Rechtsprechung zu den drei Verfahrensarten. Drafter ordnet das Begehren der richtigen Verfahrensart zu und führt die Zulässigkeitsprüfung im Gutachtenstil. Reviewer prüft Fristen, Antragsbefugnis und Subsidiarität gegenüber konkurrierenden Verfahren.

## Ablauf

### 1. Verfahrenswahl

| Verfahren | Norm | Wer | Worum geht es |
|---|---|---|---|
| **Organstreit** | Art. 93 I Nr. 1 GG; §§ 13 Nr. 5, 63–67 BVerfGG | Oberste Bundesorgane oder andere durch GG / Geschäftsordnung mit eigenen Rechten ausgestattete Beteiligte (z. B. Bundestagsfraktion) | Kompetenzstreit / Verletzung verfassungsmäßiger Rechte des Antragstellers durch Maßnahme oder Unterlassen des Antragsgegners |
| **Bund-Länder-Streit** | Art. 93 I Nr. 3 GG; §§ 13 Nr. 7, 68–70 BVerfGG | Bundesregierung / Landesregierung | Meinungsverschiedenheit über Rechte und Pflichten des Bundes und der Länder (insbes. Bundesaufsicht) |
| **Abstrakte Normenkontrolle** | Art. 93 I Nr. 2 GG; §§ 13 Nr. 6, 76–79 BVerfGG | Bundesregierung, Landesregierung, ein Viertel der Mitglieder des Bundestages | Förmliche Überprüfung der Vereinbarkeit von Bundes- oder Landesrecht mit dem GG bzw. mit sonstigem Bundesrecht |

Abgrenzung zur **konkreten Normenkontrolle** (Art. 100 I GG, §§ 80 ff. BVerfGG): dort initiiert das Fachgericht, nicht ein Verfassungsorgan.

### 2. Organstreit (§§ 63–67 BVerfGG)

| Stufe | Maßstab |
|---|---|
| **Parteifähigkeit** | § 63 BVerfGG: Bundespräsident, Bundestag, Bundesrat, Bundesregierung sowie deren Teile, die im GG oder in der Geschäftsordnung mit eigenen Rechten ausgestattet sind (z. B. Fraktionen, einzelne Abgeordnete, Ausschüsse — vgl. [BVerfGE 2, 143](https://www.servat.unibe.ch/dfr/bv002143.html), EVG-Vertrag) |
| **Antragsgegner** | Ebenfalls oberstes Bundesorgan oder dessen Teil |
| **Antragsgegenstand** | § 64 Abs. 1 BVerfGG: Maßnahme oder Unterlassen des Antragsgegners |
| **Antragsbefugnis** | Möglichkeit der Verletzung verfassungsmäßiger Rechte des Antragstellers oder des Organs, dem er angehört |
| **Frist** | § 64 Abs. 3 BVerfGG: sechs Monate nach Bekanntwerden der beanstandeten Maßnahme |
| **Form** | § 64 Abs. 2 BVerfGG: Antrag mit Bezeichnung der Maßnahme und der verletzten Bestimmung des GG |
| **Rechtsschutzbedürfnis** | bei einfacheren Klärungsmöglichkeiten (z. B. Geschäftsordnungsverfahren) sorgfältig zu prüfen |

### 3. Bund-Länder-Streit (§§ 68–70 BVerfGG)

| Stufe | Maßstab |
|---|---|
| **Parteifähigkeit** | § 68 BVerfGG: Bundesregierung und Landesregierung |
| **Antragsgegenstand** | § 69 BVerfGG i.V.m. § 64 BVerfGG: Maßnahme oder Unterlassen, das Rechte und Pflichten des Bundes oder eines Landes betrifft |
| **Antragsbefugnis** | Möglichkeit, dass eigene verfassungsmäßige Rechte / Pflichten aus dem Bund-Länder-Verhältnis verletzt sind |
| **Frist** | § 69 i.V.m. § 64 Abs. 3 BVerfGG: sechs Monate |

Abgrenzung: Streit zwischen **demselben Bundesland**-Organen ist Landesverfassungsstreit (vor Landesverfassungsgericht), nicht Bund-Länder-Streit.

### 4. Abstrakte Normenkontrolle (§§ 76–79 BVerfGG)

| Stufe | Maßstab |
|---|---|
| **Antragsberechtigung** | § 76 Abs. 1 BVerfGG: Bundesregierung, Landesregierung, ein Viertel der Mitglieder des Bundestages |
| **Antragsgegenstand** | Bundesrecht oder Landesrecht (Gesetze, Rechtsverordnungen) |
| **Antragsbefugnis** | Bundesregierung / Landesregierung: Bedenken **oder** Halten für gültig wenn Gericht / Behörde es für unanwendbar hält; Bundestagsdrittel: Meinungsverschiedenheiten oder Zweifel an der Vereinbarkeit mit höherrangigem Recht |
| **Frist** | keine starre Frist, aber **objektives Klarstellungsinteresse** erforderlich |
| **Verhältnis zu anderen Verfahren** | Vorrang konkreter Normenkontrolle / Verfassungsbeschwerde, wenn Individualrechtsschutz möglich |

### 5. Bindungswirkung und Gesetzeskraft

Auch hier gilt **§ 31 BVerfGG**:

- Abs. 1: Bindung aller Verfassungsorgane, Gerichte und Behörden an die Entscheidung.
- Abs. 2: Gesetzeskraft für Entscheidungen nach § 13 Nr. 6 BVerfGG (abstrakte Normenkontrolle) sowie weitere ausdrücklich genannte Verfahren — Veröffentlichung im Bundesgesetzblatt.

Dies ist die **gesetzliche Ausnahme** vom Grundsatz, dass deutsches Recht keine Präjudizienbindung kennt.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [Art. 93 GG](https://www.gesetze-im-internet.de/gg/art_93.html) (Zuständigkeiten des BVerfG)
- [§ 13 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__13.html) (Zuständigkeitskatalog)
- [§ 63 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__63.html) (Parteifähigkeit im Organstreit)
- [§ 64 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__64.html) (Antragsgegenstand, Frist im Organstreit)
- [§ 68 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__68.html) (Bund-Länder-Streit)
- [§ 69 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__69.html) (Verfahren Bund-Länder-Streit)
- [§ 76 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__76.html) (Antrag abstrakte Normenkontrolle)
- [§ 78 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__78.html) (Tenor Nichtigkeit / Unvereinbarkeit)
- [§ 31 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__31.html) (Bindungswirkung, Gesetzeskraft)

### Kommentare

- Bethge, in: Maunz/Schmidt-Bleibtreu/Klein/Bethge, BVerfGG, Loseblatt, § 63 Rn. 1 ff. (Parteifähigkeit Organstreit)
- Pestalozza, Verfassungsprozessrecht, 3. Aufl. 1991, § 7 (Bund-Länder-Streit)
- Schlaich/Korioth, Das Bundesverfassungsgericht, 12. Aufl. 2021, Rn. 87 ff. (Organstreit), Rn. 138 ff. (abstrakte Normenkontrolle), Rn. 119 ff. (Bund-Länder-Streit)
- Stern, Staatsrecht II, § 44 (Organstreit), § 45 (Bund-Länder-Streit)

### Rechtsprechung

1. BVerfG, Urt. v. 05.04.1952 – 2 BvH 1/52, BVerfGE 1, 208 (7,5%-Sperrklausel im schleswig-holsteinischen Landeswahlgesetz; Parteifähigkeit politischer Parteien, Wahlrechtsgleichheit — frühe Linie), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1952-04-05&Aktenzeichen=2%20BvH%201/52)
2. BVerfG, Urt. v. 23.10.1952 – 1 BvB 1/51, BVerfGE 2, 1 (Verbot der SRP — Parteiverbotsverfahren nach Art. 21 II GG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1952-10-23&Aktenzeichen=1%20BvB%201/51)
3. BVerfG, Urt. v. 30.07.1958 – 2 BvF 3, 6/58, [BVerfGE 8, 104](https://www.servat.unibe.ch/dfr/bv008104.html) (abstrakte Normenkontrolle, Volksbefragung Hamburg/Bremen)
4. BVerfG, Urt. v. 14.12.1965 – 1 BvR 413/60 u.a., BVerfGE 19, 206 („Kirchenbausteuer"; Heranziehung juristischer Personen zur Kirchenbausteuer verletzt Art. 2 I GG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1965-12-14&Aktenzeichen=1%20BvR%20413/60)

## Ausgabeformat

```
GUTACHTEN ORGANSTREIT / BUND-LÄNDER-STREIT / ABSTRAKTE NORMENKONTROLLE
<Datum> — <Skill-Mandat-ID>

A. Sachverhalt
   <knapp>

B. Frage / Verfahrenswahl
   Welche Verfahrensart ist statthaft? Welches Verfassungsorgan kann
   was angreifen?

C. Kurzantwort
   <1 Satz>

D. Verfahrenswahl
   1. Organstreit (Art. 93 I Nr. 1 GG, §§ 63 ff. BVerfGG): einschlägig?
   2. Bund-Länder-Streit (Art. 93 I Nr. 3 GG, §§ 68 ff. BVerfGG):
      einschlägig?
   3. Abstrakte Normenkontrolle (Art. 93 I Nr. 2 GG, §§ 76 ff. BVerfGG):
      einschlägig?
   4. Konkurrenz und Vorrang

E. Zulässigkeit des gewählten Verfahrens
   I.   Parteifähigkeit / Antragsberechtigung
   II.  Antragsgegner (soweit relevant)
   III. Antragsgegenstand
   IV.  Antragsbefugnis (Möglichkeit der Rechtsverletzung)
   V.   Frist (§ 64 III BVerfGG bzw. ohne Frist bei abstrakter
        Normenkontrolle)
   VI.  Form (§ 23 I, § 64 II BVerfGG)
   VII. Rechtsschutzbedürfnis / Subsidiarität gegenüber anderen
        Verfahren

F. Begründetheit
   <Maßstab je nach Verfahren — Verletzung verfassungsmäßiger Rechte /
   Vereinbarkeit der Norm mit höherrangigem Recht>

G. Ergebnis
   Verfahren statthaft ✅/❌; Zulässigkeit ✅/❌; Begründetheit ✅/❌

H. Bindung und Tenor (§ 31, § 78 BVerfGG)

I. Risiken / offene Punkte

J. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Falsche Verfahrenswahl** — Bundestagsfraktion macht „Bund-Länder-Streit" geltend, obwohl sie nicht parteifähig ist; statthaft wäre Organstreit.
- **Frist § 64 Abs. 3 BVerfGG übersehen** — sechs Monate ab Bekanntwerden, auch im Bund-Länder-Streit (§ 69 i.V.m. § 64 BVerfGG).
- **Antragsbefugnis bei abstrakter Normenkontrolle** — Bundestagsdrittel-Schwelle (Art. 93 I Nr. 2 GG, § 76 BVerfGG) muss tatsächlich vorliegen.
- **Konkurrenz nicht beachtet** — bei Individualrechtsschutz Vorrang der Verfassungsbeschwerde / konkreten Normenkontrolle.
- **§ 31 BVerfGG fehlinterpretiert** — Gesetzeskraft (§ 31 Abs. 2 BVerfGG) gilt nur für die im Katalog des § 13 Nr. 6, 6a, 11, 12, 14 BVerfGG genannten Verfahren.
- **Landesverfassungsstreit als Bund-Länder-Streit qualifiziert** — Streit zwischen Organen desselben Landes ist Landesverfassungssache.
