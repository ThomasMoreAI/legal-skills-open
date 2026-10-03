# Evidence Handling Protocol (Beweisprotokoll)

> This protocol is referenced by all advisory skills when the user provides evidence (documents, photos, emails, contracts, witness statements, expert reports). Follow it systematically whenever evidence is part of the analysis.

---

## 1. Evidence Classification by ZPO Hierarchy

Austrian civil procedure law (ZPO) establishes a hierarchy of evidence types. Classify each piece of evidence the user provides into the appropriate tier:

### Stufe 1: Urkunden (§§292ff ZPO) — Documentary Evidence

The strongest form of evidence. Sub-classify:

| Urkundentyp | Beweiskraft | §§ ZPO | Beispiele |
|-------------|-------------|--------|-----------|
| **Oeffentliche Urkunden** (§292 ZPO) | Voller Beweis fuer die beurkundeten Tatsachen (widerlegbar nur durch Beweis der Unrichtigkeit) | §292 Abs 1 ZPO | Grundbuchauszug, Firmenbuchauszug, Notariatsakt, gerichtliches Protokoll, Staatsbuergerschaftsnachweis, beglaubigte Urkunden |
| **Auslaendische oeffentliche Urkunden** | Voller Beweis, wenn mit Apostille oder Beglaubigung | §292 Abs 2 ZPO iVm Haager Apostille-Uebereinkommen | Auslaendische Geburts-/Heiratsurkunden mit Apostille |
| **Private Urkunden** (§294 ZPO) | Beweis nur fuer die Tatsache der Erklaerung, NICHT fuer deren inhaltliche Richtigkeit | §294 ZPO | Privatschriftlicher Vertrag, Quittung, E-Mail, Brief, SMS, WhatsApp-Nachrichten, Fotos, Screenshots |
| **Dispositive Urkunden** | Hohe Beweiskraft, weil sie das Rechtsgeschaeft selbst enthalten | — | Mietvertrag, Arbeitsvertrag, Kaufvertrag, Testament, Scheidungsvergleich |

**Echtheitspruefung (§310 ZPO):**
- Wenn die Echtheit einer Privaturkunde bestritten wird, muss derjenige, der sich auf die Urkunde beruft, deren Echtheit beweisen
- Bei oeffentlichen Urkunden gilt die Vermutung der Echtheit (§292 Abs 1 ZPO) — der Gegner muss die Unechtheit beweisen
- Elektronische Signaturen: Qualifizierte elektronische Signatur (SigG) = oeffentliche Urkunde gleichgestellt; einfache E-Mail = Privaturkunde

### Stufe 2: Zeugen (§§320ff ZPO) — Witness Evidence

| Aspekt | Regelung | §§ ZPO |
|--------|----------|--------|
| Zeugenpflicht | Jeder ist zur Zeugenaussage verpflichtet | §321 ZPO |
| Verweigerungsrecht | Nahe Angehoerige (§321 Abs 1 Z 1 ZPO), Berufsgeheimnisse (Anwaelte, Aerzte — §321 Abs 1 Z 3-4 ZPO), Selbstbelastung (§321 Abs 1 Z 2 ZPO) | §321 ZPO |
| Glaubwuerdigkeit | Richterliche freie Beweiswuerdigung (§272 ZPO) | §272 ZPO |
| Unbeteiligtheit | Zeugen, die am Ausgang des Verfahrens kein Interesse haben, gelten als glaubwuerdiger | — |

**Bewertung von Zeugenaussagen:**
- Unmittelbare Wahrnehmung (Augenzeuge) > Vom-Hoerensagen-Zeuge
- Zeitnaehe der Beobachtung zum Ereignis erhoht Beweiskraft
- Anzahl uebereinstimmender, unabhaengiger Zeugen erhoht Beweiskraft
- Naehe des Zeugen zu einer Partei (Familie, Freunde, Mitarbeiter) mindert Beweiskraft
- Schriftliche Zeugenerklaerung (Privatgutachten) hat weniger Gewicht als Aussage vor Gericht

### Stufe 3: Sachverstaendige (§§351ff ZPO) — Expert Evidence

