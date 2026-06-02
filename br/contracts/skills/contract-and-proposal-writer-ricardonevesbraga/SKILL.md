---
name: contract-and-proposal-writer-ricardonevesbraga
title: Redator de Contratos e Propostas — Brasil
description: Gerador de contratos e propostas comerciais para o mercado brasileiro. Contratos de prestação de serviço, proposta comercial, SOW, NDA, MSA — todos adaptados à legislação brasileira (Código Civil, CLT, LGPD). Use quando precisar criar contratos de desenvolvimento, propostas para clientes, acordos de confidencialidade, contratos de consultoria ou contratos de parceria comercial.
author: ricardonevesbraga
author_url: https://github.com/ricardonevesbraga/flowgrammers-skills/tree/main/business-growth/contract-and-proposal-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Redator de Contratos e Propostas — Brasil

Gerador de documentos comerciais profissionais adaptados à **legislação brasileira**: contratos de prestação de serviços, propostas comerciais, SOWs, NDAs e MSAs.

> ⚠️ **Aviso Legal:** Estes templates são pontos de partida. Para contratos de alto valor ou situações complexas, consulte um advogado.

---

## Visão Geral

Cobre os principais tipos de documentos comerciais no Brasil:
- Contrato de Prestação de Serviços (PJ × PJ / PF × PJ)
- Proposta Comercial com detalhamento de escopo e prazo
- Statement of Work (SOW) com matriz de entregáveis
- NDA — Acordo de Confidencialidade (bilateral e unilateral)
- MSA — Acordo-Quadro de Serviços
- Adendo de Tratamento de Dados (LGPD)

---

## Referência de Cláusulas Principais

| Cláusula | Opções |
|----------|--------|
| Pagamento | À vista, parcelado (boleto/PIX/cartão), por marco, retainer mensal |
| Propriedade intelectual | Cessão total ao cliente, licença de uso, obra por encomenda (Art. 4º Lei 9.609/98) |
| Limite de responsabilidade | 1x valor do contrato (padrão), 3x (alto risco) |
| Rescisão | Por justa causa (prazo de cura 15 dias), sem justa causa (aviso prévio 30/60/90 dias) |
| Confidencialidade | Prazo de 2-5 anos, perpétua para segredos comerciais |
| Garantia | Isenção "no estado em que se encontra", garantia limitada 30/90 dias para defeitos |
| Resolução de disputas | Mediação → Arbitragem (CAMARB/FIESP) ou Foro da comarca do contratante |
| Regime tributário | MEI, Simples Nacional, Lucro Presumido, Lucro Real |

---

## Quando Usar

- Iniciar um novo projeto com cliente e precisar de contrato rápido
- Cliente solicitar proposta com precificação e cronograma
- Parceria ou relação com fornecedor exigindo MSA
- Proteger IP ou informações confidenciais com NDA
- Projeto envolvendo dados pessoais que exige adendo LGPD

---

## Fluxo de Trabalho

### 1. Coletar Requisitos

Perguntar ao usuário:

```
1. Tipo de documento? (contrato / proposta / SOW / NDA / MSA)
2. Tipo de engajamento? (projeto fixo / hora trabalhada / retainer mensal)
3. Partes? (nomes, CNPJ/CPF, endereços)
4. Resumo do escopo? (1-3 frases)
5. Valor total ou taxa horária?
6. Data de início / término ou duração?
7. Forma de pagamento? (PIX / boleto / cartão / transferência)
8. Requisitos especiais? (cessão de IP, white-label, subcontratados, LGPD)
9. Prestador é MEI, PJ ou PF?
```

### 2. Selecionar Template

| Tipo | Contexto | Template |
|------|----------|----------|
| Contrato dev preço fixo | PJ × PJ | Template A |
| Retainer de consultoria | PJ × PJ | Template B |
| Parceria SaaS | PJ × PJ | Template C |
| NDA bilateral | Qualquer | NDA-B |
| NDA unilateral | Qualquer | NDA-U |
| SOW | Qualquer | SOW base |

### 3. Gerar e Preencher

Preencher todos os campos [ENTRE COLCHETES]. Sinalizar dados ausentes como "OBRIGATÓRIO".

### 4. Converter para DOCX

