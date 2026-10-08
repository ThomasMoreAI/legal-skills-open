---
name: sozialklausel-widerspruch-borghei
title: /mietrecht:sozialklausel-widerspruch
description: Sozialklausel und Widerspruch gegen die ordentliche Kündigung von Wohnraum – Härtegründe und Interessenabwägung § 574 BGB, fehlender angemessener Ersatzwohnraum § 574 Abs. 2 BGB, Fortsetzung des Mietverhältnisses § 574a BGB, Form und Frist des Widerspruchs § 574b BGB, Fortsetzung nach Wegfall der Härte § 574c BGB, Unabdingbarkeit § 574 Abs. 4 BGB, Verhältnis zur Räumungsklage und zur Räumungsfrist § 721 ZPO. Use when ein Mieter einer ordentlichen Kündigung widersprechen und Fortsetzung verlangen will oder ein Vermieter die Erfolgsaussichten eines Härteeinwands bewertet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/sozialklausel-widerspruch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:sozialklausel-widerspruch

## Zweck

Die Sozialklausel ist die letzte Verteidigungslinie des Mieters: Sie greift erst, wenn die Kündigung **wirksam** ist. Sie beseitigt die Kündigung nicht, sondern verlangt die **Fortsetzung** des Mietverhältnisses — befristet oder unbefristet. Diese Skill strukturiert die Härtegründe, führt die zweiseitige Interessenabwägung, wahrt die Form- und Fristerfordernisse des § 574b BGB und ordnet den Widerspruch prozessual in das Räumungsverfahren ein.

## Eingaben

- **Kündigungsschreiben**: Kündigungsart, Grund, Zugangsdatum, Beendigungszeitpunkt, Hinweis nach § 568 Abs. 2 BGB
- **Persönliche Lage** des Mieters und aller Haushaltsangehörigen: Alter, Gesundheit (ärztliche Atteste), Behinderung, Pflegebedürftigkeit, Schwangerschaft, Schulsituation der Kinder
- **Mietdauer** und Verwurzelung im Wohnumfeld (soziales Netz, Betreuung, Arbeitsplatznähe)
- **Wirtschaftliche Lage**: Einkommen, Leistungsbezug, Angemessenheitsgrenzen des Sozialleistungsträgers
- **Ersatzwohnraumsuche**: Zahl und Ergebnis der Bewerbungen, Zeitraum, Dokumentation
- **Vermieterinteressen**: Dringlichkeit des Eigenbedarfs, wirtschaftliche Nachteile, Alternativwohnungen im Bestand

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Vorfragen-Prüfer** klärt zuerst, ob überhaupt eine ordentliche Kündigung vorliegt — gegen die außerordentliche fristlose Kündigung ist der Widerspruch gesperrt. Ein **Härte-Sammler** trägt die Härtegründe belegt zusammen und trennt Behauptung von Nachweis. Ein **Abwägungs-Prüfer** stellt Mieter- und Vermieterinteressen gegenüber. Ein **Form-Prüfer** sichert Schriftform, Frist und Begründung nach § 574b BGB. Ein **Prozess-Prüfer** verknüpft das Ergebnis mit Räumungsklage, Räumungsfrist und Vollstreckungsschutz.

## Ablauf

### 1. Anwendungsbereich und Sperren ([§ 574 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__574.html))

Der Mieter kann der Kündigung des Vermieters widersprechen und die Fortsetzung des Mietverhältnisses verlangen, wenn die Beendigung für ihn, seine Familie oder einen anderen Angehörigen seines Haushalts eine **Härte** bedeuten würde, die auch unter Würdigung der berechtigten Interessen des Vermieters **nicht zu rechtfertigen** ist.

Der Widerspruch ist **ausgeschlossen**, wenn ein Grund vorliegt, der den Vermieter zur **außerordentlichen fristlosen Kündigung** berechtigt (Abs. 1 S. 2) — also insbesondere bei Zahlungsverzug nach § 543 Abs. 2 S. 1 Nr. 3 BGB. Er gilt ferner nicht bei Kündigungen nach § 573a BGB (erleichterte Kündigung im Zweifamilienhaus) hinsichtlich der verlängerten Frist, wohl aber der Sache nach. Abweichende Vereinbarungen zum Nachteil des Mieters sind nach **§ 574 Abs. 4 BGB unwirksam**.

### 2. Härtegründe ([§ 574 Abs. 1, Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__574.html))

