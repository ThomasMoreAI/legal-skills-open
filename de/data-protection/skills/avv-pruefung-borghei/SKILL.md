---
name: avv-pruefung-borghei
title: /datenschutzrecht:avv-pruefung
description: Prüfung eines Auftragsverarbeitungsvertrags (AVV) nach Art. 28 DSGVO – Pflichtklauseln Art. 28 Abs. 3 lit. a–h, Unterauftragsverarbeiter Art. 28 Abs. 2 und Abs. 4, technische und organisatorische Maßnahmen Art. 32 DSGVO, § 203 StGB bei Berufsgeheimnisträgern, Bußgeldrisiko Art. 83 Abs. 4 DSGVO. Use when ein Verantwortlicher oder Auftragsverarbeiter einen AVV auf Wirksamkeit und Vollständigkeit prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenschutzrecht/skills/avv-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
---

# /datenschutzrecht:avv-pruefung

## Zweck

Wer personenbezogene Daten durch einen Dienstleister verarbeiten lässt (Cloud, Lohnabrechnung, IT-Wartung, Marketing), benötigt einen Auftragsverarbeitungsvertrag (AVV) nach [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679). Das Besondere: Eine **fehlende oder mangelhafte AVV ist selbst ein eigenständiger, bußgeldbewehrter Verstoß** – unabhängig davon, ob es jemals zu einer Datenpanne kommt. Fehlt eine der Pflichtklauseln des Art. 28 Abs. 3 lit. a–h, ist der Vertrag unvollständig und die Auftragsverarbeitung formell rechtswidrig. Dieser Skill prüft Rollen, Pflichtklauseln, Unterauftragsverarbeiter, technische und organisatorische Maßnahmen sowie – bei Berufsgeheimnisträgern – den zusätzlichen Schutz nach § 203 StGB und erstellt eine konkrete Mängelliste.

## Eingaben

- Vertragstext (AVV-Entwurf oder unterzeichnete Fassung)
- Rollen: Wer ist Verantwortlicher, wer Auftragsverarbeiter? (ggf. mehrstufig)
- Berufsgeheimnisträger ja/nein (Rechtsanwalt, Steuerberater, Arzt, Notar)
- Eingesetzte Unterauftragsverarbeiter (bekannt / geplant / Liste vorhanden?)
- Drittlandbezug (Serverstandort, Konzernmutter, Support aus Drittland)
- Anlagen: TOM-Beschreibung (Art. 32), Subunternehmerliste, Genehmigungsregime

## Sub-Agent-Architektur

Die Prüfung läuft in drei Rollen, die nacheinander arbeiten:

- **Researcher** – liest den Vertragstext und die Anlagen, ordnet jede Klausel den gesetzlichen Anforderungen des Art. 28 Abs. 3 lit. a–h zu und sammelt offene Stellen. Klärt den Drittlandbezug und die tatsächlich eingesetzten Subunternehmer.
- **Drafter** – formuliert zu jeder fehlenden oder schwachen Klausel einen konkreten Nachbesserungsvorschlag und entwirft die Mängelliste mit Priorität.
- **Reviewer** – kontrolliert auf Vollständigkeit (alle lit. a–h abgedeckt?), prüft die § 203-StGB-Einbindung bei Berufsgeheimnisträgern und bewertet das Haftungs- und Bußgeldrisiko. Keine erfundenen Klauselnummern, keine erfundene Rechtsprechung.

## Ablauf

### 1. Rollenklärung

Zuerst festlegen, wer **Verantwortlicher** und wer **Auftragsverarbeiter** ist. Eine echte Auftragsverarbeitung liegt nur vor, wenn der Dienstleister weisungsgebunden und ohne eigenen Entscheidungsspielraum über Zwecke und Mittel handelt. Entscheidet der Dienstleister selbst über Zwecke (z. B. eigene Auswertung), liegt keine Auftragsverarbeitung, sondern eigene Verantwortlichkeit oder gemeinsame Verantwortlichkeit (Art. 26 DSGVO) vor – dann ist eine AVV das falsche Instrument. Bei mehrstufigen Ketten jede Stufe einzeln einordnen.

