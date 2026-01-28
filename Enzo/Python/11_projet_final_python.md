# Projet final (10e PI) — Jeu de questions (Quiz) en Python

**Durée :** 2 à 3 semaines 
**Groupes :** 3 étudiants 
**Type :** Application console (terminal)

---

## 1) Contexte et objectif

Vous développerez un **jeu de questions** (un quiz) en Python, exécuté dans le terminal.

L'objectif du projet n'est pas seulement de « le faire fonctionner ». C'est la formation qui coûte le plus cher au début :

- passer d'un **énoncé** à un **plan**
- concevoir une **structure de données** cohérente
- diviser le problème en **fonctions** et **modules**
- valider les entrées et réaliser le programme **robuste**

---

## 2) Ce que vous allez construire (aperçu)

Une application avec :

- un **menu**
- un mode **jeu** (répondez aux questions et marquez des points)
- un **score simple système**
- lecture des questions à partir d'un fichier **`perguntas.json`**

> Le programme doit être « convivial » sur le terminal : messages clairs, options numérotées, validation des entrées et résultats bien présentés.

---

## 3) Règles et restrictions

### Obligatoire

- Python 3.x
- Aucune bibliothèque externe (uniquement la bibliothèque standard : `json`, `random`, `time`, etc.)
- Utiliser des **fonctions** (il ne peut pas s'agir d'un fichier géant avec tout dans `main`)
- Valider les entrées de l'utilisateur (ne supposez pas que l'utilisateur écrit "well")
- Lire les questions à partir d'un fichier JSON

### Autorisé / recommandé

- Utiliser des listes et des dictionnaires comme une "base de données en mémoire"
- Organiser le projet en **modules** (plus d'un fichier `.py`)
- Enregistrer les partitions dans un fichier (par exemple : `pontuacoes.json`) pour conserver l'historique

---

## 4) Fichier de questions (JSON)

Vous devez créer un fichier JSON avec des questions pour le jeu. Une fois que vous avez une structure pour le fichier, vous pouvez demander à un agent IA (par exemple ChatGPT) de générer automatiquement des questions.

### Structure JSON (schéma attendu)

Le fichier aura une **liste de questions**, et chaque question devra stocker des champs similaires à ceux-ci :

- `id` (int ou str)
- `pergunta` (str)
- `opcoes` (liste de chaînes)
- `resposta` (int **ou** str — selon le fichier fourni)
- `categoria` (str) - Le cas échéant
- `dificuldade` (str: `"facil"`, `"media"`, `"dificil"`) — facultatif
- `explicacao` (str) — facultatif (à afficher à la fin)

**Remarque importante :** Le champ `resposta` peut être :

- un **index** (par exemple `1` signifie l'option n°2, si vous utilisez l'index 0)
- ou le **texte** de l'option correcte

---

## 5) Caractéristiques

### 5.1 — MVP (obligatoire)

Ces fonctionnalités doivent exister et fonctionner correctement :

1. **Charger les questions**

- Lire `perguntas.json`
- Valider les bases : ça existe, ce n'est pas vide, chaque question a `pergunta` et `opcoes`

2. **Menu principal**

- (1) Jouer
- (2) Règles / aide
- (3) Quitter 
 (Vous pouvez ajouter plus d'options, mais celles-ci sont obligatoires.)

3. **Mode de jeu**

- Choisissez **N questions aléatoires** (par exemple : 5, 10 ou configurable)
- Pour chaque question :
 - afficher le libellé et les options numérotées
 - demander une réponse à l'utilisateur
 - valider la saisie (ne peut pas planter avec des lettres, des blancs, des chiffres en dehors de l'intervalle)
 - dites si vous avez obtenu c'est vrai/faux
 - score de mise à jour

4. **Résumé final**

- Note totale
- Nombre de bonnes/mauvaises réponses
- Pourcentage de bonnes réponses

5. **Relecture**

- À la fin, vous permet de rejouer sans redémarrer le programme

---

### 5.2 — Niveau 2

Choisissez au moins **2** de ces améliorations :

A) **Catégories et/ou difficulté**

- Avant de jouer, autorisez le choix de la catégorie et/ou de la difficulté
- Si l'utilisateur choisit « tout », le jeu utilise tout

B) **Évitez les répétitions**

- Assurez-vous que dans une session les questions **ne se répètent pas**
- (Extra) évitez les répétitions dans plusieurs sessions alors qu'il y a des questions new

C) **Scores enregistrés**

- Demander un nom/surnom au début
- Sauvegarder le résultat dans un fichier (ex. : `pontuacoes.json`)
- Dans le menu, avoir une option pour voir le **Top 10**

D) **Explication**

- S'il y a `explicacao` dans la question, affichez-le à la fin (ou après avoir répondu)

---

### 5.3 — Niveau 3 (bonus)

Choisissez **1** si vous avez déjà le MVP + Niveau 2 solides :

A) **Mode contre-la-montre**

