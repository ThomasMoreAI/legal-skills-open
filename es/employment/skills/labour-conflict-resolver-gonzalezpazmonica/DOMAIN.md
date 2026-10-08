# DOMAIN.md — labour-conflict-resolver
# Proceso laboral, costes y estrategia de resolución (España)

## Fases del proceso laboral individual

### Fase 0 — Actuación previa (pre-proceso)

```
Conflicto → Papeleta SMAC (obligatoria en despidos individuales)
         → Suspende plazo de caducidad 20 días hábiles
         → Acto de conciliación ante el SMAC
              ├── Acuerdo → Fin (sin juicio)
              └── Sin acuerdo / Sin avenencia → Apertura plazo judicial
```

### Fase 1 — SMAC (Servicio de Mediación, Arbitraje y Conciliación)

- **Plazo para acudir**: el trabajador debe presentar papeleta antes de que caduque su acción
- **Plazo de caducidad del despido**: 20 días hábiles desde la fecha de efectos del despido
- **Efecto de la papeleta**: suspende el plazo desde su presentación hasta que se celebra el acto
- **Coste**: gratuito para el trabajador; sin representación letrada obligatoria
- **Duración**: el acto se celebra en 15-30 días hábiles (varía por SMAC territorial)

### Fase 2 — Juzgado de lo Social (JS)

- **Plazo para interponer demanda**: 20 días hábiles desde el acto de conciliación sin acuerdo
- **Duración media**: 6-18 meses (varía enormemente por juzgado y CCAA)
- **Coste trabajador**: tarifa fija de abogado + procurador si contratan (no obligatorio)
- **Coste empresa**: honorarios de abogado + riesgo de salarios de tramitación
- **Salarios de tramitación**: si el despido se declara improcedente y la empresa opta por
  readmisión, debe abonar los salarios desde el despido hasta la sentencia

### Fase 3 — Tribunal Superior de Justicia (TSJ)

- **Recurso de suplicación**: cabe contra sentencias del JS en determinadas materias
- **Plazo**: 10 días hábiles desde la notificación para anunciar el recurso
- **Requisito**: depósito de 300 € y consignación de la condena (si la hay)
- **Duración**: 1-3 años adicionales

### Fase 4 — Tribunal Supremo (TS)

- **Recurso de casación para unificación de doctrina**: solo cuando hay contradicción
  entre sentencias de distintos TSJ sobre los mismos supuestos
- **Muy selectivo**: el TS admite un porcentaje muy bajo de recursos

## Cálculo de indemnización por despido

### Despido improcedente (art. 56 ET — desde 12/02/2012)

```
Indemnización = 33 días/año × salario bruto diario × años de antigüedad
                con un máximo de 24 mensualidades

Fórmula concreta:
  salario_diario = salario_bruto_anual / 365
  indemnización = 33 × salario_diario × años_antigüedad
  tope = salario_bruto_mensual × 24

  Si indemnización > tope → aplicar tope

Ejemplo:
  Salario bruto anual: 30.000 €
  Antigüedad: 8 años
  salario_diario = 30.000 / 365 = 82,19 €
  indemnización = 33 × 82,19 × 8 = 21.698 €
  tope = 2.500 × 24 = 60.000 €
  → Indemnización aplicable: 21.698 €
```

### Régimen transitorio (contratos antes de 12/02/2012)

```
Período hasta 11/02/2012: 45 días/año (máx. 42 mensualidades del período anterior)
Período desde 12/02/2012: 33 días/año (máx. 24 mensualidades del período posterior)
La suma de ambos períodos no puede superar 720 días ni 42 mensualidades
```

### Despido objetivo procedente (art. 53 ET)

```
Indemnización = 20 días/año × salario bruto diario × años de antigüedad
                máximo 12 mensualidades
```

### Despido nulo

No hay indemnización — hay readmisión obligatoria + abono de todos los salarios
de tramitación desde la fecha de despido hasta la readmisión efectiva.

## Cuándo negociar vs cuándo litigar

### Señales para negociar (favorecer acuerdo)

- El despido tiene vicios formales claros (hechos vagos, prescripción, falta de audiencia sindical)
- La empresa no tiene documentación sólida de los hechos
- El trabajador es representante sindical (riesgo de nulidad muy alto)
- El coste de un juicio largo supera la indemnización de improcedente
- La relación laboral no tiene retorno posible (readmisión disfuncional)
- Hay urgencia económica para el trabajador

### Señales para litigar

- El acuerdo propuesto es claramente inferior a la indemnización judicial esperada
- Hay cuestiones de principio (nulidad por vulneración de derechos fundamentales)
- La empresa necesita precedente judicial para sentar doctrina interna
- Existen ilegalidades que van más allá de la indemnización (IRPF, SS, acoso)

## Criterios de proporcionalidad en sanciones

El principio de proporcionalidad exige que la sanción sea adecuada a la gravedad
de la falta. Los jueces valoran:

| Factor | Atenúa | Agrava |
|---|---|---|
| Historial disciplinario | Sin antecedentes | Reiteración de faltas similares |
| Antigüedad en la empresa | No es factor de agravar | Puede agravar si supone mayor confianza |
| Intencionalidad | Error no intencional | Fraude o mala fe deliberada |
| Daño causado | Sin consecuencias reales | Daño económico o reputacional concreto |
| Arrepentimiento | Reconocimiento y corrección | Negación de los hechos |

## Ley 3/2004 — Plazos de pago

Relevante cuando el conflicto involucra pagos pendientes a trabajadores o empresas:
- Máximo 60 días naturales para pagos empresa-empresa
- Interés de demora: tipo BCE + 8 puntos porcentuales
- Morosidad permite reclamar costes de cobro (40 € mínimo + daños mayores si se acreditan)

## Plazos críticos de caducidad

| Acción | Plazo |
|---|---|
| Impugnar despido | 20 días hábiles desde efectos del despido |
| Impugnar sanción grave/muy grave | 20 días hábiles desde notificación |
| Reclamar salarios | 1 año desde devengo (prescripción, no caducidad) |
| Reclamar diferencias salariales | 1 año desde que se pudo exigir |
| Impugnar modificación sustancial | 20 días hábiles desde efectos |

**SMAC suspende los plazos de caducidad** (no los de prescripción) desde la
presentación de la papeleta hasta el intento de conciliación.
