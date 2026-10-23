# Saber em Jogo — versão 0.9

[Jogar](https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site) · [Baixar Android 0.9](https://drive.google.com/file/d/1MQb4O4vpKAJGzwleyeDsHY23D8KPh98s/view)

**10.040 questões jurídicas**: as 10.000 anteriores foram restauradas, mantendo os 40 casos novos. O banco completo está acessível por padrão. Os exercícios antigos estão identificados com revisão pendente: a restauração não corrige sua baixa dificuldade. Há filtros separados para casos revisados, nível e lei seca; as 240 perguntas gerais e a biblioteca de 24 normas permanecem disponíveis.

Nove provas oficiais: OAB 42–47, Delegado PCMG 2025, Defensor DPE-PE 2025 e Promotor MPRJ 2025. Cadernos originais em PDF externo e cartão no app com gabaritos definitivos; não são enunciados transcritos ao quiz nem têm comentários individuais. O treino de concurso não calcula aprovação segundo o edital.

## Executar e testar

```bash
python3 web/scripts/prepare-content.py
python3 -m http.server 8080 --directory web/dist
```

Em outro terminal:

```bash
cd web
node --test tests/*.test.cjs
```

31 resultados aprovados, incluindo preservação dos campos originais por ID e filtros. As fontes canônicas são o snapshot `questions.v7.json.gz`, a biblioteca v7 e os casos de `casos-revisados.py`; o preparo gera o snapshot v9 e os JSON de execução para web e Android. Não usar o gerador antigo de alternativas aleatórias.

[Correção e pendências da 0.9](RESTAURACAO_09.md) · [Histórico da revisão 0.8](REVISAO_PEDAGOGICA_08.md) · [Guia técnico](PROJETO_SABER_EM_JOGO.md) · [Alterações](CHANGELOG.md)

`web/`: versão atual. `android-offline/`: Java/WebView com arquivos locais. `mobile/`: base Expo histórica. Progresso local, sem sincronização entre dispositivos. Chaves e senhas não são publicadas. A instalação no A53 e o Play Protect não foram validados. O jogo **não está publicado na Google Play**.
