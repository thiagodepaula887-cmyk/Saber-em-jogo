# Saber em Jogo 0.5 — validação de 40 pontos

19/10/2026. **36 verificações aprovadas; 4 pendentes.** A lista inclui testes executáveis, inspeção de dados e revisão estrutural, identificados na tabela. Não são 40 testes em celular. A causa do relato “não abre” ainda não foi reproduzida nem confirmada por logs.

## Correções implementadas

- Tela nativa de recuperação com diagnóstico copiável (código, aparelho, Android), sem envio de dados.
- Tratamento de exceções na configuração da WebView e de encerramento do renderer.
- Limite de 15 segundos para iniciar, com confirmação quando a capa fica pronta.
- Recarregar disponível mesmo sem scripts externos; validação do banco antes da partida.
- Rejeição de questões corrompidas, IDs e opções duplicados, gabaritos ou versões inválidos.
- Histórico malformado não bloqueia a capa; armazenamento indisponível é informado.
- Build limpo, versionCode 5 e mesmo certificado/pacote das versões anteriores.

## Evidências e limites

Executados: `node quality/audit.cjs`, `cd web && node --test tests/*.test.cjs` (11 resultados aprovados), compilação Java/D8, apksigner e zipalign. Os testes de interface usam DOM simulado. Inspeções de Java não executam o ciclo de vida Android.

Sem aparelho nem emulador Android neste ambiente. A tentativa de obter Chromium falhou por download inválido: não houve teste visual em navegador real nesta rodada. Compilar e assinar não comprova abertura no Samsung.

O APK contém interface web offline numa Activity Java. O projeto Expo permanece separado e não foi alterado nesta rodada. Não foi criado instalador iOS nem publicada versão nas lojas.

## 40 verificações

| Nº | Verificação | Método | Resultado |
|---:|---|---|---|
| 1 | Sintaxe JavaScript do aplicativo | execução | APROVADO |
| 2 | Sintaxe do motor de jogo | execução | APROVADO |
| 3 | Banco completo passa pela validação de produção | execução | APROVADO |
| 4 | IDs das 400 questões são únicos | dados | APROVADO |
| 5 | Enunciados das 400 questões são únicos | dados | APROVADO |
| 6 | Módulo OAB contém 160 questões | dados | APROVADO |
| 7 | Módulo geral contém 240 questões | dados | APROVADO |
| 8 | OAB cobre 20 disciplinas | dados | APROVADO |
| 9 | Trivia cobre 9 categorias | dados | APROVADO |
| 10 | Questões OAB são identificadas como autorais | dados | APROVADO |
| 11 | Referências e fontes OAB presentes | dados | APROVADO |
| 12 | Banco vazio é rejeitado | injeção de falha | APROVADO |
| 13 | ID duplicado é rejeitado | injeção de falha | APROVADO |
| 14 | Gabarito fora do intervalo é rejeitado | injeção de falha | APROVADO |
| 15 | Quantidade incorreta de alternativas é rejeitada | injeção de falha | APROVADO |
| 16 | Alternativas duplicadas são rejeitadas | injeção de falha | APROVADO |
| 17 | Versão inválida é rejeitada | injeção de falha | APROVADO |
| 18 | Fonte com protocolo inseguro é rejeitada | injeção de falha | APROVADO |
| 19 | Desafio diário repetível e sem duplicação | execução | APROVADO |
| 20 | Desafio diário inclui cinco questões por módulo | execução | APROVADO |
| 21 | Caderno remove erro após acerto | execução | APROVADO |
| 22 | Ajuda 50/50 preserva gabarito em todas as posições | execução | APROVADO |
| 23 | Erros não pontuam e pontuação cresce | execução | APROVADO |
| 24 | Sequência diária atravessa virada do ano | execução | APROVADO |
| 25 | Fluxos: resposta dupla, três erros, tempo e diário | simulação de DOM | APROVADO |
| 26 | Assets JavaScript e JSON iguais no APK e web | comparação de bytes | APROVADO |
| 27 | Tela inicial contém recuperação sem JavaScript externo | revisão estrutural | APROVADO |
| 28 | Inicialização captura exceções nativas e incompatibilidade | revisão estrutural | APROVADO |
| 29 | Inicialização possui limite e confirmação de prontidão | revisão estrutural | APROVADO |
| 30 | Falhas do renderer e navegação têm diagnóstico | revisão estrutural | APROVADO |
| 31 | Ciclo de vida cancela callbacks e protege WebView ausente | revisão estrutural | APROVADO |
| 32 | Manifest declara launcher exportado e Android mínimo | revisão estrutural | APROVADO |
| 33 | Pacote preservado e versão incrementada para atualização | revisão estrutural | APROVADO |
| 34 | WebView bloqueia arquivo, conteúdo e conteúdo misto | revisão estrutural | APROVADO |
| 35 | APK assinado com v2/v3 e certificado compatível | ferramenta Android | APROVADO |
| 36 | Alinhamento e assets completos do APK final | ferramenta Android | APROVADO |
| 37 | Instalação e abertura pelo ícone no Samsung A53/Android 16 | aparelho/publicação | PENDENTE |
| 38 | Uso offline, suspensão e retorno no Android real | aparelho/publicação | PENDENTE |
| 39 | Atualização instalada preserva histórico no aparelho | aparelho/publicação | PENDENTE |
| 40 | Revisão editorial jurídica integral e validação para publicação nas lojas | aparelho/publicação | PENDENTE |

## Correções e validações sugeridas

1. Instalar por cima da versão anterior e abrir pelo ícone no Samsung. Em caso de falha, copiar o diagnóstico. Se nem a tela nativa abrir, obter logcat para identificar uma falha anterior à recuperação.
2. Validar uso offline, suspensão, retorno e preservação do histórico no aparelho. Não desinstalar a versão anterior para evitar perder dados locais.
3. Revisar integralmente o conteúdo jurídico com profissional responsável; ampliar questões situacionais e dificuldade antes do lançamento como preparatório completo.
4. Validar TalkBack, fonte ampliada e contraste; preparar privacidade, assinatura de produção e requisitos das lojas após a validação Android.

## Como instalar

Baixe Saber_em_Jogo_0.5_Android.apk e abra **Meus Arquivos → Downloads**. Instale a atualização e abra o ícone Saber em Jogo. A identidade do pacote e o certificado foram preservados; o teste de atualização no aparelho continua pendente.

Fontes técnicas consultadas: documentação Android de conteúdo local em WebView (https://developer.android.com/develop/ui/views/layout/webapps/load-local-content) e API WebViewAssetLoader (https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader). Sem alteração das perguntas jurídicas nesta rodada.

SHA-256 APK: `243a2e7a2274b36ae907949688d9dc246c521134ee020b4105c6f1c3c5e87e24`.
