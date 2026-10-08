# Diseño interno: /audit — Cuestionario base + Motor de inferencia

> Documento de diseño. No es el SKILL.md final — es la especificación que lo produce.
> Versión: 1.0.0 | 2026-06-02

---

## Fase 1: Las 5 preguntas y su mapa a variables

### Principio de diseño
Cada pregunta extrae el máximo de señal legal con el mínimo de fricción. El orden importa:
primero el dato (define C_base), luego el país (define F_rigor), luego los penalizadores
(consentimiento → infraestructura → estado actual). Así, si el usuario abandona a mitad,
ya tenemos los inputs más importantes.

---

### Pregunta 1 — Datos: ¿qué maneja el sistema?

**Texto de la pregunta:**
> "¿Qué tipos de datos recopila o procesa tu sistema? Describe brevemente
> (ej: email y nombre, historial médico, geolocalización, pagos...)"

**Variable que determina:** `C_base` (puntaje base del dato más sensible)

**Mapa de clasificación:**

| Palabras clave en la respuesta | Categoría | C_base | Flag adicional |
|---|---|---|---|
| diagnóstico, médico, salud, clínico, prescripción, historial clínico, enfermedad, síntoma | Sensible — Salud | 80 | — |
| huella, facial, iris, biometría, reconocimiento, voz (autenticación) | Sensible — Biométrico | 80 | — |
| genético, ADN, genoma | Sensible — Genético | 80 | — |
| menor, niño, infante, escolar, edad < 18, guardería, colegio, jardín | Sensible — Menores | 80 | FLAG_MINORS = true |
| religión, político, sindical, raza, étnico, sexual, orientación, ideología | Sensible — Ideológico | 80 | — |
| antecedentes, judicial, penal, condena, proceso legal | Sensible — Penal | 80 | FLAG_CRIMINAL = true |
| migratorio, refugiado, estatus migratorio | Sensible — Migratorio | 80 | FLAG_EC_ONLY = true |
| crédito, scoring, calificación financiera, bureau | Personal + riesgo financiero | 40 | FLAG_CREDIT = true |
| pago, tarjeta, cuenta bancaria, IBAN, CVV | Personal — Financiero | 40 | FLAG_FINANCIAL = true |
| email, correo, teléfono, celular, nombre, apellido, dirección, IP, cookies, geolocalización, GPS, device ID, CURP, cédula, CPF, RUT | Personal General | 40 | — |
| nombre empresa, NIT, razón social, registro mercantil, estadísticas agregadas | Público | 10 | — |

**Regla de tiebreak:** Si hay múltiples categorías, usar siempre la de mayor puntaje.
Si hay datos de salud Y email → C_base = 80 (salud domina).

---

### Pregunta 2 — Países: ¿dónde opera?

**Texto de la pregunta:**
> "¿En qué países opera actualmente o planeas operar?"

**Variable que determina:** `F_rigor` + conjunto de leyes aplicables

**Mapa de F_rigor:**

| Respuesta contiene | F_rigor | Leyes que se activan |
|---|---|---|
| Brasil / Brazil / BR / LGPD | 1.25 | LGPD — activa: DPO obligatorio, base legal por finalidad, portabilidad |
| Ecuador / EC / LOPDP | 1.25 | LOPDP — activa: situación migratoria como sensible, portabilidad |
| Europa / EU / GDPR / Unión Europea / España / Francia / Alemania / (cualquier país UE) | 1.25 | GDPR — activa: DPO condicional, SCCs para transferencias, 72h breach |
| Colombia / CO | 1.00 | Ley 1581 — ARCO, aviso de privacidad, SIC |
| México / MX | 1.00 | LFPDPPP 2025 — ARCO, aviso de privacidad, autoridad: SABG (ex-INAI) |
| Chile / CL | 1.00 | Ley 19.628 → reformada por Ley 21.719 (vigencia 01-12-2026, APDP) |
| Argentina / AR | 1.00 | Ley 25.326 |
| Perú / PE | 1.00 | Ley 29733 |

**Regla:** Si hay al menos un país con F_rigor = 1.25, usar 1.25 para todo el cálculo.
Documentar en el output qué ley activa el multiplicador.

**Flag especial:** Si menciona "Estados Unidos" / "EE.UU." / "California" como mercado
(no solo como servidor) → activar FLAG_CCPA = true → mencionarlo en el output.

---

### Pregunta 3 — Consentimiento: ¿cómo autoriza el usuario?

