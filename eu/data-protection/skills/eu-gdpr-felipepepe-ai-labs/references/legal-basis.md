# Bases Legales — GDPR Art. 6

## Las 6 bases legales

Cada procesamiento de datos DEBE tener una base legal. Ninguna base legal se aplica automáticamente.

### 1. Consentimiento (Art. 6(1)(a))

| Criterio | Requisito |
|------|---------|
| **Libre** | Sin coacción, sin desequilibrio de poder |
| **Específico** | Para cada finalidad separada |
| **Informado** | El interesado sabe qué datos se procesan y para qué |
| **Inequívoco** | Acción afirmativa clara (no silencio, no pre-check) |
| **Retirable** | Mecanismo de retiro tan fácil como dar consentimiento |

```typescript
// ❌ INCORRECTO — No cumple GDPR
<input type="checkbox" checked /> Accept our privacy policy

// ✅ CORRECTO — Cumple GDPR
<input type="checkbox" name="consent" id="consent" />
<label for="consent">He leído y acepto la política de privacidad</label>
<small>
  Tus datos se procesarán para enviar newsletters.
  Puedes retirar tu consentimiento en cualquier momento.
</small>
```

### 2. Ejecución de contrato (Art. 6(1)(b))

Cuando el procesamiento es necesario para cumplir un contrato con el interesado.

**Ejemplos válidos**:
- Almacenar nombre y email para crear una cuenta de usuario
- Procesar datos de facturación para enviar una factura
- Guardar dirección de envío para entregar un pedido

**Ejemplos NO válidos**:
- Marketing (no es necesario para el contrato)
- Analytics (no es necesario para el contrato)
- Compartir datos con terceros (no es necesario para el contrato)

### 3. Obligación legal (Art. 6(1)(c))

Cuando el procesamiento es necesario para cumplir una obligación legal.

**Ejemplos válidos**:
- Guardar datos de empleados para nóminas (ley laboral)
- Reportar transacciones sospechosas (ley antilavado)
- Guardar facturas (ley fiscal — 5+ años en España)

### 4. Interés legítimo (Art. 6(1)(f))

El procesamiento es necesario para un interés legítimo del responsable o de un tercero, siempre que no predominen los derechos del interesado.

**Ejemplos válidos**:
- Log security para prevenir ataques
- Anti-fraud detection en transacciones
- Copias de seguridad de datos de usuarios

**Balance de intereses (test obligatorio)**:
1. ¿Existe un interés legítimo válido?
2. ¿Es necesario el procesamiento para ese interés?
3. ¿Predominan los derechos del interesado?

### 5. Vida del interesado (Art. 6(1)(d))

Para proteger la vida del interesado o de otra persona.

**Solo aplica en urgencias médicas o emergencias**.

### 6. Tarea de interés público (Art. 6(1)(e))

Para una tarea realizada en interés público o en ejercicio de autoridad pública.

**Solo aplica a organismos públicos**.

## Mapeo común

| Caso de uso | Base legal recomendada |
|------|-----|---------|
| Registro de usuario | Contrato (b) |
| Login/autenticación | Contrato (b) |
| Newsletter | Consentimiento (a) |
| Analytics | Consentimiento (a) o interés legítimo (f) |
| Cookies esenciales | Consentimiento (a) o necesario para contrato (b) |
| Cookies de marketing | Consentimiento (a) |
| Email transaccional | Contrato (b) |
| Backups de BD | Interés legítimo (f) |
| Datos de empleados | Obligación legal (c) |
| Datos de clientes (CRM) | Interés legítimo (f) o contrato (b) |
| Datos de menores | Consentimiento + parental |
| Datos de salud | Consentimiento explícito (a) + Art. 9 (2)(a) |
| Biometría | Consentimiento explícito (a) + Art. 9 (2)(a) |

## Consentimiento vs Interés Legítimo

```
¿Es necesario para cumplir el contrato?
  ├── Sí → Interés legítimo (b)
  └── No
      ¿Es un dato sensible (salud, biometría, etc.)?
        ├── Sí → Consentimiento explícito (a) + Art. 9
        └── No
            ¿Puede el interesado oponerse?
              ├── Sí → Interés legítimo (f)
              └── No → Consentimiento (a)
```
