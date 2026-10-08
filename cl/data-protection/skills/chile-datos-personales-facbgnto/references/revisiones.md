# Listas de revisión

Seis secciones. **A, B y C se eligen** según lo que se tocó —recorrerlas todas en
cada cambio es la forma más rápida de que el equipo deje de hacerlo. **D, E y F se
consultan cuando corresponde**: D si el tratamiento puede exigir evaluación de
impacto, E antes de declarar terminado, F si encuentras algo fuera del alcance.

Los controles de seguridad genéricos (XSS, CSRF, inyección, CSP, cabeceras, rate
limiting, dependencias, almacenamiento en navegador) se delegan a
`facbgnto-security-review` y `security-storage`. Aquí solo aparecen los que, al
fallar, **exponen datos personales**.

---

## A. Revisión de modelo o migración

Campo por campo. No apruebes una migración sin haber contestado esto:

```
Campo: pacientes.diagnostico

Clase:            SENSIBLE (salud)
Finalidad:        atención clínica
Base de licitud:  consentimiento expreso  ← ¿registrada dónde?
¿Es el mínimo?    sí / no — si no, ¿por qué existe?
Cifrado:          evaluar a nivel de columna
Índices:          ¿el índice permite enumerar o inferir?
Logs:             prohibido
Retención:        ver docs/privacidad/inventario.md
En respuestas:    solo DTO clínico, nunca en DTO público
Al eliminar:      eliminar; el histórico se conserva anonimizado
```

Preguntas transversales de la migración:

- [ ] ¿Algún campo nuevo carece de finalidad clara? → no implementarlo.
- [ ] ¿Hay campos de texto libre que recibirán datos sensibles en la práctica?
- [ ] ¿El identificador expuesto es opaco, o es el RUT?
- [ ] ¿Las tablas nuevas se pueden vincular a un titular para acceso y eliminación?
- [ ] ¿Hay `ON DELETE` definido de forma que eliminar al titular no deje huérfanos con PII?
- [ ] ¿Los seeds y fixtures usan datos sintéticos, no reales?
- [ ] ¿Se anotó la clasificación en el esquema y en el inventario?

---

## B. Revisión de endpoint

Para cada endpoint que toca datos personales:

- [ ] **Autenticado.** ¿Existe alguna ruta que llegue aquí sin sesión válida?
- [ ] **Autorizado.** ¿El rol permite esta operación sobre este recurso?
- [ ] **Pertenencia.** Acceso por id: ¿se verifica que el recurso sea del solicitante?
      `Model.findByPk(req.params.id)` sin filtro es el patrón de IDOR/BOLA.
- [ ] **Tenant.** ¿El `tenant_id` sale del contexto autenticado y **no** del cliente?
      Si viene en el body, la query string o una cabecera, es un hallazgo CRÍTICO.
- [ ] **Entrada validada en backend.** Tipo, largo, formato, rango, enum, relación.
      La validación de frontend mejora la experiencia; no sustituye nada.
- [ ] **Asignación masiva.** `Model.update(req.body)` permite escribir `rol`,
      `tenant_id` o `verificado`. Usa lista blanca explícita de campos.
- [ ] **Salida minimizada.** DTO por audiencia, no el modelo serializado.
      ¿La respuesta incluye `password_hash`, tokens, notas internas o campos
      sensibles que esta audiencia no necesita?
- [ ] **Auditado**, si lee o exporta datos sensibles, o cambia permisos.
- [ ] **Rate limit**, si es login, recuperación de clave, OTP, registro, búsqueda de
      personas o exportación.
- [ ] **Errores controlados.** Sin stack trace, SQL, rutas ni secretos en la respuesta.
- [ ] **Sin enumeración.** ¿La respuesta permite descubrir si una persona existe?

### Los cuatro patrones que más filtran datos

```js
// 1. IDOR — sin verificar pertenencia
// ✘  const doc = await Documento.findByPk(req.params.id);
const doc = await Documento.findOne({                    // ✔
  where: { id: req.params.id, tenantId: req.user.tenantId }
});

// 2. Tenant desde el cliente
// ✘  const tenantId = req.body.tenantId;
const tenantId = req.user.tenantId;                      // ✔

// 3. Serialización completa
// ✘  res.json(usuario);
res.json(UsuarioPublicoDTO.from(usuario));               // ✔

// 4. Asignación masiva
// ✘  await usuario.update(req.body);
const { nombres, telefono } = req.body;                  // ✔
await usuario.update({ nombres, telefono });
```

### Búsqueda de personas y exportación masiva

Merecen su propio párrafo porque su riesgo no es leer un registro, sino
**extraer la base completa**:

- largo mínimo de término de búsqueda; sin búsqueda por prefijo de RUT;
- paginación con tope duro, no solo por defecto;
- rate limit por usuario, no solo por IP;
- permiso específico para exportar, distinto del permiso de leer;
- auditoría de cada exportación con actor, fecha, tenant, tipo y **cantidad de
  registros**;
