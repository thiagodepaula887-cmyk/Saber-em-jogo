# Saber em Jogo — revisão 0.8

[Jogar na web](https://saber-em-jogo-thiago.thiagodepaula887.chatgpt.site).

A revisão remove as 9.788 lacunas de lei seca que podiam ser resolvidas por gramática. O treino padrão agora usa **40 casos autorais em 20 disciplinas**, com filtros médio/difícil e comentários. As **212 questões introdutórias** continuam em um filtro Básico explícito, com revisão individual pendente. Há ainda 240 perguntas de conhecimentos gerais e biblioteca de 24 normas.

**Provas oficiais:** seis exames OAB 42–47, Delegado PCMG 2025, Defensor DPE-PE 2025 e Promotor MPRJ 2025. Cadernos originais em PDF e cartão no app, com gabaritos definitivos. Os 280 itens dos concursos não foram transcritos ao quiz; não têm comentários individuais. O treino de concurso não calcula aprovação pelo edital.

## Executar

Requer Python 3 e Node.js:

```bash
python3 web/scripts/prepare-content.py
python3 -m http.server 8080 --directory web/dist
```

Abra http://localhost:8080. Para testar:

```bash
cd web
node --test tests/*.test.cjs
```

Para editar/reconstruir os casos: `python3 web/scripts/review-content.py`, seguido do preparo. A fonte ativa é `web/content/questions.v8.json.gz`; o snapshot v7 é histórico. O gerador de lacunas foi desativado.

## Continuidade

- [Revisão, fontes, contagens e limites](REVISAO_PEDAGOGICA_08.md)
- [Guia técnico e arquitetura](PROJETO_SABER_EM_JOGO.md)
- [Histórico e problemas abertos](HISTORICO_E_PENDENCIAS_SABER_EM_JOGO.md)
- [Alterações](CHANGELOG.md)

29 resultados automatizados aprovados. Revisão jurídica integral das 10 mil questões **não concluída**; não anunciar 10 mil questões revisadas ou de banca. Dificuldade dos casos é estimativa editorial. A conferência visual no navegador ficou bloqueada neste ambiente.

`web/` contém a versão atual. `android-offline/` contém Java/WebView e os assets revisados; **APK 0.8 compilado e assinado com o mesmo certificado do APK 0.7**. Instalação em aparelho e Play Protect ainda não validados. [Baixar APK 0.8](https://drive.google.com/file/d/1MQb4O4vpKAJGzwleyeDsHY23D8KPh98s/view). `mobile/` é uma base Expo histórica. Chaves privadas e senhas não são publicadas. Play Protect continua pendente. Progresso local, sem sincronização entre dispositivos.
