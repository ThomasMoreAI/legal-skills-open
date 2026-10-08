## Resumo

<!-- O que muda e por quê. Para mudanças normativas, cite a norma e o link oficial. -->

## Issue relacionada

Closes #

## Checklist

- [ ] Paridade entre a skill (`SKILL.md`) e o framework modular (`.agents/lgpd-enterprise-auditor/`) verificada.
- [ ] `validation/parity-checklist.md` (e `validation/traceability-matrix.md`, se for o caso) atualizados, se a cobertura mudou.
- [ ] Se mexi em item do checklist: tabela do módulo atualizada, `scripts/update-skill-catalog.sh` rodado e `scripts/tests/test-framework.sh` passando.
- [ ] Se mexi em score, formato do relatório, catálogo ou modelo HTML: relatório de exemplo atualizado (`.md` e `.html`) e `scripts/tests/test-html-report.sh` passando.
- [ ] Entrada adicionada em `## [Não lançado]` no `CHANGELOG.md`.
- [ ] `README.md` e `README.en.md` em sincronia; data de sincronização atualizada nos dois, se a mudança é normativa.
- [ ] Se mexi nos instaladores: `install.sh` e `install.ps1` alterados juntos e testes rodados (`scripts/tests/test-install.sh`, `scripts/tests/test-versions.sh` e, se possível, `scripts/tests/test-install.ps1`).
- [ ] `scripts/tests/run-all.sh` passando na minha máquina.
- [ ] Nenhum dado pessoal, segredo ou trecho de relatório confidencial no diff.
