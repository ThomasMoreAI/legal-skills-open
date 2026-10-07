{{ gesellschaft.name }}
{{ gesellschaft.rechtsform }} mit Sitz in {{ gesellschaft.sitz }}
RCS Luxembourg: {{ gesellschaft.rcs }}
USt-IdNr.: {{ gesellschaft.ust_id }}

{{ ort }}, den {{ datum }}

An die Gesellschafter der {{ gesellschaft.name }}

# Einladung zur ordentlichen Gesellschafterversammlung

Sehr geehrte Damen und Herren,

hiermit lade ich Sie als {{ einberufender.funktion }} zur ordentlichen Gesellschafterversammlung der {{ gesellschaft.name }} ein. Die Versammlung findet statt am:

**Datum:** {{ versammlung.datum }}
**Uhrzeit:** {{ versammlung.uhrzeit }} Uhr
**Ort:** {{ versammlung.ort }}

## Tagesordnung

{% for punkt in tagesordnung %}
{{ loop.index }}. {{ punkt }}
{% endfor %}

## Hinweise

- Die Bilanz, die Gewinn- und Verlustrechnung sowie der Anhang für das Geschäftsjahr {{ geschaeftsjahr }} können ab dem {{ einsicht_ab }} am Sitz der Gesellschaft eingesehen werden.
- Stimmberechtigt ist jeder Gesellschafter entsprechend seinem Anteil am Stammkapital von {{ stammkapital }} EUR.
- Vertretung ist gemäß Artikel {{ statuten_artikel_vertretung | default('11') }} der Satzung möglich. Eine schriftliche Vollmacht ist mindestens {{ vollmacht_vorlauf_tage | default('3') }} Tage vor der Versammlung am Sitz einzureichen.
- Die Einberufung erfolgt unter Beachtung der Artikel 710-15 und 710-16 des Gesetzes vom 10. August 1915 über die Handelsgesellschaften (modifizierte Fassung).

Mit freundlichen Grüßen

{{ einberufender.name }}
{{ einberufender.funktion }}
{{ gesellschaft.name }}
