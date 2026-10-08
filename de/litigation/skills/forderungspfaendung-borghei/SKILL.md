---
name: forderungspfaendung-borghei
title: /zwangsvollstreckung:forderungspfaendung
description: Pfändung und Überweisung von Geldforderungen – Pfändungs- und Überweisungsbeschluss §§ 829, 835 ZPO, Zustellung an Drittschuldner und Schuldner, Drittschuldnererklärung § 840 ZPO, Pfändungsschutz für Arbeitseinkommen § 850c ZPO nebst der jährlichen Pfändungsfreigrenzenbekanntmachung, unpfändbare und bedingt pfändbare Bezüge §§ 850a, 850b ZPO, Zusammenrechnung mehrerer Einkommen § 850e ZPO, Pfändungsschutzkonto §§ 850k, 850l ZPO sowie Vorpfändung § 845 ZPO. Use when eine Konto-, Lohn- oder sonstige Forderungspfändung beantragt, eine Drittschuldnererklärung abgegeben oder der Pfändungsschutz eines Schuldners geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/zwangsvollstreckung/skills/forderungspfaendung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /zwangsvollstreckung:forderungspfaendung

## Zweck

Die Forderungspfändung ist der wirksamste Zugriff der Zwangsvollstreckung: Sie greift nicht auf Gegenstände zu, deren Verwertung Zeit kostet, sondern unmittelbar auf Geld — Konto, Lohn, Steuererstattung, Mietforderung. Ihre Kehrseite ist ein dichtes Netz von Schutzvorschriften, das das Existenzminimum des Schuldners sichert und dessen Verletzung die Pfändung angreifbar macht. Dieser Skill formuliert den Pfändungs- und Überweisungsbeschluss, führt den Drittschuldner durch seine Erklärungspflicht und prüft den Pfändungsschutz auf Schuldnerseite.

## Eingaben

- **Titel, Klausel, Zustellung** — geprüft nach `/zwangsvollstreckung:vollstreckungsvoraussetzungen`
- **Forderungsaufstellung**: Hauptforderung, titulierte Zinsen, Vollstreckungskosten, bereits erlangte Teilbeträge
- **Drittschuldner**: Arbeitgeber, Kreditinstitut, Finanzamt, Mieter, Versicherer — mit vollständiger Anschrift
- **Art der zu pfändenden Forderung**: Arbeitseinkommen, Kontoguthaben, Steuererstattung, Mietzins, Herausgabeanspruch
- Auf Schuldnerseite: **Nettoeinkommen**, Zahl der **Unterhaltsberechtigten**, Sonderzahlungen, Naturalleistungen
- Besteht bereits ein **Pfändungsschutzkonto (P-Konto)**? Seit wann, mit welchen Bescheinigungen?
- Vorrangige Pfändungen, Abtretungen oder Lohnpfändungen anderer Gläubiger
- Bei Unterhaltsvollstreckung: Titel und Rangverhältnis (§ 850d ZPO)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft §§ 828–863 ZPO mit URL, die aktuelle Pfändungsfreigrenzenbekanntmachung und Kommentarstellen (Zöller, Musielak/Voit, Stöber Forderungspfändung).
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt den PfÜB-Antrag, die Drittschuldnererklärung oder den Schutzantrag.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Bestimmtheit der gepfändeten Forderung, Zustellungsreihenfolge, Freigrenzen und Rangfragen.

## Ablauf

### 1. Pfändungs- und Überweisungsbeschluss ([§ 829 ZPO](https://www.gesetze-im-internet.de/zpo/__829.html), [§ 835 ZPO](https://www.gesetze-im-internet.de/zpo/__835.html))

