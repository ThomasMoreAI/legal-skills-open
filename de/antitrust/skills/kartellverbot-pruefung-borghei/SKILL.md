---
name: kartellverbot-pruefung-borghei
title: /kartellrecht:kartellverbot-pruefung
description: Subsumtion einer Vereinbarung, eines Beschlusses oder einer abgestimmten Verhaltensweise unter das Kartellverbot § 1 GWB / Art. 101 AEUV – Unternehmens- und Vereinbarungsbegriff, Wettbewerbsbeschränkung als Zweck (Hardcore) oder Wirkung, Spürbarkeit (De-minimis), Vertikal-GVO 2022/720-Sicherheitshafen, Einzelausnahme § 2 GWB / Art. 101 III AEUV. Use when ein Liefer-, Vertriebs-, Kooperations- oder Lizenzvertrag oder eine horizontale Absprache kartellrechtlich zu bewerten ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kartellrecht/skills/kartellverbot-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: antitrust
language: de
---

# /kartellrecht:kartellverbot-pruefung

## Zweck

Der Skill prüft, ob eine Vereinbarung, ein Beschluss einer Unternehmensvereinigung oder eine abgestimmte Verhaltensweise gegen das Kartellverbot § 1 GWB bzw. Art. 101 I AEUV verstößt, und ob ein Sicherheitshafen (De-minimis-Bekanntmachung; Vertikal-GVO 2022/720; FuE-GVO 2023/1066; Spezialisierungs-GVO) oder die Einzelausnahme § 2 GWB / Art. 101 III AEUV greift. Er adressiert die zivilrechtliche Folgenseite (Nichtigkeit § 134 BGB iVm § 1 GWB), das Bußgeldrisiko §§ 81 ff. GWB und die private Schadensersatzhaftung §§ 33 ff. GWB.

## Eingaben

- Vertragstext oder Beschreibung der Absprache / des Verhaltens (horizontal vs. vertikal)
- Beteiligte Unternehmen, deren Tätigkeit und ihre **Marktanteile** auf den betroffenen Märkten
- Zwischenstaatlichkeitsbezug (grenzüberschreitende Auswirkung iSv Art. 101 AEUV)
- Vorhandensein etwaiger Hardcore-Beschränkungen (Preis, Markt, Mengen, Kunden, Submission, absoluter Gebietsschutz)
- Bei Einzelausnahme-Plädoyer: Effizienzgewinne, Verbraucherbeteiligung, Unerlässlichkeit, Restwettbewerb

## Sub-Agent-Architektur

Researcher liefert § 1, § 2 GWB, Art. 101 AEUV, Vertikal-GVO 2022/720, FuE-/Spezialisierungs-GVO 2023, De-minimis-Bekanntmachung, einschlägige EuGH-Leitentscheidungen (STM, Allianz Hungária, Cartes Bancaires, Generics, Coty), BGH-Kartellsenat-Rspr. und Kommentarstellen (Immenga/Mestmäcker, Langen/Bunte). Drafter führt die vierstufige Subsumtion durch (Tatbestand → Spürbarkeit/De-minimis → GVO-Sicherheitshafen → Einzelausnahme). Reviewer prüft Hardcore-Identifikation, GVO-Marktanteilsschwelle und Vollständigkeit der vier kumulativen Voraussetzungen des Art. 101 III AEUV / § 2 GWB.

## Ablauf

### 1. Anwendungsbereich

- **§ 1 GWB**: Vereinbarung/Beschluss/abgestimmtes Verhalten mit Wettbewerbsbeschränkung im Inland.
- **Art. 101 AEUV**: zusätzlich **Eignung zur Beeinträchtigung des zwischenstaatlichen Handels**. Bei Zwischenstaatlichkeit gilt Art. 3 VO 1/2003: nationale Behörden müssen Art. 101 anwenden, dürfen bei Vereinbarungen nicht strenger sein.

### 2. Tatbestandsmerkmale

