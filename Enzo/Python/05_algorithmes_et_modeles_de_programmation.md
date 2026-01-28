# Python (10ème année) - 05 · Algorithmes et modèles de programmation

> **Objectif de ce fichier** 
> Apprendre à résoudre des problèmes de programmation courants, à l'aide de listes, de dictionnaires et de fonctions.
>
> - lire un problème,
> - découvrir quelles sont les **données d'entrée**,
> - décider quelles sont les Le **traitement** est (comptes, moyennes, filtrage, etc.),
> - définissez ce qui doit apparaître comme **sortie**,
> - et transformez tout cela en code avec des listes, des dictionnaires et des fonctions.

Tout au long de ce document :

- Les sections marquées **[ESSENTIEL]** sont la base que vous devez maîtriser pour les tests et projets.
- Les sections marquées **[EXTRA]** sont à explorer lorsque vous êtes plus à l'aise.

---

## Index

- [0. Comment résoudre un problème de programmation · [ESSENTIEL]](#0-como-resolver-um-problema-de-programa%C3%A7%C3%A3o--essencial)
- [1. Patrons classiques avec listes · [ESSENTIEL]](#1-padr%C3%B5es-cl%C3%A1ssicos-com-listas--essencial)
- [2. Normes avec dictionnaires · [ESSENTIEL]](#2-padr%C3%B5es-com-dicion%C3%A1rios--essencial)
- [3. Rassemblez le tout en fonctions · [ESSENTIEL]](#3-juntar-tudo-em-fun%C3%A7%C3%B5es--essencial)
- [4. Stratégie étape par étape sur un problème plus vaste · [ESSENTIEL]](#4-estrat%C3%A9gia-passo-a-passo-num-problema-maior--essencial)
- [5. Erreurs typiques et débogage de base · [ESSENTIEL]](#5-erros-t%C3%ADpicos-e-debugging-b%C3%A1sico--essencial)
- [6. Exercices - Algorithmes et modèles de programmation](#6-exercices-algorithmes-et-modeles-de-programmation)
- [7. Journal des modifications](#7-journal-des-modifications)

---

## 0. Comment résoudre un problème de programmation · [ESSENTIEL]

De nombreuses erreurs apparaissent parce que vous commencez à écrire du code tout de suite, sans réfléchir.  
Une approche plus sûre :

### 0.1. Étape 1 - Lisez calmement la déclaration

- Soulignez ou surlignez :
 - ce qui est donné (**input**),
 - ce qui est demandé (**output**),
 - des indices sur ce que vous devez faire entre les deux (**processing**).

Exemple de déclaration :

> "Demande à l'utilisateur l'âge de 5 personnes, calcule l'âge moyen et indique combien sont supérieurs ou égaux à 18 ans."

- Entrées :
 - 5 âges (entiers).
- Sortie :
 - âge moyen,
 - nombre de personnes ≥ 18.
- Traitement :
 - enregistrer les âges quelque part (liste),
 - ajouter des âges pour calculer la moyenne,
 - compter combien d'âges ont ≥ 18 ans.

Vous pouvez créer un tableau avec ces informations, si cela peut vous aider.
exemple :

| Entrées | Traitement | Sortie |
| ---------- | -------------------------------- | ---------------------------- |
| 5 âges (int) | enregistrer les âges dans une liste | âge moyen (flotteur) |
|                | ajouter des âges pour calculer la moyenne | nombre de personnes ≥ 18 (int) |
|                | compter les âges ≥ 18 |                              |

---

### 0.2. Étape 2 - Créez 2 à 3 exemples à la main

Choisissez les données et faites le calcul sur papier.

Exemple :

- Âges : 15, 20, 18, 30, 16
- Somme : 15 + 20 + 18 + 30 + 16 = 99
- Moyenne : 99 / 5 = 19,8
- Supérieur ou égal à 18 : 20, 18, 30 → 3 personnes

Vous avez déjà une idée de ce que doit faire le programme.

### 0.3. Étape 3 - Rédiger un plan en portugais (pseudocode)

Exemple de plan :

1. Créez une liste vide pour stocker les âges.
2. Répétez 5 fois :
 - demandez un âge à l'utilisateur,
 - convertissez en entier,
 - ajoutez à la liste.
3. Calculez la somme des âges.
4. Calculez la moyenne.
5. Comptez combien d'âges ont ≥ 18 ans.
6. Afficher la moyenne et le nombre supérieur ou égal à 18.

### 0.4. Étape 4 - Transformer le plan en code

Tout d'abord, sans fonctions (juste pour comprendre la logique).  
Ensuite, refactorisez les fonctions (voir section 4).

---

## 1. Modèles classiques avec des listes · [ESSENTIEL]

Regardons les **modèles de raisonnement** qui apparaissent souvent.

### 1.1. Modèle « lire les valeurs et créer une liste »

Exemple : lire 5 âges dans une liste.

```python
age_2 = []                      # liste vide

for _ in range(5):               # répéter 5 fois
    age = int(input("Âge: "))
    age_2.append(age)         # ajouter à la fin de la liste

print("Âge:", age_2)
```

Ce modèle est très courant : commencer par une liste vide et faire `append`.

---

### 1.2. Modèle d'accumulation (ajouter des valeurs)

Nous voulons ajouter tous les éléments d'une liste.

```python
age_2 = [15, 20, 18, 30, 16]

total = 0
for age in age_2:
    total += age       # total = total + âge

moyenne = total / len(age_2)
print("Moyenne:", moyenne)
```

Ce modèle (variable `total` qui commence à 0 et s'accumule) apparaît dans :

- les sommations,
- les calculs de moyennes,
- le calcul des ventes totales, etc.

---

### 1.3. Modèle de comptage conditionnel

Comptez le nombre d'éléments qui remplissent une certaine condition.

```python
age_2 = [15, 20, 18, 30, 16]

superieur_ou_egal_a_18 = 0
for age in age_2:
    if age >= 18:
        superieur_ou_egal_a_18 += 1

print("Personnes âgées de 18 ans ou plus :", superieur_ou_egal_a_18)
```

Uniquement la condition de comptabilisation des changements :

- négatifs,
- paires,
- notes ≥ 10, etc.

---

### 1.4. Modèle min/max manuel

Sans utiliser `min()` ou `max()`.

```python
age_2 = [15, 20, 18, 30, 16]

age_minimum = age_2[0]       # commencer par le premier
age_maximum = age_2[0]

for age in age_2:
    if age < age_minimum:
        age_minimum = age
    if age > age_maximum:
        age_maximum = age

print("Minimum:", age_minimum)
print("Maximum:", age_maximum)
```

Ce modèle est important lorsque nous **ne pouvons** pas** utiliser des fonctions toutes faites (dans des tests ou des défis).

---

### 1.5. Modèle de filtrage (créer une nouvelle liste)

Créez une nouvelle liste avec uniquement les éléments qui passent le « filtre ».

```python
age_2 = [15, 20, 18, 30, 16]

superieur_ou_egal_a_18 = []          # nouvelle liste
for age in age_2:
    if age >= 18:
        superieur_ou_egal_a_18.append(age)

print("Âges ≥ 18 :", superieur_ou_egal_a_18)
```

Souvent, nous souhaitons conserver la liste originale et créer une **version filtrée**.

---

### 1.6. Modèle de transformation (valeurs de la carte)

Créez une nouvelle liste avec une transformation appliquée à chaque élément.

```python
nombres = [1, 2, 3, 4]

carres = []
for n in nombres:
    carre = n ** 2
    carres.append(carre)

print("Originaux :", nombres)
print("Carrés :", carres)
```

Autres exemples de transformation :

- convertir les températures de Celsius en Fahrenheit,
- normaliser les valeurs (par exemple diviser tout par le maximum),
- convertir les chaînes en minuscules.

---

## 2. Modèles avec dictionnaires · [ESSENTIEL]

Les dictionnaires sont parfaits pour simuler des **« petites bases de données » en mémoire**.

### 2.1. Dictionnaire simple : clé → valeur

Exemple : personnes et âges.

```python
age_2 = {
    "Nain": 16,
    "Bruno": 17,
    "Carla": 15
}

print(age_2["Nain"])    # 16
```

---

### 2.2. Rechercher une clé

Vérifier si une personne est dans le dictionnaire.

```python
nom = input("Nom à rechercher : ")

if nom in age_2:
    print("Âge de", nom, "et", age_2[nom])
else:
    print("Personne non trouvée.")
```

Le modèle est très courant :

```python
if cle in dictionnaire:
    # utiliser le dictionnaire[clé]
else:
    # gérer le cas où la clé n'existe pas
```

---

### 2.3. Compter des choses avec des dictionnaires

Comptez combien de fois chaque mot apparaît dans une liste :

```python
mots = ["litière", "banane", "litière", "poire", "banane", "litière"]

compte = {}                         # dictionnaire vide

for p in mots:
    if p in compte:
        compte[p] += 1
    else:
        compte[p] = 1

print(compte)   # {'pomme' : 3, 'banane' : 2, 'poire' : 1}
```

Il s'agit d'un modèle très important : dictionnaire comme **carte de fréquence**.

---

### 2.4. Dictionnaire de listes

Classes avec listes d'élèves.

```python
cours_2 = {
    "10A": ["Nain", "Bruno", "Carla"],
    "10B": ["David", "Veille", "Fabio"]
}

for classe, etudiants in cours_2.items():
    print(f"La classe {classe} compte {len(etudiants)} élèves.")
```

Ici, nous combinons :

- dictionnaire (`turma` → liste),
- fonction `len`,
- cycle `for` avec `items()`.

---

## 3. Mettre le tout ensemble dans les fonctions · [ESSENTIEL]

Une bonne pratique est de séparer :

- **les fonctions pures** (qui reçoivent des données, les calculent et les renvoient avec `return`);
- la partie du programme qui fait `input` et `print`.

### 3.1. Exemple : moyenne et nombre d'adultes

Tout d'abord, nous écrivons la fonction pour la **logique** :

```python
def moyen_et_superieur_ou_egal_a_18(age_2):
    total = 0
    plus_gros_comptes = 0

    for age in age_2:
        total += age
        if age >= 18:
            plus_gros_comptes += 1

    moyenne = total / len(age_2)
    return moyenne, plus_gros_comptes
```

Puis, dans le programme principal :

```python
def lire_les_ages(quantite):
    age_2 = []
    for _ in range(quantite):
        age = int(input("Âge: "))
        age_2.append(age)
    return age_2


if __name__ == "__principal__":
    age_2 = lire_les_ages(5)   # saisir
    moyenne, plus_gros_2 = moyen_et_superieur_ou_egal_a_18(age_2)  # traitement
    print("Âges moyens :", moyenne)                      # sortir
    print("Supérieur ou égal à 18 :", plus_gros_2)
```

Donc, si on veut **tester** la fonction `media_e_maiores_ou_iguais_18`, on peut l'appeler avec des listes inventées (sans `input`).

---

### 3.2. Exemple : trouver le plus ancien

```python
def plus_vieux(personnes):
    '''
    Reçoit un dictionnaire nom -> âge et renvoie le nom de la personne la plus âgée.
    '''
    # on suppose que le dictionnaire n'est pas vide
    nom_le_plus_ancien = None
    age_avance_2 = -1

    for nom, age in personnes.items():
        if age > age_avance_2:
            age_avance_2 = age
            nom_le_plus_ancien = nom

    return nom_le_plus_ancien
```

Programme principal :

```python
if __name__ == "__principal__":
    personnes = {
        "Nain": 16,
        "Bruno": 17,
        "Carla": 15
    }

    nom = plus_vieux(personnes)
    print("Personne âgée :", nom)
```

---

## 4. Stratégie étape par étape dans un problème plus vaste · [ESSENTIEL]

Prenons un énoncé un peu plus complet.

> "Dans une classe, chaque élève a un nom et des notes dans plusieurs matières. 
> C'est prévu à :
>
> - afficher la moyenne de chaque élève,
> - indiquer combien d'élèves ont au moins un négatif,
> - indiquer quel élève a la meilleure moyenne.”

### 4.1. Modéliser les données

On peut utiliser une structure imbriquée :

```python
classe = {
    "étudiants": [
        {"nom": "Nain", "remarques": {"Mathématiques": 18, "portugais": 16}},
        {"nom": "Bruno", "remarques": {"Mathématiques": 14, "portugais": 15}},
        {"nom": "Carla", "remarques": {"Mathématiques": 12, "portugais": 9}}
    ]
}
```

### 4.2. Décomposer en fonctions

Nous pouvons définir des fonctions telles que :

- Average_aluno(student) → renvoie la moyenne des notes de cet élève;
- count_students_with_negatives(class) → renvoie combien d'élèves ont au moins une note < 10;
- best_student(class) → renvoie le nom de l'étudiant ayant obtenu la moyenne la plus élevée.

### 4.3. Mise en œuvre progressive

1. Implémenter et tester media_aluno avec 1 étudiant.
2. Ensuite, utilisez media_aluno dans Melhor_aluno.
3. Enfin, écrivez count_students_with_negatives.

Exemple de Average_student :

```python
def eleve_moyen(etudiant):
    remarques = etudiant["remarques"].values()
    total = 0
    for avis in remarques:
        total += avis
    return total / len(remarques)
```

Exemple de counting_students_with_negatives :

```python
def compter_les_eleves_avec_des_resultats_negatifs(classe):
    comptoir = 0
    for etudiant in classe["étudiants"]:
        for avis in etudiant["remarques"].values():
            if avis < 10:
                comptoir += 1
                break           # On sait déjà que cet élève est négatif
    return comptoir
```

---

## 5. Erreurs typiques et débogage de base · [ESSENTIEL]

Quelques erreurs très courantes :

1. **Oublier le retour dans une fonction**

 - Résultat : la fonction renvoie Aucun et à partir de là le programme commence à échouer.

2. **Mélanger l'impression avec la logique**

 - Si une fonction imprime au lieu de renvoyer, vous ne pouvez pas réutiliser le résultat dans un autre calcul.

3. **Confondre = avec ==**

 - = attribue des valeurs ;
 - == compare les valeurs.

4. **Erreurs de plage dans la plage (un par un)**

 - N'oubliez pas : la plage (début, fin) va à la fin - 1.

5. **Changer la mauvaise variable dans les cycles ou les fonctions**
 - Exemples :
 - oublier i += 1 num while,
 - utiliser la mauvaise liste dans une annexe.

### 5.1. Conseils de débogage

- Imprime les valeurs intermédiaires (par exemple, dans des boucles) pour voir comment le programme pense.
- Teste les fonctions avec des données petites et faciles à prédire.
- Utilise l'assertion pour garantir que certaines conditions sont remplies :

```python
def somme(a, b):
    return a + b

assert somme(2, 3) == 5
assert somme(-1, 1) == 0
```

Si une assertion échoue, Python génère une erreur, ce qui aide à localiser le problème.

---

## 6. Exercices - Algorithmes et modèles de programmation

> Suggestion :
>
> - faites d'abord les exercices 1–6;
> - puis essayez 7–10;
> - 11 et 12 sont un peu plus difficiles.

---

### Exercice 1 - Compter les positifs, les négatifs et les zéros

Demandez à l'utilisateur n nombres (vous choisissez la valeur de n, par exemple 10) e:

1. Enregistrez-les dans une liste.
2. Comptez combien il y en a :
 - positif,
 - négatif,
 - égal à zéro.
3. À la fin, il affiche les 3 comptes.

Essayez d'identifier dans votre code les modèles de :

- lecture dans une liste,
- comptage conditionnel.

---

### Exercice 2 - Approuvé et failed

Crée une fonction count_passed_failed(notes) qui reçoit une liste de notes (0-20) et :

- renvoie deux valeurs :
 - nombre de personnes approuvées (note ≥ 10),
 - nombre d'échecs (note < 10).

In le programme principal :

1. Créez une liste avec quelques notes (peut être corrigée ou demandée à l'utilisateur).
2. Appelle la fonction et affiche le résultat.

---

### Exercice 3 - Minimum et maximum manuels

Ecrire une fonction min_max(list_numbers) qui :

- reçoit une liste de nombres,
- renvoie un tuple (minimum, maximum),
- n'utilise pas min() ou max().

Tests avec au moins 3 listes 

---

### Exercice 4 - Filtrer les pairs et les impairs

Écrire une fonction Separate_even_odd(list_numbers) qui :

- reçoit une liste d'entiers,
- renvoie deux listes :
 - une avec des nombres pairs nombres,
 - un autre avec des nombres impairs.

Dans le programme principal :

- crée une liste avec des nombres de 1 à 20,
- appelle la fonction et affiche les deux listes.

---

### Exercice 5 - Transformation : carrés de nombres

Écrire une fonction squares(list_numbers) qui :

- reçoit une liste de nombres,
- renvoie une nouvelle liste avec le carré de chaque nombre.

Test :

- carrés([1, 2, 3, 4]) → [1, 4, 9, 16].

---

### Exercice 6 - Produits et prix

Crée un dictionnaire de prix dans lequel :

- les clés sont des noms de produits (ex. : "pain", "lait", "jus"),
- le les valeurs sont les prix respectifs (flottants).

Écrivez une fonction product_more_expensive(prices) qui :

- reçoit le dictionnaire,
- renvoie le nom du produit avec le prix le plus élevé,
- n'utilise pas max() directement dans price.values() (fait le minimum/maximum manuellement à l'aide d'un cycle).

---

### Exercice 7 - Âges et majorité

Crée un dictionnaire des âges (nom → âge) et écrit une fonction stats_ages(ages) qui renvoie :

- l'âge moyen,
- combien de personnes sont supérieures ou égales à 18 ans.

Dans le programme principal, il affiche un rapport de ce type :

```text
Média das idades: X
Maiores ou iguais a 18: Y
```

---

### Exercice 8 - Compter les élèves par classe

Créer un dictionnaire de classes dans lequel :

- les clés sont des noms de classes (ex. : "10A", "10B"),
- les valeurs sont des listes avec les noms de étudiants.

Écrire une fonction count_students_per_turma(classes) qui :

- reçoit ce dictionnaire,
- renvoie un nouveau dictionnaire avec :
 - les mêmes clés,
 - comme valeur, le nombre d'élèves dans chaque classe.

Au final, cela montre quelque chose du genre :

```text
Turma 10A -> 3 alunos
Turma 10B -> 4 alunos
```

---

### Exercice 9 - Échec par classe

Utilisez une structure similaire à la structure de classe de la section 4 (avec étudiants et notes par matière) et écrivez une fonction :

failed_by_class(classes) qui :

- reçoit un dictionnaire des classes,
- pour chaque classe, compte combien d'élèves ont au moins un négatif,
- renvoie un dictionnaire du type :
 - "10A" -> nombre d'élèves avec des négatifs, etc.

Il affiche ensuite un petit rapport par classe.

---

### Exercice 10 - Algorithme en portugais (pas de code au préalable)

Lisez attentivement cet énoncé :

> « Dans une école, chaque élève participe à diverses activités (club de robotique, sport, musique, etc.). 
> Le but est de créer un programme qui :
>
> - demande le nom de chaque élève et les activités auxquelles il participe,
> - vous permet de voir combien d'élèves participent à chaque activité,
> - vous permet de voir à quelles activités un élève spécifique participe. Identification de :
 - entrées,
 - traitements,
 - sorties.
2. Conception d'une éventuelle structure de données (quelles listes et dictionnaires utiliseriez-vous ?).
3. Planifiez par étapes numérotées (pseudocode) comment le programme pourrait fonctionner.

Seulement ensuite, si vous le souhaitez, essayez de commencer la programmation.

---

### Exercice 11 (Défi) - Compteur de fréquence de lettres

Écrire une fonction count_letras(text) qui :

- reçoit une chaîne,
- renvoie un dictionnaire dans lequel :
 - les clés sont des lettres (en ignorant les espaces),
 - les valeurs correspondent au nombre de fois où chaque lettre apparaît.

Exemple :

- "banane" → {'b' : 1, 'a' : 3, 'n' : 2}

Conseil : vous pouvez d'abord convertir le texte en minuscules et l'ignorer espaces.

---

### Exercice 12 (Défi) - Refactoriser avec des fonctions

Choisissez l'un des programmes que vous avez déjà réalisés (par exemple, celui qui fonctionne avec les classes, les notes ou les températures) et :

1. Analyse le code actuel.
2. Identifie les parties répétées et les blocs logiques (par exemple « calculer la moyenne », « la liste a échoué »).
3. Créez au moins 3 fonctions pour organiser le code :
 - chacune avec un nom clair,
 - avec return au lieu d'imprimer (quand cela a du sens).
4. Testez à nouveau le programme et confirmez qu'il se comporte de la même manière.

---

## 7. Changelog

> Journal des modifications apportées à ce fichier.

- **2025-11-17 · v1.1**
 - Table des matières mise à jour.
- **2025-11-17 · v1.0**
 - Création initiale du document.
 - Ajout de sections sur :
 - stratégie d'attaque des problèmes (entrée/traitement/sortie et pseudocode),
 - modèles classiques avec listes (accumulation, comptage, min/max, filtrage, transformation),
 - modèles avec dictionnaires (base de données simple, comptage de fréquence, dictionnaire de listes),
 - regrouper tout en fonctions (exemples avec âges et classes),
 - erreurs typiques et conseils de débogage.
 - 12 exercices progressifs créés, y compris des défis avec des dictionnaires et la refactorisation de code dans fonctions.