| Aspekt | Regelung | §§ ZPO |
|--------|----------|--------|
| Gerichtlich bestellter Sachverstaendiger | Vom Gericht bestellt, unabhaengig, hoechste Beweiskraft | §351 ZPO |
| Privatgutachten | Vom Partei beauftragt, gilt als qualifiziertes Parteivorbringen, NICHT als Beweis im strengen Sinn | — |
| Gegengutachten | Partei kann Gegengutachten vorlegen und Erlaeuterung/Ergaenzung beantragen | §362 ZPO |

**Bewertung:**
- Gerichtlicher SV > Privatgutachten
- Privatgutachten ist dennoch wertvoll: es kann den Richter veranlassen, einen gerichtlichen SV zu bestellen
- Kosten: Gerichtlicher SV wird von der Partei bevorschusst, die den Beweis anbietet (§365 ZPO)

### Stufe 4: Augenschein (§§368ff ZPO) — Physical Inspection / Visual Evidence

| Beweismittel | Beweiskraft | Hinweise |
|-------------|-------------|----------|
| Gerichtlicher Augenschein | Hoch — Richter nimmt selbst wahr | §368 ZPO; Ortstermin, Besichtigung |
| Fotos | Mittel — Privaturkunde, Echtheit kann bestritten werden | Metadaten (EXIF) koennen Zeitpunkt und Ort belegen |
| Videos | Mittel bis hoch — je nach Qualitaet und Nachvollziehbarkeit | Ueberwachungskamera-Aufnahmen haben hoehere Beweiskraft |
| Screenshots | Niedrig — leicht manipulierbar | Zusaetzliche Sicherung empfehlenswert (Notar, Timestamps) |

### Stufe 5: Parteienvernehmung (§§371ff ZPO) — Party Testimony

- Schwaechtestes Beweismittel, weil die Partei ein eigenes Interesse am Ausgang hat
- Nur zulaessig als **subsidiaeres Beweismittel** — wenn andere Beweismittel nicht zur Verfuegung stehen oder nicht ausreichen (§371 ZPO)
- Kann entweder von der Partei selbst beantragt oder vom Gericht von Amts wegen angeordnet werden
- Eidesstaettliche Erklaerung (§377 ZPO): Unter Wahrheitspflicht, aber dennoch Parteibeweis

---

## 2. Evidence Assessment Steps

When the user provides evidence, follow these steps in order:

### 2A: Klassifizieren

Fuer jedes Beweisstuck:
1. In welche ZPO-Stufe faellt es? (Urkunde/Zeuge/SV/Augenschein/Partei)
2. Innerhalb der Stufe: Welcher Untertyp? (oeffentlich/privat, gerichtlich bestellt/privat)
3. Tabellarisch darstellen:

| Nr. | Beweisstuck | ZPO-Stufe | Untertyp | Beweiskraft |
|-----|-------------|-----------|----------|-------------|
| 1 | [z.B. Mietvertrag] | Stufe 1: Urkunde | Privaturkunde, dispositiv | Hoch |
| 2 | [z.B. E-Mail vom Vermieter] | Stufe 1: Urkunde | Privaturkunde | Mittel |
| 3 | [z.B. Aussage der Nachbarin] | Stufe 2: Zeuge | Unbeteiligter Dritter | Mittel |

### 2B: Beweiskraft bewerten

Fuer jedes Beweisstuck die Beweiskraft einschaetzen:
- **Hoch:** Oeffentliche Urkunden, gerichtliche SV-Gutachten, unbestrittene Vertraege
- **Mittel:** Private Urkunden mit klarem Inhalt, unbeteiligte Zeugen, Privatgutachten, Fotos mit Metadaten
- **Niedrig:** Screenshots ohne Verifizierung, Zeugen mit Naheverhaeltnis zu einer Partei, Parteivorbringen ohne Untermauerung
- **Fragwuerdig:** Nicht unterschriebene Dokumente, kopierte Urkunden ohne Original, anonyme Mitteilungen

### 2C: Echtheit pruefen (§310 ZPO)

Fuer jede Urkunde:
- Ist sie im Original vorhanden oder nur als Kopie?
- Traegt sie die erforderlichen Unterschriften?
- Gibt es Anzeichen fuer Manipulation (nachtrgliche Aenderungen, Streichungen, unterschiedliche Schriften)?
- Bei elektronischen Dokumenten: Sind Metadaten konsistent? Qualifizierte elektronische Signatur vorhanden?
- **Flaggen:** Wenn Echtheitsbedenken bestehen, explizit darauf hinweisen

