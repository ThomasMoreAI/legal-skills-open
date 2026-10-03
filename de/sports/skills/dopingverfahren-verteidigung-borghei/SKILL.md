---
name: dopingverfahren-verteidigung-borghei
title: 'Dopingverfahren verteidigung'
description: Verteidigung der Athletin/des Athleten im sportrechtlichen Dopingverfahren – Anhörung bei NADA, Verbandsschiedsgericht, CAS-Berufung; WADC Art. 2.1 verschuldensunabhängige Anwesenheit, Sanktionsmilderung Art. 10.5/10.6 (No Significant Fault); Parallelverfahren § 4 IV AntiDopG (Selbstdoping Spitzensportler) und Verhältnis Sport-/Strafrecht; Whereabouts, B-Probe, Berufsverbot Art. 12 GG. Use when eine positive Probe gemeldet wurde, die NADA zur Anhörung lädt, ein Verband eine Sperre aussprechen oder bereits ausgesprochen hat, oder eine CAS-Berufung vorbereitet werden muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/sportrecht/skills/dopingverfahren-verteidigung
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: de
practice: sports
language: de
---

# /sportrecht:dopingverfahren-verteidigung

## Zweck

Der Skill begleitet die Verteidigung im sportrechtlichen Dopingverfahren von der ersten Mitteilung der A-Probe bis zur CAS-Berufung. Er identifiziert das anwendbare Regelwerk (WADC + NADC + Verbandsstatut), prüft die Voraussetzungen verschuldensunabhängiger Verstöße (WADC Art. 2.1) und entwickelt eine Verteidigungslinie über Art. 10.5/10.6 WADC (No (Significant) Fault). Er adressiert zugleich das parallele Strafverfahren nach § 4 IV AntiDopG (Selbstdoping Spitzensportler) und die grundrechtliche Folgenseite (Art. 12 GG, Sperre als Berufsverbot).

## Eingaben

- Sportart, Verband, Wettkampfklasse (Spitzensport iSv § 4 VII AntiDopG `[unverifiziert]`?)
- Substanz / Methode der WADA-Verbotsliste (S0–S9, M1–M3)
- A-Probe-Mitteilung: Datum, Frist B-Probe, NADA-Anschreiben
- Verfahrensstand (Anhörung anberaumt? Verbandsentscheidung ergangen? CAS-Frist läuft?)
- Verteidigungsthese (Kontamination NEM, Verschreibungsfehler, TUE-Antrag, Verfahrensmangel)
- bisherige Whereabouts-Compliance, frühere Doping-Verstöße
- ggf. Parallelermittlungen StA nach AntiDopG

## Sub-Agent-Architektur

Researcher liefert WADC-Artikel, NADC-Bestimmungen, einschlägiges Verbandsstatut, CAS- und BGH-Leitentscheidungen (Pechstein, Mutu) sowie Standardliteratur (Adolphsen, Pfister/Steiner zu AntiDopG, Holla). Drafter entwirft Anhörungsstellungnahme an NADA und – soweit erforderlich – CAS-Berufungsskizze in Urteilsstil; adressiert Parallelverfahren § 4 IV AntiDopG. Reviewer prüft 21-Tage-Berufungsfrist, Anhörungsrecht, B-Probe-Frist und Berufsfreiheits-Verhältnismäßigkeit.

## Ablauf

### 1. Anwendbares Regelwerk identifizieren

