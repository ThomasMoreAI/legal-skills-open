# AgendaFácil (projeto fictício de demonstração)

> **Atenção:** este projeto é **fictício** e **intencionalmente falho**. Ele existe apenas para demonstrar o uso do LGPD Enterprise Auditor e **não deve ser usado em produção**, nem como base para um sistema real. A empresa, as pessoas, os CNPJs, os domínios e todos os dados são inventados.

O relatório gerado pelo framework para este projeto está em [`relatorio-auditoria-lgpd.md`](relatorio-auditoria-lgpd.md). A versão visual, com os mesmos dados, está em [`relatorio-auditoria-lgpd.html`](relatorio-auditoria-lgpd.html): baixe o arquivo e abra no navegador.

## O que é

O AgendaFácil é um sistema de agendamento on-line para pequenas clínicas. Cada clínica tem uma página pública (`/?clinica=<slug>`) em que o próprio paciente marca a consulta. A equipe da clínica consulta a agenda do dia e corrige dados cadastrais pelo painel (API autenticada).

## Contexto da empresa (fictício)

- **Razão social:** AgendaFácil Tecnologia Ltda. (CNPJ 00.000.000/0001-00, fictício), São Paulo/SP.
- **Porte:** microempresa optante pelo Simples Nacional, com 3 sócios e nenhum funcionário; atua com fins econômicos.
- **Clientes:** cerca de 40 clínicas de fisioterapia e de clínica médica que atendem **apenas pacientes adultos**, com cerca de 25 mil pacientes cadastrados no total.
- **Contratação:** as clínicas assinam o serviço on-line, pelo site.

## Arquitetura

- **Back-end:** Node.js 20 + Express 5 (`api/index.js`, `src/`), autenticação por JWT.
- **Front-end:** páginas estáticas em `public/`.
- **Hospedagem:** PaaS Vercel; funções na região `gru1` (São Paulo) e arquivos estáticos servidos pela CDN da plataforma (`vercel.json`).
- **Banco de dados:** Postgres gerenciado na região `sa-east-1` (São Paulo), esquema em `db/schema.sql`.
- **Integrações:** Meta Pixel na página de agendamento, para campanhas de aquisição.
- **CI/CD:** GitHub Actions (`.github/workflows/ci.yml`), com deploy na Vercel a cada push na `main`.

## Dados tratados

Nome, CPF, telefone, e-mail, data de nascimento e motivo da consulta (texto livre, opcional) dos pacientes; e-mail e senha (hash) dos usuários das clínicas.

## Como rodar (apenas para leitura do código)

O projeto não acompanha banco de dados, lockfile nem testes reais. Ele serve para ser **lido e auditado**, não executado. Se quiser experimentar localmente, copie `.env.example` para `.env`, aponte para um Postgres de teste com `db/schema.sql` e rode `npm install && npm run dev`, sempre com dados fictícios.