### 2D: Vollstaendigkeit pruefen

- Welche Beweismittel hat der User vorgelegt?
- Welche Beweismittel fehlen, die fuer den Fall wesentlich waeren?
- Gibt es Luecken in der Beweiskette (z.B. Vertrag vorhanden, aber keine Zustellnachweise fuer Kuendigung)?
- **Beweisluecken explizit benennen** — das ist oft der wertvollste Teil der Analyse

### 2E: Pro und Contra

Fuer jeden relevanten Anspruch oder Einwand:
- Welche Beweise **stuetzen** die Position des Users?
- Welche Beweise **untergraben** die Position des Users?
- Gibt es Beweise, die fuer **beide Seiten** auslegbar sind?

### 2F: Beweisnotstand identifizieren

**Beweisnotstand** liegt vor, wenn eine Partei eine entscheidende Tatsache beweisen muss, aber kein geeignetes Beweismittel zur Verfuegung hat.

Pruefen:
- Gibt es Tatsachen, die der User beweisen muss, fuer die aber kein Beweis vorliegt?
- Kann der Beweisnotstand durch alternative Beweismittel aufgeloest werden?
- Greift eine Beweislasterleichterung (Anscheinsbeweis, Beweislastumkehr)?

---

## 3. Multi-Document Analysis

Wenn der User mehrere Dokumente vorlegt (z.B. Vertrag + Nachtraege + E-Mail-Korrespondenz), muessen diese als Gesamtheit analysiert werden:

### 3A: Chronologische Ordnung

1. Alle Dokumente chronologisch ordnen
2. Zeitleiste erstellen: Wann wurde welches Dokument erstellt/unterzeichnet/versendet?
3. Pruefen: Stimmt die chronologische Reihenfolge mit dem vorgetragenen Sachverhalt ueberein?

### 3B: Widersprueche identifizieren

- Widersprechen sich Dokumente inhaltlich?
- Aendert ein spaeteres Dokument ein frueheres ab? Ausdruecklich oder konkludent?
- Gibt es Aussagen in E-Mails, die dem schriftlichen Vertrag widersprechen?
- **Achtung:** Bei Widerspruch zwischen muendlicher/E-Mail-Vereinbarung und schriftlichem Vertrag gilt grundsaetzlich der schriftliche Vertrag — AUSSER es liegt eine konkludente Vertragsaenderung vor (§863 ABGB)

### 3C: Konkludente Vertragsaenderung (§863 ABGB)

Pruefen, ob durch das Verhalten der Parteien der Vertrag stillschweigend abgeaendert wurde:
- Langjaehrige abweichende Praxis von den Vertragsbedingungen
- Duldung von Vertragsverletzungen ueber laengeren Zeitraum
- Reaktionsloses Hinnehmen von Aenderungsvorschlaegen
- **Beweislast:** Wer sich auf die konkludente Aenderung beruft, muss sie beweisen

### 3D: Gesamtbild

- Was ergibt sich aus der Zusammenschau aller Dokumente?
- Gibt es ein konsistentes Bild oder Ungereimtheiten?
- Welche Schlussfolgerungen lassen sich aus der Dokumentenlage ziehen?

---

## 4. Evidence Gathering Recommendations

Wenn Beweisluecken identifiziert werden, empfehlen:

### 4A: Selbst beschaffbare Beweise

| Beweismittel | Wie beschaffen | Hinweis |
|-------------|----------------|---------|
| Kontoauszuege | Bank anfordern | Belegen Zahlungen/Ueberweisungen |
| E-Mail-Verlauf | Eigenes Postfach durchsuchen | Chronologisch sichern, als PDF exportieren |
| Fotos/Videos | Eigene Aufnahmen | Metadaten (Datum, Ort) nicht loeschen |
| Schriftverkehr | Eigene Ablage | Einschreibebelege, Zustellnachweise |
| Zeugen identifizieren | Nachdenken, wer was mitbekommen hat | Name, Adresse, was der Zeuge bezeugen kann |
| Grundbuchauszug | Bezirksgericht oder online (GISA) | Oeffentliche Urkunde, jederzeit erhaeltlich |
| Firmenbuchauszug | Firmenbuchgericht oder online | Oeffentliche Urkunde |
| Sozialversicherungsauszug | SVA/OEGK anfordern | Dienstzeiten, Beitragsgrundlagen |
| Arbeitszeitaufzeichnungen | Eigene Aufzeichnungen/App | Je zeitnaeher, desto beweiskraeftiger |

