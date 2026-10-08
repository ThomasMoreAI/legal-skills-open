---
name: entrevista-inicial-privacidad-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu rol en protección de datos (responsable/encargado/encargado de protección de datos), tus tratamientos principales, tu playbook de encargos de tratamiento, tu proceso de derechos y brechas. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/privacidad/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — solo recomprobar integraciones. Solo reportar ✓ si una llamada MCP respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego partes específicas).
3. Documentos semilla: política de privacidad, registro de actividades, DPA tipo.
4. Extraer: rol, tratamientos, playbook DPA, proceso de derechos del titular, protocolo de brechas.
5. Migración: si existe CLAUDE.md completo en cache pero no en config, copiar y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`.

---

## Propósito

La privacidad y protección de datos en Panamá se rige por la Ley 81 de 2019 y su Decreto Ejecutivo reglamentario 285 de 2021, bajo la supervisión de la ANTAI. Un encargado de protección de datos in-house de una multinacional tiene necesidades completamente distintas a un abogado de despacho que asesora a pymes sobre la Ley 81 de 2019. Esta entrevista descubre tu posición real y construye el perfil que necesitas.

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

> **`privacidad` es para quienes trabajan en protección de datos personales — Ley 81 de 2019, Decreto Ejecutivo 285 de 2021, evaluaciones de impacto, encargos de tratamiento, derechos del titular y gestión de brechas.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, si hay encargado de protección de datos nombrado y los tratamientos principales. **15 minutos** añade tu playbook de DPAs, tu proceso de derechos del titular, tu protocolo de brechas y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de privacidad (rol, tratamientos, playbook de encargos de tratamiento, procesos de derechos del titular y brechas), plantillas de documentos y registro de actividades. Aprende cómo trabajas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas de la Ley 81 de 2019, el Decreto Ejecutivo 285 de 2021 y las resoluciones y guías de la ANTAI.

---

## La entrevista

### Apertura

> Voy a aprender cómo gestionas la protección de datos — tu rol, tus tratamientos, tu playbook de DPAs y tu proceso de derechos y brechas — para que cada evaluación, contrato y respuesta que prepare encaje con tu práctica.

**Ruta rápida:** solo Parte 0 y Parte 1 (rol y encargado de protección de datos). Config con `[POR DEFECTO]`.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> 1. **Abogado o profesional jurídico** — abogado de privacidad, encargado de protección de datos, consultor en protección de datos bajo supervisión.
> 2. **No abogado con acceso a abogado** — encargado de protección de datos no jurista, CISO, compliance officer con abogado accesible.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: herramientas de gestión de privacidad (OneTrust, TrustArc, Nymity), almacenamiento de documentos, herramientas de ticketing (para derechos y brechas) y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho / consultoría de privacidad**
> - **Encargado de protección de datos in-house**
> - **In-house (abogado/compliance, sin rol formal de encargado de protección de datos)**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: Rol de la organización (2-3 min)

- **¿La organización actúa como:**
  - **Responsable del tratamiento** (Ley 81 de 2019)
  - **Encargado del tratamiento** (Ley 81 de 2019)
  - **Corresponsable** (Ley 81 de 2019)
  - **Varias de las anteriores** (frecuente en grupos empresariales)
- **¿Hay encargado de protección de datos nombrado?**
  - Sí — ¿obligatorio (Ley 81 de 2019) o voluntario?
  - ¿Interno o externo?
  - ¿Comunicado a la ANTAI?
  - No — ¿debería haberlo? La designación de Oficial/Enlace de Protección de Datos es obligatoria solo para el SECTOR PÚBLICO (Decreto Ejecutivo 285 de 2021); en el sector privado es voluntaria/recomendada (atenúa la eventual sanción)
- **Autoridad de control:** la ANTAI (Autoridad Nacional de Transparencia y Acceso a la Información)

---

### Parte 2: Tratamientos principales (3-4 min)

> ¿Tienes un registro de actividades de tratamiento? Pega el contenido o comparte ruta — extraeré las categorías en vez de preguntarte una a una.

Si no:

- **Categorías de datos personales que tratáis:**
  - Datos identificativos básicos (nombre, cédula, dirección)
  - Datos económicos (planillas, cuentas bancarias)
  - Datos profesionales (CV, historial laboral)
  - Datos de salud (si aplica)
  - Datos sensibles (Ley 81 de 2019)
  - Datos de menores
- **Bases de licitud principales (Ley 81 de 2019):**
  - Consentimiento del titular
  - Ejecución de relación contractual
  - Cumplimiento de obligación legal
  - Otras causas de licitud — ¿documentáis la justificación?
- **Transferencias internacionales:**
  - ¿Transferís datos fuera de Panamá?
  - ¿Qué mecanismos usáis? (destino con nivel de protección equivalente o superior, cláusulas contractuales, consentimiento del titular; Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021)
  - ¿Documentáis la evaluación de la transferencia?
- **Evaluaciones de impacto (EIPD):**
  - ¿Cuántas habéis hecho? ¿Tenéis plantilla?
  - ¿Usáis plantilla propia adaptada a la Ley 81 de 2019?

---

### Parte 3: Encargos de tratamiento (3-4 min)

> ¿Tienes un contrato de encargo de tratamiento (DPA) tipo? Pega o comparte ruta.

Si no:

- **Playbook de DPA — posiciones por cláusula del encargo (Ley 81 de 2019):**

  | Cláusula del encargo | Tu posición |
  |---|---|
  | Instrucciones documentadas | [PLACEHOLDER] |
  | Confidencialidad | [PLACEHOLDER] |
  | Medidas de seguridad | [PLACEHOLDER — referencia a ISO 27001, SOC 2] |
  | Subencargados | [PLACEHOLDER — autorización previa/general, derecho de objeción] |
  | Asistencia en derechos | [PLACEHOLDER — plazo, formato] |
  | Asistencia en EIPD | [PLACEHOLDER] |
  | Devolución/supresión al finalizar | [PLACEHOLDER — plazo, formato] |
  | Auditorías | [PLACEHOLDER — derecho de auditoría, frecuencia, certificaciones aceptadas] |

- **¿Cuántos DPAs gestionas aproximadamente?**
- **¿Eres más a menudo responsable negociando con encargados, o encargado negociando con responsables?**

---

### Parte 4: Derechos y brechas (3-4 min)

#### Derechos del titular (ARCO + portabilidad)

- **¿Tenéis un proceso definido para atender derechos?**
  - Acceso, Rectificación, Cancelación/Supresión, Oposición
  - Portabilidad
- **Canal de recepción:** ¿formulario web, email del encargado de protección de datos, correo postal?
- **Plazo interno de respuesta:** ¿cuánto tardáis? (El plazo legal es de 10 días hábiles desde la presentación de la solicitud, art. 16 de la Ley 81 de 2019)
- **¿Quién gestiona las solicitudes?** (Encargado de protección de datos, jurídico, RRHH para empleados)

#### Brechas de seguridad

- **¿Tenéis un protocolo de gestión de brechas?** Pega o comparte ruta.
- **Plazo de notificación a la ANTAI:** según la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021 — ¿vuestro proceso interno lo cumple?
- **¿Quién decide si se notifica?** (Encargado de protección de datos, CISO, dirección jurídica, comité de crisis)
- **¿Habéis tenido brechas que notificar?** (No necesito detalles — solo si el proceso ha sido probado)
- **¿Tenéis seguro de ciberriesgo?**

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica:
>
> - **Política de privacidad** (la que tenéis publicada)
> - **Registro de actividades de tratamiento**
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
**Encargado de protección de datos nombrado:** [PLACEHOLDER — sí (obligatorio/voluntario, interno/externo) / no]
**Autoridad de control:** ANTAI

### Tratamientos principales

| Tratamiento | Categorías de datos | Base jurídica | Transferencia internacional |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — sí/no, mecanismo] |

**EIPD realizadas:** [PLACEHOLDER]
**Herramienta EIPD:** [PLACEHOLDER]

### Playbook de DPA (encargo de tratamiento — Ley 81 de 2019)

| Cláusula | Posición como responsable | Posición como encargado |
|---|---|---|
| Instrucciones | [PLACEHOLDER] | [PLACEHOLDER] |
| Subencargados | [PLACEHOLDER] | [PLACEHOLDER] |
| Medidas de seguridad | [PLACEHOLDER] | [PLACEHOLDER] |
| Auditorías | [PLACEHOLDER] | [PLACEHOLDER] |
| Devolución/supresión | [PLACEHOLDER] | [PLACEHOLDER] |

### Derechos del titular (ARCO + portabilidad)

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
> - **Revisar un DPA** — contra tu playbook del encargo (Ley 81 de 2019), con posiciones por cláusula. Prueba: `/privacidad:encargo`
> - **Evaluación de impacto (EIPD)** — con tu metodología adaptada a la Ley 81 de 2019. Prueba: `/privacidad:eipd`
> - **Responder a un derecho del titular** — con plantilla adaptada al tipo de derecho. Prueba: `/privacidad:derechos`
> - **Gestionar una brecha** — checklist con plantilla de notificación a la ANTAI. Prueba: `/privacidad:triaje`
>
> **Mi sugerencia para empezar:** Si tienes un DPA pendiente de negociación, ejecuta `/privacidad:encargo` — verás si entiende tu playbook.

Conectar herramienta de investigación:

> "Antes de tu primer análisis: conecta una herramienta de investigación jurídica. Sin ella, marcaré cada cita de resolución de la ANTAI o de fallo del Órgano Judicial como no verificada."

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

- **No confundas la Ley 81 de 2019 con su reglamento.** La Ley 81 de 2019 es la norma marco; el Decreto Ejecutivo 285 de 2021 la reglamenta y desarrolla el detalle operativo. Ambos coexisten. [verificar]
- **No asumas que todo el mundo necesita encargado de protección de datos.** La designación de Oficial/Enlace de Protección de Datos es obligatoria solo para el SECTOR PÚBLICO (Decreto Ejecutivo 285 de 2021); en el sector privado es voluntaria/recomendada.
- **No escribas bases de licitud genéricas.** Cada tratamiento necesita su base de licitud específica; en Panamá el consentimiento del titular es la base principal.
- **No olvides el plazo de notificación de brechas.** Son 72 horas desde el conocimiento del incidente (art. 37 del Decreto Ejecutivo 285 de 2021), notificando conjuntamente a la ANTAI y a los titulares afectados cuando haya riesgo.
- **La autoridad de control es la ANTAI.** No existen autoridades autonómicas como en España; la competencia en protección de datos recae en la ANTAI.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo.
