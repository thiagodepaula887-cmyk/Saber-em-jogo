# Saber em Jogo — histórico, passo a passo e pendências

Registro de continuidade preparado em 21/10/2026 (horário de Brasília). Estado de referência: versão 0.7. Documento separado do guia técnico principal, solicitado pelo proprietário para consulta e transferência do projeto.

Este registro resume a conversa e os arquivos disponíveis. Não é uma transcrição integral. Quando uma causa não foi comprovada, ela é indicada como desconhecida. Resultados antigos não devem ser confundidos com validações completas da versão atual.

## 1. Objetivo e decisões do proprietário

Criar um jogo de perguntas e respostas, inspirado na dinâmica de programas de auditório, com dois módulos: preparação para OAB e conhecimentos gerais. Os temas gerais são esportes, religião, história, geografia, português, matemática, artes, literatura e variedades. No Direito, permitir estudo por disciplina, assunto, lei e artigo, com explicações e acompanhamento de progresso.

A intenção inicial incluía Android e iPhone, com publicação nas lojas. O proprietário optou por não pagar a taxa de cadastro da Google Play neste momento. O caminho atual é distribuir a versão web pública e o APK Android por download. Não houve publicação na Google Play nem na Apple App Store. Não existe instalador iOS entregue.

## 2. Caminho percorrido

### Etapa 1 — modelo inicial React Native/TypeScript e SQLite

Foi discutido um modelo QuestionOAB com identificador, versão, disciplina, assunto, enunciado, quatro opções, índice correto, comentário, dificuldade, origem e referências legais. O proprietário forneceu exemplos de código de banco local e tela de quiz.

A proposta de tipagem restringia as alternativas a uma tupla de quatro textos e o gabarito a 0, 1, 2 ou 3. Foram discutidas validação em execução, transações, referências e normalização. Isso é o desenho inicial; não significa que a versão Android entregue usa atualmente React Native ou SQLite.

### Etapa 2 — ajustes nos exemplos jurídicos

A questão de Ética exigia alinhar enunciado e comentário ao dispositivo adequado do Estatuto, distinguindo investigações/inquéritos e acesso a autos, com ressalvas de sigilo. O exemplo constitucional tinha uma alternativa adicional tecnicamente correta sobre retroatividade penal benéfica; foi apontada a ambiguidade para correção. Questões criadas para o projeto foram identificadas como autorais, sem atribuição falsa a exames FGV.

Esses cuidados iniciais não equivalem à revisão jurídica individual de todas as 10 mil questões acrescentadas depois.

### Etapa 3 — simplificação e primeira experiência utilizável

Após dificuldade para abrir o projeto e pedido de algo mais simples, o desenvolvimento passou a incluir interface web estática e um APK offline. A capa inicial recebeu melhorias após avaliação do proprietário. Foram criados arquivos de projeto, backup no Drive e repositório GitHub.

A implementação efetivamente entregue é HTML/CSS/JavaScript na web e Java/WebView no Android. A pasta mobile contém uma base Expo anterior e não é a origem do APK 0.7. Não iniciar uma alteração nessa pasta supondo que ela atualiza automaticamente o aplicativo distribuído.

### Etapa 4 — gamificação (versão 0.4)

Foram acrescentados modo Estudar e modo Desafio, três vidas, pontuação progressiva, ajuda 50/50, cronômetro opcional de 30 segundos, caderno de erros, desafio diário, sequência de dias, sons opcionais e navegação Voltar no Android. O banco chegou a 400 questões: 160 jurídicas e 240 gerais. As questões jurídicas cobriam 20 disciplinas, inicialmente oito por disciplina.

Históricos eram e continuam sendo locais; não há sincronização automática entre navegador, APK e projeto Expo. Pontuação crescente não comprova dificuldade adaptativa nem domínio da matéria.

### Etapa 5 — relato de instalação que não abria e revisão de 40 pontos (0.5)

O proprietário relatou que instalava, mas o aplicativo não abria e não mostrava mensagem. Não foi obtido um registro do aparelho capaz de comprovar a causa original.

