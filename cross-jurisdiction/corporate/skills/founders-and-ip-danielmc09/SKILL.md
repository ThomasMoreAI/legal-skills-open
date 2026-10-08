---
name: founders-and-ip-danielmc09
title: Founders and IP
description: '[JURISDICTION] Estructura el acuerdo entre socios y la cesion de propiedad intelectual de fundadores, empleados y contratistas. Usar antes de que entre un segundo socio, al contratar al primer colaborador, o cuando el codigo o la marca no estan a nombre de la empresa.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/founders-and-ip
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: corporate
language: es
---

# Founders and IP

Los dos errores que aparecen en todas las listas de causas de muerte de una
empresa, y los que menos gente resuelve a tiempo.

## Por qué van juntos en un solo skill

Se rompen juntos. El caso clásico: un cofundador se va al mes ocho, se
lleva su participación completa porque nadie pactó vesting, **y además el
código que escribió sigue siendo legalmente suyo** porque nunca hubo
cesión.

Dos documentos, un solo desastre.

## Requiere

- El pack de la jurisdicción: sección de constitución y de relación laboral
- **Los estatutos, si ya existen** — el acuerdo de socios no los contradice
- Quiénes son las personas y qué aportó cada una

**Si la sección de propiedad intelectual del pack tiene huecos, decláralos
antes de empezar.** Es de las áreas donde más varía la regla por país.

---

# PARTE 1 · El acuerdo entre socios

## No es lo mismo que los estatutos

| Estatutos | Acuerdo entre socios |
|---|---|
| Se registran, son públicos | Privado entre las partes |
| Contenido mínimo lo fija la ley | Contenido libre |
| Regulan la sociedad frente a terceros | Regulan a los socios entre sí |

Un error frecuente: creer que constituir la sociedad resuelve el acuerdo
entre socios. No lo resuelve. Los estatutos casi nunca dicen qué pasa si
alguien se va.

## Las nueve preguntas

Se responden **antes** de que haya algo que repartir. Después, cada una es
una negociación con dinero de por medio.

1. **¿Qué porcentaje tiene cada uno, y por qué?**
   Aporte de capital, de trabajo, de tiempo previo, de red de contactos

2. **¿Hay vesting?**
   ¿La participación se gana con el tiempo, o se entrega completa el día 1?
   Sin vesting, quien se va al mes tres se lleva lo mismo que quien se
   queda cinco años

3. **¿Qué pasa si alguien se va?**
   ¿La sociedad o los demás socios pueden recomprar? ¿A qué precio y con
   qué fórmula? Definirla ahora evita la pelea después

4. **¿Cuánto tiempo dedica cada uno?**
   Tiempo completo, parcial, con otro empleo. **Escríbanlo.** Es la primera
   fuente de resentimiento

5. **¿Quién decide qué?**
   Decisiones diarias, decisiones que exigen mayoría, decisiones que
   exigen unanimidad. Con dos socios al 50/50, definir el desempate no es
   opcional

6. **¿Hay salarios? ¿Desde cuándo? ¿Quién los cambia?**

7. **¿Qué pasa si alguien no cumple lo pactado?**
   Sin consecuencia escrita, el acuerdo es una declaración de intenciones

8. **¿Cómo se resuelve un conflicto entre socios?**

9. **¿Qué pasa si alguien muere o queda incapacitado?**
   Su participación pasa a sus herederos, que pueden no tener ninguna
   relación con el negocio

## Casos que este skill debe detectar y señalar

- **Socio con empleo de tiempo completo en otra parte** → revisar su
  contrato laboral: exclusividad y propiedad intelectual. **Puede que lo
  que construya no sea suyo**
- **Socio que aporta trabajo y no dinero** → cómo se valora, y qué pasa si
  deja de aportarlo
- **Familiar como socio formal** → el acuerdo es más necesario, no menos.
  Las conversaciones difíciles no ocurren y por eso hay que escribirlas
- **Alguien que "ayuda" sin ser socio ni contratista** → figura ambigua.
  Es donde nacen las reclamaciones

`[REDACTAR CON ABOGADO]` Todo lo relacionado con valoración, recompra,
resolución de conflictos y consecuencias por incumplimiento.

---

# PARTE 2 · Propiedad intelectual

## El principio que sorprende a todo el mundo

**Quien crea algo suele ser su titular, salvo que la ley o un contrato
digan otra cosa.** No basta con pagarle a alguien.

Consecuencia: sin cesión escrita, el código, el diseño, el logo y los
textos de tu producto pueden no ser de la empresa.

`[VERIFICAR EN EL PACK]` La regla exacta cambia por país y por tipo de
relación. La sección de relación laboral del pack tiene lo verificado.

## Los cuatro orígenes, y cada uno tiene su regla

| Quién creó | Riesgo típico |
|---|---|
| **Fundador** | Lo creó antes de constituir la sociedad → hay que aportarlo o cederlo expresamente |
| **Empleado** | Suele haber presunción a favor del empleador, **pero con límites** — y el límite es dónde empieza el problema |
| **Contratista o freelance** | **El mayor riesgo.** Sin cláusula de cesión, suele conservar la titularidad |
| **Colaborador informal** | Un amigo que hizo el logo. Sin nada escrito |

## La pregunta que casi nadie hace

**¿Lo que construiste mientras estabas empleado en otra parte es tuyo?**

Muchos contratos laborales tienen cláusulas de propiedad intelectual
amplias. Si construiste el producto durante la vigencia de un contrato así,
la titularidad puede estar en disputa.

**Este skill lo detecta y lo escala. No lo resuelve.** Es de las áreas donde
la redacción concreta del contrato decide el resultado, y donde un error de
lectura cuesta la empresa entera.

Señales para escalar a abogado sin excepción:
- Cláusula de propiedad intelectual en un contrato laboral vigente
- Cláusula de exclusividad
- Obra creada antes de la constitución de la sociedad
- Contratista sin contrato escrito que aportó código, diseño o marca

## Los activos que hay que inventariar

Se hace una lista, no una suposición:

- Código fuente y repositorios — **¿a nombre de quién está la cuenta?**
- Marca, nombre comercial, logo — ¿registrados? ¿por quién?
- Dominios — **a nombre de la empresa o de una persona**
- Diseños, ilustraciones, fotografías
- Textos, documentación, cursos
- Bases de datos
- Cuentas de redes sociales

**El dominio y la cuenta del repositorio son los que más se olvidan y los
que más duelen en una venta.** Ver `exit-readiness` si existe en el
proyecto.

## Salida

```
## Inventario
| Activo | Creado por | Relación | ¿Hay cesión escrita? | Riesgo |

## Sin cesión — actuar
## Cesión dudosa — abogado
## En orden

## Documentos que faltan
- <cuál> · <para quién> · <por qué>
```

---

## Qué NO hacer

- **No redactes el acuerdo entre socios completo.** Estructura las nueve
  preguntas, marca las decisiones, y manda lo vinculante a abogado
- **No opines sobre si una cláusula de PI de un contrato laboral aplica o
  no.** Detecta, señala, escala
- No propongas un porcentaje de reparto entre socios
- No calcules valoraciones ni fórmulas de recompra
- No asumas que la ley cede la PI al empleador. **Verifica en el pack**
- No trates un acuerdo entre familiares como menos formal
