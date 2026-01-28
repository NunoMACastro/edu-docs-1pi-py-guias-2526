# Python · 10e année (Programmeur informatique)

> Ce README décrit uniquement le dossier `Python`. Pour un aperçu du référentiel, voir [README.md](../README.md) à la racine.

Matériels de support au format **Markdown** pour l'introduction à la programmation en Python, conçus pour les **étudiants de 10e année - Cours de technicien en programmation informatique professionnelle**.

Le but de ce dossier est d'avoir un ensemble de **notes structurées + exercices progressifs**, que les étudiants peuvent utiliser comme :

- fiche de référence pendant les cours;
- matériel d'étude pour les tests;
- base pour les petits projets.

Chaque dossier se concentre sur une série de thèmes et se termine par:

- une section d'**Exercices** (10 à 12 exercices, du plus simple au plus difficile);
- une section **Changelog**, pour enregistrer les modifications.

**Index**

- [Structure du référentiel](#structure-du-referentiel)
- [`00_formulaire_support.md`](#00formularioapoiomd)
- [`00_exercices_de_preparation.md`](#00exerciciosdepreparacaomd)
- [`01_introduction_variables_types_strings_io.md`](#01introducaovariaveistiposstringsiomd)
- [`02_operateurs_et_controle_de_flux_if_boucles.md`](#02operadoresecontrolodefluxoifciclosmd)
- [`03_listes_dictionnaires_structures_imbriquees.md`](#03listasdicionariosestruturasaninhadasmd)
- [`04_fonctions_du_basique_au_avance.md`](#04funcoesdobasicoaoavancadomd)
- [`05_algorithmes_et_modeles_de_programmation.md`](#05algoritmosepadroesdeprogramacaomd)
- [`06_decoupage_list_comprehensions.md`](#06slicinglistcomprehensionsmd)
- [`07_fichiers_texte_json_csv.md`](#07ficheirostextojsoncsvmd)
- [`08_exceptions_et_traitement_des_erreurs.md`](#08excecoesetratamentodeerrosmd)
- [`09_modules_et_organisation_de_projets.md`](#09moduloseorganizacaodeprojetosmd)
- [`10_structures_et_algorithmes_classiques.md`](#10estruturasealgoritmosclassicosmd)
- [`11_projet_final_python.md`](#11projetofinalpythonmd)
- [Comment utiliser ces documents](#comment-utiliser-ces-documents)
- [Prérequis et travail sur l'environnement](#prerequis-et-travail-sur-lenvironnement)

---

## Structure du référentiel

```text
.
├── 00_formulaire_support.md
├── 00_exercices_de_preparation.md
├── 01_introduction_variables_types_strings_io.md
├── 02_operateurs_et_controle_de_flux_if_boucles.md
├── 03_listes_dictionnaires_structures_imbriquees.md
├── 04_fonctions_du_basique_au_avance.md
├── 05_algorithmes_et_modeles_de_programmation.md
├── 06_decoupage_list_comprehensions.md
├── 07_fichiers_texte_json_csv.md
├── 08_exceptions_et_traitement_des_erreurs.md
├── 09_modules_et_organisation_de_projets.md
├── 10_structures_et_algorithmes_classiques.md
├── 11_projet_final_python.md
└── README.md
```

### `00_formulaire_support.md`

[Afficher le fichier](./00_formulaire_support.md)

**Objectif :** 
Servir de feuille de référence rapide pour les tests, avec de courts exemples et des rappels de syntaxe essentiels.

Principal contenu :

- entrées/sorties, conversions et opérateurs;
- conditions, cycles et modèles fréquents;
- listes, dictionnaires et structures imbriquées;
- fonctions, découpages/compréhensions et fichiers.

---

### `00_exercices_de_preparation.md`

[Voir le fichier](./00_exercices_de_preparation.md)

**Objectif :** 
Préparer les étudiants aux évaluations, à travers des exercices impliquant les concepts de base de Python

Contenu principal :

- revue des fonctions (définition, paramètres, retour, \*args/\*\*kwargs);
- lecture et écriture de fichiers JSON;

---

### `01_introduction_variables_types_strings_io.md`

[Voir fichier](./01_introduction_variables_types_strings_io.md)

**Objectif :** à donner le premier contact avec Python et l'idée de « programme ».

Contenu principal :

- ce qu'est un programme et comment Python exécute le code ;
- variables et types de base : `int`, `float`, `str`, `bool`, `None`;
- conventions de dénomination (`snake_case`, majuscules pour les constantes);
- opérations de base avec des nombres et chaînes ;
- méthodes de chaînes les plus utilisées (`lower`, `upper`, `strip`, `replace`, `split`, `join`, etc.);
- entrée et sortie :
 - `print` (y compris _f-strings_);
 - `input` et type conversion (`int`, `float`);
- notions de commentaire et de lecture de code.

Comprend des exemples très simples et des exercices initiaux axés sur :

- déclaration de variables;
- petits comptes;
- manipulation de chaînes;
- utilisation de `input`/`print`.

---

### `02_operateurs_et_controle_de_flux_if_boucles.md`

[Voir fichier](./02_operateurs_et_controle_de_flux_if_boucles.md)

**Objectif :** introduire le « moteur » de la logique de programmation : **opérateurs**, **décisions** et **répétitions**.

Contenu principal :

- opérateurs arithmétiques : `+`, `-`, `*`, `/`, `//`, `%`, `**`
 - différence entre `/` (division réelle) et `//` (division entière) ;
 - exemples avec reste (`%`) et puissance (`**`);
- opérateurs de comparaison : `==`, `!=`, `>`, `>=`, `<`, `<=`
 - chaîne de comparaison : `1 < x <= 10`;
- opérateurs logiques : `and`, `or`, `not`
 - tables de vérité simples;
 - idée intuitive du _court-circuit_;
- `in` / `not in` (chaînes, listes, dictionnaires) et `is` / `is not` (surtout avec `None`);
- attributions composées : `+=`, `-=`, `*=`, etc.;
- **vérité** : ce qui compte comme `False` (`0`, `0.0`, `""`, `[]`, `{}`, `None`);
- structures de sélection :
 - `if`, `elif`, `else`;
 - exemples avec classification par grade (0-20) ;
 - `if` imbriqués ;
 - expression conditionnelle (« ternaire ») par curiosité ;
- structures de répétition :
 - `while` : répéter tant que la condition est vraie, soyez prudent avec des cycles infinis ;
 - `for` à propos des chaînes, des listes et `range`;
- `range()`:
 - `range(fim)`, `range(inicio, fim)`, `range(inicio, fim, passo)` (inclut l'étape négative) ;
- blocs de code et indentation :
 - 4 espaces Rule;
 - comment Python utilise l'indentation au lieu de `{}`.

Exercices axés sur :

- classification des notes;
- vérifier si un nombre est dans une plage;
- décompte (avec `for` et `while`);
- additionner de 1 à `n`;
- multiplication 
- jeu de devinettes avec limite de tentatives.

---

### `03_listes_dictionnaires_structures_imbriquees.md`

[Voir fichier](./03_listes_dictionnaires_structures_imbriquees.md)

**Objectif :** consolider le stockage des collections de données et former un façon de penser plus structurée.

Contenu principal :

- **listes** :
 - création, accès par index (positif et négatif) ;
 - modification d'éléments ;
 - méthodes : `append`, `insert`, `pop`, `remove`, `clear`, `count`, `index`, `sort`, `reverse`;
 - fonctions : `len`, `sum`, `min`, `max`, `sorted`;
 - parcourir des listes avec `for` (par élément et par index);
 - modèles classiques :
 - créer de nouveaux liste;
 - filtrer les valeurs;
 - calculer la moyenne;
 - trouver le minimum/maximum sans `min`/`max`;
 - brève introduction aux **compréhensions de liste** (par curiosité);
- **dictionnaires**:
 - idée clé→valeur;
 - création, accès, mise à jour, insertion et suppression;
 - méthodes : `keys`, `values`, `items`, `get`;
 - vérifier l'existence des clés avec `in`;
 - exemples appliqués (prix des fruits, données des personnes);
- **structures imbriquées**:
 - liste des listes (matrice);
 - dictionnaire de listes (classes et étudiants);
 - dictionnaire de dictionnaires (étudiant → matière → note);
 - liste de dictionnaires (livres, étudiants, etc.);
 - parcours avec cycles imbriqués;

Comprend des exemples appliqués tels que :

- mini « base de données » de livres ;
- classes avec élèves et notes ;
- températures mensuelles moyennes dans une ville.

Exercices axés sur :

- création et défilement de listes;
- séparation pair/impair;
- comptage positifs/négatifs;
- manipuler des dictionnaires simples;
- travailler avec des structures imbriquées (matrice, classes, notes, livres).

---

### `04_fonctions_du_basique_au_avance.md`

[Voir file](./04_fonctions_du_basique_au_avance.md)

**Objectif :** construire un module solide sur les **fonctions**, depuis le `def` de base jusqu'aux idées d'ordre supérieur, avec les parties **essentielles** clairement mises en évidence et les sujets les plus avancés clairement marqués comme **extra**.

Le fichier est organisé avec des balises :

- **[ESSENTIEL]** – obligatoire pour maîtriser les bases de Python ;
- **[EXTRA]** – curiosité / sujets plus avancés (peuvent être consultés plus tard).

Contenu principal :

- pourquoi utiliser des fonctions :
 - éviter les répétitions;
 - organiser le code;
 - faciliter les tests;
- définir et appeler des fonctions (`def`):
 - exemples de base (`ola_mundo`, `soma`, `saudacao`);
 - différence entre `print` à l'intérieur de la fonction et `return`;
- paramètres et arguments :
 - positionnel vs nommé ;
 - valeurs par défaut;
 - bonnes pratiques pour les noms et paramètres de fonction;
- `return`:
 - absence de `return` → `None`;
 - renvoie une valeur;
 - renvoie plusieurs valeurs via des **tuples** (ex. : division qui renvoie le quotient et le reste);
 - **sortie anticipée** (cas particuliers);
- scope (espace de noms) :
 - variables locales;
 - notion de global (à éviter dans la plupart des cas cas);
 - `nonlocal` par curiosité (exemple `cria_contador`);
- mutabilité et passage d'arguments:
 - immuable (`int`, `float`, `str`, `tuple`);
 - mutable (`list`, `dict`);
 - fonctions qui modifient les listes reçues;
 - danger de valeurs par défaut_ mutables (`acumulador_errado` vs `acumulador_correto`);
- **[EXTRA]** fonctions d'ordre supérieur et `lambda`:
 - fonctionne comme des valeurs;
 - `aplicar(func, valor)`;
 - `map`, `filter`, `sorted(key=...)` vs compréhensions de liste;
- **[EXTRA]** `*args` et `**kwargs`:
 -fonctions « élastiques » (`media(*nums)`, `configurar(**opcoes)`);
 - décompressez les listes et les dictionnaires lors de l'appel ;
- **[EXTRA]** docstrings et annotations de type :
 - exemple `normalizar_textos`;
 - référence rapide à `typing` (`list[str]`, `Sequence[str]`);
- **[EXTRA]** récursion :
 - idée d'une fonction qui s'appelle elle-même ;
 - cas de base et étape récursive ;
 - exemple `fatorial`, `conta_decrescente`;
 - avertissement sur les limites et quand préférer `while`/`for`;
- bonnes pratiques :
 - fonctions courtes, une responsabilité;
 - `if __name__ == "__main__":` pour les démos et petits tests;
 - utilisation de `assert` pour les tests rapides.

Exercices ciblés en :

- écrire des fonctions simples (`ola_mundo`, `soma`, compter les lettres);
- fonctions avec listes (compter impair/pair, moyenne, somme);
- fonctions avec dictionnaires (compter les élèves par classe, trouver la personne la plus âgée, moyennes par élève);
- défis avec `*args` et simples récursion.

---

### `05_algorithmes_et_modeles_de_programmation.md`

[Voir le fichier](./05_algorithmes_et_modeles_de_programmation.md)

**Objectif :** 
Commencez à penser comme un **programmeur**, en utilisant cela a déjà été appris (variables, listes, dictionnaires, fonctions) pour résoudre des problèmes complets : analyser l'instruction, planifier la solution et ensuite seulement écrire du code.

Contenu principal :

- comment s'attaquer à un problème de programmation :
 - identifier les **entrées**, **traitements** et **sorties**;
 - faire des exemples à la main avant de programmer;
 - rédiger un plan en portugais (pseudocode) avant le code;
- modèles classiques avec **listes**:
 - lire les valeurs d'une liste (saisie en cycle + `append`);
 - **modèle de cumul** (sommes, moyennes);
 - **modèle de comptage conditionnel** (compter les positifs, les paires, approuvés, etc.);
 - recherche manuelle **minimum/maximum** (sans `min`/`max`);
 - modèle de recherche **filtrage** (nouvelle liste avec les éléments qui remplir une condition);
 - **modèle de transformation** (nouvelle liste avec valeurs transformées);
- modèles avec **dictionnaires**:
 - "mini base de données" en mémoire (nom → âge, produit → prix, etc.);
 - recherche par clé (`if chave in dicionario`);
 - nombre de fréquences (combien de fois chaque mot/lettre apparaît);
 - dictionnaire de listes (classe → liste des étudiants);
- rassembler le tout dans **fonctions** :
 - séparer les fonctions « pures » (avec `return`) de `input`/`print`;
 - décomposer les problèmes plus importants en petites fonctions (moyenne des étudiants, meilleur élève, étudiants en échec, etc.);
- erreurs typiques et **de base débogage** :
 - oublier `return`, confondre `=` avec `==`, erreurs dans `range`, mutabilité ;
 - utilisation des `print` et `assert` intermédiaires pour les tests.

Exercices axés sur :

- consolidation de modèles avec des listes et des dictionnaires;
- application de stratégies de décomposition aux fonctions;
- analyse des énoncés en portugais avant d'écrire du code;
- défis avec structures imbriquées et petits « mini-projets » guidés.

---

### `06_decoupage_list_comprehensions.md`

[Voir le fichier](./06_decoupage_list_comprehensions.md)

**Objectif :**
Approfondir deux sujets importants pour manipulation de listes en Python : **slicing** et **compréhensions de listes**.

Contenu principal :

- **Slicing** :
 - syntaxe de base : `lista[inicio:fim:passo]`;
 - valeurs par défaut (omettre `inicio`, `fim` ou `passo`);
 - indices négatifs;
 - exemples pratiques (sous-listes, inversion de listes, prise d'éléments de `n` dans `n`);
 - utilisation du découpage avec des chaînes;
- **Compréhensions de listes** :
 - syntaxe de base : `[expressao for item in lista if condicao]`;
 - créer des listes de manière concise;
 - exemples avec transformation et filtrage;
 - compréhensions imbriquées (listes de listes);
 - comparaison avec des boucles traditionnelles.

Exercices axés sur :

- pratiquer le découpage en listes et chaînes;
- créer de nouvelles listes à l'aide de compréhensions;
- des défis qui combinent découpage et compréhensions.

---

### `07_fichiers_texte_json_csv.md`

[Afficher le fichier](./07_fichiers_texte_json_csv.md)

**Objectif :** 
Introduire le travail avec des **fichiers** en Python, pour sauvegarder et réutiliser les données entre les exécutions, en utilisant formats simples et pratiques.

Contenu principal :

- fichiers texte (`.txt`):
 - `open` avec les modes `"r"`, `"w"` et `"a"`;
 - utilisation de `with open(..., encoding="utf-8")`;
 - écrire des lignes avec `write`;
 - lire ligne par ligne avec `for`, `read`, `readlines`;
- Fichiers JSON (`.json`):
 - qu'est-ce que JSON (dictionnaires/listes de texte);
 - enregistrer des dictionnaires et des listes avec `json.dump`;
 - lire des structures Python avec `json.load`;
 - exemples avec un élève et liste d'élèves;
- fichiers CSV (`.csv`):
 - notion de tableau (lignes/colonnes séparées par `;`);
 - écrire « à la main » le CSV à partir de listes/dictionnaires;
 - lecture « à la main » avec `split(";")` et conversion de type;
 - curiosité : utilisation basique du module `csv` (`DictReader`);
- bonnes pratiques :
 - toujours utiliser `with open` et `encoding="utf-8"`;
 - lire des fichiers volumineux ligne par ligne.

Exercices axés sur :

- créer et lire des journaux dans `.txt`;
- enregistrer et lire les dossiers des étudiants en JSON;
- exporter des listes de dictionnaires au format CSV et calculer des statistiques simples.

---

### `08_exceptions_et_traitement_des_erreurs.md`

[Afficher le fichier](./08_exceptions_et_traitement_des_erreurs.md)

**Objectif :** 
Comprendre les types d'erreurs les plus courants en Python, apprendre à lire les messages d'erreur (tracebacks) et utiliser `try`/`except` pour rendre les programmes plus robustes et convivial.

Contenu principal :

- types d'erreurs :
 - `SyntaxError` vs erreurs d'exécution ;
 - exemples de `ValueError`, `ZeroDivisionError`, `TypeError`, `IndexError`, `KeyError`, etc.;
- lecture des messages d'erreur :
 - fichier, ligne, type d'erreur et message;
 - comment utiliser le traçage pour trouver le problème;
- `try`/`except` basic:
 - syntaxe générale;
 - utiliser `try`/`except` pour valider `input`;
 - exceptions spécifiques de capture (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, ...);
- sections **[EXTRA]**:
 - blocs multiples `except` et capture multiple;
 - exception générique (`Exception`) et précautions à prendre prendre;
 - `else` et `finally`;
 - lancer des erreurs avec `raise` et utiliser `assert`.

Exercices axés sur :

- rendre les lectures `input` plus sécurisées ;
- gérer les erreurs lors du fractionnement, de la lecture de fichiers, JSON et CSV ;
- implémenter de petits menus et des fonctions robustes avec gestion des exceptions.

---

### `09_modules_et_organisation_de_projets.md`

[Afficher le fichier]@./09_modules_et_organisation_de_projets.md)

**Objectif :** 
Apprendre à organiser le code dans plusieurs fichiers et à réutiliser les fonctions avec `import`, en préparant des projets plus petits, plus propres et plus faciles à entretenir.

Principal contenu :

- qu'est-ce qu'un module et pourquoi l'utiliser ;
- différentes formes de `import` et bonnes pratiques ;
- `if __name__ == "__main__":` pour des tests simples;
- séparation de la logique et des E/S en différents fichiers;
- exemple de mini organisé projet.

Exercices axés sur :

- créer des modules simples et importer des fonctions;
- appliquer `as` et éviter `import *`;
- organiser un mini projet avec 2-3 fichiers.

---

### `10_structures_et_algorithmes_classiques.md`

[Afficher le fichier](./10_structures_et_algorithmes_classiques.md)

**Objectif :** 
Introduire la recherche linéaire, le tri de base (bulle et sélection) et une notion simple de efficacité.

Contenu principal :

- ce que sont les algorithmes et pourquoi les étudier;
- recherche linéaire avec et sans index;
- tri à bulles et tri par sélection;
- notion simple d'efficacité et comparaison des étapes.

Exercices axés sur:

- mise en œuvre de recherches linéaires et par étapes comptage;
- trier les listes avec tri à bulles/sélection;
- appliquer le tri et la recherche aux listes de nombres et de noms.

---

### `11_projet_final_python.md`

[Voir fichier](./11_projet_final_python.md)

**Objectif :** 
Décrire le projet final du module : création d'un quiz console, avec exigences, règles et niveaux d'amélioration.

Contenu principal :

- contexte, objectifs et organisation du travail en groupe;
- structure du fichier `perguntas.json` et validations de base ;
- fonctionnalités obligatoires (MVP) et extensions facultatives ;
- bonnes pratiques de modularisation et de robustesse.

---

## Comment utiliser ces matériaux

1. Utilisez `00_formulaire_support.md` comme formulaire de référence rapide.
2. Suivez l'**ordre des fichiers** (01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10) et fusionnez `00_exercices_de_preparation.md` pour examen.
3. Dans chaque fichier :
 - lisez d'abord la théorie et les exemples;
 - copiez quelques exemples dans un fichier `.py` et essayez de les modifier;
 - essayez de résoudre tous les exercices, dans l'ordre présenté;
 - marquez les parties avec **[EXTRA]** pour les revoir plus tard si vous rencontrez des difficultés.
4. Après avoir maîtrisé 01–10, appliquez vos connaissances à `11_projet_final_python.md`.

---

## Prérequis et environnement de travail

- Python 3.x installé (idéalement une version récente, ex. : 3.11/3.12).
- Editeur recommandé : **VS Code** ou IDE en ligne avec :
 - Extension **Python** ;
 - (facultatif) outil d'exécution intégré (Run/Debug).

Pour exécuter un exemple :

1. Créez un fichier, par exemple `exemplo.py`;
2. Copiez le code du fichier `.md` vers `.py`;
3. Enregistrer ;
4. Exécutez avec :
 - `python exemplo.py` dans le terminal, ou
 - le bouton _Run_ dans l'éditeur.

---
