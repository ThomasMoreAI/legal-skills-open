# Peru — detalle operativo de tramites

Complemento de `SKILL.md`. Verificado a agosto de 2026. **Las rutas de menu cambian: si no coincide, no asumas — busca en la ayuda oficial o acompaña al usuario en pantalla.**

---

## Formalizar como persona natural con negocio

Punto de partida habitual para un negocio chico que ya tiene RUC de persona natural.

**Que se hace:** agregar la actividad economica y dar de alta los tributos de tercera categoria.

**Donde:** SUNAT Operaciones en Linea (SOL), con clave SOL propia. Modulo de actualizacion de informacion del RUC.

**Que se define:**
1. **Actividad economica (CIIU)** — principal o secundaria. Determina como te clasifican; elige la que de verdad describe lo que haces.
2. **Afectacion de tributos** — renta de tercera categoria en el regimen elegido, mas IGV cuando corresponde.
3. **Fecha de inicio de actividades** — puede ser futura. Define desde que periodo declaras.

**Ojo con esto:** el alta genera **obligacion de declarar todos los meses desde ese periodo, aunque el resultado sea cero**. No declarar genera multa aunque no hayas vendido nada. Esta es la sorpresa mas comun al formalizar.

**Acogimiento al regimen:** en varios regimenes se perfecciona **declarando y pagando el primer periodo dentro del plazo**. Formalizar y no declarar a tiempo puede dejarte fuera del regimen que elegiste.

**Solo-humano:** todo. Requiere clave SOL.

---

## Comprobantes de pago

**Boleta** — a consumidor final. **Factura** — a quien necesita credito fiscal (empresas). En NRUS solo boletas, y esa es la razon principal para no elegirlo si vendes a empresas.

**Desde junio de 2026**, los nuevos inscritos en RMT, RER o General son emisores electronicos desde el dia uno.

**Como emitir:**
- **Portal SUNAT (SEE-SOL)** — gratis, sin integracion. Suficiente para volumen bajo. Emision manual.
- **Proveedor de facturacion electronica (OSE/PSE)** — con API. Necesario cuando el volumen hace inviable lo manual, o cuando quieres emitir automatico desde tu tienda.

**Regla practica:** empieza en el portal gratuito y migra cuando el volumen duela. Migrar antes es pagar por algo que todavia no necesitas; migrar tarde es dedicarle horas a copiar datos.

---

## Declaracion mensual

**Que:** ingresos, IGV y renta del periodo. **Cuando:** segun el cronograma anual por ultimo digito del RUC. **Donde:** SOL, formulario de declaracion simplificada.

**El agente puede:** preparar los numeros desde tu sistema de ventas, verificar que cuadren con lo emitido, armar el resumen y avisar del vencimiento con dias de anticipacion.

**El agente no puede:** entrar, declarar ni pagar. Clave SOL.

**Consejo operativo:** no lo dejes para el ultimo dia. Las plataformas del Estado se caen justo el dia del vencimiento — en todos los paises, todos los meses.

---

## SIRE

Reemplaza progresivamente al PLE en registros de ventas y compras.

- **RVIE** — registro de ventas e ingresos.
- **RCE** — registro de compras.

Lo que lo hace distinto: **SUNAT precarga** los comprobantes electronicos. Tu revisas, ajustas y confirmas, en vez de armar el libro desde cero.

Quien esta obligado a SIRE lo lleva **desde el periodo en que nace la obligacion**, no despues.

---

## Registro de marca (Indecopi)

**Paso 1 — Descarte previo (gratis, 10 min).** Buscador de marcas. Busqueda fonetica **y** denominativa, en tu clase. Guarda captura de lo que encuentres: es la evidencia de la decision.

**Paso 2 — Elegir clase.** Clasificacion de Niza. Cada clase se paga aparte. Verifica cual cubre de verdad tu actividad antes de pagar.

**Paso 3 — Solicitud.** En linea, con tasa por clase. Publicacion y plazo de oposicion. Puede haber observaciones que hay que responder dentro de plazo.

**Cuando conviene registrar:** despues de validar que el negocio funciona, antes de invertir fuerte en publicidad. Registrar temprano es gastar en un nombre que quiza cambies; registrar tarde es arriesgar el nombre en el que ya invertiste.

---

## Documentos publicos obligatorios en comercio electronico

Deben estar accesibles desde el sitio:

1. **Libro de Reclamaciones virtual** — visible, con formulario funcionando y aviso de recepcion.
2. **Terminos y condiciones**.
3. **Politica de privacidad y tratamiento de datos personales**.
4. **Politica de cambios y devoluciones**.
5. **Politica de envios y entregas** — plazos reales, no optimistas. Un plazo incumplido es un reclamo con base.

Viven en `20-legal-y-fiscal/politicas/` y se publican en el sitio. **Se revisan cuando cambia la operacion**, no una sola vez: una politica de envios que ya no describe como entregas es peor que no tenerla.

---

## Cuenta bancaria del negocio

No es obligatorio legalmente para persona natural con negocio, pero **separar cuentas** es lo que hace posible un cierre mensual real. Mezclar gastos personales y del negocio hace imposible saber si el negocio gana plata, que es la unica pregunta que importa.

Ademas, varias plataformas de pago y proveedores logisticos exigen que la cuenta de retiro este **a nombre del titular del RUC**.

---

## Calendario tipico del primer año

| Cuando | Que |
|---|---|
| Al formalizar | Alta de actividad y tributos; elegir regimen (ADR) |
| Mismo dia | Descarte de marca en Indecopi |
| Antes de vender | Emision electronica configurada y probada con un comprobante real |
| Antes de publicar el sitio | Las cinco politicas publicadas y el libro de reclamaciones funcionando |
| Cada mes | Declaracion segun cronograma. **Aunque sea cero.** |
| Cuando valide el negocio | Solicitud de registro de marca |
| Al cambiar de escala | Revisar si el regimen sigue siendo el correcto |
