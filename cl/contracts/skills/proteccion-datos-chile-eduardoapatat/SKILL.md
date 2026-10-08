---
name: proteccion-datos-chile-eduardoapatat
title: Protección de datos personales en Chile
description: Diseña, implementa o audita sistemas dirigidos a Chile que tratan o probablemente tratarán datos personales, y analiza consultas e incidentes bajo las leyes chilenas 19.628 y 21.719. Actívala cuando se solicite privacidad o protección de datos chilena, o cuando concurran un nexo con Chile y funciones como cuentas, RUT, pagos, soporte, cookies, IP vinculables, logs, geolocalización, biometría, salud, perfiles, IA o transferencias. No la actives por una mención aislada de Chile, por datos irreversiblemente anónimos ni por ciberseguridad sin datos personales.
author: eduardoapatat
author_url: https://github.com/eduardoapatat/proteccion-datos-chile
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: contracts
language: es
sources:
- title: Activacion En Sistemas
  path: references/activacion-en-sistemas.md
- title: Fuentes Oficiales
  path: references/fuentes-oficiales.md
- title: Incidentes Y Sanciones
  path: references/incidentes-y-sanciones.md
- title: Metodo Y Salidas
  path: references/metodo-y-salidas.md
- title: Regimen Y Puntos Clave
  path: references/regimen-y-puntos-clave.md
- title: Revision De Sistemas
  path: references/revision-de-sistemas.md
---

# Protección de datos personales en Chile

Ayuda a construir sistemas seguros y privados desde el inicio, revisar implementaciones existentes, responder a incidentes y resolver consultas jurídicas. Trabaja con evidencia, separa el derecho vigente del régimen futuro y no trates esta materia como una traducción automática del RGPD.

## Detonante de activación

Activa directamente esta skill si el usuario pide aplicar, explicar o revisar la normativa chilena de privacidad o protección de datos.

En proyectos tecnológicos, actívala sólo cuando concurran los dos elementos siguientes:

1. **Nexo chileno:** el responsable o encargado está en Chile; el producto se dirige al mercado chileno; se ofrecen bienes o servicios a personas en Chile; se monitorea su comportamiento; o existe otro vínculo contractual o normativo relevante.
2. **Tratamiento real o razonablemente previsible:** el sistema recolecta, genera, infiere, consulta, almacena, modifica, combina, perfila, comunica, transfiere, conserva o elimina información sobre personas naturales identificadas o identificables.

No esperes a que el usuario diga “dato personal”. Infiérelo cuando una función necesariamente implique cuentas, identificación, RUT, contacto, pagos, despacho, soporte, cookies, identificadores, IP vinculables, logs de actividad, imágenes, voz, ubicación, analítica individual, datos laborales o información aportada a una IA.

Una mención aislada de “Chile”, “mercado chileno” o “seguridad” no basta. Si sólo hay una señal débil, realiza un cribado breve y confirma los dos elementos antes de desplegar el análisis completo.

No la actives para:

- preguntas generales sobre Chile sin tratamiento de datos personales;
- información exclusiva de personas jurídicas que no identifique a personas naturales;
- datos irreversiblemente anonimizados, con reidentificación razonablemente imposible;
- actividades estrictamente personales excluidas por la ley;
- revisiones de ciberseguridad sin datos personales ni impacto en su confidencialidad, integridad o disponibilidad.

La seudonimización no equivale a anonimización. El RUT y una IP vinculable son normalmente datos personales, pero no son por ese solo hecho datos sensibles. Clasifica la categoría usando el artículo 2 aplicable y el contexto.

Lee [references/activacion-en-sistemas.md](references/activacion-en-sistemas.md) para resolver casos límite y elegir el modo de trabajo.

## Modos de trabajo

Selecciona el modo según la petición; combina modos cuando corresponda:

- **Construcción:** guía requisitos, arquitectura, modelo de datos, interfaces, contratos, pruebas, despliegue y operación antes de implementar o lanzar.
- **Auditoría:** contrasta código, configuración, infraestructura, bases de datos, flujos, contratos y operación existente con controles jurídicos y técnicos.
- **Incidente:** ayuda a contener, preservar evidencia, evaluar afectación y determinar comunicaciones o acciones exigibles.
- **Consulta:** responde una cuestión jurídica concreta con artículos y fuentes oficiales.

Para construcción o auditoría, lee [references/revision-de-sistemas.md](references/revision-de-sistemas.md). Para una fuga, acceso indebido, pérdida o alteración, lee [references/incidentes-y-sanciones.md](references/incidentes-y-sanciones.md).

## Control de vigencia obligatorio

Antes de formular una conclusión jurídica:

1. Identifica la fecha de los hechos y la fecha para la cual se pide el análisis.
2. Verifica el texto consolidado en LeyChile, las publicaciones del Diario Oficial y el estado legislativo oficial siguiendo [references/fuentes-oficiales.md](references/fuentes-oficiales.md).
3. Informa separadamente la **fecha legal vigente**, cualquier **fecha propuesta** y el **estado verificado**, con fecha de consulta.
4. Al 16 de septiembre de 2026, la fecha publicada para la entrada en vigencia de las modificaciones de la Ley N.º 21.719 es el **1 de diciembre de 2026**.
5. El Boletín N.º 18.623-07 propone el **1 de diciembre de 2027**. Al 16 de septiembre de 2026 se encuentra en primer trámite constitucional en el Senado, con suma urgencia, y todavía no modifica la fecha legal.
6. Si una ley posterior se publica, aplica su texto y deja de presentar esa modificación como propuesta.
7. Para hechos anteriores a la entrada finalmente aplicable, parte de la Ley N.º 19.628 vigente en esa fecha. Trata la reforma como preparación futura, salvo una disposición específica ya vigente.
8. Desde la entrada finalmente aplicable, usa la Ley N.º 19.628 modificada, sus reglamentos y las instrucciones vigentes de la Agencia.
9. Si no puedes acceder a fuentes oficiales actuales, declara la última fecha verificada y no afirmes que el estado sigue vigente.

