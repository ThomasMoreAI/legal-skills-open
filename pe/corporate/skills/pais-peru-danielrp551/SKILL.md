---
name: pais-peru-danielrp551
title: Modulo Peru
description: Modulo de jurisdiccion Peru para el estandar empresa-os. Cubre regimenes tributarios, obligaciones mensuales, comprobantes electronicos y SIRE, registro de marca en Indecopi y proteccion al consumidor. Usala al formalizar una empresa en Peru, al preparar el cierre mensual, o cuando surja una duda de SUNAT, Indecopi o libro de reclamaciones.
author: Danielrp551
author_url: https://github.com/Danielrp551/empresa-os/tree/main/plugins/empresa-os/skills/pais-peru
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pe
practice: corporate
language: es
sources:
- title: Tramites
  path: references/tramites.md
---

# Modulo Peru

**Advertencia que va primero: esto cambia.** Las cifras y plazos de aca estan verificados a agosto de 2026, pero SUNAT e Indecopi modifican reglas y las pantallas cambian de nombre seguido. Regla 1: **verificar contra la fuente oficial antes de actuar**, no contra este documento.

Esto no es asesoria contable. Es un mapa para saber que existe, que preguntar y donde mirar.

## Los cuatro regimenes de renta de tercera categoria

Vigentes en 2026. **UIT 2026: S/ 5,500.**

| Regimen | Tope | Para quien |
|---|---|---|
| **NRUS** | S/ 96,000 al año (S/ 8,000 al mes) | Negocio muy chico, solo boletas. No emite facturas. |
| **RER** | S/ 525,000 al año | Comercio y servicios chicos. Pago mensual sobre ingresos netos. |
| **RMT** | 1,700 UIT (S/ 9,350,000 en 2026) | El intermedio, con tramos progresivos. |
| **Regimen General** | Sin tope | El resto. |

**Cambio de regimen:** de NRUS, RER o RMT hacia uno mayor, en cualquier momento del año. Del General al RMT, **solo en enero**.

La eleccion importa mas de lo que parece: define si puedes emitir factura (y por tanto si le puedes vender a empresas), cuanto pagas y que libros llevas. **Merece un ADR.**

## El cambio grande de 2026: electronico desde el dia uno

Desde el **1 de junio de 2026**, quien se inscribe en el RUC por primera vez bajo RMT, RER o Regimen General — o quien sale del NRUS — queda designado **emisor electronico desde el primer dia** y obligado a llevar sus registros por **SIRE** (RVIE de ventas y RCE de compras) desde el periodo en que nace la obligacion.

Ya no existe el periodo de gracia en papel. Si estas formalizando ahora, esto se planifica desde el inicio.

**SIRE** precarga automaticamente los comprobantes electronicos: revisas, ajustas y confirmas. Reemplaza progresivamente al PLE.

**Actualizacion de RUC:** quienes tienen RUC y no actualizaron correo y celular tienen plazo hasta el **31 de agosto de 2026**.

## Que verificar siempre en la fuente

- **Cronograma de vencimientos** — depende del ultimo digito del RUC y cambia cada año. Publicado por SUNAT.
- **Tasas y topes** — se actualizan con la UIT.
- **Rutas de los menus de SOL** — cambian de nombre seguido. Si no encuentras la ruta descrita, no asumas: busca en la ayuda de SUNAT o hazlo acompañando al usuario en pantalla.

## Marca: Indecopi

**Antes de gastar en publicidad**, descarte de marca. Es gratis y toma diez minutos.

1. Buscador de marcas de Indecopi (`pi.indecopi.gob.pe`), busqueda **fonetica** y denominativa.
2. En **la clase que corresponde** a tu actividad (clasificacion de Niza). Comercio minorista y publicidad suelen ir en clase 35, pero verifica la tuya.
3. Que mirar: marcas identicas o muy parecidas, registradas o en tramite, **en tu clase**. Una marca igual en una clase sin relacion no te bloquea.
4. Si esta limpio y el negocio valida, se presenta la solicitud (tasa por clase, tramite en linea).

Nombre comercial ante SUNAT y marca registrada en Indecopi **son cosas distintas**. El primero no te protege frente a terceros.

## Proteccion al consumidor

Si vendes al publico, aplica el Codigo de Proteccion y Defensa del Consumidor:

- **Libro de Reclamaciones** — obligatorio, tambien en version virtual para comercio electronico. Visible y accesible.
- **Politicas publicadas**: devoluciones, garantia, envios, privacidad de datos.
- **Datos personales** — hay regimen propio de proteccion de datos con obligaciones de registro segun el tratamiento. Verifica si aplica antes de asumir que no.
- **Publicidad no engañosa.** Esto conecta directo con la regla de `/creativos`: una reseña o un descuento inventado por un modelo generativo es publicidad engañosa, con sancion real.

## Estructura legal

**Persona natural con negocio** — se agrega actividad economica al RUC propio. Rapido y barato; el patrimonio personal responde.

**Persona juridica** (E.I.R.L., S.A.C.) — separa patrimonio, permite socios, da mas formalidad frente a clientes empresa. Cuesta mas y obliga a mas.

La eleccion depende del riesgo, de si habra socios y de a quien le vendes. **Es un ADR**, y de los que mas cuesta cambiar despues.

## Como se refleja en la empresa

- `20-legal-y-fiscal/regimen.md` — regimen elegido, desde cuando, por que (con enlace al ADR).
- `20-legal-y-fiscal/obligaciones.md` — que se declara, cuando vence, quien lo hace. Alimenta `/cierre-mensual`.
- `20-legal-y-fiscal/politicas/` — las publicas: privacidad, devoluciones, envios, terminos.
- `30-finanzas/cierres/YYYY-MM/` — constancias de declaracion y pago.

**Todo lo que sea presentar ante el Estado o pagar es solo-humano.** Requiere clave personal, que nunca se comparte (regla 13). El agente prepara los numeros, arma el instructivo y avisa del vencimiento; la persona entra y presenta.

## Fuentes

- SUNAT — `sunat.gob.pe` (regimenes, cronograma, SIRE, comprobantes electronicos)
- Indecopi — `indecopi.gob.pe` y el buscador de marcas
- Detalle operativo en [`references/tramites.md`](references/tramites.md)
