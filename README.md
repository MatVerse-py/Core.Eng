MatVerse-Core 2025 — IA Projetada
Sistema cognitivo antifrágil unificado.

## Solução de problemas de Git
Se ao tentar baixar o release aparecer uma mensagem como:

- `Provided git ref codex/prepare-release-v1.0.0-for-core.eng does not exist`
- `fatal: couldn't find remote ref codex/add-documentation-for-modules`

o ambiente está tentando acessar uma referência (branch/tag) que não existe
no repositório remoto. Execute as etapas a seguir:

1. Atualize os refs remotos para garantir que todos os branches e tags
   estejam visíveis localmente:
   ```bash
   git fetch --all --prune
   ```
2. Verifique se o ref está disponível no repositório remoto ou se houve
   alteração no nome:
   ```bash
   git ls-remote --heads origin | grep "codex/"
   git ls-remote --tags origin | grep "prepare-release"
   ```
3. Se o branch foi criado localmente e ainda não está no GitHub, publique-o:
   ```bash
   git push -u origin codex/add-documentation-for-modules
   ```
4. Caso o ref realmente não exista, confirme qual é o branch ou tag correto
   para o release e use esse identificador no clone/checkout, por exemplo:
   ```bash
   git checkout main
   ```

Esses passos ajudam a garantir que os comandos de release apontem para refs
válidos e evitam falhas ao preparar o pacote de lançamento.
