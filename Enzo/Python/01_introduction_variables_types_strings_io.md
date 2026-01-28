# Python (10e année) - 01 · Introduction, Variables, Types, Chaînes et E/S

> **Objectif de ce fichier** 
> Vous donner des bases solides en Python : qu'est-ce que programmer, comment déclarer des variables, connaître les types de données les plus utilisés, travailler avec du texte (chaînes) et communiquer avec l'utilisateur en utilisant `print()` et `input()`.

---

## Index

- [0. Comment utiliser ce fichier](#0-comment-utiliser-ce-fichier)
- [1. Qu'est-ce que la programmation ?](#1-quest-ce-que-la-programmation)
- [2. Premier contact avec Python](#2-premier-contact-avec-python)
- [3. Variables](#3-variables)
- [4. Types de données de base](#4-types-de-donnees-de-base)
- [5. Chaînes (texte)](#5-chaines-texte)
- [6. Commentaires](#6-commentaires)
- [7. Entrée et sortie : `print()` et `input()`](#7-entree-et-sortie-print-et-input)
- [8. Exercices (Introduction, Variables, Types, Chaînes, E/S)](#8-exercices-introduction-variables-types-chaines-es)
- [9. Changelog](#9-changelog)

---

## 0. Comment utiliser ce fichier

1. Lisez calmement l'explication théorique.
2. Analysez les exemples de code - essayez de prédire le résultat **avant** de l'exécuter.
3. Reproduisez les exemples dans votre éditeur / IDE.
4. À la fin, résolvez les **exercices** (10-12). Commencez par les plus faciles et progressez en difficulté.

Si vous avez des questions, écrivez-les et parlez-en à l'enseignant.

---

## 1. Qu'est-ce que la programmation ?

La programmation consiste à donner des **instructions très précises** à l'ordinateur pour qu'il puisse résoudre un problème.<

- Au lieu de faire le calcul à la main, vous indiquez exactement à l'ordinateur :
 - quelles données il va lire (saisie),
 - ce qu'il doit faire avec ces données (traitement),
 - et ce qu'il doit afficher à l'écran (sortie).

Python est un langage de programmation **largement utilisé dans le monde réel** (web, science des données, intelligence artificielle, automatisation, etc.) et est également très bon pour apprendre à programmer pour la première fois.

---

## 2. Premier contact avec Python

Il existe deux manières principales de essayez Python :

1. **REPL / Console interactive** 
 Vous écrivez une commande, appuyez sur Entrée et voyez le résultat.  
 Exemple dans la console Python :

```python
    >>> 2 + 3
    5
    >>> "Bonjour" * 3
    'BonjourBonjourBonjour'
```

2. **Fichiers `.py` (scripts)** 
 Vous enregistrez votre code dans un fichier, par exemple `exemplo.py`, puis exécutez ce fichier.  
 Avantage : vous obtenez des programmes plus longs, plus organisés et plus faciles à sauvegarder.

Dans ce module, nous penserons aux fichiers `.py`, mais tous les exemples fonctionnent également dans la console interactive.

---

## 3. Variables

### 3.1. Qu'est-ce qu'une variable ?

Une variable est comme **une étiquette coincée dans une boîte** où vous stockez une valeur.

- L'étiquette est le **nom de la variable**.
- Le contenu de la boîte est la **valeur** (nombre, texte, etc.).
- En Python, le type de valeur est **automatiquement déduit** (saisie dynamique).

Exemple :

```python
age = 16            # age est une "tag" pour la valeur entière 16
hauteur = 1.72         # float (nombre décimal)
nom = "Nain"          # chaîne (texte)
approuve = True       # booléen (Vrai/Faux)
```

### 3.2. Noms de variables (conventions)

- Utiliser **snake_case** : mots minuscules séparés par `_` 
 → `media_turma`, `numero_alunos`, `nota_final`
- Ne pas commencer par un chiffre ni utiliser d'espaces :
 - ✅ `idade_aluno`
 - ❌ `1idade`, `idade aluno`
- Évitez les noms comme `a`, `b`, `x` dans les programmes réels.  
 Il est préférable d'utiliser des noms qui **expliquent la signification**.

### 3.3. Réaffectation (changement de valeur)

La même variable peut stocker des valeurs de différents types tout au long du programme (ce n'est pas une bonne pratique d'en abuser, mais c'est possible).

```python
age = 16
print(age)          # 16

age = "seize"   # maintenant age stocke une chaîne
print(age)          # "seize"
```

Dans les programmes plus volumineux, il est préférable de garder le type de chaque variable cohérent (ne pas trop le mélanger).

---

## 4. Types de données de base

Python a plusieurs types de données. Les plus importants à ce stade :

| Tapez | Nom | Exemple |
| ---------- | ---------- | ---------------- |
| `int` | Entier | `10`, `-3`, `0` |
| `float` | Décimal | `3.14`, `-0.5` |
| `str` | Chaîne (texte) | `"Olá"`, `"123"` |
| `bool` | Booléen | `True`, `False` |
| `NoneType` | Valeur « aucun » | `None` |

### 4.1. Afficher le type d'une valeur

La fonction `type()` renvoie le type d'une valeur ou d'une variable.

```python
nombre = 10
texte = "Python"
vrai = True

print(type(nombre))     # <classe 'int'>
print(type(texte))      # <classe 'str'>
print(type(vrai)) # <classe 'bool'>
```

### 4.2. Conversions de types (casting)

Parfois, vous devez effectuer une conversion entre les types :

```python
# De la chaîne à l'int/float
age_str = "16"
age_entier = int(age_str)         # 16 (int)

hauteur_str = "1,75"
hauteur_du_flotteur = float(hauteur_str)   # 1,75 (flotteur)

# Du nombre à la chaîne
dans_un = 123
num_str = str(dans_un)                 # "123"

# Pour booléen (bool)
print(bool(0))       # FAUX
print(bool(1))       # Vrai
print(bool(""))      # Faux (chaîne vide)
print(bool("x"))     # Vrai (chaîne non vide)
```

**Règle importante :** 
`input()` renvoie TOUJOURS un `str`.  
Si vous souhaitez travailler avec des nombres, vous devez presque toujours les convertir.

---

## 5. Chaînes (texte)

Une **chaîne** est une séquence de caractères : lettres, chiffres, espaces, symboles.

```python
phrase = "Bonjour le monde"
mot = 'Python'   # travail entre guillemets simples ou doubles
```

### 5.1. Indexation (accès à un caractère)

Les caractères sont numérotés à partir de **0**.

```python
texte = "Python"

d_abord = texte[0]   # "P"
deuxieme  = texte[1]   # "oui"
dernier   = texte[-1]  # "n" (l'index négatif compte à partir de la fin)

print(d_abord, deuxieme, dernier)
```

Si vous essayez d'accéder à un index qui n'existe pas, cela renvoie une erreur (`IndexError`).

### 5.2. Tranchage (tranchage de chaînes)

Vous pouvez prendre des « tranches » à partir de la chaîne : `texto[inicio:fim]` (extrémité non incluse).

```python
s = "Calendrier"

tranche1 = s[0:7]    # "Programme"
tranche2 = s[2:7]    # "gramme"
tranche3 = s[4:]     # de l'index 4 à la fin -> "branche"
tranche4 = s[:4]     # du début à l'index 3 -> "Prog"
inverse = s[::-1]  # chaîne inversée

print(tranche1)
print(inverse)
```

### 5.3. Les chaînes sont immuables

Vous ne pouvez pas modifier directement un caractère :

```python
nom = "Nain"
# nom[0] = "J" # ERREUR ! (Erreur de type)

# Au lieu de cela, vous créez une nouvelle chaîne :
nouveau_nom = "J." + nom[1:]   # "Jna"
```

Chaque fois que vous « modifiez » une chaîne, vous en créez une nouvelle.

### 5.4. Méthodes de chaîne utiles

Quelques méthodes couramment utilisées :

```python
s = "  Bonjour le monde  "

s_bande   = s.strip()           # supprimer les espaces au début et à la fin
ralentissez   = s_bande.lower()     # "Bonjour le monde"
souper   = s_bande.upper()     # "BONJOUR LE MONDE"
il_y_a_un_monde = "Monde" in s        # Vrai (en opérateur)

phrase = "un deux trois"
mots = phrase.split()        # ["un deux trois"]

articulations = "-".join(["le", "b", "w"])  # "ABC"

print(len(s))        # longueur de la chaîne (comprend les espaces)
print(len(s_bande))  # longueur sans espaces de fin
```

Liste des méthodes à connaître à ce stade (ne pas tout mémoriser, mais vous savez ce qu'elles font en général) :

- `strip()`, `lstrip()`, `rstrip()`
- `lower()`, `upper()`, `capitalize()`
- `replace(antigo, novo)`
- `split(separador)`
- `join(lista_de_strings)`
- `startswith(...)`, `endswith(...)`

---

## 6. Commentaires

Les commentaires sont utilisés pour **expliquer le code**, les deux pour vous comme pour les autres (et pour le « vous futur »).

- En Python, un commentaire de ligne commence par `#`.
- Tout ce qui se trouve après `#` sur la ligne est ignoré par l'interprète.

```python
# Ce programme imprime un message d'accueil simple
nom = "Nain"               # enregistrer le nom de la personne
print("Bonjour,", nom)        # montre "Bonjour Ana"
```

Plus tard, nous examinerons les **docstrings**, qui sont des « commentaires spéciaux » utilisés pour documenter les fonctions et les modules.

---

## 7. Entrée et sortie : `print()` et `input()`

### 7.1. `print()` - afficher les informations

La fonction `print()` écrit du texte sur l'écran.

```python
cours = "PI 10ème"
annee = 2025

print("Bienvenue au cours", cours)
print("Année scolaire:", annee)
```

Vous pouvez joindre des valeurs avec des virgules (Python met un espace entre elles par défaut) ou utiliser des **f-strings** (voir ci-dessous).

### 7.2. `input()` - ​​​​​​lire les informations

La fonction `input()` affiche un message (facultatif) et **lit une ligne de texte** écrite par l'utilisateur.  
Le résultat est toujours un `str`.

```python
nom = input("Quel est ton nom? ")      # lit le texte
age_txt = input("Âge? ")          # c'est toujours de la ficelle !

print("tapez âge_txt :", type(age_txt))   # <classe 'str'>
```

Si vous souhaitez travailler avec l'âge sous forme de nombre (pour additionner, comparer, etc.), vous devez convertir :

```python
age = int(age_txt)        # convertir une chaîne en entier
print("Dans 5 ans tu auras", age + 5, "années.")
```

Vous pouvez également convertir directement dans `input()` :

```python
age = int(input("Âge? "))
hauteur = float(input("Hauteur en mètres ? "))

print("Type d'âge :", type(age))   # int
print("Type de hauteur :", type(hauteur)) # flotter
```

### 7.3. Les f-strings (interpolation et formatage)

**f-strings** facilitent la construction de phrases avec des variables à l'intérieur.

- Vous écrivez une chaîne qui commence par `f` ou `F`.
- À l'intérieur du `{}`, vous mettez le nom de la variable ou une expression.

```python
nom = "Béatrice"
avis = 17.375

message_2 = f"Étudiant : {nom} | Remarque : {avis:.2f}"
print(message_2)  # "Étudiante : Beatriz | Note : 17,38"
```

Dans l'expression `{nota:.2f}` :

- `:.2f` signifie « format sous forme de nombre décimal à 2 places ».

Plus d'exemples :

```python
x = 5
y = 3

print(f"{x} + {y} = ​​​​ {x + y}")      # "5 + 3 = 8"

prix = 12.5
print(f"Prix ​​: {prix:.1f} €")     # "Prix : 12,5€"

nom = "nain"
print(f"Nom formaté : {nom.capitalize()}")
```

---

## 8. Exercices (Introduction, Variables, Types, Chaînes, E/S)

> Suggestion : copiez chaque exercice dans un fichier `.py` et résolvez-le.  
> Essayez d'abord **sans regarder la solution**. Ensuite seulement, comparez-le avec la correction.

### Exercice 1 - Données de base de l'élève

Créez un programme qui :

1. Enregistrez vos `nome`, `idade` et `curso` (en texte) dans des variables.
2. Affiche un message comme :

```
    Olá, eu sou a/o <nome>, tenho <idade> anos e estou no curso <curso>.
    ```

Vous pouvez utiliser `print()` normal ou une f-string.

> Résolution :

```python
nom = "Votre nom"
age = 16
cours = "PI 10ème"
print(f"Bonjour, je m'appelle {nom}, j'ai {age} ans et je suis au cours {cours}.")
```

---

### Exercice 2 - Types de données

Écrivez un programme qui :

1. Crée les variables suivantes :

```python
    age = 16
    hauteur = 1.70
    nom = "John"
    approuve = False
```

2. Utilisez `type()` pour imprimer le type de chaque variable.
3. A la fin, écrivez une phrase :

```text
    A variável idade é do tipo ...
    ```

(Complétez avec le type correct dans le texte.)

> Résolution :

```python
age = 16
hauteur = 1.70
nom = "John"
approuve = False

print(f"La variable âge est de type {type(age)}")
print(f"La variable de hauteur est de type {type(hauteur)}")
print(f"La variable nom est de type {type(nom)}")
print(f"La variable approuvée est de type {type(approuve)}")
```

---

### Exercice 3 - Conversion d'entrée

Écrivez un programme qui :

1.  Demande à l'utilisateur son âge (avec `input()`).
2.  Convertissez cet âge en `int`.
3.  Calcule quel âge aura la personne dans 10 ans.
4.  Affiche une phrase utilisant une f-string, par exemple :

```
        Daqui a 10 anos terás 25 anos.
        ```

 > Résolution :

```python
age_str = input("Quel âge avez-vous? ")
age = int(age_str)
age_futur = age + 10
print(f"Dans 10 ans, vous aurez {age_futur} ans.")
```

---

### Exercice 4 - Longueur d'un mot

Créez un programme qui :

1. Demande un mot à l'utilisateur.
2. Affiche le premier et le dernier caractère du mot.
3. Affiche le nombre de caractères du mot en utilisant `len()`.

> Résolution :

```python
mot = input("Écrivez un mot : ")
print("Premier personnage :", mot[0])
print("Dernier personnage :", mot[-1])
print("Nombre de caractères :", len(mot))
```

---

### Exercice 5 - Lettres de cas

Écrire un programme qui :

1. Demande à l'utilisateur une phrase.
2. Affiche la phrase :
 - tout en majuscules,
 - tout en minuscules,
 - avec seulement la première lettre en majuscule (`capitalize()`).

> Résolution :

```python
phrase = input("Écrivez une phrase : ")
print("Lettres majuscules :", phrase.upper())
print("Minuscule:", phrase.lower())
print("En majuscule :", phrase.capitalize())
```

---

### Exercice 6 - Effacer les espaces

Créez un programme qui :

1. Il demande à l'utilisateur d'écrire une phrase, mais **à dessein** avec des espaces supplémentaires au début et à la fin.
2. Affiche :
 - la longueur de la phrase originale (`len()`),
 - la phrase sans espaces aux extrémités (`strip()`),
 - la longueur de la phrase après `strip()`.

> Résolution :

```python
phrase = input("Écrivez une phrase avec des espaces au début et à la fin : ")
print("Longueur d'origine :", len(phrase))
phrase_propre = phrase.strip()
print("Phrase sans espaces :", phrase_propre)
print("Longueur sans espaces :", len(phrase_propre))
```

---

### Exercice 7 - Rechercher une lettre dans le mot

Écrivez un programme qui :

1. Demande un mot à l'utilisateur.
2. Demande une lettre à l'utilisateur.
3. Indique si la lettre apparaît ou non dans le mot, à l'aide de l'opérateur `in`.

Exemple de sortie :

```text
A letra "a" existe na palavra "banana".
```

ou

```text
A letra "x" não existe na palavra "banana".
```

> Résolution :

```python
mot = input("Écrivez un mot : ")
lettre = input("Écrire une lettre: ")
existe = lettre in mot
print(f'La lettre "{lettre}" {"existe" if existe else "não existe"} dans le mot "{mot}".')
```

---

### Exercice 8 - Conversion de température

Créez un programme qui :

1. Demande à l'utilisateur une température en degrés Celsius (peut être décimal).
2. Convertit cette valeur en `float`.
3. Convertissez en Fahrenheit en utilisant la formule :

 \[
 F = C imes 9/5 + 32
 \]

4. Affiche un message avec **2 décimales** dans la température en degrés Fahrenheit.

> Résolution :

```python
degres_celsius = input("Température en Celsius : ")
celsius = float(degres_celsius)
degres_fahrenheit = celsius * 9/5 + 32
print(f"Température en degrés Fahrenheit : {degres_fahrenheit:.2f} °F")
```

---

### Exercice 9 - Valeurs « vides » et `bool()`

Écrire un programme qui :

1. Crée les variables suivantes :

```python
    a = 0
    b = ""
    c = []
    d = "Python"
    e = 123
```

2. Utilisez `bool()` dans chacun et imprimez le résultat, par exemple :

```text
    bool(a) -> False
    ```

3. A la fin, écrivez un petit commentaire (en texte, dans un `print` ou dans un commentaire) expliquant quelles valeurs sont considérées comme `False` en Python.

> Résolution :

```python
a = 0
b = ""
c = []
d = "Python"
e = 123
print(f"bool(a) -> {bool(a)}")
print(f"bool(b) -> {bool(b)}")
print(f"bool(c) -> {bool(c)}")
print(f"bool(d) -> {bool(d)}")
print(f"bool(e) -> {bool(e)}")
# En Python, les valeurs comme 0, chaîne vide "", liste vide [], None sont considérées comme False.
```

---

### Exercice 10 - Questionnaire simple

Créez un petit « questionnaire » dans lequel le programme demande à l'utilisateur :

- nom,
- ville où vous habitez,
- langage de programmation favori.

Ensuite, il affiche une phrase organisée, en utilisant une f-string, par exemple :

```text
Olá, eu sou a/o <nome>, vivo em <cidade> e a minha linguagem favorita é <linguagem>.
```

> Résolution :

```python
nom = input("Quel est ton nom? ")
ville = input("Où  habites-tu? ")
langue = input("Quel est votre langage de programmation préféré ? ")
print(f"Bonjour, je m'appelle {nom}, j'habite à {ville} et ma langue préférée est {langue}.")
```

---

### Exercice 11 (Défi) - Formater une « carte d'étudiant »

Créez un programme qui :

1. Il demande à l'utilisateur :
 - nom,
 - âge,
 - classe,
 - moyenne (en float).
2. Utilisez des f-strings pour afficher quelque chose comme ceci :

```text
    =========================
        CARTÃO DE ALUNO
    =========================
    Nome : Ana Silva
    Idade: 16 anos
    Turma: 10.º PI
    Média: 15.75 valores
    =========================
    ```

Vous pouvez utiliser `
` pour les sauts de ligne et, si vous le souhaitez, le formatage avec des décimales au milieu (`{media:.2f}`).

> Résolution :

```python
nom = input("Nom: ")
age = int(input("Âge: "))
classe = input("Classe: ")
moyenne = float(input("Moyenne: "))
print(f"""=========================
 CARTE ÉTUDIANT
========================
Nom : {nom}
Âge : {age} ans
Classe : {classe}
Moyenne : {moyenne:.2f} valeurs
=========================""")
```

---

## 9. Journal des modifications

> Enregistrement des modifications importantes apportées à ce fichier.

- **2025-11-17 · v1.2**
 - Ajout de solutions à tous les exercices.
- **2025-11-17 · v1.1**
 - Table des matières mise à jour.
- **2025-11-17 · v1.0**
 - Création initiale du document.
 - Sections : introduction, variables, types de base, chaînes, commentaires, `print()`/`input()` et f-strings.
 - Ajout de 12 exercices notés (niveau : 10e année, première unité Python).
