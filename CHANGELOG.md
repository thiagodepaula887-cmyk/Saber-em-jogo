# 0.7 — sincronização da entrega em 21/10/2026

- 10.000 exercícios jurídicos e 240 gerais, biblioteca de 24 normas, pesquisa por lei/artigo e progresso.
- Código Android com lembretes, manifesto API 36 e scripts de APK/AAB recuperados do ZIP 0.7.
- Snapshots compactados versionados; prepare-content.py gera os JSON web e Android após clonar.
- Documentação de continuidade e pendências atualizada; Expo anterior preservado.
- 27 resultados Node aprovados. Build Android não repetido nesta sincronização; Play Protect e notificações em aparelho pendentes.

# 0.6.0-teste — 2026-10-20

- Seis simulados OAB: 42º ao 47º, PDF oficial tipo 1 + cartão de 80 respostas.
- Gabaritos definitivos, anuladas, meta 40/80, prazo opcional de cinco horas e retomada.
- Resultado bloqueado para edição e opção refazer; fontes em SIMULADOS_OAB.md.
- 19 resultados de testes Node aprovados e APK verificado; teste real em Android pendente.

# 0.5.0-teste — 2026-10-19

- Recuperação de inicialização e renderer, diagnóstico copiável e watchdog.
- Validação de banco e testes de falhas de carga e armazenamento.
- Build limpo, versionCode 5 e certificado de teste preservado.
- Lista de 40 pontos: 36 aprovados por execução/inspeção e quatro pendentes; sem reprodução em Samsung.

# Histórico de versões

## 0.4 — 16/10/2026

Na versão web e no APK Android offline:

- Modos Estudar e Desafio.
- Desafio com três vidas, pontuação progressiva e uma ajuda 50/50 por rodada.
- Cronômetro opcional de 30 segundos, calculado por prazo real, inclusive após saída temporária para segundo plano.
- Caderno de erros baseado na resposta mais recente; uma nova resposta correta remove a questão do caderno.
- Desafio diário determinístico com cinco perguntas OAB e cinco gerais, sem repetição interna.
- Registro local do melhor resultado diário e sequência de dias.
- Sons curtos opcionais de acerto e erro.
- Navegação pelo botão Voltar no Android.
- Atualização com o mesmo identificador e certificado da versão 0.3.

As perguntas continuam introdutórias; pontuação crescente não significa dificuldade adaptativa. Não há premiação em dinheiro. Histórico local independente entre web, APK e projeto Expo. O projeto Expo permanece na base anterior; esses recursos foram implementados na web e no APK offline.

Verificações: testes unitários do motor; teste do fluxo com DOM simulado, incluindo três erros, tempo expirado e conclusão diária; assinatura APK e zipalign. Não executado em aparelho real.

