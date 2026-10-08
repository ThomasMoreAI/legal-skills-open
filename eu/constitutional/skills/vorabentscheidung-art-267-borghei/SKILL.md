---
name: vorabentscheidung-art-267-borghei
title: /europarecht:vorabentscheidung-art-267
description: Prüfung der Vorlagepflicht eines deutschen Gerichts nach Art. 267 AEUV und Entwurf der Vorlagefrage an den EuGH – CILFIT/acte clair/acte éclairé, fakultative Vorlage Art. 267 II, BVerfG-Kontrolle über Art. 101 I 2 GG. Use when ein deutsches Gericht in letzter oder vorletzter Instanz vor einer auslegungsbedürftigen Norm des Unionsrechts steht oder ein Mandant die unterbliebene Vorlage rügen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/europarecht/skills/vorabentscheidung-art-267
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: constitutional
language: de
---

# /europarecht:vorabentscheidung-art-267

## Zweck

Der Skill prüft, ob ein deutsches Gericht zur Vorlage an den EuGH **verpflichtet** (Art. 267 III AEUV) oder lediglich **berechtigt** (Art. 267 II AEUV) ist, und unterstützt beim Entwurf des Vorlagebeschlusses. Er adressiert zugleich die verfassungsrechtliche Folgenseite einer unterbliebenen Vorlage durch das letztinstanzliche Gericht (Art. 101 I 2 GG, BVerfG-Beschwerde).

## Eingaben

- Verfahrensstand (Instanz, Gericht, Aktenzeichen, ggf. Verfahrensart)
- konkrete unionsrechtliche Norm, deren Auslegung streitig ist (Art. AEUV, EUV, GRCh, oder Sekundärrechtsakt mit CELEX)
- Sachverhalt mit Bezug zur streitigen Auslegungsfrage
- bisherige EuGH-Rspr. zur Norm (sofern bekannt)
- Position des Mandanten: prozessführende Partei, die Vorlage anregt, oder Partei, die unterbliebene Vorlage rügen will

## Sub-Agent-Architektur

Researcher liefert AEUV-Statute, EuGH-Leitentscheidungen (CILFIT, Da Costa, Consorzio Italian Management) und BVerfG-Rechtsprechung (Solange II, Honeywell, PSPP) sowie Kommentarstellen. Drafter prüft die Vorlagepflicht in Gutachtenstil, entwirft die Vorlagefrage und ggf. den Vorlagebeschluss-Tenor. Reviewer prüft, ob CILFIT sauber abgearbeitet und Art. 101 I 2 GG adressiert ist.

## Ablauf

### 1. Anwendungsbereich des Unionsrechts

Vor jeder weiteren Prüfung klären: Liegt überhaupt eine Auslegungsfrage des Unionsrechts vor (Art. 267 I lit. a, b AEUV)? Bei reiner Anwendung nationaler Vorschriften ohne Unionsrechtsbezug ist Art. 267 AEUV nicht eröffnet.

### 2. Vorlageberechtigung (Art. 267 II AEUV)

Jedes Gericht eines Mitgliedstaats darf vorlegen, wenn es die Entscheidung über die unionsrechtliche Frage für seine Entscheidung für erforderlich hält. Maßstab der **Entscheidungserheblichkeit** ist großzügig; der EuGH lehnt die Beantwortung nur bei offensichtlicher Irrelevanz oder hypothetischer Frage ab (EuGH, Foglia/Novello, Rs. 104/79 [Urt. v. 11.03.1980] und Rs. 244/80 [Urt. v. 16.12.1981], [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=en&num=C-104/79)).

### 3. Vorlagepflicht (Art. 267 III AEUV)

Pflicht trifft Gerichte, deren Entscheidung nicht mit Rechtsmitteln des innerstaatlichen Rechts angefochten werden können — funktionaler Begriff der letzten Instanz (BVerfG-Linie; vgl. Art. 101 I 2 GG-Rechtsprechung). Beispiele: BGH, BVerwG, BFH, BSG, BAG idR; aber auch ein OLG, wenn Nichtzulassungsbeschwerde gem. § 544 ZPO bzw. Revision unstatthaft ist.

### 4. CILFIT-Ausnahmen (acte clair / acte éclairé)

