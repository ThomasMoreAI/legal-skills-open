---
name: data-act-vertragsklauseln-borghei
title: /datenwirtschaftsrecht:data-act-vertragsklauseln
description: Vertragsgestaltung und Klauselkontrolle nach der EU-Datenverordnung – Bedingungen der Bereitstellung an Datenempfänger Art. 8 (fair, angemessen, diskriminierungsfrei, transparent), angemessene Gegenleistung Art. 9 mit Kostendeckelung für KMU und Forschungseinrichtungen Art. 9 Abs. 4, Streitbeilegung Art. 10, Unwirksamkeit einseitig auferlegter missbräuchlicher Klauseln Art. 13 mit schwarzer Liste Abs. 4 und grauer Liste Abs. 5, Unbeachtlichkeit abweichender Klauseln Art. 7 Abs. 2, Verhältnis zur AGB-Kontrolle §§ 305 ff. BGB und zeitliche Geltung nach Art. 50. Use when ein Datenlizenz-, Datenbereitstellungs- oder IoT-Vertrag zu entwerfen oder auf Data-Act-Konformität zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenwirtschaftsrecht/skills/data-act-vertragsklauseln
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: de
---

# /datenwirtschaftsrecht:data-act-vertragsklauseln

## Zweck

Der Skill prüft und entwirft die vertragliche Ebene der Datenwirtschaft: die Bedingungen, unter denen ein Dateninhaber Daten an einen Datenempfänger bereitstellt, die Berechnung der Gegenleistung und die Kontrolle einseitig auferlegter Klauseln nach Art. 13. Er hält die beiden deutschen Kontrollmaßstäbe auseinander — die unionsrechtliche Missbrauchskontrolle des Art. 13 und die AGB-Kontrolle der §§ 305 ff. BGB — und ordnet jede beanstandete Klausel dem richtigen Maßstab zu.

## Eingaben

- Vertragsentwurf oder Klauselwerk mit Bezeichnung der einseitig gestellten Klauseln
- Rollen: Dateninhaber, Datenempfänger, Nutzer; Größenklasse jeder Partei
- Datum des Vertragsschlusses; bei Altverträgen: Laufzeit, unbefristet oder Enddatum
- Kalkulationsgrundlage der geforderten Gegenleistung (Kosten, Investitionen, Marge)
- Ob der Datenempfänger KMU oder gemeinnützige Forschungseinrichtung ist
- Ob die Bereitstellung auf Art. 5 (Verlangen des Nutzers) oder auf freiwilliger Vereinbarung beruht

## Sub-Agent-Architektur

Der Researcher beschafft Normtext, Erwägungsgründe, etwaige Mustervertragsklauseln nach Art. 41 und Kommissionsleitlinien zur Berechnung der Gegenleistung nach Art. 9 Abs. 5. Der Drafter ordnet jede Klausel den Katalogen des Art. 13 Abs. 4 und Abs. 5 zu und formuliert konforme Alternativen. Der Reviewer prüft die zeitliche Anwendbarkeit nach Art. 50, die Abgrenzung zur AGB-Kontrolle und ob die Behauptung „einseitig auferlegt" tatsächlich belegt ist.

## Ablauf

### 1. Kontrollmaßstab bestimmen — Art. 13 oder §§ 305 ff. BGB

Beide Regime können nebeneinander anwendbar sein, sie sind aber nicht deckungsgleich:

| Merkmal | Art. 13 Data Act | §§ 305 ff. BGB |
|---|---|---|
| Anwendungsbereich | B2B; Klauseln über Datenzugang, Datennutzung, Haftung und Rechtsbehelfe bei datenbezogenen Pflichten | alle vorformulierten Vertragsbedingungen |
| Auslöser | Klausel **einseitig auferlegt** | Klausel für eine Vielzahl von Verträgen vorformuliert und **gestellt** |
| Maßstab | grobe Abweichung von guter Geschäftspraxis bei Datenzugang und -nutzung oder Verstoß gegen Treu und Glauben (Art. 13 Abs. 3) | unangemessene Benachteiligung entgegen Treu und Glauben ([§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html)) |
| Kataloge | schwarze Liste Abs. 4, graue Liste Abs. 5 | [§ 308](https://www.gesetze-im-internet.de/bgb/__308.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html) — im B2B über § 310 Abs. 1 nur Indizwirkung |
| Rechtsfolge | Klausel bindet die andere Partei nicht | Klausel unwirksam, Vertrag im Übrigen wirksam ([§ 306 BGB](https://www.gesetze-im-internet.de/bgb/__306.html)) |

Zwei Klarstellungen, die Streit ersparen:

- **Art. 13 Abs. 2**: Klauseln, die zwingenden Bestimmungen des Unionsrechts entsprechen oder die bei Fehlen einer Regelung geltenden unionsrechtlichen Bestimmungen abbilden, gelten **nicht** als missbräuchlich.
- **Art. 7 Abs. 2**: Klauseln, die die Nutzerrechte aus Kapitel II ausschließen, davon abweichen oder deren Wirkung abändern, sind für den Nutzer **schon deshalb** nicht bindend — ohne Missbrauchsprüfung.

### 2. Zeitliche Anwendbarkeit des Kapitels IV prüfen (Art. 50)

- Verträge, die **nach dem 12.09.2025** geschlossen wurden: Art. 13 gilt.
- Verträge, die **am oder vor dem 12.09.2025** geschlossen wurden: Art. 13 gilt **ab dem 12.09.2027**, sofern der Vertrag unbefristet ist oder seine Geltungsdauer frühestens zehn Jahre nach dem 11.01.2024 endet.

Bei Altverträgen ist deshalb zuerst die Laufzeitklausel auszuwerten, bevor über Missbräuchlichkeit gestritten wird.

### 3. Bereitstellungsbedingungen nach Art. 8 prüfen

Ist der Dateninhaber verpflichtet, einem Datenempfänger Daten bereitzustellen, hat er dies zu **fairen, angemessenen und diskriminierungsfreien Bedingungen** und **transparent** zu tun. Praktische Konsequenzen:

- Unterschiedliche Konditionen für vergleichbare Datenempfänger sind zu rechtfertigen; die Diskriminierungsfreiheit ist dokumentationspflichtig.
- Der Dateninhaber darf die Bereitstellung nicht von der Einräumung weitergehender Nutzungsrechte an eigenen Daten des Empfängers abhängig machen, wenn dies der guten Geschäftspraxis grob widerspricht (Verzahnung mit Art. 13 Abs. 5 Buchst. b).
- Exklusivitätsabreden über Daten, die einem Zugangsanspruch unterliegen, sind kritisch zu prüfen.

### 4. Gegenleistung nach Art. 9 berechnen

Art. 9 Abs. 1: Jede zwischen Dateninhaber und Datenempfänger im B2B-Verhältnis vereinbarte Gegenleistung muss **diskriminierungsfrei und angemessen** sein; sie **darf eine Marge enthalten**.

Nach Art. 9 Abs. 2 sind insbesondere zu berücksichtigen:

1. die **angefallenen Kosten der Bereitstellung** — insbesondere Formatierung, elektronische Verbreitung und Speicherung;
2. **Investitionen in die Erhebung und Generierung** der Daten, wobei zu berücksichtigen ist, ob andere Parteien beigetragen haben.

Nach Art. 9 Abs. 3 kann die Gegenleistung von Umfang, Format und Art der Daten abhängen.

**Deckelung nach Art. 9 Abs. 4:** Ist der Datenempfänger ein **KMU** oder eine **gemeinnützige Forschungseinrichtung** ohne Partner- oder verbundene Unternehmen, die keine KMU sind, darf die Gegenleistung die **Kosten nach Abs. 2 Buchst. a nicht übersteigen** — also keine Marge und keine Investitionsumlage.

Nach Art. 9 Abs. 7 hat der Dateninhaber die **Berechnungsgrundlage so detailliert offenzulegen**, dass der Empfänger die Einhaltung der Abs. 1 bis 4 beurteilen kann. Eine Pauschale ohne Kalkulationsnachweis ist damit angreifbar.

### 5. Klauselkatalog des Art. 13 abarbeiten

**Stets missbräuchlich (Art. 13 Abs. 4 — schwarze Liste), wenn die Klausel bezweckt oder bewirkt:**

- a) Ausschluss oder Beschränkung der Haftung der auferlegenden Partei für **Vorsatz oder grobe Fahrlässigkeit**;
- b) Ausschluss der Rechtsbehelfe der anderen Partei bei Nichterfüllung oder Ausschluss der Haftung der auferlegenden Partei bei Pflichtverletzung;
- c) **alleiniges Bestimmungsrecht** der auferlegenden Partei darüber, ob die gelieferten Daten vertragsgemäß sind, oder über die Auslegung der Vertragsklauseln.