### 2. Checkliste Pflichtklauseln (Art. 28 Abs. 3 lit. a–h DSGVO)

Der AVV muss ein bindender Vertrag sein und sämtliche Pflichtklauseln des **Art. 28 Abs. 3 DSGVO** enthalten. Jede der folgenden lit. a–h einzeln abhaken:

- **lit. a – Weisungsbindung:** Verarbeitung nur auf dokumentierte Weisung des Verantwortlichen, einschließlich Drittlandübermittlungen.
- **lit. b – Vertraulichkeit:** Verpflichtung der zur Verarbeitung befugten Personen auf Vertraulichkeit.
- **lit. c – Sicherheit:** Umsetzung aller Maßnahmen nach Art. 32 DSGVO (siehe Schritt 4).
- **lit. d – Unterauftragsverarbeiter:** Einhaltung der Bedingungen aus Art. 28 Abs. 2 und Abs. 4 (siehe Schritt 3).
- **lit. e – Betroffenenrechte:** Unterstützung des Verantwortlichen bei Anträgen Betroffener (Kapitel III DSGVO).
- **lit. f – Unterstützung Art. 32–36:** Hilfe bei Sicherheit, Meldung von Datenpannen und Datenschutz-Folgenabschätzung.
- **lit. g – Löschung/Rückgabe:** nach Wahl des Verantwortlichen Löschung oder Rückgabe aller Daten nach Ende der Verarbeitung.
- **lit. h – Nachweise/Audits:** Bereitstellung aller erforderlichen Informationen und Ermöglichung von Überprüfungen/Audits.

Jede fehlende oder nur scheinbar geregelte Position ist eine **fehlende Pflichtklausel** und wandert in die Mängelliste.

### 3. Unterauftragsverarbeiter-Regime + Drittland

- **Genehmigung (Art. 28 Abs. 2 DSGVO):** Kein Unterauftragsverarbeiter ohne vorherige gesonderte oder allgemeine schriftliche Genehmigung des Verantwortlichen. Bei allgemeiner Genehmigung muss der AVV ein Informations- und Widerspruchsrecht bei Wechsel/Hinzunahme vorsehen.
- **Weitergabe der Pflichten (Art. 28 Abs. 4 DSGVO):** Dem Unterauftragsverarbeiter sind dieselben Datenschutzpflichten aufzuerlegen wie dem Auftragsverarbeiter; der Auftragsverarbeiter haftet für dessen Pflichtverletzungen.
- **Drittland:** Liegt ein **Drittlandtransfer** vor (Serverstandort, Support, Subunternehmer außerhalb EU/EWR), ist eine Transfergrundlage nach Kapitel V DSGVO erforderlich (Angemessenheitsbeschluss oder Standardvertragsklauseln samt Transfer Impact Assessment). Fehlt sie, ist die Übermittlung unzulässig.

### 4. TOM-Abgleich (Art. 32 DSGVO)

