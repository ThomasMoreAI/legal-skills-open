---
name: cloud-auftragsverarbeitung-borghei
title: /it-recht:cloud-auftragsverarbeitung
description: 'Datenschutzkonforme Gestaltung der Cloud-Nutzung: Auftragsverarbeitung nach Art. 28 DSGVO, technische und organisatorische Maßnahmen nach Art. 32 DSGVO und Drittlandtransfer nach Kapitel V DSGVO (Art. 44 ff.). Use when ein Cloud- oder SaaS-Dienst eingesetzt wird und der AVV sowie der Datentransfer geprüft oder gestaltet werden sollen.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/cloud-auftragsverarbeitung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: de
---

# /it-recht:cloud-auftragsverarbeitung

## Zweck

Wer einen Cloud-Dienst nutzt, lässt regelmäßig personenbezogene Daten durch den Anbieter verarbeiten und bleibt als Verantwortlicher in der Pflicht. Dieser Skill prüft die drei kritischen Achsen einer datenschutzkonformen Cloud-Nutzung: den Auftragsverarbeitungsvertrag (**Art. 28 DSGVO**), die Sicherheit der Verarbeitung (**Art. 32 DSGVO**) und die Zulässigkeit des Datentransfers in Drittländer (**Art. 44 DSGVO** ff., Kapitel V). Er deckt Lücken auf, bevor sie zum Bußgeldfall werden, und verzahnt sich mit dem AVV-Prüfskill des Datenschutzbereichs.