**Vermutet missbräuchlich (Art. 13 Abs. 5 — graue Liste), wenn die Klausel bezweckt oder bewirkt:**

- a) unangemessene Beschränkung der Rechtsmittel oder der Haftung bzw. Erweiterung der Haftung der unterlegenen Partei;
- b) Zugriff auf und Nutzung von Daten der anderen Partei in einer Weise, die deren berechtigten Interessen erheblich schadet — insbesondere bei sensiblen Geschäftsdaten, Geschäftsgeheimnissen oder Rechten des geistigen Eigentums;
- c) Hinderung an der Nutzung der von ihr bereitgestellten oder generierten Daten;
- d) Hinderung an der Kündigung innerhalb angemessener Frist;
- e) Hinderung, während der Laufzeit oder in angemessener Frist nach Kündigung eine **Kopie** der bereitgestellten oder generierten Daten zu erhalten;
- f) Kündigung durch die auferlegende Partei mit unangemessen kurzer Frist, außer bei schwerwiegenden Gründen;
- g) wesentliche einseitige Änderung von Preis, Art, Format, Qualität oder Menge der Daten ohne stichhaltige, im Vertrag spezifizierte Begründung und ohne Kündigungsrecht der anderen Partei.

Zu Buchst. g stellt Art. 13 klar: Änderungsvorbehalte in unbefristeten Verträgen bleiben zulässig, wenn eine im Vertrag spezifizierte stichhaltige Begründung vorliegt, die Gegenpartei rechtzeitig unterrichtet wird und ihr ein Kündigungsrecht zusteht.

### 6. Streitbeilegung und Durchsetzung

- **Art. 10** — Streitbeilegungsstellen entscheiden über Streitigkeiten zur Gegenleistung und zu den Bedingungen der Bereitstellung. In Deutschland lässt die Bundesnetzagentur diese Stellen nach [§ 5 DADG](https://www.gesetze-im-internet.de/dadg/__5.html) zu; die unterlassene Unterrichtung nach § 5 Abs. 2 S. 3 DADG ist nach § 15 Abs. 1 Nr. 1 DADG bußgeldbewehrt.
- **Art. 38, 39** — Beschwerde bei der Bundesnetzagentur und gerichtlicher Rechtsbehelf.
- Die Unwirksamkeitsfolge des Art. 13 Abs. 1 wirkt **einredeweise im Zivilprozess**: Die betroffene Partei ist an die Klausel nicht gebunden; einer behördlichen Feststellung bedarf es nicht.

## Deterministische Berechnung

Die Angemessenheit der Gegenleistung ist keine Rechenaufgabe, die Vertragsfristen sind es. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) berechnet Kündigungs- und Übergangsfristen sowie den Verjährungslauf für Rückforderungen überhöhter Entgelte:

