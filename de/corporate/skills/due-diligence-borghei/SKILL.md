---
name: due-diligence-borghei
title: /m-a-transaktionsrecht:due-diligence
description: Steuerung der rechtlichen Due Diligence beim Unternehmenskauf – Aufbau der DD-Request List, Abgrenzung Red-Flag-Report und Full-Scope-Report, Datenraumorganisation und Vertraulichkeit, Disclosure Schedules und Disclosure gegen den Garantiekatalog, Übersetzung von Findings in Vertragsinstrumente (Freistellung, Kaufpreisabschlag, Closing-Bedingung, Walk-away), Datenschutz in der Due Diligence nach Art. 6 Abs. 1 lit. f DSGVO mit Schwärzung von Personaldaten sowie kartellrechtliche Grenzen des Informationsaustauschs und Gun-Jumping. Use when eine Due Diligence geplant, eine Request List erstellt, ein Datenraum aufgesetzt oder ein DD-Report in Vertragsklauseln überführt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/m-a-transaktionsrecht/skills/due-diligence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
---

# /m-a-transaktionsrecht:due-diligence

## Zweck

Die Due Diligence ist kein Selbstzweck: Ihr Wert entsteht erst dort, wo ein Finding in eine Vertragsklausel übersetzt wird. Dieser Skill organisiert die rechtliche Prüfung von der Request List über den Datenraum bis zum Report — und stellt sicher, dass Datenschutz und Kartellrecht die Prüfung nicht in einen eigenständigen Rechtsverstoß verwandeln.

## Eingaben

- Transaktionsstruktur: Share Deal oder Asset Deal, Zielgesellschaft, Branche, Größenordnung
- Rolle: Käuferseite (Buy-side) oder Verkäuferseite (Vendor DD / Vendor Legal Due Diligence)
- Prüfungstiefe und Budget: Red Flag oder Full Scope, Wesentlichkeitsschwelle in Euro
- Zeitplan: Datenraumöffnung, Q&A-Fenster, Reportabgabe, Signing-Ziel
- Prüfgebiete: Corporate, Verträge, Arbeitsrecht, IP/IT, Datenschutz, Immobilien, Öffentliches Recht, Litigation, Compliance, Steuern, Versicherungen
- Wettbewerbsverhältnis der Parteien (entscheidet über den Informationsaustausch-Rahmen)
- Vorhandenes NDA und dessen Reichweite (siehe `/vertragsrecht:vorvertragliche-phase`)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert die Rechtsgrundlagen für Datenraumzugriff und Informationsaustausch (DSGVO, GWB, GeschGehG) und branchenspezifische Prüfnormen.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Request List, Findings-Matrix und Reportstruktur und formuliert die abgeleiteten Vertragsklauseln.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft, ob jedes wesentliche Finding eine Vertragsentsprechung hat, ob geschwärzt wurde, wo erforderlich, und ob die Clean-Team-Regeln eingehalten sind.

## Ablauf

### 1. Scoping — Red Flag oder Full Scope

| Kriterium | Red-Flag-Report | Full-Scope-Report |
|---|---|---|
| **Zweck** | Deal-Breaker und Preisrelevantes identifizieren | Vollständige Bestandsaufnahme, Grundlage des Garantiekatalogs |
| **Darstellung** | Nur Abweichungen und Risiken, nach Ampel priorisiert | Beschreibung **und** Bewertung je Prüfgebiet |
| **Wesentlichkeitsschwelle** | hoch, ausdrücklich beziffert | niedriger, ebenfalls beziffert |
| **Typischer Einsatz** | Auktionsverfahren, frühe Phase, begrenztes Budget | Bilateraler Prozess, finanzierende Banken, W&I-Underwriting |

Die **Wesentlichkeitsschwelle** ist vor Prüfungsbeginn schriftlich zu vereinbaren und im Report zu nennen — sonst ist der Report weder haftungsrechtlich noch für das W&I-Underwriting brauchbar. Ebenso festzuhalten: Stichtag des Datenraums, Sprachen, geprüfte und ausdrücklich **nicht** geprüfte Bereiche (Scope Limitations).

