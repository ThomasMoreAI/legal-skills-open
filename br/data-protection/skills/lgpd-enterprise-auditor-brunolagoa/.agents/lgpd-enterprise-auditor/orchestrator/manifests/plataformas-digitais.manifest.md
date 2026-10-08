# Manifesto — `plataformas-digitais`

- `module`: plataformas-digitais
- `required`: false
- `files`: `legal/plataformas-digitais.md`
- `inputs`: tipo de serviço (intermediação de conteúdo de terceiros, anúncios/impulsionamento pagos, IA que gera ou altera imagem/som), canal de denúncia e fluxo de notificação/contestação, políticas de moderação e gestão de riscos sistêmicos, base de anúncios e anunciantes, guarda de registros de acesso (IP e porta lógica), representante legal no País, termos de uso e relatórios de transparência
- `prerequisites`: core, legal
- `activates_when`: cenário `digital_platform`, cenário `full_audit`, ou gatilho normativo de plataformas digitais — provedor de aplicações que intermedeie conteúdo gerado por terceiros com difusão pública, ofereça anúncio ou impulsionamento pago, ou disponibilize IA capaz de gerar ou alterar imagem ou som de pessoas
- `primary_outputs`: conformidade com o Decreto nº 12.975/2026 (Decreto nº 8.771/2016, arts. 15-A, 16-A a 16-P, 19-A e 20-A) e o Decreto nº 12.976/2026 — deveres gerais e representante legal (art. 16-A), dever de cuidado e falha sistêmica (art. 16-B), riscos sistêmicos (art. 16-C), notificação, remoção e contestação (arts. 16-D a 16-J), anúncios, impulsionamentos e publicidade (arts. 16-K a 16-N), exclusões e critérios diferenciados (arts. 16-O e 16-P), guarda de registros com porta lógica (MCI art. 15 e art. 15-A), termos de uso e relatório anual de transparência (art. 20-A), proteção de mulheres — Ligue 180, conteúdo íntimo em 2 horas, ataques coordenados, vedação de deepfake íntimo e prazos transitórios (Dec. 12.976, arts. 4º a 13), exposição às sanções do art. 12 do MCI
- `notes`: o arquivo do módulo é `legal/plataformas-digitais.md` — módulo normativo derivado da regulamentação do Marco Civil da Internet, não de um diretório de domínio técnico. Todo `finding` deve citar o dispositivo do decreto e o correlato na LGPD.
