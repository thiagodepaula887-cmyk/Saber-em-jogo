## Atualização 0.6 — simulados OAB

Os exames 42º a 47º estão acessíveis na capa: PDF oficial branco/tipo 1 e cartão de 80 respostas com correção definitiva, anuladas, prazo opcional e retomada. Consulte [SIMULADOS_OAB.md](SIMULADOS_OAB.md). O APK contém cartão/gabaritos; leitura do caderno usa o PDF externo. Teste de instalação em aparelho continua pendente.

# Saber em Jogo

Aplicativo de perguntas e respostas: 400 questões autorais, sendo 160 jurídicas em 20 disciplinas e 240 gerais em nove categorias.

Teste: https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site

- `android-offline/`: código Java e assets usados no APK de teste 0.4, que funciona sem Expo Go.
- `web/`: versão publicada, conteúdo editorial e testes.
- `mobile/`: projeto React Native/Expo/SQLite para evolução multiplataforma, separado do APK atual.

Web: `cd web && node tests/web.test.cjs`.
Mobile: `cd mobile && npm ci && npm run typecheck && npm test`.

Para baixar o APK Android, use o botão Baixar Android no site. Não há binário iOS nesta versão. Compilação e assinatura verificadas; instalação em aparelho real ainda precisa de validação.

Perguntas autorais de fixação, sem vínculo com OAB/FGV. Chaves de assinatura, dados de usuários e credenciais não são versionados. Veja os READMEs de cada pasta e PROJETO_SABER_EM_JOGO.md.

Novidades na web e no APK 0.4: modo Desafio, ajuda 50/50, cronômetro opcional, caderno de erros e desafio diário. Veja CHANGELOG.md.
