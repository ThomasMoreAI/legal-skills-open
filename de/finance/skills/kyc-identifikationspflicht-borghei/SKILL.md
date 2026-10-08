---
name: kyc-identifikationspflicht-borghei
title: /geldwaesche-aml-kyc:kyc-identifikationspflicht
description: Identifizierung des Vertragspartners (§§ 10, 11 GwG) und des wirtschaftlich Berechtigten (§§ 3 ff. GwG) mit Transparenzregister-Abgleich (§§ 18–26 GwG); Trigger-Schwellen, vereinfachte (§ 14) und verstärkte Sorgfaltspflichten (§ 15), Aufzeichnung § 8 GwG. Use when ein Verpflichteter eine Geschäftsbeziehung aufnimmt, eine Schwellen-Transaktion durchführt oder bei Verdacht KYC nachholt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/geldwaesche-aml-kyc/skills/kyc-identifikationspflicht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /geldwaesche-aml-kyc:kyc-identifikationspflicht

## Zweck

Der Skill strukturiert die KYC-Prüfung („Know your customer") nach §§ 10 ff. GwG: Identifizierung des Vertragspartners, Feststellung des wirtschaftlich Berechtigten, Transparenzregister-Abfrage, Klärung von Zweck und Art der Geschäftsbeziehung sowie kontinuierliche Überwachung. Er trennt zwischen allgemeiner, vereinfachter und verstärkter Sorgfalt und stellt die Aufzeichnungspflicht § 8 GwG (5 Jahre) sicher.

> **⚠️ Aktualität (Stand 2026-07):** **Das GwG ist weiterhin das operativ maßgebliche Recht.** KYC-Prüfungen werden heute nach §§ 10 ff. GwG durchgeführt — nicht nach der AMLR. Das EU-AML-Paket verändert jedoch bereits jetzt die Arbeitsplanung:
>
> - **AMLA** (Anti-Money Laundering Authority, VO (EU) 2024/1620) ist seit dem **01.07.2025 in Frankfurt am Main operativ tätig**.
> - **AMLD6** (RL (EU) 2024/1640): Die Umsetzungsfrist für **Art. 11–13 und 15** — die Vorschriften zu den **Registern wirtschaftlich Berechtigter** — ist am **10.07.2026 abgelaufen**. Die allgemeine Umsetzungsfrist der Richtlinie läuft bis **10.07.2027**.
> - **AMLR** (VO (EU) 2024/1624) gilt ab **10.07.2027** als unmittelbar anwendbares **Single Rulebook**. Sie ersetzt die materiellen Sorgfaltspflichten des GwG weitgehend; eine nationale Umsetzung ist nicht erforderlich und nicht abzuwarten.
> - Der Großteil der **AMLA-Level-2-/Level-3-Maßnahmen** war zum **10.07.2026** fällig; eine umfangreiche Pipeline von etwa **23 RTS/ITS und Leitlinien** ist noch offen. Zeitpläne und Inhalte sind laufend zu verfolgen.
> - **EU-weite Bargeldobergrenze von 10.000 EUR**; Mitgliedstaaten dürfen **niedrigere** Grenzen festlegen. Für Deutschland ist die konkrete Umsetzung am geltenden Recht zu prüfen. `[unverifiziert - prüfen]`
>
> **Laufende Aufgabe:** Die Angaben im **Transparenzregister** sind an der **25-%-Schwelle** auszurichten und mit den selbst erhobenen Daten abzugleichen; die bestehenden GwG-Verfahren sind auf das **AMLR-Single-Rulebook zum 10.07.2027 zu mappen** (siehe Schritt 9).

## Eingaben

- Verpflichteten-Typ nach § 2 GwG
- Geschäftsvorgang (Begründung Geschäftsbeziehung / Einzeltransaktion / Verdachtsfall)
- Vertragspartner (natürliche Person / juristische Person / Personengesellschaft / Trust / Stiftung)
- Beteiligungs- und Kontrollstruktur, soweit bekannt
- bei Bargeld / Kunst / Edelmetallen: Transaktionsvolumen (Schwellenwerte)
- Risikoklasse aus der Risikoanalyse (§ 5 GwG, siehe Skill `gwg-risikoanalyse`)
- besondere Indikatoren: PEP-Status, Hochrisikoland-Bezug, ungewöhnliches Konstrukt

## Sub-Agent-Architektur

Researcher liefert §§ 10–17 GwG, §§ 3 ff. GwG, Transparenzregister-Normen §§ 18–26 GwG, BaFin- und FIU-AuA sowie Kommentarstellen (Herzog, Bülte). Drafter erstellt das KYC-Memo mit Identifizierungs-Checkliste, WB-Analyse und Empfehlung zum Pflichtenniveau. Reviewer prüft Vollständigkeit der Identifizierungsdaten, korrekte Anwendung von § 14 / § 15, Transparenzregister-Abgleich, Aufzeichnungspflicht und Hinweis auf Folgepflichten (insb. § 43 GwG).

## Ablauf

### 1. Trigger der Identifizierungspflicht (§ 10 III GwG)

Die Pflicht greift bei:

- **Begründung einer Geschäftsbeziehung** (§ 10 III Nr. 1 GwG) — unabhängig vom Volumen
- **Einzeltransaktion außerhalb einer Geschäftsbeziehung**:
  - Bargeld ≥ 15.000 EUR (oder mehrere kleinere, die augenscheinlich verbunden sind) (§ 10 III Nr. 2 GwG)
  - Güterhändler: Bargeld ≥ 10.000 EUR (§ 4 V GwG); Edelmetallhändler: 2.000 EUR (§ 4 V GwG) `[unverifiziert – aktuellen Schwellenwert prüfen]`
  - Kunsthandel / Kunstvermittler: 10.000 EUR (auch unbar bei bestimmten Konstellationen) `[unverifiziert]`
- **Verdacht** auf Geldwäsche oder Terrorismusfinanzierung (§ 10 III Nr. 3 GwG) — unabhängig von jedem Schwellenwert und unabhängig vom Pflichtenniveau
- **Zweifel an Richtigkeit oder Vollständigkeit** zuvor erhobener Daten (§ 10 III Nr. 4 GwG)

### 2. Identifizierung des Vertragspartners (§ 11 GwG)

**Natürliche Person** (§ 11 IV Nr. 1 GwG): Name (Vor- und Nachname), Geburtsort, Geburtsdatum, Staatsangehörigkeit, Anschrift. Beleg: gültiges Ausweisdokument iSv § 12 I 1 Nr. 1 GwG (Personalausweis, Reisepass, Pass-Ersatz). Erfassung Dokumenten-Nr., ausstellende Behörde, Gültigkeit.

**Juristische Person / Personengesellschaft** (§ 11 IV Nr. 2 GwG): Firma, Name oder Bezeichnung, Rechtsform, Registernummer (sofern vorhanden), Anschrift Sitz / Hauptniederlassung, Mitglieder Vertretungsorgan / gesetzliche Vertreter. Beleg: Auszug aus Handels- / Genossenschafts- / Vereins- / Partnerschafts- / Stiftungsregister oder gleichwertiges amtliches Register.

**Identifizierungsverfahren** (§ 12 I GwG): Vorlage Original / qualifizierte elektronische Signatur / Videoidentifizierung (BaFin-Rundschreiben 3/2017 zur Videoident `[unverifiziert]`) / eID-Funktion / Notar-/Anwalts-Vermittlung (§ 12 I 2 GwG).

### 3. Wirtschaftlich Berechtigter (§ 3 GwG)

**Tatsächlicher WB** (§ 3 II GwG, juristische Person ohne börsenrechtliche Ausnahme):

- jede natürliche Person, die unmittelbar oder mittelbar
  - **mehr als 25 %** der Kapitalanteile hält, oder
  - **mehr als 25 %** der Stimmrechte kontrolliert, oder
  - auf vergleichbare Weise Kontrolle ausübt

**Fiktiver WB** (§ 3 II 5 GwG): Lässt sich nach Ausschöpfung aller Möglichkeiten **kein** tatsächlicher WB ermitteln, gilt der gesetzliche Vertreter, geschäftsführende Gesellschafter oder Partner als WB. Die Fiktion ist zu **begründen** und zu **dokumentieren** — sie ist kein Default.

Bei **Trusts / Treuhand / nicht rechtsfähigen Stiftungen** (§ 3 III GwG): Treugeber, Treuhänder, Protektor, Begünstigte, sowie sonstige natürliche Personen mit beherrschendem Einfluss.

### 4. Transparenzregister-Abgleich (§§ 18–26 GwG)

Seit Umstellung auf Vollregister (Transparenzregister- und Finanzinformationsgesetz, in Kraft seit 01.08.2021) `[unverifiziert – Datum prüfen]` müssen Verpflichtete bei juristischen Personen / Personengesellschaften / Trusts / Stiftungen das Transparenzregister abfragen und mit den selbst erhobenen WB-Daten **abgleichen** (§ 11 V GwG iVm § 23a GwG `[unverifiziert – §-Verweis prüfen]`).

**Unstimmigkeitsmeldung** (§ 23a GwG): Weichen die Registerangaben von den selbst erhobenen Daten ab, ist eine Unstimmigkeit an das registerführende BVA zu melden — dies ist **keine** Verdachtsmeldung nach § 43 GwG und unterliegt nicht dem Tippoff-Verbot des § 47 GwG (str.; herrschend in BaFin-AuA).

### 5. Pflichtenniveau (Risikoanalyse-abhängig)

| Pflichtenniveau | Trigger | Maßnahmen |
|---|---|---|
| **vereinfachte Sorgfalt** § 14 GwG | nachgewiesen niedriges Risiko (z. B. börsennotierte EWR-AG, inländische Behörden) | reduzierter Identifizierungsumfang, lockere Aktualisierung |
| **allgemeine Sorgfalt** § 10 GwG | Standardfall | Identifizierung, WB, Zweck, kontinuierliches Monitoring |
| **verstärkte Sorgfalt** § 15 GwG | PEP § 1 XII; Hochrisikodrittstaat-Bezug § 15 III Nr. 2; komplexe / unübliche Struktur § 15 III Nr. 3; Korrespondenzbankbeziehung außerhalb EWR | Geschäftsleitung-Zustimmung, Herkunft Vermögen / Mittel, verstärkte laufende Überwachung |

### 6. Klärung von Zweck und Art (§ 10 I Nr. 2 GwG)

Plausibilität des Geschäftszwecks dokumentieren. Bei Diskrepanz zwischen erklärtem Zweck und beobachtetem Transaktionsverhalten: Eskalation an GW-Beauftragten, ggf. § 43 GwG-Prüfung.

### 7. Aufzeichnung und Aufbewahrung (§ 8 GwG)

**5 Jahre** ab Ende der Geschäftsbeziehung oder ab Abwicklung der Einzeltransaktion. Aufzeichnungspflicht umfasst Identifizierungsdaten, Kopien der Belege, Risikoeinstufung, Monitoring-Erkenntnisse.

### 8. Folgepflicht: Verdachtsmeldung

KYC-Erkenntnisse können die Meldepflicht nach § 43 GwG auslösen (Skill `verdachtsmeldung-fiu`). Bei Verdacht: **Identifizierung trotzdem durchführen** (§ 10 IX GwG schließt Abbruch nur eng aus), aber **kein Tippoff** und **Stillhaltepflicht** beachten.

### 9. Übergang auf das EU-AML-Paket (AMLR / AMLD6 / AMLA)

Die KYC-Prüfung selbst folgt heute dem GwG. Parallel ist die Umstellung vorzubereiten:

**a) UBO-Daten an der 25-%-Schwelle ausrichten.** Die Umsetzungsfrist für die Register-Vorschriften der **AMLD6 (Art. 11–13, 15)** ist am **10.07.2026 abgelaufen**. Transparenzregister-Eintragungen und intern gehaltene WB-Daten sind daran zu messen, dass **jede** natürliche Person mit **mehr als 25 %** Kapitalanteil, Stimmrechten oder vergleichbarer Kontrolle vollständig, aktuell und mit dokumentierter Kontrollkette erfasst ist. Historisch gewachsene Bestände mit lückenhafter mittelbarer Beteiligungskette sind der typische Befund.

