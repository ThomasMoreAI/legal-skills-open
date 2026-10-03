---
name: recht-sozial-beschwerde-momarcode1
title: /recht sozial-beschwerde — Sozialrechtliche Beschwerde / Klage
description: Austrian social security appeals — challenging Bescheide from ÖGK/PVA/AMS/SVS, Klage to Arbeits- und Sozialgericht (ASG), pension disputes, Pflegestufe appeals, and AMS sanctions (Sperren). Kostenfreiheit in Sozialrechtssachen.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-sozial-beschwerde
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: social-security
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht sozial-beschwerde — Sozialrechtliche Beschwerde / Klage

When the user has received an unfavorable decision (Bescheid) from a social security institution (ÖGK, PVA, SVS, BVAEB, AMS) or wants to challenge a benefit denial, follow these steps.

---

## Step 1: Read the Bescheid / Situation

Gather all relevant information:

1. **Which institution issued the decision?** — ÖGK, PVA, SVS, BVAEB, AMS, Pflegegeldstelle?
2. **What was decided?** — Benefit denied, reduced, withdrawn, Sperre imposed?
3. **When was the Bescheid delivered (zugestellt)?** — CRITICAL for deadline calculation
4. **What is the Rechtsmittelbelehrung?** — What does the Bescheid say about appeal options and deadlines?
5. **What are the grounds for disagreement?** — Why does the user think the decision is wrong?
6. **What evidence does the user have?** — Medical reports, employment records, income documentation, witnesses?

If the Bescheid is available, read it carefully. Focus on:
- Spruch (operative part / decision)
- Begründung (reasoning)
- Rechtsmittelbelehrung (appeal instructions)

If the Bescheid is not available, ask:
> "Haben Sie den Bescheid zur Hand? Ich brauche vor allem den Spruch, die Begründung und die Rechtsmittelbelehrung. Wann wurde er Ihnen zugestellt?"

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz (OGH Sozialrechtssachen)
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH decisions in Sozialrechtssachen (10 ObS ...).

---

## Step 3: Classify — Verwaltungssache or Leistungssache?

This is the **most critical distinction** in Austrian social security appeals. The wrong forum = appeal rejected.

### Leistungssachen (→ Arbeits- und Sozialgericht)

Disputes about **benefits and entitlements** go to the ordentliche Gerichte (ASG):

| Streitgegenstand | Rechtsgrundlage | Zuständig |
|-----------------|-----------------|-----------|
| Pension (Gewährung, Höhe, Entziehung) | §65 Abs 1 Z 1 ASGG | ASG |
| Pflegegeld (Einstufung, Höhe) | §65 Abs 1 Z 2 ASGG | ASG |
| Versehrtenrente (UV-Leistung) | §65 Abs 1 Z 1 ASGG | ASG |
| Krankengeld | §65 Abs 1 Z 1 ASGG | ASG |
| Rehabilitationsgeld | §65 Abs 1 Z 1 ASGG | ASG |
| Wochengeld | §65 Abs 1 Z 1 ASGG | ASG |
| Kinderbetreuungsgeld | §65 Abs 1 Z 8 ASGG | ASG |
| Arbeitsunfall-Anerkennung | §65 Abs 1 Z 1 ASGG | ASG |
| Feststellung von Versicherungszeiten | §65 Abs 1 Z 1 ASGG | ASG |

**Verfahren:** Klage (nicht Beschwerde!) gegen den Sozialversicherungsträger als Beklagten. Klagefrist: Grundsätzlich innerhalb der im Bescheid genannten Frist (oft 4 Wochen). Keine Klagsgebühr (§80 ASGG).

### Verwaltungssachen (→ Bundesverwaltungsgericht)

Disputes about **administrative decisions** go to the BVwG:

| Streitgegenstand | Rechtsgrundlage | Zuständig |
|-----------------|-----------------|-----------|
| AMS-Bescheide (Sperre, Arbeitslosengeld-Bezugsdauer) | §56 AlVG | BVwG |
| Pflichtversicherung ja/nein | §410 ASVG | BVwG |
| Beitragsrecht (Nachforderung, Beitragsgrundlage) | §410 ASVG | BVwG |
| Mindestsicherung / Sozialhilfe | Landes-Sozialhilfegesetz | LVwG |

**Verfahren:** Beschwerde gemäß §7 VwGVG. Beschwerdefrist: 4 Wochen ab Zustellung (§7 Abs 4 VwGVG).

### Sonderfälle

