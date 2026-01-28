# Python (10e année) - 07 · Fichiers texte, JSON et CSV

> **Objectif de ce fichier** 
> Apprenez à lire et à écrire des fichiers simples en Python (texte, JSON et CSV) pour sauvegarder et réutiliser des données entre les exécutions du programme.

---

## Index

- [0. Comment utiliser ce fichier](#0-comment-utiliser-ce-fichier)
- [1. Introduction : pourquoi utiliser des fichiers ?](#1-introduction-pourquoi-utiliser-des-fichiers)
- [2. Fichiers JSON (`.json`)](#2-fichiers-json-json)
- [3. Fichiers texte (`.txt`)](#3-fichiers-texte-txt)
- [4. Fichiers CSV (`.csv`)](#4-fichiers-csv-csv)
- [5. Bonnes pratiques avec les fichiers](#5-bonnes-pratiques-avec-les-fichiers)
- [6. Exercices - Fichiers texte, JSON et CSV](#6-exercices-fichiers-texte-json-et-csv)
- [7. Changelog](#7-changelog)

---

## 0. Comment utiliser ce fichier

1. Assurez-vous de connaître :
 - les variables, les types de base et `input`/`print` (`01_introduction_variables_types_strings_io.md`);
 - `if`, cycles `for`/`while` (`02_operateurs_et_controle_de_flux_if_boucles.md`);
 - les listes et dictionnaires (`03_listes_dictionnaires_structures_imbriquees.md`);
 - les fonctions simples (`04_fonctions_du_basique_au_avance.md`).
2. Lit les sections dans l'ordre : texte → JSON → CSV.
3. Testez tous les exemples dans un fichier `.py`:
 - observez quels fichiers sont créés dans le même dossier;
 - ouvrez les fichiers dans l'éditeur pour voir le « résultat ».
4. À la fin, résolvez les **exercices**.  
 Commencez par les fichiers texte, puis JSON et enfin CSV.

---

## 1. Introduction : pourquoi utiliser des fichiers ?

Jusqu'à présent, les programmes :

- lisaient les données avec `input`;
- effectuaient des calculs/traitements;
- montraient les résultats avec `print`;
- à la fin du programme, **tout a été perdu**.

Avec **fichiers**, nous pouvons :

- enregistrer des données pour les utiliser **dans une autre exécution** du programme;
- lire des informations écrites par une autre personne / programme;
- échanger des données avec d'autres programmes (par exemple, Excel).

Types de fichiers que nous utilisons voir :

- **texte (`.txt`)** → lignes de texte normal;
- **JSON (`.json`)** → structure de données (dictionnaires/listes) au format texte;
- **CSV (`.csv`)** → tableau simple (lignes/colonnes), souvent utilisé dans les feuilles de calcul calcul.

---

## 2. Fichiers JSON (`.json`)

### 2.1. Qu’est-ce que JSON ? · [ESSENTIEL]

JSON est un format de texte pour stocker des **structures de données** :

- dictionnaires (`{ ... }`) → paires clé/valeur;
- listes (`[ ... ]`);
- nombres, chaînes, `true`/`false` (en Python → `True`/`False`), `null` (Python → `None`).

Exemple de JSON dans le fichier `aluno.json` :

```json
{
    "nome": "Ana",
    "idade": 16,
    "notas": [14, 15, 12],
    "aprovado": true
}
```

Json est largement utilisé pour échanger des données entre programmes (API, bases de données, etc.). Il fait partie de l'épine dorsale du Web moderne puisque la plupart des services Web utilisent JSON pour communiquer.

Python dispose d'un module pour travailler avec JSON : `import json`.

#### 2.1.1. Importer le module JSON

Avant d'utiliser les fonctions JSON, il faut importer le module :

```python
import json
```

Un module (que nous verrons plus tard) est un ensemble de fonctions et de variables prédéfinies que nous pouvons utiliser dans notre code.
A partir du moment où nous faisons `import json`, nous pouvons utiliser les fonctions du module `json` avec le préfixe `json.`.

---

### 2.2. Enregistrez les données en JSON avec `json.dump` · [ESSENTIEL]

Imaginez que nous ayons une liste de nombres :

```python
nombres = [10, 20, 30, 40]
```

Nous souhaitons maintenant enregistrer cette liste dans un fichier JSON.
Pour cela, nous allons utiliser une nouvelle structure, `with`.

Le `with`crée un contexte pour ouvrir le fichier et s'assurer qu'il est fermé à la fin du bloc.

Ensuite, nous utilisons la fonction `open` pour ouvrir le fichier en mode écriture (`"w"`).

```python
import json

nombres = [10, 20, 30, 40]

with open("nombres.json", "w") as f:
    json.dump(nombres, f)
```

Cela crée un fichier `numeros.json` avec le contenu suivant :

```json
[10, 20, 30, 40]
```

Autre exemple, avec un dictionnaire.
Enregistrons un dictionnaire dans un fichier `aluno.json` :

```python
import json

etudiant = {
    "nom": "Nain",
    "âge": 16,
    "remarques": [14, 15, 12],
    "approuvé": True,
}

with open("étudiant.json", "w", codage="utf-8") as f:
    json.dump(etudiant, f, assurer_ascii=False, retrait=4)
```

Remarques :
Remarquez que nous avons maintenant plus d'arguments dans `json.dump` et `open`. Les deux fonctions acceptent plusieurs paramètres facultatifs pour contrôler le comportement de l'interaction avec le fichier.

- `encoding="utf-8"` → pour prendre en charge les accents.
- `json.dump(dados, ficheiro, ...)` écrit les données au format JSON.
- `ensure_ascii=False` → permet les accents dans le fichier.
- `indent=4` → « beau » (en retrait) et facile à lire.

Ouvrez `aluno.json` dans l'éditeur et observez la structure.

> Qu'est-ce que utf-8 ?
> UTF-8 est une norme de codage de caractères qui vous permet de représenter pratiquement tous les caractères utilisés dans les langues humaines. L'utilisation d'UTF-8 garantit que les accents, les symboles et les caractères spéciaux sont stockés correctement dans les fichiers texte.
> Fondamentalement, il s'agit d'une carte qui indique à l'ordinateur comment transformer les bits (0 et 1) en lettres et symboles que nous comprenons.
> Par exemple :
>
> - La lettre minuscule "a" est représentée par l'octet 01100001 dans UTF-8.
> - La lettre "á" (avec accent) est représentée par deux octets : 11000011 10100001.
> L'utilisation d'UTF-8 est importante pour éviter les problèmes liés aux caractères étranges ou illisibles, en particulier lorsque vous travaillez avec des langues qui utilisent des accents ou des symboles spéciaux.

> Qu'est-ce que l'ASCII ?
> ASCII (American Standard Code for Information Interchange) est une norme de codage de caractères qui représente des lettres, des chiffres et des symboles de base à l'aide de 7 bits (128 caractères). Il est limité aux caractères anglais sans accents ni symboles spéciaux.
> Par exemple :
>
> - La lettre majuscule "A" est représentée par l'octet 01000001 en ASCII.
> - Le chiffre "0" est représenté par l'octet 00110000.
> L'ASCII est simple et efficace, mais ne prend pas en charge les caractères accentués ou symboles utilisés dans d’autres langues. Ainsi, pour les textes avec des accents ou des caractères spéciaux, nous utilisons UTF-8, qui est plus complet.

> Alors pourquoi utilisons-nous les deux ? Un dans `open` et un dans `json.dump`?
> Nous utilisons `encoding="utf-8"` dans `open` pour garantir que le fichier est lu et écrit correctement avec des accents et des caractères spéciaux. `ensure_ascii=False` dans `json.dump` indique à Python de ne pas convertir les caractères non-ASCII en séquences d'échappement (comme `\u00e1` pour "á"), permettant d'écrire les accents directement dans le fichier JSON. De cette façon, nous garantissons que la lecture/écriture du fichier et le format JSON supportent correctement les caractères spéciaux.

### 2.3. Lecture de données JSON avec `json.load` · [ESSENTIEL]

Lisons maintenant le même fichier et travaillons avec les données en Python :

```python
import json

with open("étudiant.json", "r", codage="utf-8") as f:
    etudiant = json.load(f)   # redevient un dictionnaire Python dans "étudiant"

# À partir de là, nous pouvons utiliser « étudiant » comme dictionnaire normal.

print("Nom:", etudiant["nom"])
print("Remarques :", etudiant["remarques"])
moyenne = sum(etudiant["remarques"]) / len(etudiant["remarques"])
print("Moyenne:", moyenne)
```

Remarque :

- `json.load(f)` → lit le fichier et renvoie un dictionnaire/liste Python normal.
- Ensuite, nous pouvons utiliser `[]`, `for`, etc., comme dans n'importe quelle structure.

---

### 2.4. Liste de plusieurs enregistrements en JSON · [ESSENTIEL]

Il est très courant de sauvegarder **une liste de dictionnaires** :

```python
import json

etudiants = [
    {"nom": "Nain", "âge": 16, "avis": 15},
    {"nom": "Bruno", "âge": 17, "avis": 12},
    {"nom": "Carla", "âge": 16, "avis": 18},
]

with open("étudiants.json", "w", codage="utf-8") as f:
    json.dump(etudiants, f, assurer_ascii=False, retrait=4)
```

Après :

```python
import json

with open("étudiants.json", "r", codage="utf-8") as f:
    etudiants = json.load(f)

for etudiant in etudiants:
    print(etudiant["nom"], "-", etudiant["avis"])
```

Ceci est utile pour les petits systèmes de gestion (étudiants, produits, etc.).

---

### 2.5. Modes d'ouverture de fichiers · [ESSENTIEL]

Lors de l'ouverture de fichiers (quel que soit le type de fichier), nous utilisons différents modes :

- `"r"` → lire → le fichier doit exister ;
- `"w"` → écrire → créer ou supprimer un contenu ancien. L'ancien contenu est perdu ;
- `"a"` → append → crée s'il n'existe pas, l'ajoute à la fin sans supprimer l'ancien contenu.
- `"x"` → créer → crée le fichier vide, donne une erreur s'il existe déjà.
- `"b"` → binaire → utilisé pour les fichiers non texte (images, sons, etc.). Nous ne l'utiliserons pas ici.

On peut combiner des modes, par exemple :

- `"rb"` → lire en binaire;
- `"wb"` → écrire en binaire;
- `"ab"` → ajouter binaire.

---

## 3. Fichiers texte (`.txt`)

### 3.1. Ouvrez un fichier avec `open` et `with` · [ESSENTIEL]

En Python, nous pouvons utiliser des fichiers texte. Les fichiers texte sont des fichiers simples qui contiennent uniquement du texte lisible (sans formatage particulier).
Ils portent généralement l'extension `.txt`, mais ils peuvent également avoir d'autres extensions.

Syntaxe de base (forme recommandée) :

```python
with open("exemple.txt", "w", codage="utf-8") as f:
    f.write("Bonjour, fichier !\n")
```

Remarques :

> Toutes les règles d'ouverture des fichiers JSON s'appliquent également ici (modes, encodage, etc.).

---

### 3.2. Écrire plusieurs lignes dans un fichier texte · [ESSENTIEL]

Exemple : demander 3 phrases à l'utilisateur et les enregistrer dans un fichier.

```python
with open("phrases.txt", "w", codage="utf-8") as f:
    for i in range(3):
        phrase = input(f"Phrase {i + 1} : ")
        f.write(phrase + "\n")
```

Puis ouvrez `frases.txt` dans l'éditeur et confirmez le contenu.

---

### 3.3. Lire un fichier texte ligne par ligne · [ESSENTIEL]

Exemple : lire le fichier `frases.txt` et afficher les lignes numérotées.

```python
with open("phrases.txt", "r", codage="utf-8") as f:
    for numero_de_ligne, doubler in enumerate(f, commencer_2=1):
        doubler = doubler.rstrip("\n")   # supprimer le saut de ligne à la fin
        print(f"{numero_de_ligne} : {doubler}")
```

Remarques :

- Le fichier lui-même peut être parcouru avec `for`, ligne par ligne.
- `enumerate` nous donne le numéro de ligne et le texte de la ligne.

### 3.4. Lire le fichier en entier d'un coup · [EXTRA]

Parfois, il est utile de tout lire dans une chaîne ou une liste :

```python
with open("phrases.txt", "r", codage="utf-8") as f:
    contenu = f.read()       # chaîne avec le fichier ENTIER

print(contenu)
```

Ou :

```python
with open("phrases.txt", "r", codage="utf-8") as f:
    lignes = f.readlines()    # liste de chaînes (lignes)

print(lignes)
```

Pour les gros fichiers, il est plus efficace de lire **ligne par ligne** avec `for`.

---

## 4. Fichiers CSV (`.csv`)

### 4.1. Qu'est-ce qu'un CSV ? · [ESSENTIEL]

CSV signifie **Comma-Separated Values** (valeurs séparées par des virgules).

- Il s'agit d'un format de texte pour stocker des **tableaux** (lignes et colonnes).
- Chaque ligne est un enregistrement (par exemple, un étudiant).
- Les colonnes sont séparées par des virgules ou point-virgule.

Exemple de `alunos.csv` :

```text
nome;idade;nota
Ana;16;15
Bruno;17;12
Carla;16;18
```

### 4.2. Écrire CSV « à la main » · [ESSENTIEL]

Sans utiliser de modules, nous pouvons écrire des lignes de texte séparées par `;` :

```python
with open("étudiants.csv", "w", codage="utf-8") as f:
    f.write("nom;âge;grade\n")  # en-tête

    etudiants = [
        {"nom": "Nain", "âge": 16, "avis": 15},
        {"nom": "Bruno", "âge": 17, "avis": 12},
        {"nom": "Carla", "âge": 16, "avis": 18},
    ]

    for etudiant in etudiants:
        doubler = f"{etudiant['nome']};{etudiant['idade']};{etudiant['nota']}\n"
        f.write(doubler)
```

Ensuite, vous pouvez ouvrir `alunos.csv` dans Excel / LibreOffice / Google Sheets.

### 4.3. Lisez le CSV « à la main » · [ESSENTIEL]

Lisons `alunos.csv` et calculons la moyenne des scores :

```python
with open("étudiants.csv", "r", codage="utf-8") as f:
    en_tete = f.readline()   # lit la première ligne et ignore

    ajoute_des_notes = 0
    comptoir = 0

    for doubler in f:
        doubler = doubler.strip()          # décoller \n
        nom, age_str, note_str = doubler.split(";")

        age = int(age_str)
        avis = int(note_str)

        ajoute_des_notes += avis
        comptoir += 1

moyenne = ajoute_des_notes / comptoir
print("Moyenne scolaire :", moyenne)
```

Remarques :

- `split(";")` → divise la ligne en parties (liste de chaînes).
- Il est important de convertir `idade` et `nota` en `int`.

### 4.4. Utilisez le module `csv` (curiosité / EXTRA)

Python dispose d'un module `csv` qui permet de gérer les cas plus ennuyeux (virgules dans les textes, etc.).  
À titre de curiosité :

```python
import csv

with open("étudiants.csv", "r", codage="utf-8", nouvelle_ligne_2="") as f:
    lecteur = csv.DictReader(f, delimiteur=";")
    for doubler in lecteur:
        print(doubler["nom"], "-", doubler["avis"])
```

Pour la 10e année, vous voudrez peut-être d'abord vous familiariser avec la version « à la main ».

---

## 5. Meilleures pratiques avec les fichiers

- Utilisez toujours `with open(...)` pour vous assurer que le fichier est fermé.
- Utilisez `encoding="utf-8"` pour évitez les problèmes d'accents.
- Si le fichier est volumineux, **lisez ligne par ligne** avec une boucle `for`.
- Choisissez des noms de fichiers clairs : `alunos.txt`, `produtos.csv`, etc.
- Enregistrez les fichiers de données **à côté de votre script** pendant que vous apprenez (pour plus de simplicité chemins).

---

## 6. Exercices - Fichiers texte, JSON et CSV

### Exercice 1 - Liste de nombres en JSON · [BASIC]

Créer un programme qui :

- Générer un liste de 100 entiers aléatoires compris entre 1 et 1000;
- Enregistrez cette liste dans un fichier `numeros.json` en utilisant `json.dump`.

---

### Exercice 2 - Lire la liste des nombres depuis JSON · [BASIC]

Créer un programme que :

- Lire le fichier `numeros.json` de l'exercice précédent en utilisant `json.load`;
- Calculer et afficher :

 - le plus grand nombre;
 - le plus petit nombre;
 - la moyenne des nombres.

- Ensuite, il demande à l'utilisateur un numéro et vérifie s'il est dans le fichier.

---

### Exercice 3 - Journal simple (`.json`) · [BASIC]

Créez un programme qui :

- demande à l'utilisateur d'écrire une phrase (message du jour) ;
- ajoute cette phrase à la fin du fichier `diario.json` (utilise une liste) ;
- à la fin, affiche un message indiquant que la phrase a été enregistrée.

Exécutez le programme 2 à 3 fois et vérifiez si le fichier a été enregistré. mis à jour.

---

### Exercice 4 - Lire le journal · [BASIC]

Écrire un programme qui :

- lit le fichier `diario.json`;
- affiche toutes les phrases numérotées (1:, 2:, 3:, ...).

---

### Exercice 5 - Écrire un dictionnaire en JSON · [BASIC]

Écrire un programme qui :

- demande à l'utilisateur de saisir ses données personnelles :
 - nom (chaîne) [BASIC]

Crée un fichier `utilizadores.json` avec le contenu suivant :

```json
[
    { "username": "ana", "password": "senha123" },
    { "username": "bruno", "password": "qwerty" },
    { "username": "carla", "password": "abc123" }
]
```

Ensuite, écrivez un programme qui :

- lit le fichier `utilizadores.json`;
- demande à l'utilisateur d'insérer son `username` et `password`;
- vérifie si `username` et `password` correspondent à l'un des utilisateurs du fichier;
- affiche un message "Connexion réussie" ou "Identifiants non valides".

---

### Exercice 7 - Utiliser des fonctions, des dictionnaires et JSON · [INTERMÉDIAIRE]

Écrire un programme qui :

- définit une fonction `adicionar_tarefa(titulo, descricao)` qui :
 - lit le fichier `tarefas.json` (s'il existe);
 - ajoute une nouvelle tâche (dictionnaire avec `titulo` et `descricao`) à une liste de tâches;
 - enregistre la liste mise à jour des tâches dans le fichier;
- définit une fonction `mostrar_tarefas()` qui:
 - lit le fichier `tarefas.json`;
 - affiche toutes les tâches numérotées ;
- dans le programme principal, crée un menu de navigation simple avec 3 options :

 - ajouter une tâche;
 - afficher les tâches;
 - quitter.

---

### Exercice 8 - Gestion des contacts · [INTERMÉDIAIRE]

Écrivez un programme qui :

- définit une fonction `adicionar_contacto(nome, telefone)` qui :
 - lit le fichier `contactos.json` (s'il existe) ;
 - ajoute un nouveau contact (dictionnaire avec `nome` et `telefone`) à une liste de contacts ;
 - enregistre la liste mise à jour des contacts dans le fichier ;
- définit une fonction `mostrar_contactos()` qui :
 - lit le fichier `contactos.json`;
 - affiche tous les contacts numérotés;
- dans le programme principal, crée un menu de navigation simple avec 4 options :
 - ajouter un contact;
 - afficher les contacts;
 - rechercher un contact par nom;
 - exit.

---

### Exercice 9 - Gestion des notes · [DÉFI]

Écrire un programme qui :

- définit une fonction `adicionar_nota(aluno, disciplina, nota)` qui :
 - lit le fichier `notas.json` (s'il existe) ;
 - ajoute une nouvelle note (dictionnaire avec `aluno`, `disciplina` et `nota`) à une liste de notes ;
 - enregistre la liste de notes mise à jour dans le fichier ;
- définit une fonction `mostrar_notas()` qui :
 - lit le fichier `notas.json`;
 - affiche toutes les notes numérotées ;
- définit une fonction `calcular_media(aluno)` qui :
 - lit le fichier `notas.json`;
 - calcule et renvoie la moyenne des notes à partir du fichier spécifié étudiant;
- dans le programme principal, crée un menu de navigation simple avec 5 options :
 - ajouter une note;
 - afficher les notes;
 - calculer la moyenne d'un élève;
 - afficher l'étudiant avec la meilleure moyenne;
 - quitter.

---

## 7. Journal des modifications

- **2025-11-26 · v1.0**
 - Création initiale du fichier avec introduction de fichiers texte, JSON et CSV.
