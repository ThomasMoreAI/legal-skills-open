---
name: vereinsrechtliche-sanktion
title: 'Vereinsrechtliche sanktion'
description: Anfechtung sportrechtlicher Vereins- und Verbandssanktionen – Vereinsausschluss (BGB §§ 25, 39), Verbandssperre (Disziplinargewalt aus Satzung iVm Mitgliedschaft), Stadionverbot (§ 858, § 1004 BGB Hausrecht); Inhaltskontrolle der Satzung §§ 138, 242 BGB, Art. 9 III GG vs. Art. 12 GG; Schiedsklausel-Wirksamkeit nach Pechstein-Linie, 2-Instanzen-Erfordernis; Anfechtungsfrist § 32 BGB / § 246 AktG analog. Use when ein Vereins- oder Verbandsmitglied gegen Ausschluss, Sperre oder andere disziplinarische Maßnahme vorgehen will oder ein Veranstalter ein Stadionverbot verteidigen oder anfechten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/sportrecht/skills/vereinsrechtliche-sanktion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: sports
language: de
---

# /sportrecht:vereinsrechtliche-sanktion

## Zweck

Der Skill prüft die formelle und materielle Rechtmäßigkeit einer Vereins- oder Verbandssanktion und entwirft den passenden Rechtsbehelf — verbandsintern (Berufung), schiedsgerichtlich (CAS / DIS-Sportschiedsgericht) oder zivilrechtlich (Anfechtungsklage vor LG nach § 32 BGB / § 246 AktG analog). Er deckt zugleich die zivilrechtliche Sonderform **Stadionverbot** ab (§ 858, § 1004 BGB iVm BVerfG-Drittwirkung Art. 3 GG).

## Eingaben

- Sanktionstyp (Ausschluss, Sperre, Geldbuße, Stadionverbot, Aberkennung Titel/Punkte)
- Sanktionierende Stelle (Verein, Landesverband, Bundesverband)
- Satzungs- und Verfahrensordnungstext (relevanter Auszug)
- Verfahrensgang (Anhörung? Schriftliche Begründung? Rechtsmittelbelehrung?)
- Mitgliedschaft / Lizenz / Athletenvereinbarung mit Schiedsklausel?
- Datum der Sanktionsentscheidung (Fristbeginn!)
- bisherige Eskalation (Berufung verbandsintern bereits erfolgt?)

## Sub-Agent-Architektur

Researcher liefert BGB-Vereinsrechtsnormen, BGH-Rechtsprechung zur Inhaltskontrolle der Vereinssatzung und zum Stadionverbot, BVerfG zur Drittwirkung der Grundrechte sowie Reichert/Sauter-Schweyer-Waldner. Drafter erstellt entweder Anfechtungsklage (LG, § 32 BGB / § 246 AktG analog) oder verbandsinterne Beschwerde / Schiedsklage je nach Verfahrensstand. Reviewer prüft Anhörungsrecht (BLOCKER), Bestimmtheit der Satzungsnorm, Schiedsklausel-Wirksamkeit (Pechstein-Linie) und Anfechtungsfrist.

## Ablauf

### 1. Anwendbares Regelwerk und Hierarchie

```
Satzung (BGB § 25)
  ↳ Verfahrensordnung / Strafordnung des Verbands
  ↳ Einzelne Disziplinarentscheidung
```

Die **Disziplinargewalt** des Vereins/Verbands folgt nicht aus § 25 BGB unmittelbar, sondern aus der **Satzung iVm der Mitgliedschaft** (st. Rspr. `[unverifiziert]`). Ohne Satzungsgrundlage keine Disziplinarsanktion.

### 2. Formelle Rechtmäßigkeit

- **Zuständigkeit**: Hat das satzungsmäßig zuständige Organ entschieden (Vorstand, Ehrenrat, Sportgericht)?
- **Anhörung des Mitglieds** vor der Entscheidung — Ausfluss des allgemeinen rechtsstaatlichen Prinzips, gilt im Vereinsrecht analog (BGH, st. Rspr. `[unverifiziert – prüfen]`). **🔴 BLOCKER bei Fehlen.**
- **Bestimmtheit der Sanktionsnorm** in der Satzung (Art. 103 II GG analog im Vereinsdisziplinarrecht `[unverifiziert]`).
- **Schriftform der Entscheidung mit Begründung und Rechtsmittelbelehrung** (idR satzungsrechtlich geboten).
- **2-Instanzen-Erfordernis** bei Bundesverbänden vor Anrufung des Schiedsgerichts (verbandsintern Berufung idR Pflicht).

