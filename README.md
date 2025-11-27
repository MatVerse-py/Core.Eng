MatVerse-Core 2025 — IA Projetada
Sistema cognitivo antifrágil unificado.

## Solução de problemas de Git
Se ao tentar baixar o release aparecer a mensagem
`Provided git ref codex/prepare-release-v1.0.0-for-core.eng does not exist`,
execute as etapas a seguir:

1. Atualize os refs remotos para garantir que todos os branches e tags
   estejam visíveis localmente:
   ```bash
   git fetch --all --prune
   ```
2. Verifique se o ref está disponível no repositório remoto ou se houve
   alteração no nome:
   ```bash
   git branch -r | grep "codex/prepare-release"
   git tag -l | grep "prepare-release"
   ```
3. Caso o ref realmente não exista, confirme qual é o branch ou tag correto
   para o release e use esse identificador no clone/checkout, por exemplo:
   ```bash
   git checkout main
   ```

Esses passos ajudam a garantir que os comandos de release apontem para refs
válidos e evitam falhas ao preparar o pacote de lançamento.
