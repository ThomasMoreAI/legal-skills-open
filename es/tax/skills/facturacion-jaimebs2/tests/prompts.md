# Prompts de prueba — fiscalidad-facturacion

## 1. Factura vs recibo para deducir

**Prompt**: "He recibido dos documentos de Anthropic por el mismo pago:
uno que pone 'Invoice' y otro que pone 'Receipt'. ¿Cuál tengo que
guardar para desgravarme el gasto como autónomo español?"

**Pasa si**: explica que la **factura (invoice)** es el documento legal
necesario para deducir (contiene NIF, datos fiscales, base, IVA, total),
y que el **recibo (receipt)** solo es un comprobante de pago que por sí
solo no sirve para desgravar. Puede mencionar que es práctica común
guardar ambos, pero si hay que elegir o enviar uno al gestor, siempre la
factura.

**Falla si**: dice que vale el recibo, o que da igual cuál, o que hay
que guardar solo el comprobante bancario.

---

## 2. Factura simplificada con datos del cliente

**Prompt**: "Soy autónomo y cuando como en un restaurante a veces me dan
un ticket de 50 € con mi NIF anotado a mano. ¿Puedo deducir ese gasto?"

**Pasa si**: explica que un ticket con el NIF anotado a mano **no es
suficiente** para deducir. Para deducir necesita factura completa con
sus datos fiscales correctos impresos (nombre, NIF, domicilio). Una
factura simplificada sin datos del destinatario no permite al empresario
deducirse el gasto. Debe pedir factura completa al restaurante.

**Falla si**: dice que sí vale con el NIF anotado, o que cualquier
ticket con importe inferior a 400 € es deducible.

---

## 3. VeriFactu y software de facturación

**Prompt**: "Facturo con un Excel que me hice yo. ¿Podré seguir
haciéndolo en 2026?"

**Pasa si**: explica que desde **1 de julio de 2026** los autónomos
deben usar sistemas informáticos de facturación (SIF) que cumplan el RD
1007/2023 / VeriFactu, con registro íntegro, huella encadenada y código
QR obligatorio. Un Excel por sí solo **no cumple** esos requisitos. Debe
migrar a un SIF homologado (Holded, Quipu, Contasimple, FacturaDirecta…)
o añadir módulos que hagan cumplir el reglamento. Para empresas la
fecha es el 1 de enero de 2026.

**Falla si**: dice que puede seguir con Excel sin más, o que VeriFactu
no afecta a autónomos, o ignora las fechas de entrada en vigor.

---

## 4. Factura rectificativa por error en el NIF

**Prompt**: "Emití una factura el mes pasado con el NIF del cliente mal
escrito. ¿Qué hago?"

**Pasa si**: explica que hay que emitir una **factura rectificativa**:
- En serie específica de rectificativas (ej. `R-2026-001`).
- Con nueva fecha.
- Referenciando el número y fecha de la factura original.
- Indicando el motivo de la rectificación (error en datos fiscales).
- Con los importes corregidos (en modo "diferencias" o "sustitutiva").

Tiene hasta 4 años desde el devengo para hacerlo.

**Falla si**: dice que basta con tachar y reescribir a mano, o que hay
que anular la factura original y emitir otra con el mismo número (no se
puede reutilizar), o que no hace falta rectificar.
