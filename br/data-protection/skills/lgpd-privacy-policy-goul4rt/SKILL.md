---
name: lgpd-privacy-policy-goul4rt
title: Política de Privacidade (Art. 9 LGPD)
description: Draft, version, and publish a privacy policy compliant with LGPD Art. 9 (seven mandatory elements) and ECA Digital if minors are present. Use when user asks "política de privacidade", "privacy policy", "termos de uso", "aviso de privacidade", or as part of an audit pipeline. Versions every published change. Output goes to `.lgpd/policies/privacy-policy-v{N}.md`. CHECKPOINT skill — never publish without legal review.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-privacy-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Política de Privacidade (Art. 9 LGPD)

Documento público que cumpre o dever de informação (Art. 6º, VI — transparência + Art. 9º — direito do titular ao acesso).

## 7 elementos obrigatórios (Art. 9º)

1. **Finalidade específica** do tratamento
2. **Forma e duração** do tratamento
3. **Identificação** do controlador
4. **Contato** do controlador/encarregado
5. **Uso compartilhado** de dados e finalidade
6. **Responsabilidades** dos agentes que realizam o tratamento
7. **Direitos do titular** com menção explícita ao Art. 18

Recomendado adicionar:
8. Versão, data de vigência, changelog
9. Bases legais por finalidade
10. Transferências internacionais
11. Retenção
12. Cookies e tecnologias similares
13. Mudanças e como serão comunicadas

## Linguagem

- **Clara e acessível** (não juridiquês)
- **Em português brasileiro** (ECA Digital exige se houver menores)
- **Versão resumida no topo** (TL;DR) — boa prática emergente
- **Estrutura em camadas** — resumo + detalhe expansível

## Template

Ver `assets/privacy-policy-template.md`.

## Versionamento

Toda mudança material → nova versão. Material = mudança em:
- Finalidades
- Bases legais
- Compartilhamentos novos
- Transferência internacional nova
- Retenção
- Direitos

Mudanças cosméticas (gramática, layout) — micro-versão (v1.0 → v1.0.1).

## Publicação

- Salvar em `.lgpd/policies/privacy-policy-v{N}.md`
- Publicar em URL estável: `/privacy` ou `/politica-de-privacidade`
- Versões antigas acessíveis: `/privacy/v3.1`
- Changelog visível ao titular
- Comunicar mudanças materiais aos titulares ativos (e-mail/in-app)

## ⏸ CHECKPOINT obrigatório

**NUNCA publique sem revisão jurídica.** Após produzir a versão draft:
1. Salve em `.lgpd/policies/privacy-policy-v{N}-draft.md`
2. Notifique o usuário e pause
3. Aguarde aprovação explícita antes de mover para `v{N}.md` (versão final)

## Status update

```markdown
## F4 — Privacy policy ✓
- v{N} draft em `.lgpd/policies/privacy-policy-v{N}-draft.md`
- Aguardando revisão jurídica
- Próximo (pós-aprovação): lgpd-dsar
```
