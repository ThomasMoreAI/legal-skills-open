---
name: contrato-servico-ialabdigital-prog
title: Contrato de Prestação de Serviço
description: Esta skill deve ser usada ao gerar contrato de prestação de serviço para um lead fechado — contrato simples, claro, protegendo ambas as partes. Acione quando o usuário disser "gerar contrato", "contrato de serviço", "fazer contrato" ou rodar /contrato.
author: ialabdigital-prog
author_url: https://github.com/ialabdigital-prog/prospector-iabotz/tree/main/skills/contrato-servico
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
sources:
- title: Contrato Template
  path: references/contrato-template.md
---

# Contrato de Prestação de Serviço

Gera contrato simples, claro, protegendo ambas as partes.

## Dados do Contrato (preencher do lead + conversa de fechamento)

| Campo | Fonte |
|-------|-------|
| `cliente_nome` | Lead (nome fantasia ou razão social) |
| `cliente_cpf_cnpj` | Perguntar no fechamento |
| `cliente_endereco` | Lead (endereco) + confirmar |
| `prestador_nome` | Config `assinatura.nome` |
| `prestador_cpf_cnpj` | Config / perguntar |
| `prestador_endereco` | Config / perguntar |
| `objeto` | "Desenvolvimento de website institucional + página de proposta + deploy + SSL" |
| `valor_total` | Combinado no fechamento (registrado no dashboard `valor`) |
| `valor_entrada` | % ou valor combinado (ex.: 50% na assinatura) |
| `valor_parcelas` | Restante em X parcelas (ex.: 2x mensais) |
| `manutencao_mensal` | Se houver (registrado no dashboard `manutencao`) |
| `prazo_entrega` | Dias úteis após assinatura + recebimento materiais (padrão 15) |
| `vigencia_manutencao` | Meses (padrão 12, renovável) |

## Template (`references/contrato-template.md`)

```markdown
# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE DESENVOLVIMENTO WEB

**CONTRATANTE:** {{cliente_nome}}, {{cliente_cpf_cnpj}}, {{cliente_endereco}}
**CONTRATADO:** {{prestador_nome}}, {{prestador_cpf_cnpj}}, {{prestador_endereco}}

## 1. OBJETO
{{objeto}}. Inclui: estrutura responsiva, SEO on-page, integração WhatsApp, formulário de contato, deploy em servidor do CONTRATADO com SSL, página de proposta (antes/depois), e treinamento básico de edição.

## 2. PRAZO
Entrega em {{prazo_entrega}} dias úteis após: (a) assinatura deste contrato, (b) pagamento da entrada, (c) recebimento de todos os materiais (textos, fotos, logos, credenciais de domínio/hospedagem se aplicável).

## 3. VALOR E PAGAMENTO
- **Total:** R$ {{valor_total}}
- **Entrada ({{valor_entrada_pct}}%):** R$ {{valor_entrada}} — na assinatura
- **Parcelas:** {{parcelas}}x de R$ {{valor_parcela}} — vencimentos mensais a partir da entrega

{% if manutencao_mensal > 0 %}
- **Manutenção mensal (opcional):** R$ {{manutencao_mensal}}/mês — inclui hospedagem, SSL, backups semanais, atualizações de segurança, pequenas alterações de texto/imagem (até 2h/mês). Vigência: {{vigencia_manutencao}} meses, renovável automaticamente.
{% endif %}

Pagamento via PIX (chave informada pelo CONTRATADO) ou transferência. Comprovante = quitação.

## 4. OBRIGAÇÕES DO CONTRATANTE
- Fornecer materiais completos e corretos em até 7 dias da assinatura.
- Aprovar layout/estrutura em até 3 dias úteis após apresentação (silêncio = aprovação).
- Informar alterações de domínio, e-mail ou hospedagem com 30 dias de antecedência.

## 5. OBRIGAÇÕES DO CONTRATADO
- Entregar site funcional, responsivo, com SSL válido, nos prazos acordados.
- Garantir funcionamento por 30 dias pós-entrega (bugs = correção gratuita).
- Manter sigilo de dados e credenciais do CONTRATANTE.

## 6. PROPRIEDADE INTELECTUAL
Código, design e estrutura = propriedade do CONTRATADO (licença de uso perpétua ao CONTRATANTE para o fim contratado). Conteúdo (textos, fotos, marca) = propriedade do CONTRATANTE.

## 7. RESCISÃO
Qualquer parte pode rescindir com 15 dias de aviso prévio. Se o CONTRATANTE rescindir após início: entrada retida + proporcionais aos dias trabalhados. Se o CONTRATADO rescindir: devolve valores pagos integralmente.

## 8. FORO
Foro da comarca de {{cidade_foro}} para dirimir dúvidas.

---

**E, por estarem assim justos e contratados, assinam digitalmente:**

_________________________________________    _________________________________________
{{cliente_nome}}                              {{prestador_nome}}
Data: __/__/____                              Data: __/__/____
```

## Geração

1. Colete dados faltantes (CPF/CNPJ, endereços completos, valores finais, parcelamento).
2. Preencha template → salve como `contratos/[slug]-contrato.md` e `.html` (versão printável).
3. Atualize dashboard: `contratoStatus='enviado'`, `contratoEm=hoje`, `docCliente` (se houver).
4. Oriente envio: anexar no e-mail de proposta (resposta ao lead) ou WhatsApp + assinatura digital (Gov.br, Clicksign, DocuSign — link no contrato).

## Após Assinatura

- Lead confirma assinatura → dashboard: `contratoStatus='assinado'`
- Pagamento entrada confirmado → `pago=1` (parcial) + agendar entrega
- Pagamento total → `pago=1` (total)