- **AMS-Sperre:** Verwaltungssache → BVwG. ABER: Wenn es um die Höhe des Arbeitslosengeldes als solche geht → auch BVwG (§56 AlVG).
- **Feststellung der Pflichtversicherung:** Verwaltungssache → BVwG. ABER: Leistungsansprüche, die davon abhängen → ASG (Vorfragenbeurteilung).
- **Mindestsicherung:** Landesverwaltungsgericht (LVwG), nicht BVwG.

---

## Step 4: Check Deadlines

### ⚠️ FRISTEN SIND KRITISCH — Versäumte Fristen bedeuten Verlust des Rechtsmittels!

| Rechtsmittel | Frist | Ab wann? | Rechtsgrundlage |
|-------------|-------|----------|-----------------|
| Klage ans ASG (Sozialrechtssache) | Im Bescheid genannt (meist 4 Wochen) | Ab Zustellung des Bescheids | §67 ASGG |
| Beschwerde an BVwG (AMS etc.) | 4 Wochen | Ab Zustellung des Bescheids | §7 Abs 4 VwGVG |
| Beschwerde an LVwG (Mindestsicherung) | 4 Wochen | Ab Zustellung des Bescheids | §7 Abs 4 VwGVG |
| Wiedereinsetzung in den vorigen Stand | 2 Wochen ab Wegfall des Hindernisses | §71 AVG / §146 ZPO | §71 AVG (Verwaltung) / §146 ZPO (Gericht) |

Berechnung:
- Tag der Zustellung = Tag 0
- 4 Wochen = 28 Tage (Kalendertage, nicht Werktage)
- Fällt der letzte Tag auf Sa/So/Feiertag → Frist endet am nächsten Werktag (§33 Abs 2 AVG / §126 Abs 2 ZPO)
- Gerichtsferien (15.7.–17.8., 24.12.–6.1.): In Sozialrechtssachen am ASG hemmen die Gerichtsferien die Frist NICHT (§§23 Abs 1, 92 Abs 1 ASGG)

**Prüfen und klar angeben:**
- Zustelldatum: [Datum]
- Fristende: [Datum]
- Verbleibende Tage: [n] Tage
- Status: 🟢 Ausreichend Zeit / 🟡 Eilig (< 7 Tage) / 🔴 Frist abgelaufen

Wenn die Frist abgelaufen ist:
> "Die Frist ist leider abgelaufen. Prüfen Sie, ob ein Wiedereinsetzungsantrag (§71 AVG / §146 ZPO) möglich ist — dafür brauchen Sie einen unvorhergesehenen und unabwendbaren Hinderungsgrund."

---

## Step 5: Identify Appeal Grounds

For each type of dispute, check the typical Beschwerdegründe:

### Pensionsstreitigkeiten (Klage ans ASG)
- Fehlende Versicherungsmonate in der Berechnung (z.B. Kindererziehungszeiten §227a ASVG, Präsenzdienst §227 ASVG)
- Falsche Kontoerstgutschrift (§15 APG) — Zeiten vor 2005 falsch bewertet
- Abschläge falsch berechnet
- Invalidität/Berufsunfähigkeit zu Unrecht verneint → Gutachten unvollständig oder widersprüchlich
- Verweisungsfeld zu weit gefasst (§255 ASVG)
- Stichtag falsch festgesetzt

### Pflegestufe-Beschwerde (Klage ans ASG)
- Pflegebedarf wurde im Gutachten unterschätzt
- Verrichtungen wurden nicht berücksichtigt oder mit zu wenig Zeit bewertet
- Erschwerniszuschlag (§4 Abs 4 EinstV) nicht berücksichtigt
- Zustand hat sich seit dem Gutachten verschlechtert → neues Gutachten erforderlich
- Sachverständigengutachten ist mangelhaft (fehlende Untersuchung, Widersprüche)

### AMS-Sperre anfechten (Beschwerde an BVwG)
- Angebotene Stelle war nicht zumutbar (§9 AlVG):
  - Entgelt liegt unter dem zustehenden Niveau (Berufsschutz in den ersten 100 Tagen: §9 Abs 2 AlVG)
  - Gesundheitliche Gründe gegen die Stelle
  - Betreuungspflichten machen Arbeitszeit/Arbeitsort unzumutbar
  - Wegzeit über 1,5 Stunden einfach (§9 Abs 2 AlVG: Wegzeit muss zumutbar sein, OGH-Judikatur: 1,5h als Richtwert)
- Eigenkündigung lag ein wichtiger Grund vor (§11 AlVG):
  - Mobbing, sexuelle Belästigung, Gesundheitsgefährdung
  - Entgeltvorenthaltung durch Arbeitgeber
  - Umzug zum Ehegatten/Lebenspartner
