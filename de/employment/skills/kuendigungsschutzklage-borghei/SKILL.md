---
name: kuendigungsschutzklage-borghei
title: /arbeitsrecht:kuendigungsschutzklage
description: Erhebung und Führung der Kündigungsschutzklage – 3-Wochen-Frist § 4 KSchG ab Zugang der schriftlichen Kündigung, Präklusion § 7 KSchG, nachträgliche Zulassung § 5 KSchG, verlängerte Anrufungsfrist § 6 KSchG, allgemeiner Feststellungsantrag, Weiterbeschäftigungsantrag (§ 102 Abs. 5 BetrVG und allgemeiner Weiterbeschäftigungsanspruch), Auflösungsantrag §§ 9, 10 KSchG, Güte- und Kammertermin § 54 ArbGG, Kostentragung § 12a ArbGG. Use when ein Arbeitnehmer eine Kündigung erhalten hat und Klage zu erheben ist, oder wenn ein Arbeitgeber die Erfolgsaussichten einer bereits erhobenen Klage bewertet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/kuendigungsschutzklage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:kuendigungsschutzklage

## Zweck

Die Kündigungsschutzklage ist ein Fristenmandat, kein Argumentationsmandat. Wer die drei Wochen des [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html) versäumt, verliert **jeden** Unwirksamkeitsgrund — auch die fehlende BR-Anhörung, auch die Formnichtigkeit nach § 623 BGB (§ 7 KSchG). Dieser Skill sichert zuerst die Frist, formuliert dann die Anträge und bewertet erst zuletzt die materielle Erfolgsaussicht.

## Eingaben

- **Zugangsdatum** der schriftlichen Kündigung (Datum, Zugangsart: Übergabe / Einwurf-Einschreiben / Bote) — der rechtlich entscheidende Wert
- Kündigungsart: ordentlich / außerordentlich / Änderungskündigung (§ 2 KSchG)
- Behördliche Zustimmung erforderlich? (§ 168 SGB IX, § 17 MuSchG, § 18 BEEG) — dann Fristbeginn erst ab Bekanntgabe der Behördenentscheidung (§ 4 S. 4 KSchG)
- Betriebsgröße (§ 23 KSchG), Beschäftigungsdauer (§ 1 Abs. 1 KSchG), BR vorhanden und Widerspruch erklärt?
- Bruttomonatsentgelt (für Streitwert und Abfindungsprognose)
- Mandantenziel: **Bestandsschutz** oder **Abfindung** — steuert Antragswahl und Vergleichsstrategie

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert die Fristnormen mit URL, die Rspr. zum Zugangsbegriff und zur nachträglichen Zulassung, Kommentarstellen zu §§ 4–7 KSchG.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) formuliert Klageschrift, Anträge und Begründung im Urteilsstil.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft ausschließlich zuerst die Frist, dann Antragsfassung, Streitwert, Quellenmarker.

## Ablauf

### 1. Fristbeginn: Zugang bestimmen ([§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html))

Die Frist beginnt mit **Zugang der schriftlichen Kündigung**, nicht mit Kenntnisnahme und nicht mit dem Datum des Schreibens. Maßgeblich ist der Zeitpunkt, in dem die Erklärung so in den Machtbereich des Arbeitnehmers gelangt ist, dass unter gewöhnlichen Umständen mit Kenntnisnahme zu rechnen war (st. Rspr. des BAG zu § 130 BGB `[unverifiziert – prüfen]`).

Praxisfälle:

| Zugangsart | Zugang |
|---|---|
| Persönliche Übergabe | Am Tag der Übergabe |
| Einwurf in den Hausbriefkasten | Am Einwurftag, wenn vor der ortsüblichen Leerungszeit; sonst Folgetag |
| Einwurf-Einschreiben | Mit Einlegen in den Briefkasten durch den Zusteller |
| Übergabe-Einschreiben (Benachrichtigungszettel) | **Nicht** mit dem Zettel — erst mit Abholung; Zugangsvereitelung nur bei Treuwidrigkeit |
| Urlaubsabwesenheit | Ändert am Zugang nichts — begründet aber ggf. § 5 KSchG |

**Behördliche Zustimmung:** Bedarf die Kündigung der Zustimmung einer Behörde, läuft die Frist erst ab Bekanntgabe der Behördenentscheidung an den Arbeitnehmer (§ 4 S. 4 KSchG). Vorsorgliche Klage dennoch empfohlen.

### 2. Präklusion ([§ 7 KSchG](https://www.gesetze-im-internet.de/kschg/__7.html))

