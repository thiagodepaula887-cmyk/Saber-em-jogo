> Atualização 22/10/2026: a revisão web 0.8 retirou as lacunas e separou o básico. Consulte ../REVISAO_PEDAGOGICA_08.md para a contagem atual e limites. As descrições da 0.7 abaixo são históricas; o APK 0.8 foi posteriormente compilado, assinado e verificado; instalação em aparelho e Play Protect pendentes.

# Android offline — APK de teste

## Estado atual: 0.7

O APK atual usa 10.000 exercícios jurídicos, 240 gerais e biblioteca de 24 normas, com pesquisa, progresso e lembretes. Execute `python3 web/scripts/prepare-content.py` na raiz antes de trabalhar nos assets. O ambiente de compilação atual (API 36, build-tools 35, AAPT2 e bundletool) está descrito em [PROJETO_SABER_EM_JOGO.md](../PROJETO_SABER_EM_JOGO.md). As notas abaixo são históricas da 0.4/0.6. A instalação da 0.7 foi confirmada pelo proprietário; o aviso Play Protect e a entrega de notificações em aparelho continuam pendentes. A compilação Android não foi repetida durante a sincronização GitHub.

Aplicativo Android instalável, independente do Expo Go, com a interface web e as 400 questões embarcadas e os modos de jogo descritos no CHANGELOG.md. Compatibilidade declarada: Android 8.0 (API 26) ou superior. Assinatura de teste, sem publicação nas lojas. A instalação não foi validada em aparelho/emulador nesta entrega.

## Implementação

Activity Java com WebView, conteúdo servido de assets por interceptação de URL HTTPS em origem local. Sem permissão de internet ou acesso ao armazenamento externo. Fontes externas são abertas no navegador do aparelho. Histórico em localStorage, independente do SQLite do projeto Expo. Não usa servidor remoto para jogar.

Este é um pacote Android offline separado do projeto React Native de `mobile/`. O APK atual foi produzido desta pasta. O projeto Expo permanece como base multiplataforma para evolução e futura distribuição iOS.

## Compilação

Usa Java 17, compilador Eclipse ECJ 3.37.0, platform Android 35 (platform-35_r02.zip) e build-tools 35.0.0 (build-tools_r35_linux.zip), obtidos dos fornecedores oficiais. O diretório apontado por QUIZ_ANDROID_TOOLS deve conter `android-35/android.jar`, `android-15/` com as build-tools extraídas e `ecj.jar`. Executar `python3 build.py`.

Verificações executadas: compilação de recursos e Java, conversão DEX, zipalign, assinatura e verificação apksigner v2/v3, pacote e manifesto com aapt2, e correspondência de todas as 400 questões ao banco da web. Sem bibliotecas nativas específicas de CPU.

A chave de teste não está neste repositório e permanece no backup privado do proprietário para permitir atualizações de teste. Não usar essa chave em produção. Não publicar keystores no GitHub; `.gitignore` os exclui.

Mudanças no conteúdo offline exigem nova compilação e instalação de atualização. Desinstalar apaga o progresso local.

Versão 0.4: mesmo pacote e certificado de teste da 0.3. Instale por cima da versão anterior para preservar o progresso. Não desinstale antes de atualizar.


Versão 0.6: simulados oficiais 42–47 com cartão e gabarito embarcados. PDFs oficiais abrem no navegador externo e exigem conexão para obter o caderno. Mantidos pacote e certificado de teste.
