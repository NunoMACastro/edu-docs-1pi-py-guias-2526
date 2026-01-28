# Guide complet des commandes Git (10e à 12e année)

> **Objectif :** 
> Aider les étudiants à comprendre et à appliquer les commandes essentielles de Git, de l'utilisation individuelle à la collaboration via GitHub.  
> Comprend de la théorie, des exemples pratiques et des observations pour éviter les erreurs courantes.

---

## 1. Concepts fondamentaux

| Terme | Explication |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Git** | Système de contrôle de version — vous permet de sauvegarder l’historique des modifications de code.                      |
| **Dépôt (dépôt)** | Répertoire contenant le code et l'historique des versions.                                                    |
| **S'engager** | Journal des modifications avec un message descriptif.                                                         |
| **Branche** | Ligne de développement parallèle. Permet de travailler sans toucher au principal.                               |
| **Fusionner** | Combine le contenu de deux branches.                                                                       |
| **À distance (origine)** | Dépôt distant, généralement sur GitHub.                                                                 |
| **Cloner** | Copie locale d'un référentiel distant.                                                                      |
| **Zone de préparation** | Zone intermédiaire où les modifications sont prêtes à être validées.                                              |
| **Demande de tirage** | Demande d'intégration des modificationsd'une branche à l'autre, souvent utilisées en collaboration.                 |
| **Fourchette** | Copie personnelle d'un référentiel distant, vous permettant de contribuer sans affecter l'original.                       |
| **.gitignore** | Fichier qui spécifie les fichiers ou dossiers que Git doit ignorer.                                      |
| **TÊTE** | Pointez sur le commit actuel sur lequel vous travaillez.                                                         |
| **Tirez** | Met à jour le référentiel local avec les modifications apportées par le distant (peut fusionner/rebase).                           |
| **Pousser** | Pousse les validations locales vers le référentiel distant.                                                            |
| **Récupérer** | Obtient les mises à jour du référentiel distant sans fusion automatique.                                       |
| **SHA / Hachage** | Identifiant unique d'un commit (séquence de lettres et de chiffres).                                          |
| **TÊTE détachée** | Indiquez où vous êtes « dans un commit » mais **pas** dans une branche (utile à inspecter, dangereux à travailler). |

---

## 2. Configuration initiale

Avant d'utiliser Git pour la première fois, identifiez-vous :

```bash
git config --global user.name "O Teu Nome"
git config --global user.email "teuemail@example.com"
```

Vérifiez :

```bash
git config --list
```

---

## 3. Créer ou obtenir un référentiel

### Créer un référentiel local

```bash
git init
```

### Cloner le référentiel distant

```bash
git clone https://github.com/utilizador/repositorio.git
```

---

## 4. Statut et historique

| Commande | Explication |
| ------------------- | ---------------------------------------------------------------- |
| `git status` | Affiche les fichiers modifiés, nouveaux ou supprimés.                 |
| `git log` | Liste des commits avec auteur, date et message.                        |
| `git log --oneline` | Affiche l'historique récapitulatif (hachage court + message).               |
| `git diff` | Affiche les différences entre les fichiers modifiés et le dernier commit. |

---

## 5. Cycle de travail (ajouter → valider → pousser)

```bash
git add .
git commit -m "Mensagem descritiva"
git push origin main
```

> Le commit est local et doit toujours avoir un message sur ce qui a été fait.  
> Le push envoie les modifications au référentiel distant.

---

## 6. Branches

> Remarque : il existe aujourd'hui `git switch` (plus « moderne ») et `git checkout` (plus ancien, mais toujours largement utilisé).  
> Vous pouvez utiliser l'un ou l'autre — l'important est de comprendre ce qu'il fait.

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

> **Règle d'or de la fusion :** la fusion se produit **dans la succursale où vous vous trouvez**.  
> Si vous êtes à `main` et faites `git merge feature`, vous rejoignez `feature` à `main`.

---

## 7. Mettre à jour le projet

```bash
git pull                 # atualiza a branch atual com alterações do remoto (pode fazer merge automaticamente)
git fetch                # obtém alterações do remoto sem mexer no teu código
git merge origin/main    # junta ao teu código as alterações obtidas com fetch (exemplo para main)
```

---

## 8. Revenir, revenir en arrière et corriger (IMPORTANT)

Cette section est l'une des plus importantes car il existe **3 façons différentes** de « revenir en arrière », et chacune est utilisée pour des choses différentes.

### 8.1) Annuler les modifications **pas encore commit**

#### Annuler les modifications apportées à un fichier (retour au dernier commit)

Manière moderne :

```bash
git restore caminho/do/ficheiro
```

Ancienne forme (équivalent) :

```bash
git checkout -- caminho/do/ficheiro
```

#### Supprimer un fichier du staging (vous aviez déjà fait `git add` mais vous ne souhaitez pas)

```bash
git restore --staged caminho/do/ficheiro
```

Alternative classique :

```bash
git reset caminho/do/ficheiro
```

> Attention : cela ne supprime pas les modifications apportées au fichier ; donc le retrait de la mise en scène.

