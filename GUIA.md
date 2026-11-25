# Guia de configuração e apresentação

1. Confirme com o professor a entrega estática e registre a combinação na planilha da turma.
2. Instale Python 3.12, Git e VS Code. Abra a pasta extraída e siga o README.
3. Crie um repositório público vazio em https://github.com/new chamado api-produtos-cicd.
4. No terminal, execute (troque SEU-USUARIO):

```sh
git init
git add .
git commit -m "Estrutura inicial da API"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/api-produtos-cicd.git
git push -u origin main
```

5. Settings > Pages > Source > GitHub Actions. Se necessário, execute novamente o workflow na aba Actions.
6. Após a primeira execução, Settings > Branches > Add branch protection rule: padrão main; Require a pull request before merging; Require status checks to pass before merging (build-test); Do not allow bypassing the above settings. Não exija o job deploy no PR. Recomenda-se uma aprovação de outro integrante e branches atualizadas.
7. Settings > Collaborators: convide os integrantes. Cada um deve clonar o repositório e criar sua própria branch, editar um arquivo, fazer commit, push e abrir PR para main.

```sh
git checkout main
git pull origin main
git checkout -b feature/minha-alteracao
# Edite os arquivos antes de continuar
git add .
git commit -m "Minha contribuicao"
git push -u origin feature/minha-alteracao
```

8. Demonstração: crie uma branch demo/teste-falhando a partir da main atualizada. Altere o assert de status 201 para 500 em test_cadastrar_produto. Faça commit, push e abra PR. Mostre a falha e o merge bloqueado. Corrija para 201 e acrescente `assert resposta.json()['quantidade'] == 10`. Faça commit e push. Mostre o sucesso, solicite a revisão se exigida e faça merge. Confira build-test e deploy em Actions. Prepare também um PR aprovado separado, com mudança simples na documentação.
9. Apresentação (15 minutos): 1 min introdução; 2 min tecnologias; 2 min API; 2 min YAML; 3 min PR falhando; 4 min correção, merge e entrega; 1 min conclusão. Tenha execuções anteriores disponíveis caso haja demora.

## Checklist (marcar após comprovação real)

- [ ] Grupo e combinação registrados na planilha.
- [ ] Repositório público criado.
- [ ] Build e pelo menos 3 testes executados.
- [ ] Build e testes no PR.
- [ ] Build, testes e entrega no merge.
- [ ] Main protegida e pipeline obrigatório.
- [ ] Cada integrante com PR próprio.
- [ ] PRs de demonstração com sucesso e falha preparados.
- [ ] Apresentação ensaiada em até 15 minutos.
