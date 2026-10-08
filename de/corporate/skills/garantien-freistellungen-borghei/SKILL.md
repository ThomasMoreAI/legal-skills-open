---
name: garantien-freistellungen-borghei
title: /m-a-transaktionsrecht:garantien-freistellungen
description: Aufbau und Verhandlung des Garantie- und Freistellungsregimes im Unternehmenskaufvertrag – selbständige Garantieversprechen nach § 311 Abs. 1 BGB statt Beschaffenheitsgarantie § 443 BGB, Abbedingung des gesetzlichen Gewährleistungsrechts der §§ 434 ff. BGB mit der Arglistgrenze § 444 BGB, Garantiekatalog (Legal, Tax, Financial, Operational), Rechtsfolgenregime mit Ausschluss der Naturalrestitution, De-minimis, Basket als Freibetrag oder Freigrenze, Cap, vertragliche Verjährung, Kenntnis des Käufers § 442 BGB und ihre Modifikation, Steuerfreistellung und W&I-Versicherung. Use when ein Garantiekatalog entworfen, eine Haftungsbegrenzung verhandelt oder ein Garantieverstoß nach Closing geltend gemacht wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/m-a-transaktionsrecht/skills/garantien-freistellungen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
---

# /m-a-transaktionsrecht:garantien-freistellungen

## Zweck

Das Garantieregime ist das wirtschaftliche Herzstück des Unternehmenskaufvertrags: Es verteilt die Risiken, die die Due Diligence nicht ausräumen konnte. Der deutsche Vertrag arbeitet dabei **nicht** mit dem gesetzlichen Mängelrecht, sondern mit einem geschlossenen, **selbständigen Garantieversprechen** samt eigenem Rechtsfolgenregime. Dieser Skill baut dieses System auf und prüft es auf Lücken.

## Eingaben

- Transaktionsstruktur: Share Deal oder Asset Deal, Zielgesellschaft, Kaufpreis
- Verhandlungsposition und Verkäufertyp (Gründer, Familie, Private Equity, Insolvenzverwalter)
- Due-Diligence-Findings und Disclosure Schedules — Stand und Vollständigkeit
- Bereits verhandelte Eckwerte: De-minimis, Basket, Cap, Verjährungsfristen, Escrow
- Steuerhistorie: laufende Betriebsprüfung, offene Veranlagungszeiträume, Organschaften
- Ist eine W&I-Versicherung (Warranty & Indemnity) vorgesehen oder ausgeschrieben?
- Bei Geltendmachung: Verstoß, Kenntniszeitpunkt, bereits eingetretener Schaden, Fristenlage

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 311, 434 ff., 442, 444 BGB, die Kommentarliteratur zur selbständigen Garantie und die Rechtsprechung zur Reichweite des § 444 BGB.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) formuliert Garantiekatalog, Rechtsfolgenklausel, Haftungsbegrenzungen und Steuerfreistellung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft, ob der Ausschluss des gesetzlichen Rechts vollständig und wirksam ist, ob jede Begrenzung an die richtige Garantiegruppe anknüpft und ob Fristen und Escrow-Laufzeit zusammenpassen.

## Ablauf

### 1. Rechtsnatur — selbständige Garantie ([§ 311 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__311.html))