Typische, in der Praxis anerkannte Härtegründe:

- **Hohes Alter** in Verbindung mit langer Mietdauer und Verwurzelung — das Alter allein genügt nicht, wohl aber in der Gesamtschau.
- **Schwere Erkrankung, Behinderung, Pflegebedürftigkeit** — belegt durch **ärztliches Attest**, das Art, Schwere und die konkrete Umzugsfolge benennt; im Prozess ist regelmäßig ein **Sachverständigengutachten** einzuholen, wenn eine erhebliche Gesundheitsgefahr substantiiert vorgetragen ist (BGH, Urt. v. 22.05.2019 – VIII ZR 180/18 u.a., https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2019-05-22&Aktenzeichen=VIII%20ZR%20180/18).
- **Schwangerschaft** und die Zeit unmittelbar nach der Entbindung.
- **Bevorstehendes Examen oder Schulabschluss** der im Haushalt lebenden Kinder.
- **Fehlender angemessener Ersatzwohnraum zu zumutbaren Bedingungen** — nach § 574 Abs. 2 BGB ausdrücklich ein Härtegrund. Der Mieter muss die Suche **dokumentieren**: Zahl der Bewerbungen, Zeitraum, Absagen, Suchradius, Preisgrenze. Wer nicht sucht, verliert.

Nicht ausreichend sind allgemeine Unannehmlichkeiten des Umzugs, Kosten oder eine höhere Miete für sich genommen — wohl aber eine Miete, die die Angemessenheitsgrenze des Leistungsträgers deutlich übersteigt.

### 3. Interessenabwägung

Die Härte muss **auch unter Würdigung der berechtigten Interessen des Vermieters** nicht zu rechtfertigen sein. Gegenüberzustellen sind:

| Mieterseite | Vermieterseite |
|---|---|
| Alter, Gesundheit, Pflegebedarf | Dringlichkeit und Konkretheit des Eigenbedarfs |
| Mietdauer, Verwurzelung, Betreuungsnetz | Wirtschaftliche Nachteile bei Verzögerung |
| Erfolglose Ersatzwohnraumsuche | Verfügbarkeit anderer Wohnungen im Bestand |
| Wirtschaftliche Leistungsfähigkeit | Eigene gesundheitliche oder familiäre Lage |
| Zahl und Alter der Haushaltsangehörigen | Dauer der bereits hingenommenen Verzögerung |

Die Abwägung ist **einzelfallbezogen** und ohne Schematismus vorzunehmen; eine feste Rangordnung der Kriterien gibt es nicht. Bei der Eigenbedarfskündigung ist zusätzlich die Wirksamkeit der Kündigung selbst zu prüfen: `/mietrecht:eigenbedarfskuendigung`.

### 4. Form und Frist des Widerspruchs ([§ 574b BGB](https://www.gesetze-im-internet.de/bgb/__574b.html))

Der Widerspruch ist **schriftlich** zu erklären (§ 574b Abs. 1 S. 1 BGB; Textform genügt **nicht**). Auf Verlangen des Vermieters hat der Mieter über die **Gründe des Widerspruchs unverzüglich Auskunft** zu erteilen (Abs. 1 S. 2). Die Erklärung muss dem Vermieter **spätestens zwei Monate vor Beendigung** des Mietverhältnisses zugegangen sein (Abs. 2 S. 1).

**Ausnahme:** Hat der Vermieter den Mieter nicht rechtzeitig — spätestens zu Beginn der Widerspruchsfrist — auf die Möglichkeit des Widerspruchs sowie auf Form und Frist **hingewiesen** (§ 568 Abs. 2 BGB), kann der Mieter den Widerspruch noch **im ersten Termin des Räumungsrechtsstreits** erklären (§ 574b Abs. 2 S. 2 BGB). Der fehlende Hinweis ist daher stets zu prüfen — er rettet den verspäteten Widerspruch.

### 5. Fortsetzung des Mietverhältnisses ([§ 574a BGB](https://www.gesetze-im-internet.de/bgb/__574a.html))

Rechtsfolge ist nicht die Unwirksamkeit der Kündigung, sondern der Anspruch auf **Fortsetzung** — **auf bestimmte oder auf unbestimmte Zeit**. Der Mieter kann zugleich verlangen, dass das Mietverhältnis zu **geänderten Bedingungen** fortgesetzt wird, soweit dies dem Vermieter zumutbar ist (Abs. 1 S. 2) — etwa Anpassung der Miete an das ortsübliche Niveau. Kommt keine Einigung zustande, entscheidet das **Gericht** durch Urteil (Abs. 2). Ist ungewiss, wann die Umstände wegfallen, die zur Fortsetzung geführt haben, kann die Fortsetzung auf unbestimmte Zeit angeordnet werden.