Welche **Fassung** des WADC (idR 2021 ff. `[unverifiziert]`) und des NADC ist über das Verbandsstatut und die Athletenvereinbarung in das konkrete Verfahren einbezogen? Schiedsklausel zugunsten CAS wirksam nach Pechstein-Linie (BGH, Urt. v. 07.06.2016 – KZR 6/15, BGHZ 210, 292 = NJW 2016, 2266, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-06-07&Aktenzeichen=KZR%206/15); EGMR, Urt. v. 02.10.2018 – Nr. 40575/10 und 67474/10, *Mutu und Pechstein/Schweiz*, [hudoc.echr.coe.int](https://hudoc.echr.coe.int/eng?i=001-186828); Fortsetzung BVerfG, Beschl. v. 03.06.2022 – 1 BvR 2103/16, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2022-06-03&Aktenzeichen=1%20BvR%202103/16))?

### 2. Verstoßtatbestand WADC Art. 2

WADC Art. 2.1 normiert die **Anwesenheit** einer verbotenen Substanz in der Probe als **verschuldensunabhängigen** Verstoß (strict liability). Zusätzlich relevant:

- Art. 2.2 Use or attempted use
- Art. 2.3 Verweigerung Probenentnahme
- Art. 2.4 Whereabouts-Verstöße (3 missed tests / filing failures binnen 12 Monaten)
- Art. 2.5 Tampering
- Art. 2.6 Possession; Art. 2.7 Trafficking; Art. 2.8 Administration; Art. 2.9 Complicity; Art. 2.10 Prohibited Association

### 3. Beweislast und B-Probe

Antibehörde trägt Beweislast für den Verstoß zum Komfortmaßstab "comfortable satisfaction" (höher als Zivilprozess, niedriger als Strafprozess). Athletin kann **B-Probe** beantragen (idR binnen 7 Tagen nach Mitteilung A-Probe — verbandsabhängig). Versäumte B-Probe = stillschweigende Anerkennung des A-Probe-Ergebnisses (`[unverifiziert]`).

### 4. Verfahrensgang

```
A-Probe positiv
  → NADA ergebnismanagementliche Mitteilung
  → Athletin: Stellungnahme + ggf. B-Probe-Antrag
  → Anhörung beim zuständigen Verbandsorgan (1. Instanz)
  → Verbandsschiedsgericht / DIS-Sportschiedsgericht (2. Instanz, idR Pflicht)
  → CAS Lausanne (Berufung, Frist 21 Tage WADC Art. 13)
  → ggf. Aufhebungsantrag Schweizer Bundesgericht / ZPO § 1059
parallel:
  → StA-Ermittlung § 4 IV / V AntiDopG
```

Pflicht zur **Anhörung** (WADC Art. 8): Verstoß = rechtsstaatliches Defizit → Sanktion anfechtbar. **🔴 BLOCKER**, wenn Sanktion ohne Anhörung ergangen.

### 5. Sanktionsmilderung WADC Art. 10

- Art. 10.2: Grundsanktion 4 Jahre (vorsätzlich) / 2 Jahre (nicht vorsätzlich)
- **Art. 10.5 No Fault or Negligence**: vollständige Aufhebung — sehr enge Voraussetzungen (Athletin trägt Beweislast, dass sie nicht einmal leichteste Sorgfaltspflicht verletzt hat)
- **Art. 10.6 No Significant Fault or Negligence**: Reduktion bis zur Hälfte; bei "Specified Substance" / "Contaminated Product" weitergehende Reduktion möglich
- Art. 10.7 Substantielle Hilfe; Art. 10.8 Eingeständnis / Vereinbarung
- Art. 10.9 mehrere Verstöße

Verteidigungslinie bei **Kontamination eines Nahrungsergänzungsmittels**: konkreter Nachweis der Kontaminationsquelle erforderlich (analytischer Nachweis der NEM-Charge); abstrakter Vortrag genügt der CAS-Rechtsprechung nicht (`[unverifiziert – prüfen in cas.tas-cas.org]`).

### 6. Parallel: Strafverfahren § 4 AntiDopG

[§ 4 AntiDopG](https://www.gesetze-im-internet.de/antidopg/__4.html):

- Abs. 1: Anwenden / Verabreichen / In-Verkehr-bringen verbotener Stoffe – bis 3 Jahre Freiheitsstrafe / Geldstrafe
- **Abs. 4 (Selbstdoping Spitzensportler)**: Eigendoping eines Spitzensportlers iSd § 4 VII iVm § 4 III AntiDopG `[unverifiziert]` – bis 3 Jahre Freiheitsstrafe / Geldstrafe; **Spezialvorschrift**, die das frühere straflose Eigendoping aufhebt
- Abs. 5: gewerbsmäßig / Bande / Gesundheitsgefahr – bis 10 Jahre

Schnittstelle:

- Sportrechtsverfahren und Strafverfahren laufen **unabhängig** (kein `ne bis in idem` zwischen sportrechtlicher Sperre und staatlicher Strafe nach hM `[unverifiziert]`).
- Aussagen im Sportverfahren können in das Strafverfahren einfließen — **Aussageabstimmung** ist verteidigerische Pflicht (§ 43a BRAO).
- TUE (Therapeutic Use Exemption) wirkt sportrechtlich, nicht ohne weiteres strafrechtlich.

### 7. Grundrechtliche Folgenseite

Sperre kann faktisches **Berufsverbot** iSv Art. 12 GG sein (Profisportlerin: existenzielle wirtschaftliche Folge). Inhaltskontrolle der Sperrdauer am Maßstab der Verhältnismäßigkeit; CAS muss Verhältnismäßigkeit prüfen (st. Rspr. `[unverifiziert]`). DSGVO Art. 9 (Gesundheits- und biologische Daten) für ABP-Steroidprofil etc.

### 8. Whereabouts-Pflichten

Registered Testing Pool (RTP) – Meldepflicht **24/7-Verfügbarkeit eines 60-Min-Slots** pro Tag. 3 missed tests / filing failures binnen 12 Monaten = Verstoß Art. 2.4 WADC. Verteidigungsansätze: technische Fehler ADAMS, Force majeure, Doppelmeldung.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute und Regelwerke

- [§ 2 AntiDopG](https://www.gesetze-im-internet.de/antidopg/__2.html) (Begriff Doping)
- [§ 3 AntiDopG](https://www.gesetze-im-internet.de/antidopg/__3.html) (Verbote)
- [§ 4 AntiDopG](https://www.gesetze-im-internet.de/antidopg/__4.html) (Strafvorschriften, insb. Abs. 4 Selbstdoping)
- [Art. 12 GG](https://www.gesetze-im-internet.de/gg/art_12.html) (Berufsfreiheit)
- [Art. 9 III GG](https://www.gesetze-im-internet.de/gg/art_9.html) (Koalitions- und Verbandsfreiheit)
- [§§ 1025 ff. ZPO](https://www.gesetze-im-internet.de/zpo/__1025.html) (Schiedsverfahren)
- WADC 2021 (`https://www.wada-ama.org/en/resources/world-anti-doping-code`) – insb. Art. 2, 7, 8, 10, 13
- NADC (Nationaler Anti-Doping-Code, NADA) `[unverifiziert – aktuelle Fassung prüfen unter nada.de]`
- CAS-Code (`https://www.tas-cas.org/en/arbitration/code-procedural-rules.html`)
- DIS-Sportschiedsgerichtsordnung (`https://www.disarb.org`)
- WADA-Verbotsliste (jährliche Fassung)

### Kommentare und Handbücher

- Adolphsen, in: Adolphsen, Sportrecht, X. Aufl. Jahr, Kap. zu Anti-Doping Rn. 1 ff.
- Summerer, in: Fritzweiler/Pfister/Summerer, Praxishandbuch Sportrecht, X. Aufl. Jahr, Kap. zu Anti-Doping Rn. 1 ff.
- Pfister, in: Pfister/Steiner, Sportrecht-Kommentar, X. Aufl. Jahr, § 4 AntiDopG Rn. 1 ff.
- Vieweg/Steinbach, Sportrecht, Loseblatt, Stand Jahr, Kap. Anti-Doping
- Holla, Praxishandbuch Sportrecht, X. Aufl. Jahr, Kap. zu CAS-Verfahren

### Staatliche Rechtsprechung (verifiziert)

1. BGH, Urt. v. 07.06.2016 – KZR 6/15, BGHZ 210, 292 = NJW 2016, 2266 = SchiedsVZ 2016, 268 (*Pechstein/ISU* – Schiedsklausel wirksam, aber Inhaltskontrolle), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-06-07&Aktenzeichen=KZR%206/15)
2. OLG München, Urt. v. 15.01.2015 – U 1110/14 Kart, SchiedsVZ 2015, 40 = SpuRt 2015, 78 (Vorinstanz – Schiedsklausel kartellrechtswidrig), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=U%201110/14%20Kart)
3. EGMR, Urt. v. 02.10.2018 – Nr. 40575/10 und 67474/10, ECLI:CE:ECHR:2018:1002JUD004057510 (*Mutu und Pechstein/Schweiz* – öffentliche Verhandlung vor dem CAS nach Art. 6 Abs. 1 EMRK), [hudoc.echr.coe.int](https://hudoc.echr.coe.int/eng?i=001-186828)
4. BVerfG, Beschl. v. 03.06.2022 – 1 BvR 2103/16 (*Pechstein* – Justizgewährungsanspruch; rechtsstaatliche Mindeststandards der Sportschiedsgerichtsbarkeit), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2022-06-03&Aktenzeichen=1%20BvR%202103/16)
5. EuGH, Urt. v. 18.07.2006 – C-519/04 P, NJW 2007, 2097 = SpuRt 2006, 195 (*Meca-Medina und Majcen/Kommission* – Anti-Doping-Regeln unterliegen dem Kartellrecht, sind aber bei Verhältnismäßigkeit gerechtfertigt), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=C-519/04)

### Schiedssprüche und Verbandsregelwerke — **keine staatliche Rechtsprechung**

CAS-Awards sind **Schiedssprüche** eines privaten Schiedsgerichts, keine Gerichtsentscheidungen. Sie sind weder in dejure.org noch in juris nachgewiesen, entfalten keine Bindungswirkung nach deutschem Recht und sind nur über die CAS-Datenbank ([jurisprudence.tas-cas.org](https://jurisprudence.tas-cas.org)) zu belegen. Dasselbe gilt für WADC und NADC als **Verbandsregelwerke**. Im Gutachten sind sie ausdrücklich als solche zu kennzeichnen und nicht mit staatlicher Rechtsprechung in einer Liste zu führen.

- CAS 2009/A/1912 (*Pechstein ./. ISU*) — Schiedsspruch `[unverifiziert – nicht über dejure/juris belegbar; Volltext über jurisprudence.tas-cas.org prüfen]`
- CAS 2008/A/1644 (*Mutu ./. Chelsea*) — Schiedsspruch `[unverifiziert – nicht über dejure/juris belegbar; Volltext über jurisprudence.tas-cas.org prüfen]`
- WADC / NADC in der jeweils einbezogenen Fassung — Verbandsregelwerk `[unverifiziert – Fassung über wada-ama.org bzw. nada.de prüfen]`

## Ausgabeformat

```
STELLUNGNAHME — Anhörung NADA / Verbandsschiedsgericht
Athlet/in: <Pseudonym>   Verband: <…>   Az.: <…>

I. Sachverhalt
   - A-Probe: <Datum>, Substanz: <…>, Konzentration: <…>
   - B-Probe: <Antrag ja/nein, Ergebnis>
   - Verfahrensstand: <…>

II. Anwendbares Regelwerk
    WADC <Fassung> + NADC + Statut <Verband>
    Schiedsklausel: <Prüfung Pechstein-Linie>

III. Verstoßtatbestand
     Art. 2.1 WADC: Anwesenheit (strict liability)
     Beweislage A-/B-Probe: <…>

IV. Verteidigungslinie
    1. Verfahrensmängel (Anhörung, B-Probe-Recht, Chain of Custody)
    2. No Significant Fault Art. 10.6 WADC
       - Kontaminationsquelle: <konkreter Nachweis>
       - Sorgfaltsmaßstab: <…>
    3. Verhältnismäßigkeit Sperrdauer (Art. 12 GG)

V. Parallel: § 4 IV AntiDopG
   - Spitzensportler-Eigenschaft: <…>
   - Vorsatzfrage / Beweisverwertung
   - Aussageabstimmung mit StA-Verfahren

VI. Fristkalender
    - B-Probe-Antrag bis:    <Datum>
    - Stellungnahme bis:     <Datum>
    - CAS-Berufung 21 Tage:  <Datum>
    - § 1059 ZPO 3 Monate:   <Datum>

VII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VIII. Quellenverzeichnis

----------------- bei CAS-Berufung zusätzlich -----------------

BERUFUNGSSCHRIFT (Skizze) — CAS Lausanne
Appellant: <…>   Respondent: <Verband / NADA>

A. Anträge
B. Sachverhalt
C. Rechtliche Würdigung
   – Verfahrensmängel
   – Art. 10.5/10.6 WADC
   – Verhältnismäßigkeit
D. Beweismittel
E. Sprache, Schiedsort, Kostenhinweis
```

## Risiken / typische Fehler

- **Versäumte B-Probe-Frist** → A-Probe gilt als anerkannt.
- **Versäumte CAS-Frist 21 Tage** → Sperre rechtskräftig, Aufhebungsantrag Schweizer BG nur in engen Grenzen.
- **Abstrakte Kontaminationsbehauptung** ohne analytischen Nachweis der NEM-Charge → Art. 10.6 WADC scheitert.
- **Aussagen im Sportverfahren ohne Abstimmung mit Strafverteidigung** → Selbstbelastung iSv § 4 IV AntiDopG.
- **Anhörung übergangen** → Sanktion rechtsstaatlich defizitär; CAS hebt regelmäßig auf.
- **Schiedsklausel-Wirksamkeit unkritisch übernommen** → Pechstein-Linie versäumt; Einrede der Unwirksamkeit nach BGH `[unverifiziert]` möglich.
- **§ 4 IV AntiDopG übersehen** → strafrechtliche Folgen für Mandantin nicht aufgezeigt; Anwaltshaftung.