Die Garantien im Unternehmenskaufvertrag sind **selbständige, verschuldensunabhängige Garantieversprechen** im Sinne eines durch Rechtsgeschäft begründeten Schuldverhältnisses nach § 311 Abs. 1 BGB — **nicht** Beschaffenheitsgarantien nach [§ 443 BGB](https://www.gesetze-im-internet.de/bgb/__443.html) und **nicht** Beschaffenheitsvereinbarungen nach § 434 BGB. Der Grund ist praktisch: Das kaufrechtliche Mängelrecht passt auf ein Unternehmen schlecht — Nacherfüllung ist regelmäßig unmöglich, Rücktritt nach Vollzug wirtschaftlich untragbar, und der Mangelbegriff des § 434 BGB erfasst die Zielgesellschaft nur mittelbar über den Rechtskauf.

Die Klausel muss das ausdrücklich klarstellen:

> „Der Verkäufer gibt die nachstehenden Garantien als **selbständige Garantieversprechen im Sinne des § 311 Abs. 1 BGB** ab. Es handelt sich **nicht** um Beschaffenheitsgarantien im Sinne des § 443 BGB und **nicht** um Beschaffenheitsvereinbarungen im Sinne des § 434 BGB. Die Rechtsfolgen richten sich ausschließlich nach Ziffer [N]."

### 2. Abbedingung des gesetzlichen Gewährleistungsrechts ([§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html))

Das gesetzliche Mängelrecht der §§ 434 ff. BGB wird **vollständig ausgeschlossen** — einschließlich Rücktritt, Minderung, Nacherfüllung, Aufwendungsersatz sowie der Ansprüche aus Störung der Geschäftsgrundlage (§ 313 BGB), aus Verschulden bei Vertragsschluss (§§ 280, 311 Abs. 2, 241 Abs. 2 BGB) und aus Delikt, soweit dispositiv.

**Grenzen des Ausschlusses:**

- **§ 444 BGB:** Der Verkäufer kann sich auf den Ausschluss nicht berufen, soweit er den Mangel **arglistig verschwiegen** oder eine **Garantie für die Beschaffenheit** übernommen hat. Arglist ist nicht abdingbar — sie durchbricht jede Haftungsbegrenzung, jeden Cap und jede vertragliche Verjährung.
- **§ 276 Abs. 3 BGB:** Haftung für **Vorsatz** kann nicht im Voraus erlassen werden.
- **AGB-Kontrolle:** Beim individuell ausverhandelten SPA regelmäßig nicht einschlägig; bei standardisierten Beteiligungsverträgen und Musterunterlagen aber zu prüfen (§§ 305 ff. BGB).
- Ansprüche wegen **arglistiger Täuschung** (§ 123 BGB) und die Anfechtung bleiben ohnehin unberührt.

### 3. Garantiekatalog — Struktur

Der Katalog wird in vier Gruppen gegliedert, weil daran unterschiedliche Caps und Verjährungsfristen anknüpfen.

**A. Fundamental Warranties (Title & Capacity)** — vollwertiger Bestand des Kaufgegenstands:

1. Bestand, Rechtsform und ordnungsgemäße Errichtung der Zielgesellschaft; Richtigkeit der Registereintragungen
2. Stammkapital vollständig und wirksam erbracht, **keine Rückzahlung entgegen §§ 30, 31 GmbHG**, keine offenen Einlagen
3. Der Verkäufer ist alleiniger und unbeschränkter Inhaber der Anteile; keine Belastungen, Rechte Dritter, Treuhand-, Unterbeteiligungs- oder Stimmbindungsverhältnisse
4. Keine Zustimmungserfordernisse außer den offengelegten; volle Verfügungsbefugnis und Vertretungsmacht

**B. Legal / Operational Warranties:**

5. Wesentliche Verträge — Bestand, keine Kündigung, keine Change-of-Control-Rechte außer den offengelegten
6. Arbeitsverhältnisse, Betriebsvereinbarungen, Tarifbindung, Versorgungszusagen; keine ungedeckten Pensionsverpflichtungen
7. Gewerbliche Schutzrechte und Lizenzen — Inhaberschaft, Bestand, keine Verletzung Dritter
8. IT-Systeme, Datenschutz-Compliance (Verarbeitungsverzeichnis, AVV, keine offenen Meldeverfahren)
9. Öffentlich-rechtliche Genehmigungen, Umwelt- und Produktsicherheitslage, Rückrufe
10. Rechtsstreitigkeiten und Behördenverfahren — abschließende Auflistung in der Anlage
11. Versicherungsschutz, laufende Schadensfälle

**C. Financial Warranties:**

12. Jahresabschlüsse — aufgestellt nach den anzuwendenden Rechnungslegungsvorschriften unter Wahrung der Bilanzkontinuität, Vermittlung eines den tatsächlichen Verhältnissen entsprechenden Bildes
13. Keine über den offengelegten Rahmen hinausgehenden Verbindlichkeiten, Bürgschaften, Garantien oder Patronatserklärungen
14. **Ordinary Course** zwischen Bilanzstichtag und Signing/Closing; keine außergewöhnlichen Maßnahmen

**D. Tax Warranties:**

15. Steuererklärungen vollständig und fristgerecht abgegeben, Steuern gezahlt, Rückstellungen ausreichend, keine laufenden Verfahren außer den offengelegten

Jede Garantie erhält eine **Wissensqualifikation** nur dort, wo sie sachlich gerechtfertigt ist; „Kenntnis" ist dann als positive Kenntnis eines abschließend benannten Personenkreises nach zumutbarer Erkundigung zu definieren.

### 4. Rechtsfolgenregime

> „Im Falle einer Garantieverletzung hat der Verkäufer den Käufer **in Geld** so zu stellen, wie dieser stünde, wenn die Garantie zutreffend gewesen wäre. Der Anspruch ist auf **Geldersatz** gerichtet; **Naturalrestitution nach § 249 Abs. 1 BGB ist ausgeschlossen**. Nicht ersatzfähig sind entgangener Gewinn, mittelbare Schäden, Folgeschäden, interne Verwaltungskosten sowie Schäden, die auf einer Multiplikatorbetrachtung des Kaufpreises beruhen."

Ergänzend zu regeln: Vorteilsausgleichung, Anrechnung von Versicherungsleistungen und Steuervorteilen, Verbot der Doppelkompensation, Schadensminderungspflicht (§ 254 BGB), Mitwirkung bei der Abwehr von Drittansprüchen (Third Party Claims) und eine **Rügefrist** mit Beschreibung des Verstoßes.

### 5. Haftungsbegrenzungen

| Instrument | Funktion | Verhandlungshinweis |
|---|---|---|
| **De-minimis** | Einzelanspruch zählt erst ab einem Mindestbetrag | Üblich als Promillegröße des Kaufpreises; verhindert Bagatellstreit |
| **Basket** | Ansprüche werden erst ersatzfähig, wenn ihre Summe eine Schwelle übersteigt | **Freibetrag (Deductible/Excess):** nur der übersteigende Teil ist zu ersetzen. **Freigrenze (Tipping Basket):** bei Überschreiten wird der **volle** Betrag ab dem ersten Euro geschuldet. Der Unterschied ist wirtschaftlich erheblich und wird häufig übersehen |
| **Cap** | Haftungshöchstbetrag | Gestaffelt: niedrig für operative Garantien, höher für Tax, bis zur Kaufpreishöhe für Fundamental Warranties |
| **Verjährung** | Vertraglich abweichend von §§ 195, 199 BGB | Operative Garantien typischerweise 18–24 Monate ab Closing (ein Bilanzzyklus muss durchlaufen sein); Steuergarantien orientiert an der steuerlichen Festsetzungsverjährung; Fundamental Warranties deutlich länger |
| **Escrow** | Sicherung durch Treuhandkonto | Laufzeit muss die Verjährungsfrist der abgesicherten Garantien überdecken |

**Zwingend:** De-minimis, Basket, Cap und die verkürzte Verjährung gelten **nicht** bei Vorsatz und Arglist (§§ 276 Abs. 3, 444 BGB) — das ist im Vertrag ausdrücklich klarzustellen, sonst entsteht der Eindruck einer unwirksamen Gesamtbegrenzung.

Die Fristberechnung für Verjährungs- und Rügefristen übernimmt der deterministische Rechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er rechnet **ausschließlich** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — ob eine Rüge zugegangen und wann der Verstoß bekannt geworden ist, bewertet der Bearbeiter.

### 6. Kenntnis des Käufers ([§ 442 BGB](https://www.gesetze-im-internet.de/bgb/__442.html)) und Disclosure

Nach § 442 Abs. 1 BGB sind Rechte des Käufers ausgeschlossen, wenn er den Mangel bei Vertragsschluss **kannte**; bei grob fahrlässiger Unkenntnis nur, wenn der Verkäufer nicht arglistig gehandelt oder eine Beschaffenheitsgarantie übernommen hat. Weil die selbständige Garantie das gesetzliche Regime verdrängt, muss der Vertrag die Kenntniswirkung **selbst** regeln — sonst entsteht Streit darüber, ob der Datenraum den Anspruch entwertet.

Zwei Modelle:

- **Käuferfreundlich (Pro-Sandbagging):** „Die Kenntnis oder das Kennenmüssen des Käufers von Umständen, die eine Garantieverletzung begründen, lässt die Ansprüche unberührt. § 442 BGB wird abbedungen."
- **Verkäuferfreundlich (Anti-Sandbagging):** Ansprüche sind ausgeschlossen, soweit die Umstände in den **Disclosure Schedules** oder im Datenraum **fair disclosed** waren.

Wird das zweite Modell gewählt, ist der Offenlegungsmaßstab zu definieren: Genügt die bloße Aufnahme eines Dokuments in den Datenraum, oder ist eine Offenlegung erforderlich, die einem sachkundigen Käufer die Bedeutung **ohne Weiteres erkennbar** macht (Fair-Disclosure-Standard)? Der Datenraum ist zu Beweiszwecken auf einem Datenträger zu sichern und im Vertrag zu referenzieren. Siehe `/m-a-transaktionsrecht:due-diligence`.

### 7. Freistellungen (Indemnities) und W&I-Versicherung

Die **Freistellung** ist die Antwort auf ein **bekanntes** Risiko: Sie setzt keinen Garantieverstoß voraus, sondern greift bei Eintritt eines definierten Ereignisses und ist typischerweise von De-minimis, Basket und Cap **ausgenommen**. Anwendungsfälle: laufende Rechtsstreitigkeiten, Altlasten, ein identifizierter Compliance-Verstoß, ein streitiger Sachverhalt aus der Betriebsprüfung.

**Steuerfreistellung:** Der Verkäufer stellt von Steuern frei, die auf Zeiträume bis zum Stichtag entfallen und die die in der Bilanz gebildeten Rückstellungen übersteigen. Zu regeln sind Zeitraumabgrenzung, Anrechnung von Steuervorteilen, Erstattungsansprüchen und Verlustvorträgen, die **Führung des Rechtsbehelfsverfahrens** (Tax Contest) sowie Mitwirkungs- und Informationspflichten. Vgl. `/steuerrecht:aussenpruefung-betriebspruefung`.

**W&I-Versicherung:** Deckt Garantieverstöße gegenüber dem Käufer (Buy-side-Police) und ermöglicht einen faktisch haftungsfreien Exit — praktisch der Regelfall bei Private-Equity-Verkäufern. Zu beachten: Die Police deckt **keine bekannten Risiken** (dafür Freistellung oder Kaufpreisabschlag), keine Arglist des Versicherten und regelmäßig weder Übertragungspreise noch Altlasten; Deckungsausschlüsse und Selbstbehalt müssen zum Basket des SPA **passen**, sonst entsteht eine Deckungslücke zwischen Vertrag und Police.

## Quellen

### Statute

- [§ 311 BGB](https://www.gesetze-im-internet.de/bgb/__311.html) (Abs. 1 rechtsgeschäftliches Schuldverhältnis — Grundlage der selbständigen Garantie)
- [§ 443 BGB](https://www.gesetze-im-internet.de/bgb/__443.html) (Beschaffenheitsgarantie — bewusst **nicht** einschlägig), [§ 434 BGB](https://www.gesetze-im-internet.de/bgb/__434.html)
- [§ 442 BGB](https://www.gesetze-im-internet.de/bgb/__442.html) (Kenntnis des Käufers), [§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html) (Arglist, Beschaffenheitsgarantie)
- [§ 276 BGB](https://www.gesetze-im-internet.de/bgb/__276.html) (Abs. 3 Vorsatzhaftung nicht abdingbar), [§ 249 BGB](https://www.gesetze-im-internet.de/bgb/__249.html), [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html), [§ 202 BGB](https://www.gesetze-im-internet.de/bgb/__202.html) (Grenzen vertraglicher Verjährungsvereinbarungen)
- [§ 30 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__30.html), [§ 31 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__31.html) (Kapitalerhaltung)

### Kommentare

- Weidenkaff, in: Grüneberg, BGB, 83. Aufl. 2024, § 444 Rn. 1 ff.; § 442 Rn. 1 ff. `[unverifiziert - Auflagenstand prüfen]`
- Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 20 ff. (Unternehmenskauf, selbständige Garantien)
- Beisel/Klumpp, Der Unternehmenskauf, 8. Aufl. 2022, Kap. 16 (Garantien und Haftungsbegrenzung) `[unverifiziert - Auflagenstand prüfen]`

### Rechtsprechung

- BGH, Urt. v. 27.03.2009 – V ZR 30/08 (Reichweite des § 444 BGB, Arglist und Haftungsausschluss) `[unverifiziert - prüfen]`

> Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen dieses Skills folgen aus §§ 311, 442, 444 BGB und der Kommentarliteratur zum Unternehmenskauf.

## Ausgabeformat

```
GARANTIEN & FREISTELLUNGEN — <Transaktion> — <Datum>

I.    Rechtsnatur                   [selbständige Garantie § 311 Abs. 1 BGB — klargestellt ✅/❌]
II.   Ausschluss §§ 434 ff. BGB     [vollständig / 🔴 Lücke: <…>]
        Grenze § 444 BGB:           [Arglistvorbehalt ausdrücklich ✅/❌]
        Grenze § 276 Abs. 3 BGB:    [Vorsatzvorbehalt ✅/❌]
III.  Garantiekatalog
        A Fundamental               [Ziff. <…> — Cap: <…>, Verjährung: <…>]
        B Legal/Operational         [Ziff. <…> — Cap: <…>, Verjährung: <…>]
        C Financial                 [Ziff. <…>]
        D Tax                       [Ziff. <…> — Verjährung an Festsetzungsverjährung]
        Wissensqualifikationen:     [Personenkreis definiert ✅/❌]
IV.   Rechtsfolge                   [Geldersatz — Naturalrestitution ausgeschlossen ✅/❌]
V.    Begrenzungen                  De-minimis: <…>
                                    Basket: <…>  [Freibetrag / Freigrenze]
                                    Cap: <…>
                                    Escrow: <Betrag> bis <Datum>
VI.   Kenntnis § 442 BGB            [Pro-Sandbagging / Anti-Sandbagging — Maßstab: <…>]
        Datenraum gesichert:        [✅ / ❌]
VII.  Freistellungen                1. <Sachverhalt> — Cap-frei? [ja/nein]
        Steuerfreistellung:         [Stichtag <…>, Tax Contest geregelt ✅/❌]
VIII. W&I-Versicherung              [vorgesehen / nein — Deckungslücke zum SPA: <…>]
IX.   Fristen                       Rügefrist: <…>   Verjährung je Gruppe: <…>

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Punkte: <Liste>
```

## Risiken / typische Fehler

- **Garantie als Beschaffenheitsgarantie formuliert** — dann greift § 443 BGB samt gesetzlichem Mängelrecht, und § 444 BGB entwertet die vereinbarten Haftungsbegrenzungen.
- **Freibetrag und Freigrenze verwechselt** — beim Tipping Basket schuldet der Verkäufer ab Überschreiten den vollen Betrag ab dem ersten Euro; die wirtschaftliche Differenz zum Deductible ist erheblich.
- **Arglistvorbehalt vergessen** — eine Begrenzung, die dem Wortlaut nach auch Vorsatz und Arglist erfasst, ist insoweit nach §§ 276 Abs. 3, 444 BGB unwirksam und stellt die gesamte Klausel in Frage.
- **Verjährungsfrist kürzer als der erste Bilanzzyklus** — Verstöße in den Financial Warranties werden erst mit dem ersten Jahresabschluss nach Closing sichtbar.
- **Escrow-Laufzeit kürzer als die Verjährung** — die Sicherheit fällt weg, bevor der Anspruch verjährt.
- **Anti-Sandbagging ohne definierten Offenlegungsmaßstab** — der Verkäufer entwertet den Katalog durch Massenupload in den Datenraum; ohne Fair-Disclosure-Standard bleibt nur Streit.
- **W&I-Police nicht mit dem SPA abgestimmt** — abweichende Selbstbehalte, Ausschlüsse für bekannte Risiken und Definitionsunterschiede erzeugen eine Deckungslücke, die niemand trägt.
- **Steuerfreistellung ohne Tax-Contest-Regelung** — der Käufer führt das Verfahren, der Verkäufer zahlt; ohne Mitwirkungs- und Zustimmungsrechte ist das Konfliktprogrammierung.
