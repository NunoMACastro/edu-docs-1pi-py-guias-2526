# Python (10e année) - 05 · Découpage et compréhension de listes

> **Objectif de ce fichier** 
> Comprendre comment « couper » des séquences en Python (listes, chaînes, etc.) avec _slicing_ et comment créer de nouvelles listes à partir d'autres de manière compacte en utilisant _list compréhensions_.

---

## Index

- [0. Guide pour ne pas se perdre](#0-guide-pour-ne-pas-se-perdre)
- [1. Revue rapide : listes et séquences · \[ESSENTIEL\]](#1-revisão-rápida-listas-e-sequências--essencial)
- [2. Index et accès simple · \[ESSENTIEL\]](#2-índices-e-acesso-simples--essencial)
- [3. Découpage de base : `lista[início:fim]` · \[ESSENTIAL\]](#3-slicing-básico-listainíciofim--essencial)
- [4. Découpage avec pas et indices négatifs · \[EXTRA mais très utile\]](#4-slicing-com-passo-e-índices-negativos--extra-mas-muito-útil)
- [5. Découpage en chaînes et autres séquences · \[ESSENTIEL (notion de base)\]](#5-slicing-em-strings-e-outras-sequências--essencial-noção-básica)
- [6. Introduction à la compréhension des listes · \[ESSENTIEL\]](#6-introdução-a-list-comprehensions--essencial)
- [7. Liste des compréhensions avec condition (filtre) · \[ESSENTIEL\]](#7-list-comprehensions-com-condição-filtro--essencial)
- [8. Liste des compréhensions avec `if/else` dans l'expression · \[EXTRA\]](#8-list-comprehensions-com-ifelse-na-expressão--extra)
- [9. `for` Compréhension normale vs liste · \[ESSENTIEL (état d'esprit)\]](#9-for-normal-vs-list-comprehension--essencial-mentalidade)
- [10. Autres compréhensions (ensembles, dicts, générateurs) · \[EXTRA / curiosité\]](#10-outras-comprehensions-sets-dicts-generators--extra--curiosidade)
- [11. Bonnes pratiques et erreurs courantes · \[ESSENTIEL (mentalité)\]](#11-boas-práticas-e-erros-comuns--essencial-mentalidade)
- [12. Exercices de découpage et de compréhension](#12-exercices-de-decoupage-et-de-comprehension)
- [13. Journal des modifications](#13-journal-des-modifications)

---

## 0. Guide pour ne pas vous perdre

Deux thèmes qui ont tendance à se confondre ici apparaissent :

- la syntaxe avec deux points (`:`) au milieu des listes et des chaînes;
- la syntaxe compacte de **list compréhensions**.

Pour s'organiser :

- Concentrez-vous d'abord sur :
 - **Section 2 et 3** (index et découpage de base),
 - **Section 6 et 7** (compréhensions de listes simples avec conditions).
- Les parties marquées **[EXTRA]** lisent lorsque vous êtes à l'aise avec l'essentiel.
- Utilisez l'interpréteur (`python` / VS Code) pour tester des petits exemples.

---

## 1. Revue rapide : listes et séquences · [ESSENTIEL]

Rappelons-en quelques-uns concepts :

- Une **list** en Python stocke plusieurs valeurs dans un ordre :

```python
nombres = [10, 20, 30, 40, 50]
noms = ["Nain", "Bruno", "Carla"]
```

- Une **chaîne** est également une séquence de caractères :

```python
texte = "Programmeur"
```

- Autres séquences apparaissant ultérieurement :
 - `tuple` → `tuplo = (1, 2, 3)`
 - `range` → `range(0, 10, 2)`

Toutes ces structures ont deux caractéristiques importantes :

1. Les éléments sont dans **un ordre**.
2. Nous pouvons accéder aux éléments en utilisant les **indices**.

---

## 2. Index et accès simple · [ESSENTIEL]

Avant de faire du _slicing_, vous devez être à l'aise avec les **indices**.

- En Python, les indices commencent à **0**.
- Index 0 → premier élément.
- Index 1 → deuxième, et ainsi de suite.

```python
nombres = [10, 20, 30, 40, 50]

print(nombres[0])  # 10
print(nombres[1])  # 20
print(nombres[4])  # 50 (5ème élément)
```

Si vous essayez d'accéder à un index qui n'existe pas, vous obtenez une erreur :

```python
print(nombres[5])  # IndexError : index de la liste hors plage
```

Vous pouvez également utiliser des **indices négatifs** :

- `-1` → dernier élément
- `-2` → avant-dernier
- etc.

```python
print(nombres[-1])  # 50
print(nombres[-2])  # 40
```

Cela fonctionne de la même manière sur les **chaînes** :

```python
texte = "Python"
print(texte[0])   # 'P'
print(texte[-1])  # 'n'
```

---

## 3. Découpage de base : `lista[início:fim]` · [ESSENTIEL]

_slicing_ vous permet d'obtenir **une partie** d'une liste (ou d'une chaîne).

Syntaxe de base :

```python
sous_liste = liste[commencer:fin]
```

- `inicio` → index où il commence (inclut cet élément).
- `fim` → index où **s'arrête** (n'inclut pas cet élément).
- Le résultat est une **nouvelle liste** (ne change pas l'original).

Imaginez :

```python
nombres = [10, 20, 30, 40, 50, 60]
# indices : 0 1 2 3 4 5
```

### 3.1. Exemples simples

```python
print(nombres[0:3])  # [10, 20, 30] (indices 0, 1, 2)
print(nombres[2:5])  # [30, 40, 50] (index 2, 3, 4)
```

Remarque : l'index `fim` est **exclusif**, c'est-à-dire qu'il n'est pas inclus dans la tranche.

### 3.2. Omettez `inicio` ou `fim`

Si **vous n'écrivez pas** `inicio`, cela suppose le début de la liste.  
Si **vous n'écrivez pas** `fim`, la fin de la liste sera supposée.

```python
print(nombres[:3])   # [10, 20, 30] (du début à avant l'index 3)
print(nombres[3:])   # [40, 50, 60] (de l'index 3 à la fin)
print(nombres[:])    # copie de la liste entière
```

Cette forme `lista[:]` est souvent utilisée pour faire une **copie superficielle** de la liste.

---

## 4. Découpage avec échelons et indices négatifs · [EXTRA mais très utile]

Il existe une forme plus complète :

```python
sous_liste = liste[commencer:fin:etape]
```

- `passo` → de combien d'indices il avance.
 - Si c'est 1 → ça va élément par élément.
 - Si c'est 2 → ça saute de 2 à 2, etc.

### 4.1. Étape positive

```python
nombres = [10, 20, 30, 40, 50, 60]

print(nombres[0:6:2])  # [10, 30, 50]
print(nombres[1:6:2])  # [20, 40, 60]
```

Vous pouvez également omettre `inicio` et/ou `fim` :

```python
print(nombres[::2])    # [10, 30, 50] (du début à la fin, tous les 2)
print(nombres[1::2])   # [20, 40, 60] (de l'index 1, de 2 à 2)
```

### 4.2. Pas négatif (inverse)

Si `passo` est négatif, la séquence va **en arrière**.

```python
nombres = [10, 20, 30, 40, 50, 60]

print(nombres[::-1])   # [60, 50, 40, 30, 20, 10] (liste à l'envers)
print(nombres[4:1:-1]) # [50, 40, 30] (des indices 4 à > 1, en revenant)
```

Pour les chaînes :

```python
texte = "Python"
print(texte[::-1])  # "nohtyP"
```

### 4.3. Indices négatifs en découpage

Vous pouvez mélanger des indices positifs et négatifs :

```python
nombres = [10, 20, 30, 40, 50, 60]
# indices : 0 1 2 3 4 5
# nég.: -6 -5 -4 -3 -2 -1

print(nombres[1:-1])   # [20, 30, 40, 50]
print(nombres[-3:])    # [40, 50, 60]
print(nombres[:-2])    # [10, 20, 30, 40]
```

---

## 5. Découpage en chaînes et autres séquences · [ESSENTIEL (notion de base)]

_Slicing_ n'est pas uniquement destiné aux listes.  
Fonctionne avec **n'importe quelle séquence** prenant en charge les index :

- chaînes,
- tuples,
- `range` (partiellement), etc.

### 5.1. Tranchage de chaîne

```python
texte = "Programmeur"

print(texte[0:4])   # "Programme"
print(texte[:7])    # "Programme"
print(texte[4:])    # "ramasseur"
print(texte[::-1])  # "rodamargorP"
```

Ceci est très utile pour :

- récupérer les préfixes et suffixes,
- supprimer des parties de début ou de fin,
- vérifier certaines structures (par exemple, les extensions de fichiers).

### 5.2. Découper en tuples

```python
points = (10, 20, 30, 40, 50)

print(points[1:4])  # (20, 30, 40)
print(points[::-1]) # (50, 40, 30, 20, 10)
```

---

## 6. Introduction aux compréhensions de listes · [ESSENTIEL]

Une **compréhension de liste** est une manière **compacte** de créer des listes à partir d'autres listes (ou séquences).

Forme générale la plus simple :

```python
nouvelle_liste = [expression for article in iterable]
```

- `iteravel` → quelque chose que vous pouvez parcourir avec `for` (liste, chaîne, plage, etc.).
- `item` → chaque élément de l'itérable.
- `expressao` → ce que vous voulez mettre dans la nouvelle liste.

### 6.1. Exemple : carrés numériques

Version normale avec `for` :

```python
nombres = [1, 2, 3, 4, 5]
carres = []

for n in nombres:
    carres.append(n ** 2)

print(carres)  # [1, 4, 9, 16, 25]
```

Version avec compréhension de liste :

```python
nombres = [1, 2, 3, 4, 5]
carres = [n ** 2 for n in nombres]

print(carres)  # [1, 4, 9, 16, 25]
```

### 6.2. Exemple : convertir des chaînes en majuscules

```python
noms = ["nain", "bruno", "carla"]
noms_en_majuscules = [nom.upper() for nom in noms]

print(noms_en_majuscules)  # ["ANA", "BRUNO", "CARLA"]
```

Règle mentale :

1. Écrivez d'abord la version avec `for` « normal ».
2. Si vous vous retrouvez avec un modèle « créer une liste vide + ajouter », envisagez de le transformer en une compréhension de liste.

---

## 7. Compréhensions de liste avec condition (filtre) · [ESSENTIEL]

Nous pouvons ajouter une **condition** pour filtrer les éléments :

```python
nouvelle_liste = [expression for article in iterable if condition_2]
```

`condição` est une expression qui doit renvoyer `True` ou `False`.  
Seuls les éléments pour lesquels la condition est `True` entrent dans la nouvelle liste.

### 7.1. Exemple : filtrer les nombres pairs

Version normale :

```python
nombres = [1, 2, 3, 4, 5, 6]
paires = []

for n in nombres:
    if n % 2 == 0:
        paires.append(n)

print(paires)  # [2, 4, 6]
```

Version avec compréhension de liste :

```python
nombres = [1, 2, 3, 4, 5, 6]
paires = [n for n in nombres if n % 2 == 0]

print(paires)  # [2, 4, 6]
```

### 7.2. Exemple : longueurs de nom comportant 4 lettres ou plus

```python
noms = ["Nain", "Bruno", "Carla", "Di"]
longueurs = [len(nom) for nom in noms if len(nom) >= 4]

print(longueurs)  # [5, 5]
```

---

## 8. Liste des compréhensions avec `if/else` dans l'expression · [EXTRA]

Il est également possible de mettre un `if/else` dans l'**expression**, au lieu d'être à la fin.  
Cela permet de transformer les valeurs différemment selon les cas.

Forme générale :

```python
nouvelle_liste = [exprimer_si_c_est_vrai if condition_2 else expr_si_faux
              for article in iterable]
```

Exemple : classer les nombres comme `"par"` ou `"ímpar"` :

```python
nombres = [1, 2, 3, 4, 5]
genres = ["paire" if n % 2 == 0 else "impair" for n in nombres]

print(genres)  # ["impair", "pair", "impair", "pair", "impair"]
```

Attention : ne pas le confondre avec `if` pour filtre.

- `[...] for n in numeros if condição]` → supprime certains éléments.
- `[..., "par" if condição else "ímpar", ...]` → les conserve tous, mais change la valeur.

---

## 9. `for` Compréhension normale vs liste · [ESSENTIEL (état d'esprit)]

### 9.1. Quand utiliser `for`

- Lorsque la logique est **compliquée** (plusieurs `if`, plusieurs étapes).
- Lorsqu'il y a des **effets secondaires** (par exemple : `print` à l'intérieur du cycle, écriture dans des fichiers).
- Quand vous devez **déboguer** et voir étape par étape étape.

Exemple (peut-être trop pour la compréhension) :

```python
resultat = []
for n in nombres:
    if n % 2 == 0:
        valeur = n ** 2
        print("carré de", n, "=", valeur)
        resultat.append(valeur)
```

### 9.2. Quand utiliser la compréhension de liste

- Lorsque vous **voulez simplement créer une nouvelle liste** à partir d'une autre,
- avec une simple transformation,
- et éventuellement un simple **filtre**.

Exemples typiques :

- Carrés, cubes, longueurs de chaînes.
- Filtrer les _paires_, _positives_, _names avec plus de 
> **la compréhension de liste** est généralement une bonne option.

---

## 10. Autres compréhensions (ensembles, dicts, générateurs) · [EXTRA / curiosité]

La notion de compréhension n'est pas exclusive aux listes.

### 10.1. Compréhension d'ensemble

Crée un **ensemble** (sans répétitions) :

```python
nombres = [1, 2, 2, 3, 3, 3]
pas_de_repetitions = {n for n in nombres}

print(pas_de_repetitions)  # {1, 2, 3} (commande non garantie)
```

### 10.2. Compréhension de dictés

Crée un **dictionnaire** :

```python
noms = ["Nain", "Bruno", "Carla"]
tailles = {nom: len(nom) for nom in noms}

print(tailles)  # {"Ana": 3, "Bruno": 5, "Carla": 5}
```

### 10.3. Expression génératrice

Similaire à la compréhension de liste mais avec `()` au lieu de `[]`.  
Il ne crée pas la liste entière en même temps, il la génère selon les besoins.

```python
nombres = [1, 2, 3, 4, 5]
generation = (n ** 2 for n in nombres)

for valeur in generation:
    print(valeur)
```

Cette année, l'important est de comprendre d'abord les **compréhensions de la liste**.

---

## 11. Bonnes pratiques et erreurs courantes · [ESSENTIEL (mentalité)]

### 11.1. N'abusez pas de la « magie »

- Si l'expression devient trop longue, la lisibilité se détériore.
- Plusieurs conditions liées peuvent rendre le code confus.

Un `for` normal très clair est préférable à une compréhension que personne ne comprend.

### 11.2. Évitez les effets secondaires en compréhension

Techniquement, vous pouvez faire :

```python
[print(n) for n in nombres]
```

Mais cela est considéré comme une **mauvaise pratique** : 
une compréhension de liste doit être utilisée pour **créer des listes**, et non pour faire `print`.

Mieux :

```python
for n in nombres:
    print(n)
```

### 11.3. Faites attention aux index dans le découpage

Erreurs typiques :

- Faire une erreur de comptage (rappelez-vous : `fim` n'est pas inclus).
- Oublier que `lista[a:b]` ne donne jamais d'erreur si `b` est trop grand ; coupez simplement aussi loin que vous le pouvez :

```python
nombres = [10, 20, 30]
print(nombres[0:10])  # [10, 20, 30] (pas d'erreur)
```

- Utilisez `[::-1]` sans vous rendre compte que vous inversez la séquence.

En cas de confusion, écrivez la liste avec les indices en dessous sur une feuille de papier et marquez l'intervalle `[inicio, fim[` (fermé à gauche, ouvert à droite).

---

## 12. Exercices de découpage et de compréhension

> Suggestion : commencer par les exercices de base, puis passer aux exercices et défis intermédiaires.  
> Vous pouvez (et devez) tester chaque exercice dans l'interpréteur Python ou VS Code.

### Exercice 1 · Découpage de base dans une liste · [BASIC]

Étant donné la liste :

```python
nombres = [10, 20, 30, 40, 50, 60, 70]
```

En utilisant uniquement _slicing_ (`lista[inicio:fim]`), crée des expressions qui renvoient :

1. `[10, 20, 30]`
2. `[40, 50, 60]`
3. `[30, 40, 50, 60]`
4. Une copie complète de la liste.

> Résolution :

```python
nombres = [10, 20, 30, 40, 50, 60, 70]
print(nombres[0:3])    # [10, 20, 30
print(nombres[3:6])    # [40, 50, 60
print(nombres[2:6])    # [30, 40, 50, 60]
print(nombres[:])      # copie complète
```

---

### Exercice 2 · Découpage avec des indices négatifs · [BASIC]

Utilisez le _slicing_ et les indices négatifs pour, à partir de :

```python
paroles = ["le", "b", "w", "d", "et", "f"]
```

obtenir :

1. `["d", "e", "f"]`
2. `["b", "c", "d", "e"]`
3. `["e", "f"]` en utilisant uniquement des indices négatifs.

> Résolution :

```python
paroles = ["le", "b", "w", "d", "et", "f"]
print(paroles[-3:])     # ["d", "e", "f"]
print(paroles[1:-1])    # ["b", "c", "d", "e"]
print(paroles[-2:])     # ["e", "f"]
```

---

### Exercice 3 · Découpage en chaînes · [BASIC]

Donné :

```python
texte = "Programmeur informatique"
```

Utilisez _slicing_ pour obtenir :

1. `"Programador"`
2. `"Informático"`
3. La chaîne à l'envers.

> Résolution :

```python
texte = "Programmeur informatique"
print(texte[:11])        # "Programmeur"
print(texte[12:])        # "IL"
print(texte[::-1])       # "ocitamrofI rodamargoP"
```

---

### Exercice 4 · Tranchage avec pas · [MEDIUM]

Avec la liste :

```python
chiffres = list(range(1, 21))  # [1, 2, 3, ..., 20]
```

Utilisez _slicing_ avec `passo` pour obtenir :

1. Tous les nombres impairs.
2. Tous les nombres pairs.
3. La liste `[20, 18, 16, 14, 12, 10]`.

> Résolution :

```python
chiffres = list(range(1, 21))
print(chiffres[::2])        # Nombres impairs
print(chiffres[1::2])       # Des nombres pairs
print(chiffres[-1:-11:-2])  # [20, 18, 16, 14, 12, 10]
```

---

### Exercice 5 · Carrés avec compréhension de liste · [BASIC]

Crée une **compréhension de liste** qui, à partir de :

```python
chiffres = [1, 2, 3, 4, 5]
```

retour :

```python
[1, 4, 9, 16, 25]
```

> Résolution :

```python
chiffres = [1, 2, 3, 4, 5]
carres = [n ** 2 for n in chiffres]
print(carres)  # [1, 4, 9, 16, 25]
```

---

### Exercice 6 · Compréhension de tranches et de listes · [MEDIUM]

Étant donné la liste :

```python
mots = ["maison", "voiture", "vélo", "avion", "bateau"]
```

Utilisez _slicing_ pour obtenir une nouvelle liste avec les **deux premières lettres** de chaque mot, en utilisant une **compréhension de liste**.
Exemple de résultat :

```python
["ici", "ici", "bi", "av", "ba"]
```

> Résolution :

```python
mots = ["maison", "voiture", "vélo", "avion", "bateau"]
initiales = [mot[:2] for mot in mots]
print(initiales)  # ["ca", "ca", "bi", "av", "ba"]
```

---

### Exercice 7 · Filtrer les paires avec compréhension de liste · [BASIC]

Étant donné la liste :

```python
chiffres = [3, 8, 12, 5, 7, 20, 21]
```

Crée une compréhension de liste qui renvoie uniquement des **nombres pairs**.

> Résolution :

```python
chiffres = [3, 8, 12, 5, 7, 20, 21]
paires = [n for n in chiffres if n % 2 == 0]
print(paires)  # [8, 12, 20]
```

---

### Exercice 8 · Longueurs de nom avec filtre · [MEDIUM]

Étant donné la liste :

```python
noms = ["Nain", "Bruno", "Carla", "Diogo", "Veille"]
```

Crée une compréhension de liste qui renvoie une liste avec les **longueurs de noms** comportant **4 lettres ou plus**.

Exemple de résultat :

```python
[5, 5, 5]
```

> Résolution :

```python
noms = ["Nain", "Bruno", "Carla", "Diogo", "Veille"]
longueurs = [len(nom) for nom in noms if len(nom) >= 4]
print(longueurs)  # [5, 5, 5]
```

---

### Exercice 9 · Classer les nombres comme « pairs »/« impairs » · [MOYENNE]

Étant donné la liste :

```python
chiffres = [1, 2, 3, 4, 5, 6]
```

Utilisez une compréhension de liste avec `if/else` dans l'**expression** pour obtenir :

```python
["impair", "paire", "impair", "paire", "impair", "paire"]
```

> Résolution :

```python
chiffres = [1, 2, 3, 4, 5, 6]
genres = ["paire" if n % 2 == 0 else "impair" for n in chiffres]
print(genres)  # ["impair", "pair", "impair", "pair", "impair", "pair"]
```

---

### Exercice 10 · Mélange de découpage et de compréhension · [MEDIUM]

Compte tenu de la liste :

```python
mots = ["Python", "Programmeur", "Liste", "Compréhension"]
```

1. Utilisez _slicing_ pour obtenir une nouvelle liste avec uniquement les **deux dernières lettres** de chaque mot (vous pouvez utiliser un `for` normal).
2. Ensuite, faites de même, mais en utilisant une **compréhension de liste** (et un découpage au sein de l'expression).

Exemple de résultat :

```python
["sur", "ou", "d'accord", "sur"]
```

> Résolution :

```python
mots = ["Python", "Programmeur", "Liste", "Compréhension"]
# Utilisation normale
dernier_2 = []
for mot in mots:
    dernier_2.append(mot[-2:])
print(dernier_2)  # ["sur", "ou", "ta", "sur"]
# Utiliser la compréhension de liste
derniere_lc = [mot[-2:] for mot in mots]
print(derniere_lc)  # ["sur", "ou", "ta", "sur"]
```

---

### Exercice 11 · Filtrer et transformer · [MEDIUM]

Étant donné la liste :

```python
chiffres = list(range(1, 21))  # de 1 à 20
```

Utilise une **compréhension de liste** pour créer une liste avec :

- les carrés des nombres **pairs**,
- mais **uniquement** ceux qui sont **supérieurs à 10**.

> Résolution :

```python
chiffres = list(range(1, 21))
resultat = [n ** 2 for n in chiffres if n % 2 == 0 and n > 10]
print(resultat)  # [144, 196, 256, 324, 400]
```

---

### Exercice 12 · LC en chaînes · [MEDIUM]

Étant donné la chaîne :

```python
phrase = "Vous êtes des beautés"
```

Crée une compréhension de liste avec uniquement les voyelles de la phrase en majuscules.

> Résolution :

```python
phrase = "Vous êtes des beautés"
voyelles_majuscules = [lettre.upper() for lettre in phrase if lettre.lower() in "aeiouáéíóúâêôãõ"]
print(voyelles_majuscules)  # ['O', 'E', 'A', 'O', 'U', 'A', 'E', 'E', 'U', 'A']
```

---

### Exercice 13 (Défi) · Filtrer et transformer en même temps · [DÉFI]

Étant donné la liste :

```python
chiffres = list(range(-5, 11))  # de -5 à 10
```

Utilise **une seule compréhension de liste** pour créer une liste avec :

- les carrés des nombres **positifs**,
- mais **uniquement** ceux qui sont **pairs**.

Exemple (pas la réponse complète) :

```python
[4, 16, 36, ...]
```

> Résolution :

```python
chiffres = list(range(-5, 11))
resultat = [n ** 2 for n in chiffres if n > 0 and n % 2 == 0]
print(resultat)  # [4, 16, 36, 64, 100]
```

---

### Exercice 14 (Défi) · Découpage en « fenêtres » · [DÉFI]

Compte tenu de la liste :

```python
donnees = [10, 20, 30, 40, 50, 60]
```

Crée du code qui produit une liste de **sous-listes**, où chaque sous-liste comporte 3 éléments consécutifs :

```python
[[10, 20, 30],
 [20, 30, 40],
 [30, 40, 50],
 [40, 50, 60]]
```

Suggestion :

- Utiliser un cycle `for` sur les indices.
- À chaque itération, utiliser _slicing_ `dados[i:i+3]`.
- Ensuite, essayez de transformer la solution en compréhension de liste.

> Résolution :

```python
donnees = [10, 20, 30, 40, 50, 60]
fenetres = [donnees[i:i+3] for i in range(len(donnees) - 2)]
print(fenetres)
```

> Explication : `range(len(dados) - 2)` garantit que `i+3` ne dépasse pas la taille de la liste.

---

## 13. Changelog

> Enregistrement des modifications importantes apportées à ce fichier.

- **2025-11-26 · v1.0**
 - Création initiale du document.
 - Sections essentielles : revue de séquence, indices, découpage de base, découpage de chaîne, introduction aux compréhensions de liste et compréhensions de filtres.
 - Sections supplémentaires : découpage avec indices pas et négatifs, compréhensions avec `if/else`, autres compréhensions (ensembles, dicts, générateurs).
 - Ajout d'exercices progressifs (tranchage de base, compréhensions, découpage mixte+compréhension, défis).
