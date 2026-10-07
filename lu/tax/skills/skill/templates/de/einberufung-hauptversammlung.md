{{ gesellschaft.name }}
Aktiengesellschaft mit Sitz in {{ gesellschaft.sitz }}
RCS Luxembourg: {{ gesellschaft.rcs }}

{{ ort }}, den {{ datum }}

# Einberufung der ordentlichen Hauptversammlung

Die Aktionäre der {{ gesellschaft.name }} werden hiermit zur ordentlichen Hauptversammlung eingeladen, die am

**{{ versammlung.datum }} um {{ versammlung.uhrzeit }} Uhr**

am Sitz der Gesellschaft ({{ versammlung.ort }}) stattfindet.

## Tagesordnung

{% for punkt in tagesordnung %}
{{ loop.index }}. {{ punkt }}
{% endfor %}

## Anwesenheits- und Mehrheitsbedingungen

Gemäß Artikel 450-1 ff. des modifizierten Gesetzes vom 10. August 1915 über die Handelsgesellschaften gelten für die ordentliche Hauptversammlung folgende Bedingungen:

- Kein Quorum erforderlich
- Beschlussfassung mit einfacher Mehrheit der abgegebenen Stimmen

## Vertretung

Aktionäre, die persönlich nicht teilnehmen können, haben das Recht, sich durch einen Bevollmächtigten vertreten zu lassen. Die Vollmacht muss spätestens {{ vollmacht_vorlauf_tage | default('5') }} Werktage vor der Versammlung am Sitz der Gesellschaft eingereicht werden.

## Hinterlegung der Aktien

Inhaber von Inhaberaktien werden gebeten, ihre Aktien spätestens {{ aktien_hinterlegung_tage | default('5') }} Werktage vor der Versammlung am Sitz der Gesellschaft oder bei einem zugelassenen Kreditinstitut zu hinterlegen.

Der Verwaltungsrat
{{ gesellschaft.name }}
