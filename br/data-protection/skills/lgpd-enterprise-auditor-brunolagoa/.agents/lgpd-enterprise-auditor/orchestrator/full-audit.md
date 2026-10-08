# Auditoria completa (`full_audit`) — cobertura obrigatória

## Objetivo
Definir a cobertura obrigatória do modo `full_audit` e sua equivalência com a skill (`SKILL.md`), a versão autocontida do auditor.

## Skill (`SKILL.md`)
- Arquivo de origem: `SKILL.md`, na raiz do repositório do framework.
- Em um projeto auditado, a skill só existe se tiver sido instalada (opcional no `scripts/install.sh` / `scripts/install.ps1`). Procure nesta ordem:
  1. `.claude/skills/lgpd-enterprise-auditor/SKILL.md` (Claude Code);
  2. `.agents/skills/lgpd-enterprise-auditor/SKILL.md` (Cursor, VS Code + Copilot, OpenCode, Codex, Gemini CLI e similares);
  3. `SKILL.md` na raiz do projeto (cópia manual).
- A ausência da skill não bloqueia a auditoria: o framework modular cobre os 17 domínios abaixo por conta própria.

## Domínios obrigatórios
- O modo `full_audit` cobre os 17 domínios de auditoria, os mesmos da skill:
  1. mapeamento de dados
  2. consentimento
  3. direitos do titular
  4. política de privacidade
  5. cookies e tracking
  6. segurança da informação
  7. cloud security
  8. mobile security
  9. APIs e integrações
  10. DevSecOps
  11. logs e observabilidade
  12. IA/LLM
  13. governança
  14. compartilhamento de dados
  15. retenção e exclusão
  16. proteção de crianças e adolescentes no ambiente digital (ECA Digital — Lei nº 15.211/2025)
  17. plataformas digitais e conteúdo de terceiros (Decretos nº 12.975/2026 e nº 12.976/2026)

## Critérios mínimos de equivalência com a skill
- manter o mesmo catálogo de itens (o da skill é gerado a partir dos módulos);
- manter classificação de severidade em 4 níveis;
- manter score global 0-100, classificação final canônica e teto de classificação por achado crítico;
- manter formato obrigatório do relatório;
- manter exigência de evidência para conclusões.
