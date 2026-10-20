# Simulados oficiais OAB — versão 0.6

Atualização de 20/10/2026. Seleção das seis primeiras fases mais recentes já aplicadas e com gabarito definitivo: exames 42 a 47. O 48º tem 1ª fase prevista para 10/01/2027 (fonte: https://examedeordem.oab.org.br/Noticias/Noticia/64648).

## Experiência entregue

Entrada “Simulados OAB · provas oficiais” na capa. Cada prova usa o caderno branco tipo 1, aberto por link oficial no navegador/leitor PDF do usuário. O app contém o cartão de 80 respostas e o gabarito definitivo; os enunciados não foram transcritos para o banco de questões do quiz. Os cadernos não estão embarcados no APK: requerem conexão para abrir/baixar pela primeira vez. O usuário lê o caderno e volta para marcar as respostas, que podem ser alteradas até a finalização.

Sem comentários jurídicos individuais neste modo. Nota de treino 0–80, meta 40, acertos, erros, respostas em branco e pontos de anuladas separados. Timer opcional de cinco horas corridas; rascunho e último resultado por exame no localStorage `saber-exams-v1`. O tempo continua fora do app. O usuário pode sair e retomar. Sem login ou sincronização entre aparelhos. Os dois módulos anteriores e o banco de 400 questões autorais permanecem independentes.

## Documentos usados

Gabaritos definitivos do tipo 1 conferidos a partir dos PDFs oficiais; no 42º foi usado o documento retificado. Os hashes são do PDF de gabarito para rastreabilidade. Não se afirma revisão da legislação atual de cada enunciado antigo.

### 47º Exame — 2026-09-06

- Caderno oficial: https://s.oab.org.br/arquivos/2026/09/7d502f11-d906-4378-bd43-27e0c854b981.pdf
- Gabarito definitivo: https://s.oab.org.br/arquivos/2026/09/572dc8e2-78a0-4e37-b6de-20709e2c59ab.pdf
- Anuladas no tipo 1: 47.
- SHA-256 do gabarito: `480e9da40f4609a9515c20a9de6a239e8be601069b34e3bc09ac699d3d69d669`.

### 46º Exame — 2026-05-03

- Caderno oficial: https://s.oab.org.br/arquivos/2026/05/b5f2a4bd-8885-4f42-909f-a2ecac329dab.pdf
- Gabarito definitivo: https://s.oab.org.br/arquivos/2026/05/0662d6ed-01a3-4ee5-905f-a6704d72992b.pdf
- Anuladas no tipo 1: nenhuma no documento utilizado.
- SHA-256 do gabarito: `c57ac6a6c713f5efa3c3976506cb7f204f734b8ffb34d22cc0d3e23ab6651a5a`.

### 45º Exame — 2025-12-21

- Caderno oficial: https://s.oab.org.br/arquivos/2025/12/d092ea6d-5bdc-435e-a043-31520b8cdc95.pdf
- Gabarito definitivo: https://s.oab.org.br/arquivos/2026/01/183549bb-ee34-4ac4-aefb-5962d96acca0.pdf
- Anuladas no tipo 1: nenhuma no documento utilizado.
- SHA-256 do gabarito: `a3c90403f91370714d631063896eac3e96a5cfdd0490e7490e5a4b58b20345a6`.

### 44º Exame — 2025-08-17

- Caderno oficial: https://s.oab.org.br/arquivos/2025/08/fda2cc49-fbbd-4893-9b75-0f61c177cd5d.pdf
- Gabarito definitivo: https://s.oab.org.br/arquivos/2025/09/b6fb7503-e2cf-4e9b-8b0a-9b822df591fe.pdf
- Anuladas no tipo 1: nenhuma no documento utilizado.
- SHA-256 do gabarito: `ae020716059b5913da3ff15b3ab8ed2e86a9658051f891c21f704e1c7f435d12`.

### 43º Exame — 2025-04-27

- Caderno oficial: https://s.oab.org.br/arquivos/2025/04/145104f9-1301-453d-9079-3d5af4f8e60a.pdf
- Gabarito definitivo: https://s.oab.org.br/arquivos/2025/05/2d003602-840e-4ef2-9a4a-004144a35268.pdf
- Anuladas no tipo 1: 1, 74.
- SHA-256 do gabarito: `31e27871a5efb011d71a737e47c690b6126b894c908e8423aa28c5c600792bf4`.

### 42º Exame — 2024-12-01

- Caderno oficial: https://s.oab.org.br/arquivos/2024/12/6588c7e0-3c87-4efd-a0f5-ebef5dfcbb74.pdf
- Gabarito definitivo: https://s.oab.org.br/arquivos/2024/12/f7a7e51f-5468-402d-b594-c09a0e499b9f.pdf
- Anuladas no tipo 1: 43.
- SHA-256 do gabarito: `acc91b855bc6769a24eb1b08ed60833f9f1773c0f36ce76315f7d496b0b0385c`.

## Validação

19 resultados de testes Node aprovados, incluindo seis cenários do motor dos simulados, dois fluxos de UI com DOM simulado e regressões anteriores. Testados todos os gabaritos completos (80 pontos), todas as respostas em branco, anuladas, limiar 39/40, rejeição de dados inválidos, restauração de rascunho e tempo esgotado. Build Java/D8, assinatura v2/v3, certificado anterior e zipalign aprovados. A lista de 40 pontos foi reexecutada: 36 aprovados por testes/inspeção, quatro dependentes de aparelho/publicação permanecem pendentes.

Sem teste visual em navegador real ou instalação em Samsung nesta rodada. É necessário conferir abertura dos PDFs no Android real, troca entre navegador e app, fonte ampliada e atualização com preservação dos dados. Nenhum APK iOS/AAB de produção foi produzido.

## Entrega

APK: https://drive.google.com/file/d/18QgIpXDTE27jR3p5HQk1VqOCR_lHO--a/view?usp=drivesdk

Instalar por cima da versão anterior, sem desinstalar. Código e conteúdo de simulados no GitHub; backup privado inclui chave de teste, que não deve ser publicada nem usada em produção.

SHA-256 APK: `a175802cac9782155fef0a2a5c69db3adb65cf64bf448d1a2bf8fd640785be7d`.