> **⚠️ Aktualität (Stand 2026-07):** Cloud-Verträge unterliegen seit dem **12.09.2025** neben der DSGVO auch dem **Data Act** ([VO (EU) 2023/2854](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854)). Dessen Kapitel VI (**Art. 23–31**) regelt den **Wechsel zwischen Datenverarbeitungsdiensten** und gilt **unabhängig davon, ob personenbezogene Daten betroffen sind** — eine reine Art.-28-DSGVO-Prüfung greift damit zu kurz.
>
> - **Wechselentgelte** („switching charges") werden **bis zum 12.01.2027 vollständig abgeschafft**. Bis dahin sind ausschließlich **kostenbasiert reduzierte** Entgelte zulässig; pauschale Ausstiegs- oder Datenexportgebühren sind bereits jetzt unzulässig.
> - **Art. 25** verlangt vertragliche Regelungen zur **Unterstützung beim Wechsel** (Ausstiegshilfe, Übergangsfristen, Datenexport in einem strukturierten, gängigen und maschinenlesbaren Format).
> - **Art. 13** unterwirft **einseitig auferlegte Vertragsklauseln über den Datenzugang in B2B-Verhältnissen** einer eigenständigen Missbräuchlichkeitskontrolle — neben §§ 305 ff. BGB.
> - Das deutsche **Data-Act-Durchführungsgesetz (DADG)** wurde am **26.03.2026** vom Bundestag beschlossen und im **BGBl. vom 29.05.2026** verkündet. Zuständige Behörde ist die **Bundesnetzagentur** (Bekanntgabe **30.05.2026**). Im selben Paket vom 26.03.2026 wurde das deutsche Durchführungsgesetz zum **Data Governance Act** beschlossen; auch dort beaufsichtigt die **BNetzA** Datenvermittlungsdienste und datenaltruistische Organisationen.
>
> Einzelne Paragrafen des DADG sind vor mandantengerichteter Verwendung am verkündeten Text zu verifizieren. `[unverifiziert - prüfen]`

## Eingaben

- Cloud-Modell (IaaS, PaaS, SaaS) und Anbieter
- Verarbeitete Datenkategorien (Standard, besondere Kategorien Art. 9, Beschäftigtendaten)
- Standort der Verarbeitung / Speicherung (EU, USA, sonstiges Drittland)
- Konzernzugehörigkeit des Anbieters (US-Mutter? Cloud Act-Zugriff?)
- Vorliegender AVV-Entwurf und Liste der Sub-Auftragsverarbeiter
- Vorhandene TOM-Dokumentation, Zertifikate (ISO 27001, C5)

## Sub-Agent-Architektur

Die Prüfung verteilt sich gedanklich auf drei Rollen. Ein **AVV-Agent** prüft den Auftragsverarbeitungsvertrag gegen den Pflichtenkatalog des Art. 28 Abs. 3 DSGVO (Gegenstand, Dauer, Weisungsbindung, Sub-Auftragsverarbeiter, Unterstützungspflichten, Löschung, Audit). Ein **TOM-Agent** bewertet die technischen und organisatorischen Maßnahmen nach Art. 32 DSGVO (Verschlüsselung, Pseudonymisierung, Verfügbarkeit, Belastbarkeit, regelmäßige Überprüfung) und gleicht sie mit dem Risiko der Datenkategorien ab. Ein **Transfer-Agent** prüft jeden Drittlandbezug nach Kapitel V (Angemessenheitsbeschluss, Standardvertragsklauseln, Transfer Impact Assessment, ergänzende Maßnahmen). Ein **Wechsel-Agent** prüft schließlich die Ausstiegs- und Wechselklauseln gegen Art. 23–31 Data Act (Wechselentgelte, Ausstiegsunterstützung, Exportformate) sowie Art. 13 Data Act (missbräuchliche Datenzugangsklauseln) — diese Achse ist von der DSGVO unabhängig und erfasst auch nicht-personenbezogene Daten. Die Rollen melden ihre Befunde an eine zusammenführende Bewertung; ein Mangel auf einer Achse blockiert die Konformität insgesamt. Rechtsprechung und Aufsichtsbeschlüsse werden nur verifiziert zitiert, sonst mit `[unverifiziert – prüfen]` markiert.

## Ablauf

### 1. Rollen- und Anwendbarkeitsklärung

- Liegt Auftragsverarbeitung vor (weisungsgebundene Verarbeitung) oder gemeinsame Verantwortlichkeit (Art. 26) oder eigene Verantwortlichkeit des Anbieters?
- Nur bei Auftragsverarbeitung ist ein AVV nach Art. 28 DSGVO der richtige Vertragstyp.

### 2. AVV-Inhaltskontrolle (Art. 28 DSGVO)

Pflichtinhalte nach Art. 28 Abs. 3 DSGVO:

- Gegenstand, Dauer, Art und Zweck der Verarbeitung, Datenkategorien, Betroffenenkreis
- Verarbeitung nur auf dokumentierte Weisung
- Vertraulichkeitsverpflichtung der Beschäftigten
- Maßnahmen nach **Art. 32 DSGVO**
- Genehmigung und Verträge mit Sub-Auftragsverarbeitern (Art. 28 Abs. 2, 4)
- Unterstützung bei Betroffenenrechten und bei Art. 32–36
- **Löschung** oder Rückgabe der Daten nach Vertragsende
- Nachweis- und **Audit**-Rechte des Verantwortlichen

### 3. Technische und organisatorische Maßnahmen (Art. 32 DSGVO)

- Verschlüsselung (Transport und Ruhe), Pseudonymisierung
- Sicherstellung von Vertraulichkeit, Integrität, Verfügbarkeit, Belastbarkeit
- Wiederherstellbarkeit nach Zwischenfall; regelmäßiges Testen
- Risikoangemessenheit insb. bei besonderen Datenkategorien (Art. 9)

### 4. Drittlandtransfer (Kapitel V, Art. 44 DSGVO ff.)

- **Angemessenheitsbeschluss** (Art. 45) — z. B. EU-US Data Privacy Framework für zertifizierte US-Anbieter
- **Standardvertragsklauseln** (Art. 46) + **Transfer Impact Assessment** + ggf. ergänzende Maßnahmen (Schrems II)
- Zugriffsrisiken durch Drittstaatsbehörden (Cloud Act) bewerten
- Sub-Auftragsverarbeiter in Drittländern gesondert absichern

### 5. Anbieterwechsel und Ausstieg nach dem Data Act (Art. 23–31 VO (EU) 2023/2854)

Diese Prüfung läuft **neben** der DSGVO-Prüfung und erfasst **alle** in der Cloud verarbeiteten Daten, auch nicht-personenbezogene.

**a) Wechselentgelte (Art. 29).** Entgelte für den Wechsel zu einem anderen Anbieter oder zurück in die eigene Infrastruktur werden **bis zum 12.01.2027 vollständig abgeschafft**. In der Übergangszeit sind nur **kostenbasiert reduzierte** Entgelte zulässig, die die tatsächlich entstandenen Kosten nicht übersteigen dürfen.