```bash
# Instalar pandoc
brew install pandoc        # macOS
apt install pandoc         # Ubuntu

# Conversão básica
pandoc contrato.md -o contrato.docx \
  --reference-doc=referencia.docx \
  -V geometry:margin=2.5cm

# Com seções numeradas (estilo jurídico)
pandoc contrato.md -o contrato.docx \
  --number-sections \
  -V documentclass=article \
  -V fontsize=11pt
```

---

## Template A: Contrato de Desenvolvimento Web (Preço Fixo)

```markdown
# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE DESENVOLVIMENTO DE SOFTWARE

**Data de Celebração:** [DATA]
**Contratante:** [NOME/RAZÃO SOCIAL DO CLIENTE], inscrito(a) no CNPJ/CPF nº [CNPJ/CPF],
  com sede/domicílio em [ENDEREÇO COMPLETO] ("Contratante")
**Contratado:** [SEU NOME/RAZÃO SOCIAL], inscrito(a) no CNPJ/CPF nº [SEU CNPJ/CPF],
  com sede/domicílio em [SEU ENDEREÇO] ("Contratado")

---

## CLÁUSULA 1ª — DO OBJETO

O Contratado obriga-se a projetar, desenvolver e entregar:

**Projeto:** [NOME DO PROJETO]
**Descrição:** [Descrição do escopo em 1-3 frases]

**Entregáveis:**
- [Entregável 1] — prazo: [DATA]
- [Entregável 2] — prazo: [DATA]
- [Entregável 3] — prazo: [DATE]

## CLÁUSULA 2ª — DO PREÇO E FORMA DE PAGAMENTO

**Valor Total:** R$ [VALOR]

| Marco | Valor | Vencimento |
|-------|-------|-----------|
| Assinatura do contrato | 50% | Na assinatura |
| Entrega da versão beta | 25% | [DATA] |
| Aceite final | 25% | Em até 5 dias após aceite |

**Forma de pagamento:** [PIX / Boleto bancário / Transferência TED/DOC]
**Chave PIX do Contratado:** [CHAVE PIX]

O atraso no pagamento acarretará multa moratória de 2% sobre o valor em atraso,
acrescida de juros de 1% ao mês, nos termos do Art. 395 do Código Civil.

O Contratante tem [10] dias úteis para aceitar ou rejeitar os entregáveis por escrito.
Decorrido o prazo sem manifestação, o aceite será considerado tácito.

## CLÁUSULA 3ª — DA PROPRIEDADE INTELECTUAL

Mediante o recebimento integral do pagamento, o Contratado cede ao Contratante
todos os direitos patrimoniais sobre o produto desenvolvido, nos termos da
Lei nº 9.609/98 (Lei de Software) e Lei nº 9.610/98 (Lei de Direitos Autorais).

O Contratado reserva-se o direito de mencionar o projeto em seu portfólio, salvo
solicitação expressa de confidencialidade pelo Contratante em até [30] dias da entrega.

Ferramentas, bibliotecas e frameworks pré-existentes permanecem de propriedade
do Contratado. Fica concedida ao Contratante licença perpétua e gratuita para
utilizá-los na medida incorporada ao produto entregue.

## CLÁUSULA 4ª — DA CONFIDENCIALIDADE

Cada parte manterá em sigilo todas as informações não públicas recebidas da outra,
nos termos da Lei nº 9.279/96 (Lei de Propriedade Industrial) e do Art. 189 da Lei
nº 11.101/05. Esta obrigação sobrevive à extinção do contrato por [3] anos.

## CLÁUSULA 5ª — DAS GARANTIAS

O Contratado garante que o produto entregue estará substancialmente em conformidade
com as especificações acordadas por [90] dias após a entrega. Defeitos materiais
serão corrigidos gratuitamente neste período. Ressalvado o exposto, o produto
é entregue "no estado em que se encontra".

## CLÁUSULA 6ª — DA RESPONSABILIDADE

A responsabilidade total do Contratado não excederá o valor total dos honorários
pagos sob este contrato. Nenhuma das partes será responsável por danos indiretos,
incidentais ou consequentes.

## CLÁUSULA 7ª — DA RESCISÃO

**Por justa causa:** Qualquer parte pode rescindir se a outra descumprir
materialmente o contrato e não sanar a falta em [15] dias após notificação escrita.

**Sem justa causa:** O Contratante pode rescindir com aviso prévio de [30] dias
e deverá pagar por todo o trabalho concluído acrescido de [10%] do valor restante.

## CLÁUSULA 8ª — DA RELAÇÃO ENTRE AS PARTES

O Contratado é prestador de serviços autônomo, não havendo entre as partes qualquer
vínculo empregatício, societário ou de representação. O Contratado é responsável
por seus próprios tributos e contribuições previdenciárias.

*[Se MEI: O Contratado declara ser Microempreendedor Individual (MEI), CNPJ nº [CNPJ],
e é responsável pelo recolhimento do DAS mensalmente.]*

## CLÁUSULA 9ª — DO TRATAMENTO DE DADOS (LGPD)

Na hipótese de o Contratado ter acesso a dados pessoais de titulares do Contratante
no curso dos serviços, o Contratado atuará como operador nos termos do Art. 5º, VII
da Lei nº 13.709/18 (LGPD), processando os dados apenas conforme instruções documentadas
do Contratante e adotando medidas técnicas e organizacionais adequadas à sua proteção.

## CLÁUSULA 10ª — DO FORO

As partes elegem o foro da comarca de [CIDADE/ESTADO DO CONTRATANTE] para dirimir
quaisquer controvérsias decorrentes deste contrato, com renúncia expressa a qualquer
outro, por mais privilegiado que seja.

*[Opcional — Para contratos de maior valor:]*
*As partes acordam em submeter eventuais litígios à arbitragem perante a*
*[CÂMARA DE ARBITRAGEM — ex: CAMARB, FIESP, CAM-CCBC], nos termos da Lei nº 9.307/96.*

## CLÁUSULA 11ª — DAS DISPOSIÇÕES GERAIS

- **Instrumento completo:** Substitui todos os acordos anteriores sobre o mesmo objeto.
- **Alterações:** Devem ser feitas por escrito e assinadas por ambas as partes.
- **Invalidade parcial:** A invalidade de uma cláusula não invalida as demais.

---

CONTRATANTE: _________________________ Data: _________
[NOME DO CLIENTE], [CARGO]
CNPJ: [CNPJ]

CONTRATADO: _________________________ Data: _________
[SEU NOME], [CARGO]
CNPJ/CPF: [SEU CNPJ/CPF]

Testemunha 1: _________________________ CPF: _________
Testemunha 2: _________________________ CPF: _________
```

