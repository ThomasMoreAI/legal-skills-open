---
name: juridico-advocacia-ricneves-ai
title: Jurídico & Advocacia (Nível PODEROSO)
description: 'Skills para advogados e gestores jurídicos: petições, contratos, captação de clientes, precificação e conformidade com o direito brasileiro. Use quando precisar estruturar documentos jurídicos, estratégias para escritórios de advocacia ou orientação sobre legislação brasileira.'
author: ricneves-ai
author_url: https://github.com/ricneves-ai/flowgrammers-skills/tree/main/juridico-advocacia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
tags: [juridico, advocacia, contratos, peticoes, lgpd, oab, cdc, trabalhista]
---

# Jurídico & Advocacia (Nível PODEROSO)

Skills para advogados, gestores jurídicos e empreendedores que lidam com questões legais no Brasil. Cobrindo desde a estruturação de petições e contratos até estratégias de captação de clientes dentro dos limites éticos da OAB, precificação de serviços jurídicos e adequação à legislação brasileira vigente.

Este domínio respeita os limites do exercício da advocacia: o agente auxilia na estrutura, linguagem e organização — a responsabilidade técnica e a assinatura são sempre do advogado habilitado.

---

## Início Rápido

### Claude Code
```
/read /caminho/juridico-advocacia/SKILL.md
> Estruture uma petição inicial de cobrança de honorários advocatícios não pagos no Juizado Especial
```

### Cursor
Adicione ao `.cursor/rules/juridico-advocacia.md` e use:
```
@juridico-advocacia Preciso de um contrato de prestação de serviços jurídicos para cliente PJ
```

### Codex
Inclua no `AGENTS.md`:
```
Contexto jurídico: use as diretrizes de juridico-advocacia para tarefas que envolvam documentos legais, 
estratégias para escritórios e conformidade com o direito brasileiro.
```

### Windsurf
Em **Settings > AI Rules**, adicione o conteúdo de `SKILL.md` e então:
```
Com base nas skills de juridico-advocacia, crie uma estratégia de captação de clientes 
para escritório de direito trabalhista respeitando o Código de Ética da OAB
```

---

## Visão Geral das Skills

| Skill | Pasta | Foco |
|-------|-------|------|
| Petição Inicial | `peticao-inicial/` | Estrutura de petições, contestações e recursos |
| Contrato de Serviços | `contrato-servicos/` | Contratos de prestação de serviços conforme CC/CDC BR |
| Captação de Clientes | `captacao-clientes/` | Estratégias respeitando o Código de Ética da OAB |
| Honorários | `honorarios/` | Tabela de honorários e precificação de serviços jurídicos |
| LGPD Jurídico | `lgpd-juridico/` | Adequação LGPD para escritórios: contratos, políticas, DPA |
| Trabalhista | `trabalhista/` | CLT, reforma trabalhista, TST, dissídio e acordos |
| Empresarial | `empresarial/` | Constituição de empresa, alterações societárias, SIMPLES |
| Consumidor | `consumidor/` | CDC, Procon, Reclame Aqui, mediação de conflitos |
| Rotina do Escritório | `rotina-escritorio/` | SOP para advocacia solo e boutique: prazos, agenda, clientes |
| Marketing Jurídico | `marketing-juridico/` | Marketing permitido pela OAB: LinkedIn, Instagram, WhatsApp |

---

## Exemplos de Uso

### Petição Inicial
```
Preciso estruturar uma petição inicial de ação de cobrança no JEC (Juizado Especial Cível) 
para reclamar honorários não pagos de R$ 8.000 por cliente PJ. 
Inclua: qualificação das partes, fatos, direito aplicável e pedidos.
```

### Contrato de Serviços
```
Crie um contrato de prestação de serviços jurídicos para atendimento a pessoa jurídica 
(empresa de tecnologia, SIMPLES Nacional) em matéria trabalhista preventiva. 
Inclua: objeto, honorários, forma de pagamento, confidencialidade e rescisão.
```

### Captação de Clientes
```
Sou advogada especialista em direito de família. Crie uma estratégia de captação 
de clientes via Instagram e LinkedIn respeitando o Código de Ética da OAB. 
Inclua: tipo de conteúdo permitido, frequência e o que é vedado.
```

### LGPD Jurídico
```
Preciso adequar meu escritório de advocacia à LGPD. Temos dados de 200+ clientes 
armazenados em planilhas. Crie um plano de adequação com: inventário de dados, 
cláusulas contratuais, política de privacidade e procedimentos internos.
```

### Trabalhista
```
Meu cliente tem uma empresa com 15 funcionários CLT e quer implantar banco de horas 
e home office parcial. Quais são os requisitos legais, riscos e como documentar 
corretamente conforme a CLT e a Reforma Trabalhista?
```

