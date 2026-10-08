---
name: mstv-medienrechtspruefung-borghei
title: /urheber-medienrecht:mstv-medienrechtspruefung
description: Pflichtenprüfung für Diensteanbieter und journalistisch-redaktionelle Telemedien nach MStV (Impressum § 18, Trennungsgebot § 22, Sorgfaltspflichten § 19), Entwurf eines Gegendarstellungsantrags nach § 20 MStV/Landespressegesetz mit strenger Form-/Fristprüfung, Hilfsansprüche Berichtigung/Unterlassung iVm §§ 823 I, 1004 BGB und §§ 22, 23 KUG. Use when ein Diensteanbieter Pflichten auf Konformität prüfen lassen will oder ein Betroffener eine unrichtige Tatsachenbehauptung in einem journalistisch-redaktionellen Medium beanstanden möchte.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/urheber-medienrecht/skills/mstv-medienrechtspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /urheber-medienrecht:mstv-medienrechtspruefung

## Zweck

Der Skill prüft medienrechtliche Pflichten nach MStV und Landespressegesetzen — Impressum, Trennungsgebot, journalistisch-redaktionelle Sorgfaltspflichten — und entwirft auf Betroffenenseite Gegendarstellungsantrag, Berichtigungs- und Unterlassungsschreiben unter Abwägung mit der Presse-/Meinungsfreiheit (Art. 5 I GG). Schnittstellen: §§ 22, 23 KUG (Bildnis), DSA Art. 12 ff. (Plattformen), DSGVO-Medienprivileg Art. 85.

## Eingaben

- Medium: Tageszeitung / Zeitschrift / Online-Magazin / Rundfunk / Telemedium (journalistisch-redaktionell ja/nein)
- Sitz / einschlägiges Landespressegesetz (Art. 30 GG-Länderzuständigkeit)
- Konkrete Beanstandung (Tatsachenbehauptung vs. Werturteil; Bildnisveröffentlichung)
- Datum der Erstveröffentlichung, Zeitpunkt der Kenntnisnahme (Frist!)
- Position des Mandanten: Diensteanbieter (Pflichtenprüfung) / Betroffener (Reaktion)
- Bei Diensteanbieter-Prüfung: Geschäftsmodell, Impressum-Status quo

## Sub-Agent-Architektur

Researcher liefert MStV-Normen (§§ 18, 19, 20, 22, 78 ff.), das einschlägige Landespressegesetz (insb. Gegendarstellungs- und Auskunftsanspruch), §§ 22, 23 KUG, BGH VI ZS-Rspr. zum allgemeinen Persönlichkeitsrecht, BVerfG-Linie zu Presse-/Meinungsfreiheit. Drafter entwirft Pflichtenkatalog für Anbieter bzw. Gegendarstellungsantrag/Unterlassungsschreiben. Reviewer prüft Tatsachen-/Meinungs-Abgrenzung, Fristen, Form, Aktualität, Verhältnis zu Pressefreiheit.

## Ablauf

### 1. Anwendungsbereich

- **MStV** gilt bundesweit (Staatsvertrag aller Länder); Telemedien § 2 II Nr. 1 MStV.
- **Journalistisch-redaktionelle Telemedien** § 19 MStV: erhöhte Sorgfaltspflichten.
- **Landespressegesetze** für periodische Druckwerke (gestaffelt nach Sitz des Verlags); klassisch Gegendarstellungs-, Berichtigungs-, Auskunftsansprüche.
- **Rundfunk** §§ 92 ff. MStV (Zulassung).
- **Plattform-Schnittstelle** DSA (EU) 2022/2065 für sehr große Online-Plattformen und Suchmaschinen.

### 2. Impressumspflicht § 18 MStV

Pflichtinhalt:

1. Name und Anschrift des Diensteanbieters; bei juristischen Personen auch Vertretungsberechtigte,
2. Angaben zur schnellen elektronischen Kontaktaufnahme (E-Mail),
3. zuständige Aufsichtsbehörde (bei behördlicher Zulassung),
4. Handelsregister, Vereinsregister, Partnerschaftsregister mit Registernummer,
5. bei freien Berufen: gesetzliche Berufsbezeichnung, Staat, Kammer, berufsrechtliche Regelungen,
6. Umsatzsteuer-IdNr. bzw. Wirtschafts-IdNr.,
7. bei journalistisch-redaktionellen Telemedien: Verantwortlicher iSv § 18 II MStV mit Name und Anschrift.

