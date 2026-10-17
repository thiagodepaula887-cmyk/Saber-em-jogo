# Validação — 16/10/2026

- `npm run typecheck`: aprovado.
- `npm test`: 7 testes aprovados, zero falhas, SQLite real via Node 24.
- `npx expo export --platform android --platform ios --output-dir artifacts`: aprovado, bundles Hermes para Android e iOS.

Casos exercitados: sementes dos dois módulos; rejeição de dados inválidos; rollback integral por conflito; preservação de versões antigas; idempotência e bloqueio de troca de resposta; sessão/versão inválida; conclusão incompleta; downgrade; duplicidade de IDs; inicialização repetida e integridade de chaves estrangeiras.

Limites: não executado em emulador ou aparelho real; não testado com VoiceOver/TalkBack; sem compilação nativa assinada ou publicação. O teste do banco usa a mesma lógica de produção com adaptador SQLite do Node; o adaptador nativo foi validado por tipagem e empacotamento, não por execução em dispositivo.