**Texto de la pregunta:**
> "¿Cómo obtiene la autorización de sus usuarios? Por ejemplo: ¿tienen un solo
> 'Acepto los términos', checkboxes individuales por uso, o aún no lo han definido?"

**Variable que determina:** penalizador de consentimiento (+15 si aplica)

**Mapa:**

| Respuesta | Penalizador | Nota para output |
|---|---|---|
| "no tenemos" / "no lo hemos definido" / "pendiente" | +15 | Sin mecanismo de consentimiento |
| "un solo acepto" / "checkbox único" / "términos y condiciones" / "acepto todo" | +15 | Consentimiento no granular |
| "toggles por finalidad" / "granular" / "uno por cada uso" / "opt-in por categoría" | +0 | Consentimiento adecuado |
| No menciona / no está claro | +15 | Asumir no granular — indicarlo como supuesto en el output |

---

### Pregunta 4 — Infraestructura y terceros

**Texto de la pregunta:**
> "¿Dónde están sus servidores y usan algún servicio externo?
> (ej: AWS, Firebase, GCP, Mixpanel, HubSpot, Stripe, Google Analytics...)"

**Variable que determina:** penalizadores de servidores (+20) y transferencia a terceros (+15)

**Mapa de servidores:**

| Respuesta contiene | Inferencia | Penalizador |
|---|---|---|
| Firebase (sin región especificada) | Servidores en EE.UU. (us-central1 por defecto) | +20 salvo que mencionen SCCs con Google |
| AWS (sin región) | Preguntar región O asumir us-east-1 y marcar como supuesto | +20 (supuesto) |
| AWS sa-east-1 / South America | Servidores en Brasil | +0 |
| GCP southamerica-east1 | Servidores en Brasil | +0 |
| AWS eu-west / GCP europe | Servidores en UE — adecuado para GDPR | +0 (pero ojo transferencia de vuelta a LATAM) |
| Heroku / Railway / Render (sin región) | Servidores en EE.UU. por defecto | +20 (supuesto) |
| Servidores propios en [país LATAM] | En jurisdicción del usuario | +0 |
| No mencionan servidores | Asumir cloud internacional → +20 marcado como supuesto | +20 |

**Mapa de terceros:**

| Servicio mencionado | Inferencia | Penalizador |
|---|---|---|
| Mixpanel, Amplitude, Segment | Transferencia de datos de comportamiento a EE.UU. | +15 si no mencionan DPA |
| Google Analytics (GA4) | Transferencia + posiblemente sin consentimiento de cookies | +15 + flag de cookies |
| HubSpot, Salesforce, Pipedrive | Transferencia de datos de contacto a EE.UU. | +15 si no mencionan DPA |
| Stripe, Conekta, Kushki | Transferencia de datos financieros — PCI DSS aplica | +15 + flag financiero |
| Twilio, SendGrid | Transferencia de email/teléfono — verificar DPA | +15 si no mencionan DPA |
| Login con Google / Facebook / Apple | Transferencia de perfil del usuario a tercero | +15 si no mencionan DPA |
| No mencionan terceros | Sin penalizador de transferencia | +0 |

**Regla:** Si mencionan terceros pero también dicen "tenemos DPA firmados" o "cláusulas contractuales",
eliminar el penalizador +15 de transferencia.

---

### Pregunta 5 — Estado de cumplimiento actual

**Texto de la pregunta:**
> "¿Ya cuentan con alguno de estos? (pueden marcar los que sí tienen):
> ① Política de privacidad publicada  ② Canal para solicitudes de datos (ARCO)
> ③ Contratos firmados con proveedores  ④ Plan de respuesta ante brechas de seguridad"

**Variable que determina:** penalizadores de cumplimiento (hasta +45 pts si ninguno existe)

**Mapa:**

| Ítem | Ausente → penalizador | Presente → sin penalizador |
|---|---|---|
| ① Política de privacidad | +10 | +0 |
| ② Canal ARCO / ARSOP | +10 | +0 |
| ③ Contratos con proveedores (DPA) | +15 (transferencia sin garantías) | Eliminar penalizador de Q4 si ya lo cubre |
| ④ Plan de respuesta a brechas | +15 (aplica si BR, EC o GDPR) / flag si otros | +0 |

**Nota:** El ítem ④ solo genera penalizador si F_rigor = 1.25 (Brasil, Ecuador, GDPR).
Para regímenes LATAM estándar, se menciona como recomendación pero no suma puntos.

---

