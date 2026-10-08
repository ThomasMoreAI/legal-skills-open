---
id: DEC-0006
titulo: "Unificación del corpus en un repositorio multietapa"
estado: "Aceptada"
fecha: 2026-04-26
relacionadas: [TAREA-047]
---

# DEC-0006: Unificación del corpus en un repositorio multietapa

## Estado
Aceptada (2026-04-26)

## Contexto
Originalmente, el repositorio fue concebido con un enfoque principal en la Educación Secundaria Obligatoria (ESO). Sin embargo, la interconexión normativa (decretos comunes de currículo para ESO y Bachillerato, órdenes de evaluación comunes para Infantil y Primaria) sugería una fragmentación ineficiente si se mantenían repositorios separados por etapas.

## Decisión
Se decide unificar todas las etapas de la educación no universitaria en Canarias (Infantil, Primaria, ESO, Bachillerato y Formación Profesional) en este único corpus. 

Esto implica:
1. Una estructura de carpetas unificada bajo `03_curriculos/{etapa}/`.
2. Un índice centralizado de fuentes y normativa que permita trazar relaciones entre etapas (ej. el tránsito de 6.º de Primaria a 1.º de ESO).
3. La normalización de los IDs de currículos (`CUR-NNN`) de forma secuencial sin importar la etapa.

## Consecuencias
- **Positivas:** Mayor coherencia documental, eliminación de duplicidad de fuentes estatales, mayor facilidad para sistemas RAG al tener un mapa completo del sistema educativo canario.
- **Negativas:** El repositorio crece en volumen de archivos, requiriendo mayor disciplina en la gestión de índices.
