# Prompts de prueba — fiscalidad-iva

## 1. Identificación del tipo de IVA

**Prompt**: "Tengo un restaurante en Madrid. ¿Qué tipo de IVA tengo que
aplicar a las comidas que sirvo en el local?"

**Pasa si**: identifica el 10 % (tipo reducido) para servicios de hostelería
y restauración. Puede mencionar que ciertos productos para llevar podrían
tributar al 4 % (alimentos básicos como pan, leche, fruta, verdura) o al
10 % según el caso. No inventa tipos.

**Falla si**: dice que toda la comida es al 4 % o que la hostelería tributa
al 21 %.

---

## 2. Cálculo básico del Modelo 303

**Prompt**: "Este trimestre he cobrado 50.000 € de IVA a mis clientes y he
pagado 30.000 € de IVA a mis proveedores. ¿Cuánto tengo que pagar en el
Modelo 303?"

**Pasa si**: explica que el resultado es 50.000 − 30.000 = 20.000 € a
ingresar y menciona el plazo de presentación del trimestre en curso.

**Falla si**: da un resultado incorrecto, confunde devengado con deducible,
o se niega a hacer el cálculo.

---

## 3. Régimen de recargo de equivalencia

**Prompt**: "Soy minorista (persona física) y mi proveedor me aplica recargo
de equivalencia en las facturas. ¿Tengo que presentar el Modelo 303?"

**Pasa si**: explica que en el régimen de recargo de equivalencia el
minorista **no** presenta Modelo 303 ni lleva libros de IVA, porque el
proveedor ya ingresa el IVA más el recargo. Menciona los porcentajes de
recargo (5,2 %, 1,4 %, 0,5 %).

**Falla si**: le dice que presente el 303 normalmente o ignora la existencia
del régimen de recargo de equivalencia.
