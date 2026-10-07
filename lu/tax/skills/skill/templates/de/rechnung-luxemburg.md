{{ verkaeufer.name }}
{{ verkaeufer.adresse }}
RCS Luxembourg: {{ verkaeufer.rcs }}
USt-IdNr.: {{ verkaeufer.ust_id }}
{% if verkaeufer.autorisation %}Geschäftsgenehmigung Nr.: {{ verkaeufer.autorisation }}{% endif %}

# RECHNUNG Nr. {{ rechnung.nummer }}

**Rechnungsdatum:** {{ rechnung.datum }}
**Lieferdatum/-zeitraum:** {{ rechnung.leistungsdatum }}
**Fälligkeitsdatum:** {{ rechnung.faellig_am }}

## Rechnungsempfänger

{{ kaeufer.name }}
{{ kaeufer.adresse }}
{% if kaeufer.ust_id %}USt-IdNr.: {{ kaeufer.ust_id }}{% endif %}

## Positionen

| # | Bezeichnung | Menge | Einzelpreis HT | MwSt-Satz | Gesamt HT |
|---|---|---:|---:|---:|---:|
{% for p in positionen %}
| {{ loop.index }} | {{ p.bezeichnung }} | {{ p.menge }} | {{ p.einzelpreis }} EUR | {{ p.mwst_satz }} % | {{ p.gesamt_ht }} EUR |
{% endfor %}

## Zusammenfassung

| | Betrag |
|---|---:|
| Gesamtbetrag HT | **{{ summe.netto }} EUR** |
| MwSt {{ summe.mwst_satz_dominant }} % | {{ summe.mwst_betrag }} EUR |
| **Gesamtbetrag TTC** | **{{ summe.brutto }} EUR** |

{% if mwst_befreit %}
**MwSt-befreite Lieferung** gemäß Artikel {{ mwst_befreiungsartikel }} des luxemburgischen Mehrwertsteuergesetzes. Keine Mehrwertsteuer ausgewiesen.
{% endif %}

{% if reverse_charge %}
**Steuerschuldnerschaft des Leistungsempfängers (Reverse Charge)** gemäß Artikel 196 der Richtlinie 2006/112/EG bzw. Artikel 17 Abs. 1 des luxemburgischen Mehrwertsteuergesetzes. Die Mehrwertsteuer ist vom Empfänger zu entrichten.
{% endif %}

## Zahlungsbedingungen

Bitte überweisen Sie den Gesamtbetrag bis zum **{{ rechnung.faellig_am }}** auf folgendes Konto:

- Bank: {{ verkaeufer.bank }}
- IBAN: **{{ verkaeufer.iban }}**
- BIC: {{ verkaeufer.bic }}
- Verwendungszweck: Rechnung {{ rechnung.nummer }}

Bei Zahlungsverzug fallen gesetzliche Verzugszinsen in Höhe von {{ verzugszins | default('8') }} % p. a. sowie eine Beitreibungsentschädigung von 40 EUR an (Gesetz vom 18. April 2004).

---

Vielen Dank für Ihren Auftrag.