- alerta cuando el volumen supere un umbral **explícito**. Si el proyecto no tiene
  uno definido, propón `> 1.000 registros por exportación` o `> 3 exportaciones por
  hora y usuario` como punto de partida, y déjalo escrito en el inventario en vez
  de dejarlo a criterio de quien revise la próxima vez.

---

## C. Checklist de Pull Request

Copia esto al PR cuando el cambio toca datos personales:

```
Privacidad — Ley 21.719

[ ] Introduce datos personales nuevos ....... sí / no
[ ] Finalidad documentada .................... sí / no / n.a.
[ ] Base de licitud identificada ............. ______
[ ] Minimización aplicada .................... sí / no
[ ] Contiene datos sensibles ................. sí / no  (incl. socioeconómicos)
[ ] Involucra NNA ............................ sí / no
[ ] Autorización verificada en backend ....... sí / no / n.a.
[ ] Riesgo IDOR/BOLA revisado ................ sí / no / n.a.
[ ] Aislamiento de tenant verificado ......... sí / no / n.a.
[ ] Entrada validada en backend .............. sí / no / n.a.
[ ] Sin asignación masiva .................... sí / no / n.a.
[ ] Sin PII en logs ni telemetría ............ sí / no
[ ] Auditoría donde corresponde .............. sí / no / n.a.
[ ] Retención definida ....................... ______
[ ] Datos compartidos con terceros ........... ______
[ ] Transferencia internacional .............. sí / no
[ ] Derechos del titular siguen ejercibles ... sí / no
[ ] Requiere evaluación de impacto ........... sí / no
[ ] Inventario de privacidad actualizado ..... sí / no

Privacy Review: <enlace o resumen>
```

---

## D. Cuándo escalar a evaluación de impacto

Recomienda una evaluación de impacto en protección de datos —y marca
`REVISIÓN LEGAL REQUERIDA`— cuando concurra alguno de estos:

```
biometría o reconocimiento facial
datos de salud a escala
datos socioeconómicos usados para decidir sobre personas
perfilamiento o scoring de personas
decisiones automatizadas con efecto relevante (crédito, empleo, beneficio, precio)
monitoreo sistemático (vigilancia, productividad, geolocalización continua)
tratamiento masivo de datos de NNA
cruce de bases de datos antes separadas
uso de IA sobre datos personales a escala
```

No la redactes tú como documento legal: identifica el disparador, describe el
tratamiento en términos técnicos, y entrégalo a quien corresponda.

---

## E. Antes de declarar terminado

Aplica **a todo trabajo que haya pasado de la Fase 2** —es decir, que trate al menos
un dato `PERSONAL`. Un cambio que salió en el triaje por ser todo `INTERNO` no pasa
por aquí ni genera Privacy Review ni inventario.

Cinco condiciones. Si alguna falla, la funcionalidad no está lista y se dice así:

1. Todo dato personal tiene finalidad y base de licitud registradas.
2. No hay hallazgos CRÍTICOS ni ALTOS abiertos.
3. Los derechos del titular siguen siendo ejercibles sobre los datos nuevos.
4. Hay retención definida para cada categoría agregada.
5. `docs/privacidad/inventario.md` está actualizado.

**Qué significa "detener" en la práctica.** No puedes impedir un despliegue, pero
sí puedes —y debes— hacer tres cosas: reportar el hallazgo antes que cualquier
resumen de avance, proponer la corrección mínima que desbloquea, y decir
explícitamente que la funcionalidad no debe considerarse terminada. Marcar la
tarea como completa con un hallazgo CRÍTICO abierto es el error que este skill
existe para evitar.

---

## F. Si encuentras una vulnerabilidad de paso

Mientras haces otra cosa vas a encontrar problemas preexistentes. La regla es
simple: **se reportan igual.**

No los ignores porque no son parte del ticket, no los silencies porque el arreglo
es incómodo, y no sigas construyendo encima como si no existieran. Repórtalos con
el formato de hallazgo y deja que el equipo priorice — esa decisión es suya, pero
solo pueden tomarla si lo saben.

Si el hallazgo indica que **ya hubo exposición** de datos —no solo que era
posible—, dilo de forma destacada: eso deja de ser un asunto de desarrollo y pasa
a gestión de incidentes, con deber de notificar. Los datos que el equipo necesitará
reunir son:

```
detectado_en · tipo · severidad · sistemas afectados
categorías de datos · titulares afectados (cuántos, quiénes)
ventana temporal · riesgo para los titulares
acciones de contención · estado
```

Para eso hace falta auditoría de accesos. Si no existe, esa ausencia es en sí misma
un hallazgo: un sistema que no puede dimensionar una brecha tampoco puede
notificarla.