## Fase 2: Motor de inferencia automática

### Principio
Si el usuario describe su proyecto en una sola oración, el motor debe extraer suficiente
información para calcular un score sin hacer todas las preguntas. Preguntar solo lo que
no pueda inferirse con razonable certeza.

### Tabla maestra de inferencias por dominio

| Dominio / vertical mencionada | Inferencias automáticas | Preguntas que se omiten |
|---|---|---|
| "telemedicina" / "app de salud" / "historial médico" | C_base = 80 (salud) + posible FLAG_MINORS si hay pediatría | Q1 (dato ya conocido) |
| "plataforma educativa" / "edtech" / "app para colegios" | FLAG_MINORS = true + C_base mínimo 40 | Parte de Q1 |
| "fintech" / "app de crédito" / "scoring financiero" | FLAG_CREDIT = true + C_base = 40 + FLAG_FINANCIAL | Parte de Q1 |
| "e-commerce" / "tienda online" | C_base = 40 (email, dirección, pago) + FLAG_FINANCIAL | Parte de Q1 |
| "HR" / "nómina" / "recursos humanos" | C_base = 40-80 (datos laborales, posible salud laboral) | Parte de Q1 |
| "Firebase" sin región | Servidores en EE.UU. → penalizador +20 (supuesto) | Parte de Q4 |
| "early-stage" / "MVP" / "recién lanzamos" | Probablemente sin política ni ARCO → marcar como supuesto | Parte de Q5 |
| "startup" sin más contexto | Preguntar Q5 con énfasis — alta probabilidad de ausencia de cumplimiento | — |

### Regla de supuestos
Cuando se infiere algo que no fue confirmado explícitamente, el output debe marcarlo:
> ⚠️ *Supuesto: servidores en EE.UU. (inferido por uso de Firebase sin región especificada).
> Si están en sa-east-1, el penalizador de +20 no aplica.*

Esto mantiene la transparencia y permite al usuario corregir sin rehacer todo el análisis.

---

## Fase 3: Diseño del output unificado

### Principios
- Máximo 400 tokens de output
- Máximo 3 hallazgos (los de mayor impacto en el score)
- Máximo 2 acciones inmediatas (la más urgente y la segunda más urgente)
- Siempre mostrar el desglose del cálculo (C_base + penalizadores + F_rigor)
- Supuestos marcados explícitamente si los hay
- Rutas opcionales al final — no como parte del análisis principal

### Formato aprobado

```
╔══════════════════════════════════════════════════════╗
║         🔍 Privacy Compliance Skills — Auditoría Rápida       ║
╠══════════════════════════════════════════════════════╣
║  [Proyecto]  |  [País(es)]                           ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║              [SCORE] / 100    [CARA EMOJI]           ║
║                  [🟢 BAJO / 🟡 MEDIO / 🔴 ALTO]      ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  Cálculo: [C_base] + [Σ penalizadores] × [F_rigor]  ║
╠══════════════════════════════════════════════════════╣
║  Top hallazgos:                                      ║
║  🔴 [hallazgo crítico #1]               +XX pts      ║
║  🟡 [hallazgo importante #2]            +XX pts      ║
║  🟡 [hallazgo importante #3]            +XX pts      ║
╠══════════════════════════════════════════════════════╣
║  Acción esta semana:                                 ║
║    → [acción #1 concreta y específica]               ║
║  Antes de lanzar:                                    ║
║    → [acción #2 concreta y específica]               ║
╚══════════════════════════════════════════════════════╝
[Supuestos aplicados, si los hay — fuera del box, en cursiva]
[Escalamiento legal si score ≥ 71 — fuera del box]
[Disclaimer — una línea]
[Rutas opcionales — una línea por skill]
```

### Reglas de priorización de hallazgos
Ordenar penalizadores de mayor a menor impacto en puntos. En caso de empate, priorizar:
1. Menores de edad (riesgo reputacional y legal más alto)
2. Datos sensibles sin base legal
3. Servidores sin garantías (riesgo de transferencia internacional)
4. Sin política de privacidad
5. Sin canal ARCO

### Rutas opcionales (siempre al final, nunca dentro del box)
```
¿Necesitas más detalle?
→ /clasificar-datos [campo] --pais [XX]  — para analizar un campo específico
→ /privacy-check [endpoint o código]    — para auditar implementación técnica
→ /derechos-usuario --pais [XX]         — para implementar el canal ARCO
→ /matriz-normativa [dimensión]         — para comparar leyes entre países
```