Prüfpunkte im Vertrag:

- [ ] Enthält der Vertrag **Datenexport-, Ausstiegs- oder Migrationsgebühren**? Pauschalen und „Egress-Fees" für den Wechsel sind bereits jetzt unzulässig.
- [ ] Ist eine **Auslaufregelung zum 12.01.2027** aufgenommen, die die Entgelte ab diesem Datum entfallen lässt?
- [ ] Werden verbleibende Entgelte **kostenbasiert begründet und belegt**?

**b) Ausstiegsunterstützung (Art. 25).** Der Vertrag muss den Wechsel praktisch ermöglichen:

- [ ] **Wechselfrist** und Kündigungsmodalitäten vertraglich fixiert
- [ ] **Übergangszeitraum** mit aktiver Mitwirkung des Anbieters
- [ ] **Export aller Daten und digitalen Vermögenswerte** in einem strukturierten, gängigen und maschinenlesbaren Format
- [ ] **Beschreibung der exportierbaren Daten** und der verfügbaren Schnittstellen
- [ ] **Löschung** der Daten beim Altanbieter nach Abschluss des Wechsels — hier verzahnt sich Art. 25 Data Act mit der Löschpflicht aus Art. 28 Abs. 3 lit. g DSGVO
- [ ] Keine vertraglichen oder technischen **Wechselhindernisse** (Lock-in durch proprietäre Formate ohne Exportpfad)

**c) Missbräuchliche Klauseln (Art. 13).** Einseitig auferlegte Klauseln über den Datenzugang in B2B-Verträgen unterliegen einer **eigenständigen** Missbräuchlichkeitskontrolle. Sie tritt **neben** die AGB-Kontrolle nach §§ 305 ff. BGB und ist auch dort zu prüfen, wo die AGB-Kontrolle nicht greift.

**d) Zuständigkeit und Durchsetzung.** Zuständige deutsche Behörde ist nach dem **DADG** (BGBl. 29.05.2026, Bekanntgabe 30.05.2026) die **Bundesnetzagentur** — nicht die Datenschutzaufsicht. Data-Act-Verstöße und DSGVO-Verstöße werden damit von **unterschiedlichen Behörden** verfolgt; beide Verfahren können nebeneinander laufen. Sanktionsrahmen und Verfahrensvorschriften am verkündeten DADG-Text prüfen. `[unverifiziert - prüfen]`

### 6. Dokumentation und Rechenschaft

- Eintrag im Verzeichnis von Verarbeitungstätigkeiten (Art. 30)
- Datenschutz-Folgenabschätzung (Art. 35) bei hohem Risiko

## Risiken / typische Fehler

- **Fehlender AVV** — Cloud-Nutzung ohne AVV nach Art. 28 DSGVO ist ein eigenständiger Verstoß; Bußgeldrisiko nach Art. 83 DSGVO.
- **Drittlandtransfer** ohne tragfähige Grundlage — US-Anbieter ohne DPF-Zertifizierung oder ohne Standardvertragsklauseln samt TIA verletzt Kapitel V (Art. 44 DSGVO).
- **Sub-Auftragsverarbeiter** ungeprüft — fehlende Genehmigung oder Weiterreichung der Pflichten verletzt Art. 28 Abs. 4 DSGVO.
- **Bußgeld** — unzureichende Maßnahmen nach Art. 32 DSGVO oder unzulässiger Transfer können Bußgelder bis 20 Mio. EUR / 4 % auslösen (Art. 83 DSGVO).
- **Cloud-Vertrag nur nach DSGVO geprüft** — der **Data Act** gilt seit **12.09.2025** und erfasst **auch nicht-personenbezogene Daten**. Eine reine Art.-28-Prüfung übersieht die Wechsel- und Ausstiegspflichten der Art. 23–31 vollständig.
- **Wechsel- und Datenexportentgelte im Vertrag belassen** — sie entfallen **bis zum 12.01.2027 vollständig**; bis dahin sind nur **kostenbasiert reduzierte** Entgelte zulässig. Pauschale Ausstiegs- oder Egress-Gebühren sind bereits heute unzulässig, auch wenn der Anbieter sie weiter in Rechnung stellt.
- **Keine Ausstiegsunterstützungsklausel nach Art. 25** — Wechselfrist, Übergangszeitraum, Exportformat und Mitwirkungspflichten des Anbieters müssen **vertraglich** geregelt sein; ein faktisch funktionierender Export genügt nicht.
- **Löschpflichten nicht verzahnt** — Art. 25 Data Act (Löschung beim Altanbieter nach dem Wechsel) und Art. 28 Abs. 3 lit. g DSGVO (Löschung/Rückgabe nach Vertragsende) sind gemeinsam zu regeln, sonst bleibt eine Regelungslücke.
- **Art. 13 Data Act neben §§ 305 ff. BGB übersehen** — einseitig auferlegte Datenzugangsklauseln in B2B-Verträgen unterliegen einer **eigenständigen** Missbräuchlichkeitskontrolle, die auch dort greift, wo die AGB-Kontrolle nicht durchdringt.
- **Falsche Aufsichtsbehörde adressiert** — für den Data Act ist in Deutschland nach dem **DADG** (BGBl. 29.05.2026) die **Bundesnetzagentur** zuständig, nicht die Datenschutzaufsicht. Data-Act- und DSGVO-Verfahren laufen getrennt und können parallel geführt werden.

