---
name: konkurrentenstreit-borghei
title: /beamten-disziplinarrecht:konkurrentenstreit
description: Beamtenrechtlicher Konkurrentenstreit um ein Beförderungs- oder Einstellungsamt – Bestenauslese Art. 33 Abs. 2 GG, dienstliche Beurteilungen als Auswahlgrundlage, Anforderungsprofil, Auswahlvermerk und Dokumentationspflicht, Bewerbungsverfahrensanspruch, Konkurrentenmitteilung und Wartefrist, einstweilige Anordnung § 123 VwGO, Grundsatz der Ämterstabilität und seine Durchbrechung, Rechtsschutz nach Ernennung. Use when eine Mandantin oder ein Mandant in einem Auswahlverfahren um ein öffentliches Amt unterlegen ist und die Ernennung des Mitbewerbers verhindert oder angegriffen werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/beamten-disziplinarrecht/skills/konkurrentenstreit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /beamten-disziplinarrecht:konkurrentenstreit

## Zweck

Der Skill prüft die Rechtmäßigkeit einer beamtenrechtlichen Auswahlentscheidung und sichert den Rechtsschutz des unterlegenen Bewerbers. Der praktisch allein wirksame Rechtsbehelf ist die **einstweilige Anordnung nach § 123 VwGO vor der Ernennung**: Ist der Mitbewerber erst ernannt, sperrt der Grundsatz der Ämterstabilität den Zugriff auf das Amt. Der Skill arbeitet deshalb fristgetrieben und erzeugt den Eilantrag mit getrenntem Anordnungsanspruch und Anordnungsgrund.

## Eingaben

- Dienstherr (Bund / Land / Kommune) und ausgeschriebenes Amt (Besoldungsgruppe, Statusamt, Dienstposten)
- Ausschreibungstext mit Anforderungsprofil
- Konkurrentenmitteilung: Datum des Zugangs, gesetzte Wartefrist, benannter Auswahlgrund
- Eigene und — soweit bekannt — fremde Beurteilungen (Stichtag, Gesamtnote, Statusamt)
- Auswahlvermerk, soweit übersandt oder eingesehen
- Bereits erfolgte Ernennung? Datum der Aushändigung der Urkunde
- Etwaige Schwerbehinderung, Gleichstellung, Frauenförderplan, Personalratsbeteiligung

## Sub-Agent-Architektur

Ein Researcher bestimmt den Rechtskreis (Bund oder Land), sammelt Art. 33 Abs. 2 GG, § 9 BBG bzw. § 9 BeamtStG, die einschlägige Laufbahn- und Beurteilungsregelung sowie die Rechtsprechung des 2. Senats des BVerwG und des 2. Senats des BVerfG. Ein Drafter prüft Anordnungsanspruch und Anordnungsgrund getrennt und entwirft den Antrag nach § 123 VwGO nebst eidesstattlicher Versicherung. Ein Reviewer kontrolliert die Wartefrist, die Vollständigkeit der Fehlerrügen, die Kausalität des Fehlers für das Auswahlergebnis und jede Fundstelle; nicht bestätigte Entscheidungen werden mit `[unverifiziert - prüfen]` markiert. Keine Rolle erfindet ein Aktenzeichen.

## Ablauf

### 1. Anwendbares Recht bestimmen ([§ 1 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__1.html))

**Erster Schritt, ohne Ausnahme.** Art. 33 Abs. 2 GG gilt für alle Dienstherren; das einfache Recht nicht:

| Dienstherr | Auswahlnorm | Laufbahn-/Beurteilungsrecht |
|---|---|---|
| Bund | [§ 9 BBG](https://www.gesetze-im-internet.de/bbg_2009/__9.html) | BLV, Beurteilungsrichtlinien der Behörde |
| Land, Kommune | [§ 9 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__9.html) + Landesbeamtengesetz | Landeslaufbahnverordnung, landesrechtliche Beurteilungsrichtlinien |

Landesrechtliche Besonderheiten — insbesondere zu Frauenförderung, Wartefristen und Beteiligung der Schwerbehindertenvertretung — sind konkret zu ermitteln `[unverifiziert - prüfen]` je Land.

### 2. Bestenauslese als Anspruchsgrundlage ([Art. 33 Abs. 2 GG](https://www.gesetze-im-internet.de/gg/art_33.html))

Jeder Deutsche hat nach Eignung, Befähigung und fachlicher Leistung gleichen Zugang zu jedem öffentlichen Amt. Diese drei Kriterien sind **abschließend**. Sachfremde Erwägungen — Dienstalter als solches, Proporz, Verwendungswünsche der Behörde, Haushaltsgesichtspunkte — sind unzulässig, soweit sie nicht ihrerseits an Eignung, Befähigung oder Leistung anknüpfen.

Aus Art. 33 Abs. 2 GG iVm Art. 19 Abs. 4 GG folgt der **Bewerbungsverfahrensanspruch**: ein subjektives Recht auf eine rechtsfehlerfreie Auswahlentscheidung. Er gibt **keinen** Anspruch auf das Amt, wohl aber auf ein ordnungsgemäßes Verfahren und darauf, dass das Amt nicht besetzt wird, bevor über den Anspruch effektiv entschieden werden konnte (BVerfG, Beschl. v. 29.07.2003 – 2 BvR 311/03, BVerfGK 1, 292 = NVwZ 2004, 95, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=29.07.2003&Aktenzeichen=2%20BvR%20311/03)).