---

## Template B: Retainer de Consultoria Mensal

```markdown
# CONTRATO DE CONSULTORIA — RETAINER MENSAL

**Data:** [DATA]
**Contratante:** [NOME/RAZÃO SOCIAL], CNPJ [CNPJ] ("Contratante")
**Consultor:** [NOME/RAZÃO SOCIAL], CNPJ [CNPJ] ("Consultor")

## 1. DOS SERVIÇOS

O Consultor prestará serviços de [ÁREA, ex: "consultoria em CTO e arquitetura técnica"].

**Horas mensais:** Até [X] horas/mês
**Hora adicional:** R$ [VALOR]/hora para horas excedentes ao pacote
**Acúmulo:** Horas não utilizadas [se acumulam / não se acumulam] (máximo [X] horas)

## 2. DOS HONORÁRIOS

**Retainer mensal:** R$ [VALOR], vencimento todo dia [X] de cada mês
**Pagamento:** PIX [chave] / Boleto bancário / TED
**Multa por atraso:** 2% + juros de 1% ao mês após vencimento

## 3. DO PRAZO E RESCISÃO

**Prazo inicial:** [3] meses a partir de [DATA]
**Renovação:** Automática por iguais períodos, salvo aviso com [30] dias de antecedência
**Rescisão imediata:** Por descumprimento grave não sanado em [7] dias de notificação

Na rescisão, o Consultor entregará todos os trabalhos em andamento em até [5] dias úteis.

## 4. DA PROPRIEDADE INTELECTUAL

Os trabalhos produzidos neste contrato pertencem a [Contratante / Consultor / ambos].
Relatórios, análises e recomendações são propriedade do Contratante após pagamento integral.

## 5. DA EXCLUSIVIDADE

[OPÇÃO A — Não exclusivo:]
Este contrato é não exclusivo. O Consultor pode atender outros clientes.

[OPÇÃO B — Exclusividade parcial:]
O Consultor não prestará serviços a concorrentes diretos do Contratante durante
a vigência e nos [90] dias seguintes ao término.

## 6. DO TRATAMENTO DE DADOS (LGPD)

Se o Consultor processar dados pessoais de titulares do Contratante, as partes
firmam o Adendo de Tratamento de Dados em anexo, conforme Art. 37 da LGPD.

## 7. DA RESPONSABILIDADE

A responsabilidade agregada do Consultor limita-se a [3x] os honorários pagos
nos [3] meses anteriores ao evento que gerou o dano.

---
Assinaturas e testemunhas conforme Template A.
```

