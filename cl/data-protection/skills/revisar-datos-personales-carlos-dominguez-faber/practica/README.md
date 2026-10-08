# Barbería El Corte — la app que dice que borra tus datos

App de citas para una barbería. Pide diecinueve datos para cortarte el pelo, y su
botón de **"eliminar mi cuenta"** no elimina absolutamente nada.

Está rota a propósito. Es el proyecto de práctica de la clase sobre la
**Ley 21.719** de protección de datos personales de Chile.

> Cada error está marcado en el código con un comentario `[SEMBRADO n]` y el
> artículo que incumple. No copies nada de aquí a un proyecto real.

---

## Cómo correrlo

Necesitas **Node 22.5 o superior**. Nada más — no hay `npm install`, no hay
base de datos que instalar, no hay variables de entorno.

```bash
npm run seed     # carga tres clientes de ejemplo
npm start        # abre http://localhost:3000
```

Para volver a empezar de cero en cualquier momento:

```bash
npm run reset && npm run seed
```

---

## El guion de la demo en vivo

**Antes de empezar:** `npm run reset && npm run seed && npm start`, y ten una
segunda pestaña de terminal abierta en esta carpeta.

### 1 · Enséñales el formulario · 1 min

Abre `http://localhost:3000/registro`.

Es un formulario para **agendar un corte de pelo** que pide RUT, fecha de
nacimiento, dirección, ocupación, ingreso mensual y el teléfono de un familiar.
Y abajo, un solo checkbox premarcado que acepta todo junto.

La pregunta para la sala: *¿cuál de estos campos necesita una barbería para
cortarte el pelo?*

### 2 · Entra a la ficha de Camila · 1 min

`http://localhost:3000/cliente/1`

Además de sus datos, hay dos cosas que conviene señalar:

- La nota de su cita dice **"alérgica al tinte con amoniaco"**. Eso es un dato
  de salud viviendo en un campo de texto libre.
- La app la etiquetó como **"riesgo alto de no asistir"** con puntaje 34. Nadie
  guardó por qué, ni con qué versión del modelo, ni cómo pedir que lo revisen.

### 3 · Borra la cuenta · 30 seg

Baja al botón rojo: **"Eliminar mi cuenta y todos mis datos"**. Aprieta.

Sale el mensaje verde: *"Todos tus datos personales fueron borrados de forma
permanente de nuestros sistemas."*

Deja ese mensaje en pantalla un segundo de más. Esa frase es la mentira.

### 4 · El forense · 3 min

En la segunda terminal:

```bash
npm run forense 18.402.551-K
```

Sale el rastreo: la persona sigue viva en **7 de 7 lugares**. La fila completa
en la tabla, la copia íntegra en auditoría, el dato de salud en las citas, la
etiqueta del scoring, el payload que ya salió hacia un tercero, el RUT en texto
plano en `datos/app.log`, y el export en `datos/crm-export.json`.

Cada hallazgo trae el artículo que incumple.

### 5 · El remate · 1 min

> El borrado no es una consulta, es un mapa.

Y la frase de cierre de la clase:

> Que tu política de privacidad no prometa algo que tu base de datos no cumple.

### 6 · Enséñales el `UPDATE` · 1 min

Abre `app.js` y busca la función `eliminarCuenta`. Son tres líneas. Lo único que
pasa es `UPDATE clientes SET activo = 0`.

Ese es el punto: nadie escribió esto de mala fe. Es lo que sale por defecto
cuando le pides a un agente "agrega un botón para eliminar la cuenta".

---

## Los nueve errores sembrados

| # | Dónde | Qué está mal | Artículo |
|---|---|---|---|
| 1 | `db.js` · tabla `clientes` | Diecinueve campos para agendar un corte | 3 c) y 14 quáter |
| 2 | `db.js` · `acepto_todo` | Un booleano para todas las finalidades, sin fecha ni versión | 12 y 14 ter k) |
| 3 | `app.js` · `eliminarCuenta` | El borrado es un `UPDATE` de una bandera | 8 y 11 |
| 4 | `db.js` · tabla `auditoria` | Copia íntegra en JSON que sobrevive al borrado | 8 |
| 5 | `db.js` · `citas.notas` | Datos de salud en texto libre | 2 y 16 |
| 6 | `db.js` · tabla `scoring` | Decisión automatizada sin factores ni revisión humana | 8 bis |
| 7 | `db.js` · tabla `webhooks` | Payload completo enviado a un tercero | 15 bis |
| 8 | `db.js` · `log()` | RUT, teléfono y correo en texto plano en el log | 3 c) |
| 9 | `db.js` · `exportarACrm()` | Export a un sistema externo fuera de tu control | 27 a 29 |

Faltan además tres cosas que la ley exige y que esta app simplemente no tiene:
**exportar tus datos** (portabilidad, art. 9), **bloquear el tratamiento**
mientras se resuelve un reclamo (art. 8 ter), y una **página pública de política
de tratamiento** (art. 14 ter).

---

## El reto para la comunidad

Corre la skill de auditoría sobre este repo y compara su reporte con la tabla de
arriba. ¿Los encontró todos? ¿Inventó alguno que no existe?

Después hazlo con tu propio proyecto.

---

*Material de clase de Imperio Agéntico. Esto no es asesoría legal.*