Foram implementados captura de exceções, tela nativa de recuperação, diagnóstico copiável, detecção de falha do renderizador WebView, limite de 15 segundos para inicialização, confirmação de prontidão e recuperação de falhas de carga. Banco inválido ou duplicado é rejeitado antes de iniciar a partida. Histórico corrompido não deve impedir a capa; armazenamento bloqueado gera aviso.

A auditoria histórica de 40 pontos registrou 36 verificações aprovadas e quatro pendentes. Incluía inspeções e simulações, não 40 testes em aparelho. Naquela etapa não houve teste visual em navegador real porque a tentativa de obter Chromium falhou. Mais tarde houve verificação da versão 0.7 em navegador real.

### Etapa 6 — provas anteriores (0.6)

Foram incluídos seis exames da primeira fase, 42º a 47º: links aos PDFs oficiais tipo 1, cartão de 80 respostas por exame, gabaritos definitivos, tratamento de anuladas, meta de 40/80, tempo opcional de cinco horas, retomada e correção.

Importante: são documentos oficiais com cartão/gabarito, separados do banco autoral. As 480 posições de gabarito não significam 480 enunciados oficiais incorporados na interface pergunta a pergunta. O pedido de uma experiência inteiramente integrada com enunciados reais ainda requer trabalho adicional.

### Etapa 7 — busca, biblioteca e expansão para 10 mil (0.7)

O pedido passou de pelo menos mil para 10 mil questões jurídicas no total. A versão atual tem:

- 10.000 exercícios jurídicos em 20 disciplinas;
- 9.788 exercícios de completar trechos de lei seca;
- 212 questões conceituais;
- mais 240 questões de conhecimentos gerais, totalizando 10.240;
- biblioteca de 24 normas federais, com fontes e data de consulta;
- pesquisa por disciplina, assunto, nome/número de lei e artigo;
- acompanhamento local de cobertura e respostas;
- lembretes Android configuráveis por disciplina/tema/lei.

Não são 10.000 questões oficiais FGV, nem 10.000 situações-problema revisadas individualmente. A biblioteca não contém toda a legislação brasileira. A maior parte da expansão é de memorização literal; variedade e qualidade pedagógica ainda precisam de evolução editorial.

Os dados foram importados de textos oficiais e organizados em arquivos compactados versionados. O importador foi corrigido para lidar com HTML malformado da CLT, números altos de artigos no Código Civil, separação de artigos como 7, 7-A e 7-B, e distinção entre Constituição principal e ADCT. Essas correções foram verificadas por testes específicos.

### Etapa 8 — geração e entrega

Foram gerados APK de teste e AAB assinado para eventual envio à Google Play. A compilação, o alinhamento e a assinatura do APK foram verificados. O AAB foi validado com bundletool e sua assinatura foi conferida. Isso não representa aprovação por loja ou certificação de ausência de riscos.

Um comando de testes foi executado inicialmente a partir da pasta errada e falhou por não encontrar dist/game-engine.js. Foi repetido na pasta web, que é o diretório esperado; os 27 resultados passaram. Essa falha de execução dos testes foi resolvida e não foi um defeito identificado no aplicativo.

O proprietário confirmou depois: “Funcionou perfeitamente”. Isso confirma funcionamento no aparelho utilizado por ele, mas não uma matriz completa de testes em dispositivos diferentes.

### Etapa 9 — distribuição sem loja e acesso público

O proprietário relatou aviso/bloqueio do Play Protect. Foi solicitada a mensagem exata; ela ainda não foi recebida e analisada. A decisão foi não pagar o cadastro Google Play neste momento.

A versão web foi inicialmente publicada com acesso apenas ao proprietário. Após solicitação expressa, o acesso foi alterado para público e confirmado pela configuração do serviço. O APK carrega os arquivos locais e não exige conta ChatGPT. Provas/PDFs e outros links externos exigem internet. O progresso do jogo permanece local.

### Etapa 10 — entrega de controle e documentação

Ao conferir a documentação, foi encontrado o documento principal ainda descrevendo a versão 0.4. Ele foi reescrito para a 0.7, com arquitetura real, comandos, dependências, arquivos de referência e pendências. O ZIP de código no Drive também foi atualizado.

