---
name: recht-klage-momarcode1
title: /recht klage — Schriftsatz-Entwurf
description: Drafts Austrian legal filings — Klage, Klagebeantwortung, Berufung, Mahnschreiben, einstweilige Verfügung, Einspruch. Proper Austrian court format.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-klage
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: litigation
language: de
---

# /recht klage — Schriftsatz-Entwurf

When the user needs a legal filing drafted, follow these steps.

---

## Step 1: Determine the Filing Type

Ask or infer what is needed:

| If user wants to... | Draft a... |
|---------------------|-----------|
| Demand payment before suing | **Mahnschreiben** |
| Sue for money (undisputed) | **Antrag auf Zahlungsbefehl** (Mahnverfahren) |
| Sue (general) | **Klage** |
| Respond to a lawsuit | **Klagebeantwortung** |
| Appeal a judgment | **Berufung** (4 weeks from Zustellung!) |
| Object to a Zahlungsbefehl | **Einspruch** (4 weeks!) |
| Get emergency protection | **Antrag auf einstweilige Verfügung** |
| Apply in non-contentious matter | **Antrag** (AußStrG) |

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Gather Required Information

For ANY filing you need:
- [ ] Full name + address of Kläger/Antragsteller (+ Geburtsdatum if natürliche Person)
- [ ] Full name + address of Beklagter/Antragsgegner
- [ ] The facts (chronological, complete)
- [ ] The evidence (what documents, witnesses exist)
- [ ] What the user wants the court to order (Begehren)
- [ ] Streitwert

Ask for anything missing. Be specific:
> "Ich brauche die vollständige Adresse des Beklagten für den Schriftsatz."

---

## Step 4: Draft the Filing

### For a KLAGE, use this exact structure:

```
An das [Bezirksgericht/Landesgericht] [Ort]

Kläger:     [Vollständiger Name]
            [Straße, PLZ Ort]
            geboren am [Datum]
            [vertreten durch: RA Name, Adresse — if applicable]

Beklagter:  [Vollständiger Name]
            [Straße, PLZ Ort]

wegen:      [Kurzbeschreibung — z.B. "Zahlung", "Gewährleistung", "Räumung"]
Streitwert: €[Betrag]

                            K L A G E

I. SACHVERHALT

1.  [First fact — chronological. State only facts, no legal conclusions.]

    Beweis: Beilage ./A [Beschreibung];
            PV [= Parteienvernehmung des Klägers]

2.  [Second fact]

    Beweis: Beilage ./B; Zeuge [Name], [Adresse]

3.  [Continue for all relevant facts]

    Beweis: [evidence]

II. RECHTLICHE BEURTEILUNG

[Now apply law to facts. Structure:]
- State the applicable legal basis (§[x] [Gesetz])
- Subsume: "Der Beklagte hat [Tatbestandsmerkmal] verwirklicht, indem..."
- Cite OGH case law if helpful: "Der OGH hat in [GZ] entschieden, dass..."
- Address potential defenses preemptively if obvious

III. KLAGEBEGEHREN

Der Kläger stellt daher den

                            A N T R A G,

das Gericht möge den Beklagten schuldig erkennen,

1.  dem Kläger den Betrag von €[Betrag] samt 4% Zinsen
    seit [Datum — Fälligkeit oder Mahnung] binnen 14 Tagen
    bei sonstiger Exekution zu bezahlen;

    [ODER für B2B:]
    ... samt Zinsen in Höhe von 9,2 Prozentpunkten über dem
    Basiszinssatz seit [Datum] ...

    [ODER für Leistungsklage:]
    [die konkrete Leistung zu erbringen / zu unterlassen / herauszugeben]

2.  dem Kläger die Kosten dieses Rechtsstreits binnen 14 Tagen
    bei sonstiger Exekution zu ersetzen.

[Ort], am [Datum]

                            ____________________
                            [Name des Klägers / RA]


BEILAGENVERZEICHNIS:
./A  [Beschreibung — z.B. "Kaufvertrag vom 01.03.2025"]
./B  [Beschreibung — z.B. "E-Mail des Beklagten vom 15.04.2025"]
./C  [Beschreibung]
```