### 3. Materielle Rechtmäßigkeit

- **Tatbestandsmäßigkeit**: Subsumtion unter die Satzungsnorm.
- **Verhältnismäßigkeit**: Eignung, Erforderlichkeit, Angemessenheit. Mildere Mittel (Verwarnung statt Ausschluss)?
- **Inhaltskontrolle der Satzungsnorm** nach §§ 138, 242 BGB (BGH zur Vereinsstrafgewalt: Kontrolle nur auf grobe Unbilligkeit, *aber* bei monopolistischen Bundesverbänden strengerer Maßstab `[unverifiziert]`).
- **Grundrechtskonforme Auslegung** (Drittwirkung): Art. 12 GG (Berufsfreiheit der Athletin), Art. 5 GG (Meinungsäußerung), Art. 3 GG iVm AGG, Art. 9 III GG für Athletenkoalitionen vs. Verbandsmonopol.

### 4. Schiedsklausel-Wirksamkeit (Pechstein-Linie)

Athletenvereinbarungen mit Schiedsklausel zugunsten CAS/DIS sind grundsätzlich wirksam (BGH, Urt. v. 07.06.2016 – KZR 6/15, BGHZ 210, 292 = NJW 2016, 2266 = SchiedsVZ 2016, 268 – *Pechstein/ISU*, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-06-07&Aktenzeichen=KZR%206/15)); bei "strukturellem Ungleichgewicht" Inhaltskontrolle:

- Verband hat Monopolstellung in der Sportart
- Athletin muss zustimmen, um an Wettkämpfen teilzunehmen
- Auswahl der Schiedsrichter / Verfahrensgestaltung muss neutralitätswahrend sein
- EGMR, Urt. v. 02.10.2018 – Nr. 40575/10 und 67474/10, ECLI:CE:ECHR:2018:1002JUD004057510 (*Mutu und Pechstein/Schweiz*): öffentliche Verhandlung in Disziplinarsachen nach Art. 6 Abs. 1 EMRK ([hudoc.echr.coe.int](https://hudoc.echr.coe.int/eng?i=001-186828))
- Verfassungsrechtliche Fortsetzung: BVerfG, Beschl. v. 03.06.2022 – 1 BvR 2103/16 (*Pechstein*): Der BGH hat den Justizgewährungsanspruch (Art. 2 Abs. 1 iVm Art. 20 Abs. 3 GG) verletzt; die Schiedsvereinbarung muss rechtsstaatliche Mindeststandards — insbesondere die vom EGMR geforderte öffentliche Verhandlung — wahren ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2022-06-03&Aktenzeichen=1%20BvR%202103/16))

Konsequenz für die Verteidigung: Einrede der Unwirksamkeit der Schiedsklausel öffnet den Weg zum staatlichen Gericht.

### 5. Rechtsbehelfsweg

| Sanktion | Erstinstanzlicher Rechtsbehelf | Frist |
|---|---|---|
| Vereinsausschluss aus e.V. | Anfechtungsklage vor LG (§ 32 BGB / § 246 AktG analog) | **1 Monat** ab Zugang `[unverifiziert]` |
| MV-Beschluss (z. B. Beitragserhöhung) | Anfechtungsklage vor LG | 1 Monat analog § 246 AktG |
| Verbandssperre Profisportler | verbandsinterne Berufung → DIS / CAS | satzungs-/regelwerkabhängig; CAS: **21 Tage** |
| Stadionverbot | Unterlassungs-/Beseitigungsklage AG/LG; §§ 858, 1004 BGB | §§ 195, 199 BGB (3 Jahre) |
| Schiedsspruch | Aufhebungsantrag OLG, **§§ 1059, 1062 ZPO** | **3 Monate** ab Zustellung |

### 6. Stadionverbot — zivilrechtliche Sonderlage