Eine Vorlage entfällt ausnahmsweise, wenn (EuGH, CILFIT, Rs. 283/81 [Urt. v. 06.10.1982], [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-283/81); jüngst präzisiert in **Consorzio Italian Management**, C-561/19 [Urt. v. 06.10.2021], [curia.europa.eu](https://curia.europa.eu/juris/documents.jsf?num=C-561/19)):

1. die Frage nicht entscheidungserheblich ist, oder
2. die Frage bereits Gegenstand einer Auslegung durch den EuGH war (**acte éclairé**), oder
3. die richtige Anwendung des Unionsrechts derart offenkundig ist, dass keinerlei Raum für vernünftige Zweifel besteht (**acte clair**) — und zwar so offenkundig auch für die Gerichte anderer Mitgliedstaaten und den EuGH selbst.

Das letztinstanzliche Gericht muss begründen, **welche** Ausnahme greift; Pauschalverneinungen tragen nicht.

### 5. Verfassungsrechtliche Folgenseite

Verletzt das letztinstanzliche Gericht die Vorlagepflicht **willkürlich** oder **unhaltbar**, verstößt es gegen den Anspruch auf den gesetzlichen Richter (Art. 101 I 2 GG). Maßstab: BVerfG, **Honeywell** (Beschl. v. 06.07.2010, 2 BvR 2661/06, BVerfGE 126, 286, [bverfg.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2010/07/rs20100706_2bvr266106.html)); weiterentwickelt in **PSPP** (Urt. v. 05.05.2020, 2 BvR 859/15 u.a., BVerfGE 154, 17, [bverfg.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2020/05/rs20200505_2bvr085915.html)). Folge: Verfassungsbeschwerde gegen das letztinstanzliche Urteil.

### 6. Entwurf der Vorlagefrage

Die Frage muss (vgl. EuGH-Empfehlungen für Vorabentscheidungsersuchen, ABl. 2019 C 380/1):

- abstrakt formuliert sein, nicht als Subsumtionsbitte
- die ausgelegte Norm präzise benennen
- den Sachverhaltskern in einem knappen Absatz darstellen
- die einschlägigen nationalen Vorschriften zitieren
- bisherige EuGH-Rspr. anführen, soweit der vorlegende Senat sie für nicht ausreichend hält

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Primär- und Verfahrensrecht

- [Art. 267 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E267) (Vorabentscheidungsverfahren)
- [Art. 19 EUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012M019) (Rechtsschutzpflicht der Gerichte)
- [Art. 4 Abs. 3 EUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012M004) (Unionstreue)
- [Art. 47 GRCh](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012P047) (effektiver Rechtsschutz)
- [Art. 101 Abs. 1 S. 2 GG](https://www.gesetze-im-internet.de/gg/art_101.html) (gesetzlicher Richter)
- EuGH-Satzung; EuGH-Verfahrensordnung; Empfehlungen für Vorabentscheidungsersuchen, ABl. 2019 C 380/1

### Kommentare

- Wegener, in: Calliess/Ruffert, EUV/AEUV, 6. Aufl. 2022, Art. 267 AEUV Rn. 1 ff.
- Karpenstein, in: Grabitz/Hilf/Nettesheim, Recht der EU, Stand 2024, Art. 267 AEUV Rn. 1 ff.
- Streinz, in: Streinz, EUV/AEUV, 3. Aufl. 2018, Art. 267 AEUV Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 06.10.1982 – Rs. 283/81, CILFIT (acte clair-Kriterien), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?language=de&jur=C,T,F&num=C-283/81)
2. EuGH, Urt. v. 27.03.1963 – verb. Rs. 28–30/62, Da Costa (acte éclairé), [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:61962CJ0028)
3. EuGH, Urt. v. 06.10.2021 – Rs. C-561/19, Consorzio Italian Management (Präzisierung CILFIT), [curia.europa.eu](https://curia.europa.eu/juris/documents.jsf?num=C-561/19)
4. BVerfG, Beschl. v. 06.07.2010 – 2 BvR 2661/06, BVerfGE 126, 286 (Honeywell), [bverfg.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2010/07/rs20100706_2bvr266106.html)
5. BVerfG, Urt. v. 05.05.2020 – 2 BvR 859/15 u.a., BVerfGE 154, 17 (PSPP), [bverfg.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2020/05/rs20200505_2bvr085915.html)

## Ausgabeformat

```
GUTACHTEN — Vorlagepflicht Art. 267 AEUV
Verfahren: <Gericht, Az., Instanz>

I. Sachverhalt (knapp)
II. Frage(n) der Auslegung des Unionsrechts
III. Kurzantwort
    – Vorlagepflicht: [ja / nein / fakultativ nach Abs. 2]
    – Empfehlung: [Vorlage / kein Vorlagebedürfnis]

IV. Rechtliche Bewertung
    1. Anwendungsbereich Unionsrecht
    2. Vorlageberechtigung Art. 267 II AEUV
    3. Vorlagepflicht Art. 267 III AEUV
       a) Letztinstanzlichkeit
       b) CILFIT-Ausnahmen
          – acte éclairé?  (Belegstellen)
          – acte clair?    (Begründung der Offenkundigkeit)
    4. Verfassungsrechtliche Folgen bei Pflichtverletzung
       (Art. 101 I 2 GG, BVerfG-Beschwerde)

V. Entwurf der Vorlagefrage
    "Ist Art. X der RL/VO YYYY/JJ dahin auszulegen, dass …?"

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Pauschale Verneinung der Vorlagepflicht** mit "acte clair" ohne Auseinandersetzung mit anderssprachigen Fassungen und der EuGH-Rspr. — willkürliche Vorlagepflicht-Verneinung, Art. 101 I 2 GG-Verstoß.
- **Vorlagefrage als Subsumtionsbitte** ("Ist der Mandant Verbraucher iSv …?") — der EuGH legt aus, er subsumiert nicht.
- **Sachverhalt unvollständig**, sodass der EuGH die Frage als hypothetisch zurückweist (Foglia-Linie).
- **Übersehen der GRCh-Anwendbarkeit** bei Durchführung von Unionsrecht (Art. 51 I GRCh).
- **Verkennen, dass auch ein OLG letztinstanzlich sein kann**, wenn Revision/Nichtzulassungsbeschwerde unstatthaft.
