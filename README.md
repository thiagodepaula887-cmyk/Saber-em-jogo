# Saber em Jogo

Aplicativo de perguntas e respostas: 400 questões autorais, sendo 160 jurídicas em 20 disciplinas e 240 gerais em nove categorias.

Teste: https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site

- `android-offline/`: código Java e assets usados no APK de teste 0.3, que funciona sem Expo Go.
- `web/`: versão publicada, conteúdo editorial e testes.
- `mobile/`: projeto React Native/Expo/SQLite para evolução multiplataforma, separado do APK atual.

Web: `cd web && node tests/web.test.cjs`.
Mobile: `cd mobile && npm ci && npm run typecheck && npm test`.

Para baixar o APK Android, use o botão Baixar Android no site. Não há binário iOS nesta versão. Compilação e assinatura verificadas; instalação em aparelho real ainda precisa de validação.

Perguntas autorais de fixação, sem vínculo com OAB/FGV. Chaves de assinatura, dados de usuários e credenciais não são versionados. Veja os READMEs de cada pasta e PROJETO_SABER_EM_JOGO.md.
