# Validação de legislação pelo Silo

Use somente quando o conector Silo estiver autenticado. Não crie confirmação
intermediária por chamada.

## Descoberta

Descubra o manifesto real de capabilities em runtime. A capability esperada é
`verify_legislation_in_planalto`; se o nome ou contrato não estiver disponível,
registre a ausência e continue com a biblioteca versionada. Não substitua por
busca externa direta.

## Duas passagens

1. Depois de delimitar as normas federais materiais, envie cada referência
   relevante para validação.
2. Ao finalizar o mapa, audite todas as afirmações legais e reenvie qualquer
   referência federal nova surgida durante a aplicação.

Para cada retorno, registre:

- dispositivo solicitado;
- texto localizado;
- URL oficial;
- correspondência ou divergência com a biblioteca;
- capability efetivamente usada;
- ponto do mapa afetado.

## Limite

A verificação confirma localização, texto e URL conforme o contrato observado.
Não a descreva como confirmação de vigência. Vacatio legis, revogação, regra
especial, controle de constitucionalidade e incidência temporal exigem análise
separada.

Se houver divergência entre biblioteca e Planalto, suspenda somente a conclusão
dependente, preserve ambas as versões e marque `[verificar]` antes de atualizar
o corpus.