### 4B: Gerichtlich zu beschaffende Beweise

In manchen Faellen kann Beweis nur durch gerichtliche Anordnung erhoben werden:

| Beweismittel | Verfahren | §§ | Hinweis |
|-------------|-----------|-----|---------|
| Urkundenvorlage durch Gegner | Antrag auf Urkundenvorlage | §303ff ZPO | Gegner kann nur unter bestimmten Voraussetzungen zur Vorlage gezwungen werden |
| Urkundenvorlage durch Dritte | Antrag auf Editionspflicht | §308 ZPO | Dritte sind nur eingeschraenkt vorlagepflichtig |
| Gerichtlicher Sachverstaendiger | Beweisantrag im Verfahren | §351ff ZPO | Kostenvorschuss durch die beweisfuehrende Partei |
| Auskunft von Behoerden | Gerichtliche Anfrage | §273a ZPO | Z.B. Steuerunterlagen, Grundbuchdaten |
| Kontoeroeffnung | Gerichtliche Anordnung | §§303ff ZPO | Bei begrundeten Verdachtsmomenten |

### 4C: Beweissicherung (§§384ff ZPO)

**Dringender Handlungsbedarf** bei Beweismitteln, die verloren gehen koennten:

- Antrag auf Beweissicherung beim zustaendigen Gericht (§384 ZPO)
- Voraussetzung: Besorgnis, dass das Beweismittel verloren geht oder seine Benutzung wesentlich erschwert wird (§384 Abs 1 ZPO)
- Auch VOR Klageerhebung moeglich (§384 Abs 2 ZPO)
- Beispiele:
  - Zustand einer Wohnung vor Auszug (Fotos durch SV)
  - Zustand eines Fahrzeugs nach Unfall
  - Zeuge, der schwer erkrankt ist
  - Gegenstaende, die beseitigt werden koennten

**Flaggen:** Wenn ein Beweismittel droht verloren zu gehen, IMMER sofort auf die Moeglichkeit der Beweissicherung hinweisen.

---

## 5. Beweislast (Burden of Proof)

### 5A: Grundregel

**Wer etwas behauptet, muss es beweisen** (§1296 ABGB als allgemeiner Grundsatz).

Im Detail:
- **Klager** muss die anspruchsbegruendenden Tatsachen beweisen (Tatbestandsmerkmale)
- **Beklagter** muss die anspruchshindernden, anspruchsvernichtenden und anspruchshemmenden Tatsachen beweisen (Einwendungen)
- **Beweismass:** Freie richterliche Beweiswuerdigung (§272 ZPO) — der Richter muss von der Wahrheit der Tatsache ueberzeugt sein (volle Ueberzeugung, keine blosse Wahrscheinlichkeit)

### 5B: Beweislastumkehr und -erleichterung

In folgenden Faellen ist die Beweislast abweichend geregelt:

| Bereich | Regelung | §§ | Wer muss was beweisen? |
|---------|----------|-----|----------------------|
| **Vertragshaftung** | Verschuldensvermutung | §1298 ABGB | Schuldner muss beweisen, dass ihn KEIN Verschulden trifft (Umkehr!) |
| **B2C Gewaehrleistung** | Mangelvermutung (12 Monate) | §924 ABGB | Unternehmer muss beweisen, dass Ware bei Uebergabe mangelfrei war |
| **Arzthaftung** | Grosse Wahrscheinlichkeit | OGH-Judikatur | Beweis, dass Schaden mit ueberwiegender Wahrscheinlichkeit auf Behandlungsfehler zurueckzufuehren ist, genuegt |
| **Anscheinsbeweis** (Prima-facie-Beweis) | Typischer Geschehensablauf | OGH-Judikatur | Wenn ein typischer Geschehensablauf vorliegt, wird die Kausalitaet vermutet — Gegner muss ernsthafte Moeglichkeit eines atypischen Verlaufs beweisen |
| **Schutzgesetzverletzung** | Umkehr der Kausalitaet | §1311 ABGB | Wer ein Schutzgesetz verletzt, muss beweisen, dass der Schaden auch ohne die Verletzung eingetreten waere |
| **Diskriminierung (GlBG)** | Glaubhaftmachung genuegt | §12 Abs 12 GlBG | AN muss Diskriminierung nur glaubhaft machen; AG muss beweisen, dass anderer Grund vorlag |
| **Produkthaftung** | Fehlervermutung bei typischem Schaden | §1 PHG, OGH-Judikatur | Geschaedigter muss Fehler, Schaden und Kausalitaet beweisen, aber erleichtert durch typischen Geschehensablauf |
| **Verkehrsunfall (StVO-Verstoss)** | Schutzgesetzverletzung | §1311 ABGB | Verstoss gegen StVO-Norm ist Schutzgesetzverletzung — Kausalitaetsbeweis wird umgekehrt |
| **Mietrecht (Rueckstellung)** | Zustandsvermutung | §1109 ABGB | Mieter muss beweisen, dass er die Wohnung in ordnungsgemaessem Zustand zurueckgestellt hat |
| **Arbeitnehmerhaftung** | Verschuldensvermutung | §1298 ABGB analog | Arbeitgeber muss den Schaden und die Pflichtverletzung beweisen; AN muss fehlendes Verschulden beweisen |

### 5C: Beweislast nach Rechtsgebiet

In jedem Advisory-Skill die spezifische Beweislast fuer den konkreten Anspruch bestimmen:

1. **Wer traegt die Beweislast fuer die Anspruchsvoraussetzungen?**
2. **Greift eine Beweislastumkehr oder -erleichterung?**
3. **Welches Beweismass gilt?** (Volle Ueberzeugung vs. ueberwiegende Wahrscheinlichkeit vs. Glaubhaftmachung)
4. **Welche Partei profitiert von Beweisluecken?** (Non liquet — wenn der Beweis nicht erbracht werden kann, geht das zulasten der beweisbelasteten Partei)

---

## 6. Integration with Advisory Skills

Jeder Advisory-Skill soll bei Vorliegen von Beweismaterial folgenden Block in die Analyse einfuegen:

### Beweiswuerdigung

| Nr. | Beweisstuck | ZPO-Stufe | Beweiskraft | Beweisthema | Pro/Contra User |
|-----|-------------|-----------|-------------|-------------|-----------------|
| 1 | [Beschreibung] | [Stufe 1-5] | [Hoch/Mittel/Niedrig] | [Was wird damit bewiesen?] | [Pro/Contra] |

### Beweislast

| Tatsache | Beweislast bei | Beweismittel vorhanden? | Beweislage |
|----------|---------------|------------------------|------------|
| [Anspruchsvoraussetzung] | [Klager/Beklagter] | [Ja/Nein/Teilweise] | [Guenstig/Offen/Ungünstig] |

### Beweisluecken

| Fehlender Beweis | Relevant fuer | Empfehlung | Dringlichkeit |
|-----------------|---------------|------------|---------------|
| [Was fehlt?] | [Welchen Anspruch/Einwand?] | [Wie beschaffen?] | [Hoch/Mittel/Niedrig] |

### Beweisnotstand

[Nur wenn zutreffend:] Fuer die folgende(n) Tatsache(n) besteht ein Beweisnotstand: [Beschreibung]. Moegliche Auswege: [Anscheinsbeweis, Beweislasterleichterung, alternative Beweismittel].

---

## Quick Reference: ZPO Hierarchy at a Glance

```
Beweiskraft (absteigend):

1. Oeffentliche Urkunden (§292 ZPO)     ████████████████████ Hoechste
2. Private dispositive Urkunden          ██████████████████
3. Gerichtlicher Sachverstaendiger        █████████████████
4. Unbeteiligte Zeugen                    ████████████████
5. Private Urkunden (E-Mail, SMS)         ██████████████
6. Privatgutachten                        ████████████
7. Fotos/Videos mit Metadaten             ███████████
8. Beteiligte Zeugen                      █████████
9. Augenschein (nachtraeglich)            ████████
10. Screenshots ohne Verifizierung        ██████
11. Parteienvernehmung                    ████         Niedrigste
```

---

*Dieses Protokoll ist Teil des Austrian Legal Skill und wird von allen Advisory-Skills referenziert. Letzte Aktualisierung: 2026-04-08.*
