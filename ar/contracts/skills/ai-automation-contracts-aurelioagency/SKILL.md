---
name: ai-automation-contracts-aurelioagency
title: Contratos para automatizaciones con IA
description: Genera contratos en derecho argentino para vender proyectos de automatización con IA — implementación llave en mano, mantenimiento con abono mensual y órdenes de trabajo puntuales — a partir de los datos del proyecto, y los entrega en Word listos para firmar. Usar SIEMPRE que el usuario mencione contrato, contrato de servicios, contrato de implementación, contrato de mantenimiento, orden de trabajo, anexo técnico, cláusulas, alcance contractual, propiedad intelectual de un desarrollo, garantía de un sistema entregado, o cuando cierre un proyecto con un cliente y necesite formalizarlo. Usar también cuando pregunte qué datos necesita pedirle al cliente antes de firmar, cuando quiera revisar o modificar una cláusula, o cuando describa un proyecto vendido y haya que documentarlo — aunque no diga la palabra "contrato".
author: aurelioagency
author_url: https://github.com/aurelioagency/skills/tree/main/ai-automation-contracts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: contracts
language: es
sources:
- title: Intake
  path: references/intake.md
---

# Contratos para automatizaciones con IA

Genera contratos en derecho argentino, redactados a favor del proveedor, para el modelo de negocio **llave en mano**: el sistema se implementa íntegramente en la infraestructura del cliente, se entrega, y la relación se agota con la aceptación.

## Los tres documentos

**Implementación** (`assets/implementacion.md`) — el contrato completo, con todo el bloque legal de fondo y los Anexos I y II. Se usa siempre. Es el documento del que dependen los otros dos.

**Mantenimiento** (`assets/mantenimiento.md`) — abono mensual con horas incluidas, tiempo de respuesta y renovación automática. Se genera solo si el cliente contrata abono. Se apoya en el de implementación y no lo repite.

**Orden de trabajo** (`assets/orden-trabajo.md`) — una página para la intervención puntual del cliente que vuelve meses después. Se apoya en el contrato original, no renegocia nada.

Cuando el cliente contrata implementación **más** abono, no existe un cuarto documento: se generan los dos primeros y se firman en el mismo acto, con el de mantenimiento arrancando a la fecha de aceptación. Esto se hace así a propósito — si el cliente cancela el abono, nada de la implementación entregada se ve afectado.

## Flujo de trabajo

1. **Determinar qué documentos hacen falta.** Si el usuario no lo aclara, preguntarlo. La respuesta habitual es implementación sola, o implementación más mantenimiento.

2. **Reunir los datos.** Leer `references/intake.md`, que tiene el checklist completo por bloques. Contrastarlo con lo que el usuario ya haya dado — muchas veces la propuesta comercial que le mandó al cliente cubre alcance, plazos, precio y plataformas. Preguntar solo lo que falte y sea relevante para los documentos que se van a generar.

   Preguntar en tandas cortas y agrupadas por bloque, no de a una variable. Las variables con valor por defecto en `assets/defaults.json` no se preguntan salvo que el caso lo justifique.

   Si falta algún dato que el usuario todavía no cerró con el cliente, no frenar: generar igual. Los campos vacíos salen marcados en rojo como `[COMPLETAR: X]` y el script los lista al final.

3. **Armar el JSON de datos.** Partir de `assets/defaults.json` y pisar con los datos del proyecto. Guardarlo como `datos.json` en el directorio de trabajo.

4. **Generar el Word.**

```bash
python3 scripts/generar_contrato.py assets/implementacion.md datos.json "Contrato Implementacion - <Cliente>.docx"
```

El script sustituye los `{{PLACEHOLDERS}}`, arma el .docx con formato de contrato (Calibri 10.5, texto justificado, títulos, salto de página antes de cada anexo) y reporta los campos sin completar.

5. **Verificar antes de entregar.** Convertir a PDF y mirar al menos la primera página y la de firmas:

```bash
python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf salida.docx
pdftoppm -jpeg -r 80 salida.pdf pg
```

6. **Entregar** con `present_files` y listar en el mensaje los campos que quedaron por completar.

## Redacción de los campos de contenido

Varias variables no son un dato suelto sino un bloque de texto (`ALCANCE_INCLUIDO`, `ROLES_IA`, `CRITERIOS_ACEPTACION`, `ESQUEMA_PAGOS`, `ACCESOS_REQUERIDOS`). Redactarlas en registro jurídico, no conversacional, y en listas cortas con guiones. Evitar nombres de herramientas en el cuerpo del contrato cuando alcance con la categoría — salvo en el Anexo I, donde nombrarlas es correcto y necesario porque delimitan el alcance.

Para `CRITERIOS_ACEPTACION`, escribir en positivo y en términos verificables: qué tiene que hacer el sistema para considerarse entregado. Nunca "que el cliente esté conforme".

## Decisiones de política ya tomadas

Estas están fijadas en las plantillas y no se negocian salvo pedido expreso del usuario. Conviene conocerlas para explicarlas si el cliente las objeta.

**Obligación de medios, no de resultado** (art. 1252 CCyC). No se garantiza facturación, ventas ni conversiones. Solo métricas bajo control operativo propio. Las propuestas comerciales previas no integran el contrato.

**Desempeño de la IA en tres capas.** Las acciones determinísticas deben funcionar. Los roles de IA verificables tienen umbral de 90%. La calidad de redacción no se mide. Y hay tres exclusiones separadas, deliberadamente redactadas aparte porque protegen contra cosas distintas: dominio de conocimiento no provisto por el cliente, calidad del input, y naturaleza probabilística de la IA. Mantenerlas separadas — fundidas en una sola cláusula parecen un paraguas y se defienden peor.

**Propiedad intelectual partida.** Se cede la implementación específica en forma total, irrevocable y **no exclusiva**, operativa contra pago total. Se retienen los componentes base (plantillas de flujos, librerías de prompts, arquitecturas, scripts genéricos) con derecho irrestricto de reutilización, y sobre esos se otorga al cliente una licencia perpetua e irrevocable para operar y modificar el sistema. Más reserva expresa de know-how. Esta partición es el activo del negocio: sin ella se empieza de cero en cada cliente.

**Difusión sin aprobación previa.** Autorización irrevocable para publicar nombre, logo, arquitectura, herramientas, metodología y resultados, con renuncia expresa del cliente a objetar. Único límite: credenciales y datos personales identificables de terceros. Más la salvedad de que el contenido educativo sobre componentes propios queda fuera de toda restricción.

**Garantía de 30 días** desde la aceptación, con exclusiones amplias (modificaciones del cliente, cambios de terceros, credenciales vencidas, cambios en sistemas del cliente). Remedio único: corregir. Vencida la garantía, soporte por hora sin obligación de disponibilidad.

**Aceptación tácita a los 7 días** y aceptación no condicionable a preferencias estéticas ni funcionalidades no pactadas.

**Falta de colaboración del cliente**: plazos suspendidos a los 7 días de silencio, fase dada por entregada y facturable a los 30 de inactividad.

**Tope de responsabilidad del 50% del precio percibido**, con exclusión de daños indirectos y lucro cesante, salvo dolo o culpa grave.

**Ley argentina, tribunales comerciales de CABA.**

## Advertencia obligatoria

Al entregar el primer contrato de una serie, recordarle al usuario que esta plantilla debe ser revisada una vez por un abogado argentino antes de usarla con clientes reales. El skill produce un documento consistente y a favor del proveedor, reutilizable indefinidamente; la revisión legal única es lo que lo vuelve seguro. No repetir la advertencia en cada generación posterior.