- Nachsichtsgründe: Berücksichtigungswürdige Gründe nach §10 Abs 3 AlVG
- Verfahrensfehler: AMS hat nicht ordnungsgemäß belehrt, Parteiengehör verletzt

### Unfallversicherung (Klage ans ASG)
- Unfall wurde nicht als Arbeitsunfall anerkannt → Kausalität bestreiten
- Wegunfall: Umweg war sachlich begründet (z.B. Kinderbetreuung, §175 Abs 2 Z 1 ASVG)
- Berufskrankheit nicht anerkannt → medizinischer Kausalzusammenhang
- MdE (Minderung der Erwerbsfähigkeit) zu niedrig eingestuft → Gutachten anfechten
- Versehrtenrente zu gering berechnet

---

## Step 6: Draft the Beschwerde / Klage

### A: Klage ans Arbeits- und Sozialgericht (Leistungssache)

```
An das Arbeits- und Sozialgericht [Ort]

Kläger/in:   [Vollständiger Name]
             [Straße, PLZ Ort]
             geboren am [Datum]
             SVNR: [Sozialversicherungsnummer]

Beklagte:    [Pensionsversicherungsanstalt / Österreichische Gesundheitskasse /
              Sozialversicherungsanstalt der Selbständigen / BVAEB /
              Allgemeine Unfallversicherungsanstalt]
             [Adresse des SVT]

wegen:       [z.B. "Invaliditätspension" / "Pflegegeld der Stufe 4" /
              "Anerkennung als Arbeitsunfall" / "Versehrtenrente"]

                         K L A G E
              in Sozialrechtssachen (§65 ASGG)

I. BESCHEID

1.  Mit Bescheid vom [Datum], GZ [Geschäftszahl], hat die beklagte Partei
    [Inhalt des Bescheids — z.B. "den Antrag des Klägers auf Gewährung
    einer Invaliditätspension abgewiesen" / "Pflegegeld der Stufe 2
    zuerkannt"].

    Beweis: Bescheid vom [Datum] (Beilage ./A)

2.  Dieser Bescheid wurde dem Kläger am [Zustelldatum] zugestellt.
    Die Klagefrist von [x] Wochen ist daher gewahrt.

II. KLAGEGRÜNDE

3.  [Erster Klagegrund — z.B. "Der dem Bescheid zugrunde liegende
    ärztliche Sachverständigengutachten vom [Datum] ist mangelhaft.
    Der Sachverständige hat [konkreter Mangel] nicht berücksichtigt."]

    Beweis: [z.B. Befund von Dr. [Name] vom [Datum] (Beilage ./B);
            PV des Klägers]

4.  [Zweiter Klagegrund]

    Beweis: [Beweisanbot]

[Weitere Klagegründe mit Beweisanboten]

III. KLAGEBEGEHREN

Der Kläger stellt daher den

                         A N T R A G,

das Gericht möge

1.  [z.B. "die beklagte Partei schuldig erkennen, dem Kläger ab [Stichtag]
    eine Invaliditätspension im gesetzlichen Ausmaß zu gewähren"]

    [ODER: "die beklagte Partei schuldig erkennen, dem Kläger Pflegegeld
    der Stufe [x] ab [Datum] zu gewähren"]

    [ODER: "feststellen, dass das Ereignis vom [Datum] als Arbeitsunfall
    anerkannt wird und die beklagte Partei schuldig erkennen, dem Kläger
    eine Versehrtenrente im gesetzlichen Ausmaß zu gewähren"]

[Ort], am [Datum]

                         ____________________
                         [Unterschrift des Klägers]


BEILAGENVERZEICHNIS:
./A  Bescheid der beklagten Partei vom [Datum]
./B  [Befund / Gutachten / Bestätigung]
./C  [Weiteres Beweismittel]
```

### B: Beschwerde an das BVwG (Verwaltungssache, z.B. AMS-Sperre)

