# legal-document-drafter — Dominio

## Por qué existe esta skill

La redacción de documentos legales en España requiere conocer estructuras formales, artículos aplicables y convenciones de redacción. Esta skill acelera la generación de borradores estructurados, garantizando que todos los elementos obligatorios estén presentes y los datos pendientes estén claramente marcados.

## Estructura NDA (Acuerdo de Confidencialidad)

### Elementos obligatorios
1. **Identificación de partes** — denominación social, CIF, domicilio, representante legal
2. **Definición de información confidencial** — qué es confidencial y qué queda excluido
3. **Obligaciones del receptor** — estándar de diligencia, restricciones de uso
4. **Exclusiones de confidencialidad**:
   - Información ya en dominio público (sin culpa del receptor)
   - Información conocida previamente (con prueba documental)
   - Información recibida lícitamente de terceros
   - Información requerida por ley o autoridad judicial
5. **Duración** — vigencia del acuerdo + duración de la obligación post-término
6. **Devolución/destrucción** — protocolo al término del acuerdo
7. **Ausencia de licencia** — la información no otorga derechos de PI
8. **Responsabilidad** — consecuencias del incumplimiento (cláusula penal opcional)
9. **Ley aplicable y jurisdicción** — obligatorio en acuerdos internacionales
10. **Firmas** — lugar, fecha, nombre, cargo y rúbrica

### Cláusulas red flag a evitar en NDAs propios
- Reciprocidad sin límite temporal en acuerdos unilaterales
- Definición de confidencialidad sin exclusiones → nulidad potencial
- Renuncia a acciones legales por incumplimiento
- Prohibición de uso de información en contextos no relacionados con la negociación

## Estructura carta de despido disciplinario (art. 54-55 ET)

### Requisitos formales (art. 55 ET)
1. **Forma escrita** — obligatoria, entrega al trabajador con acuse de recibo
2. **Fecha de efectos** — debe ser la misma fecha o posterior a la comunicación
3. **Hechos que motivan el despido** — descripción factual y pormenorizada
4. **Causa legal** — encuadre expreso en art. 54 ET

### Causas del art. 54 ET (taxativas)
- 54.1.a: faltas de asistencia o puntualidad repetidas e injustificadas
- 54.1.b: indisciplina o desobediencia en el trabajo
- 54.1.c: ofensas verbales o físicas al empresario o compañeros
- 54.1.d: transgresión de la buena fe contractual, abuso de confianza
- 54.1.e: disminución continuada y voluntaria en el rendimiento
- 54.1.f: embriaguez habitual o toxicomanía con repercusión en trabajo
- 54.1.g: acoso por razón de origen, religión, discapacidad, edad, orientación sexual, sexo

### Requisitos de validez
- Describir los hechos con precisión (no genérico "mal rendimiento")
- Indicar fechas concretas de los incidentes
- NO mencionar causas no incluidas en art. 54 ET
- Verificar prescripción: faltas muy graves prescriben a los 60 días desde conocimiento empresarial

## Estructura acuerdo de extinción de mutuo acuerdo (art. 49.1.a ET)

1. Identificación de partes
2. Reconocimiento de la relación laboral (fecha inicio, categoría, salario)
3. Causa de extinción: mutuo acuerdo
4. Fecha de extinción
5. **Indemnización pactada** (libre, puede ser 0 o cualquier importe) — [DATO PENDIENTE: importe]
6. Pagos pendientes (liquidación, vacaciones no disfrutadas, pagas extra)
7. **Finiquito** — reconocimiento de no tener reclamaciones pendientes
8. Compromiso de no reclamación judicial (si se pacta)
9. Cláusula de confidencialidad (si aplica)
10. Firmas

### Cautela laboral
- El trabajador puede firmar bajo coerción → recomendable periodo de reflexión y asistencia sindical
- El finiquito firmado no impide acción judicial si hay vicios del consentimiento

## Convenciones de redline (marcado de cambios)

```
[TEXTO ORIGINAL] → [TEXTO PROPUESTO]
Añadir: "[nuevo texto]" después de "..."
Eliminar: la frase "..." en el párrafo X
```

## Marcadores obligatorios

| Marcador | Cuándo usar |
|---|---|
| `[DATO PENDIENTE: descripción]` | Falta dato que el cliente debe proporcionar |
| `[VERIFICAR CON ABOGADO: motivo]` | Punto con criterio jurídico específico necesario |
| `[ACTUALIZAR: referencia normativa]` | Artículo que puede haber sido modificado |
| `[DECISIÓN PENDIENTE: opciones]` | El cliente debe elegir entre alternativas |