Wird die Rechtsunwirksamkeit nicht rechtzeitig geltend gemacht, gilt die Kündigung **als von Anfang an rechtswirksam**. Die Präklusion erfasst nach h.M. alle Unwirksamkeitsgründe — auch Verstöße gegen § 102 BetrVG, § 623 BGB, §§ 17, 18 KSchG und das AGG.

**Ausnahmen von der Fristbindung:** Die Frist gilt nur für den Streit über die *Beendigung durch diese Kündigung*. Nicht erfasst sind etwa Zahlungsansprüche, der Zeugnisanspruch oder der Streit über die **Kündigungsfrist** — insoweit genügt eine Klage nach Fristablauf, allerdings unter Beachtung tariflicher Ausschlussfristen.

### 3. Verlängerte Anrufungsfrist ([§ 6 KSchG](https://www.gesetze-im-internet.de/kschg/__6.html))

Ist die Klage fristgerecht erhoben, können **weitere** Unwirksamkeitsgründe bis zum Schluss der mündlichen Verhandlung erster Instanz nachgeschoben werden. Das Arbeitsgericht soll darauf hinweisen. Praktische Folge: eine schlanke, aber fristwahrende Klageschrift ist besser als eine perfekte verspätete.

### 4. Nachträgliche Zulassung ([§ 5 KSchG](https://www.gesetze-im-internet.de/kschg/__5.html))

Voraussetzungen kumulativ:

1. Der Arbeitnehmer war **trotz Anwendung aller zumutbaren Sorgfalt** an der rechtzeitigen Klageerhebung gehindert (Maßstab streng; Anwaltsverschulden wird zugerechnet).
2. Der Antrag ist **mit der Klageerhebung zu verbinden** (§ 5 Abs. 2 S. 1 KSchG) und enthält die begründenden Tatsachen samt Glaubhaftmachungsmitteln.
3. Antragsfrist: **zwei Wochen nach Behebung des Hindernisses**, absolute Grenze **sechs Monate** ab Ende der versäumten Frist (§ 5 Abs. 3 KSchG).

Sonderfall: Kenntnis von der Schwangerschaft erst nach Fristablauf, ohne dass die Arbeitnehmerin dies zu vertreten hat (§ 5 Abs. 1 S. 2 KSchG).

### 5. Klageanträge formulieren ([§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html), [§ 46 ArbGG](https://www.gesetze-im-internet.de/arbgg/__46.html))

**Formulierungshilfe — Standardanträge:**

```
1. Es wird festgestellt, dass das zwischen den Parteien bestehende
   Arbeitsverhältnis durch die Kündigung der Beklagten vom
   <Datum>, zugegangen am <Datum>, nicht aufgelöst worden ist.

2. Es wird festgestellt, dass das Arbeitsverhältnis auch nicht durch
   andere Beendigungstatbestände endet, sondern über den <Datum>
   hinaus zu unveränderten Bedingungen fortbesteht.
   [allgemeiner Feststellungsantrag — fängt Nachkündigungen ab]

3. Für den Fall des Obsiegens mit dem Antrag zu 1.: Die Beklagte wird
   verurteilt, den Kläger zu unveränderten arbeitsvertraglichen
   Bedingungen als <Funktion> bis zum rechtskräftigen Abschluss des
   Kündigungsschutzverfahrens weiterzubeschäftigen.

4. Die Beklagte trägt die Kosten des Rechtsstreits.
```

**Antrag zu 2.** ist der sog. Schleppnetz- oder allgemeine Feststellungsantrag (§ 256 ZPO). Er sollte gestellt werden, wenn mit Folgekündigungen zu rechnen ist; das Feststellungsinteresse ist darzulegen.

**Antrag zu 3.** ist der Weiterbeschäftigungsantrag. Zwei Grundlagen sind zu unterscheiden:

- **[§ 102 Abs. 5 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html):** gesetzlicher Anspruch, wenn der Betriebsrat frist- und ordnungsgemäß widersprochen hat und Kündigungsschutzklage erhoben ist. Kein Abwägungserfordernis; Entbindung nur per einstweiliger Verfügung (§ 102 Abs. 5 S. 2 BetrVG).
- **Allgemeiner Weiterbeschäftigungsanspruch:** von der Rspr. aus §§ 611a, 613, 242 BGB i.V.m. Art. 1, 2 GG entwickelt; greift regelmäßig ab erstinstanzlichem Obsiegen (st. Rspr. des BAG, Großer Senat, zum allgemeinen Weiterbeschäftigungsanspruch `[unverifiziert – prüfen]`).

### 6. Güte- und Kammertermin ([§ 54 ArbGG](https://www.gesetze-im-internet.de/arbgg/__54.html))

