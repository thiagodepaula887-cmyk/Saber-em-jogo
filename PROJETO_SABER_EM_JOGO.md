# Saber em Jogo — projeto e continuidade

Atualização: 16/10/2026. Versão 0.4.

## Acesso e arquivos

- Aplicativo web: https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site
- APK Android de teste: https://drive.google.com/file/d/1QoYjzzpeSSHa58LHXF-O9JeTnPLcv6uL/view
- Backup: pasta Saber em jogo no Drive, incluindo este resumo, código completo e APK.
- GitHub: https://github.com/thiagodepaula887-cmyk/Saber-em-jogo — repositório público criado pelo usuário.

## Estado funcional

400 questões autorais comentadas: 160 jurídicas em 20 disciplinas e 240 gerais em nove categorias. Acrescentadas 100 questões em relação à versão anterior, com Eleitoral, Previdenciário, Financeiro, Direitos Humanos e Filosofia do Direito.

Tela inicial com troféu, cartões de modos, estatísticas, nível e XP; escolha de tema; rodadas de até dez perguntas; alternativas embaralhadas na web e APK; comentários e fontes; resultado e prioridade para inéditas. A página web também oferece botão para baixar o APK. Não há prêmios em dinheiro.

| Categoria ou disciplina | Questões |
| --- | ---: |
| esportes | 26 |
| religião | 26 |
| história | 26 |
| geografia | 26 |
| português | 26 |
| matemática | 26 |
| artes | 26 |
| literatura | 26 |
| variedades | 32 |
| Ética Profissional | 8 |
| Direito Constitucional | 8 |
| Direito Civil | 8 |
| Processo Civil | 8 |
| Direito Penal | 8 |
| Processo Penal | 8 |
| Direito do Trabalho | 8 |
| Processo do Trabalho | 8 |
| Direito Administrativo | 8 |
| Direito Tributário | 8 |
| Direito Empresarial | 8 |
| Direito do Consumidor | 8 |
| Estatuto da Criança e do Adolescente | 8 |
| Direito Ambiental | 8 |
| Direito Internacional | 8 |
| Direito Eleitoral | 8 |
| Direito Previdenciário | 8 |
| Direito Financeiro | 8 |
| Direitos Humanos | 8 |
| Filosofia do Direito | 8 |

## Arquitetura e diferenças entre versões

- `web/`: HTML/CSS/JS, localStorage, hospedagem Sites. Não sincroniza histórico com outros aparelhos.
- `android-offline/`: Activity Java + WebView com todos os arquivos locais; APK compilado nesta entrega, independente de Expo Go. Histórico em localStorage do aplicativo.
- `mobile/`: base React Native + Expo + TypeScript + SQLite para evolução multiplataforma. Não é o código usado para compilar este APK. Ainda sem binário iOS.

O APK offline foi escolhido para permitir instalação imediata sem exigir configuração de uma conta Expo ou ambiente de desenvolvimento do usuário. A assinatura é de teste. Produção nas lojas exige assinatura definitiva e cumprimento dos requisitos de publicação.

## Validação

Todas as 400 perguntas têm IDs e enunciados únicos, quatro alternativas distintas e gabarito válido. Web validada em testes com DOM simulado; sem nova inspeção visual automatizada. Mobile Expo aprovado na tipagem e em sete testes com SQLite real. APK compilado, alinhado, assinado e verificado (v2/v3); manifesto e recursos conferidos. Confirmado que o APK contém o mesmo banco de 400 questões da web. Não executado em aparelho ou emulador.

## Conteúdo e fontes

Exercícios autorais introdutórios de fixação. Não são reproduções oficiais de exames FGV e não substituem simulados completos. As questões jurídicas contêm artigos e fontes oficiais; Filosofia utiliza obras primárias de Kant e Aristóteles em domínio público via Project Gutenberg. Revisão assistida por IA, sem validação independente por professor.

As fontes editoriais são `web/content/general.txt` e `web/content/oab.txt`. O gerador `web/scripts/build-content.py` valida quantidades e gera o JSON. Revisões de conteúdo devem aumentar o número de versão correspondente. O pacote mobile usa uma cópia validada desse JSON.

## Próximas etapas

1. Testar instalação, abertura, fluxo de partida e reabertura do APK no celular.
2. Manter o código atualizado no GitHub, excluindo chaves de assinatura e arquivos temporários.
3. Acrescentar situações-problema e níveis de dificuldade OAB, com revisão editorial independente.
4. Implementar caderno de erros, revisão espaçada, retomada de partidas e acessibilidade validada em dispositivo.
5. Configurar nuvem, painel editorial e sincronização, se desejado.
6. Definir identidade definitiva, política de privacidade, contas de desenvolvedor, assinatura e distribuição nas lojas.

## Integridade

- SHA-256 do APK: `4077e6b79161112370ec5884f430efed3061761df8c02b454a7d89aa67b2405e`
- SHA-256 do banco: `6c6c7a91526443ca52f18f0a6bc0cb53023efb1d75966850809cea4b857a2bcc`
- Commit web: `2f6507052320723c00412ce1453b30343b95b26a`.


## Atualização 0.4

Implementados na web e no APK offline: modo Desafio com três vidas, pontuação por fase e ajuda 50/50; cronômetro opcional de 30 segundos; caderno de erros; desafio diário de dez perguntas com sequência de dias; sons opcionais. O projeto Expo continua separado, na base anterior.

Verificações: cinco testes unitários de motor, smoke test do fluxo com DOM simulado (três erros, expiração, duplicidade, revisão e conclusão diária), assinatura APK e alinhamento. Certificado comparado ao da versão 0.3: idêntico. Atualização instalável por cima da anterior, preservando os dados locais; não desinstalar antes. Ainda sem teste em aparelho real.


## Versão 0.5 — diagnóstico e revisão de 40 pontos

Recuperação de inicialização, watchdog, validação de banco e build limpo. Consulte VALIDACAO_40_PONTOS.md e quality/results.json: 36 verificações aprovadas; quatro pendentes. A causa da não abertura no Samsung ainda não foi confirmada. Atualização em aparelho e publicação não foram validadas.

APK atual: https://drive.google.com/file/d/1UgnHCt-2-q-cXM5NlxHtG1GVMoikHhq0/view?usp=drivesdk


## Versão 0.6 — seis provas oficiais

Exames 42–47, caderno branco tipo 1, com PDF oficial externo e cartão de respostas no app. 480 posições de resposta, gabaritos definitivos, pontuação das anuladas, timer opcional e retomada. Não são 480 enunciados importados no quiz: leia o PDF e responda no cartão. Consulte SIMULADOS_OAB.md para fontes e limites. 19 resultados Node aprovados; instalação real continua pendente.

APK atual: https://drive.google.com/file/d/18QgIpXDTE27jR3p5HQk1VqOCR_lHO--a/view?usp=drivesdk