### 6. Erneute Kündigung und Wegfall der Härte ([§ 574c BGB](https://www.gesetze-im-internet.de/bgb/__574c.html))

Ist das Mietverhältnis auf unbestimmte Zeit fortgesetzt worden, kann der Mieter eine **erneute Fortsetzung** nur verlangen, wenn sich die Umstände **wesentlich geändert** haben (Abs. 1). Wurde die Fortsetzung auf **bestimmte Zeit** angeordnet und kündigt der Vermieter zum Ablauf, kann der Mieter erneut Fortsetzung verlangen, wenn die Voraussetzungen noch vorliegen (Abs. 2). Fällt der Härtegrund weg, kann der Vermieter erneut kündigen — mit den Fristen des [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html).

### 7. Prozessuale Einordnung

Der Widerspruch wird im **Räumungsrechtsstreit** als Einwendung geltend gemacht; das Gericht entscheidet zugleich über Wirksamkeit der Kündigung und Fortsetzungsanspruch. Scheitert der Widerspruch, bleibt die **Räumungsfrist** nach [§ 721 ZPO](https://www.gesetze-im-internet.de/zpo/__721.html) (bis zu einem Jahr) und im Vollstreckungsverfahren der **Vollstreckungsschutz** nach [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html). Diese drei Instrumente sind gestuft und dürfen nicht verwechselt werden: § 574 BGB ist materiellrechtlich und führt zur Fortsetzung, § 721 ZPO verlängert nur die Räumungszeit, § 765a ZPO stellt die Vollstreckung vorübergehend ein. Vertiefung: `/mietrecht:raeumungsklage`.

## Quellen

### Statute

- [§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html), [§ 574a BGB](https://www.gesetze-im-internet.de/bgb/__574a.html), [§ 574b BGB](https://www.gesetze-im-internet.de/bgb/__574b.html), [§ 574c BGB](https://www.gesetze-im-internet.de/bgb/__574c.html)
- [§ 573 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 573a BGB](https://www.gesetze-im-internet.de/bgb/__573a.html), [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html), [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html)
- [§ 721 ZPO](https://www.gesetze-im-internet.de/zpo/__721.html), [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html)

### Kommentare

- Blank, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 574 BGB Rn. 1 ff.
- Häublein, in: MüKoBGB, 9. Aufl. 2023, § 574 Rn. 1 ff.; § 574a Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 574 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 22.05.2019 – VIII ZR 180/18 und VIII ZR 167/17 (Interessenabwägung bei Eigenbedarfskündigung eines langjährigen erkrankten Mieters; Anforderungen an die Sachaufklärung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2019-05-22&Aktenzeichen=VIII%20ZR%20180/18
- BGH, Urt. v. 10.06.2015 – VIII ZR 99/14 (Schadensersatz bei vorgetäuschtem Eigenbedarf — flankierend zur Härteprüfung) `[unverifiziert - prüfen]`
- Zu den Anforderungen an die Dokumentation der Ersatzwohnraumsuche ist die einschlägige Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Widerspruch nach §§ 574, 574b BGB

```
Einschreiben mit Rückschein

Sehr geehrte Frau …, sehr geehrter Herr …,

Ihrer Kündigung des Mietverhältnisses über die Wohnung <Anschrift> vom
<Datum>, mir zugegangen am <Datum>, zum <Beendigungszeitpunkt>

                          w i d e r s p r e c h e   i c h

hiermit gemäß § 574 BGB und verlange die Fortsetzung des Mietverhältnisses
gemäß § 574a BGB auf unbestimmte Zeit, hilfsweise auf bestimmte Zeit bis
zum <Datum>.

Begründung (§ 574b Abs. 1 S. 2 BGB):

1. Ich bewohne die Wohnung seit <Jahr>, mithin seit <…> Jahren. Mein
   gesamtes soziales und medizinisches Umfeld befindet sich im Stadtteil.
2. Ich bin <Alter> Jahre alt und leide an <Erkrankung>. Nach dem
   beigefügten Attest von <Arzt> vom <Datum> würde ein Umzug zu
   <konkrete gesundheitliche Folge> führen. Ein Sachverständigengutachten
   biete ich an.
3. Angemessenen Ersatzwohnraum zu zumutbaren Bedingungen habe ich trotz
   intensiver Suche nicht gefunden (§ 574 Abs. 2 BGB). Seit <Datum> habe
   ich mich auf <Zahl> Wohnungen beworben; die Absagen füge ich bei. Die
   ortsüblichen Mieten überschreiten die Angemessenheitsgrenze des
   <Leistungsträger> von <Betrag> EUR erheblich.
4. Demgegenüber wiegt Ihr Interesse geringer, weil <konkret: weitere
   Wohnung im Bestand frei / Nutzungswunsch zeitlich nicht dringlich>.

Die Frist des § 574b Abs. 2 BGB ist gewahrt.

Anlagen: Attest vom <Datum>; <Zahl> Bewerbungen und Absagen

Mit freundlichen Grüßen
<eigenhändige Unterschrift>
```

## Ausgabeformat

```
SOZIALKLAUSEL / WIDERSPRUCH §§ 574 ff. BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Kündigungsart                      [ordentlich § 573 / § 573a / fristlos ❌ gesperrt]
      Wirksamkeit der Kündigung          [✅ / ⚠️ — zuerst angreifen]
II.   Härtegründe (§ 574 Abs. 1, 2)
      - Alter / Mietdauer / Verwurzelung  <…>
      - Gesundheit / Pflege               <Attest vom …>  [substantiiert / dünn]
      - Schwangerschaft / Examen          <…>
      - Fehlender Ersatzwohnraum          <Zahl Bewerbungen>  [dokumentiert / nicht ⚠️]
III.  Vermieterinteressen                 <Dringlichkeit, Alternativen im Bestand>
IV.   Interessenabwägung                  [Härte überwiegt / offen / Vermieter überwiegt]
V.    Form und Frist (§ 574b)
      - Schriftform, Unterschrift         [✅ / ❌]
      - Zugang 2 Monate vor Beendigung    [✅ / ❌]
      - Hinweis § 568 Abs. 2 BGB erteilt  [ja / nein → Widerspruch noch im
                                            ersten Termin möglich]
VI.   Fortsetzungsverlangen (§ 574a)      [unbestimmte Zeit / bis <Datum>]
      Geänderte Bedingungen               [keine / Mietanpassung auf <Betrag>]
VII.  Erneute Kündigung (§ 574c)          [Wegfall der Härte absehbar? ja/nein]
VIII. Prozessuale Absicherung
      - Räumungsfrist § 721 ZPO           [zu beantragen — bis <Datum>]
      - Vollstreckungsschutz § 765a ZPO   [kein Anlass / vorzubereiten]

Ergebnis: <Widerspruch erfolgversprechend / offen / aussichtslos>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Zwei-Monats-Frist des § 574b BGB versäumt** — der Widerspruch ist verspätet, sofern der Vermieter ordnungsgemäß nach § 568 Abs. 2 BGB hingewiesen hat; ohne Hinweis bleibt der Weg über den ersten Termin.
- **Textform statt Schriftform** — der Widerspruch bedarf der eigenhändigen Unterschrift; E-Mail genügt nicht.
- **Härtegründe nur behauptet** — pauschale Angaben zu Alter oder Krankheit tragen nicht; erforderlich sind Attest, konkrete Umzugsfolge und Beweisantritt.
- **Ersatzwohnraumsuche nicht dokumentiert** — der wichtigste Härtegrund des § 574 Abs. 2 BGB scheitert regelmäßig am fehlenden Nachweis der Suchbemühungen.
- **Widerspruch gegen fristlose Kündigung** — nach § 574 Abs. 1 S. 2 BGB gesperrt; hier hilft nur die Schonfristzahlung oder der Angriff auf die Kündigung selbst.
- **Wirksamkeit der Kündigung nicht vorab geprüft** — die Sozialklausel ist die zweite Verteidigungslinie; die formelle Angreifbarkeit der Kündigung ist meist der schnellere Weg.
- **§ 574 BGB, § 721 ZPO und § 765a ZPO verwechselt** — nur die Sozialklausel führt zur Fortsetzung des Mietverhältnisses.
- **Fortsetzungsverlangen ohne Zeitangabe** — der Antrag sollte primär auf unbestimmte Zeit und hilfsweise befristet gestellt werden.
