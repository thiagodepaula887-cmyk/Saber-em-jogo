# Correção 0.9 — restauração do banco jurídico

O usuário solicitou mais dificuldade, não a redução de 10 mil questões para 40. A versão 0.8 havia retirado 9.788 exercícios e deixado apenas 40 casos novos no treino padrão. Essa decisão foi revertida na 0.9.

## Estado atual

- 10.000 questões jurídicas da versão 0.7 restauradas integralmente, mais os 40 casos novos da 0.8: **10.040 jurídicas**.
- 240 questões gerais: **10.280 registros ativos** no quiz.
- Padrão de pesquisa, seleção por disciplina/lei, modo desafio e desafio diário usam o banco completo. O filtro de casos revisados é opcional.
- Filtros explícitos: banco completo, 40 casos novos, casos médios, casos difíceis, 212 conceitos básicos e 9.788 exercícios de lei seca.
- Exercícios antigos seguem com revisão pendente: restaurar seu acesso não resolve a baixa dificuldade nem representa revisão jurídica concluída.
- Não houve alteração de ID, versão, enunciado, alternativas, gabarito ou explicação de qualquer registro original. Histórico e caderno de erros podem reconhecer os mesmos registros restaurados. Dados já apagados no dispositivo não podem ser recuperados por essa medida.
- As nove provas oficiais com PDF externo e cartão de respostas continuam disponíveis. Não se somam os cartões à contagem do quiz.

## Reprodução e verificação

`python3 web/scripts/prepare-content.py` reconstrói a versão 0.9 a partir do snapshot original v7 e dos casos autorais mantidos em `casos-revisados.py`. O snapshot v9 é gerado, não é mais uma cópia canônica versionada. Não há regra de exclusão por estar em revisão. O inventário editorial v9 registra zero itens retirados.

31 resultados automatizados aprovados, incluindo comparação integral dos campos originais por ID, recuperação do progresso, acesso padrão às 10.040 jurídicas, filtros com contagens coerentes, busca por lei, cartões de concurso e modos de jogo. A conferência visual em navegador continua limitada pelo ambiente. A compilação do Android usa versionCode 9 e a chave original. A instalação no A53 e o aviso Play Protect precisam de confirmação em aparelho.

## Publicação na Google Play

A conta conectada abriu a página de cadastro do Play Console. Não houve criação de conta, pagamento nem envio do jogo para análise. Em 22/10/2026, a taxa informada pelo Google é US$ 25 (única). Novas contas pessoais têm requisitos de teste fechado. AAB gerado e assinado é apenas parte da preparação: faltam cadastro/verificações, política de privacidade acessível no app e na página, ficha de loja, classificação e declarações de conteúdo/dados, testes aplicáveis e análise da plataforma.

Não publicar a versão reduzida 0.8 como se contivesse as 10 mil anteriores. O alvo atual para eventual envio é 0.9, após concluir os requisitos acima. A biblioteca e os gabaritos antigos não representam acompanhamento contínuo da legislação.
