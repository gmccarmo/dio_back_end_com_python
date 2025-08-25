# 📌 Resumos Git

Este repositório contém um resumo com alguns dos principais comandos utilizados no **Git** via terminal, organizado em tabelas para facilitar a consulta.  

> ⚡ Observações importantes:  
> - `CTRL + L` → limpa o terminal.  
> - O **Git não reconhece diretórios vazios**. Para resolver, crie um arquivo dentro do diretório ou utilize um arquivo especial como `.gitkeep`.  
> - É recomendado criar um `.gitignore` para definir arquivos/pastas que devem ser ignorados pelo Git.  

---

## 📑 Índice
1. [Comandos de Diretório](#-comandos-de-diretório)  
2. [Configuração de Repositório](#-configuração-de-repositório)  
3. [Controle de Versões](#-controle-de-versões)  
4. [Branches](#-branches)  
5. [Repositório Remoto](#-repositório-remoto)  
6. [Reset e Reflog](#-reset-e-reflog)  
7. [Stash (Armazenar Alterações)](#-stash-armazenar-alterações)  

---

## 📂 Comandos de Diretório

| Comando | Descrição |
|---------|-----------|
| `mkdir nome_da_pasta` | Cria uma pasta no diretório atual. |
| `cd caminho_da_pasta` | Acessa a pasta indicada. |
| `rm -rf .git` | Remove a pasta `.git` e todo o histórico do repositório local (cuidado!). |

---

## ⚙️ Configuração de Repositório

| Comando | Descrição |
|---------|-----------|
| `git init` | Inicializa um repositório Git vazio no diretório atual. |
| `git clone URL` | Clona um repositório remoto do GitHub para o diretório local. |
| `git clone URL novo_nome` | Clona o repositório em uma pasta com o nome definido. |
| `git clone URL --branch branch --single-branch` | Clona apenas uma branch específica. |
| `git remote -v` | Lista os repositórios remotos vinculados. |
| `git remote add origin URL` | Vincula o repositório local a um repositório remoto. |

---

## 📌 Controle de Versões

| Comando | Descrição |
|---------|-----------|
| `git status` | Mostra o status do repositório (arquivos modificados, não rastreados etc.). |
| `git add .` | Adiciona todos os arquivos para a área de preparação (staging). |
| `git commit -m "mensagem"` | Cria um commit com a mensagem definida. |
| `git commit --amend -m "nova mensagem"` | Altera a mensagem do último commit. |
| `git reflog` | Mostra o histórico de referências (útil para recuperar commits). |

---

## 🌱 Branches

| Comando | Descrição |
|---------|-----------|
| `git branch` | Lista todas as branches locais. |
| `git branch -v` | Mostra o último commit de cada branch. |
| `git branch -M main` | Renomeia a branch atual para `main`. |
| `git branch -d nome_branch` | Exclui a branch especificada. |
| `git checkout -b nova_branch` | Cria e muda para uma nova branch. |
| `git checkout main` | Volta para a branch `main`. |
| `git merge nome_branch` | Mescla a branch especificada na branch atual. |

---

## 🌍 Repositório Remoto

| Comando | Descrição |
|---------|-----------|
| `git push -u origin main` | Envia os commits da branch local para o repositório remoto. |
| `git pull` | Baixa e mescla as alterações do repositório remoto. |
| `git fetch origin main` | Baixa as atualizações da branch remota sem aplicar. |
| `git diff main origin/main` | Mostra diferenças entre a branch local e a remota. |
| `git merge origin/main` | Aplica as atualizações baixadas da branch remota. |

---

## ♻️ Reset e Reflog

| Comando | Descrição |
|---------|-----------|
| `git reset --soft hash` | Volta para o commit indicado, mantendo os arquivos na **staging area**. |
| `git reset --mixed hash` | Volta para o commit indicado, mantendo arquivos modificados no diretório. |
| `git reset --hard hash` | Volta para o commit indicado e descarta todas as alterações. |

---

## 📦 Stash (Armazenar Alterações)

| Comando | Descrição |
|---------|-----------|
| `git stash` | Salva alterações atuais e limpa a área de trabalho. |
| `git stash list` | Lista todas as alterações armazenadas. |
| `git stash pop` | Recupera alterações armazenadas e remove da lista. |
| `git stash apply` | Recupera alterações armazenadas mas mantém na lista. |

---