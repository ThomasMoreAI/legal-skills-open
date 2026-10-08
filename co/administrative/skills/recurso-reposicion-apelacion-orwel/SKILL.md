---
name: recurso-reposicion-apelacion-orwel
title: Recursos en Vía Gubernativa — Colombia
description: Redacta recursos de reposición y apelación contra actos administrativos colombianos. Usar cuando el usuario necesite impugnar una decisión de una entidad pública, contestar una resolución sancionatoria, recurrir una multa, o ejercer el derecho de contradicción en vía gubernativa.
author: Orwel
author_url: https://github.com/Orwel/legal-skills-colombia-juandatrifuerza/tree/main/jurisdicciones/colombia/derecho-administrativo/recurso-reposicion-apelacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: co
practice: administrative
language: es
---

# Recursos en Vía Gubernativa — Colombia

Eres un experto en procedimiento administrativo colombiano con dominio del CPACA y la jurisprudencia del Consejo de Estado.

## Vía gubernativa — concepto y función

La vía gubernativa es el mecanismo de control interno de la administración. Antes de acudir a la jurisdicción contencioso administrativa, el administrado debe agotar la vía gubernativa interponiendo los recursos disponibles contra el acto que lo afecta.

**Fundamento constitucional:** Art. 29 C.P. — derecho de contradicción y debido proceso administrativo.

## Recursos disponibles (Art. 74 CPACA)

### Recurso de reposición
- **Ante quién:** el mismo funcionario que expidió el acto
- **Objeto:** que revoque, aclare o modifique el acto
- **Término para interponer:** 10 días hábiles desde la notificación
- **Término para resolver:** 1 mes desde su interposición
- **Es opcional** — no es requisito previo para la apelación

### Recurso de apelación
- **Ante quién:** el superior jerárquico del funcionario que expidió el acto
- **Objeto:** que revoque, modifique o aclare el acto
- **Término para interponer:** 10 días hábiles desde la notificación
- **Término para resolver:** 2 meses desde su interposición
- **Puede interponerse:** solo o subsidiariamente con la reposición
- **Agota la vía gubernativa** cuando el superior lo resuelve (o guarda silencio)

### Recurso de queja
- Procede cuando se deniega el recurso de apelación
- Ante el superior del funcionario que negó la apelación
- Término: 5 días hábiles desde la notificación de la denegación

## ¿Cuándo NO procede la apelación?
- Cuando el acto fue expedido por el jefe del organismo (no tiene superior jerárquico para efectos administrativos)
- Cuando la ley expresamente lo excluye

En estos casos, la reposición agota la vía gubernativa.

## Estructura del recurso

### 1. Encabezado
```
[Ciudad], [fecha]

Señor(a)
[Cargo del funcionario destinatario]
[Entidad]
[Ciudad]

Ref.: Recurso de [reposición / apelación / reposición y en subsidio apelación]
contra [identificación del acto: número, fecha, contenido]
```

### 2. Identificación del recurrente
Nombre, identificación, dirección, correo, calidad en que actúa (directamente o por apoderado).

### 3. Identificación del acto recurrido
- Número o referencia del acto
- Fecha de expedición
- Fecha de notificación
- Contenido de la decisión impugnada

### 4. Oportunidad
Manifestar expresamente que el recurso se interpone dentro del término legal de 10 días hábiles desde la notificación.

### 5. Causales de impugnación

**Por infracción de norma superior:**
"El acto viola el artículo [X] de [norma] porque [explicación]..."

**Por falsa motivación:**
"Los hechos en que se fundamenta el acto no son ciertos / fueron tergiversados porque [evidencia]..."

**Por incompetencia:**
"El funcionario que expidió el acto no tenía competencia para hacerlo porque [fundamento]..."

**Por violación del debido proceso:**
"En la expedición del acto se omitió [trámite / notificación / audiencia] exigido por [norma]..."

**Por desproporción de la sanción:**
"La sanción impuesta es desproporcionada frente a la infracción porque [argumentos]..."

### 6. Pruebas
Documentos, testimonios o indicios que sustentan los argumentos del recurso.

### 7. Petición concreta
```
En mérito de lo expuesto, solicito respetuosamente:

PRIMERO: Que se admita el presente recurso de [reposición / apelación].

SEGUNDO: Que se [revoque totalmente / modifique en el siguiente sentido / aclare] 
el acto administrativo [identificación], por las razones expuestas.

[Si es subsidio de apelación:]
TERCERO: En subsidio, si se niega la reposición, elévese el expediente al superior 
jerárquico para que resuelva el recurso de apelación.
```

### 8. Notificaciones
Dirección y correo electrónico.

## Silencio administrativo en vía gubernativa

Si la entidad no resuelve el recurso dentro del término legal:
- Opera el **silencio administrativo negativo**
- Se entiende que el recurso fue negado
- Queda agotada la vía gubernativa
- El recurrente puede acudir a la jurisdicción contencioso administrativa

**Importante:** el silencio no impide que la entidad resuelva tardíamente — si lo hace, el administrado puede demandar ese acto tardío si lo afecta.

## Efectos de la interposición del recurso

- Suspende los efectos del acto impugnado mientras se resuelve (Art. 87 CPACA)
- Interrumpe el término de caducidad de la acción contencioso administrativa
- Obliga a la entidad a resolver dentro del término legal

## Acto administrativo ficto — silencio positivo

En algunos procedimientos especiales (licencias de construcción, permisos ambientales con términos específicos), el silencio de la administración implica la aprobación de la solicitud. Verificar siempre la norma especial aplicable al procedimiento.

## Errores comunes que debes evitar
- No interponer el recurso fuera del término de 10 días hábiles — es fatal, la oportunidad se pierde
- No confundir la reposición (ante el mismo funcionario) con la apelación (ante el superior) — son recursos distintos
- No omitir la manifestación expresa de que el recurso se interpone en tiempo — la entidad debe verificar la oportunidad
- No olvidar que la interposición del recurso suspende los efectos del acto — el recurrente no debe cumplir el acto mientras se resuelve
- No agotar la vía gubernativa incorrectamente — si hay apelación disponible y no se interpone, puede quedar trabada la acción contencioso administrativa
