# Política de Segurança

## Versões suportadas

Apenas a **última versão publicada** (release mais recente) recebe correções de segurança. Antes de relatar, confirme que o problema ocorre nela.

## Como relatar uma vulnerabilidade

**Não abra issue pública.** Use o relato privado do GitHub:

1. Acesse a aba **Security** do repositório.
2. Clique em **Report a vulnerability**.
3. Descreva o problema, o impacto, os passos para reproduzir, a versão afetada e o sistema/shell utilizado.

Não inclua dados pessoais reais, segredos ou trechos de relatórios confidenciais no relato; use dados fictícios.

## Escopo

Dentro do escopo:

- os instaladores `scripts/install.sh` e `scripts/install.ps1` (por exemplo: escrita ou remoção de arquivos fora do projeto, execução de código não pretendida, falhas de validação de caminho ou do manifesto em `.agents/lgpd-enterprise-auditor/.install/`);
- qualquer instrução da skill, do framework ou dos comandos que possa levar o assistente de IA a vazar dados do projeto auditado ou a executar ações não pretendidas (por exemplo: enviar conteúdo a serviços externos, modificar arquivos ou rodar comandos sem que o usuário peça).

Fora do escopo:

- achados produzidos pelo auditor sobre projetos de terceiros (trate-os com o responsável por aquele projeto);
- divergências de interpretação jurídica ou lacunas de cobertura normativa (abra uma issue comum);
- vulnerabilidades das próprias ferramentas de IA (Claude Code, Cursor, Copilot etc.), que devem ser relatadas aos respectivos fornecedores.

## O que esperar

- **Meta** de confirmação de recebimento em até 7 dias, em regime de melhor esforço (o projeto é mantido por voluntários, então não há garantia de prazo).
- Após a análise, você será informado se o relato foi aceito, do plano de correção e da versão que a conterá.
- Pedimos que a vulnerabilidade não seja divulgada publicamente até a publicação da correção. Com sua autorização, o crédito será dado nas notas da versão.