Die mündliche Verhandlung **beginnt** mit der Güteverhandlung vor dem Vorsitzenden allein (§ 54 Abs. 1 S. 1 ArbGG). Sie findet in Kündigungssachen typischerweise 2–4 Wochen nach Klageeingang statt; über 70 % der Kündigungsschutzverfahren enden hier durch Vergleich.

- Bleibt die Güteverhandlung erfolglos, schließt sich die streitige Verhandlung unmittelbar an oder es wird Kammertermin bestimmt (§ 54 Abs. 4 ArbGG).
- Erscheinen **beide** Parteien nicht, ordnet das Gericht das Ruhen an; der Antrag auf Kammertermin ist nur binnen sechs Monaten zulässig (§ 54 Abs. 5 ArbGG).
- **Kostenfalle:** In erster Instanz besteht **kein Anspruch auf Erstattung der Anwaltskosten der Gegenseite** ([§ 12a Abs. 1 ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html)) — auch bei vollem Obsiegen. Darauf ist der Mandant vor Klageerhebung hinzuweisen.

### 7. Auflösungsantrag ([§ 9 KSchG](https://www.gesetze-im-internet.de/kschg/__9.html), [§ 10 KSchG](https://www.gesetze-im-internet.de/kschg/__10.html))

Ist die Kündigung sozialwidrig, aber die Fortsetzung unzumutbar, kann das Gericht auf Antrag das Arbeitsverhältnis auflösen und eine Abfindung festsetzen. Höchstbeträge § 10 KSchG: 12 Monatsverdienste; 15 bei ≥ 50 Jahren und 15 Jahren Betriebszugehörigkeit; 18 bei ≥ 55 Jahren und 20 Jahren. Der **Arbeitgeber** kann den Antrag nur stellen, wenn Gründe vorliegen, die eine gedeihliche Zusammenarbeit ausschließen — der Maßstab ist streng, da § 9 KSchG kein Abfindungskaufrecht ist.

### 8. Streitwert und Abfindungsprognose

Streitwert der Bestandsschutzklage: **Vierteljahresverdienst** als Regelobergrenze (§ 42 Abs. 2 GKG). Faustformel für Vergleiche: 0,5 Bruttomonatsgehälter je Beschäftigungsjahr — kein Rechtsanspruch, sondern Verhandlungsanker; Abweichungen nach Prozessrisiko, Alter, Arbeitsmarktlage.

## Deterministische Berechnung

Die 3-Wochen-Frist des § 4 KSchG ist eine Ereignisfrist nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html); ihr Ende verschiebt sich nach [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) auf den nächsten Werktag, wenn es auf Samstag, Sonntag oder einen am Gerichtsort geltenden Feiertag fällt ([§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html)). Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — der Zugangszeitpunkt und die Frage, welches Bundesland für die Feiertage maßgeblich ist, bleiben juristische Eingaben.

```bash
# Kündigung zugegangen am 15.01.2026, Arbeitsgericht in Bayern
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 3 --einheit wochen --land BY

# Ergebnis (gekürzt):
#   Fristbeginn: 16.01.2026   (§ 187 Abs. 1 BGB — Zugangstag zählt nicht)
#   Fristende:   05.02.2026   (§ 188 Abs. 2 BGB)

# Antragsfrist § 5 Abs. 3 S. 1 KSchG: 2 Wochen ab Behebung des Hindernisses
python -m scripts.legal_calc.cli frist --ereignis 20.02.2026 --menge 2 --einheit wochen --land NW

# Absolute Grenze § 5 Abs. 3 S. 2 KSchG: 6 Monate ab Ende der versäumten Frist
python -m scripts.legal_calc.cli frist --ereignis 05.02.2026 --menge 6 --einheit monate --land NW
```

`--json` liefert die Rechenschritte maschinenlesbar samt Normzitat. **Nie** das Fristende ohne Gegenprüfung des Zugangsnachweises in den Kalender eintragen; Wiedervorlage stets mit mindestens drei Werktagen Puffer.

## Quellen

### Statute