```
An das Bundesverwaltungsgericht
einzubringen über:
[AMS — Arbeitsmarktservice / Regionale Geschäftsstelle [Ort]]
[Adresse der Behörde]

Beschwerdeführer/in:  [Vollständiger Name]
                      [Straße, PLZ Ort]
                      geboren am [Datum]
                      SVNR: [Sozialversicherungsnummer]

Belangte Behörde:     [AMS — Regionale Geschäftsstelle [Ort]]

GZ des Bescheids:     [Geschäftszahl]

wegen:                [z.B. "Einstellung des Arbeitslosengeldes" /
                       "Bezugssperre gemäß §11 AlVG"]

                  B E S C H W E R D E
              gemäß Art 130 Abs 1 Z 1 B-VG iVm §7 VwGVG

I. ANGEFOCHTENER BESCHEID

1.  Mit Bescheid vom [Datum], GZ [Geschäftszahl], hat das AMS [Ort]
    [Inhalt des Bescheids — z.B. "den Bezug des Arbeitslosengeldes
    für den Zeitraum [Datum] bis [Datum] gemäß §10 AlVG eingestellt"].

2.  Dieser Bescheid wurde am [Zustelldatum] zugestellt. Die
    Beschwerdefrist von vier Wochen (§7 Abs 4 VwGVG) ist gewahrt.

II. BESCHWERDEGRÜNDE

Die Beschwerde richtet sich gegen den Bescheid seinem gesamten
Inhalt nach und stützt sich auf folgende Gründe:

A. Inhaltliche Rechtswidrigkeit

3.  [Erster Beschwerdegrund — z.B. "Die angebotene Stelle als [Beruf]
    war nicht zumutbar im Sinne des §9 AlVG. Die Wegzeit von [x] Stunden
    einfach übersteigt die zumutbare Grenze erheblich."]

4.  [Zweiter Beschwerdegrund]

B. Verfahrensfehler [falls zutreffend]

5.  [z.B. "Die belangte Behörde hat es unterlassen, den
    Beschwerdeführer vor Bescheiderlassung anzuhören (Verletzung
    des Parteiengehörs gemäß §45 Abs 3 AVG)."]

III. ANTRÄGE

Der Beschwerdeführer stellt daher die Anträge, das
Bundesverwaltungsgericht möge

1.  den angefochtenen Bescheid ersatzlos beheben;
    [ODER: den angefochtenen Bescheid dahingehend abändern, dass
    [gewünschter Inhalt]]

2.  eine mündliche Verhandlung durchführen;

3.  in eventu den angefochtenen Bescheid aufheben und die
    Angelegenheit zur neuerlichen Entscheidung an die belangte
    Behörde zurückverweisen.

[Ort], am [Datum]

                         ____________________
                         [Unterschrift]


BEILAGENVERZEICHNIS:
./A  Angefochtener Bescheid vom [Datum]
./B  [Beweismittel]
./C  [Weiteres Beweismittel]
```

---

## Step 7: Present with Timeline, Costs, and Next Steps

