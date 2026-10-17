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