---

## Adendo de Tratamento de Dados (LGPD — Art. 37)

```markdown
## ADENDO DE TRATAMENTO DE DADOS PESSOAIS — LGPD

Controlador: [NOME DO CLIENTE]
Operador: [NOME DO PRESTADOR]

### Objeto
O Operador trata dados pessoais por conta e ordem do Controlador exclusivamente
para a execução dos serviços do contrato principal.

### Categorias de Titulares
[ex: usuários finais, colaboradores, clientes]

### Categorias de Dados Pessoais
[ex: nomes, e-mails, CPF, dados de uso]

### Prazo de Tratamento
Pelo período de vigência do contrato principal; exclusão em até [30] dias do término.

### Obrigações do Operador (Art. 38 LGPD)
- Tratar dados apenas conforme instruções documentadas do Controlador
- Garantir que as pessoas autorizadas ao tratamento comprometam-se com a confidencialidade
- Adotar medidas técnicas e organizacionais de segurança (Art. 46 LGPD)
- Auxiliar o Controlador no atendimento a direitos dos titulares (Art. 18 LGPD)
- Não subcontratar o tratamento sem autorização prévia por escrito
- Eliminar ou devolver todos os dados ao término

### Suboperadores (na data de vigência)
| Suboperador | Localização | Finalidade |
|-------------|-------------|------------ |
| [AWS / GCP / Azure] | [Região] | Hospedagem em nuvem |
| [Outro] | [Local] | [Finalidade] |

### Transferência Internacional
*Dados pessoais [são / não são] transferidos para fora do Brasil.*
*Se sim, o Operador garantirá proteção equivalente conforme Art. 33 LGPD.*
```

---

## Pontos de Atenção — Direito Brasileiro

1. **Vínculo empregatício (CLT):** Contratos de prestação de serviços PJ com subordinação habitual, horários fixos e exclusividade podem ser reconhecidos como vínculo empregatício. Defina claramente a autonomia do prestador.

2. **MEI:** O MEI tem limite de faturamento anual (atualmente R$81.000). Acima disso, deve migrar para ME. Contratos com MEI acima de R$78.000/ano ao mesmo tomador podem gerar vínculo empregatício.

3. **Retenção de ISS:** O tomador de serviços pode ser obrigado a reter e recolher o ISS do prestador (alíquota de 2% a 5% conforme município).

4. **INSS sobre serviços:** Dependendo do tipo de serviço, o contratante pode ter obrigação de recolher 11% de INSS sobre o valor pago ao autônomo (PF sem CNPJ).

5. **Nota Fiscal:** Sempre exija NF-e (serviços) ou NFS-e (municipal). Sem NF, o pagamento pode ser questionado pela Receita Federal.

6. **Contratos digitais:** Válidos no Brasil desde o Art. 10 da MP 2.200-2/2001 (ICP-Brasil). Assinaturas eletrônicas (DocuSign, Clicksign, etc.) têm validade jurídica.

7. **Reajuste:** Defina claramente o índice de reajuste (IGP-M, IPCA, INPC) e periodicidade.

---

## Melhores Práticas Brasil

- Use **PIX** como forma de pagamento preferencial — rastreável e instantâneo
- Para projetos > R$10.000: pagamento por marcos reduz risco de inadimplência
- Sempre exija **NF de serviços** (NFS-e municipal) do prestador
- Para contratos com dados pessoais: inclua sempre o Adendo LGPD
- Defina foro na cidade do Contratante para facilitar eventual cobrança judicial
- Para PF (autônomo): verifique a necessidade de retenção de INSS (11%)
- Armazene contratos assinados por pelo menos 5 anos (prescrição civil geral)
- Revise anualmente — limites do MEI, alíquotas de ISS e INSS mudam