## Ausgabeformat

```
CLOUD-AUFTRAGSVERARBEITUNG — <Dienst / Anbieter> — <Datum>

I.    Rolle:                      [Auftragsverarbeitung / gem. Verantwortl. / eigen]
II.   AVV (Art. 28 DSGVO)
      Vollständigkeit:            [✓ / 🔴 lückenhaft]   Fehlend: <…>
      Sub-Auftragsverarbeiter:    [genehmigt / ungeregelt]
      Audit / Löschung:           [✓ / 🔴]
III.  TOM (Art. 32 DSGVO)
      Verschlüsselung / Risiko:   [angemessen / ⚠️]
IV.   Drittlandtransfer (Art. 44 DSGVO)
      Standort:                   [EU / USA / Drittland]
      Grundlage:                  [Angemessenheit / SCC + TIA / 🔴 keine]
V.    Wechsel / Ausstieg (Data Act Art. 23–31)
      Wechselentgelte:            [keine / kostenbasiert / 🔴 pauschal unzulässig]
      Auslauf zum 12.01.2027:     [geregelt / 🔴 fehlt]
      Ausstiegshilfe Art. 25:     [Frist / Übergang / Exportformat — ✓ / 🔴]
      Löschung beim Altanbieter:  [✓ / 🔴]
      Art. 13 (missbräuchliche Datenzugangsklauseln): [✓ / ⚠️]
      Zuständige Behörde:         BNetzA (DADG) — getrennt von der Datenschutzaufsicht
VI.   Dokumentation
      VVT / DSFA:                 [✓ / offen]

Bußgeldrisiko (Art. 83 DSGVO):    <Einschätzung>
Data-Act-Risiko (BNetzA):         <Einschätzung>
Handlungsempfehlung:              <…>
```

## Quellen

- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Auftragsverarbeiter)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Sicherheit der Verarbeitung)
- [Art. 44 DSGVO ff. — Kapitel V](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Drittlandtransfer), Art. 45, 46
- [Art. 83 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Geldbußen)
- EU-US Data Privacy Framework; EDSA-Empfehlungen 01/2020 (ergänzende Maßnahmen) `[unverifiziert – prüfen]`
- [VO (EU) 2023/2854 (Data Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854) — anwendbar seit **12.09.2025**; Art. 13 (missbräuchliche Klauseln), Art. 23–31 (Wechsel zwischen Datenverarbeitungsdiensten), insb. Art. 25 (Ausstiegsunterstützung) und Art. 29 (Wechselentgelte, vollständiger Wegfall bis **12.01.2027**)
- **Data-Act-Durchführungsgesetz (DADG)** — Bundestag 26.03.2026, BGBl. 29.05.2026; zuständige Behörde: **Bundesnetzagentur** (Bekanntgabe 30.05.2026). Einzelnormen `[unverifiziert - prüfen]`
- [Bundesnetzagentur](https://www.bundesnetzagentur.de/) — zuständige Behörde für Data Act und Data Governance Act (Datenvermittlungsdienste, datenaltruistische Organisationen)
