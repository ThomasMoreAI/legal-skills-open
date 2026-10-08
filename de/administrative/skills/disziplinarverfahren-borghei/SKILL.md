---
name: disziplinarverfahren-borghei
title: /beamten-disziplinarrecht:disziplinarverfahren
description: Behördliches Disziplinarverfahren gegen Beamtinnen und Beamte – Dienstvergehen § 47 BeamtStG / § 77 BBG, Einleitung § 17 BDG, Unterrichtung und Belehrung § 20 BDG, Beweiserhebung § 24 BDG, Disziplinarmaßnahmen § 5 BDG, Bemessung § 13 BDG, Maßnahmeverbot wegen Zeitablaufs § 15 BDG, Verhältnis zum Strafverfahren §§ 22, 23 BDG, Abschluss durch Disziplinarverfügung § 33 BDG und Rechtsschutz §§ 41, 52 BDG. Use when gegen eine Beamtin oder einen Beamten ein Disziplinarverfahren eingeleitet ist oder droht und Maßnahmenprognose, Verfahrensrechte und Rechtsschutz zu klären sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/beamten-disziplinarrecht/skills/disziplinarverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /beamten-disziplinarrecht:disziplinarverfahren

## Zweck

Der Skill führt ein Disziplinarverfahren von der Einleitung bis zur Abschlussentscheidung durch und liefert eine belastbare Maßnahmenprognose. Er sichert die Verfahrensrechte der beschuldigten Beamtin bzw. des beschuldigten Beamten und prüft die drei Sperren, die in der Praxis am häufigsten übersehen werden: Straf- und Bußgeldverfahren (§ 14 BDG), Zeitablauf (§ 15 BDG) und Verwertungsverbot (§ 16 BDG). Er entwirft die Stellungnahme nach § 20 BDG und den Rechtsbehelf gegen die Disziplinarverfügung.

## Eingaben

- Dienstherr (Bund / Land / Kommune) und Statusamt (Lebenszeit, Probe, Widerruf, Ruhestand)
- Vorwurf mit Zeitpunkt und Ort der behaupteten Pflichtverletzung
- Datum der Einleitung und der Unterrichtung, Wortlaut der Belehrung
- Innerdienstlicher oder außerdienstlicher Bezug
- Paralleles Straf-, Bußgeld- oder sonstiges Verfahren (Stand, Aktenzeichen)
- Bisherige Disziplinarvorgänge, Beurteilungen, Dienstzeit, persönliche Umstände
- Vorläufige Dienstenthebung oder Einbehaltung von Bezügen angeordnet?

## Sub-Agent-Architektur

Ein Researcher bestimmt zuerst den Rechtskreis (BBG/BDG oder BeamtStG plus Landesbeamten- und Landesdisziplinargesetz) und sammelt die Norm- und Kommentarbelege sowie die Rechtsprechung des 2. Senats des BVerwG. Ein Drafter subsumiert den Vorwurf unter die konkrete Pflichtnorm, prüft Vorwerfbarkeit und Milderungsgründe und entwirft die Stellungnahme oder den Rechtsbehelf. Ein Reviewer kontrolliert die Fristen des § 15 BDG, die Bindungswirkung nach § 23 BDG, die Zuständigkeit nach § 34 BDG und jede Fundstelle; nicht bestätigte Entscheidungen werden mit `[unverifiziert - prüfen]` markiert oder weggelassen. Keine Rolle erfindet ein Aktenzeichen.

## Ablauf

### 1. Anwendbares Recht bestimmen ([§ 1 BDG](https://www.gesetze-im-internet.de/bdg/__1.html))

**Dieser Schritt steht vor allem anderen und darf nicht übersprungen werden.** Er ist die häufigste Fehlerquelle des Gebiets.

