# Saber em Jogo — MVP mobile 0.1

Projeto React Native + Expo + TypeScript para Android e iOS. Nome provisório.

## Executar

Requisitos: Node.js 24 e npm. Na pasta do projeto:

```sh
npm ci
npx expo start
```

Abra com uma versão compatível do Expo Go no celular, usando o QR code exibido pelo Expo. O computador e o celular precisam conseguir se comunicar pela rede. Para desenvolvimento nativo, use emulador Android ou simulador iOS no macOS.

```sh
npm run typecheck
npm test
npx expo export --platform android --platform ios
```

## Entregue nesta versão

- Dois módulos: OAB e conhecimentos gerais.
- Seleção de disciplina e das nove categorias gerais.
- Partida com até dez perguntas, ordem aleatória, comentário e resultado.
- XP e nível derivados das respostas corretas; estatísticas locais.
- 400 questões autorais: 160 jurídicas em 20 disciplinas e 240 gerais em nove categorias.
- SQLite offline com chaves estrangeiras, versões imutáveis e importação atômica.
- Respostas vinculadas à sessão e à versão exata da pergunta.
- Repetição da mesma gravação é idempotente; uma resposta diferente para a mesma pergunta é rejeitada.
- Proteção de interface contra seleção, avanço e conclusão duplicados.
- Feedback textual de acerto, erro e falha de gravação.
- Áreas seguras e tamanho de texto adaptável ao sistema.

## Organização

- `App.tsx`: início, seleção, estatísticas e resultado.
- `src/screens/QuizScreen.tsx`: interação da partida.
- `src/types/quiz.ts`: contratos, validação de JSON e serialização determinística.
- `src/database/schema.ts`: migração inicial.
- `src/database/repository.ts`: importação, consulta e histórico, sem dependência nativa.
- `src/database/db.ts`: adaptador expo-sqlite.
- `src/data/seed.ts`: conteúdo inicial.
- `tests/repository.cjs`: testes com SQLite real do Node, reutilizando o repositório de produção.

## Regras de conteúdo e versões

Importações recebem `unknown`, validam o envelope e o conteúdo de acordo com o módulo. Questões OAB exigem referências legais e origem; questões gerais não precisam de campos jurídicos. As quatro alternativas devem ser não vazias e distintas.

A combinação `(id, version)` é imutável. Reimportar o mesmo conteúdo é permitido; alterá-lo sem aumentar a versão rejeita o lote inteiro. A versão antiga permanece no banco e partidas já iniciadas continuam usando seu próprio gabarito. A consulta para novas partidas seleciona a última versão. IDs repetidos no mesmo lote, inclusive com versões distintas, são rejeitados deliberadamente. Um lote publica somente uma revisão por ID.

O banco desta implementação usa `saber_em_jogo_v1.db`, um arquivo novo: não modifica nem migra bancos dos exemplos anteriores. `PRAGMA user_version` aplica a migração inicial uma vez e rejeita esquemas futuros. Migrações de versões futuras deverão ser adicionadas explicitamente, preservando dados existentes.

A validação técnica não substitui revisão editorial e jurídica. O conteúdo inicial não é uma preparação completa nem representa questões oficiais da FGV. Atualizar legislação exige revisão do conteúdo e incremento de versão.

## Privacidade e persistência

Não há login, nuvem, anúncios, pagamentos, rastreadores ou envio de respostas nesta versão. Dados ficam no aparelho; desinstalar o app remove o histórico. Partidas interrompidas mantêm respostas no histórico, mas ainda não podem ser retomadas. Não há ranking competitivo: um banco local pode ser modificado pelo usuário.

## Compilação nativa e lojas

`eas.json` inclui perfis preview (APK Android) e production. Nenhum APK/AAB/IPA foi gerado ou assinado nesta entrega. A exportação Metro valida os pacotes JavaScript, não substitui compilação nativa nem teste em aparelho.

Próximas etapas para binários:

1. Definir identificadores Android/iOS próprios em `app.json`, ícone e nome definitivos.
2. Vincular este projeto a uma conta Expo/EAS usando `npx eas-cli@latest init`.
3. Para APK de teste: `npx eas-cli@latest build --platform android --profile preview`.
4. Para produção: configurar contas de desenvolvedor, credenciais de assinatura e executar `npx eas-cli@latest build --platform all --profile production`.
5. Validar em aparelhos Android/iOS, preparar privacidade, suporte, classificação etária e materiais das lojas.

O perfil development exige instalação de `expo-dev-client` antes de uso. Publicação nas lojas e configuração de contas não foram realizadas. A aceitação depende da análise de cada loja.

## Ainda fora do MVP

Sincronização em nuvem, painel editorial, importação remota, login, revisão espaçada, retomada de partida, simulados completos, áudio, conquistas persistentes, desafio diário, assinaturas e ranking. Os ícones incluídos pelo template Expo são provisórios.
