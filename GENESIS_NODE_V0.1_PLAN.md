# Genesis Node v0.1 — Decisão Estratégica

## Modelo escolhido

**D) Completo (todas as camadas ativas)**, com ativação em fases para reduzir risco operacional sem perder a definição formal de Genesis Node.

## Justificativa

O material já descreve que os componentes principais existem (`cerberosGate`, `metrics`, `executeAndAnchor`, `qiskitRunner`, `polygonMinter`), então o gargalo é integração, consistência e auditabilidade — não pesquisa inicial.

Escolher o modelo completo evita publicar um "quase-nó" e garante que o primeiro release público já cumpra o princípio de organismo auditável fim-a-fim:

1. decisão constitucional (Ω-GATE),
2. cálculo métrico (Ψ, CVaR, Ω, PoLE),
3. execução reprodutível (quântico/simulador),
4. evidência verificável (hash + ledger),
5. ancoragem pública opcional.

## Definição operacional de pronto para público

O Genesis Node v0.1 só deve ser exposto publicamente quando estes critérios estiverem simultaneamente verdadeiros:

- `fail-closed` ativo (erro => `REJECT`);
- thresholds congelados e versionados (`Ψ >= 0.85`, `CVaR <= 0.05`, `Ω >= 0.85`);
- replay determinístico validado (`hash(state) == hash(replay(state))`);
- bundle de evidência assinado e persistido em ledger local;
- caminho de ancoragem testado (on-chain ou dataset auditável);
- release com commit hash, tag (`v0.1.0`) e imagem Docker com digest fixo.

## Plano de execução recomendado

### Fase 1 — Constituição e métricas (dia 1)

- consolidar módulos duplicados;
- congelar fórmulas e thresholds em um único arquivo de configuração imutável;
- garantir que toda exceção no pipeline termine em `REJECT`.

### Fase 2 — Reprodutibilidade (dia 2)

- executar bateria de replay determinístico;
- gerar vetor de testes com casos `ALLOW`, `QUARANTINE`, `REJECT`;
- validar estabilidade de hash do Evidence Bundle.

### Fase 3 — Exposição pública controlada (dia 3)

- deploy com Docker digest fixo;
- publicar endpoint de execução e endpoint de saúde;
- documentar procedimento de reconstrução a partir do commit.

### Fase 4 — Ancoragem e nota de evidência (dia 4)

- ancorar hash do release (Polygon Amoy/Sepolia ou alternativa auditável);
- publicar Evidence Note com hashes, assinatura e instrução de verificação.

## Regra de go/no-go do launch

Se qualquer invariante falhar (threshold, replay, fail-closed, assinatura, persistência), o lançamento público é automaticamente **NO-GO**.

Se todos os invariantes passarem, o release é **GO** e pode ser tratado como o primeiro organismo público do MatVerse.

## Marca de registro

Registro de autoria/referência institucional vinculado ao ORCID: <https://orcid.org/0009-0008-2973-4047>.