### 3. Beurteilungen als Auswahlgrundlage ([§ 21 BBG](https://www.gesetze-im-internet.de/bbg_2009/__21.html))

Regelmäßiger Erkenntnisträger ist die aktuelle dienstliche Beurteilung. Zu prüfen sind:

- **Aktualität** — die Beurteilung muss den gegenwärtigen Leistungsstand abbilden; bei veralteter Regelbeurteilung ist eine Anlassbeurteilung geboten.
- **Vergleichbarkeit** — gleicher Beurteilungszeitraum, gleicher Beurteilungsmaßstab, gleiche Vergleichsgruppe.
- **Statusamtsbezug** — eine Beurteilung im höheren Statusamt wiegt bei gleicher Note grundsätzlich schwerer; das ist zu begründen, nicht zu unterstellen.
- **Ausschöpfung** — bei gleicher Gesamtnote sind die Einzelmerkmale inhaltlich auszuwerten („Binnendifferenzierung"), bevor Hilfskriterien greifen.

Ist die eigene Beurteilung selbst fehlerhaft, ist sie zusätzlich gesondert anzugreifen: `/beamten-disziplinarrecht:dienstliche-beurteilung`.

### 4. Anforderungsprofil und Auswahlvermerk ([Art. 33 Abs. 2 GG](https://www.gesetze-im-internet.de/gg/art_33.html))

Ein **konstitutives** Anforderungsprofil engt den Bewerberkreis ein und muss durch die Aufgaben des Amtes sachlich gerechtfertigt sein; ein bloß beschreibendes Profil tut das nicht. Die Auswahlentscheidung ist **vor** der Ernennung schriftlich zu dokumentieren, so dass die maßgeblichen Erwägungen für den unterlegenen Bewerber und das Gericht nachvollziehbar werden. Eine erst im Prozess nachgeschobene Begründung heilt den Dokumentationsmangel nicht (BVerwG, Beschl. v. 20.06.2013 – 2 VR 1.13, BVerwGE 147, 20 = NVwZ 2014, 75).

Typische Fehlerbilder: Auswahlvermerk fehlt oder besteht aus einem Satz; Vergleich nur der Gesamtnoten ohne Ausschöpfung; Hilfskriterien vor Ausschöpfung; Anforderungsprofil auf den Wunschkandidaten zugeschnitten; Beteiligung von Personalrat oder Schwerbehindertenvertretung unterblieben.

### 5. Konkurrentenmitteilung und Wartefrist ([Art. 19 Abs. 4 GG](https://www.gesetze-im-internet.de/gg/art_19.html))

Der Dienstherr muss den unterlegenen Bewerber vor der Ernennung unterrichten und ihm eine Frist einräumen, in der er Eilrechtsschutz erlangen kann. Diese **Wartefrist ist die kritischste Frist des Gebiets**. Praxisregel: Antrag nach § 123 VwGO sofort nach Zugang der Mitteilung anhängig machen, notfalls zunächst mit vorläufiger Begründung, und den Dienstherrn schriftlich um Zusicherung bitten, bis zur gerichtlichen Entscheidung nicht zu ernennen. Parallel Akteneinsicht in Auswahlvermerk und Beurteilungen der Mitbewerber verlangen.

### 6. Einstweilige Anordnung ([§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html))

Statthaft ist die **Sicherungsanordnung** nach § 123 Abs. 1 S. 1 VwGO, gerichtet auf Freihaltung der Stelle.

- **Anordnungsanspruch**: Der Bewerbungsverfahrensanspruch ist verletzt, und die Auswahl des Antragstellers erscheint bei fehlerfreier Wiederholung **möglich**. Ein Erfolg in der Sache muss nicht überwiegend wahrscheinlich sein — es genügt, dass die Auswahl nicht ausgeschlossen ist. Das ist der entscheidende Hebel des Eilverfahrens.
- **Anordnungsgrund**: Die bevorstehende Ernennung schafft wegen der Ämterstabilität vollendete Tatsachen.
- **Kein Vorwegnahmeverbot**: Der Antrag zielt nicht auf das Amt, sondern auf Freihaltung — deshalb liegt keine unzulässige Vorwegnahme der Hauptsache vor.
- Glaubhaftmachung nach § 123 Abs. 3 VwGO iVm §§ 920, 294 ZPO durch eidesstattliche Versicherung.

### 7. Ämterstabilität und ihre Durchbrechung ([Art. 33 Abs. 2 GG](https://www.gesetze-im-internet.de/gg/art_33.html))

Ist der Mitbewerber ernannt, ist der Bewerbungsverfahrensanspruch grundsätzlich untergegangen; die Ernennung ist als solche bestandskräftig und wird nicht rückabgewickelt (**Grundsatz der Ämterstabilität**). Eine **Durchbrechung** kommt in Betracht, wenn der Dienstherr den Rechtsschutz des unterlegenen Bewerbers vereitelt hat — etwa durch Ernennung ohne oder vor Ablauf der Wartefrist oder während des laufenden Eilverfahrens (BVerwG, Urt. v. 04.11.2010 – 2 C 16.09, BVerwGE 138, 102 = NJW 2011, 695).

### 8. Rechtsschutz nach Ernennung und Sekundäransprüche ([§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html))

Ist die Durchbrechung nicht zu erreichen, verbleiben:

- Fortsetzung des Verfahrens auf **erneute Auswahlentscheidung** bezogen auf ein weiteres freies Amt, soweit vorhanden;
- **Schadensersatz** wegen Verletzung des Bewerbungsverfahrensanspruchs aus dem Beamtenverhältnis, gerichtet auf Besoldungsdifferenz — Voraussetzung ist, dass der Bewerber bei fehlerfreier Auswahl **voraussichtlich** ausgewählt worden wäre und dass er es nicht schuldhaft unterlassen hat, den Schaden durch Eilrechtsschutz abzuwenden (Rechtsgedanke des § 839 Abs. 3 BGB) `[unverifiziert - prüfen]`;
- Amtshaftung nach § 839 BGB iVm [Art. 34 GG](https://www.gesetze-im-internet.de/gg/art_34.html) vor den ordentlichen Gerichten.

Die **Obliegenheit zum Eilrechtsschutz** ist der Grund, warum ein versäumter § 123-Antrag regelmäßig auch den Sekundäranspruch zerstört.

## Quellen

### Statute

- [Art. 33 GG](https://www.gesetze-im-internet.de/gg/art_33.html), [Art. 19 GG](https://www.gesetze-im-internet.de/gg/art_19.html), [Art. 34 GG](https://www.gesetze-im-internet.de/gg/art_34.html)
- [§ 9 BBG](https://www.gesetze-im-internet.de/bbg_2009/__9.html), [§ 21 BBG](https://www.gesetze-im-internet.de/bbg_2009/__21.html)
- [§ 9 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__9.html), [§ 8 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__8.html)
- [§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html), [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html)
- Landesbeamtengesetze und Laufbahnverordnungen der Länder (konkret zu zitieren) `[unverifiziert - prüfen]`

### Kommentare

- Battis, BBG, § 9 Rn. 1 ff.
- von Roetteken, in: von Roetteken/Rothländer, BeamtStG, § 9 Rn. 1 ff.
- Schnellenbach/Bodanowitz, Beamtenrecht in der Praxis, Kap. Auswahlentscheidung.
- Kopp/Schenke, VwGO, § 123 Rn. 1 ff.
- Plog/Wiedow, BBG, § 9 Rn. 1 ff.

### Rechtsprechung

1. BVerfG, Beschl. v. 29.07.2003 – 2 BvR 311/03, BVerfGK 1, 292 = NVwZ 2004, 95 (effektiver Rechtsschutz im beamtenrechtlichen Auswahlverfahren), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=29.07.2003&Aktenzeichen=2%20BvR%20311/03)
2. BVerwG, Beschl. v. 20.06.2013 – 2 VR 1.13, BVerwGE 147, 20 = NVwZ 2014, 75 (Anforderungen an Auswahlentscheidung und Dokumentation) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2013-06-20&Aktenzeichen=2%20VR%201.13))
3. BVerwG, Urt. v. 04.11.2010 – 2 C 16.09, BVerwGE 138, 102 = NJW 2011, 695 (Ämterstabilität, Durchbrechung bei Rechtsschutzvereitelung) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2010-11-04&Aktenzeichen=2%20C%2016.09))
4. Zur landesrechtlichen Ausgestaltung der Wartefrist ist die Rechtsprechung des zuständigen OVG heranzuziehen `[unverifiziert - prüfen]`

