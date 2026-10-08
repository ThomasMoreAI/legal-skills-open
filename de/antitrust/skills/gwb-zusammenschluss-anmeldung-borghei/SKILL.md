---
name: gwb-zusammenschluss-anmeldung-borghei
title: /kartellrecht:gwb-zusammenschluss-anmeldung
description: Prüfung der Anmeldepflicht eines Zusammenschlusses beim Bundeskartellamt nach §§ 35 ff. GWB inkl. Umsatzschwellen § 35, Transaktionswert-Schwelle § 35 Ia, Verhältnis zur EU-FK-VO 139/2004 (One-Stop-Shop), Vorprüfung und Hauptprüfung § 40, Vollzugsverbot § 41. Use when ein M&A-Vorhaben (Anteils-/Vermögenserwerb, gemeinschaftliche Kontrolle, Joint Venture) ansteht und die kartellrechtliche Genehmigungspflicht zu klären ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kartellrecht/skills/gwb-zusammenschluss-anmeldung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: antitrust
language: de
---

# /kartellrecht:gwb-zusammenschluss-anmeldung

## Zweck

Der Skill klärt vor einem geplanten Unternehmenszusammenschluss, ob eine kartellrechtliche Anmeldepflicht besteht — nach deutschem Recht beim Bundeskartellamt (§§ 35–43 GWB) oder vorrangig bei der EU-Kommission nach der EU-FK-VO 139/2004 (One-Stop-Shop). Er liefert eine Anmeldeschrift-Skizze und ein Risk-Memo zur materiellen Untersagungsprüfung und zum Vollzugsverbot. Closing vor Freigabe ist bußgeldbewehrt nach § 81 II GWB bis zu 10 % des weltweiten Konzernumsatzes — Gun-Jumping ist der zentrale Blocker.

## Eingaben

- Transaktionsstruktur (Anteilserwerb / Vermögenserwerb / gemeinschaftliche Kontrolle / Joint Venture)
- Beteiligte Unternehmen und Konzernzugehörigkeit (verbundene Unternehmen § 36 II GWB)
- Letztabgeschlossene Geschäftsjahre — weltweite Umsätze, EU-Umsätze, Inlandsumsätze (mindestens 3 Jahre)
- Kaufpreis / Wert der Gegenleistung (für § 35 Ia GWB Transaktionswert-Schwelle)
- Geplanter Signing- und Closing-Termin
- Märkte / Tätigkeitsgebiete der Parteien (Horizontal- / Vertikal- / Konglomeratüberlappung)
- Bei JV: Vollfunktion-/Teilfunktion-Charakter; Joint-Venture-Vereinbarungen

## Sub-Agent-Architektur

Researcher liefert die einschlägigen GWB- und FK-VO-Vorschriften, BKartA-Beschlusspraxis (z. B. zu Aufgreifschwellen, Transaktionswert, Vollfunktion-JV), EuGH/EuG-Entscheidungen zur Marktabgrenzung und Untersagungspraxis sowie Kommentarstellen. Drafter erstellt eine Anmeldeschrift-Skizze (Beteiligte, Transaktion, Umsätze, Märkte, materielle Würdigung) und ein Risk-Memo mit Untersagungs-Wahrscheinlichkeit und Auflagen-Optionen. Reviewer prüft Schwellenberechnung, One-Stop-Shop-Zuordnung, Frist-Kalender und Gun-Jumping-Risiko.

## Ablauf

### 1. Zusammenschlusstatbestand § 37 GWB / Art. 3 EU-FK-VO

Ein Zusammenschluss liegt vor (§ 37 I GWB) bei:

1. Erwerb des Vermögens eines anderen Unternehmens ganz oder zu einem wesentlichen Teil,
2. Erwerb der unmittelbaren oder mittelbaren Kontrolle iSv § 37 I Nr. 2 GWB,
3. Erwerb von Anteilen, die allein oder zusammen mit anderen, dem Erwerber bereits gehörenden Anteilen **25 %** oder **50 %** des Kapitals oder der Stimmrechte erreichen,
4. jede sonstige Verbindung von Unternehmen, aufgrund deren ein oder mehrere Unternehmen unmittelbar oder mittelbar einen wettbewerblich erheblichen Einfluss auf ein anderes Unternehmen ausüben können.

