---
name: qualificacao-notarial-transversal-sbroggioadv
title: Qualificação notarial transversal
description: 'Checklist transversal de qualificação humana para atos notariais: capacidade, legitimidade, licitude, forma, identidade, união estável, representação e atualidade de poderes, cadastro PLD e consultas CEP/CENSEC, RCTO e CNIB. Esta skill deve ser usada antes de escritura, ata, procuração, testamento ou ato eletrônico, ou quando o pedido mencionar qualificação notarial, capacidade, representante, procuração, união estável, PEP/PLD, poderes revogados, CENSEC, CEP, RCTO, CNIB, testemunha por deficiência ou conferência prévia das partes.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/qualificacao-notarial-transversal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Qualificação notarial transversal

> Camada C1. Organizar as verificações que se repetem em todos os atos. Não substituir a análise jurídica nem emitir decisão final.

## Anexos obrigatórios

- `context/cc-notarial.md`;
- `context/lei-8935-94.md`;
- `context/cnn-149-2023-compilado.md`;
- `context/precedentes-notariais.md`;
- `context/travas-defasagem.md`.
- `regime-de-ia-da-uf` — gate obrigatório antes de qualquer enquadramento jurídico.

Carregar também o anexo específico do ato e a regra da UF.

## Pré-gates

1. Fixar UF.
2. Fixar ato e modalidade.
3. Confirmar competência.
4. Rodar `varredura-de-vigencia-pre-lavratura`.
5. Rodar `regime-de-ia-da-uf` para a função pretendida.
6. Separar fatos/documentos confirmados de declarações ainda não comprovadas.

Se a norma estadual vedar qualificação, interpretação, enquadramento ou influência sobre decisão jurídica, interromper antes de classificar. No MT, o art. 4º, II e III, do Provimento 1/2026-GAB-CGJ proíbe esse uso **ainda que sob revisão humana**; a saída deve apenas organizar fatos e fontes e devolver o enquadramento ao titular.

## Matriz de qualificação

### 1. Identidade e capacidade

- Conferir identidade e correspondência documental de todos os comparecentes.
- Aplicar CC arts. 3º, 4º e 104 na redação vigente; absolutamente incapaz é somente menor de 16 anos.
- Não presumir incapacidade por deficiência.
- Identificar representação, assistência ou apoio juridicamente aplicável sem inventar requisito.

Não exigir testemunha apenas porque a parte tem deficiência. A Lei 8.935/1994, art. 7º, §2º veda essa prática; respeitar exceções expressas, como testamento de pessoa cega.

### 2. Legitimidade e vontade

- Confirmar vínculo da parte com o direito/negócio.
- Verificar manifestação livre, compreendida e sem contradição aparente.
- Identificar existência de união estável, exigida na qualificação pelo CNN art. 111.
- Conferir outorga conjugal ou suprimento quando aplicável, sem confundir separação absoluta e obrigatória.

### 3. Licitude, objeto e forma

- Aplicar CC art. 104: agente capaz, objeto lícito/possível/determinado ou determinável e forma prescrita/não proibida.
- Aplicar CC art. 215 à estrutura da escritura.
- Identificar forma pública essencial e norma especial do ato.
- Não usar anulabilidade/ineficácia como recusa automática quando a norma estadual mandar advertir e consignar.

### 4. Representação e poderes

- Examinar procuração e substabelecimento quanto a forma, legitimidade e poderes.
- Verificar atualidade antes da lavratura, conforme CNN art. 150.
- Não impor prazo genérico de validade à procuração pública; o PCA 0007885-89 reprova essa exigência.
- Exigir poder especial/expresso e individualização quando o ato de disposição assim exigir.
- Registrar que a CEP informa **se** a procuração existe; não prova **o conteúdo** suficiente dos poderes.

### 5. Cadastro PLD

- Aplicar CNN art. 145 aos atos protocolares com conteúdo econômico.
- Incluir representantes e procuradores no cadastro aplicável.
- Conferir estado civil, cônjuge, sanções e enquadramento PEP quando a norma exigir.
- Não recusar apenas pela falta de informação obtida exclusivamente para PLD: consignar a recusa da parte e comunicar à UIF quando cabível, conforme CNN arts. 155-A, 165-A e 179.

### 6. Consultas

- **CEP/CENSEC:** existência e eventos; não substituir leitura do instrumento.
- **RCTO/CENSEC:** consulta obrigatória em inventário, partilha, separação, divórcio e extinção de união estável quando a norma determinar.
- **CNIB:** aplicar a regra da UF e consignar o resultado quando exigido; indisponibilidade pode não impedir lavratura na norma local.
- Outras centrais: usar somente quando o ato e a norma as exigirem.

### 7. Documentos, tributos e fronteiras

- Encaminhar rol documental à skill específica; não criar lista aberta.
- Separar certidão informativa de condição de lavratura.
- Verificar tributos como gate quando a norma mandar, sem lançar ou arbitrar valor.
- Separar qualificação notarial de qualificação registral posterior.

## Resultado do checklist

Somente classificar os eixos abaixo quando o gate estadual admitir a função. Se o gate vedar, entregar o quadro factual e normativo sem atribuir estado jurídico, com a marca **ENQUADRAMENTO RESERVADO AO TITULAR**.

Classificar cada eixo:

- **CONFIRMADO:** documento/fato lido e requisito atendido;
- **PENDENTE SANÁVEL:** falta item legalmente exigido;
- **GATE EXTERNO:** depende de juízo, MP, tributo, outorga ou outro órgão;
- **CONSIGNÁVEL:** a norma manda lavrar com advertência/registro;
- **DEVOLVER AO TITULAR:** exige juízo jurídico humano.

Não emitir “aprovado/reprovado” sobre o ato. Entregar o mapa para decisão do titular.

## Guard

Não carregar dados pessoais no perfil da serventia. Não enviar documento/acervo a ferramenta externa. Não usar IA para qualificação, interpretação ou enquadramento legal onde a UF veda, inclusive como apoio sob revisão humana no MT. Não converter consulta negativa em prova absoluta e não inventar documento fora do rol legal.

## Entrega obrigatória

Entregar tabela por eixo, fonte, pendência, caminho de correção e itens devolvidos ao titular. Encaminhar somente depois à skill do ato/minuta.