**b) Gap-Mapping GwG → AMLR bis 10.07.2027.** Die **AMLR (VO (EU) 2024/1624)** gilt ab dem **10.07.2027** unmittelbar. Bestehende KYC-Verfahrensanweisungen sind Pflicht für Pflicht auf die AMLR-Kapitel abzubilden und in drei Kategorien zu sortieren:

| Kategorie | Bedeutung | Handlung |
|---|---|---|
| deckungsgleich | GwG-Pflicht entspricht der AMLR-Pflicht | Normverweis austauschen |
| verschärft | AMLR verlangt mehr als das GwG | Prozess und IT anpassen, Vorlauf einplanen |
| entfallen / abweichend | nationale Besonderheit ohne AMLR-Entsprechung | Streichung prüfen — Vollharmonisierung lässt nationale Zusatzpflichten nur begrenzt zu |

**c) AMLA-Level-2-Pipeline verfolgen.** Ein erheblicher Teil der zum **10.07.2026** fälligen technischen Regulierungs- und Durchführungsstandards sowie Leitlinien (Größenordnung **ca. 23 RTS/ITS/Guidelines**) steht noch aus. Sie konkretisieren gerade die Sorgfaltspflichten. Bis zu ihrer Veröffentlichung sind Detailfestlegungen als **vorläufig** zu kennzeichnen; ein Verantwortlicher für das Monitoring ist zu benennen.