Anforderungen: leicht erkennbar, unmittelbar erreichbar, ständig verfügbar (BGH `[unverifiziert]`).

### 3. Trennungsgebot § 22 MStV

Kommerzielle Kommunikation muss als solche klar erkennbar sein; redaktionelle Inhalte und Werbung sind eindeutig zu trennen (auch akustisch/optisch im Rundfunk; im Telemedienbereich Kennzeichnung „Anzeige" / „Werbung"). Verstoß: § 115 MStV-Bußgeld; Schnittstelle UWG (`wettbewerbsrecht`).

### 4. Journalistisch-redaktionelle Sorgfaltspflichten § 19 MStV

- Recherchepflicht: Nachrichten vor Verbreitung mit der nach den Umständen gebotenen Sorgfalt auf Wahrheit und Herkunft prüfen.
- Wahrheits- und Sachlichkeitsgebot; Trennung von Meldung und Kommentar.
- Bezugnahme auf den Pressekodex des Deutschen Presserats (nicht rechtsverbindlich, aber Maßstab der Sorgfaltspflicht).

### 5. Gegendarstellungsanspruch § 20 MStV / Landespressegesetz

**Voraussetzungen** (kumulativ — strenger Pflichtenkatalog):

1. **Tatsachenbehauptung** (keine Meinungsäußerung, keine Werbung, kein strafbarer Inhalt). Maßstab der Abgrenzung: Beweisbarkeit; BVerfG-Linie `[unverifiziert]`.
2. **Persönliche Betroffenheit**: Antragsteller muss durch die Behauptung individuell betroffen sein.
3. **Berechtigtes Interesse** an der Gegendarstellung (idR indiziert).
4. **Frist**: „unverzüglich, spätestens binnen 3 Monaten" ab Kenntnis (typische Landesregelung — Wortlaut variiert je Landespressegesetz; § 20 III MStV bei Telemedien `[unverifiziert – Landesregelung im Einzelfall prüfen]`).
5. **Form**: schriftlich, mit eigenhändiger Unterschrift, Bezug zur Erstmitteilung, Gegendarstellungstext im selben Umfang.
6. **Umfang**: nicht wesentlich länger als die beanstandete Mitteilung; auf konkrete Beanstandung beschränkt.
7. **Aktualität**: Beanstandung darf nicht überholt sein.
8. **Sachgerechte Wiedergabe**: Anspruch auf Veröffentlichung in derselben Aufmachung, am selben Ort.

**Inhaltsverbote** (Beispielkatalog, je Landesregelung):

- Meinungsäußerung als Gegendarstellung,
- werblicher Inhalt,
- strafbarer Inhalt,
- offensichtlich unwahre Gegenbehauptung.

### 6. Hilfsansprüche: Berichtigung / Unterlassung / Schadensersatz

- **Berichtigungsanspruch** (presserechtlich, ungeschrieben — st. BGH-Rspr. `[unverifiziert]`) bei nachweislich unwahren Tatsachenbehauptungen.
- **Unterlassungsanspruch** §§ 823 I, 1004 BGB analog iVm Art. 1 I, 2 I GG (allgemeines Persönlichkeitsrecht).
- **Schadensersatz** § 823 I BGB iVm aPR (materiell); Geldentschädigung („Schmerzensgeld") bei schwerwiegender Persönlichkeitsverletzung (BVerfG/BGH `[unverifiziert]`).
- **Schnittstelle § 22, 23 KUG** bei Bildnisveröffentlichung: Einwilligungserfordernis § 22; Ausnahmen § 23 (insb. Nr. 1 „Bildnisse aus dem Bereich der Zeitgeschichte" — abgestuftes Schutzkonzept BVerfG „Caroline von Monaco III", Urt. v. 26.02.2008 – 1 BvR 1602/07 ua, BVerfGE 120, 180, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2008-02-26&Aktenzeichen=1%20BvR%201602/07)).

### 7. Abwägung Pressefreiheit Art. 5 I GG

- Schutzbereich Presse-/Rundfunk-/Telemedienfreiheit.
- Schranken Art. 5 II GG (allgemeine Gesetze, gesetzliche Bestimmungen zum Schutz der Jugend, Recht der persönlichen Ehre).
- **Wechselwirkungslehre** (Lüth-Doktrin, BVerfG, Urt. v. 15.01.1958 – 1 BvR 400/51, BVerfGE 7, 198, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-01-15&Aktenzeichen=1%20BvR%20400/51)): Einschränkende Gesetze sind im Lichte der Pressefreiheit auszulegen.
- Bei Berichterstattung über die Privatsphäre: BVerfG-Linie, sphärentheoretisch (Sozial-, Privat-, Intimsphäre).

