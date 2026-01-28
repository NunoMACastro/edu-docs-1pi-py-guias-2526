# Guia Completo de Comandos Git (10º ao 12º Ano)

> **Objetivo:**  
> Ajudar alunos a compreender e aplicar os comandos essenciais do Git, do uso individual até à colaboração via GitHub.  
> Inclui teoria, exemplos práticos e observações para evitar erros comuns.

---

## 1. Conceitos Fundamentais

| Termo                  | Explicação                                                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Git**                | Sistema de controlo de versões — permite guardar o histórico de alterações do código.                      |
| **Repositório (repo)** | Diretoria que contém o código e o histórico de versões.                                                    |
| **Commit**             | Registo de alterações com uma mensagem descritiva.                                                         |
| **Branch**             | Linha de desenvolvimento paralela. Permite trabalhar sem mexer na principal.                               |
| **Merge**              | Combina o conteúdo de duas branches.                                                                       |
| **Remote (origin)**    | Repositório remoto, normalmente no GitHub.                                                                 |
| **Clone**              | Cópia local de um repositório remoto.                                                                      |
| **Staging Area**       | Zona intermédia onde ficam as alterações prontas para commit.                                              |
| **Pull Request**       | Pedido para integrar alterações de uma branch para outra, geralmente usado em colaboração.                 |
| **Fork**               | Cópia pessoal de um repositório remoto, permitindo contribuir sem afetar o original.                       |
| **.gitignore**         | Ficheiro que especifica quais ficheiros ou pastas o Git deve ignorar.                                      |
| **HEAD**               | Aponta para o commit atual onde estás a trabalhar.                                                         |
| **Pull**               | Atualiza o repositório local com alterações do remoto (pode fazer merge/rebase).                           |
| **Push**               | Envia commits locais para o repositório remoto.                                                            |
| **Fetch**              | Obtém atualizações do repositório remoto sem fazer merge automático.                                       |
| **SHA / Hash**         | Identificador único de um commit (sequência de letras e números).                                          |
| **Detached HEAD**      | Estado em que estás “num commit” mas **não** numa branch (útil para inspecionar, perigoso para trabalhar). |

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
| `git log --oneline` | Mostra histórico resumido (hash curta + mensagem).               |
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

> Nota: Hoje em dia existe `git switch` (mais “moderno”) e `git checkout` (mais antigo, mas ainda muito usado).  
> Podes usar qualquer um — o importante é perceber o que faz.

```bash
git branch nome-da-branch               # cria uma nova branch (não muda para ela)
git checkout nome-da-branch             # muda para a branch (forma antiga)
git checkout -b nova-branch             # cria e muda (forma antiga)

git switch nome-da-branch               # muda para a branch (forma moderna)
git switch -c nova-branch               # cria e muda (forma moderna)

git merge nome-da-branch                # junta a branch "nome-da-branch" na branch atual
git branch -d nome-da-branch            # apaga a branch local (se já foi merged)
git push origin --delete nome-da-branch # apaga a branch remota
```

> **Regra de ouro do merge:** o merge acontece **na branch onde estás**.  
> Se estás na `main` e fazes `git merge feature`, estás a juntar a `feature` na `main`.

---

## 7. Atualizar o Projeto

```bash
git pull                 # atualiza a branch atual com alterações do remoto (pode fazer merge automaticamente)
git fetch                # obtém alterações do remoto sem mexer no teu código
git merge origin/main    # junta ao teu código as alterações obtidas com fetch (exemplo para main)
```

---

## 8. Reverter, Voltar Atrás e Corrigir (IMPORTANTE)

Esta secção é das mais importantes porque existem **3 formas diferentes** de “voltar atrás”, e cada uma serve para coisas diferentes.

### 8.1) Desfazer alterações **ainda não commitadas**

#### Desfazer alterações num ficheiro (voltar ao último commit)

Forma moderna:

```bash
git restore caminho/do/ficheiro
```

Forma antiga (equivalente):

```bash
git checkout -- caminho/do/ficheiro
```

#### Tirar um ficheiro do staging (já tinhas feito `git add` mas afinal não queres)

```bash
git restore --staged caminho/do/ficheiro
```

Alternativa clássica:

```bash
git reset caminho/do/ficheiro
```

> Atenção: isto não apaga alterações do ficheiro; só o retira do staging.

---

### 8.2) Voltar a um commit antigo **só para ver / inspecionar** (não mexe no histórico)

```bash
git log --oneline
git checkout <hash_do_commit>
```

Ficas em **detached HEAD** (não estás numa branch). Para voltares à normalidade:

```bash
git checkout main
# ou (moderno) git switch main
```

Se quiseres trabalhar a partir desse commit, cria uma branch:

```bash
git checkout -b minha-branch <hash_do_commit>
# ou (moderno) git switch -c minha-branch <hash_do_commit>
```

---

### 8.3) Voltar a um commit antigo **mexendo no histórico** (RESET)

`git reset` move o ponteiro da branch para trás. Existem 3 níveis:

#### A) `--soft` (mantém as alterações no staging)

Usa quando queres “desfazer o commit” mas manter tudo pronto a commitar.

```bash
git reset --soft <hash_do_commit>
```

#### B) `--mixed` (default) — mantém as alterações no working directory, mas tira do staging

É o mais comum quando queres voltar atrás e depois escolher o que commitar.

```bash
git reset --mixed <hash_do_commit>
# ou simplesmente: git reset <hash_do_commit>
```

#### C) `--hard` (cuidado!) — apaga tudo e fica exatamente como nesse commit

Perdes alterações **não guardadas** depois desse commit.

```bash
git reset --hard <hash_do_commit>
```

> Dica de segurança antes de `--hard`:
>
> ```bash
> git status
> git stash -u
> ```

---

### 8.4) “Desfazer” um commit **sem reescrever histórico** (REVERT) — recomendado em trabalho de equipa

`git revert` **cria um novo commit** que anula as alterações de um commit anterior.

```bash
git revert <hash_do_commit> 
```

Isto é o mais seguro quando:

- já fizeste `push` para o GitHub;
- estás a trabalhar com outras pessoas na mesma branch.

#### Reverter vários commits (intervalo)

```bash
git revert <hash_mais_antigo>^..<hash_mais_recente>
```

---

### 8.5) Se já fizeste **push**: cuidado com `reset`

- Se fizeres `reset` numa branch que já está no GitHub, o teu histórico local fica diferente do remoto.
- Para “forçar” o remoto a aceitar, teria de ser um _force push_ (perigoso em equipa).

Se for mesmo necessário:

```bash
git push --force-with-lease
```

> **Regra prática para alunos:**  
> Se já está no GitHub e é uma branch partilhada → **usa `git revert`**.

---

### 8.6) Voltar atrás **só num ficheiro** para um estado antigo

Ver histórico daquele ficheiro:

```bash
git log --oneline -- caminho/do/ficheiro
```

Repor o ficheiro como estava num commit específico:

```bash
git restore --source <hash> -- caminho/do/ficheiro
```

Alternativa antiga:

```bash
git checkout <hash> -- caminho/do/ficheiro
```

Depois disso, guardas a correção com commit:

```bash
git add caminho/do/ficheiro
git commit -m "Repor ficheiro X para estado anterior"
```

---

### 8.7) “Socorro”: recuperar um commit que perdeste (RELOG / reflog)

Se fizeste `reset` e achas que “perdeste” commits, muitas vezes ainda dá para recuperar usando:

```bash
git reflog
```

O `reflog` mostra para onde o `HEAD` apontou recentemente. Depois podes voltar a um estado antigo com:

```bash
git reset --hard <hash_que_aparece_no_reflog>
```

> Isto é uma ferramenta de emergência. Vale ouro quando alguém faz asneira.

---

### 8.8) Voltar a um commit anterior — UI do VSCode

- Projeto inteiro: abre a Command Palette (Ctrl+Shift+P) → `Git: Checkout to...` → escolhe o commit.
- Ficheiro específico: no Explorer, seleciona o ficheiro → abre a view **Timeline** → escolhe um commit → **Restore**.
- Se quiseres manter o histórico, usa **Revert** (quando disponível) em vez de **Reset**.

---

## 9. Comparar

```bash
git diff                 # diferenças entre working directory e último commit
git diff --staged        # diferenças entre staging e último commit
git diff main..feature   # diferenças entre duas branches
```

---

## 10. Sincronização

```bash
git remote -v              # lista repositórios remotos
git remote add origin URL  # adiciona remoto para poderes fazer push/pull
git push origin main       # envia alterações para a branch main do remoto
git pull origin main       # puxa alterações da branch main do remoto
git fetch --prune          # remove referências a branches remotas que foram apagadas
```

---

## 11. Pull Requests

1. `git push origin feature/login`
2. Criar Pull Request no GitHub
3. Fazer merge e apagar branch

---

## 12. Ajuda

```bash
git help <comando>   # mostra ajuda sobre um comando específico
git status           # estado do repositório
git log --oneline    # histórico resumido
```

---

## 13. Fluxo Recomendado para Alunos

```bash
git switch -c ficha6
git add .
git commit -m "Resolução da Ficha 6"
git push origin ficha6
```

> Se ainda estiverem a usar `checkout`, isto é equivalente:
>
> ```bash
> git checkout -b ficha6
> ```
