---
name: kapitalerhaltung-borghei
title: /gesellschaftsrecht:kapitalerhaltung
description: Prüfung der GmbH-Kapitalerhaltung – Verbot der Auszahlung des zur Erhaltung des Stammkapitals erforderlichen Vermögens § 30 GmbHG, Rückgewähranspruch § 31 GmbHG, Unterbilanz und bilanzielle Betrachtung, Cash-Pooling und Upstream-Sicherheiten, Geschäftsführerhaftung § 43 Abs. 3 GmbHG, Abgrenzung zur Insolvenzverschleppung. Use when geprüft werden soll, ob eine Leistung der GmbH an einen Gesellschafter gegen die Kapitalerhaltung verstößt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gesellschaftsrecht/skills/kapitalerhaltung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
---

# /gesellschaftsrecht:kapitalerhaltung

## Zweck

Die Kapitalerhaltung ist das Kernschutzsystem des GmbH-Gläubigerschutzes: Das zur Erhaltung des Stammkapitals erforderliche Vermögen darf nicht an die Gesellschafter ausgekehrt werden. Verstöße lösen einen Rückgewähranspruch der Gesellschaft sowie eine persönliche Geschäftsführerhaftung aus. Dieser Skill prüft strukturiert, ob eine geplante oder erfolgte Leistung der GmbH an einen Gesellschafter eine **verbotene Auszahlung** im Sinne des § 30 GmbHG darstellt und welche Folgen daraus erwachsen.

## Eingaben

- Art und Höhe der geplanten / erfolgten Leistung an den Gesellschafter (Darlehen, Gewinnvorab, Sachzuwendung, Sicherheitenbestellung, Dienstleistung zu nicht marktüblichen Konditionen)
- Bilanzielle Lage: Höhe des Stammkapitals, Reinvermögen (Aktiva ./. echte Passiva) vor und nach der Leistung
- Bestellte Sicherheiten zugunsten des Gesellschafters oder einer ihm nahestehenden Person (Upstream / Cross-Stream)
- Einbindung in einen Cash-Pool (physisches oder virtuelles Cash-Pooling, Konditionen, Rückführbarkeit)
- Werthaltigkeit der Gegenleistung bzw. des Rückgewähranspruchs (Bonität des Gesellschafters, Besicherung, Fälligkeit)
- Bestehen eines Beherrschungs- oder Gewinnabführungsvertrags
- Stand der Einlagen (volleingezahlt? offene Einlageforderung nach § 19 GmbHG?)

## Sub-Agent-Architektur

Die Prüfung wird in fachlich getrennte Schritte zerlegt, die nacheinander aufeinander aufbauen. Ein erster Schritt klärt den **Anwendungsbereich** des § 30 GmbHG (Leistung an einen Gesellschafter in dieser Eigenschaft). Ein bilanzieller Schritt ermittelt, ob durch die Leistung eine **Unterbilanz** entsteht oder vertieft wird. Ein dritter Schritt bewertet die **Sonderfälle** Cash-Pooling und Upstream-Besicherung sowie die **Vollwertigkeit** eines etwaigen Gegenleistungs- oder Rückgewähranspruchs nach § 30 Abs. 1 S. 2 GmbHG. Erst danach werden Rückgewähranspruch (§ 31 GmbHG) und Geschäftsführerhaftung (§ 43 Abs. 3 GmbHG) sowie die Abgrenzung zum insolvenzrechtlichen Solvenzschutz bestimmt. Jeder Schritt liefert ein Zwischenergebnis, das der nächste übernimmt; offene Tatsachenfragen werden ausdrücklich als solche markiert, nicht unterstellt.

## Ablauf

### 1. Anwendungsbereich § 30 GmbHG

[§ 30 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__30.html) verbietet die Auszahlung des zur Erhaltung des Stammkapitals erforderlichen Vermögens an die Gesellschafter. Voraussetzungen:

- **Auszahlung** = jede Leistung aus dem Gesellschaftsvermögen ohne (vollwertige) Gegenleistung, auch verdeckt (überhöhte Vergütung, zinsloses Darlehen, Sicherheitenstellung, Nutzungsüberlassung).
- **Empfänger** = ein Gesellschafter oder eine ihm zuzurechnende nahestehende Person; die Leistung muss an ihn **in seiner Eigenschaft als Gesellschafter** (causa societatis) erfolgen, nicht aus einem unabhängigen Drittgeschäft.
- Maßgeblich ist das **Mindeststammkapital** von 25.000 EUR ([§ 5 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__5.html)) bzw. das tatsächlich übernommene, höhere Stammkapital.