### 2. DD-Request-List — Systematik

Die Liste wird nach Prüfgebieten gegliedert und pro Position mit Status geführt (angefordert / geliefert / unvollständig / verweigert):

```
A.  GESELLSCHAFTSRECHT
    A.1  Aktueller HR-Auszug, Gesellschaftsvertrag in geltender Fassung, alle Änderungen
    A.2  Gesellschafterlisten (vollständige Kette seit Gründung), Anteilsabtretungsurkunden
    A.3  Gesellschafterbeschlüsse der letzten 5 Jahre, Geschäftsordnungen, Beiratsunterlagen
    A.4  Gesellschaftervereinbarungen, Stimmbindungen, Options-, Treuhand- und Poolverträge
    A.5  Unternehmensverträge (Beherrschung, Gewinnabführung), Beteiligungen, Tochtergesellschaften
B.  FINANZEN UND FINANZIERUNG
    B.1  Jahresabschlüsse und Prüfberichte der letzten 3 Geschäftsjahre, aktuelle BWA
    B.2  Kredit- und Darlehensverträge, Sicherheiten, Covenants, Change-of-Control-Klauseln
    B.3  Gesellschafterdarlehen, Rangrücktritte, Bürgschaften und Patronatserklärungen
C.  WESENTLICHE VERTRÄGE
    C.1  Kunden- und Lieferantenverträge oberhalb der Schwelle, Rahmenverträge
    C.2  Miet-, Pacht- und Leasingverträge; Change-of-Control- und Kündigungsklauseln
    C.3  Kooperations-, Vertriebs-, Handelsvertreter- und Lizenzverträge
D.  ARBEITSRECHT   (Personaldaten pseudonymisiert, siehe Ziffer 5)
    D.1  Anonymisierte Mitarbeiterliste: Funktion, Eintritt, Befristung, Entgeltband, Kündigungsfrist
    D.2  Musterarbeitsverträge, Verträge der Leitungsebene, Vorstands-/GF-Anstellungsverträge
    D.3  Betriebsvereinbarungen, Tarifbindung, Betriebsratsstruktur
    D.4  Versorgungszusagen, Pensionsgutachten, Deckungsmittel
E.  IP, IT UND DATENSCHUTZ
    E.1  Schutzrechtsregister (Marken, Patente, Designs), Lizenzverträge in beide Richtungen
    E.2  IT-Systeme, Softwarelizenzen, Open-Source-Nutzung, Wartungsverträge
    E.3  Verzeichnis der Verarbeitungstätigkeiten, AVV, TOM, Datenschutzvorfälle
F.  ÖFFENTLICHES RECHT, COMPLIANCE, LITIGATION
    F.1  Genehmigungen, Auflagen, behördliche Anordnungen, Altlastenkataster
    F.2  Compliance-Management-System, Hinweisgebersystem, interne Untersuchungen
    F.3  Anhängige und angedrohte Rechtsstreitigkeiten, Streitwerte, Rückstellungen
G.  STEUERN UND VERSICHERUNGEN
    G.1  Steuerbescheide und Betriebsprüfungsberichte der offenen Veranlagungszeiträume
    G.2  Versicherungspolicen, Schadenshistorie, Deckungssummen
```

Jede Position erhält eine eindeutige Nummer, die im Report, in der Findings-Matrix und in den Disclosure Schedules **durchgehend gleich** bleibt. Ein Q&A-Log dokumentiert Nachfragen und Antworten mit Datum — es ist später der Beweis dafür, was offengelegt wurde.

### 3. Datenraum und Vertraulichkeit

Der virtuelle Datenraum wird nach der Struktur der Request List angelegt. Anforderungen: benannter Nutzerkreis nach Need-to-know, personalisierte Zugänge, Wasserzeichen, revisionssicheres Zugriffsprotokoll und eine **vollständige Sicherung des Datenrauminhalts auf einem Datenträger** zum Zeitpunkt des Signing — dieser Datenträger wird im SPA als Anlage referenziert und entscheidet später darüber, was als offengelegt gilt.