### Key Rules for the Klage:

1. **Sachverhalt: ONLY facts** — no legal opinions, no "der Beklagte hat rechtswidrig..."
2. **Every fact needs Beweis** — cite Beilage, Zeuge, Sachverständiger, or PV after each paragraph
3. **Beilagen** — number ./A, ./B, ./C sequentially. Describe each briefly.
4. **Klagebegehren must be vollstreckbar** — the court must be able to enforce it. "Der Beklagte soll zahlen" is too vague. "€5.000 samt 4% Zinsen seit 01.05.2025 binnen 14 Tagen bei sonstiger Exekution" is correct.
5. **Zinsen:**
   - B2C default: 4% per §1333 ABGB
   - B2B: 9,2% über Basiszinssatz per §456 UGB
   - Start date: ab Fälligkeit or ab Mahnung (whichever applies)
6. **Kostenantrag** — ALWAYS include "Kostenersatz" per §41 ZPO

### For a MAHNSCHREIBEN:

```
[Absender Name + Adresse]

                                        Per Einschreiben

An [Empfänger Name]
[Adresse]

[Ort], am [Datum]

Betreff: Zahlungsaufforderung — [Vertrag/Rechnung vom [Datum]]

Sehr geehrte Damen und Herren, [ODER: Sehr geehrte(r) Herr/Frau [Name],]

wir beziehen uns auf [den Vertrag vom / die Rechnung Nr. X vom / die Lieferung vom]
[Datum]. Der daraus resultierende Betrag von €[Betrag] war am [Fälligkeitsdatum]
fällig.

Trotz Fälligkeit ist der Betrag bis dato nicht auf unserem Konto eingegangen.

Wir fordern Sie hiermit auf, den offenen Betrag von

    €[Betrag]
    zuzüglich Verzugszinsen in Höhe von [4% / 9,2% über dem Basiszinssatz]
    seit [Fälligkeitsdatum],
    sohin per heute insgesamt €[Gesamtbetrag inkl. Zinsen]

bis spätestens [Datum + 14 Tage] auf folgendes Konto zu überweisen:

    IBAN: [IBAN]
    BIC: [BIC]
    Lautend auf: [Kontoinhaber]
    Verwendungszweck: [Referenz]

Sollte der Betrag nicht fristgerecht bei uns einlangen, werden wir ohne
weitere Ankündigung den Rechtsweg beschreiten. Die daraus entstehenden
Kosten (Gerichtsgebühren, Anwaltskosten) gehen zu Ihren Lasten.

Mit freundlichen Grüßen

____________________
[Unterschrift]
[Name]
```

### For a KLAGEBEANTWORTUNG:

Same structure as Klage, but:
- Title: "KLAGEBEANTWORTUNG"
- Respond to each numbered paragraph of the Klage: "Zu Punkt 1: [zugestanden / bestritten / nicht bekannt]"
- Raise all Einwendungen (defenses) explicitly
- Include Eventualanträge (in the alternative)
- Gegenklage (Widerklage) if applicable

---

## Step 5: Review and Flag Issues

Before presenting:
- [ ] Is the Rubrum complete? (Names, addresses, Geburtsdatum)
- [ ] Is every fact supported by Beweis?
- [ ] Is the Klagebegehren specific and vollstreckbar?
- [ ] Are Zinsen correctly calculated?
- [ ] Is Kostenersatz included?
- [ ] Is Streitwert stated?

---

## Step 6: Present with Disclaimer

Present the draft in a code block, then add the Quellenstatus and disclaimer:

```markdown
## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |
```

```
⚠️ WICHTIG: Dieser Entwurf ist eine Vorlage und muss vor Einreichung von
einem zugelassenen Rechtsanwalt geprüft werden. Bei Verfahren vor dem
Landesgericht besteht Anwaltspflicht (§27 ZPO) — Sie MÜSSEN einen
Rechtsanwalt beauftragen.

Anwaltspflicht:
- BG: Keine Anwaltspflicht bei Streitwert ≤ €5.000
- BG: Anwaltspflicht bei Streitwert > €5.000
- LG: Immer Anwaltspflicht
```