- [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html), [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html), [§ 5 KSchG](https://www.gesetze-im-internet.de/kschg/__5.html), [§ 6 KSchG](https://www.gesetze-im-internet.de/kschg/__6.html), [§ 7 KSchG](https://www.gesetze-im-internet.de/kschg/__7.html), [§ 9 KSchG](https://www.gesetze-im-internet.de/kschg/__9.html), [§ 10 KSchG](https://www.gesetze-im-internet.de/kschg/__10.html), [§ 13 KSchG](https://www.gesetze-im-internet.de/kschg/__13.html), [§ 23 KSchG](https://www.gesetze-im-internet.de/kschg/__23.html)
- [§ 46 ArbGG](https://www.gesetze-im-internet.de/arbgg/__46.html), [§ 54 ArbGG](https://www.gesetze-im-internet.de/arbgg/__54.html), [§ 12a ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html)
- [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html)
- [§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html), [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html)
- [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html), [§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html)

### Kommentare

- Kiel, in: ErfK, 24. Aufl. 2024, § 4 KSchG Rn. 1 ff. (Klagefrist und Zugang)
- Hergenröder, in: MüKoBGB, 9. Aufl. 2023, § 4 KSchG Rn. 1 ff.
- Ascheid / Hesse, in: APS, 6. Aufl. 2021, § 5 KSchG Rn. 20 ff. (nachträgliche Zulassung)
- Spilger, in: KR, 13. Aufl. 2022, § 9 KSchG Rn. 1 ff. (Auflösungsantrag)

### Rechtsprechung

- st. Rspr. des BAG zu § 130 BGB (Zugang bei Einwurf in den Hausbriefkasten, ortsübliche Leerungszeit) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 7 KSchG (Präklusion erfasst alle Unwirksamkeitsgründe) `[unverifiziert – prüfen]`
- BAG (Großer Senat) zum allgemeinen Weiterbeschäftigungsanspruch nach erstinstanzlichem Obsiegen `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 9 KSchG (strenger Maßstab für den Auflösungsantrag des Arbeitgebers) `[unverifiziert – prüfen]`

> Aktenzeichen werden hier bewusst nicht genannt. Vor Verwendung in einem Schriftsatz sind die Fundstellen in juris, Beck-Online oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
KÜNDIGUNGSSCHUTZKLAGE — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

⚠️ FRISTBLOCK (zuerst lesen)
    Zugang:              <Datum, Zugangsart, Nachweis>
    Fristbeginn:         <Datum>   § 187 Abs. 1 BGB
    Fristende § 4 KSchG: <Datum>   [berechnet mit scripts/legal_calc]
    Wiedervorlage:       <Fristende minus 3 Werktage>

I.    Zugang und Fristwahrung          [🟢 gewahrt / 🔴 abgelaufen]
II.   Präklusionsprüfung § 7 KSchG     [N/A / 🔴 eingetreten]
III.  Nachträgliche Zulassung § 5      [N/A / beantragt — Hindernis: <…>]
IV.   Anträge
      1. Feststellungsantrag § 4 KSchG
      2. Allgemeiner Feststellungsantrag  [gestellt / nicht gestellt]
      3. Weiterbeschäftigung             [§ 102 V BetrVG / allgemein / keiner]
      4. Auflösungsantrag §§ 9, 10       [N/A / gestellt]
V.    Materielle Erfolgsaussicht        [🟢 / 🟡 / 🔴]
      Angriffspunkte: <…>
VI.   Streitwert                        <Vierteljahresverdienst>
VII.  Kostenhinweis § 12a ArbGG         erteilt am <Datum>
VIII. Vergleichskorridor                <Untergrenze> – <Obergrenze>

Offene Tatsachenfragen: <…>
Offene Verifizierungen: <BAG-Fundstellen in juris ermitteln>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Fristbeginn falsch angesetzt** — Datum des Kündigungsschreibens statt Zugang. Häufigster Haftungsfall des Mandats.
- **Übergabe-Einschreiben mit Benachrichtigungszettel** als Zugang behandelt — Zugang tritt erst mit Abholung ein; umgekehrt darf sich der Arbeitnehmer nicht auf treuwidrige Zugangsvereitelung stützen.
- **Präklusion nach § 7 KSchG unterschätzt** — auch die evident fehlende BR-Anhörung heilt durch Fristablauf.
- **Kein allgemeiner Feststellungsantrag** gestellt, obwohl eine Nachkündigung im Raum steht — die zweite Kündigung läuft dann in eine eigene 3-Wochen-Frist.
- **Weiterbeschäftigungsantrag ohne Grundlage** — § 102 Abs. 5 BetrVG setzt einen **frist- und ordnungsgemäßen Widerspruch** des Betriebsrats voraus, nicht bloß dessen Bedenken.
- **§ 12a ArbGG nicht erklärt** — Mandant erwartet Kostenerstattung in erster Instanz und ist bei Obsiegen enttäuscht.
- **Auflösungsantrag des Arbeitgebers als Abfindungsweg** missverstanden — der Maßstab des § 9 KSchG ist streng; der Antrag kann das Verfahren verteuern, ohne zu wirken.
- **Behördliche Zustimmung übersehen** — bei § 168 SGB IX / § 17 MuSchG beginnt die Frist erst mit Bekanntgabe der Behördenentscheidung (§ 4 S. 4 KSchG); vorsorgliche Klage bleibt dennoch die sichere Variante.