## Ausgabeformat

```
KONKURRENTENSTREIT — <Mandat> — <Datum>

I.   Anwendbares Recht
     Dienstherr:              <Bund / Land <X> / Kommune>
     Auswahlnorm:             <§ 9 BBG | § 9 BeamtStG> iVm Art. 33 Abs. 2 GG
     Beurteilungsregime:      <BLV | Landesrichtlinie>

II.  Verfahrensstand und Frist
     Konkurrentenmitteilung:  zugegangen am <Datum>
     Wartefrist endet:        <Datum>   ← FRISTBLOCK
     Ernennung erfolgt:       [nein / ja am <Datum>]

III. Auswahlgrundlage
     Eigene Beurteilung:      <Stichtag / Note / Statusamt>
     Ausgewählter Bewerber:   <Note / Statusamt, soweit bekannt>
     Anforderungsprofil:      [konstitutiv / beschreibend / fehlt]
     Auswahlvermerk:          [vorhanden / unzureichend / fehlt]

IV.  Fehlerrügen
     1. <Fehler>            — Kausalität für das Ergebnis: <…>
     2. <Fehler>            — Kausalität für das Ergebnis: <…>

V.   Eilrechtsschutz § 123 VwGO
     Anordnungsanspruch:      [+ / – ] <Begründung>
     Anordnungsgrund:         [+ / – ] <Begründung>
     Glaubhaftmachung:        <eidesstattliche Versicherung / Unterlagen>
     Zuständiges Gericht:     VG <Ort>

VI.  Nach Ernennung
     Ämterstabilität:         [greift / durchbrochen wegen <…>]
     Sekundäransprüche:       <Schadensersatz / Amtshaftung>

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Antrag nach § 123 VwGO (Gerüst)

```
An das Verwaltungsgericht <Ort>

