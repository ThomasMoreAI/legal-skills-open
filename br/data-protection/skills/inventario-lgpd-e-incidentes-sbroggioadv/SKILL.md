---
name: inventario-lgpd-e-incidentes-sbroggioadv
title: Inventário LGPD e incidentes
description: Produz o inventário de dados pessoais da serventia, separa a camada administrativa da camada de fé pública e organiza contratos, riscos e resposta a incidentes pelos arts. 85 a 98 do CNN. Esta skill deve ser usada quando o pedido mencionar LGPD, inventário de dados, RIPD, fornecedor, titular de dados, incidente, vazamento, ANPD, acesso, privacidade ou mapa de tratamento.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/inventario-lgpd-e-incidentes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Inventário LGPD e incidentes

## Três invioláveis

1. Nada do acervo sai sem anonimização irreversível prévia.
2. Nada alimenta treinamento: nem entrada, nem saída, nem dado inferido.
3. Nada produzido pelo plugin é ato notarial ou registral nem pode parecer ato dotado de fé pública.

Aplicar **IMUTABILIDADE, RASTREABILIDADE e RETENÇÃO MÍNIMA** em toda automação. Base normativa atualizada até 25/08/2026.

Tratar o acervo como patrimônio funcional **do serviço**, não do titular; tudo que esta skill gerar deve ser extraível em formato não proprietário, sem anuência de fornecedor. Separar a camada administrativa da camada de fé pública: nesta última, leitura autorizada pode ocorrer, mas saída com aparência de ato nunca.

## Anexos e skills obrigatórios

- `context/cnn-indice-de-enderecamento.md` — endereços dos arts. 85 a 98;
- `context/prov-cnj-213-2026-e-anexos.md` — incidentes e proteção tecnológica;
- `context/res-cnj-615-2025-recorte-dados.md` — referência de risco, sem vinculação própria à serventia;
- `context/travas-defasagem.md` — prazo de 48 horas úteis;
- `diagnostico-do-acervo`, `avaliacao-de-impacto-e-ripd` e `busca-local-no-acervo-e-a-fronteira`.

## Separação estrutural do CNN art. 98

Manter dois inventários vinculados, nunca uma base indiferenciada:

1. **camada administrativa:** dados de pessoal, fornecedores, contratos, atendimento, segurança e gestão; sujeita ao acesso administrativo e às rotinas de LGPD;
2. **camada de fé pública:** dados próprios do acervo notarial ou registral; não abrangida pelo acesso administrativo do titular na mesma forma.

Quando houver saída do art. 98, inserir o aviso de que **não é documento dotado de fé pública** e não substitui certidão. O plugin não emite certidão, traslado ou ato.

## Inventário de dados pessoais

Para cada operação, registrar finalidade, categoria de dados e titulares, origem, base normativa, sistema, operador, compartilhamentos, localização, acessos, segurança, retenção, descarte, risco e responsável. Mapear o ciclo completo e as inferências produzidas.

Revisar contratos e exigir adequação LGPD do fornecedor, confidencialidade, segregação, incidentes, reversibilidade, portabilidade e exclusão. Não aceitar treinamento ou aperfeiçoamento com entrada, saída ou dado inferido.

A Resolução CNJ 615/2025 rege o Judiciário e **não vincula a serventia por força própria**; usar seu recorte de dados apenas quando norma aplicável o incorporar ou como referência expressamente rotulada, nunca como obrigação federal direta.

## Resposta a incidente

Ao tomar conhecimento de incidente com dados pessoais:

1. conter, preservar evidência e registrar horário da ciência;
2. classificar impacto, titulares, sistemas e dados;
3. comunicar titular dos dados, **ANPD**, juiz corregedor permanente e CGJ em até **48 horas úteis**, conforme CNN art. 91;
4. comunicar também incidente crítico de TIC à Corregedoria em até **72 horas**, quando aplicável, sem usar um prazo para apagar o outro;
5. documentar causa raiz, correção, recuperação e lições aprendidas;
6. atualizar inventário, risco, contratos e controles.

Não aguardar certeza absoluta para iniciar o fluxo. Não expor dados pessoais no próprio relatório de comunicação além do necessário.

## Saída

Entregar inventário por camada, mapa de fluxos e fornecedores, bases e retenções, riscos, plano de correção, matriz de comunicação e registro cronológico do incidente. Produzir modelos administrativos claramente sem fé pública.

## Reprovação automática

- fundir camada administrativa e fé pública;
- oferecer acesso administrativo como substituto de certidão;
- atribuir vinculação direta da Resolução 615 à serventia;
- usar dado do acervo em treinamento;
- omitir ANPD, juiz corregedor ou CGJ no prazo de 48 horas úteis;
- confundir 48 horas úteis de dados com 72 horas de incidente crítico de TIC.
