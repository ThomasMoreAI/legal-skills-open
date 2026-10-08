---
name: eu-richtlinien-umsetzungspruefung-borghei
title: /europarecht:eu-richtlinien-umsetzungspruefung
description: Prüfung von Umsetzung, unmittelbarer Wirkung und richtlinienkonformer Auslegung einer EU-Richtlinie nach Art. 288 AEUV – vertikale unmittelbare Wirkung (Marshall/Faccini Dori), richtlinienkonforme Auslegung (von Colson/Marleasing/Pfeiffer), Francovich-Staatshaftung. Use when ein Mandant sich auf eine nicht oder fehlerhaft umgesetzte Richtlinie berufen will oder eine deutsche Norm auf RL-Konformität geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/europarecht/skills/eu-richtlinien-umsetzungspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: constitutional
language: de
---

# /europarecht:eu-richtlinien-umsetzungspruefung

## Zweck

Der Skill prüft systematisch, ob eine EU-Richtlinie ordnungsgemäß ins deutsche Recht umgesetzt wurde und welche Konsequenzen ein Umsetzungsdefizit hat: **richtlinienkonforme Auslegung** (vorrangig), **unmittelbare Wirkung** (subsidiär, nur vertikal), **Francovich-Staatshaftung** (letztes Mittel). Er liefert ein klares Prüfungsraster für die Praxis vor deutschen Zivil- und Verwaltungsgerichten.

## Eingaben

- konkrete EU-Richtlinie (Titel, RL-Nummer, ABl.-Fundstelle, CELEX)
- Umsetzungsfrist (Art. … RL) und Datum des Fristablaufs
- vermeintliches deutsches Umsetzungsgesetz (Name, Norm, Fundstelle)
- konkretes Auslegungs-/Anwendungsproblem (welche RL-Bestimmung wird wie unzureichend umgesetzt?)
- Konstellation: Bürger gegen Staat (vertikal) oder Bürger gegen Bürger (horizontal)?

## Sub-Agent-Architektur

Researcher liefert AEUV-Normen, EuGH-Leitentscheidungen (van Gend, Marshall, Faccini Dori, von Colson, Marleasing, Pfeiffer, Francovich, Köbler) und Kommentarstellen. Drafter prüft im Gutachtenstil die drei Folgenrichtungen und ordnet das Risiko ein. Reviewer prüft insb. die Abgrenzung vertikal/horizontal und die Grenze "contra legem" der RL-konformen Auslegung.

## Ablauf

### 1. Umsetzungsfrist und Umsetzungsakt

- Wann ist die Umsetzungsfrist (Art. … RL) abgelaufen?
- Gibt es ein nationales Umsetzungsgesetz? Welcher Teil der RL ist gegebenenfalls **nicht** oder **fehlerhaft** umgesetzt?
- Bei richtigen, aber sprachlich abweichenden Umsetzungsakten: Auslegung nach Wortlaut der RL und EuGH-Rspr.

### 2. Richtlinienkonforme Auslegung (Stufe 1, vorrangig)

Nationale Gerichte sind nach Art. 4 III EUV und Art. 288 III AEUV verpflichtet, das nationale Recht **soweit wie möglich** im Lichte des Wortlauts und des Zwecks der Richtlinie auszulegen.

- Grundsatz: EuGH, **von Colson**, Rs. 14/83 (Urt. v. 10.04.1984), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&num=C-14/83)
- Ausweitung: EuGH, **Marleasing**, C-106/89 (Urt. v. 13.11.1990), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-106/89)
- Methodische Grenzen: EuGH, **Pfeiffer**, C-397/01 u.a. (Urt. v. 05.10.2004), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?num=C-397/01&language=de)
- **Grenze**: keine Auslegung **contra legem**; keine Begründung strafrechtlicher Haftung gegen den Bürger durch RL-konforme Auslegung (nulla poena, Art. 7 EMRK).

