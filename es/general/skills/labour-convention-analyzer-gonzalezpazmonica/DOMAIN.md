# DOMAIN.md — labour-convention-analyzer
# Estructura y análisis de convenios colectivos (España)

## Estructura tipo de un convenio colectivo

### Partes del convenio

```
1. Identificación de las partes — representación empresarial y sindical firmante
2. Ámbito de aplicación
   - Funcional: actividades y empresas incluidas (código CNAE)
   - Personal: trabajadores incluidos y excluidos
   - Territorial: estatal / autonómico / provincial / empresa
   - Temporal: vigencia (fecha inicio → fin) y condiciones de prórroga
3. Vigencia y denuncia — procedimiento y plazos para revisar el convenio
4. Clasificación profesional — grupos, categorías y niveles
5. Estructura salarial — salario base, complementos, tablas por categoría
6. Jornada y horario — horas anuales, distribución, horas extraordinarias
7. Permisos y licencias — días retribuidos por causa (art. 37 ET como mínimo)
8. Régimen disciplinario — tipificación de faltas y sanciones por nivel
9. Derechos sindicales — crédito horario, tablones, locales
10. Comisión Paritaria — composición, funciones, plazos de resolución
```

## Prioridad aplicativa (jerarquía normativa)

### Regla general

```
Estatuto de los Trabajadores (ET)
        ↓  (norma mínima — el convenio puede mejorar pero no empeorar)
Convenio colectivo sectorial estatal
        ↓  (unidad de negociación superior)
Convenio colectivo sectorial autonómico / provincial
        ↓  (unidad de negociación inferior)
Convenio colectivo de empresa
        ↓  (norma más cercana al trabajador)
Contrato individual de trabajo
```

### Excepción post-2012 (art. 84.2 ET — Reforma Laboral)

El convenio de empresa PREVALECE sobre el sectorial en las siguientes materias,
aunque el sectorial sea más favorable para el trabajador:

| Materia | Prevalencia empresa |
|---|---|
| Salario base y complementos salariales | Sí |
| Abono o compensación de horas extra | Sí |
| Horario y distribución del tiempo de trabajo | Sí |
| Régimen de trabajo a turnos | Sí |
| Sistema de clasificación profesional | Sí |
| Modalidades de contratación | Sí |
| Medidas para favorecer la conciliación | Sí |

**Excepción a la excepción**: El convenio sectorial puede prohibir expresamente
la inaplicación del convenio de empresa en estas materias.

### Cláusula de inaplicación (descuelgue — art. 82.3 ET)

En situaciones de crisis económica documentada, la empresa puede inaplicar
las condiciones del convenio sectorial previa negociación con los representantes
y, si no hay acuerdo, con sometimiento a la Comisión Consultiva Nacional.

## Interpretación de artículos

### Criterios de interpretación laboral (en orden)

1. **Sentido propio de las palabras** — literalidad del texto
2. **Contexto del artículo** — en relación con el resto del convenio
3. **Antecedentes** — actas de la negociación (si están disponibles)
4. **Criterio de la Comisión Paritaria** — si existe resolución previa
5. **Jurisprudencia del TS/TSJ** — sentencias sobre el mismo convenio o cláusula similar
6. **Principio pro-operario** — en caso de duda sobre norma más favorable al trabajador

### Señales de ambigüedad que requieren criterio jurídico

- Artículos con redacción diferente a la ET que podrían contradecirla
- Cláusulas con condiciones suspensivas o resolutorias no desarrolladas
- Referencias a "acuerdo de las partes" sin procedimiento definido
- Remisiones a anexos o protocolos no incluidos en el texto publicado en BOE

## Consulta al BOE para convenios vigentes

### Procedimiento de verificación

1. Acceder a `https://www.boe.es/buscar/act.php` o buscador de disposiciones
2. Buscar por: título del convenio + año + ámbito
3. Verificar: código de convenio en el registro (REGCON) — `https://expinterweb.mites.gob.es/regcon/`
4. Confirmar vigencia: comprobar si hay denuncias o nuevos convenios publicados después

### Alertas de desactualización a emitir

```
ALERTA DE VIGENCIA: Este convenio tenía vigencia hasta [FECHA].
No se ha podido verificar si ha sido renovado o sustituido.
Consulte el REGCON (Ministerio de Trabajo) o el BOE para confirmar
que está aplicando la versión vigente antes de tomar decisiones.
```

## Régimen disciplinario en el convenio

### Estructura típica

Los convenios tipifican las faltas en tres niveles (coherente con art. 58 ET):

| Nivel | Ejemplos frecuentes en convenios | Sanciones habituales |
|---|---|---|
| Leve | Impuntualidad aislada, descuido en apariencia | Amonestación verbal o escrita |
| Grave | Acumulación de faltas leves, desobediencia puntual | Suspensión 1-10 días |
| Muy grave | Fraude, acoso, embriaguez habitual, faltas leves reiteradas | Suspensión >10 días / despido |

**Principio de proporcionalidad**: La sanción debe guardar proporción con la gravedad
de la falta. Sancionar una falta leve como muy grave es impugnable.

## Tablas salariales y SMI

- Las tablas del convenio fijan el salario mínimo para cada categoría
- El SMI vigente es el **límite absoluto infranqueable** — ningún salario puede estar por debajo
- Si la tabla del convenio queda por debajo del SMI: prevalece el SMI (art. 27 ET)
- Las tablas se actualizan normalmente por comisión paritaria y publicación en BOE

## Permisos retribuidos (art. 37 ET — mínimos legales)

| Permiso | Días ET (mínimo) |
|---|---|
| Matrimonio o pareja de hecho (si equipara convenio) | 15 días |
| Nacimiento / adopción | 2 días (ampliados por convenio frecuentemente) |
| Fallecimiento familiar 1º grado | 2-4 días (según distancia) |
| Traslado domicilio | 1 día |
| Deberes inexcusables (jurado, tribunal, etc.) | Tiempo necesario |
| Exámenes prenatales y técnicas de preparación al parto | Tiempo necesario |