```bash
# Kündigungsfrist aus dem Datenlizenzvertrag: 3 Monate ab 31.03.2026
python -m scripts.legal_calc.cli frist --ereignis 31.03.2026 --menge 3 --einheit monate --land BY

# Regelverjährung § 195 BGB für Rückforderung überhöhter Gegenleistung
python -m scripts.legal_calc.cli verjaehrung --entstehung 12.05.2026 --kenntnis 12.05.2026
```

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/2854, Art. 7 Abs. 2, Art. 8, 9, 10, 12, 13, 38, 39, 41, 50 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- [DADG § 5](https://www.gesetze-im-internet.de/dadg/__5.html), [§ 15](https://www.gesetze-im-internet.de/dadg/__15.html)
- [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 306 BGB](https://www.gesetze-im-internet.de/bgb/__306.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html)

### Kommentare und Literatur

- Hennemann/Steinrötter, Data Act – Handkommentar, Art. 8, Art. 9, Art. 13.
- Specht-Riemenschneider/Hennemann, Data Act, Kommentar, Art. 13 (Verhältnis zur AGB-Kontrolle).
- Grüneberg/Grüneberg, BGB, §§ 305 ff. (Maßstab im unternehmerischen Verkehr).
- Ulmer/Brandner/Hensen, AGB-Recht, § 307 BGB (Indizwirkung der §§ 308, 309 im B2B).

### Rechtsprechung

Zur AGB-Kontrolle im unternehmerischen Verkehr ist die gefestigte Rechtsprechung des BGH zur Indizwirkung der Klauselverbote heranzuziehen; die konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren `[unverifiziert – prüfen]`. Zu Art. 13 Data Act liegt noch keine Judikatur vor; jede genannte Entscheidung ist zu belegen.

## Ausgabeformat

```
DATA-ACT-KLAUSELPRÜFUNG — <Vertrag> — <Datum>

I.   Rahmen
     Parteien / Rollen:       Dateninhaber <…> | Datenempfänger <…>
     Größenklassen:           <…>
     Vertragsschluss:         <Datum>
     Kapitel IV anwendbar:    [ja ab <Datum> / nein — Art. 50]

II.  Klauselmatrix
     Nr. | Klausel | einseitig auferlegt? | Art. 13 Abs. 4 | Art. 13 Abs. 5 | §§ 305 ff. BGB | Ergebnis
     <…>

III. Bereitstellungsbedingungen Art. 8
     Fair / angemessen / diskriminierungsfrei / transparent: <Bewertung>
     Dokumentation der Gleichbehandlung: [vorhanden / fehlt]

IV.  Gegenleistung Art. 9
     Kalkulation offengelegt (Abs. 7):   [ja / nein]
     Kostenbestandteile (Abs. 2 lit. a): <…>
     Investitionen (Abs. 2 lit. b):      <…>
     Marge:                              <…>
     KMU-/Forschungsdeckel Abs. 4:       [einschlägig — nur Kosten / nicht einschlägig]
     Ergebnis:                           [angemessen / überhöht um <…>]

V.   Änderungsvorschläge
     Klausel <Nr.>: statt „<…>" → „<konforme Fassung>"

VI.  Durchsetzung
     Streitbeilegung Art. 10 / § 5 DADG | Beschwerde Art. 38 | Klage Art. 39
     Bußgeldrisiko:            <§ 15 DADG>

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Art. 13 auf Altverträge angewandt.** Für vor dem 13.09.2025 geschlossene Verträge greift Kapitel IV erst ab dem 12.09.2027 und nur unter den Voraussetzungen des Art. 50 UAbs. 6.
- **„Einseitig auferlegt" ungeprüft unterstellt.** Art. 13 setzt die einseitige Auferlegung voraus; ausgehandelte Klauseln fallen heraus. Die Darlegung ist zu führen, nicht zu behaupten.
- **Art. 13 und §§ 305 ff. BGB vermengt.** Die Kataloge, Maßstäbe und Rechtsfolgen unterscheiden sich; jede Beanstandung ist einem Maßstab zuzuordnen.
- **Marge gegenüber einem KMU einkalkuliert.** Art. 9 Abs. 4 deckelt die Gegenleistung gegenüber KMU und gemeinnützigen Forschungseinrichtungen auf die Kosten nach Abs. 2 Buchst. a.
- **Pauschalentgelt ohne Kalkulationsnachweis.** Art. 9 Abs. 7 verlangt eine so detaillierte Offenlegung, dass die Angemessenheit überprüfbar ist.
- **Entgelt vom Nutzer statt vom Datenempfänger.** Gegenüber dem Nutzer ist die Bereitstellung nach Art. 4 Abs. 1 und Art. 5 Abs. 1 unentgeltlich.
- **Haftungsausschluss für grobe Fahrlässigkeit stehen gelassen.** Art. 13 Abs. 4 Buchst. a ist die schwarze Liste — Nichtbindung ohne Abwägung.
- **Rechtsprechung erfunden.** Zu Art. 13 gibt es noch keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