Foi salvo um backup separado de chaves de assinatura na pasta do Drive, cuja permissão consultada mostrava somente o proprietário. As chaves não devem ir para o GitHub público nem para o site do jogo. O GitHub não recebeu todas as alterações da 0.7: a sincronização final foi interrompida e continua pendente. O ZIP atualizado do Drive é a referência de entrega atual.

## 3. Problemas abertos e limites

| Item | Estado e evidência | Próxima ação |
|---|---|---|
| Play Protect | Proprietário relatou aviso/bloqueio; causa desconhecida | Obter captura/texto completo, versão Android e APK exato; analisar antes de redistribuir amplamente. Não orientar desativação da proteção |
| Falha original “não abre” | Causa não reproduzida; recuperação implementada; versão posterior funcionou para o proprietário | Guardar diagnóstico se reaparecer; não atribuir causa sem logs |
| GitHub desatualizado | Código completo 0.7 está no ZIP do Drive; atualização remota incompleta | Sincronizar a entrega completa, sem credenciais, e conferir clone limpo |
| Revisão jurídica | Validação técnica não substitui revisão de conteúdo | Revisar gabaritos, explicações, vigência, referências e ambiguidade; identificar revisão por questão |
| Qualidade das 10 mil questões | 9.788 são lacunas de lei seca | Aumentar casos práticos, distratores plausíveis, dificuldade e diversidade; não vender como 10 mil questões FGV |
| Cobertura legislativa | Apenas 24 normas federais; fotografia da consulta | Definir processo contínuo de atualização, jurisprudência e normas adicionais |
| Rótulos vazios no leitor | Na inspeção da biblioteca apareceram marcadores como “§ 1º .” após retirada de conteúdo revogado; não há correção final documentada | Tratar trechos revogados/vazios preservando clareza e fidelidade à fonte |
| Notificações | Implementadas no Android; concessão/negação da permissão, reinício e entrega ainda não verificados em aparelho | Testar Android 13+, economia de bateria, reinício, horário e cancelamento; horários são aproximados |
| Provas oficiais na interface | PDFs e cartão implementados, sem banco integral de enunciados oficiais | Se desejado, estruturar enunciados/alternativas e conferir origem, tipo de prova, gabarito e anuladas |
| Backup de progresso | Local, sem conta/sincronização/exportação confirmada | Se necessário, criar exportação/importação e plano de migração antes de mudanças de assinatura |
| Atualização Android | Assinaturas de teste e upload diferentes | Definir estratégia definitiva; preservar chave adequada e incrementar versionCode |
| Build em outro computador | Scripts exigem layout específico de ferramentas, fora do ZIP | Instalar dependências do guia ou migrar para Gradle/SDK padrão; conferir build limpo |
| Lojas e iOS | Não publicado; não há instalador iOS | Só retomar se o proprietário decidir; cumprir requisitos então vigentes |
| Privacidade/suporte de produção | Cadastro final da loja e materiais completos não concluídos | Definir contato e publicar política compatível com o comportamento final |
| Administração do site | Hospedagem atual vinculada à conta do proprietário | Autorizar editor ou migrar hospedagem; link público não concede administração |

## 4. O que foi efetivamente validado

Na última execução da versão 0.7, 27 resultados de testes automatizados passaram, incluindo validação do banco, filtros, busca por Lei 8.906/94, progresso por versão de questão, correspondência de trechos de lei seca à biblioteca e mecanismos de provas anteriores.

Houve teste em navegador real da entrada no módulo OAB, pesquisa “lei 8906/94”, biblioteca, Estatuto da OAB e leitura do art. 7º. Houve validação de ferramentas de assinatura/build Android. O proprietário confirmou funcionamento do aplicativo.

Não há comprovação de testes completos em diferentes aparelhos, de todas as notificações, de atualização preservando histórico no dispositivo, de revisão jurídica individual de 10 mil questões ou de aprovação do Play Protect/lojas. O relatório antigo VALIDACAO_40_PONTOS.md é histórico da 0.5, com números de conteúdo daquela versão.

