# Data Subject Rights — GDPR Secciones 12-22

Los interesados tienen derechos específicos que el código DEBE soportar técnicamente.

## Los 8 derechos

### 1. Derecho de acceso (Art. 15)

El interesado puede solicitar TODOS sus datos personales.

```typescript
// GET /api/data-subject/access
// Response: all personal data about the user
interface AccessResponse {
  data: PersonalData[];
  purposes: string[];  // why each data point is processed
  retentionPeriods: RetentionPeriod[];
  recipients: string[];  // who has access to the data
  source: string;  // where the data came from
  automatedDecision: boolean;  // if profiling is used
}
```

### 2. Derecho de rectificación (Art. 16)

El interesado puede solicitar corrección de datos inexactos.

```typescript
// PATCH /api/data-subject/rectify
// Must be handled within 1 month
interface RectifyRequest {
  field: string;      // which field to update
  newValue: any;      // what to change it to
}
```

### 3. Derecho al olvido / supresión (Art. 17)

El interesado puede solicitar eliminación de sus datos.

```typescript
// DELETE /api/data-subject/erasure
// Must be completed within 1 month
// Exceptions: legal obligation, public interest, exercise of rights
interface ErasureResponse {
  erasureComplete: boolean;
  exceptions: string[];  // why some data couldn't be deleted
  backupsScheduled: boolean;  // confirm cleanup from backups too
}
```

### 4. Derecho a la limitación del tratamiento (Art. 18)

El interesado puede solicitar que se暂停 el procesamiento de sus datos.

```typescript
// POST /api/data-subject/restrict
// Data must be stored but not processed while restriction is active
interface RestrictionRequest {
  reason: 'accuracy' | 'unlawful' | 'no_longer_needed' | 'objection_pending';
}
```

### 5. Derecho a la portabilidad de datos (Art. 20)

El interesado puede recibir sus datos en formato estructurado, de uso común y lectura mecánica.

```typescript
// GET /api/data-subject/export
// Format: JSON, CSV, or XML (structured, machine-readable)
interface ExportResponse {
  format: 'json' | 'csv' | 'xml';
  data: any;  // all personal data in portable format
  directlyTransferable: boolean;  // can it be sent to another controller?
}
```

### 6. Derecho de oposición (Art. 21)

El interesado puede oponerse al procesamiento de sus datos.

```typescript
// POST /api/data-subject/objection
// Must be stopped immediately unless compelling legitimate grounds
interface ObjectionRequest {
  reason: string;
  processingPurpose: string;  // which purpose they object to
}
```

### 7. Derechos relacionados con decisiones automatizadas (Art. 22)

El interesado tiene derecho a no ser sujeto de decisión automatizada.

```typescript
// If using AI/ML for decisions:
// - Provide human review option
// - Explain the logic involved
// - Allow the user to contest the decision
interface AutomatedDecisionRights {
  humanReviewAvailable: true;
  explanation: string;  // why the decision was made
  contestProcess: string;  // how to contest
}
```

### 8. Derecho a no ser sujeto de decisiones automatizadas

Para perfiles o decisiones automatizadas:
- [ ] Derecho a intervención humana
- [ ] Derecho a expresar su punto de vista
- [ ] Derecho a impugnar la decisión

## Plazos de respuesta

| Derecho | Plazo máximo |
|------|------|
| Acceso | 1 mes (ampliable a 3 si complejo) |
| Rectificación | 1 mes |
| Supresión | 1 mes |
| Limitación | 1 mes |
| Portabilidad | 1 mes |
| Oposición | Inmediato |

## Coste

- **Generalmente gratuito** (Art. 12(5))
- Solo se puede cobrar una tasa razonable si las solicitudes son **manifiestamente infundadas o excesivas** (Art. 12(5))
- Debe proporcionarse evidencia de que la solicitud es excesiva

## Formato de respuesta

- [ ] Gratuito
- [ ] Sin demora indebida (máx. 1 mes)
- [ ] En formato comprensible y accesible
- [ ] Por los mismos medios por los que se solicitó (ej: si por email, responder por email)
