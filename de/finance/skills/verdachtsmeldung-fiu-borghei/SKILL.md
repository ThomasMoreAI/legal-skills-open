---
name: verdachtsmeldung-fiu-borghei
title: /geldwaesche-aml-kyc:verdachtsmeldung-fiu
description: Prüfung und Entwurf einer Verdachtsmeldung an die FIU nach § 43 GwG – niedrige Meldeschwelle ('Tatsachen darauf hindeuten'), Form über goAML, § 46 Stillhaltefrist (3 Werktage), § 47 Tippoff-Verbot, § 48 Haftungsfreistellung, Berufsrechts-Sondervorschrift § 43 II GwG für RAe / Notare / StB. Use when ein Verpflichteter eine auffällige Geschäftsbeziehung oder Transaktion bewerten und ggf. melden muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/geldwaesche-aml-kyc/skills/verdachtsmeldung-fiu
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /geldwaesche-aml-kyc:verdachtsmeldung-fiu

## Zweck

Der Skill prüft die Meldepflicht nach § 43 I GwG („Tatsachen, die darauf hindeuten"), entwirft den Meldetext für das elektronische FIU-Portal **goAML** und stellt die flankierenden Pflichten sicher: **Unverzüglichkeit** (§ 43 I GwG), **Stillhaltefrist** drei Werktage (§ 46 GwG), **Tippoff-Verbot** (§ 47 GwG), **Anonymitäts- und Haftungsschutz** der meldenden Person (§§ 47 II, 48 GwG). Berufsrechtliche Sondervorschriften für Anwälte / Notare / StB (§ 43 II GwG) werden gesondert geprüft.

## Eingaben

- Verpflichteten-Typ nach § 2 GwG (mit besonderer Markierung bei § 2 I Nr. 10–12 GwG: RAe / Patentanwälte / Notare / StB / WP)
- konkreter Anlass (Transaktionsmuster, KYC-Auffälligkeit, Drittinformation, Medien)
- bisherige KYC-Erkenntnisse (Sorgfaltspflichtniveau, Transparenzregister)
- Zeitdruck (geplante Transaktion / Beurkundungstermin)
- bei Berufsgeheimnisträgern: liegt eine Konstellation des § 43 II GwG vor (wissentliche Beteiligung an GW)?

## Sub-Agent-Architektur

Researcher liefert § 43 GwG mit § 46 (Stillhaltepflicht) und § 47 (Tippoff-Verbot, Anonymitätsschutz), § 48 (Haftungsfreistellung), Berufsrechts-Sondervorschriften (§ 43e BRAO, § 14a BNotO), FIU-Anwendungshinweise, Rspr. (BVerwG zur Meldeschwelle) und Kommentarstellen. Drafter entwirft den goAML-Meldetext (Sachverhalt → Auffälligkeiten → Risikoindikatoren, **ohne** rechtliche Subsumtion). Reviewer prüft Pflicht-Blocker § 43 (Unverzüglichkeit), § 46 (3 Werktage), § 47 (Tippoff) und Berufsrechts-Privileg.

## Ablauf

### 1. Meldeschwelle (§ 43 I GwG)

Tatbestand: „Tatsachen, die darauf hindeuten, dass …"

- ein Vermögensgegenstand aus einer **Vortat zur Geldwäsche** (§ 261 StGB) herrührt,
- die Transaktion / Geschäftsbeziehung der **Terrorismusfinanzierung** dient, oder
- der Vertragspartner seiner Pflicht zur **Offenlegung des wirtschaftlich Berechtigten** nicht nachgekommen ist.

Die Schwelle ist **niedrig**: kein konkreter Tatverdacht iSv § 152 II StPO, sondern objektive Anhaltspunkte. Pflicht entsteht **unabhängig** vom Wert der Transaktion. Maßgeblich ist die ex-ante-Sicht des Verpflichteten. Auslegung der Schwelle: BVerwG, Urt. v. — Az. `[unverifiziert – BVerwG-Rspr. zur Auslegung in juris prüfen]`; FIU-AuA.

### 2. Unverzüglichkeit (§ 43 I GwG)

„Unverzüglich" = ohne schuldhaftes Zögern (§ 121 I BGB-Maßstab analog). Praktisch: binnen weniger Geschäftsstunden bis -tage nach Erkennen der Indikatoren, intern eskaliert über den GW-Beauftragten. Verzögerung ist Ordnungswidrigkeit § 56 GwG; bei Vorsatz und Vortat-Bezug ggf. § 261 StGB / § 258 StGB.

### 3. Form (§ 45 GwG, goAML)

Meldung **elektronisch** über das FIU-Portal **goAML** (Generalzolldirektion / FIU, www.zoll.de/fiu). Papierform nur in technischen Ausnahmefällen. Die Meldung enthält:

- Identifikation des meldenden Verpflichteten und der meldenden Person
- Identifizierungsdaten der Beteiligten (Vertragspartner, WB, Begünstigte)
- Sachverhaltsdarstellung in Tatsachen
- Auffälligkeiten und Risikoindikatoren (FIU-Indikatorenkatalog beachten)
- Anlagen (Belege, KYC-Dokumentation)

Eine **rechtliche Subsumtion** gegenüber der FIU ist nicht zu liefern — Tatsachen genügen.

### 4. Stillhaltefrist (§ 46 GwG, 3 Werktage)

Nach Meldung darf die gemeldete Transaktion **drei Werktage** nicht durchgeführt werden (§ 46 I GwG), beginnend mit dem auf die Meldung folgenden Werktag. Innerhalb dieser Frist können Staatsanwaltschaft / Zoll-FIU vorläufige Maßnahmen anordnen. **Ausnahmen** (§ 46 II GwG):

- die Aussetzung würde die strafrechtliche Verfolgung erschweren — dann Durchführung zulässig, aber **nachträgliche** Information FIU
- die Aussetzung ist tatsächlich nicht möglich (z. B. automatisierter Lastschriftrückgabeprozess)

### 5. Tippoff-Verbot (§ 47 GwG)

**Weder** dem Kunden / Vertragspartner / wirtschaftlich Berechtigten **noch** sonstigen Dritten darf offengelegt werden, dass eine Meldung erfolgt ist oder erwogen wird. Ausnahmen eng:

- Informationsaustausch innerhalb eines Konzerns / Konzernverbundes nach § 47 III GwG (auf Need-to-know-Basis)
- Informationsaustausch mit anderem Verpflichteten gleicher Berufsgruppe in dem Verfahren betreffenden Verpflichtungen `[unverifiziert – konkrete Norm prüfen]`
- Erörterung mit der Aufsichtsbehörde / Strafverfolgung

Verstoß: Ordnungswidrigkeit § 56 GwG, ggf. Strafbarkeit § 258 StGB (Strafvereitelung).

### 6. Anonymitäts- und Haftungsschutz (§§ 47 II, 48 GwG)

Die Identität der meldenden natürlichen Person wird **geschützt** (§ 47 II GwG); Weitergabe nur unter engen Voraussetzungen. Die Meldung führt **nicht** zur zivilrechtlichen, strafrechtlichen oder disziplinarrechtlichen Verantwortung des Meldenden, sofern nicht vorsätzlich oder grob fahrlässig unwahr gemeldet (§ 48 GwG).

### 7. Berufsgeheimnisträger (§ 43 II GwG)

Für **Rechtsanwälte, Patentanwälte, Notare, Steuerberater, vereidigte Buchprüfer** gilt die Meldepflicht nicht, soweit sich der Sachverhalt auf **Informationen bezieht, die sie im Rahmen der Tätigkeit der Rechtsberatung oder Prozessvertretung** erhalten haben. **Ausnahme**: Der Berufsträger weiß, dass der Mandant die Rechtsberatung **bewusst** für GW / TF in Anspruch nimmt — dann Meldepflicht. Maßgeblich ergänzend: § 43e BRAO, § 14a BNotO, § 50 BORA.

Die Abgrenzung ist berufsrechtlich heikel: Falschmeldung kann § 43a BRAO / § 203 StGB verletzen. **Bei Zweifelsfällen:** Konsultation der Rechtsanwaltskammer / Notarkammer und sorgfältige Dokumentation der Entscheidungsgrundlage.

### 8. Strafrechtliche Schnittstelle § 261 StGB

§ 261 StGB seit Reform 2021 als „all crimes approach" — jede rechtswidrige Tat kommt als Vortat in Betracht (§ 261 I 1 StGB). Tathandlungen: Verbergen, Verschleiern, Verschaffen, Verwahren, Verwenden. Strafbarkeit auch bei **Leichtfertigkeit** (§ 261 VI StGB). Eine **unterlassene** Verdachtsmeldung kann je nach Sachlage § 261 StGB-Beihilfe / § 258 StGB darstellen `[unverifiziert – BGH-Rspr. in juris prüfen]`.

### 9. Bußgeldrisiko

Unterlassene oder verspätete Meldung: Ordnungswidrigkeit § 56 I Nr. 64 GwG `[unverifiziert – Nr. prüfen]`. Rahmen bis 1 Mio. EUR / 10 % Jahresumsatz (§ 56 III GwG).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 43 GwG](https://www.gesetze-im-internet.de/gwg_2017/__43.html) (Meldepflicht, Sondervorschrift Berufsgeheimnisträger)
- [§ 44 GwG](https://www.gesetze-im-internet.de/gwg_2017/__44.html) (Meldepflicht Aufsichtsbehörden)
- [§ 45 GwG](https://www.gesetze-im-internet.de/gwg_2017/__45.html) (Form, goAML)
- [§ 46 GwG](https://www.gesetze-im-internet.de/gwg_2017/__46.html) (Stillhaltepflicht, 3 Werktage)
- [§ 47 GwG](https://www.gesetze-im-internet.de/gwg_2017/__47.html) (Tippoff-Verbot, Anonymitätsschutz)
- [§ 48 GwG](https://www.gesetze-im-internet.de/gwg_2017/__48.html) (Haftungsfreistellung)
- [§ 56 GwG](https://www.gesetze-im-internet.de/gwg_2017/__56.html) (Bußgeldrahmen)
- [§ 261 StGB](https://www.gesetze-im-internet.de/stgb/__261.html) (Geldwäsche-Strafrecht, „all crimes approach" seit 2021)
- [§ 258 StGB](https://www.gesetze-im-internet.de/stgb/__258.html) (Strafvereitelung)
- [§ 43e BRAO](https://www.gesetze-im-internet.de/brao/__43e.html) (GwG-Pflichten Rechtsanwälte)
- [§ 14a BNotO](https://www.gesetze-im-internet.de/bnoto/__14a.html) (Pflichten Notare)
- [Art. 33–39 RL (EU) 2015/849](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L0849) (Meldepflichten, Schutz Meldender)
- VO (EU) 2024/1624 (AMLR) `[unverifiziert – Anwendungsbeginn 2027]`

### Verwaltungsvorschriften und Portale

- FIU (Generalzolldirektion), Anwendungshinweise zum GwG, jeweils gültige Fassung — www.zoll.de/fiu
- BaFin-AuA, Besonderer Teil Kreditinstitute, Abschnitt Verdachtsmeldung
- FIU-Indikatorenkatalog für Verdachtsmomente (sektorale Ausgaben)
- goAML-Portal (elektronische Meldung) — www.goaml.fiu.bund.de `[unverifiziert – konkrete URL prüfen]`

### Kommentare

- Herzog, GwG, X. Aufl. Jahr, §§ 43–48 `[unverifiziert – Auflage prüfen]`
- Bülte, GwG, §§ 43 ff. `[unverifiziert]`
- Quedenfeld, Handbuch Bekämpfung Geldwäsche, Kap. zur Verdachtsmeldung
- MüKoStGB / NK-StGB / Fischer zu § 261 StGB

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

- BVerwG zur Auslegung der Meldeschwelle „Tatsachen darauf hindeuten" `[unverifiziert]`
- BGH-Strafsenat zu § 261 StGB n.F. nach Reform 2021 (Vortat-Spektrum, Leichtfertigkeit) `[unverifiziert]`
- BVerfG zum Verhältnis Meldepflicht / Verschwiegenheit der Berufsgeheimnisträger `[unverifiziert]`

## Ausgabeformat

**Internes Memo** (vor goAML-Meldung):

```
INTERNES MEMO — Verdachtsmeldung § 43 GwG
Verpflichteter: <Firma>, § 2 I Nr. <…> GwG
Vorgang: <Beschreibung>
Datum / Uhrzeit Eskalation an GW-Beauftragten: <…>
Datum / Uhrzeit geplante Meldung: <…>

I.   Sachverhalt
II.  Risikoindikatoren (Tatsachen, keine Wertungen)
III. Subsumtion § 43 I GwG (Meldeschwelle)
IV.  Sondervorschrift § 43 II GwG (Berufsgeheimnis)? — nur bei RAe/StB/Notaren
V.   Unverzüglichkeit § 43 I — Begründung der Frist
VI.  Stillhaltepflicht § 46 — laufende Transaktion?
VII. Tippoff-Verbot § 47 — interne Kommunikationsregeln
VIII. Risikoeinstufung
     🟢 / 🟡 / 🔴

IX.  Quellenverzeichnis
```

**goAML-Meldetext** (Tatsachen, keine rechtliche Subsumtion):

```
MELDUNG NACH § 43 GwG

1. Meldender Verpflichteter
   - Firma, Anschrift, GwG-Verpflichteten-Typ
   - meldende Person (Geldwäschebeauftragter)

2. Beteiligte
   - Vertragspartner (Identifizierungsdaten)
   - wirtschaftlich Berechtigter
   - sonstige Beteiligte

3. Sachverhalt
   <Tatsachenschilderung — Datum, Uhrzeit, Vorgang, Beträge>

4. Auffälligkeiten und Risikoindikatoren
   <FIU-Indikatorenkatalog-Verweis, soweit anwendbar>

5. Bisherige KYC-Erkenntnisse
   <Sorgfaltspflichtniveau, Transparenzregister, frühere Vorgänge>

6. Anlagen
   <Belege, KYC-Dokumentation, Transaktionsauszüge>
```

## Beispiel (Auszug, internes Memo, Gutachtenstil)

> **III. Subsumtion § 43 I GwG**
>
> Die Mandantin bietet die Anzahlung in Höhe von 80.000 EUR in bar an. Bargeldzahlungen oberhalb der typischen Branchenschwellen sind nach dem FIU-Indikatorenkatalog für den Immobiliensektor regelmäßig auffällig; verstärkt wird das Indiz dadurch, dass der Käufer über eine zwischengeschaltete Briefkastenkonstruktion in einem Offshore-Zentrum agiert (Hochrisikohinweis nach § 15 III Nr. 3 GwG, komplexe Struktur). Diese Tatsachen lassen objektiv den Schluss zu, dass die Mittel aus einer Vortat iSv § 261 StGB herrühren könnten; die Schwelle des § 43 I GwG („Tatsachen, die darauf hindeuten") ist damit erreicht. Eine über den Anfangsverdacht des § 152 II StPO hinausgehende Konkretisierung ist nicht erforderlich (vgl. FIU-AuA, Allgemeiner Teil; Herzog, GwG, § 43 Rn. 10 ff. `[unverifiziert]`). Die Sondervorschrift § 43 II GwG greift nicht: Notare sind zwar Berufsgeheimnisträger, die Vorschrift sperrt die Meldepflicht aber nicht bei Geldwäscheverdacht im Rahmen einer Beurkundungstätigkeit nach § 2 I Nr. 10 lit. b GwG (sondern primär bei Rechtsberatung); zudem deutet die Konstellation auf wissentliche Inanspruchnahme zu GW-Zwecken hin (§ 43 II 2 GwG), was die Sperrwirkung ohnehin aufhebt. **Empfehlung:** unverzügliche Meldung über goAML; Stillhaltefrist § 46 GwG beachten (Beurkundungstermin verschieben); striktes Tippoff-Verbot § 47 GwG.

## Risiken / typische Fehler

- **Schwellen-Erhöhung über den Wortlaut hinaus** — der Verpflichtete darf die Meldeschwelle nicht erhöhen („nur bei konkreten Anhaltspunkten").
- **Verspätete Meldung** wegen interner Eskalations- / Freigabeketten — Verletzung Unverzüglichkeit § 43 I GwG.
- **Tippoff durch Routinekommunikation** — Bestätigungsmails an Kunde („Ihre Transaktion wird derzeit zusätzlich geprüft"), Kontoauszugskommentare, telefonische Nachfragen.
- **Stillhaltepflicht ignoriert** — laufende automatisierte Buchungsprozesse müssen so eingerichtet sein, dass Sperrung möglich ist.
- **Falsche Anwendung Berufsrechts-Privileg § 43 II GwG** — Anwälte / Notare / StB melden zu schnell oder zu spät; Folge entweder § 203 StGB-Verstoß oder § 56 GwG-Bußgeld.
- **Rechtliche Subsumtion in der goAML-Meldung** — die FIU benötigt Tatsachen, keine Begründung; rechtliche Bewertungen werden im internen Memo dokumentiert.
- **Kein internes Vier-Augen-Prinzip** beim GW-Beauftragten — bei Krankheit / Urlaub fehlende Vertretung verletzt § 7 GwG.