### 8. Plattform- / DSA-Schnittstelle

- DSA Art. 16 ff.: Notice-and-Action-Verfahren bei illegalen Inhalten.
- DSA Art. 23: nationale Beschwerdestellen.
- NetzDG-Reste: weiterhin punktuell anwendbar.

### 9. Aufsicht

- **Landesmedienanstalten** als Aufsicht über Rundfunk und journalistisch-redaktionelle Telemedien.
- Bußgeldkatalog § 115 MStV.
- Deutscher Presserat (Selbstkontrolle Print/Online).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 18 MStV (Telemedien — Impressumspflicht)](https://www.die-medienanstalten.de/fileadmin/user_upload/Rechtsgrundlagen/Gesetze_aktuell/Medienstaatsvertrag_MStV.pdf) `[unverifiziert – aktuelle Konsolidierung prüfen]`
- § 19 MStV (Sorgfaltspflichten)
- § 20 MStV (Gegendarstellung Telemedien)
- § 22 MStV (Werbetrennung)
- §§ 78 ff. MStV (Telemedienpflichten)
- §§ 92 ff. MStV (Rundfunkzulassung)
- Landespressegesetze (z. B. [LPresseG NRW](https://recht.nrw.de/lmi/owa/br_text_anzeigen?v_id=66819670911102739), [BayPrG](https://www.gesetze-bayern.de/Content/Document/BayPrG)) — länderspezifisch
- [§ 22 KUG](https://www.gesetze-im-internet.de/kunsturhg/__22.html), [§ 23 KUG](https://www.gesetze-im-internet.de/kunsturhg/__23.html)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html), [§ 1004 BGB](https://www.gesetze-im-internet.de/bgb/__1004.html)
- [Art. 5 GG](https://www.gesetze-im-internet.de/gg/art_5.html)
- [DSA VO (EU) 2022/2065](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065)
- [Art. 85 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Medienprivileg)

### Kommentare

- Fechner, Medienrecht, 23. Aufl. 2024 `[unverifiziert]`
- Paschke/Berlit/Meyer, Hamburger Kommentar Gesamtes Medienrecht, 4. Aufl. 2021 `[unverifiziert]`
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2019 `[unverifiziert]`
- Soehring/Hoene, Presserecht, 6. Aufl. 2019 `[unverifiziert]`
- Wandtke/Ohst, Medienrecht Praxishandbuch, 4. Aufl. 2024 `[unverifiziert]`
- BeckOK Informations- und Medienrecht/Gersdorf/Paal, Stand 2024

### Rechtsprechung

1. BVerfG, Urt. v. 15.01.1958 – 1 BvR 400/51, BVerfGE 7, 198 – „Lüth" (Wechselwirkungslehre), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1958-01-15&Aktenzeichen=1%20BvR%20400/51)
2. BVerfG, Beschl. v. 14.02.1973 – 1 BvR 112/65, BVerfGE 34, 269 – „Soraya" (richterliche Rechtsfortbildung Geldentschädigung bei aPR), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1973-02-14&Aktenzeichen=1%20BvR%20112/65)
3. BVerfG, Urt. v. 26.02.2008 – 1 BvR 1602/07, 1606/07, 1626/07, BVerfGE 120, 180 – „Caroline von Monaco III" (abgestuftes Schutzkonzept Bildnis), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2008-02-26&Aktenzeichen=1%20BvR%201602/07)
4. BVerfG, Beschl. v. 14.01.1998 – 1 BvR 1861/93 ua, BVerfGE 97, 125 – „Caroline von Monaco I" (Gegendarstellung auf der Titelseite), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1998-01-14&Aktenzeichen=1%20BvR%201861/93)
5. BVerfG, Beschl. v. 08.02.1983 – 1 BvL 20/81, BVerfGE 63, 131 – „Gegendarstellung" (Gegendarstellungsanspruch im Rundfunk), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1983-02-08&Aktenzeichen=1%20BvL%2020/81)
6. BVerfG, Urt. v. 15.12.1999 – 1 BvR 653/96, BVerfGE 101, 361 – „Caroline von Monaco II" (Privatsphäre, Bildberichterstattung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=1999-12-15&Aktenzeichen=1%20BvR%20653/96)
7. BGH, Urt. v. 15.11.1994 – VI ZR 56/94, BGHZ 128, 1 – „Caroline von Monaco I" (Geldentschädigung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=1994-11-15&Aktenzeichen=VI%20ZR%2056/94)
8. BGH (VI. ZS-Linie) zum Online-Archiv und Recht auf Vergessenwerden `[unverifiziert]`
9. EuGH, Urt. v. 24.09.2019 – Rs. C-507/17, ECLI:EU:C:2019:772 – Google (Räumliche Reichweite der Auslistung) (Recht auf Vergessenwerden), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-09-24&Aktenzeichen=C-507/17)

## Ausgabeformat

### Variante A — Diensteanbieter-Pflichtenkatalog

```
PFLICHTENPRÜFUNG — MStV / Landespressegesetz
Anbieter: <…>     Angebot: <…>

I. Sachverhalt / Angebot
II. Anwendungsbereich (Telemedium / journalistisch-redaktionell / Rundfunk)

III. Pflichtenmatrix
     Pflicht                       Status   Norm           Befund
     ───────────────────────────────────────────────────────────────
     Impressum (Pflichtangaben)    [✅/❌]   § 18 MStV      <…>
     Trennungsgebot                [✅/❌]   § 22 MStV      <…>
     Sorgfaltspflichten            [✅/❌]   § 19 MStV      <…>
     Verantwortlicher § 18 II MStV [✅/❌]                  <…>
     Aufsichtsmeldung              [✅/❌]                  <…>
     DSA Notice-and-Action         [✅/❌]   Art. 16 DSA    <…>

IV. Empfehlungen
V. Risikoeinstufung 🟢/🟡/🔴
VI. Quellenverzeichnis
```

### Variante B — Gegendarstellungsantrag

```
GEGENDARSTELLUNGSANTRAG
gem. § 20 MStV / § <…> LPresseG <Land>

An die <…>-Redaktion / verantwortlichen Redakteur
<Datum, unverzüglich nach Kenntnis>

In Sachen <Mandant>
Bezug: <Mediumsname>, Ausgabe/URL vom <Datum>, Seite <…>, Artikel
       „<Überschrift>"

Sehr geehrte Damen und Herren,

namens und im Auftrag unserer Mandantschaft fordern wir Sie hiermit
auf, folgende Gegendarstellung in der nächsten Ausgabe / unverzüglich
auf derselben URL in derselben Aufmachung zu veröffentlichen:

   ─────────────────  GEGENDARSTELLUNG  ─────────────────

   In Ihrem Artikel „<…>" vom <Datum> behaupten Sie:
        „<wörtliches Zitat der Tatsachenbehauptung>"

   Hierzu stelle ich fest:
        „<konkrete Tatsachengegendarstellung — gleiche Länge,
          keine Meinung, keine Wertung, keine Werbung>"

   <Ort, Datum>
   <eigenhändige Unterschrift Mandant>

   ──────────────────────────────────────────────────────

Rechtsgrundlage: § 20 MStV / § <…> LPresseG <Land>.

Frist: Wir setzen Ihnen Frist bis zum <Datum> zur Bestätigung der
Veröffentlichung. Bei Nichtveröffentlichung werden wir den Antrag
im Wege des § 935, 940 ZPO durchsetzen.

Mit freundlichen Grüßen
<Anwalt>

Anlagen: Vollmacht, Belegexemplar
```

## Risiken / typische Fehler

- **Gegendarstellung als Meinungsäußerung getarnt** → unbegründet, kein Anspruch.
- **Werblicher Inhalt** in der Gegendarstellung → unbegründet.
- **Frist „unverzüglich, spätestens 3 Monate"** verpasst → Aktualitätsverlust → Antrag unzulässig.
- **Form** (eigenhändige Unterschrift des Betroffenen, nicht des Anwalts) verletzt → unwirksam.
- **Umfang** wesentlich länger als die beanstandete Mitteilung → unzulässig.
- **Pauschale Anwendung des MStV ohne Prüfung des einschlägigen Landespressegesetzes** bei Printmedien → falsche Anspruchsgrundlage.
- **Impressumspflicht-Prüfung ohne Differenzierung** journalistisch-redaktionell vs. allgemeines Telemedium → fehlender Verantwortlicher.
- **Bildnisveröffentlichung** ohne KUG-Prüfung (Einwilligung / Zeitgeschichte / abgestuftes Schutzkonzept).
- **Übersehen des DSGVO-Medienprivilegs** Art. 85 DSGVO iVm Landespressegesetz / § 23 MStV bei rein journalistischer Verarbeitung.
- **DSA-Pflichten** für VLOP/VLOSE nicht reflektiert bei Plattform-Mandaten.