- Le joueur a Les questions faciles valent 1 point, moyennes 2, difficiles 3

C) **Mode « Championnat »**

- Au meilleur des 3 tours, somme totale et vainqueur (s'il y en a 2 en alternance joueurs)

---

## 6) Planification initiale (obligatoire avant la programmation)

Avant d'écrire du « vrai » code, le groupe doit livrer un fichier appelé :

- **`PLANIFICACAO.md`**

Ce fichier est valable pour le grade et sert à débloquer le projet.

### Ce que `PLANIFICACAO.md` doit avoir

#### 1) Modèle de données (très important)

- Comment ils représenteront :
 - les questions en mémoire (liste des dictionnaires ?)
 - la ponctuation (entière ? dictionnaire avec les bons/les mauvais ?)
 - les ponctuations enregistrées (liste des dictionnaires dans `pontuacoes.json`?)
- Inclure **2 exemples réels** (petits) des structures.

#### 2) Entrées / Traitement / Sorties

Une table ou une liste avec :

- entrées (ce que l'utilisateur écrit / ce qui vient du JSON)
- traitement (ce que le programme calcule/décide)
- sorties (ce qu'il affiche dans le terminal / ce qu'il enregistre dans un fichier)

#### 3) Liste des fonctions (avec responsabilités)

Exemples de ce type :

- `carregar_perguntas(...)` — lit JSON et renvoie la liste
- `mostrar_menu(...)` — imprime les options et renvoie un choix valide
- `fazer_pergunta(...)` — affiche la question, demande la réponse, renvoie si elle est correcte
- `jogar(...)` — cycle de jeu principal, renvoie le résultat final
- `guardar_pontuacao(...)` — écrit dans le fichier de score

(Les noms et la division sont décidés par vous — mais vous devez justifier.)

#### 4) Déroulement du programme

Un organigramme simple (peut être sous forme de texte ou de diagramme) ou numéroté étapes qui expliquent :

- que se passe-t-il du début à la fin
- comment le menu est lié au jeu, comment le jeu se termine, etc.
- comment les entrées invalides sont traitées
- comment choisir de rejouer ou de quitter

#### 5) Structure de fichier/module (à décider par vous)

Là Il n’y a pas de « bonne » structure. Mais c'est obligatoire :

- utiliser **plus d'1 fichier `.py`**
- justifier la division : ce qu'il y a dans chaque fichier et pourquoi

#### 6) Plan de test (manuel)

Créer une liste de tests pour le type :

- "Si vous écrivez 'a' au lieu d'un nombre, le programme ne plante pas et demande à nouveau"
- "Si vous choisissez une option en dehors de la plage, il donne une erreur et se répète"
- ...

Écrivez au moins 8 tests différents qui couvrent les principales fonctionnalités et validations.

---

## 7) Organisation du travail

### Phase 1

- Livrer `PLANIFICACAO.md`
- Réaliser un prototype de menu + charger JSON

### Phase 2

- Implémenter le mode de jeu complet (MVP)
- Valider les entrées et améliorer les messages
- Commencer le niveau 2 (catégories/scores/etc.)

### Phase 3

- Terminer le niveau 2
- Exécuter les tests, corriger bugs
- Améliorer la présentation du terminal
- (Facultatif) 1 Fonctionnalité de niveau 3

---

## 8) Critères d'évaluation

- **10%** Planification (`PLANIFICACAO.md`) bien faite et cohérente
- **35%** MVP complet et fonctionnel
- **25%** Qualité du code : fonctions, organisation par modules, lisibilité
- **10%** Robustesse : validations, erreurs gérées sans crashs
- **10%** Niveau 2 et polissage
- **10%** Niveau 3 ou extras intéressants

---

## 9) Livraison finale

Livrer un dossier (ou zip) avec :

- `.py` fichiers du projet
- `perguntas.json` (tel que fourni, sans modifications « au hasard »)
- (le cas échéant) `pontuacoes.json`
- `PLANIFICACAO.md`
- `README.md` petit avec :
 - comment exécuter
 - fonctionnalités implémentées
 - extras réalisations

---

## 10) Notes finales (conseils pratiques)

- Commencez par le **flow** (menu → play → résumé). Ensuite seulement, polissez.
- S'ils sont bloqués, revenez au modèle de données : « comment vais-je sauvegarder ça ? »
- Faites fonctionner le programme avec 3 questions, puis adaptez-le à l'ensemble du fichier.
- Enregistrez toujours une version qui « fonctionne » avant d'ajouter des extras.

---

### Point de contrôle rapide (pour l'enseignant doit valider)

À la fin de la phase 1, le groupe doit être capable de :

- ouvrir le JSON et montrer combien de questions il a chargé
- avoir un menu qui accepte des choix valides
- être capable d'afficher une question et de lire une réponse

---

### Livraison finale du projet

Tous les dossiers et documents de planification doivent être livrés via Guithub à la date définie par l'enseignant.
