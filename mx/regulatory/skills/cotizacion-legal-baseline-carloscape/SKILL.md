---
name: cotizacion-legal-baseline-carloscape
title: Clausulado base de cotización (México B2B)
description: 'Baseline Mexico B2B legal clauses that EVERY quote or proposal carries from draft 1: intellectual property, LFPDPPP, confidentiality, liability cap, warranty, licensing and VAT.'
author: CarlosCaPe
author_url: https://github.com/CarlosCaPe/octorato/tree/master/skills/cotizacion-legal-baseline
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: mx
practice: regulatory
language: es
---

# Clausulado base de cotización (México B2B)

**Por qué existe.** En una sesión, un review de 6 especialistas tuvo que agregar
cláusulas legales que el primer borrador omitía (PI, LFPDPPP, límite de
responsabilidad). Una cotización de servicios debe **nacer** con este clausulado,
no adquirirlo por suerte. Operacionaliza el canon "legal & copyright always-on".

Inserta una sección **Términos y Condiciones** con estos bloques (ajusta nombres
de partes y montos; el resto es boilerplate genérico). Revisión jurídica formal
sigue siendo del operador; esto es piso profesional, no asesoría legal.

### Propiedad Intelectual
El desarrollo se realiza bajo la figura de **obra por encargo**. Cubierto el pago
total, el cliente adquiere los derechos patrimoniales sobre la aplicación, los
datos, los flujos y los reportes desarrollados específicamente para el proyecto.
El proveedor conserva la titularidad de sus **componentes preexistentes**
(librerías, plantillas, métodos genéricos) y se reserva el derecho de reutilizarlos.
*(Por defecto, Art. 84 LFDA deja la titularidad en el autor; sin esta cláusula el código no queda del cliente.)*

### Tratamiento de Datos Personales (LFPDPPP)
Cuando el sistema procese datos personales de terceros (empleados, clientes del
cliente), el cliente es el **responsable** y el proveedor el **encargado** conforme
al **Art. 50 del Reglamento de la LFPDPPP**. El proveedor usa los datos solo para
el desarrollo/pruebas/entrega contratados, no los comparte y los elimina de sus
entornos al cierre. El cliente es responsable de que su Aviso de Privacidad
contemple el tratamiento. A solicitud, se formaliza convenio de encargo.
**Un NDA NO sustituye esto.** Acordar antes de recibir cualquier dataset con datos personales.

### Confidencialidad
Aplica el NDA firmado y vigente, **citado por fecha** y confirmado que cubre el
alcance del proyecto. Datos, estructura y código entregado son confidenciales.

### Limitación de Responsabilidad
La responsabilidad total del proveedor no excede el monto efectivamente pagado.
No responde por daños indirectos, lucro cesante ni pérdida de datos posterior a la
entrega y aceptación.

### Garantía y Soporte Post-Entrega
Corrección sin costo de defectos de construcción de lo entregado por **N días
hábiles** tras la aceptación del UAT. Fuera de garantía: cambios de plataforma del
proveedor de nube, cambios organizacionales del cliente, fallos por licenciamiento
no contratado, y funciones fuera de alcance. Soporte extendido se cotiza aparte.

### Licenciamiento
El licenciamiento de terceros (ej. Power Apps Premium, Dataverse) es
responsabilidad y costo del cliente. El trabajo que dependa de esa licencia no
inicia sin confirmación de su adquisición; el proveedor no asume retrasos por su
no contratación oportuna.

### Impuestos (IVA)
Todos los montos de la propuesta se expresan **más IVA** (16%, tasa general de la
Ley del IVA); el impuesto se desglosa en la factura CFDI. La nota va junto al monto
principal Y en las condiciones de pago, nunca solo en una. Sin ella, el cliente
puede leer el precio como IVA incluido y emitir la orden de compra por el bruto: el
proveedor absorbe ~13.79% del monto (x/1.16). Si la aclaración llega después del
envío, se corrige por escrito en el mismo hilo ANTES de que se emita la OC.
`client-doc-lint` marca FAIL cualquier doc con montos $ y cero menciones de IVA.

### Pago y tipo de cambio (si aplica USD→MXN)
Plazo claro: "N días naturales desde la factura del anticipo y, para el saldo,
desde el **acta de aceptación del UAT firmada**." Ajuste cambiario **por
exhibición**, FIX Banxico del día hábil anterior a cada transferencia, recalculo si
la variación supera 5%. Facturación CFDI 4.0.

---
Antes de enviar, pasa el doc por [[client-doc-lint]]. Relacionado:
[[financial-formula-verification]], [[legal-compliance]] (si existe), canon "legal & copyright always-on".