1. **Unternehmensbegriff**: jede eine wirtschaftliche Tätigkeit ausübende Einheit (funktional, konzernweit — "single economic entity"; rein konzerninterne Vereinbarungen sind nicht erfasst).
2. **Vereinbarung / Beschluss / abgestimmtes Verhalten** — Abgrenzung zu einseitigem Verhalten (Art. 102) wesentlich.
3. **Wettbewerbsbeschränkung**:
   - **Zweckbeschränkung** ("by object"): Erfahrungssatz wettbewerbsschädigender Wirkung; insbesondere Hardcore (Preisabsprachen, Markt-/Kundenaufteilung, Mengenkontingente, Submissionsabsprachen, absoluter Gebietsschutz). Keine Wirkungsanalyse nötig (EuGH, Urt. v. 11.09.2014 – C-67/13 P, Groupement des cartes bancaires, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2014-09-11&Aktenzeichen=C-67/13): enge Auslegung, wirtschaftlicher Kontext ist einzubeziehen; EuGH, Urt. v. 30.01.2020 – C-307/18, Generics (UK) u.a., [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-01-30&Aktenzeichen=C-307/18): Pay-for-Delay als Zweck).
   - **Wirkungsbeschränkung** ("by effect"): Marktanalyse mit kontrafaktischem Szenario.
4. **Spürbarkeit**: De-minimis-Bekanntmachung der KOM (ABl. 2014 C 291/1):
   - horizontal: kombinierter Marktanteil ≤ **10 %**;
   - vertikal: jeweils ≤ **15 %**;
   - aber **niemals** bei Kernbeschränkungen.

### 3. Vertikal-GVO 2022/720-Sicherheitshafen

Vertikalvereinbarung iSv Art. 1 lit. a Vertikal-GVO ist freigestellt, wenn:

- Marktanteil **jeder** Partei auf dem relevanten Markt **≤ 30 %** (Art. 3);
- **keine Kernbeschränkung** Art. 4 (Preisbindung zweiter Hand, absoluter Gebietsschutz mit Ausnahmen, Beschränkung des aktiven/passiven Verkaufs an Endverbraucher, Selektivvertriebs-spezifische Verbote);
- nicht freigestellte Beschränkungen Art. 5 (Wettbewerbsverbote > 5 Jahre, nachvertragliche Wettbewerbsverbote > 1 Jahr, Markenausschluss-Bestimmungen in Selektivvertrieb) gesondert nichtig, aber Restvertrag bleibt.

Sonderfragen:

- Online-Vertriebsbeschränkungen: Pauschalverbot Drittplattformen — nur in Luxus-Selektivvertrieb möglich (EuGH, Urt. v. 06.12.2017 – C-230/16, Coty Germany, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2017-12-06&Aktenzeichen=C-230/16));
- Doppelvertrieb (Hersteller verkauft selbst über eigene Kanäle): Informationsaustausch geregelt in Art. 2 IV–V;
- Most-Favoured-Customer-/Best-Price-Klauseln: enge Paritätsklauseln zulässig, weite untersagt (Art. 5 I lit. d).

Andere relevante GVOen:

- FuE-GVO **2023/1066** (Sicherheitshafen für FuE-Kooperationen; Marktanteilsschwelle 25 % horizontal);
- [Spezialisierungs-GVO **2023/1067**](https://eur-lex.europa.eu/legal-content/DE/ALL/?uri=CELEX:32023R1067);
- Technologietransfer-GVO **316/2014**.

### 4. Einzelausnahme § 2 GWB / Art. 101 III AEUV

Vier **kumulative** Voraussetzungen (Selbstveranlagung — Legalausnahmesystem seit VO 1/2003):

1. **Effizienzgewinne** (objektiv messbar — Kostensenkung, Innovation, Qualität);
2. **angemessene Verbraucherbeteiligung** (Weitergabe an Verbraucher / Abnehmer);
3. **Unerlässlichkeit** der Beschränkung (kein milderes Mittel);
4. **kein Ausschluss wesentlichen Wettbewerbs**.

Bei Hardcore-Beschränkungen: keine Einzelausnahme realistisch.

### 5. Rechtsfolgen

- **Zivilrechtliche Nichtigkeit** (§ 134 BGB iVm § 1 GWB; Art. 101 II AEUV) der wettbewerbsbeschränkenden Klausel; Restvertrag § 139 BGB.
- **Bußgeld** §§ 81, 81c GWB / Art. 23 VO 1/2003: bis **10 %** des weltweiten Konzernumsatzes.
- **Kronzeugen-Programm** § 81h–81n GWB (umgesetzt aus ECN+-RL 2019/1).
- **Privater Schadensersatz** §§ 33–33h GWB (Bindungswirkung bestandskräftiger Behördenentscheidung § 33b GWB; Passing-on § 33e GWB; Verjährung § 33h: kenntnisabhängig 5 Jahre / absolut 10 Jahre, Hemmung durch behördliches Verfahren).
- **Wettbewerbsregister** §§ 1 ff. WRegG: Eintragung kann zum Ausschluss von öffentlichen Aufträgen führen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute und Sekundärrecht

- [§ 1 GWB](https://www.gesetze-im-internet.de/gwb/__1.html) (Kartellverbot)
- [§ 2 GWB](https://www.gesetze-im-internet.de/gwb/__2.html) (Einzelausnahme — Verweis auf Art. 101 III AEUV)
- [§ 134 BGB](https://www.gesetze-im-internet.de/bgb/__134.html) (gesetzliches Verbot — Nichtigkeit)
- [§§ 33–33h GWB](https://www.gesetze-im-internet.de/gwb/__33.html) (private Durchsetzung, Bindungswirkung, Passing-on, Verjährung)
- [§ 81 GWB](https://www.gesetze-im-internet.de/gwb/__81.html) (Bußgeldrahmen)
- [Art. 101 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E101)
- [VO (EG) Nr. 1/2003 (Durchsetzung)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32003R0001)
- [VO (EU) 2022/720 (Vertikal-GVO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R0720)
- [VO (EU) 2023/1066 (FuE-GVO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1066)
- KOM, [De-minimis-Bekanntmachung, ABl. 2014 C 291/1](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:52014XC0830(01))
- KOM, [Vertikalleitlinien 2022, ABl. 2022 C 248/1](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:52022XC0630(01))
- [RL (EU) 2014/104 (Kartellschadensersatz)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0104)

### Kommentare

- Roth/Ackermann, in: Frankfurter Kommentar zum Kartellrecht, Stand 2024, § 1 GWB Rn. 1 ff.
- Zimmer, in: Immenga/Mestmäcker, Wettbewerbsrecht GWB, 6. Aufl. 2020, § 1 Rn. 1 ff.
- Ellger, in: Immenga/Mestmäcker, EU-Wettbewerbsrecht, 6. Aufl. 2019, Art. 101 III AEUV Rn. 1 ff. `[unverifiziert – Auflagenstand]`
- Bunte, in: Langen/Bunte, Kartellrecht Bd. 1, 14. Aufl. 2022, § 1 GWB Rn. 1 ff. `[unverifiziert – Auflagenstand]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/EuGH-Datenbank]`)

1. EuGH, Urt. v. 30.06.1966 – Rs. 56/65, Société Technique Minière (Zweck/Wirkung-Unterscheidung)
2. EuGH, Urt. v. 11.09.2014 – C-67/13 P, Groupement des cartes bancaires (CB) ./. Kommission (enge Auslegung der Zweckbeschränkung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2014-09-11&Aktenzeichen=C-67/13)
3. EuGH, Urt. v. 30.01.2020 – C-307/18, Generics (UK) u.a. (Pay-for-Delay als Zweck; potenzieller Wettbewerb im Arzneimittelsektor), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-01-30&Aktenzeichen=C-307/18)
4. EuGH, Urt. v. 14.03.2013 – C-32/11, Allianz Hungária Biztosító u.a. (kontextbezogene Würdigung; bilaterale Vereinbarungen Versicherer/Kfz-Werkstätten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2013-03-14&Aktenzeichen=C-32/11)
5. EuGH, Urt. v. 06.12.2017 – C-230/16, Coty Germany (Drittplattformverbot im Luxus-Selektivvertrieb zulässig), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2017-12-06&Aktenzeichen=C-230/16)
6. BGH, Urt. v. 12.07.2016 – [KZR 25/14, Lottoblock II](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=75559&pos=0&anz=1) (vertikale Beschränkungen)
7. BGH, Urt. v. 28.06.2011 – [KZR 75/10, ORWI](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=56712&pos=0&anz=1) (Passing-on, § 33e GWB)
8. BKartA, Bußgeldverfahren LKW-Kartell, Zucker, Bier, Wurst (jährlich Tätigkeitsbericht)

## Ausgabeformat

```
GUTACHTEN – Kartellverbots-Prüfung § 1 GWB / Art. 101 AEUV
Vereinbarung: <Bezeichnung>
Stand: <Datum>

I. Sachverhalt (Vereinbarung, Parteien, Marktanteile, Zwischenstaatlichkeit)
II. Frage(n)
III. Kurzantwort (1 Satz)

IV. Rechtliche Bewertung
    1. Anwendungsbereich (§ 1 GWB / Art. 101 AEUV — Zwischenstaatlichkeit)
    2. Tatbestand
       a) Unternehmen
       b) Vereinbarung / Beschluss / abgestimmtes Verhalten
       c) Wettbewerbsbeschränkung
          aa) Zweckbeschränkung (Hardcore-Check)
          bb) ggf. Wirkungsbeschränkung
       d) Spürbarkeit (De-minimis)
    3. Sicherheitshafen
       a) Vertikal-GVO 2022/720 (Marktanteilsschwelle, Kernbeschränkungen Art. 4, Art. 5)
       b) ggf. FuE-GVO / Spezialisierungs-GVO / TT-GVO
    4. Einzelausnahme § 2 GWB / Art. 101 III AEUV
       a) Effizienzgewinn
       b) Verbraucherbeteiligung
       c) Unerlässlichkeit
       d) kein Restwettbewerbsausschluss
    5. Rechtsfolgen
       - Nichtigkeit § 134 BGB
       - Bußgeld § 81 GWB / Art. 23 VO 1/2003
       - Schadensersatz §§ 33 ff. GWB
       - Wettbewerbsregister

V. Risikoeinstufung
   🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VI. Empfehlung
    - Vertragsänderung (konkrete Klausel)
    - Kronzeugen-Antrag bei laufendem Kartell?
    - Compliance-Schulung

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> Die Klausel "Der Händler verpflichtet sich, die unverbindlichen Preisempfehlungen des Herstellers nicht zu unterschreiten" stellt eine **Preisbindung der zweiten Hand** dar. Dabei handelt es sich um eine Kernbeschränkung iSv Art. 4 lit. a Vertikal-GVO 2022/720; sie ist als Zweckbeschränkung iSv § 1 GWB und Art. 101 I AEUV einzuordnen (vgl. EuGH, Urt. v. 11.09.2014 – C-67/13 P, Groupement des cartes bancaires, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2014-09-11&Aktenzeichen=C-67/13)). Eine Berufung auf den Sicherheitshafen der Vertikal-GVO scheidet aus (Art. 4 a.E.). Eine Spürbarkeitsprüfung erübrigt sich, da bei Kernbeschränkungen die De-minimis-Bekanntmachung der KOM nicht greift (ABl. 2014 C 291/1 Tz. 13). Die Einzelausnahme § 2 GWB / Art. 101 III AEUV scheitert regelmäßig an der **Unerlässlichkeit**: Eine vertikale Preisbindung ist zur Erreichung von Effizienzgewinnen nicht erforderlich; mildere Mittel (UVP ohne Sanktionsmechanismus) genügen. Die Klausel ist somit gemäß § 134 BGB iVm § 1 GWB **nichtig**. ...

## Risiken / typische Fehler

- **Hardcore-Beschränkung als "Empfehlung" deklariert**, faktisch aber sanktionsbewehrt — wird vom BKartA aufgegriffen.
- **Marktanteilsschwelle Vertikal-GVO (30 %)** falsch berechnet — auf den **relevanten** Markt und auf **jede** Partei einzeln.
- **Art. 4 Vertikal-GVO** versus **Art. 5**: Kernbeschränkungen kontaminieren den Gesamtvertrag; Art. 5-Beschränkungen sind nur teilnichtig.
- **Online-Restriktionen** unterschätzt (Drittplattformverbote, Preisparitätsklauseln).
- **Einzelausnahme als Pauschalplädoyer** — alle vier Voraussetzungen sind **kumulativ** und konkret zu belegen.
- **Zwischenstaatlichkeit** verkannt — Anwendungsvorrang Art. 101 AEUV und Bindungswirkung KOM-Entscheidungen.
- **Verjährung § 33h GWB** in Folgeprozessen (5 Jahre kenntnisabhängig / 10 Jahre absolut) übersehen.
- **Bindungswirkung § 33b GWB** ignoriert: bestandskräftige BKartA-/KOM-Entscheidung bindet im Schadensersatzprozess.