Die im AVV (meist als Anlage) beschriebenen **technische und organisatorische Maßnahmen** mit den Anforderungen des Art. 32 DSGVO abgleichen: Pseudonymisierung/Verschlüsselung, Vertraulichkeit, Integrität, Verfügbarkeit und Belastbarkeit, Wiederherstellbarkeit, regelmäßige Überprüfung. Leerformeln („angemessene Maßnahmen") ohne konkrete Beschreibung genügen nicht und sind als Mangel zu vermerken.

### 5. § 203-StGB-Prüfung bei Berufsgeheimnisträgern

Bei Berufsgeheimnisträgern (Rechtsanwälte, Steuerberater, Ärzte, Notare) reicht die DSGVO-Konformität nicht aus. Das Offenbaren geschützter Geheimnisse gegenüber einem externen Dienstleister berührt **[§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html)**. Der Dienstleister und seine Mitarbeiter müssen als „mitwirkende Personen" nach § 203 Abs. 3, 4 StGB eingebunden und ausdrücklich auf die Geheimhaltung verpflichtet werden; der Umfang der offenbarten Geheimnisse ist auf das Erforderliche zu begrenzen. Fehlt diese Verpflichtung, droht neben dem Datenschutzverstoß eine **Strafbarkeit** des Berufsgeheimnisträgers.

### 6. Haftungs-/Bußgeldrisiko

Verstöße gegen Art. 28 DSGVO (fehlende oder mangelhafte AVV) sind nach **[Art. 83 Abs. 4 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679)** mit einem **Bußgeld** von bis zu 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes (je nachdem, welcher Betrag höher ist) bewehrt. Hinzu kommen mögliche Schadensersatzansprüche Betroffener (Art. 82 DSGVO) und – bei Berufsgeheimnisträgern – die Strafbarkeit nach § 203 StGB.

### 7. Mängelliste

Abschließend alle Befunde in einer priorisierten **Mängelliste** bündeln: je Eintrag die betroffene Norm, der konkrete Mangel und ein Nachbesserungsvorschlag. Trennung in „blockierend" (Vertrag nicht abschlussfähig) und „nachzubessern".

## Risiken

- **Falsche Rolleneinordnung** – AVV trotz gemeinsamer/eigener Verantwortlichkeit → falsches Instrument, weiterhin rechtswidrig.
- **Scheinklauseln** – lit. a–h nur dem Wortlaut nach abgeschrieben, ohne operativen Gehalt → formal vorhanden, materiell unwirksam.
- **Stiller Drittlandtransfer** – Support/Subunternehmer im Drittland ohne Transfergrundlage übersehen.
- **§ 203 StGB übersehen** – bei Berufsgeheimnisträgern Strafbarkeit trotz formal sauberer DSGVO-AVV.
- **Veraltete TOM-Anlage** – technische und organisatorische Maßnahmen entsprechen nicht dem tatsächlichen Stand.

## Ausgabeformat

```
AVV-PRÜFUNG — <Mandat/Vertrags-ID> — <Datum>

I.   Rollenklärung           Verantwortlicher: <…> | Auftragsverarbeiter: <…>
                             Echte Auftragsverarbeitung? [✅ / ⚠️ / ❌]
II.  Pflichtklauseln (Art. 28 Abs. 3 lit. a–h)
     a) Weisungsbindung      [✅ / ❌ fehlende Pflichtklausel]
     b) Vertraulichkeit      [✅ / ❌]
     c) Sicherheit (Art. 32) [✅ / ❌]
     d) Unterauftragsverarb. [✅ / ❌]
     e) Betroffenenrechte    [✅ / ❌]
     f) Unterstützung 32–36  [✅ / ❌]
     g) Löschung/Rückgabe    [✅ / ❌]
     h) Nachweise/Audits     [✅ / ❌]
III. Unterauftragsverarbeiter
     Genehmigung (Abs. 2)    [✅ / ❌]
     Pflichtenweitergabe (Abs. 4) [✅ / ❌]
     Drittland               [kein / ⚠️ Transfergrundlage: <…>]
IV.  TOM-Abgleich (Art. 32)  [✅ / ⚠️ Leerformel / ❌]
V.   § 203 StGB              [n/a / ✅ Verpflichtung mitwirkender Personen / ❌]
VI.  Bußgeld-/Haftungsrisiko Art. 83 Abs. 4 DSGVO: <Einordnung>

VII. Mängelliste
     [blockierend] <Norm> — <Mangel> — <Nachbesserung>
     [nachzubessern] <Norm> — <Mangel> — <Nachbesserung>

Empfehlung: <…>
```

## Quellen

### Statute

- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Auftragsverarbeiter)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Sicherheit der Verarbeitung)
- [Art. 83 Abs. 4 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Bußgelder)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) (Verletzung von Privatgeheimnissen)