## Flujo obligatorio

1. **Fijar alcance.** Define modo, componentes incluidos, fecha de corte y profundidad posible.
2. **Levantar hechos.** Identifica titulares, datos, finalidades, operaciones, roles, ubicaciones, terceros, conservación, decisiones automatizadas y fechas. Declara los supuestos.
3. **Trazar datos.** Sigue cada categoría desde la recolección hasta su eliminación, incluidos logs, analítica, soporte, respaldos, ambientes no productivos, IA y subencargados.
4. **Fijar régimen.** Usa [references/regimen-y-puntos-clave.md](references/regimen-y-puntos-clave.md) y verifica los artículos oficiales.
5. **Mapear controles.** Relaciona cada finalidad y operación con licitud, información, proporcionalidad, derechos, seguridad, encargados, transferencias, conservación y evaluación de impacto.
6. **Comprobar evidencia.** Revisa los artefactos disponibles. No des por implementado un control porque aparezca en una política o porque el usuario diga que “se cifra”.
7. **Detectar brechas.** Distingue fallas técnicas, brechas de cumplimiento, vacíos de evidencia e incidentes. Relaciona una posible infracción sólo con los elementos realmente observados.
8. **Remediar y probar.** Propón cambios concretos, responsable, prioridad y una prueba de aceptación verificable.

No detengas una orientación general por datos faltantes: trabaja con supuestos visibles. En una auditoría concreta, pide sólo el artefacto decisivo que falte o marca el punto como **no verificado**.

## Revisión de seguridad basada en evidencia

Si hay acceso al proyecto, examina dentro del alcance autorizado al menos:

- esquemas y migraciones de base de datos;
- formularios, contratos de API y validaciones;
- autenticación, autorización, aislamiento entre clientes y accesos administrativos;
- configuración de nube, almacenamiento, red, cifrado y gestión de secretos;
- logs, telemetría, trazas, URLs, errores y herramientas de analítica;
- políticas de retención, tareas de borrado y respaldos;
- exportación, rectificación, supresión, oposición, bloqueo y portabilidad;
- integraciones, proveedores, países y subencargados;
- datos de producción en desarrollo, pruebas o entrenamiento de IA;
- detección, escalamiento y registro de incidentes.

No ejecutes pruebas intrusivas ni explotes vulnerabilidades sin autorización expresa. No reproduzcas secretos ni datos personales innecesarios en la respuesta; redacta o referencia su ubicación de forma segura.

La ausencia de un hallazgo no prueba la ausencia de vulnerabilidades. Si sólo se revisó documentación, no afirmes que el código o la infraestructura son seguros.

## Calificación de hallazgos

Para cada hallazgo usa:

- **Estado:** cumple, parcial, no cumple, no verificado o no aplica.
- **Evidencia:** archivo, componente, configuración, flujo, entrevista o documento observado; nunca inventado.
- **Régimen:** vigente, futuro confirmado, proyecto o buena práctica.
- **Riesgo técnico/operacional:** crítico, alto, medio o bajo, con criterio explicado.
- **Encaje jurídico:** artículo y conducta potencial; usa “posible” o “probable” cuando falten hechos. Reserva “confirmado” para evidencia suficiente y evita declarar responsabilidad, que corresponde a la autoridad o al tribunal.
- **Corrección y prueba:** cambio concreto y forma de verificarlo.

No equipares automáticamente la prioridad técnica con la clasificación legal de infracción. Una vulnerabilidad crítica puede no haber producido todavía una infracción consumada, y una práctica técnicamente sencilla puede constituir un incumplimiento jurídico relevante.

## Reglas de exactitud

- Cita ley, artículo o disposición transitoria, versión, fecha de consulta y enlace oficial.
- Separa texto legal, interpretación, inferencia y recomendación técnica.
- No inventes reglamentos, instrucciones, decisiones de adecuación, expedientes, fallos, plazos ni montos.
- No presentes como vigente una versión futura, propuesta, noticia o guía.
- No supongas que el consentimiento es siempre necesario ni suficiente.
- No concluyas que una fuente pública permite cualquier reutilización.
- No conviertas el cifrado, una certificación o una política en garantía automática de cumplimiento.
- En incidentes, no importes un plazo general de 72 horas sin fuente chilena aplicable.
- Recomienda revisión profesional chilena cuando exista alto impacto, incidente activo, litigio, fiscalización, biometría, salud, menores, vigilancia, decisiones automatizadas o incertidumbre material.

## Salida

Usa la plantilla pertinente de [references/metodo-y-salidas.md](references/metodo-y-salidas.md). Toda entrega sustantiva debe incluir:

1. conclusión ejecutiva y alcance revisado;
2. régimen y fecha de corte;
3. mapa resumido de datos y roles;
4. hallazgos con evidencia, artículo, estado y prioridad;
5. acciones de diseño o remediación con pruebas de aceptación;
6. asuntos no verificados y artefactos faltantes;
7. fuentes oficiales.

No declares que un sistema “cumple la ley” en términos absolutos. Indica qué controles fueron comprobados, cuáles no y qué revisión adicional requiere la conclusión.
