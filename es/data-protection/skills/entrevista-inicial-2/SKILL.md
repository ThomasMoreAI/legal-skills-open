---
name: entrevista-inicial-2
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu rol en protección de datos (responsable/encargado/DPD), tus tratamientos principales, tu playbook de encargos de tratamiento, tu proceso de derechos y brechas. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/privacidad/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: en
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — solo recomprobar integraciones. Solo reportar ✓ si una llamada MCP respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego partes específicas).
3. Documentos semilla: política de privacidad, registro de actividades, DPA tipo.
4. Extraer: rol, tratamientos, playbook DPA, proceso ARCO-POL, protocolo de brechas.
5. Migración: si existe CLAUDE.md completo en cache pero no en config, copiar y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`.

---

## Propósito

La privacidad y protección de datos en España se mueve entre el RGPD y la LOPDGDD, entre la AEPD y las autoridades autonómicas, entre el DPD y el responsable del tratamiento. Un DPD in-house de una multinacional tiene necesidades completamente distintas a un abogado de despacho que asesora a pymes sobre RGPD. Esta entrevista descubre tu posición real y construye el perfil que necesitas.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → ofrecer retomar.
- **Contiene `[PLACEHOLDER]` sin pausa** → ofrecer empezar o retomar.
- **Completo** → saltar salvo `--repetir`.

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, confirmar y saltar preguntas de empresa. Si no, hacerlas y escribir el perfil compartido.

## Antes de empezar la entrevista

> **`privacidad` es para quienes trabajan en protección de datos personales — RGPD, LOPDGDD, evaluaciones de impacto, encargos de tratamiento, derechos de los interesados y gestión de brechas.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, si hay DPD nombrado y los tratamientos principales. **15 minutos** añade tu playbook de DPAs, tu proceso de derechos ARCO-POL, tu protocolo de brechas y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de privacidad (rol, tratamientos, playbook de encargos de tratamiento, procesos de derechos y brechas), plantillas de documentos y registro de actividades. Aprende cómo trabajas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas del RGPD, LOPDGDD, directrices EDPB, resoluciones AEPD.

---

## La entrevista

### Apertura

> Voy a aprender cómo gestionas la protección de datos — tu rol, tus tratamientos, tu playbook de DPAs y tu proceso de derechos y brechas — para que cada evaluación, contrato y respuesta que prepare encaje con tu práctica.

**Ruta rápida:** solo Parte 0 y Parte 1 (rol y DPD). Config con `[POR DEFECTO]`.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> 1. **Abogado o profesional jurídico** — abogado de privacidad, DPD, consultor RGPD bajo supervisión.
> 2. **No abogado con acceso a abogado** — DPD no jurista, CISO, compliance officer con abogado accesible.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: herramientas de gestión de privacidad (OneTrust, TrustArc, Nymity), almacenamiento de documentos, herramientas de ticketing (para derechos y brechas) y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho / consultoría de privacidad**
> - **DPD in-house**
> - **In-house (abogado/compliance, sin rol formal de DPD)**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: Rol de la organización (2-3 min)

- **¿La organización actúa como:**
  - **Responsable del tratamiento** (art. 4.7 RGPD)
  - **Encargado del tratamiento** (art. 4.8 RGPD)
  - **Corresponsable** (art. 26 RGPD)
  - **Varias de las anteriores** (frecuente en grupos empresariales)
- **¿Hay DPD nombrado?**
  - Sí — ¿obligatorio (art. 37 RGPD / art. 34 LOPDGDD) o voluntario?
  - ¿Interno o externo?
  - ¿Comunicado a la AEPD?
  - No — ¿debería haberlo? (Si >250 empleados, si tratan datos sensibles a gran escala, si es organismo público)
- **Autoridad de control principal:** ¿AEPD? ¿Autoridad autonómica (APDCAT, AVPD)?

---

### Parte 2: Tratamientos principales (3-4 min)

> ¿Tienes un registro de actividades de tratamiento (art. 30 RGPD)? Pega el contenido o comparte ruta — extraeré las categorías en vez de preguntarte una a una.

Si no:

- **Categorías de datos personales que tratáis:**
  - Datos identificativos básicos (nombre, DNI, dirección)
  - Datos económicos (nóminas, cuentas bancarias)
  - Datos profesionales (CV, historial laboral)
  - Datos de salud (si aplica)
  - Datos de categorías especiales (art. 9 RGPD)
  - Datos de menores
- **Bases jurídicas principales:**
  - Consentimiento (art. 6.1.a)
  - Ejecución de contrato (art. 6.1.b)
  - Obligación legal (art. 6.1.c)
  - Interés legítimo (art. 6.1.f) — ¿hacéis test de ponderación documentado?
- **Transferencias internacionales:**
  - ¿Transferís datos fuera del EEE?
  - ¿Qué mecanismos usáis? (Decisión de adecuación, SCCs, BCRs, art. 49 RGPD)
  - ¿Hacéis TIA (Transfer Impact Assessment)?
- **Evaluaciones de impacto (EIPD/DPIA):**
  - ¿Cuántas habéis hecho? ¿Tenéis plantilla?
  - ¿Usáis la herramienta FACILITA de la AEPD o propia?

---

### Parte 3: Encargos de tratamiento (3-4 min)

> ¿Tienes un contrato de encargo de tratamiento (DPA) tipo? Pega o comparte ruta.

Si no:

- **Playbook de DPA — posiciones por cláusula del art. 28 RGPD:**

  | Cláusula art. 28 | Tu posición |
  |---|---|
  | Instrucciones documentadas | [PLACEHOLDER] |
  | Confidencialidad | [PLACEHOLDER] |
  | Medidas de seguridad (art. 32) | [PLACEHOLDER — referencia a ENS, ISO 27001, SOC 2] |
  | Subencargados | [PLACEHOLDER — autorización previa/general, derecho de objeción] |
  | Asistencia en derechos | [PLACEHOLDER — plazo, formato] |
  | Asistencia en EIPD y consulta previa | [PLACEHOLDER] |
  | Devolución/supresión al finalizar | [PLACEHOLDER — plazo, formato] |
  | Auditorías | [PLACEHOLDER — derecho de auditoría, frecuencia, certificaciones aceptadas] |

- **¿Cuántos DPAs gestionas aproximadamente?**
- **¿Eres más a menudo responsable negociando con encargados, o encargado negociando con responsables?**

---

### Parte 4: Derechos y brechas (3-4 min)

#### Derechos de los interesados (ARCO-POL)

- **¿Tenéis un proceso definido para atender derechos?**
  - Acceso, Rectificación, Cancelación/Supresión, Oposición (los clásicos ARCO)
  - Portabilidad, Oposición a decisiones automatizadas, Limitación (los nuevos POL)
- **Canal de recepción:** ¿formulario web, email DPD, correo postal?
- **Plazo interno de respuesta:** ¿cuánto tardáis? (El RGPD da 1 mes, prorrogable 2 más)
- **¿Quién gestiona las solicitudes?** (DPD, jurídico, RRHH para empleados)

#### Brechas de seguridad

- **¿Tenéis un protocolo de gestión de brechas?** Pega o comparte ruta.
- **Plazo de notificación a la AEPD:** 72 horas (art. 33 RGPD) — ¿vuestro proceso interno lo cumple?
- **¿Quién decide si se notifica?** (DPD, CISO, dirección jurídica, comité de crisis)
- **¿Habéis tenido brechas que notificar?** (No necesito detalles — solo si el proceso ha sido probado)
- **¿Tenéis seguro de ciberriesgo?**

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica:
>
> - **Política de privacidad** (la que tenéis publicada)
> - **Registro de actividades de tratamiento** (art. 30 RGPD)
> - **DPA tipo** (contrato de encargo de tratamiento)
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica de privacidad
*Escrito por entrevista-inicial el [FECHA].*

### Rol

**La organización como:** [PLACEHOLDER — responsable/encargado/corresponsable]
**DPD nombrado:** [PLACEHOLDER — sí (obligatorio/voluntario, interno/externo) / no]
**Autoridad de control:** [PLACEHOLDER — AEPD / autonómica]

### Tratamientos principales

| Tratamiento | Categorías de datos | Base jurídica | Transferencia internacional |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — sí/no, mecanismo] |

**EIPD realizadas:** [PLACEHOLDER]
**Herramienta EIPD:** [PLACEHOLDER]

### Playbook de DPA (art. 28 RGPD)

| Cláusula | Posición como responsable | Posición como encargado |
|---|---|---|
| Instrucciones | [PLACEHOLDER] | [PLACEHOLDER] |
| Subencargados | [PLACEHOLDER] | [PLACEHOLDER] |
| Medidas de seguridad | [PLACEHOLDER] | [PLACEHOLDER] |
| Auditorías | [PLACEHOLDER] | [PLACEHOLDER] |
| Devolución/supresión | [PLACEHOLDER] | [PLACEHOLDER] |

### Derechos ARCO-POL

**Canal de recepción:** [PLACEHOLDER]
**Plazo interno:** [PLACEHOLDER]
**Responsable de gestión:** [PLACEHOLDER]

### Protocolo de brechas

**Protocolo:** [PLACEHOLDER — existe/no existe]
**Decisor de notificación:** [PLACEHOLDER]
**Plazo interno:** [PLACEHOLDER]

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en privacidad:**
>
> - **Revisar un DPA** — contra tu playbook del art. 28, con posiciones por cláusula. Prueba: `/privacidad:revision-dpa`
> - **Evaluación de impacto (EIPD)** — con la metodología de la AEPD o la tuya. Prueba: `/privacidad:eipd`
> - **Responder a un derecho ARCO-POL** — con plantilla adaptada al tipo de derecho. Prueba: `/privacidad:derecho-interesado`
> - **Gestionar una brecha** — checklist de 72 horas con plantilla de notificación a la AEPD. Prueba: `/privacidad:brecha`
>
> **Mi sugerencia para empezar:** Si tienes un DPA pendiente de negociación, ejecuta `/privacidad:revision-dpa` — verás si entiende tu playbook.

Conectar herramienta de investigación:

> "Antes de tu primer análisis: conecta una herramienta de investigación jurídica. Sin ella, marcaré cada cita de resolución de la AEPD o directriz del EDPB como no verificada."

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`. Todo se puede cambiar:
>
> - Edita el archivo directamente
> - `/privacidad:entrevista-inicial --repetir` para re-entrevista completa
> - `/privacidad:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta: el playbook de DPA (las posiciones evolucionan), el registro de tratamientos (cuando cambian) y el protocolo de brechas."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No confundas RGPD con LOPDGDD.** El RGPD es europeo y directamente aplicable; la LOPDGDD es la ley orgánica española que lo complementa. Ambos coexisten.
- **No asumas que todo el mundo necesita DPD.** Solo es obligatorio en los supuestos del art. 37 RGPD y art. 34 LOPDGDD.
- **No escribas bases jurídicas genéricas.** Cada tratamiento necesita su base jurídica específica — el interés legítimo no es un comodín.
- **No olvides las 72 horas.** El plazo de notificación de brechas es estricto y empieza desde que se tiene conocimiento.
- **No confundas la AEPD con autoridades autonómicas.** Cataluña (APDCAT) y País Vasco (AVPD) tienen competencia sobre el sector público y entidades que operan en su ámbito.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo.