**d) Auswahl zur direkten AMLA-Aufsicht vorbereiten.** Die AMLA wird eine begrenzte Zahl grenzüberschreitend besonders risikoreicher Verpflichteter **unmittelbar** beaufsichtigen. Betroffene Institute sollten prüfen, ob sie in Betracht kommen, und Dokumentation, Datenqualität und Ansprechstellen auf ein aufsichtsfähiges Niveau bringen. Die konkreten Auswahlkriterien und der Zeitplan sind an der AMLA-Verordnung und den AMLA-Veröffentlichungen zu verifizieren. `[unverifiziert - prüfen]`

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 XII GwG](https://www.gesetze-im-internet.de/gwg_2017/__1.html) (PEP-Definition)
- [§ 3 GwG](https://www.gesetze-im-internet.de/gwg_2017/__3.html) (wirtschaftlich Berechtigter)
- [§ 8 GwG](https://www.gesetze-im-internet.de/gwg_2017/__8.html) (Aufzeichnungs- / Aufbewahrungspflicht)
- [§ 10 GwG](https://www.gesetze-im-internet.de/gwg_2017/__10.html) (allgemeine Sorgfaltspflichten, Trigger)
- [§ 11 GwG](https://www.gesetze-im-internet.de/gwg_2017/__11.html) (Identifizierungspflicht)
- [§ 12 GwG](https://www.gesetze-im-internet.de/gwg_2017/__12.html) (Identifizierungsverfahren)
- [§ 14 GwG](https://www.gesetze-im-internet.de/gwg_2017/__14.html) (vereinfachte Sorgfalt)
- [§ 15 GwG](https://www.gesetze-im-internet.de/gwg_2017/__15.html) (verstärkte Sorgfalt; PEP, Hochrisikodrittstaat)
- [§§ 18–26 GwG](https://www.gesetze-im-internet.de/gwg_2017/__18.html) (Transparenzregister)
- [§ 56 GwG](https://www.gesetze-im-internet.de/gwg_2017/__56.html) (Bußgelder)
- [Art. 13, 14, 18, 20 RL (EU) 2015/849](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L0849)
- [VO (EU) 2024/1624 (AMLR — Single Rulebook)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1624) — unmittelbar anwendbar ab **10.07.2027**; Kapitel zu Sorgfaltspflichten (CDD), wirtschaftlich Berechtigten und der Bargeldobergrenze von 10.000 EUR
- [RL (EU) 2024/1640 (AMLD6)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1640) — Art. 11–13, 15 (Register wirtschaftlich Berechtigter) Umsetzungsfrist **10.07.2026**; allgemeine Umsetzungsfrist **10.07.2027**
- [VO (EU) 2024/1620 (AMLA-Verordnung)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1620) — AMLA seit **01.07.2025** in Frankfurt am Main operativ; direkte Aufsicht über ausgewählte Verpflichtete

### Verwaltungsvorschriften

- BaFin, AuA zum GwG, Allgemeiner Teil + Besonderer Teil
- BaFin-Rundschreiben zur Videoidentifizierung `[unverifiziert – aktuelles Rundschreiben prüfen]`
- FIU-AuA für Nichtfinanzsektor

### Kommentare

- Herzog, GwG, X. Aufl. Jahr, §§ 10, 11, 3 (mit Kommentierung WB) `[unverifiziert – Auflage prüfen]`
- Bülte, GwG, §§ 10 ff. `[unverifiziert]`
- Kreitmair, GwG, §§ 3, 11 `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

- KG / OLG-Rspr. zu Bußgeldverfahren wegen fehlerhafter KYC `[unverifiziert]`
- BGH zur zivilrechtlichen Haftung von Kreditinstituten bei KYC-Versagen (Bereich Lastschriftrückgabe / Kontoeröffnung) `[unverifiziert]`

## Ausgabeformat

```
KYC-MEMO — §§ 10, 11, 3 GwG
Verpflichteter: <Firma>, § 2 I Nr. <…> GwG
Vorgang: <Geschäftsbeziehung / Einzeltransaktion / Anlass>
Stand: <Datum>

I.   Trigger der Identifizierungspflicht
     - <§ 10 III Nr. 1/2/3/4 GwG, Begründung>

II.  Vertragspartner-Identifizierung § 11 GwG
     - Personendaten / Firma / Register
     - Belegart und -nummer
     - Identifizierungsverfahren § 12 GwG

III. Wirtschaftlich Berechtigter §§ 3 ff. GwG
     - Beteiligungs- / Kontrollkette
     - tatsächlicher WB oder fiktiver WB (Begründung)
     - Transparenzregister-Abgleich (Treffer / Unstimmigkeit?)

IV.  Pflichtenniveau
     - § 14 / § 10 / § 15 GwG (Begründung)
     - PEP-Status, Hochrisikodrittstaat, komplexe Struktur

V.   Zweck und Art der Geschäftsbeziehung
     - Plausibilität, beobachtetes Transaktionsverhalten

VI.  Aufzeichnung § 8 GwG
     - Aufbewahrung 5 Jahre, Speicherort, Verantwortlicher

VII. Folgepflichten
     - Monitoring-Trigger
     - Hinweis auf § 43 GwG (Verdachtsmeldung) — falls einschlägig

VII-a. Übergang EU-AML-Paket
     - UBO-Daten an 25-%-Schwelle ausgerichtet (AMLD6 Art. 11–13, 15; Frist 10.07.2026): <…>
     - Gap-Mapping GwG → AMLR (Anwendung 10.07.2027): <deckungsgleich / verschärft / entfällt>
     - AMLA-Level-2-Pipeline (offene RTS/ITS/Leitlinien): <Verantwortlicher, Stand>
     - Kandidat für direkte AMLA-Aufsicht? <ja / nein / offen>

VIII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴

IX.  Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Wirtschaftlich Berechtigter**
>
> Der Vertragspartner ist die A-GmbH (HRB 12345 AG München). Anteilseigner ist nach Gesellschafterliste die B-Holding S.à r.l. (Luxemburg) mit 100 %; deren Anteile werden zu 60 % von einer zypriotischen C-Holding Ltd. und zu 40 % von einer natürlichen Person Y gehalten. C-Holding wird ihrerseits durch einen Jersey-Trust gehalten, dessen Begünstigte nach Trust Deed eine natürliche Person X ist. Damit hält X mittelbar 60 % × 100 % = 60 % der A-GmbH und ist wirtschaftlich Berechtigter iSv § 3 II 1 Nr. 1 GwG; ebenso Y mit 40 %. Beide sind nach §§ 11 V, 23a GwG ins Transparenzregister einzutragen bzw. dort abzugleichen. Die Konstruktion über Jersey-Trust ist ein Risikofaktor iSv § 15 III Nr. 3 GwG (komplexe Struktur), sodass verstärkte Sorgfalt anzuwenden ist (vgl. Herzog, GwG, § 15 Rn. 20 ff. `[unverifiziert]`).

## Risiken / typische Fehler

- **Identifizierung über Kopie ohne Originalvorlage / Videoident / eID** außerhalb der gesetzlich zugelassenen Verfahren — unwirksam, Bußgeld § 56 GwG.
- **Fiktiver WB als Default** ohne dokumentierten Ermittlungsversuch — § 3 II 5 GwG verlangt **vorrangige** Ermittlung des tatsächlichen WB.
- **Transparenzregister-Abgleich unterlassen** oder Unstimmigkeit nicht gemeldet — Verletzung § 23a GwG `[unverifiziert – konkrete Norm prüfen]`.
- **PEP-Status unbeachtet** — § 1 XII GwG erfasst auch Familienangehörige und nahestehende Personen; verstärkte Sorgfalt nach § 15 III Nr. 1 GwG obligatorisch.
- **Hochrisikodrittstaaten-Liste nicht abgefragt** (delegierte VO der KOM) — Risiko § 15 III Nr. 2 GwG übersehen.
- **Aufzeichnung < 5 Jahre / Speicherort nicht zugriffsbereit für Aufsicht** — Verstoß § 8 GwG.
- **Verdachtsindikator übersehen** und KYC-Prüfung als Routine behandelt — Folge: unterlassene § 43-Meldung, ggf. § 261 StGB.
- **AMLR vorzeitig als geltendes Recht angewandt** — die AMLR gilt erst ab **10.07.2027**. Wer heute eine KYC-Prüfung auf die AMLR statt auf §§ 10 ff. GwG stützt, prüft am geltenden Recht vorbei; das GwG bleibt bis dahin operativ maßgeblich.
- **Auf eine nationale Umsetzung der AMLR gewartet** — die AMLR ist eine **Verordnung** und gilt unmittelbar. Nur die AMLD6 wird umgesetzt. Wer den Umstellungsbedarf an ein deutsches Umsetzungsgesetz koppelt, verliert den Vorlauf bis 10.07.2027.
- **UBO-Frist 10.07.2026 verstrichen ohne Datenbereinigung** — die Register-Vorschriften der AMLD6 (Art. 11–13, 15) waren zu diesem Datum umzusetzen. Lückenhafte mittelbare Beteiligungsketten oberhalb der **25-%-Schwelle** sind der typische Prüfungsbefund der Aufsicht.
- **AMLA-Level-2-Standards als bereits final behandelt** — ein großer Teil der zum 10.07.2026 fälligen RTS/ITS und Leitlinien (ca. 23) ist **noch offen**. Detailfestlegungen, die darauf gestützt werden, sind als vorläufig zu kennzeichnen.
- **Bargeldobergrenze falsch angesetzt** — die EU-weite Grenze liegt bei **10.000 EUR**, Mitgliedstaaten dürfen jedoch **niedrigere** Grenzen vorsehen. Nie allein auf den EU-Wert abstellen, ohne das nationale Recht zu prüfen; die GwG-Schwellen (§ 10 III Nr. 2, § 4 V GwG) bleiben bis zum Anwendungsbeginn der AMLR maßgeblich.
- **Direkte AMLA-Aufsicht nicht in Betracht gezogen** — grenzüberschreitend tätige Institute mit erhöhtem Risikoprofil können unmittelbar der AMLA unterstellt werden; Datenqualität und Dokumentation sind darauf auszurichten.
