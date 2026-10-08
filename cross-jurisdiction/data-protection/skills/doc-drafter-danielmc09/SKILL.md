---
name: doc-drafter-danielmc09
title: Doc Drafter
description: '[JURISDICTION] Genera borradores de terminos y condiciones, politica de tratamiento de datos, aviso de privacidad, acuerdo de encargo y manual interno a partir del pack de la jurisdiccion. Usar cuando ya existe el pack del pais y hacen falta los documentos concretos para operar.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/doc-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# Doc Drafter

De "acá está la norma" a "acá está la cláusula".

## Regla número uno

**Todo lo que produce este skill es un BORRADOR PARA ABOGADO.** Cada
documento generado abre con esa advertencia. Sin excepción, sin importar
qué tan completo se vea.

Un borrador que se ve terminado es más peligroso que uno que se ve
incompleto: se publica sin revisar.

## Requiere

- El pack de la jurisdicción en `packs/<iso>.md`
- **Verificar el semáforo de vigencia.** Si el pack está VENCIDO, detente
- Contexto del negocio: qué hace, qué datos trata, con qué arquitectura

**Si el pack está marcado `NO VALIDADO`, cada documento generado lo repite
en su encabezado.**

## Qué genera

| Documento | Cuándo aplica |
|---|---|
| Términos y condiciones | Siempre que haya contrato con clientes |
| Política de tratamiento | Si trata datos personales — obligatoria |
| Aviso de privacidad | Si recoge datos en formularios o canales |
| Acuerdo de encargo | **Solo si es plataforma multi-tenant** |
| Autorización del titular | Si el cliente del cliente aporta datos |
| Manual interno | Si el pack lo exige. **No es la política** |
| Política de retención | Si conserva datos de terceros |

## Procedimiento

### 1. Determinar la arquitectura de roles

Antes de escribir nada:

- ¿Quién decide las finalidades del tratamiento?
- ¿Hay datos de terceros aportados por el cliente?
- ¿La plataforma es Responsable, Encargado, o **ambos**?

**Si es B2B2C, carga la sección multi-tenant del pack.** La cadena
Responsable/Encargado cambia quién responde por qué, y con ella cambian
todos los documentos.

### 2. Mapear norma → cláusula

Por cada obligación del pack, la cláusula que la implementa. **Cada
cláusula cita la línea del pack que la origina.**

```
### <N>. <Título de la cláusula>
<texto de la cláusula>

> Origen: <sección del pack> · <norma> · <URL>
```

Sin origen, la cláusula no se escribe. Es lo que permite auditarla después
y actualizarla cuando cambie la norma.

### 3. Marcar lo que el humano debe decidir

Tres marcas, y ninguna se rellena sola:

| Marca | Significado |
|---|---|
| `[COMPLETAR]` | Dato del negocio: razón social, plazos, precios |
| `[REDACTAR CON ABOGADO]` | Limitación de responsabilidad, indemnidad, jurisdicción |
| `[VERIFICAR]` | Depende de un hueco declarado en el pack |

**Las cláusulas de limitación de responsabilidad e indemnidad nunca se
generan.** Se deja el encabezado y la marca. Es donde se define cuánto
pierde el negocio si algo sale mal, y no es terreno de un borrador
automático.

### 4. Declarar solo lo que existe

En secciones de medidas de seguridad, proveedores y ubicación de datos:
**pregunta qué hay, no supongas.**

```
Cifrado en tránsito:   [preguntar]
Cifrado en reposo:     [preguntar]
Control de acceso:     [preguntar]
Registro de accesos:   [preguntar]
Dónde viven los datos: [preguntar — puede disparar reglas de transferencia
                        internacional]
```

**Declarar una medida que no existe es peor que no declararla.** Convierte
un hueco técnico en una afirmación falsa por escrito.

### 5. Versionar

Todo documento sale con versión y fecha. Cuando cambie, **la versión
anterior no se borra**: quien la aceptó sigue obligado por ella.

## Encabezado obligatorio de todo documento

```
> BORRADOR — requiere revisión de abogado. No constituye asesoría legal.
> Generado a partir de packs/<iso>.md · verificado <fecha> · <VALIDADO POR
> <abogado> | NO VALIDADO>
> Las secciones marcadas [REDACTAR CON ABOGADO] están intencionalmente
> vacías.
```

## Qué NO hacer

- **No generes cláusulas de limitación de responsabilidad ni de indemnidad**
- **No afirmes cumplimiento.** Ningún documento dice "cumple con la ley X".
  Dice qué hace y bajo qué norma
- No inventes plazos. Si el pack lo marcó como hueco, la cláusula lo hereda
- No copies textos de otras jurisdicciones "porque se parecen"
- No rellenes `[COMPLETAR]` con supuestos razonables
- No entregues un documento sin su encabezado de borrador