Rechtlicher Rahmen: Die Verschwiegenheitspflicht folgt bereits aus § 241 Abs. 2 BGB, wird aber durch das **NDA** konkretisiert. Zugleich ist das NDA eine „angemessene Geheimhaltungsmaßnahme" im Sinne des § 2 Nr. 1 GeschGehG und sichert damit den gesetzlichen Geheimnisschutz. Für Anwälte gilt zusätzlich § 43a Abs. 2 BRAO, § 203 StGB — Mandats- und Zielgesellschaftsdaten gehören nur in Werkzeuge mit Auftragsverarbeitungsvertrag.

### 4. Findings-zu-Vertrag-Übersetzung

Jedes Finding wird auf genau eine der fünf Rechtsfolgen abgebildet:

| Rechtsfolge | Wann | Vertragliche Umsetzung |
|---|---|---|
| **Garantie** | Risiko unbekannt oder unwahrscheinlich | Aufnahme in den Garantiekatalog, ggf. mit Wissensqualifikation |
| **Freistellung (Indemnity)** | Risiko **bekannt** und identifiziert, Eintritt und Höhe ungewiss | Spezialfreistellung, regelmäßig ohne De-minimis, Basket und Cap |
| **Kaufpreisabschlag** | Risiko bekannt, bezifferbar, Eintritt wahrscheinlich | Reduktion des Kaufpreises oder Erhöhung des Escrow |
| **Closing-Bedingung** | Risiko vor Vollzug behebbar (Konsent, Genehmigung, Ablösung) | Aufnahme in die Conditions Precedent mit Verantwortlichem und Frist |
| **Walk-away** | Deal-Breaker: Kerngeschäft, Bestand des Schutzrechts, existenzielle Haftung | Abbruch oder Umstrukturierung, ggf. Rücktrittsrecht bis Long-Stop-Date |

**Disclosure Schedules** sind die Kehrseite: Sie enthalten die Ausnahmen zum Garantiekatalog, jeweils unter Angabe der Garantieziffer und der Datenraumfundstelle. Ob eine Offenlegung den Anspruch entfallen lässt, richtet sich nach dem im SPA vereinbarten Maßstab — bloße Aufnahme in den Datenraum oder **Fair Disclosure** (für einen sachkundigen Käufer ohne Weiteres erkennbar). Siehe `/m-a-transaktionsrecht:garantien-freistellungen`.

Für Fristen der Conditions Precedent und der Rügefristen rechnet der deterministische Fristenrechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet nur die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** und sind vom Bearbeiter zu bestimmen.

### 5. Datenschutz in der Due Diligence ([Art. 6 Abs. 1 lit. f DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679))

Die Offenlegung von Beschäftigten-, Kunden- und Lieferantendaten im Datenraum ist eine **Verarbeitung** und braucht eine Rechtsgrundlage. In der Praxis trägt regelmäßig das **berechtigte Interesse** nach Art. 6 Abs. 1 lit. f DSGVO — allerdings nur nach dokumentierter Interessenabwägung und nur, soweit die Verarbeitung erforderlich ist. Eine Einwilligung der Beschäftigten ist wegen des Abhängigkeitsverhältnisses (§ 26 Abs. 2 BDSG) kein tragfähiges Fundament.

Praktische Umsetzung, gestuft:

1. **Stufe 1 — anonymisiert/aggregiert:** Mitarbeiterlisten ohne Namen, mit Funktion, Eintrittsdatum, Entgeltband und Kündigungsfrist. Für die Bewertung fast immer ausreichend.
2. **Stufe 2 — pseudonymisiert:** laufende Nummer statt Name, Zuordnungsschlüssel bleibt beim Verkäufer.
3. **Stufe 3 — Klardaten:** nur für einen eng begrenzten Kreis (Leitungsebene, Schlüsselpersonen mit Change-of-Control-Klausel), nur in einem separaten, zugriffsbeschränkten Datenraumbereich, erst kurz vor Signing.

