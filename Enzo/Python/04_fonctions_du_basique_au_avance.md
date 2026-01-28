# Python (10e année) - 04 · Fonctions de base à « Presque avancées »

> **Objectif de ce dossier** 
> Comprendre ce que sont les fonctions en Python, comment les définir et les utiliser, et donner un premier contact avec des idées un peu plus avancées.

---

## Index

- [0. Guide pour ne pas se perdre](#0-guide-pour-ne-pas-se-perdre)
- [1. Pourquoi utiliser des fonctions ? · [ESSENTIEL]](#1-porque-usar-fun%C3%A7%C3%B5es--essencial)
- [2. Définir et appeler des fonctions · [ESSENTIEL]](#2-definir-e-chamar-fun%C3%A7%C3%B5es--essencial)
- [3. `print` contre `return` · [ESSENTIEL]](#3-print-vs-return--essencial)
- [4. Paramètres et arguments · [ESSENTIEL]](#4-par%C3%A2metros-e-argumentos--essencial)
- [5. `return` en détail · [ESSENTIEL]](#5-return-em-detalhe--essencial)
- [6. Portée (espace de noms) · [ESSENTIEL (notion de base)]](#6-scope-espa%C3%A7o-de-nomes--essencial-no%C3%A7%C3%A3o-b%C3%A1sica)
- [7. Mutabilité et passage d'arguments · [ESSENTIEL]](#7-mutabilidade-e-passagem-de-argumentos--essencial)
- [8. Fonctions d'ordre supérieur et `lambda` · [EXTRA]](#8-fun%C3%A7%C3%B5es-de-ordem-superior-e-lambda--extra)
- [9. `*args` et `**kwargs` · [EXTRA]](#9-args-e-kwargs--extra)
- [10. Docstrings et annotations de type · [EXTRA mais très utile]](#10-docstrings-e-anota%C3%A7%C3%B5es-de-tipo--extra-mas-muito-%C3%BAtil)
- [11. Récursion · [EXTRA / AVANCÉ]](#11-recurs%C3%A3o--extra--avan%C3%A7ado)
- [12. Bonnes pratiques et petits tests · [ESSENTIEL (mindset)]](#12-boas-pr%C3%A1ticas-e-pequenos-testes--essencial-mentalidade)
- [13. Exercices (Fonctions de base à avancées)](#13-exercices-fonctions-de-base-a-avancees)
- [14. Changelog](#14-changelog)

---

## 0. Guide pour ne pas se perdre

C'est là que de nombreux étudiants commencent à « s'éteindre », alors organisons-le comme ceci :

- Les sections marquées **[ESSENTIEL]** → c'est ce dont vous avez VRAIMENT besoin pour les tests et pour la programmation quotidienne.
- Les sections marquées **[EXTRA]** → sont des matières légèrement plus avancées ; Lisez si vous êtes à l'aise, sinon vous pourrez revenir plus tard.

Si vous vous sentez perdu :

1. Concentrez-vous sur les sections **[ESSENTIELS]**.
2. Faites les exemples et **les exercices** pour ces parties.
3. Alors seulement, si possible, explorez le reste.

---

## 1. Pourquoi utiliser des fonctions ? · [ESSENTIEL]

Avant de parler de syntaxe, réfléchissez au problème :

- Sans fonctions, vous avez un énorme fichier `.py`, avec du code répété partout.
- Si vous voulez changer la logique, il faut aller partout pour copier/coller les corrections.
- C'est difficile à tester, difficile à expliquer, difficile maintenir.

Une **fonction** est un « bloc de code nommé » qui :

- prend des données d'entrée (**paramètres**),
- fait quelque chose (calculs, décisions, etc.),
- et renvoie normalement un résultat avec `return`.

Avantages :

- **Éviter les répétitions** : au lieu de copier le code, on appelle la fonction plusieurs fois.
- **Organiser le code** : chaque fonction effectue une tâche bien définie.
- **Faciliter les tests** : il est plus facile de tester une fonction à la fois.

Pensez une fonction comme une **machine** :

- met des valeurs dans l'entrée,
- elle fait le travail,
- renvoie un résultat via la sortie.

---

## 2. Définir et appeler des fonctions · [ESSENTIEL]

### 2.1. Syntaxe de base de `def`

```python
def nom_de_la_fonction_2(parametre1, parametre2):
    # corps de fonction (bloc en retrait)
    ...
    return resultat
```

- `def` → mot réservé pour définir la fonction.
- `nome_da_funcao` → doit expliquer ce que fait la fonction (dans `snake_case`).
- À l'intérieur des parenthèses se trouvent les paramètres (ils peuvent être nuls ou plus).
- Le corps est **en retrait** (4 espaces).
- `return` renvoie le résultat et termine la fonction.

### 2.2. Exemple 1 - fonction très simple

```python
def bonjour_le_monde():
    print("Bonjour le monde!")
```

Appelez la fonction :

```python
bonjour_le_monde()   # exécute le code de fonction
```

### 2.3. Exemple 2 - somme de deux nombres

```python
def somme(a, b):
    resultat = a + b
    return resultat

x = somme(3, 5)      # x devient 8
print(x)
```

### 2.4. Exemple 3 - salutation

```python
def salutation(nom):
    texte = f"Bonjour, {nom} !"
    return texte

phrase = salutation("Nain")
print(phrase)   # "Bonjour Ana!"
```

---

## 3. `print` vs `return` · [ESSENTIEL]

C'est un point où beaucoup de gens sont confus.

- `print(...)` → sert à **afficher** quelque chose à l'écran (présentation).
- `return ...` → sert à **retourner** une valeur à l'endroit où la fonction a été appelée (logique).

Une fonction qui **ne fait que `print`** est difficile à réutiliser dans d'autres fonctions.  
Une fonction qui **renvoie `return`** peut être utilisée dans les comptes, les conditions, etc.

### 3.1. Même exemple, deux versions

version « collée à l'écran » :

```python
def afficher_la_somme(a, b):
    print(a + b)    # ne renvoie rien, montre juste
```

Version réutilisable (meilleure) :

```python
def somme(a, b):
    return a + b

resultat = somme(3, 5)
print("Résultat =", resultat)    # maintenant nous décidons ici si nous le montrons ou non
```

Règle générale :

- Dans les fonctions plus « logiques », vous préférez utiliser `return`.
- Laissez `print` pour la « couche » qui parle à l'utilisateur.

---

## 4. Paramètres et arguments · [ESSENTIEL]

### 4.1. Paramètres vs arguments

- **Paramètres** → les « lieux » définis dans la fonction :

```python
    def somme(a, b):  # a et b sont des paramètres
        return a + b
```

- **Arguments** → les valeurs réelles que vous transmettez lorsque vous appelez la fonction :

```python
    somme(3, 5)       # 3 et 5 sont des arguments
```

### 4.2. Arguments de position

L'ordre compte :

```python
def pouvoir(base, exposant):
    return base ** exposant

print(pouvoir(2, 3))   # 2**3=8
print(pouvoir(3, 2))   # 3 ** 2 = 9 (différent !)
```

### 4.3. Arguments nommés (mots clés)

Vous pouvez indiquer explicitement le nom :

```python
print(pouvoir(base=2, exposant=3))      # 8
print(pouvoir(exposant=3, base=2))      # 8 (l'ordre n'a plus d'importance)
```

Cela rend le code plus clair, surtout lorsqu'il y a de nombreux paramètres.

### 4.4. Valeurs par défaut

Vous permet de rendre certains paramètres **facultatifs**.

```python
def pouvoir(base, exposant=2):   # par défaut, exposant = 2
    return base ** exposant

print(pouvoir(3))            # 3 ** 2 = 9
print(pouvoir(2, 5))         # 2 ** 5 = 32
```

Autre exemple (salutation avec préfixe) :

```python
def salutation(nom, prefixe="Bonjour"):
    return f"{prefixe}, {nom} !"

print(salutation("Nain"))                         # utilisez "Bonjour"
print(salutation("Bruno", prefixe="Accueillir"))  # utilise "Bienvenue"
```

### 4.5. Bonnes pratiques pour les noms de fonctions

- Fonctions → **verbes** dans `snake_case`:
 - `calcular_media`, `contar_vogais`, `obter_idade`.
- Paramètres → noms clairs qui indiquent ce qu'ils représentent :
 - `lista_numeros`, `nome_aluno`, `notas`.

---

## 5. `return` en détail · [ESSENTIEL]

### 5.1. S'il n'y a pas de `return`.

Si une fonction n'a pas de `return` explicite, elle renvoie automatiquement `None`.

```python
def bonjour_le_monde():
    print("Bonjour le monde!")

resultat = bonjour_le_monde()
print(resultat)   # Aucun
```

### 5.2. Renvoyer une valeur

Nous avons déjà vu plusieurs exemples :

```python
def carre(n):
    return n ** 2
```

### 5.3. Renvoie plusieurs valeurs (tuples)

Nous ne pouvons pas renvoyer **deux** valeurs distinctes, mais nous pouvons renvoyer un **tuple** avec deux (ou plus) éléments.

Exemple : quotient et reste d'une division entière :

```python
def diviser(dividende, diviseur):
    quotient = dividende // diviseur
    repos = dividende % diviseur
    return quotient, repos   # c'est un tuple (quotient, reste)

q, r = diviser(17, 5)        # déballer
print("Quotient:", q)
print("Repos:", r)
```

### 5.4. Sortie anticipée (cas particuliers)

Nous pouvons quitter la fonction plus tôt avec `return`.

```python
def division_securisee(a, b):
    if b == 0:
        return None   # cas particulier : non divisible

    return a / b

print(division_securisee(10, 2))   # 5.0
print(division_securisee(10, 0))   # Aucun
```

---

## 6. Portée (espace de noms) · [ESSENTIEL (notion de base)]

« Portée » est le **endroit où « vit » une variable**.

### 6.1. Variables locales

Les variables créées au sein de la fonction sont **locales** : elles n'existent qu'à l'intérieur.

```python
def salutation(nom):
    message_2 = f"Bonjour, {nom} !"   # le message est local
    return message_2

print(salutation("Nain"))
# print(message) # ERREUR : le message n'existe pas ici
```

### 6.2. Variables globales (attention !)

Les variables définies en dehors de toute fonction sont globales.  
Il est **possible** de les changer avec le mot `global`, mais ce n'est pas une bonne pratique d'en abuser.

```python
total_mondial = 0

def s_accumuler_a_l_echelle_mondiale(valeur):
    global total_mondial
    total_mondial += valeur    # changer la variable globale

s_accumuler_a_l_echelle_mondiale(5)
s_accumuler_a_l_echelle_mondiale(7)
print(total_mondial)          # 12
```

Règle générale : 
Préférez renvoyer les valeurs avec `return` et les transmettre comme arguments à d'autres fonctions, au lieu de jouer avec les globaux.

### 6.3. `nonlocal` (curiosité) · [EXTRA]

Pour les fonctions **dans les fonctions** :

```python
def creer_un_compteur(commencer=0):
    comptoir = commencer

    def suivant():
        nonlocal comptoir   # utilise la variable de fonction « extérieur »
        comptoir += 1
        return comptoir

    return suivant

nouvel_identifiant = creer_un_compteur(100)
print(nouvel_identifiant())   # 101
print(nouvel_identifiant())   # 102
```

C'est ce qu'on appelle une **fermeture** ; est utile, mais pas indispensable en 10e année.

---

## 7. Mutabilité et passage d'arguments · [ESSENTIEL]

Quand on passe une variable à une fonction, le comportement dépend du type :

- **types immuables** → `int`, `float`, `str`, `tuple`, etc.
 - Ne peut pas être modifié « à l'intérieur ».
- Types **mutables** → `list`, `dict`, `set`, etc.
 - Peut être modifié par des méthodes telles que `append`, `pop`, etc.

### 7.1. Exemple avec des types immuables

```python
def numero_d_increment(n):
    n = n + 1
    return n

x = 10
y = numero_d_increment(x)
print("X =", x)   # 10
print("y =", y)   # 11
```

La fonction ne modifie pas la valeur de `x` en dehors de la fonction.

### 7.2. Exemple avec des listes (mutables)

```python
def ajouter_un_element(liste, element_2):
    liste.append(element_2)   # change la liste reçue (mutation)

nombres = [1, 2]
ajouter_un_element(nombres, 3)
print(nombres)   # [1, 2, 3]
```

Ici, la fonction modifie la liste d'origine, car elle change l'**objet mutable** vers lequel pointe la variable.

### 7.3. Danger des valeurs par défaut mutables

Exemple **faux** :

```python
def mauvais_accumulateur(valeur, acc=[]):
    acc.append(valeur)
    return acc

print(mauvais_accumulateur(1))   # [1]
print(mauvais_accumulateur(2))   # [1, 2] (suite de la liste précédente !)
print(mauvais_accumulateur(3))   # [1, 2, 3]
```

La liste `[]` est créée **une fois** et réutilisée dans tous les appels sans `acc`.

**Forme correcte** :

```python
def accumulateur_correct(valeur, acc=None):
    if acc is None:
        acc = []      # nouvelle liste
    acc.append(valeur)
    return acc

print(accumulateur_correct(1))           # [1]
print(accumulateur_correct(2))           # [2]
print(accumulateur_correct(3, [10]))     # [10, 3]
```

Règle générale : 
N'utilisez jamais de listes ou de dictionnaires comme valeurs par défaut. Utilisez `None` et créez la liste à l'intérieur de la fonction.

---

## 8. Fonctions d'ordre supérieur et `lambda` · [EXTRA]

> Lisez cette section lorsque vous vous sentez à l'aise avec les parties essentielles.

En Python, les fonctions sont de « 1ère classe citoyens” :

- peut être stocké dans des variables,
- peut être passé en argument,
- peut être renvoyé par d'autres fonctions.

### 8.1. Fonction qui reçoit une autre fonction

```python
def appliquer(fonction, valeur):
    return fonction(valeur)

def double_2(x):
    return 2 * x

print(appliquer(double_2, 7))   # 14
```

### 8.2. `lambda` (fonctions anonymes)

A `lambda` est une manière courte d'écrire des fonctions simples :

```python
double_lambda = lambda x: x * 2
print(double_lambda(5))   # 10

print(appliquer(lambda x: x * 3, 4))   # 12
```

À utiliser avec modération ; pour des fonctions plus complexes, il est préférable d'utiliser `def`.

### 8.3. `map`, `filter`, `sorted(key=...)` vs compréhensions

```python
donnees = [1, 2, 3, 4, 5]

# carte
double = list(map(lambda x: x * 2, donnees))      # [2, 4, 6, 8, 10]

# filtre
paires = list(filter(lambda x: x % 2 == 0, donnees))  # [2, 4]

# trié avec clé
tuples = [("le", 3), ("b", 1), ("w", 2)]
ordonne_2 = sorted(tuples, cle_2=lambda t: t[1])   # trier par 2ème élément
```

Généralement, pour des listes simples, il est plus lisible d'utiliser des **compréhensions** :

```python
comp_double = [x * 2 for x in donnees]
paires_comp = [x for x in donnees if x % 2 == 0]
```

---

## 9. `*args` et `**kwargs` · [EXTRA]

Ils permettent de créer des fonctions avec un nombre variable d'arguments.

### 9.1. `*args` - plusieurs arguments de position

```python
def moyenne(*chiffres):
    if not chiffres:
        return 0.0
    return sum(chiffres) / len(chiffres)

print(moyenne(10, 12, 14))   # 12,0
print(moyenne())             # 0,0
```

### 9.2. `**kwargs` - ​​​​​​plusieurs arguments nommés

```python
def configurer(**choix_2):
    return choix_2

cfg = configurer(deboguer=True, porte=8000)
print(cfg)   # {'debug' : vrai, 'port' : 8000}
```

Déballage sur appel :

```python
valeurs = [10, 20, 30]
choix_2 = {"déboguer": False, "porte": 5000}

print(moyenne(*valeurs))         # 20,0
print(configurer(**choix_2))    # {'debug' : Faux, 'port' : 5000}
```

---

## 10. Docstrings et annotations de type · [EXTRA mais très utile]

### 10.1. Docstrings

Une **docstring** est une chaîne juste après `def` qui explique ce que fait la fonction.

```python
def somme(a, b):
    """Renvoie la somme de a et b."""
    return a + b
```

Dans le REPL, vous pouvez utiliser `help(soma)` pour voir la docstring.

### 10.2. Exemple plus complet avec les types

```python
from dactylographie import sequence_3

def normaliser_les_textes(textes: sequence_3[str]) -> list[str]:
    """
    Normalise une séquence de textes :
 - supprime les espaces aux extrémités
 - convertit en minuscules
 - ignore les chaînes vides après trim

 :param texts : Séquence de chaînes d'entrée.
 :return : Liste des chaînes normalisées et non vides.
    """
    resultat: list[str] = []
    for t in textes:
        norme = t.strip().lower()
        if norme:
            resultat.append(norme)
    return resultat
```

Les **annotations de type** (`-> list[str]`, `textos: Sequence[str]`, etc.) ne sont pas obligatoires, mais :

- rendent le code plus lisible,
- aident l'éditeur (VS Code par exemple) à donner de meilleures suggestions,
- aident à capter certains erreurs.

---

## 11. Récursion · [EXTRA / ADVANCED]

> Vous ne devriez lire cette section que lorsque vous êtes déjà à l'aise avec `while` et `for`.

Une fonction est **récursive** lorsqu'elle s'appelle elle-même propre.

Structure typique :

- **cas de base** → lors de l'arrêt (éviter la récursion infinie),
- **étape récursive** → la fonction est appelée avec un problème plus petit.

### 11.1. Exemple : factorielle

La factorielle de `n` (`n!`) est :

- `0! = 1`
- `n! = n * (n-1)!` à `n > 0`

```python
def factorielle(n):
    if n < 0:
        raise ValueError("n doit être >= 0")
    if n in (0, 1):   # cas de base
        return 1
    return n * factorielle(n - 1)  # étape récursive
```

### 11.2. Exemple : liste décroissante

```python
def compte_decroissant(n):
    if n <= 1:
        return 1
    else:
        print(n)
        return compte_decroissant(n - 1)
```

Avertissements :

- Python a une limite sur la profondeur de récursion ; pour les grands comptes, utilisez `while` ou `for`.
- La récursion est utile dans certains problèmes (arbres, division des problèmes), mais en 10e il est plus important de bien connaître `while` et `for`.

---

## 12. Bonnes pratiques et petits tests · [ESSENTIEL (mentalité)]

Quelques règles qui vous aideront :

- **Fonctions **courtes** et avec **une responsabilité principale**.
- Noms clairs des fonctions et des paramètres.
- Préférez `return` à `print` dans les fonctions logiques.
- Évitez de changer les variables globales ; transmettre des valeurs comme arguments et renvoyer des résultats.
- Évitez les valeurs par défaut mutables (utilisez `None`).
- Écrivez de petits **tests** avec `assert`.

### 12.1. Bloc `if __name__ == "__main__":`

Il est généralement placé à la fin du fichier :

```python
def somme(a, b):
    return a + b

if __name__ == "__principal__":
    # tests rapides (exécutés uniquement si ce fichier est le fichier "principal")
    assert somme(2, 3) == 5
    print("Tout va bien !")
```

- Si vous importez ce fichier dans un autre, le code à l'intérieur de ce `if` ne s'exécute pas automatiquement.
- C'est un bon endroit pour mettre des tests et des démonstrations.

---

## 13. Exercices (Fonctions de base à avancées)

> Commencez par les premiers.  
> Ces derniers peuvent être un peu plus difficiles, surtout s'ils impliquent des dictionnaires ou de la récursion.

### <a id="ex1"></a> Exercice 1 - `ola_mundo`

Créez une fonction `ola_mundo` qui ne prend aucun paramètre et :

- l'affiche à l'écran `"Olá, Mundo!"`.

Ensuite, appelez cette fonction au moins deux fois.

> Résolution

```python
def bonjour_le_monde():
    print("Bonjour le monde!")

bonjour_le_monde()
bonjour_le_monde()
```

---

### <a id="ex2"></a> Exercice 2 - Somme de deux nombres

Créez une fonction `soma(a, b)` qui :

- reçoit deux nombres en paramètres,
- renvoie le sum,
- ne fait pas `print` à l'intérieur de la fonction.

Dans le programme principal, il demande deux nombres à l'utilisateur, appelle la fonction et affiche le résultat.

> Résolution

```python
def somme(a, b):
    return a + b

num1 = float(input("Écrivez le premier nombre : "))
numero2 = float(input("Écrivez le deuxième nombre : "))

resultat = somme(num1, numero2)
print(f"La somme de {num1} et {numero2} est {resultat}.")
```

---

### <a id="ex3"></a> Exercice 3 - Compter les lettres dans un nom

Créez une fonction `contar_letras(nome)` qui :

- reçoit une chaîne `nome`,
- renvoie le nombre de lettres (utilise `len()`).

Dans le programme principal, il demande à l'utilisateur son nom et affiche :

```text
O nome <nome> tem <n> letras.
```

> Résolution

```python
def compter_les_lettres(nom):
    return len(nom)

nom_d_utilisateur = input("Écrivez votre nom : ")
nombre_de_lettres = compter_les_lettres(nom_d_utilisateur)
print(f"Le nom {nom_d_utilisateur} comporte les lettres {nombre_de_lettres} .")
```

---

### <a id="ex4"></a> Exercice 4 - Compter les nombres pairs et impairs dans une liste

Créez une fonction `contar_pares_impares(lista_numeros)` qui :

- reçoit une liste d'entiers,
- renvoie **deux** valeurs : nombre de pairs et nombre d'impairs.

Dans le programme principal, il crée une liste de nombres (par exemple, de 1 à 10) et affiche :

```text
Números pares: X, números ímpares: Y
```

> Résolution

```python
def compter_les_paires_impaires(numeros_de_liste):
    paires = 0
    impair = 0
    for dans_un in numeros_de_liste:
        if dans_un % 2 == 0:
            paires += 1
        else:
            impair += 1
    return paires, impair

nombres = list(range(1, 11))  # Nombres de 1 à 10
en_paire, d_une_maniere_etrange = compter_les_paires_impaires(nombres)
print(f"Nombres pairs : {en_paire}, nombres impairs : {d_une_maniere_etrange}")
```

---

### <a id="ex5"></a> Exercice 5 - Moyenne d'une liste de nombres

Créer une fonction `calcular_media(lista_numeros)` qui :

- reçoit une liste de nombres,
- renvoie le moyenne,
- si la liste est vide, renvoie 0 (pour éviter la division par zéro).

Teste la fonction avec différentes listes (y compris une liste vide).

> Résolution

```python

def calculer_la_moyenne_2(numeros_de_liste):
    if not numeros_de_liste:
        return 0.0
    return sum(numeros_de_liste) / len(numeros_de_liste)

# Essais
print(calculer_la_moyenne_2([10, 20, 30]))  # 20,0
print(calculer_la_moyenne_2([]))             # 0,0
print(calculer_la_moyenne_2([5, 15]))        # 10,0
```

---

### <a id="ex6"></a> Exercice 6 - Somme de 1 à `n`

Créez une fonction `somatorio(n)` qui :

- prend un entier positif `n`,
- renvoie `1 + 2 + ... + n`.

Dans le programme principal, il demande à l'utilisateur `n`, vérifie s'il est positif et:

- si oui, affiche la somme;
- sinon, affiche un message d'erreur.

> Résolution

```python
def somme_2(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i
    return somme

n = int(input("Écrivez un entier positif : "))
if n > 0:
    resultat = somme_2(n)
    print(f"La somme de 1 à {n} est {resultat}.")
else:
    print("Erreur : le nombre doit être positif.")
```

---

### <a id="ex7"></a> Exercice 7 - Chaîne la plus longue

Créez une fonction `string_mais_longa(lista_strings)` qui :

- reçoit une liste de chaînes,
- renvoie la chaîne la plus longue length,
- si la liste est vide, renvoie `None`.

Teste la fonction avec plusieurs listes (par exemple noms de villes, joueurs, etc.).

> Résolution

```python
def chaine_la_plus_longue(lister_les_chaines):
    if not lister_les_chaines: # Liste vide
        return None

    # Si vous arrivez ici, la liste n'est pas vide puisque la précédente a échoué et que le retour n'a pas été exécuté
    le_plus_long = lister_les_chaines[0]
    for s in lister_les_chaines:
        if len(s) > len(le_plus_long):
            le_plus_long = s
    return le_plus_long

# Essais
print(chaine_la_plus_longue(["Lisbonne", "Port", "Faro"]))  # "Lisbonne"
print(chaine_la_plus_longue(["Nain", "Bruno", "Carla"]))    # "Bruno"
print(chaine_la_plus_longue([]))                             # Aucun
```

---

### <a id="ex8"></a> Exercice 8 - Compter les élèves par classe (dictionnaire simple + fonction)

Créez un dictionnaire `turmas` dans lequel :

- les clés sont des noms de classes (ex. : `"10A"`, `"10B"`),
- les valeurs sont des listes de noms d'élèves.

Ensuite, créez une fonction `contar_alunos_por_turma(turmas)` qui :

- reçoit ce dictionnaire,
- renvoie un **nouveau dictionnaire** dans lequel :
 - les clés sont les mêmes classes,
 - les valeurs sont le nombre d'élèves dans chaque classe.

Dans le programme principal, cela ressemble à ceci :

```text
Turma 10A: 3 alunos
Turma 10B: 4 alunos
```

> Résolution

```python
def compter_les_eleves_par_classe(cours_2):
    compter = {}
    for classe, etudiants in cours_2.items():
        compter[classe] = len(etudiants)
    return compter

cours_2 = {
    "10A": ["Nain", "Bruno", "Carla"],
    "10B": ["Diogo", "Veille", "Fabio", "Guide"]
}

compter = compter_les_eleves_par_classe(cours_2)
for classe, chez_des_etudiants in compter.items():
    print(f"Classe {classe} : {chez_des_etudiants} élèves")
```

---

### <a id="ex9"></a> Exercice 9 - Trouver la personne la plus âgée

Créez une fonction `mais_velho(pessoas)` qui reçoit un dictionnaire du type :

```python
personnes = {
    "Nain": 16,
    "Bruno": 17,
    "Carla": 15
}
```

La fonction doit :

- renvoyer le nom de la personne la plus âgée,
- s'il y a plus d'une personne avec l'âge maximum, vous pouvez en renvoyer une (cela n'a pas d'importance).

Tester la fonction avec différents dictionnaires.

> Résolution

```python
def plus_vieux(personnes):
    nom_le_plus_ancien = None
    age_avance = -1
    for nom, age in personnes.items():
        if age > age_avance:
            age_avance = age
            nom_le_plus_ancien = nom
    return nom_le_plus_ancien

# Essais
personnes1 = {"Nain": 16, "Bruno": 17, "Carla": 15}
print(plus_vieux(personnes1))  # "Bruno"

```

---

### Exercice 10 - Moyenne par élève (fonction + dictionnaire imbriqué)

Utilisez un dictionnaire similaire à celui-ci :

```python
classe = {
    "étudiants": [
        {"nom": "Nain", "remarques": {"Mathématiques": 18, "portugais": 16}},
        {"nom": "Bruno", "remarques": {"Mathématiques": 14, "portugais": 15}},
        {"nom": "Carla", "remarques": {"Mathématiques": 12, "portugais": 14}}
    ]
}
```

---

### <a id="ex10"></a> Exercice 10 - Moyenne par élève (fonction + dictionnaire imbriqué)

Créer une fonction `media_aluno(aluno)` qui :

- reçoit un dictionnaire avec `"nome"` et `"notas"` qui est un autre dictionnaire avec les matières et leurs notes respectives,
- renvoie la moyenne des notes de cet élève.

Ensuite, dans le programme principal, il fait défiler la liste des étudiants dans `turma["alunos"]` et affiche :

```text
Ana -> média: X
Bruno -> média: Y
Carla -> média: Z
```

> Résolution

```python
def eleve_moyen(etudiant):
    remarques = etudiant["remarques"].values()
    return sum(remarques) / len(remarques)

classe = {
    "étudiants": [
        {"nom": "Nain", "remarques": {"Mathématiques": 18, "portugais": 16}},
        {"nom": "Bruno", "remarques": {"Mathématiques": 14, "portugais": 15}},
        {"nom": "Carla", "remarques": {"Mathématiques": 12, "portugais": 14}}
    ]
}

for etudiant in classe["étudiants"]:
    nom = etudiant["nom"]
    moyenne = eleve_moyen(etudiant)
    print(f"{nom} -> moyenne : {moyenne:.2f}")
```

---

### <a id="ex11"></a> Exercice 11 - Fonction qui calcule le carré d'un nombre

Crée une fonction `quadrado(n)` qui :

- reçoit un nombre `n`;
- renvoie la valeur de `n` au carré (`n ** 2`).

Dans le programme principal :

1. Demande un numéro à l'utilisateur (avec `input` et `int` ou `float`);
2. Appelle la fonction ;
3. Affiche le résultat à l'utilisateur.

> Résolution

```python
def carre(n):
    return n ** 2

dans_un = float(input("Écrivez un nombre : "))
resultat = carre(dans_un)
print(f"Le carré de {dans_un} est {resultat}.")
```

---

### <a id="ex12"></a> Exercice 12 - Fonction qui indique si un nombre est pair

Créez une fonction `eh_par(n)` qui :

- reçoit un entier `n`;
- renvoie `True` si le nombre est pair (`n % 2 == 0`),
- renvoie `False` sinon.

Dans le programme principal :

1. Demande à l'utilisateur un entier ;
2. Appelez `eh_par(n)` et enregistrez le résultat ;
3. Si le résultat est `True`, inscrivez `"O número é par."`, sinon `"O número é ímpar."`.

> Résolution

```python
def he_paire(n):
    return n % 2 == 0
dans_un = int(input("Écrivez un entier : "))
if he_paire(dans_un):
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")
```

---

### <a id="ex13"></a> Exercice 13 - Fonction à deux paramètres : supérieur à deux nombres

Créez une fonction `maior(a, b)` qui :

- reçoit deux nombres `a` et `b`;
- renvoie le plus grand des deux.

Dans le programme principal :

1. Demande à l'utilisateur deux chiffres ;
2. Appelle la fonction ;
3. Affiche la phrase : `"O maior número é: <resultado>"`.

> Résolution

```python
def plus_gros(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input("Écrivez le premier nombre : "))
numero2 = float(input("Écrivez le deuxième nombre : "))
resultat = plus_gros(num1, numero2)
print(f"Le plus grand nombre est : {resultat}")
```

---

### <a id="ex14"></a> Exercice 14 - Filtre approuvé à partir d'un dictionnaire

Imaginez un dictionnaire `notas` du type :

```python
remarques = {
    "Nain": 17,
    "Bruno": 9,
    "Carla": 12,
    "Diogo": 8
}
```

Crée une fonction approved(grades) qui :
• reçoit ce dictionnaire;
• renvoie une liste avec les noms des étudiants dont la note est ≥ 10.

Crée ensuite une autre fonction failed(grades) qui renvoie la liste des noms avec la note < 10.

Aucun programme principal : 1. Créez un dictionnaire de notes de votre choix ; 2. Appels approuvés (notes) et échoués (notes); 3. Imprimez quelque chose comme ceci :

```text
Aprovados: ['Ana', 'Carla']
Reprovados: ['Bruno', 'Diogo']
```

> Résolution

```python
def approuve_2(remarques):
    liste_approuvee = []
    for nom, avis in remarques.items():
        if avis >= 10:
            liste_approuvee.append(nom)
    return liste_approuvee

def echoue(remarques):
    liste_refusee = []
    for nom, avis in remarques.items():
        if avis < 10:
            liste_refusee.append(nom)
    return liste_refusee

remarques = {
    "Nain": 17,
    "Bruno": 9,
    "Carla": 12,
    "Diogo": 8
}

print("Approuvé:", approuve_2(remarques))
print("Échoué:", echoue(remarques))
```

---

### <a id="ex15"></a> Exercice 15 - Fonction qui renvoie plusieurs valeurs

Créez une fonction `estatisticas_numeros(numeros)` qui reçoit une liste de nombres et renvoie **3 valeurs** :

- la somme de tous nombres;
- la valeur minimale;
- la valeur maximale;

(Utilise le calcul manuel du minimum et du maximum, sans `min()` / `max()`.)

Dans le programme principal :

1. Crée une liste avec quelques nombres, par exemple `[3, 7, -2, 10, 4]`.
2. Appelle la fonction et stocke le résultat dans trois variables.
3. Affiche un petit résumé, par exemple :

```text
Soma: ...
Mínimo: ...
Máximo: ...
```

> Résolution

```python
def numeros_de_statistiques(nombres):
    somme = 0
    minimum = nombres[0]
    maximum = nombres[0]
    for dans_un in nombres:
        somme += dans_un
        if dans_un < minimum:
            minimum = dans_un
        if dans_un > maximum:
            maximum = dans_un
    return somme, minimum, maximum

nombres = [3, 7, -2, 10, 4]
somme, minimum, maximum = numeros_de_statistiques(nombres)
print(f"Somme : {somme}")
print(f"Minimum : {minimum}")
print(f"Maximum : {maximum}")
```

---

### <a id="ex16"></a> Exercice 16 - Mutabilité : fonction qui modifie une liste reçue

Crée une fonction add_prefix(name_list, prefix) qui :
• reçoit une liste de noms (par exemple ["Ana", "Bruno"]);
• reçoit une chaîne de préfixe (par exemple "M." ou "Aluna"),
• modifie la liste reçue en transformant chaque nom en "préfixe de nom", par exemple :
• ["Ana", "Bruno"] avec "Aluna" → ["Aluna Ana", "Aluna Bruno"].

Dans le programme main:

- 1. Créer une liste de noms;
- 2. Appeler la fonction;
- 3. Imprimer la liste avant et après l'appel pour voir l'effet de la mutabilité.

> Résolution

```python
def ajouter_un_prefixe(lister_les_noms, prefixe):
    for i in range(len(lister_les_noms)):
        lister_les_noms[i] = f"{prefixe} {lister_les_noms[i]}"
noms = ["Nain", "Bruno", "Carla"]
print("Avant:", noms)
ajouter_un_prefixe(noms, "M./Mme.")
print("Après:", noms)
```

---

### <a id="ex17"></a> Exercice 17 - \*args : moyenne d'un nombre variable de nombres

Crée une fonction variable_average(\*nums) qui :
• reçoit 0 ou plusieurs nombres (entiers ou floats);
• s'il ne reçoit aucun nombre, il renvoie 0,0;
• sinon, il renvoie la moyenne arithmétique.

Dans le programme principal : 1. Testez la fonction avec :
• variable_average();
• variable_average(10, 12, 14);
• variable_moyenne (5, 7,5). 2. Imprimez les résultats.

> Résolution

```python
def moyenne_variable(*chiffres):
    if not chiffres:
        return 0.0
    return sum(chiffres) / len(chiffres)
# Essais
print(moyenne_variable())               # 0,0
print(moyenne_variable(10, 12, 14))     # 12,0
print(moyenne_variable(5, 7.5))         # 6.25
```

---

### <a id="ex18"></a> Exercice 18 - \*\*kwargs : configuration flexible

Crée une fonction create_profile(\*\*info) qui :
• reçoit des informations nommées sur une personne (par exemple, name="Ana", age=16, course="PI"),
• renvoie un dictionnaire avec ces informations.

Dans le programme principal : 1. Créez 2 profils différents à l'aide de la fonction :
• un avec nom, âge;
• un autre avec nom, âge, cours et classe (par exemple "10e A"). 2. Imprimez les dictionnaires renvoyés.

> Résolution

```python
def creer_un_profil(**infos):
    return infos
# Essais
profil1 = creer_un_profil(nom="Nain", age=16)
profil2 = creer_un_profil(nom="Bruno", age=17, cours="PI", classe="10ème A")
print(profil1)  # {'nom' : 'Ana', 'âge' : 16}
print(profil2)  # {'nom' : 'Bruno', 'âge' : 17, 'cours' : 'PI', 'classe' : '10e A'}
```

---

### <a id="ex19"></a> Exercice 19 (Défi) - Fonction avec `*args`

Créez une fonction `produto(*nums)` qui :

- reçoit 0 ou plus nombres,
- renvoie le produit de tous (multiplication),
- s'il ne reçoit aucun nombre, renvoie 1 (identité de multiplication).

Test avec :

- `produto(2, 3)` → 6
- `produto(2, 3, 4)` → 24
- `produto()` → 1

> Résolution

```python
def produit(*chiffres):
    resultat = 1
    for n in chiffres:
        resultat *= n
    return resultat
# Essais
print(produit(2, 3))        # 6
print(produit(2, 3, 4))     # 24
print(produit())            # 1
```

---

### <a id="ex20"></a> Exercice 20 (Défi avancé) - Récursion simple

Créez une fonction récursive `conta_decrescente(n)` qui :

- prend un nombre entier `n >= 1`,
- renvoie une liste `[n, n-1, ..., 1]`.

Exemple :

```python
compte_decroissant(4)  # [4, 3, 2, 1]
```

Comparez ensuite avec une version **non récursive** utilisant `while` ou `for`.  
Réfléchissez à la version que vous trouvez la plus facile à lire.

> Résolution

```python
def compte_decroissant(n):
    if n <= 1:
        return [1]
    else:
        return [n] + compte_decroissant(n - 1)
# Version non récursive
def decompte_iteratif_decroissant(n):
    resultat = []
    for i in range(n, 0, -1):
        resultat.append(i)
    return resultat
# Essais
print(compte_decroissant(4))             # [4, 3, 2, 1]
print(decompte_iteratif_decroissant(4))   # [4, 3, 2, 1]
```

---

## 14. Journal des modifications

> Enregistrement des modifications importantes apportées à ce fichier.

- **2025-11-17 · v1.2**
 - Solutions ajoutées à celles déjà réalisées.
- **2025-11-17 · v1.1**
 - Table des matières mise à jour.
- **2025-11-17 · v1.0**
 - Initiale création du document.
 - Sections essentielles : motivation pour les fonctions, définition et appel, `print` vs `return`, paramètres/arguments, `return`, portée de base, mutabilité, bonnes pratiques et tests.
 - Sections supplémentaires : fonctions d'ordre supérieur, `lambda`, `*args`/`**kwargs`, docstrings et types, récursion.
 - Ajout de 12 exercices progressifs (des bases aux défis avec récursion et structures imbriquées).