Antrag auf Erlass einer einstweiligen Anordnung

des/der <Antragsteller/in>
gegen die <Dienstherr>, vertreten durch <…>

Namens und in Vollmacht beantrage ich:

   Dem Antragsgegner wird im Wege der einstweiligen Anordnung untersagt,
   das mit Ausschreibung vom <Datum> ausgeschriebene Amt einer/eines
   <Amtsbezeichnung, Besoldungsgruppe> mit der/dem Beigeladenen oder
   einer anderen Bewerberin bzw. einem anderen Bewerber zu besetzen,
   bis über die Bewerbung der Antragstellerin bzw. des Antragstellers
   unter Beachtung der Rechtsauffassung des Gerichts erneut entschieden
   worden ist.

Begründung:

I.   Sachverhalt und Verfahrensgang
II.  Zulässigkeit
     Statthaftigkeit § 123 Abs. 1 S. 1 VwGO (Sicherungsanordnung);
     Antragsbefugnis aus Art. 33 Abs. 2 GG iVm Art. 19 Abs. 4 GG.
III. Anordnungsanspruch
     1. Bewerbungsverfahrensanspruch aus Art. 33 Abs. 2 GG.
     2. Verletzung durch <Dokumentationsmangel / fehlende Ausschöpfung /
        unzulässiges Anforderungsprofil / veraltete Beurteilung>.
     3. Die Auswahl der Antragstellerin bzw. des Antragstellers erscheint
        bei fehlerfreier Wiederholung möglich, weil <…>.
IV.  Anordnungsgrund
     Die Ernennung steht unmittelbar bevor; nach dem Grundsatz der
     Ämterstabilität wäre der Rechtsschutz danach vereitelt.
V.   Glaubhaftmachung
     Eidesstattliche Versicherung vom <Datum> (Anlage AS 1);
     Konkurrentenmitteilung vom <Datum> (Anlage AS 2).
```

## Risiken / typische Fehler

- **Wartefrist verstreichen lassen.** Nach der Ernennung sperrt die Ämterstabilität den Zugriff auf das Amt; der Bewerbungsverfahrensanspruch geht unter. Dies ist der praktisch endgültige Fehler des Gebiets.
- **Bundes- und Landesrecht vermengt.** Art. 33 Abs. 2 GG gilt überall, § 9 BBG nur im Bund; landesrechtliche Wartefristen und Förderregelungen weichen ab.
- **Nur die Gesamtnote verglichen.** Ohne Ausschöpfung der Einzelmerkmale ist der Vergleich unvollständig; Hilfskriterien dürfen erst nach Ausschöpfung greifen.
- **Kausalität nicht dargelegt.** Ein Verfahrensfehler trägt den Antrag nur, wenn die eigene Auswahl bei fehlerfreier Wiederholung möglich erscheint.
- **Akteneinsicht nicht beantragt.** Ohne Auswahlvermerk und Vergleichsbeurteilungen ist die Fehlerrüge substanzlos.
- **Eilrechtsschutz versäumt und dann Schadensersatz verlangt.** Die Obliegenheit zum Primärrechtsschutz zerstört regelmäßig auch den Sekundäranspruch.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
