> Atualização 22/10/2026: a revisão web 0.8 retirou as lacunas e separou o básico. Consulte REVISAO_PEDAGOGICA_08.md para a contagem atual e limites. As descrições da 0.7 abaixo são históricas; o APK 0.8 foi posteriormente compilado, assinado e verificado; instalação em aparelho e Play Protect pendentes.

# Saber em Jogo — entrega e continuidade

Estado confirmado em 21/10/2026: versão 0.7.

## Arquivos e controle

- Web pública: https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site
- Código completo atualizado: Saber_em_Jogo_0.7_Codigo.zip, nesta pasta do Drive. O GitHub contém a sincronização da entrega 0.7; o ZIP preserva a entrega anterior a essa sincronização.
- APK: Saber_em_Jogo_0.7_Android.apk. Independente do ChatGPT e com dados locais.
- AAB: Saber_em_Jogo_0.7_Play.aab. Gerado e assinado, sem publicação na Play Store. O proprietário decidiu não pagar o cadastro por enquanto.
- Repositório: https://github.com/thiagodepaula887-cmyk/Saber-em-jogo
- Chaves privadas: CHAVES_ASSINATURA_PRIVADAS.zip, separado. Nunca publicar no GitHub ou compartilhar com usuários do jogo.

O proprietário controla o Drive e o GitHub pela sua própria conta. A publicação atual usa Sites da conta ChatGPT do proprietário. Outro profissional precisa de acesso autorizado para alterar essa publicação; pode também hospedar os arquivos estáticos em outro serviço. Código, conteúdo e execução local não dependem do ChatGPT.

## Arquitetura atual

A versão entregue usa HTML/CSS/JavaScript em web/dist. O APK é um aplicativo Android Java com WebView e arquivos locais em android-offline/assets. A pasta mobile contém uma base Expo anterior; não é a origem do APK 0.7 entregue. Não confundir as duas implementações.

web/dist/app.js: navegação e quiz; game-engine.js: regras; study-engine.js e study-ui.js: busca, biblioteca e progresso; exam-engine.js e exam-ui.js: provas anteriores. android-offline/src contém a Activity e os lembretes. Não há servidor de usuários, login ou sincronização do histórico; os dados de progresso ficam no dispositivo/navegador.

## Executar e testar

Requer Python 3 e Node.js para os testes. Na raiz extraída:

```bash
python3 web/scripts/prepare-content.py
python3 -m http.server 8080 --directory web/dist
```

Abrir http://localhost:8080. Para os testes, em outro terminal:

```bash
cd web
node --test tests/*.test.cjs
```

Resultado anterior: 27 testes aprovados. Navegação, busca por 8906/94 e leitor do art. 7 também foram verificados no navegador. A instalação foi confirmada pelo proprietário; entrega de notificações, reinício e bloqueio do Play Protect ainda exigem verificação em aparelhos.

## Conteúdo

10.000 questões jurídicas (9.788 exercícios de completar lei seca e 212 conceituais), mais 240 gerais. Não são 10.000 questões FGV. Revisão jurídica individual completa pendente. Biblioteca de 24 normas federais, sem pretensão de conter todo o Direito brasileiro. Ver EXPANSAO_10000.md e web/content/manifest.json.

As fontes canônicas são questions.v7.json.gz e law-library.v7.json.gz, em web/content. prepare-content.py expande para web e Android. Ao editar os dados, manter os arquivos comprimidos e os dados gerados coerentes. Atualizações de questões devem incrementar sua versão para o progresso não confundir versões. O importador exige BeautifulSoup/html5lib (requirements-content.txt); a importação jurídica precisa de conferência editorial.

Provas anteriores: exames 42 a 47, documentos oficiais e 480 posições de gabarito. Não afirmar que há 480 enunciados oficiais incorporados ao banco autoral.

## Gerar Android

Java 17, Python 3 e ferramentas Android são necessárias. build.py usa um diretório definido por QUIZ_ANDROID_TOOLS com este layout específico:

- android-15/: aapt2, d8, zipalign e apksigner das build-tools 35, com seus arquivos auxiliares;
- android-36/android.jar: plataforma Android API 36;
- ecj.jar: Eclipse Compiler 3.37;
- aapt2-maven/aapt2: AAPT2 8.9.1-12782657;
- bundletool.jar: bundletool 1.18.3.

As ferramentas são dependências externas e não estão dentro do ZIP de código. O próximo programador deve instalar/configurar esse layout ou adaptar os scripts ao SDK padrão/Gradle. A reprodução não é de um clique em qualquer computador.

```bash
QUIZ_ANDROID_TOOLS=/caminho/das/ferramentas python3 android-offline/build.py
QUIZ_ANDROID_TOOLS=/caminho/das/ferramentas python3 android-offline/build-bundle.py /caminho/privado/upload-key.json
```

Restaurar a chave de teste original em android-offline/test-signing.keystore para atualizar os APKs de teste existentes. O backup privado inclui esta chave, a chave de upload do AAB e suas configurações; ajustar somente o caminho keystore do JSON ao computador novo. As chaves de teste e upload são diferentes. Antes de produção, definir uma estratégia definitiva de assinatura e migração. Preservar o identificador com.thiagolucas.saberemjogo e incrementar versionCode nas atualizações.

## Pendências para o próximo responsável

1. Manter o GitHub atualizado a cada alteração, sem chaves ou senhas.
2. Diagnosticar o texto exato do aviso Play Protect; não prometer que assinatura ou publicação resolve automaticamente.
3. Revisar juridicamente e melhorar a variedade/dificuldade das questões.
4. Testar notificações e instalação em aparelhos reais.
5. Se houver publicação comercial: privacidade, suporte, materiais da loja, testes e exigências da plataforma.

A pasta do Drive é privada do proprietário. Outro programador precisa que ele conceda acesso; uma IA precisa receber os arquivos ou ter uma conexão autorizada. O link público do jogo permite jogar, não editar o código nem administrar contas.