EU-rechtlich entspricht das Art. 3 FK-VO (Kontrollerwerb, Vollfunktions-JV). **Gemeinschaftliche Kontrolle** (50/50-JV) ist Zusammenschluss; das Vollfunktionskriterium (eigenständig auf Dauer am Markt) gilt unter der EU-FK-VO und in der Praxis des BKartA.

### 2. Aufgreifschwellen § 35 GWB

Anmeldepflicht greift nur, wenn beteiligte Unternehmen im **letzten Geschäftsjahr** kumulativ erreicht haben (§ 35 I GWB):

- weltweite Umsätze aller beteiligten Unternehmen zusammen **> 500 Mio. EUR**, **und**
- inländischer Umsatz **eines** beteiligten Unternehmens **> 50 Mio. EUR**, **und**
- inländischer Umsatz **eines weiteren** beteiligten Unternehmens **> 17,5 Mio. EUR**.

**Transaktionswert-Schwelle § 35 Ia GWB**: Greifen die Inlandsumsatzschwellen nicht, ist der Zusammenschluss dennoch anmeldepflichtig, wenn

- weltweiter Umsatz aller Beteiligten **> 500 Mio. EUR**,
- ein beteiligtes Unternehmen Inlandsumsatz **> 50 Mio. EUR**,
- der Wert der Gegenleistung **> 400 Mio. EUR**, und
- das Zielunternehmen **erheblich im Inland tätig** ist (Inland-Nexus — Leitfaden BKartA/BMWK 2018, fortgeschrieben).

Bagatellklausel § 36 II GWB: keine Untersagung, wenn der Markt klein und das beherrschte Unternehmen klein ist; Anschlussklausel § 38 GWB regelt die Umsatzberechnung für verbundene Unternehmen.

### 3. EU-FK-VO-Vorrang (One-Stop-Shop, Art. 21 FK-VO)

Sind die EU-Schwellen Art. 1 FK-VO erreicht (Grundsatz: weltw. > 5 Mrd. EUR + zwei Beteiligte je > 250 Mio. EUR Union; bzw. 2-Mrd.-Variante mit zusätzlichem Mehrstaaten-Erfordernis und 2/3-Regel), ist **ausschließlich** die EU-Kommission zuständig. Eine deutsche Anmeldung entfällt; ggf. Rückverweisung Art. 4 IV / 9 (an Mitgliedstaat) oder Art. 4 V / 22 (an KOM) prüfen.

### 4. Anmeldung § 39 GWB

Anmeldepflichtig sind die am Zusammenschluss beteiligten Unternehmen. Anmeldung **vor** Vollzug, schriftlich oder elektronisch, in deutscher Sprache, mit Mindestangaben (§ 39 III GWB): Beteiligte, Inhaber/Konzernzugehörigkeit, Marktposition (Marktanteile, in der Regel ≥ 5 % oder Wertinformationen), Umsätze, ggf. ergänzende Wettbewerbsanalyse. Form CO unter der EU-FK-VO bei EU-Anmeldungen.

### 5. Fristen § 40 GWB / Art. 10 FK-VO

**Vorprüfung** (§ 40 I GWB): **1 Monat** ab vollständiger Anmeldung. Wenn das BKartA bis zum Fristablauf kein Hauptprüfungsverfahren eröffnet, gilt der Zusammenschluss als freigegeben (Schweigen-Freigabe).

**Hauptprüfung** (§ 40 II GWB): **4 Monate** ab Anmeldung, verlängerbar (z. B. um 1 Monat bei Verpflichtungszusagen Abs. 2 S. 4, um Anrechnung ausländischer Verfahren Abs. 2 S. 5 ff.).

EU-FK-VO: Phase I 25 Arbeitstage (Art. 10 I), Phase II 90 Arbeitstage (Art. 10 III), Verlängerung bei Zusagen + 10 / + 20 Arbeitstage.

### 6. Vollzugsverbot § 41 GWB / Art. 7 FK-VO