## 5. Passo a passo para outro programador ou IA continuar

1. Obter acesso autorizado à pasta do Drive e baixar o ZIP de código 0.7, o documento principal e este histórico. Não usar somente o GitHub, que está atrasado.
2. Extrair o código. Ler README.md, PROJETO_SABER_EM_JOGO.md e EXPANSAO_10000.md. Confirmar que o trabalho deve partir de web e android-offline, não da base Expo antiga.
3. Na raiz executar `python3 web/scripts/prepare-content.py`. Ele gera os JSON de execução a partir dos arquivos .gz em web/content.
4. Executar `python3 -m http.server 8080 --directory web/dist` e abrir http://localhost:8080.
5. Em outro terminal, entrar em web e executar `node --test tests/*.test.cjs`.
6. Para Android, instalar/configurar as ferramentas e versões descritas no documento principal. O ambiente de compilação não acompanha integralmente o ZIP. Executar build.py com QUIZ_ANDROID_TOOLS adequado.
7. Somente para assinar atualizações, obter as chaves privadas diretamente do proprietário, ajustar caminhos locais e conservar cópia segura. Não adicionar esses arquivos ao controle de versão público.
8. Priorizar o diagnóstico Play Protect e a sincronização GitHub, depois os testes de aparelho e revisão editorial. Documentar cada evidência e não marcar pendência como corrigida sem confirmação.
9. Para a web hospedada, usar autorização do proprietário na hospedagem atual ou publicar web/dist em serviço estático alternativo. Não há dependência de ChatGPT para o código estático funcionar fora da hospedagem atual.
10. A cada entrega, atualizar versão, manifest de conteúdo, documentação, backup e testes relevantes. Conferir que a web e o APK receberam os mesmos arquivos de conteúdo.

## 6. Onde estão os arquivos

Pasta principal do proprietário: https://drive.google.com/drive/folders/1Ep3Gnj5zmhj6sJt1qHH7odk5RwtcEbO7

| Arquivo | Uso |
|---|---|
| PROJETO_SABER_EM_JOGO.md | Guia técnico atualizado da 0.7 e continuidade |
| HISTORICO_E_PENDENCIAS_SABER_EM_JOGO.md | Este registro independente |
| EXPANSAO_10000.md | Contagens, tipos de questão e limites editoriais |
| Saber_em_Jogo_0.7_Codigo.zip | Código e dados atualizados para continuar |
| Saber_em_Jogo_0.7_Android.apk | Instalador Android entregue |
| Saber_em_Jogo_0.7_Play.aab | Pacote preparado para eventual loja; não publicado |
| CHAVES_ASSINATURA_PRIVADAS.zip | Material restrito do proprietário; não redistribuir |
| SIMULADOS_OAB.md | Referências das provas e gabaritos |
| VALIDACAO_40_PONTOS.md | Evidência histórica da 0.5; não auditoria integral da 0.7 |

Código atualizado: https://drive.google.com/file/d/11QJBvE-aixlXgWivZyExQYdcvxncD-wC/view

Guia principal: https://drive.google.com/file/d/137i-v9dfcotIWxivwhMzt5TTxDZqz649/view

APK 0.7: https://drive.google.com/file/d/1MQb4O4vpKAJGzwleyeDsHY23D8KPh98s/view

Web pública: https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site

Compartilhar o jogo não compartilha o código nem a administração. O proprietário deve conceder acesso ao profissional; uma IA só poderá consultar arquivos que forem enviados ou disponibilizados por conexão autorizada. Não compartilhar senhas de contas para permitir continuidade.

## 7. Sincronização GitHub da entrega 0.7

O registro acima descreve o estado anterior à sincronização. Nesta entrega, o código web e Android 0.7, os snapshots compactados, scripts, testes e documentação foram preparados para o GitHub. Os JSON grandes de execução deixam de ser versionados: execute `python3 web/scripts/prepare-content.py` após clonar. O projeto Expo continua anterior e separado. Os problemas Play Protect, revisão editorial e notificações continuam pendentes. Consulte o histórico de commits para confirmar a aplicação desta sincronização.

