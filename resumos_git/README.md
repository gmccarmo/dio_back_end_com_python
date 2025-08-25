
# Resumos Git

Alguns dos comandos utilizados no terminal do Git
```
CTRL + L limpa o terminal

Obs.: o git não reconhece diretórios vazios, será necessário incluir algum arquivo no diretório para realizar o commit ou então criar um arquivo .gitkeep, além de realizar a criação de um arquivo .gitignore para incluir tudo o que deverá ser ignorado do diretório raiz

```


| Comando Terminal      | Descrição                                                                                        |
|:----------------------|:-------------------------------------------------------------------------------------------------|
| $ mkdir nome_da_pasta | Cria uma pasta no diretório que estiver                                                          |
| $ cd caminho_da_pasta | Entra na pasta do caminho digitado                                                               |
| $ git init            | Transforma o diretório no qual está em um repositório Git,                                       |
|        ''             | retornando que iniciou um repositório git vazio no caminho C:/exemplo/repo-local/.git/           |
| $ git clone https://github.com/seu_usuario/repositorio_github.git | Irá clonar o repositório do GitHub no repositório local a partir da url inserida. Para exemplo, seria usado a pasta C:/exemplo para fazer o git clone                                |
| $ git clone https://github.com/seu_usuario/repositorio_github.git repo-clonado | Com um nome após o comando do git clone com a url, quando for realizada a ação de clonagem, será criado o diretório repo-clonado no diretório no qual está e clonar a url neste mesmo diretório apontado no comando                                                                                        |
| $ git remote -v       | Verifica quais repositórios remotos que estão vinculados com o repositório local                 |
| $ git remote add origin https://github.com/seu_usuario/repositorio_github.git | Configura o vinculo com um repositório do GitHub a partir do link inserido no comando. Importante o repositório no GitHub ja ter um readme.md                                 |
| $ git clone URL --branch feature-1 --single-branch | Serve para pegar apenas uma branch do diretório do GitHub, caso não seja selecionada nenhuma branch, apenas a principal será clonada                                                                |
| $ git status          | Mostra o status da arvore de trabalho e da area de preparação                                    |
| $ git commit -m"commit inicial" | Serve para fazer uma commit do seu diretório para o git junto com uma mensagem         |
| $ git add .           | Adiciona todos os arquivos que não estão rastreáveis na area de preparação para o commit         |
| $ rm -rf .git         | Serve para apagar a pasta .git e todo o seu conteúdo forçadamente para remover um possível init no diretório errado                                                                                                           |
| $ git commit --amend -m"" | Sobreescreve a mensagem do ultimo commit realizado, sem o argumento -m, irá abrir o edit VIM para fazer a edição                                                                                                             |
| $ git reset --soft hash_do_commit | Pega os arquivos que estavam nos commits posteriores ao indicado pela hash e os adiciona na área de preparação                                                                                                         |
| $ git reset --mixed hash_do_commit | Comportamento padrão do git reset podendo ser utilizado sem o argumento --mixed, diferente do soft, ele pega os arquivos posteriores ao hash indicado e os adiciona na arvore de trabalho, sendo necessário envia-los para a área de preparação                                                                                                              |
| $ git reset --hard hash_do_commit | Ignora os arquivos que foram criados/editos após o hash indicado e limpa a arvore de trabalho, deixando-a limpa                                                                                                           |
| $ git reflog                      | Log com o histórico completo de todas as alterações realizadas                       |
| $ git remote add origin url_repositorio_github | Realizada a conexão com o repositório do GitHub                         |
| $ git branch -M main              | Força a renomeação da branch para main, caso esteja na branch master                 |
| $ git push -u origin main         | O push faz os envios do repositório local para o remoto, o -u é uma abreviação para set upstream, vai estar dizendo para configurar a branch main que estará configurada no repositório como origin como a branch upstream da main do repositório local                                                                                               |
| $ git checkout -b teste           | Altera a branch de main para teste para seguir com alterações sem alterar a main     |
| $ git checkout main               | Retorna para a branch main, apagando todas as alterações realizadas na branch criada |
| $ git branch -v                   | Mostra o ultimo commit de cada branch                                                |
| $ git merge teste                 | Mescla a branch listada no comando junto com a branch main                           |
| $ git branch                      | Lista as branch do repositório                                                       |
| $ git branch -d nome_branch       | Deleta a branch listada no comando                                                   |
| $ git pull                        | Puxa as atualizações no repositório do GitHub para o repositório local               |
|                                   comandos que fazem parte do git pull mas separados para realizar as validações do que foi baixado do que está armazenado localmente|
| $ git fetch origin main           | Baixa somente as atualizações do repositório do GitHub sem fazer alterações no repositório local|
| $ git diff main origin/main       | Mostra as diferenças entre o repositório main local (na nossa máquina) e o repositório que está no GitHub (origem, origin/main)|
| $ git merge origin/main           | Mescla as atualizações baixadas da origin/main no repositório local                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| $ git clone url_repositorio_github --branch teste --single-branch | Comando utilizado para repositórios que possuem mais de uma branch, neste exemplo estamos indicando que queremos clonar a branch teste deste repositório e finalizando com o single branch para indicar que é somente esta branch. Caso não indique qual branch irá clonar, sera feita a clonagem somente da branch principal |
| $ git stash | Arquiva a atualização do repositório que foi realizada                                                        |
| $ git stash list | Lista todas as alterações que foram arquivadas                                                           |
| $ git stash pop  | Trás as alterações arquivadas e as remove da lista                                                       |
| $ git stash apply| Trás as alterações arquivadas e mantém na listagem                                                       |