Weiter erforderlich: **Schwärzung von Personaldaten** in Verträgen und Protokollen, Beschränkung besonderer Kategorien nach Art. 9 DSGVO (Gesundheitsdaten, Schwerbehinderung, Gewerkschaftszugehörigkeit) auf das absolut Notwendige, Löschkonzept für den Fall des Abbruchs, Information der Betroffenen nach Art. 13, 14 DSGVO und Aufnahme der Verarbeitung in das Verzeichnis nach Art. 30 DSGVO. Vgl. `/datenschutzrecht:avv-pruefung`.

### 6. Kartellrecht — Informationsaustausch und Gun-Jumping

Sind die Parteien aktuelle oder potenzielle Wettbewerber, ist der Austausch **wettbewerblich sensibler Informationen** (aktuelle und geplante Preise, Kalkulationen, Kunden- und Margendaten, Kapazitäten, Strategien) am Kartellverbot des § 1 GWB / Art. 101 AEUV zu messen — unabhängig davon, ob die Transaktion zustande kommt.

Schutzmechanismen:

- **Clean Team:** ein namentlich benannter, abgeschotteter Kreis (externe Berater und nicht operativ tätige Mitarbeiter), der sensible Daten sieht und dem Erwerber nur aggregierte Bewertungsergebnisse berichtet; abgesichert durch Clean Team Agreement mit Vertraulichkeits- und Verwendungsbeschränkung.
- **Aggregation und Historisierung:** Daten aggregiert, gebündelt und mit zeitlichem Abstand statt tagesaktuell und einzelvertragsbezogen.
- **Stufung:** sensibelste Unterlagen erst spät im Prozess und nur, soweit für die Bewertung erforderlich.

**Gun-Jumping** ist die vorzeitige Verwirklichung des Zusammenschlusses vor Freigabe — verboten nach dem Vollzugsverbot des § 41 Abs. 1 GWB (Art. 7 FKVO). Typische Verstöße: Weisungen an die Zielgesellschaft, Abstimmung von Preisen oder Kundenzuordnungen, Zustimmungsvorbehalte für das Tagesgeschäft, gemeinsamer Marktauftritt vor Closing. Zulässig bleiben **Ordinary-Course-Klauseln**, die außergewöhnliche Maßnahmen an eine Zustimmung binden, ohne dem Erwerber Einfluss auf das laufende Geschäft zu geben. Siehe `/kartellrecht:gwb-zusammenschluss-anmeldung` und `/kartellrecht:kartellverbot-pruefung`.

## Quellen

### Statute