Das **Vollstreckungsgericht** — das Amtsgericht des Schuldnerwohnsitzes ([§ 828 ZPO](https://www.gesetze-im-internet.de/zpo/__828.html)) — pfändet die Geldforderung durch Beschluss. Der Beschluss enthält zwei Verbote:

- an den **Drittschuldner**, an den Schuldner zu zahlen (**arrestatorium**),
- an den **Schuldner**, über die Forderung zu verfügen und sie einzuziehen (**inhibitorium**).

Die Pfändung wird mit der **Zustellung an den Drittschuldner** wirksam (§ 829 Abs. 3 ZPO) — nicht mit dem Erlass und nicht mit der Zustellung an den Schuldner. Dieser Zeitpunkt entscheidet über den **Rang** gegenüber konkurrierenden Gläubigern (Prioritätsprinzip). Die Zustellung an den Schuldner erfolgt nachrichtlich.

Mit der **Überweisung** nach § 835 ZPO erhält der Gläubiger die Einziehungsbefugnis; Regelfall ist die Überweisung **zur Einziehung**, nicht an Zahlungs statt. Er kann dann im eigenen Namen gegen den Drittschuldner klagen. Der Antrag ist **formulargebunden**; die gepfändete Forderung muss so **bestimmt** bezeichnet sein, dass der Drittschuldner ohne Weiteres erkennen kann, was gepfändet ist.

### 2. Vorpfändung ([§ 845 ZPO](https://www.gesetze-im-internet.de/zpo/__845.html))

Weil zwischen Antrag und Zustellung des PfÜB Tage bis Wochen liegen, sichert die **Vorpfändung** den Rang: Der Gläubiger lässt dem Drittschuldner durch den Gerichtsvollzieher die Benachrichtigung zustellen, dass die Pfändung bevorsteht, verbunden mit der Aufforderung, nicht an den Schuldner zu zahlen. Sie wirkt wie ein **Arrest** und begründet den Rang bereits mit ihrer Zustellung — allerdings nur, wenn die **Pfändung binnen eines Monats** folgt (§ 845 Abs. 2 ZPO). Wird die Frist versäumt, entfällt die Wirkung rückwirkend. Die Vorpfändung setzt Titel und Klausel voraus, aber noch keinen Beschluss.

### 3. Drittschuldnererklärung ([§ 840 ZPO](https://www.gesetze-im-internet.de/zpo/__840.html))

Auf Verlangen des Gläubigers hat der Drittschuldner binnen **zwei Wochen** ab Zustellung des Pfändungsbeschlusses zu erklären:

1. ob und inwieweit er die Forderung als **begründet anerkennt** und Zahlung zu leisten bereit ist,
2. ob und welche **Ansprüche andere Personen** an die Forderung erheben,
3. ob und wegen welcher Ansprüche die Forderung bereits für **andere Gläubiger gepfändet** ist,
4. bei Arbeitseinkommen zusätzlich Angaben zur Art des Beschäftigungsverhältnisses.

Die Aufforderung muss im Pfändungsbeschluss enthalten sein. Die Erklärung ist **keine Anerkenntnis** und begründet keine eigene Zahlungspflicht; wer sie aber schuldhaft nicht, verspätet oder unrichtig abgibt, haftet dem Gläubiger auf **Schadensersatz** (§ 840 Abs. 2 S. 2 ZPO). Für Kreditinstitute und Arbeitgeber ist das die häufigste Haftungsquelle im Vollstreckungsrecht.

### 4. Pfändungsschutz für Arbeitseinkommen ([§ 850c ZPO](https://www.gesetze-im-internet.de/zpo/__850c.html))

Arbeitseinkommen ist nur pfändbar, soweit es die Beträge des § 850c ZPO übersteigt. Die Systematik:

- Ein **unpfändbarer Grundbetrag** je Monat, Woche und Tag,
- **Erhöhungsbeträge** für jede Person, der der Schuldner kraft Gesetzes Unterhalt gewährt (gestaffelt für die erste und für die zweite bis fünfte Person),
- oberhalb des Grundbetrags eine **Teilpfändung** in Stufen, bis ab einer Obergrenze der übersteigende Betrag voll pfändbar ist,
- die Beträge werden nach § 850c Abs. 4 ZPO **jährlich zum 1. Juli** an die Entwicklung des Grundfreibetrags angepasst und im Bundesgesetzblatt als **Pfändungsfreigrenzenbekanntmachung** veröffentlicht; die dazu ergehende **Pfändungstabelle** ist verbindliche Berechnungsgrundlage.

> **Nicht mit dem Rechner berechnen.** Die Tabelle des § 850c ZPO ist in `scripts/legal_calc/` **nicht implementiert**, und ihre Werte ändern sich jährlich. Jede modellseitig „errechnete" Freigrenze wäre eine Erfindung. Maßgeblich ist ausschließlich die **aktuelle Pfändungsfreigrenzenbekanntmachung** und die zugehörige Tabelle; der pfändbare Betrag ist dort abzulesen und mit dem Datum der Fassung zu dokumentieren.

Für **Unterhaltsforderungen** gilt der erweiterte Zugriff des [§ 850d ZPO](https://www.gesetze-im-internet.de/zpo/__850d.html): Das Vollstreckungsgericht belässt dem Schuldner nur den notwendigen Unterhalt; die Freigrenzen des § 850c ZPO gelten dort nicht.

### 5. Unpfändbare und bedingt pfändbare Bezüge ([§ 850a ZPO](https://www.gesetze-im-internet.de/zpo/__850a.html), [§ 850b ZPO](https://www.gesetze-im-internet.de/zpo/__850b.html))

**Unpfändbar nach § 850a ZPO** sind unter anderem: die Hälfte der für Mehrarbeit gezahlten Vergütung, Urlaubsgeld im Rahmen des Üblichen, Zuwendungen aus Anlass eines besonderen Betriebsereignisses im Rahmen des Üblichen, Aufwandsentschädigungen, Auslösungsgelder und Gefahrenzulagen, **Weihnachtsvergütungen bis zur Hälfte des monatlichen Arbeitseinkommens** innerhalb eines gesetzlich bestimmten Höchstbetrags, Heirats- und Geburtsbeihilfen, Sterbe- und Gnadenbezüge sowie Blindenzulagen.

**Bedingt pfändbar nach § 850b ZPO** sind unter anderem Renten wegen Körperverletzung, Unterhaltsrenten, Ansprüche aus Lebensversicherungen bis zu bestimmten Grenzen und Bezüge aus Witwen-, Waisen- und Hilfskassen. Sie können nur gepfändet werden, wenn die Vollstreckung in das sonstige Vermögen erfolglos war und die Pfändung nach den Umständen, insbesondere der Art des beizutreibenden Anspruchs, der **Billigkeit** entspricht.

### 6. Zusammenrechnung mehrerer Einkommen ([§ 850e ZPO](https://www.gesetze-im-internet.de/zpo/__850e.html))

Damit der Schuldner den Schutz nicht durch Aufspaltung vervielfacht, ordnet § 850e ZPO an: Unpfändbare Beträge nach § 850a ZPO bleiben außer Ansatz; Naturalleistungen sind mit ihrem Wert dem Geldeinkommen **hinzuzurechnen**; mehrere Arbeitseinkommen sowie Arbeitseinkommen und laufende Geldleistungen nach dem Sozialgesetzbuch werden auf Antrag des Gläubigers vom Vollstreckungsgericht **zusammengerechnet**. Der Freibetrag wird dann in erster Linie dem Haupteinkommen entnommen. Ohne ausdrücklichen Zusammenrechnungsantrag bleibt jedes Einkommen für sich geschützt — ein häufig übersehener Gläubigerfehler.

### 7. Pfändungsschutzkonto ([§ 850k ZPO](https://www.gesetze-im-internet.de/zpo/__850k.html), [§ 850l ZPO](https://www.gesetze-im-internet.de/zpo/__850l.html))

Wird ein Kontoguthaben gepfändet, greift der Kontopfändungsschutz **nicht automatisch**: Der Schuldner muss von seinem Kreditinstitut verlangen, dass sein Zahlungskonto als **Pfändungsschutzkonto (P-Konto)** geführt wird. Auf dem P-Konto ist Guthaben in Höhe des monatlichen **Grundfreibetrags** der Pfändung entzogen; er entspricht dem Grundbetrag des § 850c Abs. 1 ZPO und wird durch dieselbe Bekanntmachung angepasst.

- **Erhöhungsbeträge** für Unterhaltspflichten, einmalige Sozialleistungen, Kindergeld und weitere Zwecke werden durch **Bescheinigung** nachgewiesen (Arbeitgeber, Familienkasse, Sozialleistungsträger, Schuldnerberatungsstelle, Steuerberater) oder auf Antrag vom Vollstreckungsgericht festgesetzt.
- Nicht verbrauchtes geschütztes Guthaben wird in die **Folgemonate übertragen** (Ansparmöglichkeit, § 899 Abs. 2 ZPO in der geltenden Fassung des Pfändungsschutzkonto-Fortentwicklungsgesetzes); es fällt nicht am Monatsende an den Gläubiger.
- Jede Person darf nur **ein** P-Konto führen; Verstöße werden über die SCHUFA-Meldung der Institute erkannt.
- Bei schwankenden Überweisungsbeträgen ist die gerichtliche Festsetzung des Pfändungsfreibetrags an besondere Anforderungen geknüpft (BGH, Beschl. v. 10.11.2011 – VII ZB 64/10 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2011-11-10&Aktenzeichen=VII%20ZB%2064/10).
- Nach § 850l ZPO kann das Vollstreckungsgericht auf Antrag anordnen, dass ein Konto für eine bestimmte Zeit **der Pfändung nicht unterworfen** ist, wenn dem Schuldner überwiegend unpfändbare Beträge zufließen.

Verfahrenshinweis: Umwandlungsverlangen, Bescheinigung und gegebenenfalls der Festsetzungsantrag sind **eilbedürftig** — bis zur Umwandlung bleibt das Guthaben blockiert. Gegen die Freigabeverweigerung des Instituts hilft der Antrag beim Vollstreckungsgericht, nicht die Erinnerung gegen den PfÜB.

## Deterministische Berechnung

Die Höhe der **beizutreibenden Forderung** ist Arithmetik; der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur diese**. Ob Verzug eingetreten ist, ob eine Entgeltforderung vorliegt und ob ein Verbraucher beteiligt ist, bleiben juristische Eingaben; der **Basiszinssatz ist Pflichteingabe** und gegen die Veröffentlichung der Deutschen Bundesbank zu prüfen.

```bash
# Verzugszinsen auf die zugrunde liegende Entgeltforderung
python -m scripts.legal_calc.cli verzugszinsen --betrag 8500 \
    --verzug-ab 01.02.2026 --bis 21.07.2026 --basiszins 01.01.2026:1.10 \
    --entgeltforderung --kein-verbraucher-beteiligt

# Monatsfrist der Vorpfändung § 845 Abs. 2 ZPO
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY

# Zwei-Wochen-Frist der Drittschuldnererklärung § 840 ZPO
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY
```

**Ausdrücklich nicht berechenbar:** die Pfändungsfreigrenzen des § 850c ZPO und der P-Konto-Grundfreibetrag. Die Tabelle ist nicht implementiert, und ihre Werte ändern sich jährlich zum 1. Juli. Der pfändbare Betrag ist der **aktuellen Pfändungsfreigrenzenbekanntmachung** zu entnehmen und mit Fassungsdatum zu dokumentieren.

## Quellen

### Statute

- [§ 828 ZPO](https://www.gesetze-im-internet.de/zpo/__828.html), [§ 829 ZPO](https://www.gesetze-im-internet.de/zpo/__829.html), [§ 835 ZPO](https://www.gesetze-im-internet.de/zpo/__835.html), [§ 836 ZPO](https://www.gesetze-im-internet.de/zpo/__836.html), [§ 840 ZPO](https://www.gesetze-im-internet.de/zpo/__840.html), [§ 845 ZPO](https://www.gesetze-im-internet.de/zpo/__845.html)
- [§ 850 ZPO](https://www.gesetze-im-internet.de/zpo/__850.html), [§ 850a ZPO](https://www.gesetze-im-internet.de/zpo/__850a.html), [§ 850b ZPO](https://www.gesetze-im-internet.de/zpo/__850b.html), [§ 850c ZPO](https://www.gesetze-im-internet.de/zpo/__850c.html), [§ 850d ZPO](https://www.gesetze-im-internet.de/zpo/__850d.html), [§ 850e ZPO](https://www.gesetze-im-internet.de/zpo/__850e.html)
- [§ 850k ZPO](https://www.gesetze-im-internet.de/zpo/__850k.html), [§ 850l ZPO](https://www.gesetze-im-internet.de/zpo/__850l.html), [§ 899 ZPO](https://www.gesetze-im-internet.de/zpo/__899.html) (P-Konto, Übertrag)
- Pfändungsfreigrenzenbekanntmachung nach § 850c Abs. 4 ZPO (jährlich, BGBl.) — jeweils aktuelle Fassung heranziehen

### Kommentare

- Herget, in: Zöller, ZPO, 35. Aufl. 2024, § 829 Rn. 1 ff.; § 850c Rn. 1 ff.
- Stöber/Rellermeyer, Forderungspfändung, 18. Aufl. 2022, Rn. 1 ff.
- Becker, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 840 Rn. 1 ff.
- Kindl/Meller-Hannich, Gesamtes Recht der Zwangsvollstreckung, 4. Aufl. 2021, § 850k ZPO Rn. 1 ff.

### Rechtsprechung

- BGH, Beschl. v. 10.11.2011 – VII ZB 64/10 (Pfändungsschutzkonto; Anforderungen an die gerichtliche Festsetzung des Pfändungsfreibetrags bei schwankenden Überweisungsbeträgen; § 850k ZPO) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2011-11-10&Aktenzeichen=VII%20ZB%2064/10
- Zur Haftung des Drittschuldners nach § 840 Abs. 2 S. 2 ZPO bei unrichtiger oder unterlassener Erklärung ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zur Zusammenrechnung mehrerer Einkommen nach § 850e ZPO ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — PfÜB-Antrag und Drittschuldnererklärung

```
An das Amtsgericht <Ort> — Vollstreckungsgericht —

Antrag auf Erlass eines Pfändungs- und Überweisungsbeschlusses
(§§ 829, 835 ZPO)

Gläubigerin: <…>            Schuldner: <…>, geb. <…>, wohnhaft <…>
Drittschuldnerin: <Arbeitgeberin / Kreditinstitut>, <Anschrift>

Titel: Vollstreckungsbescheid des AG <…> vom <Datum>, Az. <…>, nebst
vollstreckbarer Ausfertigung; zugestellt am <Datum>.

Forderungsaufstellung:
  Hauptforderung                                <Betrag> EUR
  titulierte Zinsen bis <Datum>                 <Betrag> EUR
  festgesetzte Kosten                           <Betrag> EUR
  bisherige Vollstreckungskosten                <Betrag> EUR
  abzüglich Zahlungen                          -<Betrag> EUR
  ------------------------------------------------------------
  Gesamtbetrag                                  <Betrag> EUR

Es wird beantragt, wegen dieser Forderung zu pfänden:

  Anspruch A (Arbeitseinkommen): sämtliche gegenwärtigen und künftigen
  Ansprüche des Schuldners gegen die Drittschuldnerin auf Zahlung von
  Arbeitseinkommen einschließlich aller Nebenbezüge, soweit sie nach
  §§ 850 bis 850i ZPO pfändbar sind;

  Anspruch B (Kontoguthaben): die Ansprüche des Schuldners gegen die
  Drittschuldnerin aus der Kontoverbindung Nr. <…> auf Auszahlung und
  Gutschrift des jeweiligen Guthabens.

Die gepfändeten Forderungen werden der Gläubigerin zur Einziehung
überwiesen (§ 835 Abs. 1 ZPO).

Die Drittschuldnerin wird aufgefordert, binnen zwei Wochen ab Zustellung
die Erklärungen nach § 840 Abs. 1 ZPO abzugeben.
```

```
Drittschuldnererklärung (§ 840 Abs. 1 ZPO)

Zur Pfändung vom <Datum>, zugestellt am <Datum>, Az. <…>, erkläre ich:

1. Die gepfändete Forderung wird dem Grunde nach anerkannt / nicht
   anerkannt, weil <…>. Zahlungsbereitschaft besteht in Höhe des
   pfändbaren Betrags.
2. Ansprüche anderer Personen an der Forderung: <keine / …>.
3. Vorrangige Pfändungen: Pfändung des <Gläubiger> vom <Datum>,
   zugestellt am <Datum>, wegen <Betrag> EUR.
4. Art des Beschäftigungsverhältnisses: unbefristet seit <Datum>,
   Abrechnung monatlich; Nettoeinkommen zuletzt <Betrag> EUR;
   Unterhaltspflichten laut Angaben des Schuldners: <Zahl>.

Der pfändbare Betrag wird nach der zum <Datum> geltenden Fassung der
Pfändungsfreigrenzenbekanntmachung ermittelt und ab <Monat> abgeführt.
```

## Ausgabeformat

```
FORDERUNGSPFÄNDUNG — <Gläubiger / Drittschuldner / Schuldner> — <Datum>

I.    Vollstreckungsvoraussetzungen  Titel/Klausel/Zustellung [✅ / ❌]
                                     s. :vollstreckungsvoraussetzungen
II.   Beizutreibende Forderung       Haupt <…> + Zinsen <…> + Kosten <…>
                                     = <Gesamtbetrag>
III.  Gepfändete Forderung           [Arbeitseinkommen / Konto / sonstige]
      Bestimmtheit                   [✅ / ⚠️]
      Drittschuldner                 <Name, Anschrift>
IV.   Wirksamkeit / Rang             Zustellung an Drittschuldner: <Datum>
      Vorpfändung § 845 ZPO          [N/A / zugestellt <Datum>,
                                      Monatsfrist bis <Datum>]
      Konkurrierende Pfändungen      <Rang, Gläubiger, Datum>
V.    Überweisung § 835 ZPO          [zur Einziehung / an Zahlungs statt]
VI.   Drittschuldnererklärung § 840  Frist bis <Datum>  [offen / abgegeben]
      Haftungsrisiko § 840 II 2      [🟢 / 🔴]
VII.  Pfändungsschutz
      - § 850c ZPO                   Freigrenze aus Bekanntmachung
                                     Fassung vom <Datum>: <Betrag>
                                     (NICHT berechnet — abgelesen)
      - §§ 850a, 850b ZPO            unpfändbare Bestandteile: <…>
      - § 850e ZPO                   Zusammenrechnung [beantragt / nein]
      - § 850d ZPO Unterhalt         [N/A / erweiterter Zugriff]
VIII. P-Konto §§ 850k, 850l ZPO      [kein / seit <Datum>]
      Erhöhungsbescheinigungen       <Aussteller, Betrag>
      Festsetzungsantrag             [N/A / gestellt am <Datum>]
IX.   Zinsen / Fristen               s. Deterministische Berechnung

Ergebnis: <antragsreif / nachbessern / Pfändung angreifbar>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Pfändungsfreigrenze berechnet statt abgelesen** — die Tabelle des § 850c ZPO ist nicht implementiert und ändert sich jährlich zum 1. Juli; jeder modellseitig errechnete Betrag ist eine Erfindung.
- **Rang durch verspätete Zustellung verloren** — die Pfändung wird erst mit Zustellung an den Drittschuldner wirksam; ohne Vorpfändung nach § 845 ZPO geht die Zeit bis dahin zulasten des Gläubigers.
- **Monatsfrist der Vorpfändung versäumt** — folgt die Pfändung nicht binnen eines Monats, entfällt die Rangwirkung rückwirkend.
- **Drittschuldnererklärung unterlassen oder unrichtig** — Arbeitgeber und Kreditinstitute haften nach § 840 Abs. 2 S. 2 ZPO auf Schadensersatz; die Zwei-Wochen-Frist läuft ab Zustellung.
- **Unpfändbare Bezüge mitgepfändet** — Mehrarbeitsvergütung zur Hälfte, Urlaubsgeld, Auslösungen und Gefahrenzulagen sind nach § 850a ZPO herauszurechnen, bevor die Tabelle angewandt wird.
- **Zusammenrechnungsantrag § 850e ZPO vergessen** — ohne ausdrücklichen Antrag bleibt jedes Einkommen für sich geschützt und der Zugriff läuft weitgehend leer.
- **P-Konto nicht rechtzeitig eingerichtet** — der Kontopfändungsschutz greift erst mit der Umwandlung; bis dahin bleibt das Guthaben blockiert, und Erhöhungsbeträge wirken nur mit Bescheinigung.