| Dienstherr | Materielles Recht | Verfahrensrecht |
|---|---|---|
| Bund, bundesunmittelbare Körperschaften | [§ 77 BBG](https://www.gesetze-im-internet.de/bbg_2009/__77.html) | [BDG](https://www.gesetze-im-internet.de/bdg/) |
| Land, Kommune, landesunmittelbare Körperschaften | [§ 47 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__47.html) + Landesbeamtengesetz | Landesdisziplinargesetz des jeweiligen Landes |

Zwei Konsequenzen, die den Entwurf sofort bestimmen:

- Im **Bund** ergehen seit der Neuregelung des Bundesdisziplinarrechts **alle** Maßnahmen durch **Disziplinarverfügung** ([§ 33 BDG](https://www.gesetze-im-internet.de/bdg/__33.html)) — auch die Entfernung aus dem Beamtenverhältnis, die nach [§ 34 Abs. 4 BDG](https://www.gesetze-im-internet.de/bdg/__34.html) die oberste Dienstbehörde ausspricht. Eine **Disziplinarklage** des Dienstherrn kennt das BDG in der geltenden Fassung nicht mehr; der Beamte wehrt sich mit Widerspruch und Anfechtungsklage. Das Inkrafttreten dieser Neuregelung ist `[unverifiziert - prüfen]` gegen das BGBl. abzugleichen; maßgeblich ist die Fassung „zuletzt geändert durch Art. 6 G v. 19.7.2024 (BGBl. 2024 I Nr. 247)".
- In den **Ländern** besteht die **Disziplinarklage** für statusberührende Maßnahmen überwiegend fort. Wird ein Landesbeamter vertreten, ist die einschlägige Landesnorm konkret zu benennen; eine Übertragung der BDG-Systematik ist unzulässig `[unverifiziert - prüfen]` je Land.

Richter (DRiG) und Soldaten (WDO) sind nicht Gegenstand dieses Skills.

### 2. Dienstvergehen feststellen ([§ 47 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__47.html))

Ein Dienstvergehen setzt eine **schuldhafte Verletzung einer Beamtenpflicht** voraus. Die Generalklausel genügt nicht — es ist die konkrete Pflichtnorm zu benennen:

- Grundpflichten [§ 33 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__33.html) (volle Hingabe, uneigennützige Amtsführung, Verfassungstreue)
- Wohlverhalten und Erscheinungsbild [§ 34 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__34.html)
- Folgepflicht [§ 35 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__35.html)
- Verschwiegenheit [§ 37 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__37.html)
- Nebentätigkeit [§ 40 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__40.html); Belohnungen und Geschenke [§ 42 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__42.html)

**Außerdienstliches Verhalten** ist nur bei besonderer Erheblichkeit ein Dienstvergehen (§ 47 Abs. 1 S. 2 BeamtStG, § 77 Abs. 1 S. 2 BBG): Es muss nach den Umständen des Einzelfalls in besonderem Maße geeignet sein, das Vertrauen in einer für das Amt bedeutsamen Weise zu beeinträchtigen. Die Schwelle ist deutlich höher als innerdienstlich.

### 3. Einleitung des Verfahrens ([§ 17 BDG](https://www.gesetze-im-internet.de/bdg/__17.html))

Liegen zureichende tatsächliche Anhaltspunkte für den Verdacht eines Dienstvergehens vor, **hat** der Dienstvorgesetzte einzuleiten — Legalitätsprinzip, kein Entschließungsermessen. Die Einleitung ist aktenkundig zu machen (§ 17 Abs. 1 S. 3 BDG). Ist nach §§ 14, 15 BDG ohnehin keine Maßnahme möglich, unterbleibt die Einleitung (§ 17 Abs. 2 BDG). Der Beamte kann die Einleitung nach [§ 18 BDG](https://www.gesetze-im-internet.de/bdg/__18.html) selbst beantragen, um sich zu entlasten.

### 4. Unterrichtung, Belehrung und Anhörung ([§ 20 BDG](https://www.gesetze-im-internet.de/bdg/__20.html))

Der Beamte ist unverzüglich zu unterrichten, sobald das ohne Gefährdung der Sachverhaltsaufklärung möglich ist. Ihm ist zu eröffnen, welches Dienstvergehen ihm zur Last gelegt wird. Er ist **gleichzeitig** darauf hinzuweisen, dass es ihm freisteht, sich zu äußern oder nicht zur Sache auszusagen, und dass er sich jederzeit eines Bevollmächtigten oder Beistands bedienen kann.

Fristen des § 20 Abs. 2 BDG: höchstens **ein Monat** für die schriftliche Äußerung, höchstens **zwei Wochen** für die Erklärung, sich mündlich äußern zu wollen. Fristverlängerung ist zu beantragen, bevor die Frist abläuft. Eine unterbliebene oder unvollständige Belehrung ist ein Verfahrensfehler, der im Rechtsbehelf ausdrücklich zu rügen ist.

### 5. Ermittlungen und Beweiserhebung ([§ 24 BDG](https://www.gesetze-im-internet.de/bdg/__24.html))

Der Dienstherr ermittelt den Sachverhalt von Amts wegen, **auch die entlastenden Umstände**. Beweismittel sind Zeugen und Sachverständige ([§ 25 BDG](https://www.gesetze-im-internet.de/bdg/__25.html)), Urkunden ([§ 26 BDG](https://www.gesetze-im-internet.de/bdg/__26.html)) und, unter Richtervorbehalt, Beschlagnahme und Durchsuchung ([§ 27 BDG](https://www.gesetze-im-internet.de/bdg/__27.html)). Beweisanträge des Beamten sind zu bescheiden; ihre Ablehnung ist zu begründen. Vor Abschluss steht die **abschließende Anhörung** nach [§ 30 BDG](https://www.gesetze-im-internet.de/bdg/__30.html) — ohne sie ist die Verfügung angreifbar.

### 6. Verhältnis zum Strafverfahren ([§ 22 BDG](https://www.gesetze-im-internet.de/bdg/__22.html), [§ 23 BDG](https://www.gesetze-im-internet.de/bdg/__23.html))

- **§ 22 Abs. 1 BDG**: Ist wegen desselben Sachverhalts **öffentliche Klage** erhoben, **wird** das Disziplinarverfahren ausgesetzt. Die Aussetzung unterbleibt nur, wenn keine begründeten Zweifel am Sachverhalt bestehen.
- **§ 23 Abs. 1 BDG**: Die **tatsächlichen Feststellungen** eines **rechtskräftigen Urteils** im Straf- oder Bußgeldverfahren sind bindend. Rechtliche Wertungen und Strafzumessungserwägungen sind es **nicht**.
- **§ 23 Abs. 2 BDG**: Feststellungen aus anderen Verfahren binden nicht, können aber ohne nochmalige Prüfung zugrunde gelegt werden. Eine Einstellung nach § 153a StPO und ein Strafbefehl enthalten keine bindenden Feststellungen iSd Abs. 1 — ein häufiger Fehler der Ausgangsbehörde.
- **§ 14 BDG**: Nach einer unanfechtbaren Strafe oder Geldbuße dürfen Verweis, Geldbuße und Kürzung des Ruhegehalts wegen desselben Sachverhalts **nicht** ausgesprochen werden; eine Kürzung der Dienstbezüge nur, wenn sie zusätzlich zur Pflichtenmahnung erforderlich ist.

### 7. Disziplinarmaßnahmen und Bemessung ([§ 5 BDG](https://www.gesetze-im-internet.de/bdg/__5.html), [§ 13 BDG](https://www.gesetze-im-internet.de/bdg/__13.html))

Maßnahmen gegen aktive Beamte (§ 5 Abs. 1 BDG), in aufsteigender Schwere: **Verweis** (§ 6) – **Geldbuße** (§ 7) – **Kürzung der Dienstbezüge** (§ 8) – **Zurückstufung** (§ 9) – **Entfernung aus dem Beamtenverhältnis** (§ 10). Gegen Ruhestandsbeamte: Kürzung des Ruhegehalts (§ 11) und Aberkennung des Ruhegehalts (§ 12). Gegen Beamte auf Probe und auf Widerruf sind nur Verweis und Geldbuße zulässig (§ 5 Abs. 3 BDG).

Die **Schwere-des-Dienstvergehens-Systematik** des § 13 BDG:

1. **Ausgangspunkt** ist die Schwere des Dienstvergehens (§ 13 Abs. 1 S. 1 BDG). Sie bestimmt die Maßnahme dem Grunde nach.
2. Das **Persönlichkeitsbild** ist angemessen zu berücksichtigen (S. 2) — Dienstzeit, bisherige Beurteilungen, Nachtatverhalten, Einsicht.
3. Der Umfang der **Vertrauensbeeinträchtigung** bei Dienstherr und Allgemeinheit ist zu berücksichtigen (S. 3).
4. § 13 Abs. 2 BDG ordnet die Maßnahmen den Schweregraden zu: Verweis bei leichtem, Geldbuße bei leichtem bis mittelschwerem, Kürzung der Dienstbezüge bei mittelschwerem, Zurückstufung bei schwerem Dienstvergehen.
5. Die **Entfernung** setzt den endgültigen Vertrauensverlust voraus. Sie ist keine Ermessens-, sondern eine gebundene Folge, wenn das Vertrauensverhältnis endgültig zerstört ist (BVerwG, Urt. v. 20.10.2005 – 2 C 12.04, BVerwGE 124, 252 = NVwZ 2006, 469).

**Milderungsgründe** sind aktiv vorzutragen: einmaliges Fehlverhalten in unverschuldeter Notlage, überwundene negative Lebensphase, freiwillige Offenbarung vor Entdeckung, tätige Reue und Wiedergutmachung, erhebliche psychische Ausnahmesituation, überlange Verfahrensdauer.

### 8. Maßnahmeverbot wegen Zeitablaufs ([§ 15 BDG](https://www.gesetze-im-internet.de/bdg/__15.html))

Nach Vollendung des Dienstvergehens dürfen nicht mehr ausgesprochen werden:

| Maßnahme | Frist ab Vollendung |
|---|---|
| Verweis | 2 Jahre |
| Geldbuße, Kürzung der Dienstbezüge, Kürzung des Ruhegehalts | 3 Jahre |
| Zurückstufung | 7 Jahre |
| Entfernung, Aberkennung des Ruhegehalts | **kein Maßnahmeverbot** |

Für Dienstvergehen gegen die Pflichten aus § 60 Abs. 1 S. 3 oder Abs. 2 BBG verlängern sich die Fristen nach § 15 Abs. 2 BDG auf 4, 6 und 8 Jahre. Die Fristen werden nach § 15 Abs. 3 BDG unter anderem durch die Einleitung des Verfahrens gehemmt. **Deterministische Berechnung** siehe unten.

### 9. Abschlussentscheidung und Rechtsschutz ([§ 33 BDG](https://www.gesetze-im-internet.de/bdg/__33.html), [§ 52 BDG](https://www.gesetze-im-internet.de/bdg/__52.html))

Das Verfahren endet durch **Einstellungsverfügung** ([§ 32 BDG](https://www.gesetze-im-internet.de/bdg/__32.html)) oder **Disziplinarverfügung** (§ 33 BDG). Die Verfügung ist zu begründen und zuzustellen; die Begründung muss die tatbestandsbegründenden Tatsachen, die sonst bedeutsamen Tatsachen und die Beweismittel enthalten, bei Zurückstufung, Entfernung und Aberkennung zusätzlich Werdegang und Verfahrensgang (§ 33 Abs. 3 BDG). Zuständig ist die Behörde nach [§ 34 BDG](https://www.gesetze-im-internet.de/bdg/__34.html).

Rechtsweg: **Widerspruch** nach [§ 41 BDG](https://www.gesetze-im-internet.de/bdg/__41.html), sodann **Anfechtungsklage** nach § 52 BDG iVm §§ 74, 75, 81 VwGO zur Kammer für Disziplinarsachen beim Verwaltungsgericht. Das Gericht hebt die Verfügung nach [§ 60 Abs. 2 BDG](https://www.gesetze-im-internet.de/bdg/__60.html) auf, soweit sie rechtswidrig ist und den Kläger in seinen Rechten verletzt; es kann sie auch **zu Gunsten** des Klägers ändern. Gegen die **vorläufige Dienstenthebung** nach [§ 38 BDG](https://www.gesetze-im-internet.de/bdg/__38.html) ist der Aussetzungsantrag nach [§ 63 BDG](https://www.gesetze-im-internet.de/bdg/__63.html) statthaft.

## Deterministische Berechnung

Die Fristen des § 15 BDG sind Ereignisfristen nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html). Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — die Vollendung des Dienstvergehens, die Hemmungstatbestände des § 15 Abs. 3 BDG und die Einordnung als Dauer- oder Einzeltat bleiben juristische Eingaben und sind gesondert zu belegen.

```bash
# Verweis: 2 Jahre ab Vollendung des Dienstvergehens am 15.01.2026
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit jahre --land BY

# Geldbuße / Kürzung der Dienstbezüge: 3 Jahre
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 3 --einheit jahre --land BY

# Zurückstufung: 7 Jahre
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 7 --einheit jahre --land BY
```

`--json` liefert die Rechenschritte samt Normzitat. Für Entfernung und Aberkennung des Ruhegehalts ist **keine** Frist zu rechnen — dort gibt es kein Maßnahmeverbot wegen Zeitablaufs.

## Quellen

### Statute

- [§ 47 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__47.html), [§ 33 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__33.html), [§ 34 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__34.html), [§ 35 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__35.html), [§ 37 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__37.html), [§ 40 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__40.html), [§ 42 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__42.html)
- [§ 77 BBG](https://www.gesetze-im-internet.de/bbg_2009/__77.html)
- [§ 5 BDG](https://www.gesetze-im-internet.de/bdg/__5.html), [§ 13 BDG](https://www.gesetze-im-internet.de/bdg/__13.html), [§ 14 BDG](https://www.gesetze-im-internet.de/bdg/__14.html), [§ 15 BDG](https://www.gesetze-im-internet.de/bdg/__15.html), [§ 16 BDG](https://www.gesetze-im-internet.de/bdg/__16.html), [§ 17 BDG](https://www.gesetze-im-internet.de/bdg/__17.html), [§ 20 BDG](https://www.gesetze-im-internet.de/bdg/__20.html), [§ 22 BDG](https://www.gesetze-im-internet.de/bdg/__22.html), [§ 23 BDG](https://www.gesetze-im-internet.de/bdg/__23.html), [§ 24 BDG](https://www.gesetze-im-internet.de/bdg/__24.html), [§ 30 BDG](https://www.gesetze-im-internet.de/bdg/__30.html), [§ 33 BDG](https://www.gesetze-im-internet.de/bdg/__33.html), [§ 34 BDG](https://www.gesetze-im-internet.de/bdg/__34.html), [§ 38 BDG](https://www.gesetze-im-internet.de/bdg/__38.html), [§ 41 BDG](https://www.gesetze-im-internet.de/bdg/__41.html), [§ 52 BDG](https://www.gesetze-im-internet.de/bdg/__52.html), [§ 60 BDG](https://www.gesetze-im-internet.de/bdg/__60.html)
- Landesdisziplinargesetze der Länder (jeweils konkret zu zitieren) `[unverifiziert - prüfen]`
- [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html)

### Kommentare

- Gansen, Disziplinarrecht in Bund und Ländern, Loseblatt, § 13 BDG Rn. 1 ff.
- Urban, in: Urban/Wittkowski, BDG, § 13 Rn. 1 ff., § 15 Rn. 1 ff.
- Hummel/Köhler/Mayer/Baunack, BDG und materielles Disziplinarrecht, § 20 Rn. 1 ff.
- von Roetteken, in: von Roetteken/Rothländer, BeamtStG, § 47 Rn. 1 ff.
- Schnellenbach/Bodanowitz, Beamtenrecht in der Praxis, Kap. Disziplinarrecht.

### Rechtsprechung

1. BVerwG, Urt. v. 20.10.2005 – 2 C 12.04, BVerwGE 124, 252 = NVwZ 2006, 469 (Bemessung nach § 13 BDG, Vertrauensverlust) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2005-10-20&Aktenzeichen=2%20C%2012.04)), Kernaussage im Volltext gegenzulesen
2. BVerwG, Urt. v. 05.06.2014 – 2 C 22.13, BVerwGE 150, 1 = NVwZ 2014, 1319 (Statusrecht, amtsärztliche Feststellungen) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2014-06-05&Aktenzeichen=2%20C%2022.13))
3. Zur Kasuistik der Milderungsgründe und zur Bemessung bei Zugriffsdelikten ist die einschlägige Senatsrechtsprechung im Einzelfall zu recherchieren `[unverifiziert - prüfen]`

## Ausgabeformat

```
DISZIPLINARVERFAHREN — <Mandat> — <Datum>

I.   Anwendbares Recht
     Dienstherr:              <Bund / Land <X> / Kommune>
     Materielles Recht:       <§ 77 BBG | § 47 BeamtStG>
     Verfahrensrecht:         <BDG | LDG <X>>
     Statusamt:               <Lebenszeit / Probe / Widerruf / Ruhestand>

II.  Vorwurf und Pflichtnorm
     Sachverhalt:             <…>
     Verletzte Pflicht:       <§ N BeamtStG / BBG>
     Innerdienstlich:         [ja / nein — Erheblichkeitsschwelle geprüft]
     Vorwerfbarkeit:          [Vorsatz / Fahrlässigkeit / offen]

III. Verfahrensrechte
     Einleitung § 17:         <Datum / aktenkundig?>
     Unterrichtung § 20:      <Datum / Belehrung vollständig?>
     Äußerungsfrist:          läuft bis <Datum>
     Abschließende Anhörung:  [erfolgt / ausstehend]
     Verfahrensrügen:         <…>

IV.  Sperren
     § 14 BDG (Straf-/Bußgeld): [einschlägig / nicht einschlägig]
     § 15 BDG (Zeitablauf):     Verweis bis <Datum> | Geldbuße bis <Datum> |
                                Zurückstufung bis <Datum> | Entfernung: keine Frist
     § 22 BDG (Aussetzung):     [geboten / nicht geboten]
     § 23 BDG (Bindung):        [rechtskräftiges Urteil / kein bindender Titel]

V.   Maßnahmenprognose § 13 BDG
     Schwere:                 <…>
     Persönlichkeitsbild:     <…>
     Vertrauensbeeinträchtigung: <…>
     Milderungsgründe:        <…>
     Erwartete Maßnahme:      <Verweis / Geldbuße / Kürzung / Zurückstufung / Entfernung>

VI.  Rechtsschutz
     Widerspruch § 41 BDG:    Frist bis <Datum>
     Klage § 52 BDG:          VG <Ort>, Kammer für Disziplinarsachen
     § 63 BDG:                [Aussetzungsantrag erforderlich / nein]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Stellungnahme nach § 20 BDG (Gerüst)

```
An die <Dienstbehörde>
Disziplinarverfahren gegen <Mandant>, Az. <…>

Namens und in Vollmacht nehme ich zu dem mit Verfügung vom <Datum>
eröffneten Vorwurf wie folgt Stellung:

I.   Verfahrensrügen
     1. Die Belehrung nach § 20 Abs. 1 S. 3 BDG ist unvollständig, weil <…>.
     2. Der Beweisantrag vom <Datum> ist bislang nicht beschieden (§ 24 BDG).
II.  Zum Sachverhalt
     <tatsachenbezogen, ohne rechtliche Belehrung des Dienstherrn>
III. Rechtliche Bewertung
     1. Eine Verletzung der Pflicht aus § <N> BeamtStG liegt nicht vor, weil <…>.
     2. Jedenfalls fehlt es an der Vorwerfbarkeit, weil <…>.
     3. Vorsorglich: Eine Maßnahme ist nach § 15 Abs. 1 Nr. <N> BDG
        seit dem <Datum> ausgeschlossen.
IV.  Bemessung (hilfsweise)
     Milderungsgründe: <…>. Die Schwere des Dienstvergehens rechtfertigt
     allenfalls einen Verweis nach §§ 5 Abs. 1 Nr. 1, 13 Abs. 2 Nr. 1 BDG.
V.   Anträge
     1. Das Disziplinarverfahren nach § 32 BDG einzustellen.
     2. Hilfsweise: das Verfahren nach § 22 BDG bis zum rechtskräftigen
        Abschluss des Strafverfahrens auszusetzen.
```

## Risiken / typische Fehler

- **Bundes- und Landesrecht vermengt.** Das BDG gilt nur für Bundesbeamte. Für Landesbeamte gelten BeamtStG und das jeweilige Landesdisziplinargesetz; die Verfahrensregeln weichen ab, insbesondere beim Fortbestand der Disziplinarklage.
- **Disziplinarklage für einen Bundesbeamten entworfen.** Das BDG sieht sie nicht mehr vor; Maßnahmen ergehen durch Disziplinarverfügung nach § 33 BDG.
- **§ 15 BDG nicht gerechnet.** Verweis, Geldbuße, Kürzung und Zurückstufung sind nach 2, 3 bzw. 7 Jahren ausgeschlossen; die Frist wird regelmäßig übersehen, weil sie an die **Vollendung** des Dienstvergehens anknüpft, nicht an die Kenntnis des Dienstherrn.
- **Bindungswirkung überdehnt.** § 23 Abs. 1 BDG bindet nur an tatsächliche Feststellungen eines **rechtskräftigen Urteils**. Strafbefehl und Einstellung nach § 153a StPO tragen keine Bindung.
- **Generalklausel statt Pflichtnorm.** Ein Vorwurf ohne konkrete Pflichtnorm ist im Rechtsbehelf angreifbar.
- **Außerdienstliches Verhalten ohne Erheblichkeitsprüfung** als Dienstvergehen behandelt.
- **Milderungsgründe nicht vorgetragen.** Sie sind Vortragslast des Beamten; § 13 BDG verlangt ihre Berücksichtigung, aber der Dienstherr ermittelt sie nicht von selbst vollständig.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