- [Art. 6 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) (Abs. 1 lit. f berechtigtes Interesse), Art. 9, 13, 14, 30 DSGVO
- [§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) (Beschäftigtendatenverarbeitung, Einwilligung im Abhängigkeitsverhältnis)
- [§ 1 GWB](https://www.gesetze-im-internet.de/gwb/__1.html), [§ 41 GWB](https://www.gesetze-im-internet.de/gwb/__41.html) (Vollzugsverbot)
- [§ 2 GeschGehG](https://www.gesetze-im-internet.de/geschgehg/__2.html) (angemessene Geheimhaltungsmaßnahmen), [§ 241 BGB](https://www.gesetze-im-internet.de/bgb/__241.html)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html), [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html)

### Kommentare

- Beisel/Klumpp, Der Unternehmenskauf, 8. Aufl. 2022, Kap. 2 (Due Diligence) `[unverifiziert - Auflagenstand prüfen]`
- Buck-Heeb/Dieckmann, Selbstregulierung im Privatrecht, Kap. Compliance-DD `[unverifiziert - prüfen]`
- Schmidt, in: Immenga/Mestmäcker, Wettbewerbsrecht, 6. Aufl. 2019, § 41 GWB Rn. 1 ff. `[unverifiziert - Auflagenstand prüfen]`

### Rechtsprechung

- EuGH, Urt. v. 31.05.2018 – C-633/16 (Ernst & Young, Reichweite des Vollzugsbegriffs) `[unverifiziert - prüfen]`

> Aktenzeichen vor Verwendung in juris / Beck-Online / curia.europa.eu prüfen. Die tragenden Aussagen folgen aus Art. 6 DSGVO, §§ 1, 41 GWB und der Kommentarliteratur.

## Ausgabeformat

```
DUE-DILIGENCE-STEUERUNG — <Zielgesellschaft> — <Datum>

I.    Scope                         [Red Flag / Full Scope]
        Wesentlichkeitsschwelle:    EUR <…>
        Scope Limitations:          <nicht geprüfte Bereiche>
        Datenraum-Stichtag:         <TT.MM.JJJJ>
II.   Request-List-Status           A Corporate [x/y]  B Finanzen [x/y]  C Verträge [x/y]
                                    D Arbeitsrecht [x/y]  E IP/IT/DS [x/y]
                                    F ÖffR/Compliance [x/y]  G Steuern [x/y]
        Verweigerte Positionen:     <Liste — Konsequenz im Vertrag>
III.  Findings-Matrix
        Nr. | Gebiet | Sachverhalt | Ampel | Rechtsfolge          | Vertragsziffer
        F-1 | …      | …           | 🔴    | Freistellung         | Ziff. …
        F-2 | …      | …           | 🟡    | Closing-Bedingung    | Ziff. …
        F-3 | …      | …           | 🟡    | Kaufpreisabschlag    | Ziff. …
IV.   Disclosure Schedules          [erstellt ✅/❌ — Maßstab: Datenraum / Fair Disclosure]
V.    Datenschutz                   Rechtsgrundlage: [Art. 6 Abs. 1 lit. f DSGVO — Abwägung dokumentiert ✅/❌]
        Stufung:                    [Stufe 1 / 2 / 3 — Klardaten ab <Datum>]
        Schwärzung von Personaldaten: [✅ / 🔴 offen]
        Art. 9 DSGVO-Daten:         [ausgeschlossen / begrenzt: <…>]
        Löschkonzept bei Abbruch:   [✅ / ❌]
VI.   Kartellrecht                  Wettbewerbsverhältnis: [ja / nein]
        Clean Team:                 [eingerichtet ✅/❌ — Mitglieder: <…>]
        Gun-Jumping-Risiko:         [🟢 / 🟡 / 🔴 — <Sachverhalt>]
VII.  Deal-Breaker                  <Liste oder "keine">

Gesamtbefund: [🟢 / 🟡 / 🔴]
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Findings ohne Vertragsentsprechung** — ein Risiko, das im Report steht, aber weder Garantie noch Freistellung noch Abschlag ausgelöst hat, trägt nach Closing der Käufer.
- **Personaldaten unverändert in den Datenraum geladen** — Verstoß gegen Art. 6 Abs. 1 lit. f DSGVO und Art. 5 Abs. 1 lit. c DSGVO; Anonymisierung und Schwärzung sind vor dem Upload zu leisten, nicht danach.
- **Einwilligung der Beschäftigten als Rechtsgrundlage gewählt** — im Abhängigkeitsverhältnis nach § 26 Abs. 2 BDSG regelmäßig nicht freiwillig und damit unbrauchbar.
- **Sensible Wettbewerbsdaten ohne Clean Team ausgetauscht** — eigenständiger Verstoß gegen § 1 GWB, unabhängig vom Zustandekommen der Transaktion.
- **Gun-Jumping durch Einflussnahme vor Freigabe** — Zustimmungsvorbehalte für das Tagesgeschäft, Weisungen oder gemeinsame Kundenansprache verletzen das Vollzugsverbot des § 41 GWB.
- **Wesentlichkeitsschwelle nicht dokumentiert** — der Report ist für Haftung und W&I-Underwriting nicht verwertbar.
- **Datenraum nicht zum Signing gesichert** — im Streit über die Offenlegung fehlt der Beweis, welche Dokumente wann verfügbar waren.
- **Q&A-Antworten nur mündlich** — was nicht im Log steht, gilt später als nicht offengelegt oder wird gerade umgekehrt behauptet.