Vollzug **vor** Freigabe ist verboten. Verstoß: Bußgeld bis **10 %** des weltweiten Konzernumsatzes des vorletzten Geschäftsjahres (§ 81 II GWB; Art. 14 FK-VO). Vollzugsbegriff weit (auch teilweiser Vollzug, Personalintegration, Informationsaustausch ohne Clean Team — "Gun-Jumping"). Schwebende Unwirksamkeit der Vollzugsmaßnahmen nach § 41 I 2 GWB.

Ausnahmen: Wertpapiergeschäfte § 41 Ia GWB; Befreiung im Einzelfall § 41 II GWB.

### 7. Materielle Untersagungsprüfung (§ 36 GWB / Art. 2 FK-VO)

SIEC-Test ("Significant Impediment to Effective Competition"): Untersagung, wenn der Zusammenschluss **eine erhebliche Behinderung wirksamen Wettbewerbs** erwarten lässt, insbesondere durch Entstehung oder Verstärkung einer marktbeherrschenden Stellung. Marktbeherrschungsvermutung § 18 IV GWB als Indikator.

Prüfungsschritte:

1. Marktabgrenzung sachlich / räumlich / zeitlich (Bedarfsmarktkonzept; SSNIP-Test).
2. Marktanteile und Marktstrukturindikatoren (HHI; Marktzutrittsschranken; Innovationspotenzial).
3. Horizontale / vertikale / konglomerate Effekte; koordinierte vs. nicht-koordinierte Effekte.
4. Effizienzvorteile / Sanierungsklausel ("failing firm defence").
5. Verpflichtungszusagen / Auflagen (Veräußerung, Verhaltensauflagen).
6. Hilfsweise Ministererlaubnis § 42 GWB bei überragenden Gemeinwohlinteressen.

### 8. Beschwerde § 73 GWB