Stadionverbote werden auf das **Hausrecht** des Veranstalters gestützt (§§ 858, 903, 1004 BGB analog). BGH, Urt. v. 30.10.2009 – V ZR 253/08, NJW 2010, 534 = SpuRt 2010, 28 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2009-10-30&Aktenzeichen=V%20ZR%20253/08)): Hausrechtsausübung darf nicht willkürlich erfolgen, ein sachlicher Grund ist erforderlich; präventive Stadionverbote sind auch ohne strafrechtliche Verurteilung zulässig. BVerfG, Beschl. v. 11.04.2018 – 1 BvR 3080/09, BVerfGE 148, 267 = NJW 2018, 1667 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2018-04-11&Aktenzeichen=1%20BvR%203080/09)) bestätigt die mittelbare Drittwirkung des Art. 3 Abs. 1 GG bei Veranstaltungen, die ohne Ansehen der Person einem großen Publikum geöffnet werden. Bundesweite Stadionverbote über DFB-Richtlinien — Inhaltskontrolle nach §§ 305 ff. BGB möglich, wenn Eintrittskarten-AGB sie einbeziehen.

### 7. Anfechtungsfrist und Rechtsmittel

- Vereinsausschluss e.V.: 1 Monat ab Zugang (analog § 246 AktG; st. Rspr. `[unverifiziert]`); nach manchen Stimmen unverzüglich iSv § 121 BGB.
- ZPO § 232 für die Schiedsverfahrensbeschwerde / Aufhebung.
- Bei einstweiligem Rechtsschutz: §§ 935, 940 ZPO — vor Saison-/Wettkampfentscheidung dringend prüfen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 25 BGB](https://www.gesetze-im-internet.de/bgb/__25.html) (Verfassung des Vereins)
- [§ 27 BGB](https://www.gesetze-im-internet.de/bgb/__27.html) (Vorstand)
- [§ 32 BGB](https://www.gesetze-im-internet.de/bgb/__32.html) (Mitgliederversammlung)
- [§ 39 BGB](https://www.gesetze-im-internet.de/bgb/__39.html) (Austritt aus dem Verein)
- [§§ 138, 242 BGB](https://www.gesetze-im-internet.de/bgb/__138.html) (Inhaltskontrolle Satzung)
- [§ 858 BGB](https://www.gesetze-im-internet.de/bgb/__858.html), [§ 1004 BGB](https://www.gesetze-im-internet.de/bgb/__1004.html) (Hausrecht / Stadionverbot)
- [§ 246 AktG](https://www.gesetze-im-internet.de/aktg/__246.html) (Anfechtungsfrist analog)
- [Art. 9 III GG](https://www.gesetze-im-internet.de/gg/art_9.html), [Art. 12 GG](https://www.gesetze-im-internet.de/gg/art_12.html), [Art. 5 GG](https://www.gesetze-im-internet.de/gg/art_5.html)
- [§§ 1025 ff. ZPO](https://www.gesetze-im-internet.de/zpo/__1025.html), insb. § 1059 (Aufhebung Schiedsspruch)
- AGG (Diskriminierungsschutz Athleten / Stadionbesucher)

### Kommentare und Handbücher

- Reichert, Vereins- und Verbandsrecht, X. Aufl. Jahr, Rn. 1 ff. zu Disziplinarmaßnahmen
- Sauter/Schweyer/Waldner, Der eingetragene Verein, X. Aufl. Jahr, Rn. 1 ff. zum Ausschluss
- Pfister, in: Pfister/Steiner, Sportrecht-Kommentar, X. Aufl. Jahr, BGB §§ 25 ff. Rn. 1 ff.
- Vieweg/Steinbach, Sportrecht, Loseblatt, Stand Jahr, Kap. Verbandsstrafgewalt
- Summerer, in: Fritzweiler/Pfister/Summerer, Praxishandbuch Sportrecht, X. Aufl. Jahr, Kap. Verbandsgerichtsbarkeit
- MüKoBGB / Leuschner, § 25 BGB Rn. 1 ff. (Bandes 1, 9. Aufl. 2021)

### Rechtsprechung

1. BGH, Urt. v. 30.10.2009 – V ZR 253/08, NJW 2010, 534 = SpuRt 2010, 28 (Stadionverbot – sachlicher Grund, keine Willkür), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2009-10-30&Aktenzeichen=V%20ZR%20253/08)
2. BVerfG, Beschl. v. 11.04.2018 – 1 BvR 3080/09, BVerfGE 148, 267 = NJW 2018, 1667 (Stadionverbot – mittelbare Drittwirkung Art. 3 Abs. 1 GG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2018-04-11&Aktenzeichen=1%20BvR%203080/09)
3. BGH, Urt. v. 07.06.2016 – KZR 6/15, BGHZ 210, 292 = NJW 2016, 2266 (*Pechstein/ISU* – Schiedsklausel), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-06-07&Aktenzeichen=KZR%206/15)
4. OLG München, Urt. v. 15.01.2015 – U 1110/14 Kart, SchiedsVZ 2015, 40 = SpuRt 2015, 78 (*Pechstein/ISU* – Vorinstanz, Schiedsklausel kartellrechtswidrig), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=U%201110/14%20Kart)
5. EGMR, Urt. v. 02.10.2018 – Nr. 40575/10 und 67474/10, ECLI:CE:ECHR:2018:1002JUD004057510 (*Mutu und Pechstein/Schweiz*), [hudoc.echr.coe.int](https://hudoc.echr.coe.int/eng?i=001-186828)
6. BVerfG, Beschl. v. 03.06.2022 – 1 BvR 2103/16 (*Pechstein* – Justizgewährungsanspruch, rechtsstaatliche Mindeststandards der Sportschiedsgerichtsbarkeit), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2022-06-03&Aktenzeichen=1%20BvR%202103/16)
7. BGH zur Inhaltskontrolle der Vereinssatzung (st. Rspr.) `[unverifiziert – kein Aktenzeichen aus öffentlicher Primärquelle belegt; in juris/Beck-Online ermitteln]`
8. BGH (Kartellsenat) zum Reit-/Pferdesport `[unverifiziert – weder Aktenzeichen noch Entscheidungsname bestätigt; die im Researcher genannte „Bundesligaentscheidung Reiten" ist nicht belegt]`

## Ausgabeformat

```
ANFECHTUNG / BESCHWERDE — Vereins-/Verbandssanktion
Mandant/in: <Pseudonym>   Verband/Verein: <…>   Sanktion: <…>

I. Sachverhalt
   - Sanktionsentscheidung: <Datum, Organ, Az.>
   - Verfahrensgang: <Anhörung ja/nein, Schriftform, Begründung>
   - Mitgliedschaftsverhältnis / Schiedsklausel: <…>

II. Anwendbares Regelwerk
    Satzung § … iVm Verfahrensordnung § …; Mitgliedschaft seit …

III. Formelle Rechtmäßigkeit
     1. Zuständigkeit
     2. Anhörungsrecht  [🔴 BLOCKER falls fehlend]
     3. Bestimmtheit der Norm
     4. Form, Begründung, Rechtsmittelbelehrung
     5. 2-Instanzen-Erfordernis (bei Bundesverband)

IV. Materielle Rechtmäßigkeit
    1. Tatbestand
    2. Verhältnismäßigkeit
    3. Inhaltskontrolle §§ 138, 242 BGB
    4. Grundrechtskonforme Auslegung (Art. 12, 5, 3, 9 III GG)

V. Schiedsklausel
   - Wirksamkeit nach Pechstein-Linie
   - ggf. Einrede der Unwirksamkeit

VI. Rechtsbehelf
    [ ] Verbandsinterne Berufung   Frist: <…>
    [ ] Schiedsklage DIS/CAS       Frist: <…>
    [ ] Anfechtungsklage LG         Frist: 1 Monat (analog § 246 AktG)
    [ ] Aufhebungsantrag §§ 1059 ZPO Frist: 3 Monate
    [ ] eA §§ 935, 940 ZPO

VII. Anträge

VIII. Fristkalender
      - Anfechtungsfrist:       <Datum>
      - CAS-Berufung:           <Datum>
      - Aufhebungsantrag:       <Datum>
      - Saisonbeginn / eA-Bedarf: <Datum>

IX. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

X. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Anhörung übergangen** vom Vereins-/Verbandsorgan → Sanktion idR aufhebbar; aber: Heilung durch Anhörung im Berufungsverfahren möglich (`[unverifiziert]`).
- **1-Monats-Frist analog § 246 AktG versäumt** → Heilung der Sanktion; konsequente Wiedervorlage in der Kanzlei.
- **Schiedsklausel kritiklos akzeptiert** → keine Pechstein-Einrede.
- **Verhältnismäßigkeit nicht geprüft**: Ausschluss als ultima ratio — Verwarnung / Geldbuße zumutbar?
- **Stadionverbot mit § 823 BGB statt § 1004 BGB iVm § 858 BGB** angegriffen → falsche Anspruchsgrundlage.
- **Einstweiliger Rechtsschutz vergessen** vor wichtigem Wettkampf → Hauptsacheverfahren zu spät.
- **Satzungsgrundlage** nicht geprüft: Disziplinarsanktion ohne Satzungsbasis ist nichtig.
