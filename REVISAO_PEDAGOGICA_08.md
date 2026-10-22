# Revisão pedagógica 0.8 — 22/10/2026

## Diagnóstico e alcance

O usuário identificou que as questões de completar lei seca podiam ser respondidas por concordância ou associação vocabular. O gerador escolhia uma palavra do artigo e três palavras aleatórias de um conjunto genérico, sem equivalência gramatical ou plausibilidade jurídica. Os testes da 0.7 validavam quantidade, estrutura, fonte e execução; não demonstravam qualidade pedagógica. A entrega anterior de 10 mil exercícios não equivalia a 10 mil questões de concurso.

Foi feito um inventário dos 10.000 registros jurídicos da 0.7, com decisão e motivo por identificador em `web/content/editorial-audit.v8.json.gz`. Isso é uma triagem pedagógica de todo o lote, não revisão jurídica individual integral.

- 9.788 lacunas retiradas do banco ativo e de todos os sorteios. A versão anterior permanece no histórico e no snapshot v7, sem ser carregada pelo jogo.
- 212 conceitos mantidos apenas como nível Básico, por escolha explícita, com indicação de revisão individual pendente. Não são tratados como questões avançadas.
- 40 novos casos autorais: dois por cada uma das 20 disciplinas. Todos têm alternativas completas, uma resposta, justificativa, fonte e distinções jurídicas. O filtro padrão reúne os casos; há filtros médio e difícil, com 20 casos cada.
- O rótulo de dificuldade é estimativa editorial, não calibração estatística nem equivalência garantida ao grau de exigência de determinada carreira.
- Os casos autorais NÃO são apresentados como questões aplicadas pela FGV. Dois de Filosofia são problemas conceituais, com referências teóricas, sem falsa referência legal.
- O desafio diário e o sorteio jurídico padrão também excluem o básico e as lacunas retiradas. O histórico local é preservado; questões retiradas deixam de integrar a cobertura do banco atual. XP antigo continua sendo histórico, não prova de domínio.

## Provas oficiais localizadas e incluídas

Disponíveis em Provas de OAB e concursos, preservando o caderno original em PDF e usando cartão de respostas no aplicativo. Os enunciados dessas provas NÃO foram incorporados pergunta a pergunta ao banco de casos autorais; não há comentários individuais das 280 questões. PDF externo requer internet para obter o documento. Não há anúncio de aprovação nos concursos: o cartão só soma acertos e pontos por anuladas, sem aplicar notas mínimas por blocos ou demais critérios do edital.

| Prova | Data | Caderno | Questões | Tempo | Gabarito |
|---|---|---|---:|---:|---|
| Delegado PCMG | 26/01/2025 | tipo 1 branca | 80 | 270 min | definitivo |
| Defensor DPE-PE | 01/06/2025 | tipo 1 branca | 100 | 300 min | definitivo |
| Promotor MPRJ | 03/08/2025 | tipo 1 branca | 100 | 300 min | definitivo |

Fontes oficiais:

- https://conhecimento.fgv.br/concursos/pcmg24/01
- https://conhecimento.fgv.br/concursos/dpe-pe
- https://conhecimento.fgv.br/concursos/mprjpromotor2025

Os URLs exatos dos cadernos e gabaritos estão em `web/dist/exams.json`. O gabarito definitivo PCMG altera a questão 4 para B em relação ao preliminar. No MPRJ, anuladas 33, 43, 69, 72 e 86 do tipo 1 são tratadas como anuladas. Os seis exames OAB 42–47 continuam disponíveis, com seus 480 itens de cartão; não são contados como questões autorais novas.

## Contagem atual e reprodução

Banco de quiz: 492 registros = 40 casos + 212 básicos opcionais + 240 conhecimentos gerais. Provas oficiais: 760 posições de cartão, em nove cadernos externos. Biblioteca: 24 normas. Não somar essas categorias para anunciar 10 mil questões revisadas.

```bash
python3 web/scripts/review-content.py
python3 web/scripts/prepare-content.py
cd web
node --test tests/*.test.cjs
```

O arquivo `web/content/casos-revisados.py` é a fonte editorial dos 40 casos. `review-content.py` recria o snapshot v8, a triagem e o manifest de maneira determinística. `prepare-content.py` expande `questions.v8.json.gz` e `law-library.v7.json.gz` para web e Android. O gerador de lacunas foi desativado para impedir sua reintrodução acidental.

## Validação e pendências

29 resultados automatizados aprovados: regressão dos modos de jogo, filtros, origem e fonte, biblioteca, continuidade dos cartões OAB, cinco alternativas, provas com 100 posições, anulações, ausência de aprovação fictícia nos concursos. Em 10 de 40 casos, a correta é a alternativa mais longa; tamanho não é critério confiável de resposta. Esse diagnóstico não substitui teste de dificuldade com estudantes.

A conferência visual pelo navegador não pôde ser concluída por bloqueio do ambiente. O código e os assets Android receberam a revisão; não foi gerado nem testado um novo APK neste ambiente, que não possui o conjunto de ferramentas de compilação Android. O download Android é identificado como 0.7/banco anterior. Instalação e Play Protect continuam pendentes e independentes desta revisão de conteúdo.

Ainda falta substituir editorialmente os 9.788 itens retirados e revisar individualmente os 212 básicos; ampliar o banco de casos; integrar enunciados oficiais na experiência pergunta a pergunta quando houver fonte e possibilidade de uso; validar atualização legislativa/jurisprudencial e dificuldade por desempenho. Não afirmar que essa revisão integral foi concluída.
