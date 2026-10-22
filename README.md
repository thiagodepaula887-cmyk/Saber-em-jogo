# Saber em Jogo — versão 0.7

Quiz de conhecimentos gerais e estudo do Direito: **10.000 exercícios jurídicos em 20 disciplinas + 240 gerais**, biblioteca de 24 normas, pesquisa por lei/artigo, progresso local e simulados dos exames OAB 42–47.

Jogar: https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site

## Executar e testar

Requer Python 3 e Node.js. Na raiz do repositório:

```bash
python3 web/scripts/prepare-content.py
python3 -m http.server 8080 --directory web/dist
```

Abra http://localhost:8080. Em outro terminal:

```bash
cd web
node --test tests/*.test.cjs
```

Os snapshots compactados de `web/content/*.v7.json.gz` são a fonte versionada. O preparo expande os dados para web e Android, sem baixar dependências ou leis. Os JSON gerados não são versionados. Não execute o gerador legado de 400 questões para preparar a versão 0.7.

## Implementações

- `web/`: HTML/CSS/JavaScript da versão atual; pode ser hospedado como site estático.
- `android-offline/`: Java/WebView, assets locais, diagnóstico e lembretes; origem do APK 0.7. Veja [guia técnico](PROJETO_SABER_EM_JOGO.md) para o ambiente de compilação.
- `mobile/`: base Expo/SQLite anterior, separada do APK distribuído.

O APK funciona sem conta ChatGPT. O progresso fica no navegador/aparelho, sem sincronização. PDFs oficiais externos exigem internet. Não há instalador iOS nem publicação em loja.

## Conteúdo e continuidade

Das 10.000 questões jurídicas, 9.788 são lacunas de lei seca e 212 são conceituais. Não são 10.000 questões oficiais FGV; revisão jurídica individual permanece pendente. Os simulados usam PDFs oficiais e cartões de resposta, separados do banco autoral.

- [Guia técnico e comandos](PROJETO_SABER_EM_JOGO.md)
- [Histórico e problemas abertos](HISTORICO_E_PENDENCIAS_SABER_EM_JOGO.md)
- [Expansão e limites editoriais](EXPANSAO_10000.md)
- [Simulados OAB](SIMULADOS_OAB.md)
- [Alterações](CHANGELOG.md)

27 resultados de testes automatizados aprovados nesta sincronização. Compilação Android não foi repetida nesta atualização do GitHub. O aviso Play Protect e os testes de notificações em aparelho continuam pendentes. Chaves privadas, senhas, APKs e AABs não são publicados neste repositório.