Gegen Untersagungsentscheidungen ist die Beschwerde zum OLG Düsseldorf (Kartellsenat) statthaft, Frist **1 Monat** ab Zustellung (§ 73 II GWB). Rechtsbeschwerde an den BGH Kartellsenat nach § 77 GWB.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 35 GWB](https://www.gesetze-im-internet.de/gwb/__35.html) (Aufgreifschwellen — Umsatz + Transaktionswert § 35 Ia)
- [§ 36 GWB](https://www.gesetze-im-internet.de/gwb/__36.html) (Untersagungsvoraussetzungen — SIEC-Test, Bagatellklausel)
- [§ 37 GWB](https://www.gesetze-im-internet.de/gwb/__37.html) (Zusammenschlusstatbestand)
- [§ 38 GWB](https://www.gesetze-im-internet.de/gwb/__38.html) (Umsatzberechnung, verbundene Unternehmen)
- [§ 39 GWB](https://www.gesetze-im-internet.de/gwb/__39.html) (Anmeldung beim BKartA)
- [§ 40 GWB](https://www.gesetze-im-internet.de/gwb/__40.html) (Vorprüfung 1 Monat / Hauptprüfung 4 Monate)
- [§ 41 GWB](https://www.gesetze-im-internet.de/gwb/__41.html) (Vollzugsverbot)
- [§ 42 GWB](https://www.gesetze-im-internet.de/gwb/__42.html) (Ministererlaubnis)
- [§ 73 GWB](https://www.gesetze-im-internet.de/gwb/__73.html) (Beschwerde zum OLG Düsseldorf)
- [§ 81 GWB](https://www.gesetze-im-internet.de/gwb/__81.html) (Bußgeldrahmen bis 10 % Konzernumsatz)
- [VO (EG) Nr. 139/2004 (EU-FK-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004R0139)
- ergänzend: BKartA, Leitfaden Transaktionswert-Schwelle (gemeinsam mit BWB, Stand 2018/2022 `[unverifiziert]`); BKartA, Merkblatt Inlandsauswirkung; KOM, Konsolidierte Zuständigkeitsmitteilung (ABl. 2008 C 95/1).

### Kommentare

- Mestmäcker/Veelken, in: Immenga/Mestmäcker, Wettbewerbsrecht GWB, 6. Aufl. 2020, §§ 35 ff. Rn. 1 ff.
- Bechtold/Bosch, GWB, 11. Aufl. 2024, §§ 35–41 Rn. 1 ff. `[unverifiziert – Auflagenstand]`
- Riesenkampff/Lehr, in: Loewenheim/Meessen/Riesenkampff/Kersting/Meyer-Lindemann, Kartellrecht, 4. Aufl. 2020, § 35 GWB Rn. 1 ff.
- Körber, in: Immenga/Mestmäcker, EU-Wettbewerbsrecht, 6. Aufl. 2019, FKVO Art. 1 Rn. 1 ff. `[unverifiziert – Auflagenstand]`

### Rechtsprechung (staatliche Gerichte)

1. BGH, Beschl. v. 25.09.2007 – [KVR 19/07, Sulzer/Kelmix](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=41867&pos=0&anz=1) (Erwerb wettbewerblich erheblicher Einfluss)
2. BGH, Beschl. v. 14.11.2017 – KVR 57/16, EDEKA/Kaiser's Tengelmann (Befugnis des BKartA, Verstöße gegen das **Vollzugsverbot** zu untersagen; **nicht** die Ministererlaubnis nach § 42 GWB — über deren Anfechtung entschied das OLG Düsseldorf), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2017-11-14&Aktenzeichen=KVR%2057/16)
3. EuG, Urt. v. 28.05.2020 – T-399/16, CK Telecoms UK Investments ./. Kommission (SIEC-Test, Beweismaß; Nichtigerklärung der Untersagung Hutchison 3G UK/Telefónica UK), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuG&Datum=2020-05-28&Aktenzeichen=T-399/16) — **⚠️ im Rechtsmittel aufgehoben**: EuGH, Urt. v. 13.07.2023 – C-376/20 P; die Beweismaß-Ausführungen des EuG sind damit überholt und dürfen nicht mehr als geltender Maßstab zitiert werden `[unverifiziert – Rechtsmittelentscheidung C-376/20 P nicht eigenständig abgerufen; Aufhebung ist im dejure-Datensatz zu T-399/16 vermerkt]`
4. EuGH, Urt. v. 04.03.2020 – C-10/18 P, Mowi (vormals Marine Harvest) ./. Kommission (Gun-Jumping; Art. 4 I und Art. 7 I FK-VO als eigenständige Verstöße, ne bis in idem), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-03-04&Aktenzeichen=C-10/18)
### Behördenpraxis — **keine Gerichtsentscheidungen, getrennt zitieren**

Entscheidungen der Europäischen Kommission (`M.####`, `AT.#####`) und des Bundeskartellamts sind **Verwaltungsentscheidungen**, keine Rechtsprechung. Sie sind nicht in dejure oder juris als Rspr. nachgewiesen, entfalten keine Bindungswirkung nach § 33b GWB und dürfen in einer Rspr.-Liste nicht neben Urteile des EuGH, EuG oder BGH gestellt werden. Beleg ausschließlich über `competition-cases.ec.europa.eu` bzw. `bundeskartellamt.de`.

- BKartA, Tätigkeitsberichte mit Bußgeldern für Gun-Jumping (z. B. [Mars/Nutro 2008](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2008/15_12_2008_Mars_Vollzugsverbot.html)).
- KOM, [M.7217 Facebook/WhatsApp](https://competition-cases.ec.europa.eu/cases/M.7217); [M.8124 Microsoft/LinkedIn](https://competition-cases.ec.europa.eu/cases/M.8124); [M.10188 Illumina/GRAIL](https://competition-cases.ec.europa.eu/cases/M.10188) (Phase II; die zuvor hier genannte Nummer M.10262 gehört nicht zu diesem Vorhaben) `[unverifiziert – KOM-Fallnummer über competition-cases.ec.europa.eu gegenprüfen; über dejure nicht belegbar, weil dort keine Kommissionsentscheidungen geführt werden]`

## Ausgabeformat

```
ANMELDUNGS- UND RISK-MEMO – Zusammenschlussvorhaben
Beteiligte: <Erwerber> / <Zielgesellschaft>
Stand: <Datum>

I. Sachverhalt
   - Transaktionsstruktur
   - Beteiligte und Konzern
   - Umsätze (weltw. / EU / Inland — letzte 3 GJ)
   - Märkte (sachlich / räumlich)
   - Geplantes Signing/Closing

II. Frage(n)
   1. Liegt ein Zusammenschluss iSd § 37 GWB / Art. 3 FK-VO vor?
   2. Sind Aufgreifschwellen § 35 GWB oder § 35 Ia GWB erreicht?
   3. Greift vorrangig die EU-FK-VO (One-Stop-Shop)?
   4. Welche Frist-Risiken (Vorprüfung, Hauptprüfung, Vollzugsverbot)?
   5. Welche materiellen Untersagungsrisiken (SIEC-Test)?

III. Kurzantwort (1 Satz pro Frage)

IV. Rechtliche Bewertung
    1. Zusammenschlusstatbestand § 37 GWB
    2. Aufgreifschwellen
       a) § 35 I GWB
       b) § 35 Ia GWB (Transaktionswert + Inlands-Nexus)
    3. One-Stop-Shop Art. 1, 21 EU-FK-VO
    4. Anmeldepflicht und Anmeldungsbestandteile § 39 GWB
    5. Vollzugsverbot § 41 GWB / Art. 7 FK-VO
    6. Materielle Würdigung (SIEC § 36 GWB / Art. 2 FK-VO)
       - Marktabgrenzung
       - Marktanteile und Wettbewerbsdruck
       - Effizienzen / Auflagen-Optionen
    7. Verfahrens- und Rechtsmittelweg (§ 73 GWB, OLG Düsseldorf)

V. Anmeldeschrift-Skizze (Outline für Form A / Form CO)

VI. Frist-Kalender
    - Anmeldung vor Signing/Closing?
    - Vorprüfung Endtermin: <Datum + 1 Monat>
    - Hauptprüfung-Frist: <Datum + 4 Monate>
    - Vollzug erlaubt frühestens am: <Datum>

VII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
     - Gun-Jumping-Risiko?
     - Untersagungs-Wahrscheinlichkeit?
     - Auflagen-Bedarf?

VIII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> A. Erwerb von 100 % der Anteile an der B-GmbH durch die A-AG ist ein Zusammenschluss iSv § 37 I Nr. 3 lit. b GWB, da die 50 %-Schwelle erreicht ist. Die Aufgreifschwellen § 35 I GWB sind nach den im Sachverhalt mitgeteilten Umsätzen (weltweit > 500 Mio. EUR; Inlandsumsatz A-AG > 50 Mio. EUR; Inlandsumsatz B-GmbH > 17,5 Mio. EUR) erreicht. Da die EU-Schwellen Art. 1 FK-VO bei dem aggregierten Unionsumsatz von ca. ... nicht erfüllt sind, verbleibt die ausschließliche Zuständigkeit beim Bundeskartellamt. Der Zusammenschluss ist daher gemäß § 39 GWB **vor Vollzug** anzumelden. Vollzug vor Freigabe ist nach § 41 I GWB verboten und nach § 81 II Nr. 1 GWB bußgeldbewehrt bis zu 10 % des weltweiten Konzernumsatzes des vorletzten Geschäftsjahres (vgl. EuGH, Urt. v. 04.03.2020 – C-10/18 P, Mowi/Marine Harvest, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-03-04&Aktenzeichen=C-10/18)). ...

## Risiken / typische Fehler

- **Closing vor Freigabe** (Gun-Jumping). 🔴 BLOCKER. Selbst vorbereitende Integrationsmaßnahmen ohne Clean Team können vollzugsbegründend sein.
- **Vergessen der Transaktionswert-Schwelle § 35 Ia GWB** bei Tech-/Pharma-Käufen mit geringen Zielumsätzen aber hohem Kaufpreis.
- **Falsche Umsatzzuordnung** (verbundene Unternehmen § 36 II GWB, Veräußerergruppe versus Erwerbergruppe, Umsatz-Stichtag § 38 GWB).
- **Übersehen des EU-Vorrangs** bei sehr großen Konzernen — Anmeldung beim BKartA, obwohl Art. 1 FK-VO erfüllt.
- **Vollfunktion-Kriterium beim JV** nicht geprüft (auf Dauer eigenständig am Markt; Form CO Section 7).
- **Fehlende Marktabgrenzung** bei knapper Marktanteilslage — Untersagungsrisiko unterschätzt.
- **Keine Auflagen-Optionen** parallel mitgedacht (Veräußerung Geschäftsbereich, Lizenzen, Hold-Separate).
- **Beschwerdefrist § 73 II GWB (1 Monat)** verpasst.