### 3. Unmittelbare Wirkung (Stufe 2, subsidiär)

Voraussetzungen (EuGH, **van Gend & Loos**, Rs. 26/62; übertragen auf RL in **Marshall**, Rs. 152/84 [Urt. v. 26.02.1986], [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-152/84)):

- Umsetzungsfrist abgelaufen
- RL-Bestimmung ist **hinreichend bestimmt**, **unbedingt** und begründet **subjektive Rechte** des Einzelnen
- Konstellation: **vertikal** (Bürger gegen Mitgliedstaat oder dessen Stellen — funktionaler Staatsbegriff, einschl. öffentlicher Unternehmen)

**Keine** horizontale unmittelbare Wirkung zwischen Privaten — EuGH, **Faccini Dori**, C-91/92 (Urt. v. 14.07.1994), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-91/92). Ausnahme/Korrektur für Allgemeine Grundsätze des Unionsrechts (etwa Verbot der Altersdiskriminierung): EuGH, **Kücükdeveci**, C-555/07 (Urt. v. 19.01.2010), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&num=C-555/07).

### 4. Francovich-Staatshaftung (Stufe 3, ultima ratio)

Voraussetzungen (EuGH, **Francovich**, C-6/90 und C-9/90; konkretisiert in **Brasserie du pêcheur/Factortame**, verb. Rs. C-46/93 und C-48/93 [Urt. v. 05.03.1996], [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?num=C-46/93&language=de)):

1. Die verletzte Norm bezweckt die Verleihung von Rechten an den Einzelnen.
2. Der Verstoß ist **hinreichend qualifiziert**.
3. Zwischen Verstoß und Schaden besteht ein unmittelbarer Kausalzusammenhang.

Anspruchsgrundlage im deutschen Recht: unionsrechtlicher Staatshaftungsanspruch sui generis; verfahrensrechtliche Einbettung über § 839 BGB iVm Art. 34 GG, ohne deren engere Voraussetzungen (insb. nicht das Verschuldenserfordernis) zu übernehmen — st. Rspr. EuGH, vgl. **Köbler**, C-224/01 (Urt. v. 30.09.2003, auch für judikatives Unrecht durch letztinstanzliche Gerichte), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&num=C-224%2F01).

Verjährung: §§ 195, 199 BGB (3 Jahre ab Kenntnis); Klageweg vor deutschen Zivilgerichten.

### 5. Praktische Prüfungsreihenfolge

```
1. RL-konforme Auslegung möglich?  → wenn ja: Stop, anwenden.
2. Wenn nicht (oder contra legem):
   a) Konstellation vertikal + Bestimmtheit/Unbedingtheit/subjektives Recht?
      → unmittelbare Wirkung
   b) Konstellation horizontal?
      → keine unmittelbare Wirkung; Schaden über Francovich
3. Wenn weder a) noch b) hilft: Francovich gegen die BRD
```

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Primärrecht