### 2. Unterbilanz-Prüfung (bilanzielle Betrachtung)

Der Verstoß bestimmt sich nach der bilanziellen **Unterbilanz**: Eine verbotene Auszahlung liegt vor, wenn das nach Handelsbilanzwerten ermittelte **Reinvermögen** (Aktiva abzüglich echter Verbindlichkeiten) das Stammkapital nicht mehr deckt oder durch die Leistung darunter sinkt.

- Reinvermögen ≥ Stammkapital nach der Leistung → keine Unterbilanz, Auszahlung zulässig.
- Reinvermögen < Stammkapital → **Unterbilanz**; der das Stammkapital antastende Teil ist verboten.
- Stichtagsbetrachtung: maßgeblich ist der Zeitpunkt der Leistung; eine spätere Verschlechterung ist für § 30 GmbHG grundsätzlich unbeachtlich (anders bei Vollwertigkeit, s. Schritt 3).
- Offene Einlageforderungen nach [§ 19 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__19.html) (noch nicht voll geleistete Stammeinlagen) bleiben als Aktivposten nur eingeschränkt ansatzfähig und verschärfen die Prüfung.

### 3. Sonderfälle: Cash-Pooling, Upstream-Darlehen / -Sicherheiten, Vollwertigkeit

- **Cash-Pooling:** Die Abführung von Liquidität an den zentralen Pool (regelmäßig an die Muttergesellschaft als Gesellschafterin) ist eine Auszahlung i.S.d. § 30 GmbHG. Sie ist nach **§ 30 Abs. 1 S. 2 GmbHG** unschädlich, wenn der Rückzahlungsanspruch der GmbH gegen den Poolführer **vollwertig** ist.
- **Upstream-Darlehen / -Sicherheiten:** Ein Darlehen an den Gesellschafter oder eine zu seinen Gunsten bestellte Sicherheit ist nur zulässig, wenn der Rückgewähr- bzw. Freistellungsanspruch der GmbH vollwertig ist.
- **Vollwertigkeit** ([§ 30 Abs. 1 S. 2 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__30.html)): Der Gegenleistungs- oder Rückgewähranspruch muss nach den Maßstäben ordentlicher kaufmännischer Beurteilung **vollwertig und durchsetzbar** sein (bonitätsstarker Schuldner, keine erkennbaren Ausfallrisiken). Verschlechtert sich die Bonität nachträglich erheblich, kann eine **Pflicht zur Kündigung / Rückforderung** entstehen; deren Unterlassen begründet einen neuen Verstoß.
- Die **Ausnahme** des § 30 Abs. 1 S. 2 GmbHG gilt zudem für Leistungen aufgrund eines **Beherrschungs- oder Gewinnabführungsvertrags**.

### 4. Rückgewähranspruch § 31 GmbHG und Verjährung

Liegt eine verbotene Auszahlung vor, greift [§ 31 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__31.html):

- **Rückgewähr**: Der Empfänger hat das verbotswidrig Erlangte an die Gesellschaft zu erstatten (§ 31 Abs. 1 GmbHG).
- **Gutgläubiger Empfänger**: Erstattung nur, soweit zur Gläubigerbefriedigung erforderlich (§ 31 Abs. 2 GmbHG).
- **Ausfallhaftung der Mitgesellschafter** nach § 31 Abs. 3 GmbHG, soweit die Erstattung vom Empfänger nicht zu erlangen ist.
- **Verjährung** (§ 31 Abs. 5 GmbHG): Ansprüche aus Abs. 1 in **10 Jahren**, Ansprüche aus Abs. 3 in **5 Jahren**, beginnend mit dem Tag nach der Auszahlung.

### 5. Geschäftsführerhaftung § 43 Abs. 3 GmbHG

