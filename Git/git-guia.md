# Guia Completo de Comandos Git (10º ao 12º Ano)

> **Objetivo:**  
> Ajudar alunos a compreender e aplicar os comandos essenciais do Git, do uso individual até a colaboração via GitHub.  
> Inclui teoria, exemplos práticos e observações para evitar erros comuns.

---

## 1. Conceitos Fundamentais

| Termo                  | Explicação                                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| **Git**                | Sistema de controlo de versões - permite guardar o histórico de alterações do código.                 |
| **Repositório (repo)** | Diretoria que contém o código e o histórico de versões.                                               |
| **Commit**             | Registo de alterações com uma mensagem descritiva.                                                    |
| **Branch**             | Linha de desenvolvimento paralela. Permite trabalhar em novas funcionalidades sem mexer na principal. |
| **Merge**              | Combina o conteúdo de duas branches.                                                                  |
| **Remote (origin)**    | Repositório remoto, normalmente no GitHub.                                                            |
| **Clone**              | Cópia local de um repositório remoto.                                                                 |
| **Staging Area**       | Zona intermédia onde ficam as alterações prontas para commit.                                         |
| **Pull Request**       | Pedido para integrar alterações de uma branch para outra, geralmente usado em colaboração.            |
| **Fork**               | Cópia pessoal de um repositório remoto, permitindo contribuir sem afetar o original.                  |
| **.gitignore**         | Ficheiro que especifica quais ficheiros ou pastas o Git deve ignorar.                                 |
| **HEAD**               | Aponta para o commit atual onde estás a trabalhar.                                                    |
| **Pull**               | Atualiza o repositório local com alterações do remoto.                                                |
| **Push**               | Envia commits locais para o repositório remoto.                                                       |
| **Fetch**              | Obtém atualizações do repositório remoto sem fazer merge automático.                                  |

---

## 2. Configuração Inicial

Antes de usar o Git pela primeira vez, identifica-te:

```bash
git config --global user.name "O Teu Nome"
git config --global user.email "teuemail@example.com"
```

Verifica:

```bash
git config --list
```

---

## 3. Criar ou Obter um Repositório

### Criar repositório local

```bash
git init
```

### Clonar repositório remoto

```bash
git clone https://github.com/utilizador/repositorio.git
```

---

## 4. Estado e Histórico

| Comando             | Explicação                                                       |
| ------------------- | ---------------------------------------------------------------- |
| `git status`        | Mostra ficheiros modificados, novos ou apagados.                 |
| `git log`           | Lista commits com autor, data e mensagem.                        |
| `git log --oneline` | Mostra histórico resumido.                                       |
| `git diff`          | Mostra diferenças entre ficheiros modificados e o último commit. |

---

## 5. Ciclo de Trabalho (add → commit → push)

```bash
git add .
git commit -m "Mensagem descritiva"
git push origin main
```

> O commit é local e deve sempre ter uma mensagem do que foi feito.
> O push envia as alterações para o repositório remoto.

---

## 6. Branches

```bash
git branch nome-da-branch # cria uma nova branch
git checkout nome-da-branch # muda para a branch
git checkout -b nova-branch # cria e muda para a nova branch
git merge nome-da-branch # faz merge da branch na atual. O merge é feito na branch onde estás. Ou seja, se estás na main e fazes git merge feature, vais juntar a feature na main.
git branch -d nome-da-branch # apaga a branch local
git push origin --delete nome-da-branch # apaga a branch remota
```

---

## 7. Atualizar o Projeto

```bash
git pull # atualiza com as últimas alterações do remoto e faz merge automático com a branch atual no repositório local
git fetch # obtém as últimas alterações do remoto sem fazer merge
git merge origin/main # faz merge das alterações obtidas com fetch
```

---

## 8. Reverter e Corrigir

```bash
git checkout -- nome_do_ficheiro # desfaz alterações não commitadas no ficheiro
git reset nome_do_ficheiro # remove ficheiro da staging area
git reset --soft HEAD~1 # desfaz o último commit, mantendo as alterações na staging area
git reset --hard <hash> # desfaz o repositório para o estado do commit especificado, perdendo todas as alterações posteriores
git revert <hash> # cria um novo commit que desfaz as alterações do commit especificado
```

---

## 9. Comparar

```bash
git diff # mostra diferenças entre ficheiros modificados e o último commit
git diff --staged # mostra diferenças entre ficheiros na staging area e o último commit
git diff main..feature # mostra diferenças entre duas branches
```

---

## 10. Sincronização

```bash
git remote -v # lista repositórios remotos
git remote add origin URL # adiciona repositório remoto para que possamos fazer push/pull
git push origin main # envia alterações para a branch main do remoto
git pull origin main # puxa alterações da branch main do remoto
git fetch --prune # remove referências a branches remotas que foram apagadas
```

---

## 11. Pull Requests

1. `git push origin feature/login`
2. Criar Pull Request no GitHub
3. Fazer merge e apagar branch

---

## 12. Ajuda

```bash
git help <comando> # mostra ajuda sobre um comando específico
git status # mostra o estado do repositório
git log --oneline # mostra o histórico resumido
```

---

## 13. Fluxo Recomendado para Alunos

```bash
git checkout -b ficha6
git add .
git commit -m "Resolução da Ficha 6"
git push origin ficha6
```
