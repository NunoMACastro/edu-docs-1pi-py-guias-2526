# Python (10e année) - 02 · Opérateurs et contrôle de flux (`if`, `for`, `while`)

> **Objectif de ce fichier** 
> Pour vous donner le « moteur » de la logique en Python : apprendre à utiliser les opérateurs, prendre des décisions avec `if/elif/else` et répéter des actions avec `while` et `for`.

---

## Index

- [0. Comment utiliser ce fichier](#0-comment-utiliser-ce-fichier)
- [1. Opérateurs arithmétiques](#1-operateurs-arithmetiques)
- [2. Opérateurs de comparaison](#2-operateurs-de-comparaison)
- [3. Opérateurs logiques (`and`, `or`, `not`)](#3-operateurs-logiques-and-or-not)
- [4. Opérateurs d'adhésion et d'identité](#4-operateurs-dadhesion-et-didentite)
- [5. Travaux composés (`+=`, `-=`, ...)](#5-travaux-composes-)
- [6. Véracité (ce qui est considéré comme « vrai » ou « faux »)](#6-veracite-ce-qui-est-considere-comme-vrai-ou-faux)
- [7. Structures de sélection : `if`, `elif`, `else`](#7-structures-de-selection-if-elif-else)
- [8. Cycle `while` - répéter tant que la condition est vraie](#8-cycle-while-repeter-tant-que-la-condition-est-vraie)
- [9. Cycle `for` - parcourir les séquences](#9-cycle-for-parcourir-les-sequences)
- [10. `range()` - générer des séquences de nombres](#10-range-generer-des-sequences-de-nombres)
- [11. Blocs de code et indentation](#11-blocs-de-code-et-indentation)
- [12. Exercices (Opérateurs, `if`, `for`, `while`)](#12-exercices-operateurs-if-for-while)
- [13. Changelog](#13-changelog)

---

## 0. Comment utiliser ce fichier

1. Lisez calmement l'explication théorique.
2. Analysez les exemples et essayez de **prédire le résultat avant** de les exécuter.
3. Reproduisez les exemples dans un fichier `.py` et apportez de petites modifications à l'expérimentation.
4. À la fin, résolvez les **exercices** (10 à 12), en commençant par les plus faciles.

Ce fichier continue ce que vous avez vu dans :

- `01_introduction_variables_types_strings_io.md` (variables, types, chaînes, `print`, `input`).

---

## 1. Opérateurs arithmétiques

En Python, les opérateurs arithmétiques de base sont :

| Opérateur | Signification | Exemple | Résultat |
| -------- | -------------------- | -------- | --------- |
| `+` | ajout | `7 + 3` | `10` |
| `-` | soustraction | `7 - 3` | `4` |
| `*` | multiplications | `7 * 3` | `21` |
| `/` | division réelle (flottant) | `7 / 3` | `2.3333…` |
| `//` | division entière | `7 // 3` | `2` |
| `%` | reste de la division entière | `7 % 3` | `1` |
| `**` | puissance | `2 ** 3` | `8` |

### 1.1. Différence entre `/` et `//`

- `/` renvoie toujours une `float` (division « réelle »).
- `//` effectue une division entière, **en supprimant** la partie décimale.

```python
a = 7
b = 3

vrai_div = a / b     # 2.3333333333...
int_div  = a // b    # 2

print(vrai_div)
print(int_div)
```

### 1.2. Reste (`%`) et parité

L'opérateur `%` (modulo) renvoie le reste de la division entière.

```python
print(7 % 3)   # 1 (7 = 2*3 + 1)
print(10 % 2)  # 0 (10 est un multiple de 2)
print(11 % 2)  # 1
```

Ceci est souvent utilisé pour savoir si un nombre est **pair** ou **impair** :

```python
n = 10

if n % 2 == 0:
    print("Paire")
else:
    print("Impair")
```

### 1.3. Alimentation (`**`)

L'opérateur `**` alimente :

```python
print(2 ** 3)   # 8
print(5 ** 2)   # 25
print(9 ** 0.5) # 3.0 (racine carrée, soyez prudent avec les flotteurs)
```

---

## 2. Opérateurs de comparaison

Les comparateurs permettent de demander « est-ce égal ? », « est-il plus grand ? », « est-il plus petit ? », etc. 
Ils donnent toujours `bool` : `True` ou `False`.

| Opérateur | Signification |
| -------- | -------------- |
| `==` | égal à |
| `!=` | autre que |
| `>` | supérieur à |
| `>=` | supérieur ou égal |
| `<` | inférieur à |
| `<=` | inférieur ou égal |

Exemples :

```python
a = 7
b = 3

print(a == b)   # FAUX
print(a != b)   # Vrai
print(a > b)    # Vrai
print(a <= 10)  # Vrai
```

### 2.1. Chaînage de comparaisons

Python permet d'écrire des comparaisons chaînées de manière naturelle :

```python
x = 7

print(1 < x < 10)      # Vrai (1 < x et x < 10)
print(1 < x <= 7)      # Vrai
print(10 < x < 20)     # FAUX
```

Ceci est très utile, par exemple, pour les tranches de notes ou les âges.

---

## 3. Opérateurs logiques (`and`, `or`, `not`)

Les opérateurs logiques se combinent conditions.

- `and` - vrai si **les deux** conditions sont vraies.
- `or` - vrai si **au moins une** condition est vraie.
- `not` - inverse la valeur logique (Vrai → Faux, Faux → Vrai).

### 3.1. Tables de vérité simples

Avec `True` et `False` :

| Un | B | `A and B` | `A or B` |
| ----- | ----- | --------- | -------- |
| Vrai | Vrai | Vrai | Vrai |
| Vrai | Faux | Faux | Vrai |
| Faux | Vrai | Faux | Vrai |
| Faux | Faux | Faux | Faux |

`not`:

| Un | `not A` |
| ----- | ------- |
| Vrai | Faux |
| Faux | True |

Exemple combiné :

```python
age = 20
avoir_une_lettre = True

peut_conduire = age >= 18 and avoir_une_lettre
print(peut_conduire)   # Vrai si les deux conditions sont vraies
```

### 3.2. « Court-circuit »

Python **arrête d'évaluer** dès qu'il connaît le résultat :

- Dans `and`, si la première partie est `False`, vous n'avez pas besoin de voir le reste.
- Dans `or`, si la première partie est `True`, vous n'avez pas besoin de voir le reste. non plus. vous devez voir le reste.

Exemple illustratif :

```python
def dire_bonjour():
    print("La fonction say_hello a été appelée !")
    return True

print(False and dire_bonjour())   # ça n'appelle pas diz_hello (tu sais déjà que c'est False)
print(True or dire_bonjour())     # N'appelle pas diz_hello (tu sais déjà que c'est vrai)
```

Ceci est important lorsque la deuxième condition est « coûteuse » (ou peut donner une erreur) - vous pouvez utiliser la première condition comme « filtre ».

---

## 4. Opérateurs d'adhésion et d'identité

### 4.1. Appartenance : `in` et `not in`

Utilisé pour tester si un élément se trouve dans une séquence (chaîne, liste, etc.) ou dans les clés d'un dictionnaire.

```python
# En chaînes
print("py" in "python")       # Vrai
print("z" in "python")        # FAUX

# Dans les listes
nombres = [1, 2, 3, 4]
print(3 in nombres)           # Vrai
print(5 not in nombres)       # Vrai

# Dans les dictionnaires (test KEYS)
etudiant = {"nom": "Nain", "âge": 16}
print("nom" in etudiant)        # Vrai
print("Nain" in etudiant)         # Faux (valeur, pas clé)
```

### 4.2. Identité : `is` et `is not`

- `==` compare les **valeurs**.
- `is` compare s'il s'agit du **même objet en mémoire** (identité).

En 10e année, l'utilisation la plus importante est avec `None` :

```python
x = None

if x is None:
    print("x n'a toujours aucune valeur utile")
else:
    print("x a une certaine valeur")
```

Règle générale pour l'instant :

- Pour comparer avec `None`, utilisez `is None` ou `is not None`.
- Pour comparer des valeurs (nombres, chaînes, etc.), utilisez `==` / `!=`.

---

## 5. Affectations composites (`+=`, `-=`, ...)

Les affectations composées sont un moyen plus court de mettre à jour les variables.

```python
x = 10

x = x + 1    # forme longue
x += 1       # forme courte (équivalent)

x -= 2       # x = x - 2
x *= 3       # x = x * 3
x /= 2       # x = x / 2
x //= 2      # x = x // 2
x %= 5       # x = x % 5
x **= 2      # x = x ** 2
```

Ils sont souvent utilisés dans les cycles `for`/`while`, par exemple pour ajouter ou compter quelque chose.

---

## 6. Véracité (ce qui est considéré comme « vrai » ou « faux »)

Dans des contextes booléens (`if`, `while`), on n'utilise pas toujours uniquement `True` ou `False`.  
Certaines valeurs comptent automatiquement comme **faux** :

- `0`, `0.0`
- `""` (chaîne vide)
- `[]` (liste vide)
- `{}` (dictionnaire vide)
- `None`

Toutes les autres valeurs comptent comme **true**.

```python
if "":
    print("Cela n'apparaît pas")    # la chaîne vide est fausse
else:
    print("La chaîne vide est traitée comme False")

if [1, 2, 3]:
    print("La liste n'est pas vide")  # la liste avec les éléments est vraie
```

Cela permet d'écrire des conditions plus naturelles :

```python
texte = input("Écrivez quelque chose (ou laissez-le vide) : ")

if texte:
    print("Merci, vous avez écrit :", texte)
else:
    print("Vous n'avez rien écrit.")
```

---

## 7. Structures de sélection : `if`, `elif`, `else`

Elles permettent de prendre des décisions en choisissant un chemin d'exécution en fonction d'une condition.

### 7.1. Structure de base

```python
if etat_principal:
    # bloc 1
    ...
elif une_autre_condition:
    # bloc 2
    ...
else:
    # bloc 3 (sinon)
    ...
```

Exemple avec des notes (0 à 20) :

```python
avis = int(input("Saisissez la note (0-20) : "))

if avis < 0 or avis > 20:
    print("Remarque invalide.")
else:
    if avis >= 18:
        concept = "Excellent"
    elif avis >= 14:
        concept = "Bien"
    elif avis >= 10:
        concept = "Assez"
    else:
        concept = "Insuffisant"

    print("Concept:", concept)
```

Remarquez que nous avons utilisé un `if` **imbriqué** (dans `else`) pour traiter en premier le cas de « note invalide ».

### 7.2. Expression conditionnelle (opérateur ternaire)

Manière plus compacte d'écrire un simple `if/else`.

```python
avis = 15
resultat = "Approuvé" if avis >= 10 else "Échoué"
print(resultat)
```

Il se lit comme suit : "le résultat est `'Aprovado'` **si** `nota >= 10`, sinon `'Reprovado'`".

C'est utile pour les expressions simples, mais n'abusez pas de la logique complexe (c'est difficile à lire).

---

## 8. Cycle `while` - répéter tant que la condition est vraie

Le `while` répète un bloc **tandis que** la condition est `True`.

### 8.1. Structure de base

```python
while condition:
    # bloquer pour répéter
    ...
```

Exemple : compter de 1 à 3 :

```python
i = 1

while i <= 3:
    print(i)
    i += 1   # TRÈS IMPORTANT : mettre à jour la variable
```

Sans mettre à jour `i`, la condition ne cesserait jamais d'être vraie et nous aurions un **cycle infini**.

### 8.2. Exemple : valider la saisie

```python
avis = int(input("Niveau (0-20) : "))

while avis < 0 or avis > 20:
    print("Remarque invalide. Essayer à nouveau.")
    avis = int(input("Niveau (0-20) : "))

print("Remarque acceptée :", avis)
```

Ici, nous utilisons `while` pour répéter jusqu'à ce que la condition « note invalide » ne soit plus vraie.

---

## 9. Cycle `for` - faire défiler les séquences

`for` est idéal pour **traverser des collections** (listes, chaînes, plages).

### 9.1. Structure de base

```python
for element in sequence:
    # utiliser l'élément
    ...
```

Exemples :

```python
# Faire défiler une liste
noms = ["Nain", "Bruno", "Carla"]

for nom in noms:
    print("Bonjour,", nom)

# Parcourir une chaîne
mot = "Python"

for lettre in mot:
    print(lettre)
```

`for` est souvent utilisé avec `range()`, que nous verrons ensuite.

---

## 10. `range()` - génère des séquences numériques

`range()` génère une séquence d'entiers (ce n'est pas une liste, mais se comporte de la même manière dans un `for`).

Formes principales :

- `range(fim)` → 0, 1, 2, ..., fin-1
- `range(inicio, fim)` → début, début+1, ..., fin-1
- `range(inicio, fim, passo)` → séquence avec l'étape indiquée (peut être négatif)

Exemples :

```python
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 7)))       # [2, 3, 4, 5, 6]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]
```

Utilisé avec `for` :

```python
# Ajouter des nombres de 1 à 100
somme = 0
for i in range(1, 101):    # 1, 2, ..., 100
    somme += i

print("Somme =", somme)
```

Parcourir la liste par index :

```python
noms = ["Nain", "Bruno", "Carla"]

for i in range(len(noms)):      # 0, 1, 2
    print(i, noms[i])
```

---

## 11. Blocs de code et indentation

Dans de nombreuses langues, `{}` est utilisé pour délimiter les blocs.  
En Python, les blocs sont définis par **indentation** (espaces en début de ligne).

### 11.1. Règles importantes

- Utiliser **4 espaces** par niveau d'indentation ou une TAB (ne pas utiliser de TAB mélangée avec des espaces).
- Toutes les lignes avec la même indentation appartiennent au même bloc.
- Les deux points `:` indiquent qu'il y a ensuite un bloc (`if`, `elif`, `else`, `for`, `while`, `def`, etc.).
- Tout ce qui vient après les deux points appartient au bloc, jusqu'à ce que vous reveniez à l'indentation précédente.

Exemple avec `if/else` :

```python
x = 12

if x > 10:
    # c'est le bloc if
    print("supérieur à 10")
else:
    # c'est le bloc else
    print("10 ou moins")
print("Fin de la vérification")  # déjà en dehors de if/else (sans indentation)
```

Exemple avec `while` :

```python
comptoir = 0

while comptoir < 3:
    print("Comptoir:", comptoir)
    comptoir += 1   # toujours à l'intérieur du bloc do while

print("Fin de cycle")  # déjà hors du cycle (sans indentation)
```

Si l'indentation est incorrecte, Python donnera des erreurs (`IndentationError`) ou, pire encore, le programme fera quelque chose d'inattendu.

---

## 12. Exercices (Opérateurs, `if`, `for`, `while`)

> Essayez d'abord sans regarder les solutions précédentes.  
> Certains exercices sont des versions reformulées de ceux que vous avez déjà fait, mais maintenant ils sont regroupés par thème.

### Exercice 1 - Positif, négatif ou zéro

Lit un entier de l'utilisateur et dit s'il est :

- "positif",
- « négatif »,
- ou « zéro ».

Utilisez `if/elif/else`.

> Résolution :

```python
dans_un = int(input("Écrivez un entier : "))
if dans_un > 0:
    print("Positif")
elif dans_un < 0:
    print("Négatif")
else:
    print("Zéro")
```

---

### Exercice 2 - Positif et pair / impair

Demande un nombre à l'utilisateur. Si le nombre est **positif** :

- indique s'il est **pair** ou **impair** (utilise `%`).

S'il n'est pas positif, écrit un message indiquant que le numéro n'est pas valide pour ce contrôle.

> Résolution :

```python
dans_un = int(input("Écrivez un entier : "))
if dans_un > 0:
    if dans_un % 2 == 0:
        print("Positif et égal")
    else:
        print("Positif et étrange")
else:
    print("Le nombre n'est pas positif.")
```

---

### Exercice 3 - Classification des notes (0-20)

Lit une note entière entre 0 et 20.

1. Si la note n'est pas valide (hors plage), un message d'erreur s'affiche.
2. Si valide, écrire :

 - "Excellent" (≥ 18)
 - "Bon" (14-17)
 - "Suffisant" (10-13)
 - "Insuffisant" (< 10)

Utiliser `if/elif/else`.

> Résolution :

```python
valeur = int(input("Saisissez la note (0-20) : "))
if valeur < 0 or valeur > 20:
    print("Remarque invalide.")
else:
    if valeur >= 18:
        avis = "Excellent"
    elif valeur >= 14:
        avis = "Bien"
    elif valeur >= 10:
        avis = "Assez"
    else:
        avis = "Insuffisant"
    print("Avis:", avis)
```

---

### Exercice 4 - Le plus petit des trois nombres (sans `min()`)

Demande 3 nombres (peut être `float`) à l'utilisateur et, **sans utiliser** la fonction `min()`, imprime ce que le le plus petit.

Conseil : commencez par supposer que le premier est le plus petit et comparez-le avec les autres.

> Résolution :

```python
a = float(input("Écrivez le 1er chiffre : "))
b = float(input("Écrivez le 2ème nombre : "))
c = float(input("Écrivez le 3ème nombre : "))

plus_petit = a
if b < plus_petit:
    plus_petit = b
if c < plus_petit:
    plus_petit = c

print("Le plus petit nombre est :", plus_petit)
```

---

### Exercice 5 - Nombre dans une plage

Lit un entier et dit s'il est compris entre 5 et 15 (inclus).

Vérifie de deux manières :

1. En utilisant `if num >= 5 and num <= 15`.
2. Utilisation de la comparaison chaînée `if 5 <= num <= 15`.

> Résolution :

```python
dans_un = int(input("Écrivez un entier : "))

# Méthode 1
if dans_un >= 5 and dans_un <= 15:
    print("C'est entre 5 et 15 (méthode 1)")
else:
    print("Pas entre 5 et 15 (méthode 1)")

# Méthode 2
if 5 <= dans_un <= 15:
    print("C'est entre 5 et 15 (méthode 2)")
else:
    print("Pas entre 5 et 15 (méthode 2)")
```

---

### Exercice 6 - Même signe

Lit deux entiers et indique si :

- ils ont le **même signe** (tous deux ≥ 0 ou les deux < 0),
- ou s'ils ont **signes différent**.

Utilise des opérateurs logiques (`and`, `or`).

> Résolution :

```python
a = int(input("Écrivez le 1er entier : "))
b = int(input("Écrivez le 2ème entier : "))

if (a >= 0 and b >= 0) or (a < 0 and b < 0):
    print("Ils ont le même signal.")
else:
    print("Ils ont des signes différents.")
```

---

### Exercice 7 - Décompte

Demande à l'utilisateur un nombre entier.

S'il est supérieur à 1, décompte ce nombre jusqu'à 0 :

- 1ère version : utilise un cycle `for` avec `range()`.
- 2ème version : utilise un cycle `while`.

Si le nombre n'est pas supérieur à 1, il affiche un message d'erreur.

> Résolution :

```python
n = int(input("Écrit un entier supérieur à 1 : "))
if n > 1:
    # Version avec pour
    print("Compte à rebours (pour) :")
    for i in range(n, -1, -1):
        print(i)

    # Version avec while
    print("Compte à rebours (pendant) :")
    comptoir = n
    while comptoir >= 0:
        print(comptoir)
        comptoir -= 1
else:
    print("Erreur : le nombre n'est pas supérieur à 1.")
```

---

### Exercice 8 - Somme de 1 à `n`

Demande un entier **positif** `n` à l'utilisateur.

Si valide :

1. Calcule la somme `1 + 2 + ... + n` à l'aide d'un cycle `for`.
2. Affiche le résultat.

S'il n'est pas positif, il affiche un message d'erreur.

> Astuce : utilisez `range(1, n + 1)`.

> Résolution :

```python
n = int(input("Écrivez un entier positif : "))
if n > 0:
    somme = 0
    for i in range(1, n + 1):
        somme += i
    print("La somme de 1 à", n, "et:", somme)
else:
    print("Erreur : le nombre n'est pas positif.")
```

---

### Exercice 9 - Table de multiplication

Demande à l'utilisateur un nombre entier et affiche la table de multiplication de ce nombre de 1 à 10, par exemple :

```text
Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

Utilise un cycle `for`.

> Résolution :

```python
dans_un = int(input("Écrivez un entier pour voir la table de multiplication : "))
print("table de multiplication", dans_un, ":")
for i in range(1, 11):
    print(f"{dans_un} x {i} = ​​​​ {dans_un * i}")
```

---

### Exercice 10 - Jeu de nombres aléatoires (max. 5 tentatives)

Utilisation du module `random`:

1. Génère un entier aléatoire compris entre 1 et 100.
2. Donne à l'utilisateur **un maximum de 5 tentatives** pour deviner.
3. À chaque tentative, il indique si la supposition est « plus grande » ou « plus petite » que le numéro secret.
4. Si l'utilisateur réussit, il affiche un message de félicitations avec le nombre de tentatives utilisées.
5. Si vous manquez de 5 tentatives, révélez le nombre.

Utilisez un cycle `while` pour contrôler le nombre de tentatives.

> Résolution :

```python
import random

numero_secret = random.randint(1, 100)
tentatives = 0
tentatives_maximales = 5
print("Vous disposez de 5 tentatives pour deviner le nombre compris entre 1 et 100.")

while tentatives < tentatives_maximales:
    deviner = int(input("Écrivez votre supposition : "))
    tentatives += 1

    if deviner == numero_secret:
        print(f"Félicitations! Vous avez deviné le nombre en {tentatives} essais.")
        break
    elif deviner < numero_secret:
        print("Le nombre est plus grand.")
    else:
        print("Le nombre est plus petit.")
else:
    print(f"Fin des tentatives ! Le numéro était {numero_secret}.")
```

---

### Exercice 11 - Somme des multiples de 3

Utiliser un cycle `for` avec `range()` pour :

1. Additionnez tous les multiples de 3 entre 1 et 100 (inclus).
2. Afficher le résultat final.

> Astuce : vous pouvez utiliser `if i % 3 == 0` dans le cycle, ou commencer à 3 et utiliser un pas de 3 : `range(3, 101, 3)`.

> Résolution :

```python
somme = 0
for i in range(3, 101, 3):  # Commence à 3, va jusqu'à 100, étape 3
    somme += i
print("La somme des multiples de 3 compris entre 1 et 100 est :", somme)
```

---

### Exercice 12 (Défi) - Statistiques de notes

Écrivez un programme qui :

1. Il demande à l'utilisateur des notes entières (0 à 20).
2. Introduire la note `-1` signifie « terminer ».
3. A la fin, le programme doit afficher :
 - le nombre de notes saisies,
 - la moyenne des notes,
 - combien de notes sont **positives** (≥ 10),
 - combien sont **négatives** (< 10).

Règles :

- Ignorer la note `-1` dans les calculs (c'est juste le stop).
- Si l'utilisateur écrit toutes les notes invalides (ou se retrouve sans notes valides), traitez ce cas (par exemple, n'essayez pas de diviser par zéro).

Suggestion : utilisez un cycle `while` et cumulez :

- somme des notes,
- notes de compteur,
- compteur positif,
- compteur négatif.

> Résolution :

```python
ajoute_des_notes = 0
contre_notes = 0
compteur_positif = 0
compteur_negatif = 0

while True:
    avis = int(input("Écrivez une note (0-20) ou -1 pour terminer : "))
    if avis == -1:
        break
    if 0 <= avis <= 20:
        ajoute_des_notes += avis
        contre_notes += 1
        if avis >= 10:
            compteur_positif += 1
        else:
            compteur_negatif += 1
    else:
        print("Note invalide, réessayez.")
if contre_notes > 0:
    moyenne = ajoute_des_notes / contre_notes
    print("Nombre de notes saisies :", contre_notes)
    print("Moyenne scolaire :", moyenne)
    print("Nombre de notes positives (≥ 10) :", compteur_positif)
    print("Nombre de notes négatives (< 10) :", compteur_negatif)
else:
    print("Aucune note valide n'a été saisie.")
```

---

## 13. Journal des modifications

> Enregistrement des modifications importantes apportées à ce fichier.

- **2025-11-17 · v1.2**
 - Ajout de solutions à tous les exercices.
- **2025-11-17 · v1.1**
 - Table des matières mise à jour.
- **2025-11-17 · v1.0**
 - Création initiale du document.
 - Sections : opérateurs arithmétiques, comparaison, logique, pertinence/identité, affectations composées, véracité, `if/elif/else`, `while`, `for`, `range` et indentation.
 - Ajout de 12 exercices graduels axés sur les opérateurs, les décisions et les cycles (`for`/`while`).