Geschäftsführer, die entgegen § 30 GmbHG Zahlungen leisten oder eine verbotene Auszahlung veranlassen / nicht verhindern, haften der Gesellschaft nach [§ 43 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__43.html) (Abs. 3) persönlich auf Ersatz; die Haftung tritt neben den Rückgewähranspruch gegen den Gesellschafter. Eine Weisung der Gesellschafterversammlung enthaftet insoweit nicht, als der Ersatz zur Gläubigerbefriedigung erforderlich ist (§ 43 Abs. 3 S. 3 i.V.m. § 9b Abs. 1 GmbHG).

### 6. Abgrenzung Solvenzschutz / Insolvenzantragspflicht

Die bilanzielle Kapitalerhaltung (§§ 30, 31 GmbHG) ist vom **insolvenzrechtlichen Solvenzschutz** zu trennen:

- §§ 30, 31 GmbHG schützen das Stammkapital **bilanziell** und greifen unabhängig von einer Insolvenzreife.
- Zahlungsverbote nach Eintritt von Zahlungsunfähigkeit oder Überschuldung (§ 15b InsO) und die **Insolvenzantragspflicht** nach § 15a InsO knüpfen demgegenüber an die **Liquiditäts- bzw. Überschuldungslage** an.
- Beide Regime können **kumulativ** verletzt sein; die Prüfung ist getrennt zu führen und an die [gmbh-geschaeftsfuehrerhaftung](../gmbh-geschaeftsfuehrerhaftung/SKILL.md) zu übergeben, wenn Anhaltspunkte für Insolvenzreife bestehen.

### 7. Ergebnis

Zusammenführung: Liegt eine verbotene Auszahlung vor? In welcher Höhe? Wer schuldet Rückgewähr (§ 31 GmbHG) und haftet daneben der Geschäftsführer (§ 43 Abs. 3 GmbHG)? Bestehen parallel insolvenzrechtliche Risiken?

## Risiken

- **Drittgeschäft vs. causa societatis verwechselt** — ein zu Marktkonditionen abgeschlossenes Geschäft mit einem Gesellschafter ist keine Auszahlung; vorschnelle Bejahung des § 30 GmbHG.
- **Vollwertigkeit unterstellt** — der Rückgewähranspruch bei Upstream-Darlehen oder Cash-Pooling wird ohne Bonitätsprüfung als vollwertig behandelt; spätere Verschlechterung und Kündigungspflicht übersehen.
- **Bilanzielle Betrachtung übersprungen** — Verstoß bejaht, obwohl keine Unterbilanz vorliegt, oder umgekehrt eine bestehende Unterbilanz nicht erkannt.
- **Verjährung falsch berechnet** — 10 Jahre (§ 31 Abs. 1) und 5 Jahre (§ 31 Abs. 3) sowie der Fristbeginn am Tag nach der Auszahlung verwechselt.
- **Geschäftsführerhaftung § 43 Abs. 3 GmbHG vergessen** — nur der Gesellschafter wird in Anspruch genommen, die persönliche Haftung des Geschäftsführers bleibt ungeprüft.
- **Kapitalerhaltung mit Insolvenzantragspflicht vermischt** — bilanzieller und insolvenzrechtlicher Schutz werden nicht getrennt geprüft.

## Ausgabeformat

```
KAPITALERHALTUNGS-PRÜFUNG — <Mandat> — <Datum>

I.    Anwendungsbereich § 30 GmbHG
      Leistung an Gesellschafter (causa societatis)?   [✅ / ❌]
      Art / Höhe der Leistung                          <…>
II.   Unterbilanz (bilanziell)
      Reinvermögen vor / nach Leistung                 <…> / <…>
      Stammkapital                                     <…> (≥ 25.000 EUR, § 5 GmbHG)
      Unterbilanz?                                     [✅ / ❌ — verbotene Auszahlung in Höhe <…>]
III.  Sonderfälle
      Cash-Pooling / Upstream                          [betroffen / nicht]
      Vollwertigkeit Rückgewähr-/Gegenanspruch         [✅ / ❌ — § 30 Abs. 1 S. 2 GmbHG]
IV.   Rückgewähranspruch § 31 GmbHG
      Schuldner / Höhe                                 <…>
      Verjährung                                       [10 J. Abs. 1 / 5 J. Abs. 3]
V.    Geschäftsführerhaftung § 43 Abs. 3 GmbHG         [🟢 / 🟡 / 🔴]
VI.   Abgrenzung Insolvenzantragspflicht § 15a InsO    [kein Anhalt / prüfen → Übergabe]

Empfehlung: <…>
```