---

### 8.2) Voltar a um commit antigo **só para ver / inspecionar** (não mexe no histórico)

```bash
git log --oneline
git checkout <hash_do_commit>
```

Vous êtes en **HEAD détachée** (vous n'êtes pas en succursale). Pour revenir à la normale :

```bash
git checkout main
# ou (moderno) git switch main
```

Si vous souhaitez travailler à partir de ce commit, créez une branche :

```bash
git checkout -b minha-branch <hash_do_commit>
# ou (moderno) git switch -c minha-branch <hash_do_commit>
```

---

### 8.3) Revenir à un ancien commit **toucher l'historique** (RESET)

`git reset` déplace le pointeur de branche vers l'arrière. Il y a 3 niveaux :

#### A) `--soft` (conserve les modifications dans le staging)

À utiliser lorsque vous souhaitez « annuler la validation » mais garder tout prêt à être validé.

```bash
git reset --soft <hash_do_commit>
```

#### B) `--mixed` (par défaut) — conserve les modifications dans le répertoire de travail, mais les supprime de la préparation

C'est le plus courant lorsque vous souhaitez revenir en arrière et ensuite choisir quoi valider.

```bash
git reset --mixed <hash_do_commit>
# ou simplesmente: git reset <hash_do_commit>
```

#### C) `--hard` (attention !) — supprime tout et reste exactement comme dans ce commit

Vous perdez les modifications **non enregistrées** après ce commit.

```bash
git reset --hard <hash_do_commit>
```

> Conseil de sécurité avant `--hard` :
>
>```bash
> git status
> git stash -u
> ```

---

### 8.4) « Annuler » un commit **sans réécrire l'historique** (REVERT) — recommandé dans le travail d'équipe

`git revert` **crée un nouveau commit** qui annule les modifications d'un commit précédent.

```bash
git revert <hash_do_commit> 
```

C'est plus sûr lorsque :

- vous avez déjà fait `push` pour GitHub ;
- vous travaillez avec d'autres personnes sur la même branche.

#### Annulation de plusieurs commits (plage)

```bash
git revert <hash_mais_antigo>^..<hash_mais_recente>
```

---

### 8.5) Si vous avez déjà fait **push** : soyez prudent avec `reset`

- Si vous faites `reset` sur une branche qui est déjà sur GitHub, votre historique local sera différent de celui distant.
- Pour « forcer » la télécommande à acceptez, il faudrait être un _force push_ (dangereux en équipe).

Si c'est vraiment nécessaire :

```bash
git push --force-with-lease
```

> **Règle générale pour les étudiants :** 
> Si c'est déjà sur GitHub et qu'il s'agit d'une branche partagée → **utilisez `git revert`**.

---

### 8.6) Revenir **dans un seul fichier** à un état old

Voir l'historique de ce fichier :

```bash
git log --oneline -- caminho/do/ficheiro
```

Restaurez le fichier tel qu'il était dans un commit spécifique :

```bash
git restore --source <hash> -- caminho/do/ficheiro
```

Ancienne alternative :

```bash
git checkout <hash> -- caminho/do/ficheiro
```

Après cela, validez la correction :

```bash
git add caminho/do/ficheiro
git commit -m "Repor ficheiro X para estado anterior"
```

---

### 8.7) « Aide » : récupérer un commit que vous avez perdu (RELOG / reflog)

Si vous avez fait `reset` et pensez avoir « perdu » des commits, vous pouvez souvent encore récupérer en utilisant :

```bash
git reflog
```

`reflog` indique où `HEAD` a récemment pointé. Vous pouvez alors revenir à un ancien état avec :

```bash
git reset --hard <hash_que_aparece_no_reflog>
```

> Ceci est un outil d'urgence. Cela vaut son pesant d'or quand quelqu'un se trompe.

---

### 8.8) Revenir à un commit précédent — VSCode UI

- Projet entier : ouvrez la palette de commandes (Ctrl+Shift+P) → `Git: Checkout to...` → choisissez le commit.
- Fichier spécifique : dans l'Explorateur, sélectionnez le fichier → ouvrez la vue **Timeline** → choisissez un commit → **Restaurer**.
- Si vous souhaitez conserver l'historique, utilisez **Revert** (si disponible) au lieu de **Reset**.

---

## 9. Comparez

```bash
git diff                 # diferenças entre working directory e último commit
git diff --staged        # diferenças entre staging e último commit
git diff main..feature   # diferenças entre duas branches
```

---

## 10. Synchronisation

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
2. Créer une Pull Request sur GitHub
3. Fusionner et supprimer une branche

---

## 12. Aide

```bash
git help <comando>   # mostra ajuda sobre um comando específico
git status           # estado do repositório
git log --oneline    # histórico resumido
```

---

## 13. Déroulement recommandé pour les étudiants

```bash
git switch -c ficha6
git add .
git commit -m "Resolução da Ficha 6"
git push origin ficha6
```

> S'ils utilisent toujours `checkout`, cela équivaut à :
>
>```bash
> git checkout -b ficha6
> ```