```markdown
# Sozialrechtliche Beschwerde / Klage

**Sachverhalt:** [2-3 Sätze Zusammenfassung]
**Angefochtener Bescheid:** [Behörde], GZ [x], vom [Datum]
**Zustellung:** [Datum]
**Rechtsmittel:** [Klage ans ASG / Beschwerde an BVwG / Beschwerde an LVwG]

## ⚠️ Fristenlage

| Frist | Fristende | Status |
|-------|-----------|--------|
| [Klage-/Beschwerdefrist] | [Datum] | 🟢 / 🟡 / 🔴 |

## Forum und Verfahren

**Zuständiges Gericht/Behörde:** [ASG [Ort] / BVwG / LVwG]
**Verfahrensart:** [Sozialrechtssache gemäß §65 ASGG / Verwaltungssache gemäß §7 VwGVG]
**Einzubringen bei:** [direkt beim Gericht / über die Behörde (AMS)]

## Kostenrisiko

### Bei Klage ans ASG (Sozialrechtssache):
⚡ **KEIN KOSTENRISIKO gemäß §77 ASGG!**

In Sozialrechtssachen vor dem Arbeits- und Sozialgericht gilt:
- **Keine Gerichtsgebühren** für den Kläger/die Klägerin (§80 ASGG — Gebührenfreiheit)
- **Kein Kostenersatz an den Gegner** bei Unterliegen (§77 Abs 1 Z 1 ASGG — der SVT bekommt keine Kosten ersetzt)
- **Sachverständigengutachten** werden vom Gericht bestellt und vom Bund bezahlt
- **Anwaltspflicht:** Keine (§40 ASGG) — Sie können sich selbst vertreten
- **Kostenlose Rechtsvertretung** durch Arbeiterkammer oder Gewerkschaft möglich

→ Es gibt praktisch keinen Grund, ein Rechtsmittel in Sozialrechtssachen aus Kostengründen nicht zu ergreifen.

### Bei Beschwerde an BVwG (z.B. AMS):
- **Keine Gebühren** für Beschwerden an das BVwG
- **Kein Anwaltszwang**
- **Kostenlose Vertretung** durch AK/Gewerkschaft möglich

## Beschwerdegründe

| Grund | Rechtsgrundlage | Erfolgsaussicht |
|-------|----------------|-----------------|
| [Grund 1] | §[x] [Gesetz] | 🟢 / 🟡 / 🔴 |
| [Grund 2] | §[x] [Gesetz] | 🟢 / 🟡 / 🔴 |

## Entwurf der Beschwerde / Klage

[Hier den Entwurf aus Step 6 einfügen]

## Weitere Rechtsmittel (Instanzenzug)

### Von ASG-Urteil:
1. **Berufung an das OLG** — Frist: 4 Wochen ab Zustellung des Urteils (§§461ff ZPO)
   - Berufungsgründe: Mangelhaftigkeit des Verfahrens, unrichtige Beweiswürdigung, unrichtige rechtliche Beurteilung
   - Auch hier: §77 ASGG Kostenfreiheit gilt weiter
2. **Revision an den OGH** — nur bei erheblicher Rechtsfrage (§502 Abs 1 ZPO)
   - Revisionsbeschränkung: Streitwert über €5.000 ODER Rechtsfrage von erheblicher Bedeutung
   - In Sozialrechtssachen: §46 Abs 3 ASGG — Revision auch unter €5.000 zulässig, wenn erhebliche Rechtsfrage

### Von BVwG-Erkenntnis:
1. **Revision an den VwGH** — nur bei Rechtsfrage von grundsätzlicher Bedeutung (Art 133 Abs 4 B-VG)
2. **Beschwerde an den VfGH** — bei Grundrechtsverletzung (Art 144 B-VG)
   - Frist: jeweils 6 Wochen ab Zustellung

## Nächste Schritte

1. [Erster konkreter Schritt — z.B. "Klage bis [Fristende] beim ASG [Ort] einbringen"]
2. [Zweiter Schritt — z.B. "Medizinische Unterlagen sammeln: Befunde, Gutachten"]
3. [Dritter Schritt — z.B. "Kontakt mit der AK [Ort] aufnehmen für kostenlose Rechtsvertretung"]
4. [z.B. "Keine Beweismittel entsorgen — alle Unterlagen aufbewahren"]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Diese Analyse ersetzt nicht die Beratung durch einen Rechtsanwalt. In Sozialrechtssachen bieten Arbeiterkammer und Gewerkschaften kostenlose Rechtsvertretung an — nutzen Sie diese! Insbesondere bei komplexen Pensionsfragen oder Pflegegeld-Einstufungen ist fachkundige Vertretung empfehlenswert, auch wenn sie nicht verpflichtend ist.
```

---

## Critical Rules

1. **Always mention §77 ASGG Kostenfreiheit** — Viele Menschen fechten sozialrechtliche Bescheide nicht an, weil sie Kosten fürchten. In Sozialrechtssachen vor dem ASG gibt es praktisch KEIN Kostenrisiko für Kläger. Diese Information muss in jeder Analyse prominent vorkommen.
2. **Verwaltungssache vs. Leistungssache immer zuerst klären** — Die Unterscheidung entscheidet über das Forum (ASG vs. BVwG). Falsches Forum = Zurückweisung.
3. **Fristen sind absolut vorrangig** — Fristberechnung immer als erstes durchführen und prominent darstellen. Bei abgelaufener Frist sofort prüfen, ob Wiedereinsetzung möglich ist.
4. **Klage, nicht Beschwerde (am ASG)** — In Leistungssachen wird eine KLAGE eingebracht (§67 ASGG), keine Beschwerde. Terminologie korrekt verwenden.
5. **Beschwerde über die Behörde einbringen (BVwG)** — Beschwerden an das BVwG werden bei der Behörde eingebracht, die den Bescheid erlassen hat (§12 VwGVG), nicht direkt beim BVwG.
6. **AK/Gewerkschaft-Hinweis** — In jeder sozialrechtlichen Beschwerde-Analyse auf die kostenlose Rechtsvertretung durch AK und Gewerkschaft hinweisen.
7. **Gerichtsferien hemmen NICHT am ASG** — §§23 Abs 1, 92 Abs 1 ASGG: Die Gerichtsferien hemmen in Sozialrechtssachen die Fristen nicht. Nicht darauf vertrauen!
8. **Sachverständigengutachten anfordern** — In Pensions- und Pflegegeldsachen: Das Gericht bestellt Sachverständige von Amts wegen. Immer anregen, ein neues Gutachten einzuholen, wenn das Gutachten im Bescheid mangelhaft war.
9. **Cite specific §§** — Keine pauschalen Verweise. Immer die exakte Gesetzesstelle angeben (z.B. §65 Abs 1 Z 1 ASGG, §9 Abs 2 AlVG).
10. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