- [Art. 288 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E288) (Rechtsakte, RL-Definition)
- [Art. 4 Abs. 3 EUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012M004) (Unionstreue)
- [Art. 19 EUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012M019) (Rechtsschutzpflicht)
- [Art. 47 GRCh](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012P047) (effektiver Rechtsschutz)
- [§ 839 BGB](https://www.gesetze-im-internet.de/bgb/__839.html), [Art. 34 GG](https://www.gesetze-im-internet.de/gg/art_34.html) (deutsches Amtshaftungsgerüst für unionsrechtliche Staatshaftung)

### Kommentare

- Ruffert, in: Calliess/Ruffert, EUV/AEUV, 6. Aufl. 2022, Art. 288 AEUV Rn. 1 ff.
- Nettesheim, in: Grabitz/Hilf/Nettesheim, Recht der EU, Stand 2024, Art. 288 AEUV Rn. 1 ff.
- Streinz, in: Streinz, EUV/AEUV, 3. Aufl. 2018, Art. 288 AEUV Rn. 1 ff.
- Detterbeck, Allgemeines Verwaltungsrecht, aktuelle Aufl. (zum unionsrechtlichen Staatshaftungsanspruch)

### Rechtsprechung

1. EuGH, Urt. v. 05.02.1963 – Rs. 26/62, van Gend & Loos (unmittelbare Wirkung Primärrecht), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-26/62&td=ALL)
2. EuGH, Urt. v. 26.02.1986 – Rs. 152/84, Marshall (vertikale unmittelbare Wirkung von RL), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-152/84)
3. EuGH, Urt. v. 14.07.1994 – Rs. C-91/92, Faccini Dori (keine horizontale UW), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-91/92)
4. EuGH, Urt. v. 10.04.1984 – Rs. 14/83, von Colson (RL-konforme Auslegung), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&num=C-14/83)
5. EuGH, Urt. v. 13.11.1990 – Rs. C-106/89, Marleasing, [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-106/89)
6. EuGH, Urt. v. 05.10.2004 – verb. Rs. C-397/01 u.a., Pfeiffer, [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?num=C-397/01&language=de)
7. EuGH, Urt. v. 19.01.2010 – Rs. C-555/07, Kücükdeveci (Allg. Grundsatz), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&num=C-555/07)
8. EuGH, Urt. v. 19.11.1991 – verb. Rs. C-6/90 und C-9/90, Francovich, [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-6/90)
9. EuGH, Urt. v. 05.03.1996 – verb. Rs. C-46/93 und C-48/93, Brasserie du pêcheur/Factortame, [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?num=C-46/93&language=de)
10. EuGH, Urt. v. 30.09.2003 – Rs. C-224/01, Köbler (Staatshaftung für judikatives Unrecht), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&num=C-224%2F01)

## Ausgabeformat

```
GUTACHTEN — RL-Umsetzungsprüfung
Richtlinie: <RL (EU) NNNN/JJJJ, Art. N>
Umsetzungsfrist abgelaufen am: <Datum>

I. Sachverhalt
II. Fragen
III. Kurzantwort
    – RL-konforme Auslegung: [möglich / contra legem]
    – Unmittelbare Wirkung:   [ja, vertikal / nein, horizontal]
    – Francovich-Anspruch:    [tragfähig / nicht tragfähig]

IV. Rechtliche Bewertung
    1. Umsetzungsbefund (Norm-für-Norm-Vergleich)
    2. Stufe 1: Richtlinienkonforme Auslegung
       a) Wortlautgrenze
       b) Zweck der RL
    3. Stufe 2: Unmittelbare Wirkung
       a) Bestimmtheit/Unbedingtheit
       b) Subjektives Recht
       c) Vertikalität (funktionaler Staatsbegriff)
    4. Stufe 3: Francovich-Staatshaftung
       a) Bezweckung subjektiver Rechte
       b) Hinreichend qualifizierter Verstoß
       c) Kausalität
V. Gesamtergebnis
VI. Risiken (🟢/🟡/🔴)
VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Horizontale unmittelbare Wirkung angenommen** — Klassiker; faktisch ausgeschlossen seit Faccini Dori.
- **RL-konforme Auslegung contra legem** — überdehnt den richterlichen Spielraum, verletzt Wortlautgrenze und Gewaltenteilung.
- **Strafbarkeitsbegründung gegen den Bürger** durch RL-konforme Auslegung — unzulässig.
- **Funktionaler Staatsbegriff** verkannt: Auch Kommunen, beliehene Unternehmer und staatlich beherrschte Gesellschaften können "Staat" iSd vertikalen Wirkung sein.
- **Francovich-Verjährung** §§ 195, 199 BGB übersehen.
- **Köbler-Konstellation** (judikatives Unrecht) ohne Vorlage durch letztinstanzliches Gericht — doppeltes Risiko: Vorlagepflichtverletzung + Staatshaftung.