### Marketing Jurídico
```
Crie um calendário de conteúdo para 30 dias no LinkedIn para um advogado especialista 
em direito empresarial, respeitando as normas da OAB. 
Inclua: tipo de post, tema, formato e chamadas para ação permitidas.
```

---

## Contexto Brasileiro

- **OAB e Código de Ética**: toda estratégia de marketing deve respeitar a Resolução 02/2021 do CFOAB — vedado: autopromoção excessiva, promessa de resultado, captação irregular
- **Legislação vigente**: CC/2002, CDC, CLT, LGPD (Lei 13.709/2018), Marco Civil da Internet, Reforma Trabalhista (Lei 13.467/2017)
- **Tribunais digitais**: PROJUDI, PJe, e-SAJ — mencionar sempre o sistema do tribunal ao estruturar peças
- **JEC**: limite atual de 40 salários mínimos; causas até 20 SM dispensa advogado, mas sua presença é recomendada
- **Honorários de sucumbência**: regidos pelo art. 85 do CPC/2015 — percentual de 10% a 20% sobre o proveito econômico
- **SIMPLES Nacional para escritórios**: escritórios individuais podem ser MEI ou Simples; sociedades de advogados têm regime especial
- **Sigilo profissional**: Art. 7º do EOAB — qualquer sistema ou processo que envolva dados de clientes deve reforçar o sigilo
- **Prazos processuais**: contagem em dias úteis (CPC/2015, art. 219); atenção a feriados forenses locais

---

## Configuração de Harness

### Claude Code (CLAUDE.md)
```markdown
## Jurídico & Advocacia
Ao lidar com tarefas jurídicas:
- Use a skill juridico-advocacia para estrutura e linguagem
- Sempre reforçar que o conteúdo é orientativo e não substitui consulta jurídica
- Referenciar a legislação brasileira vigente (CC, CLT, CDC, LGPD, CPC/2015)
- Respeitar os limites éticos da OAB em estratégias de captação e comunicação
```

### Cursor (.cursorrules)
```
# Jurídico & Advocacia Rules
- Para documentos jurídicos: seguir estrutura da skill juridico-advocacia
- Sempre incluir referências legais (artigos, leis, resoluções)
- Alertar sobre necessidade de revisão por advogado habilitado
- Respeitar Código de Ética da OAB em qualquer estratégia de comunicação
```

### Codex (AGENTS.md)
```markdown
## Agente Jurídico
Especialidade: documentos jurídicos, estratégias para escritórios e conformidade com direito BR.
Referências obrigatórias: CC/2002, CLT, CDC, LGPD, CPC/2015, EOAB, Resoluções OAB.
Sempre incluir aviso: conteúdo orientativo, não substitui consulta com advogado.
```

### Windsurf (AI Rules)
```
Jurídico & Advocacia: use as skills deste domínio para estruturar documentos legais,
estratégias para escritórios e conformidade com o direito brasileiro. Sempre referenciar
legislação vigente e respeitar o Código de Ética da OAB.
```

---

## Regras

1. **Aviso obrigatório**: toda entrega deve conter nota de que o conteúdo é orientativo e não substitui consulta com advogado habilitado inscrito na OAB
2. **Referenciar legislação**: sempre citar artigos e leis específicas (ex.: "art. 85, §2º, CPC/2015") — precisão jurídica é inegociável
3. **Respeitar o Código de Ética da OAB**: nunca sugerir estratégias de captação vedadas, promessas de resultado ou autopromoção excessiva
4. **Linguagem técnica correta**: usar nomenclatura jurídica brasileira precisa — "exequente/executado", "litisconsorte", "jus postulandi" conforme o contexto
5. **Adaptar ao tribunal**: peças processuais devem ser adaptadas ao sistema (PJe, e-SAJ, PROJUDI) e comarca onde tramitarão
6. **LGPD em dados de clientes**: qualquer processo interno do escritório que envolva dados pessoais de clientes deve incluir medidas de proteção
7. **Atualização legislativa**: sempre verificar se a legislação referenciada está vigente — mencionar se houve alterações recentes relevantes
8. **Separar orientação de advocacia**: o agente estrutura, organiza e sugere; a responsabilidade técnica e a assinatura são exclusivamente do advogado
9. **Contratos equilibrados**: ao redigir contratos, verificar cláusulas abusivas conforme CDC e CC — especialmente em relações B2C
10. **Sigilo absoluto**: nunca solicitar dados reais de clientes para exemplificar; usar dados fictícios em todos os modelos e exemplos
