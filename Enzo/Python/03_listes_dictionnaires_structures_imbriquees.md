# Python (10e année) - 03 · Listes, dictionnaires et structures imbriquées

> **Objectif de ce fichier** 
> Consolider le stockage des collections de données en Python (listes et dictionnaires) et commencer à penser de manière plus structurée avec des structures imbriquées.

---

## Index

- [0. Comment utiliser ce fichier](#0-comment-utiliser-ce-fichier)
- [1. Listes](#1-listes)
- [2. Dictionnaires](#2-dictionnaires)
- [3. Structures de données imbriquées](#3-structures-de-donnees-imbriquees)
- [4. Exemples appliqués](#4-exemples-appliques)
- [5. Exercices (Listes, Dictionnaires et Structures Imbriquées)](#5-exercices-listes-dictionnaires-et-structures-imbriquees)
- [6. Changelog](#6-changelog)

---

## 0. Comment utiliser ce fichier

1. Lisez attentivement l'explication théorique.
2. Essayez tous les exemples dans un fichier `.py`.
3. Apportez de petites modifications pour comprendre l'effet (modifier les valeurs, ajouter des éléments, etc.).
4. À la fin, résolvez les **exercices**. Commencez par les plus simples et essayez de relever les défis.

Ce fichier est lié aux précédents :

- `01_introduction_variables_types_strings_io.md`
- `02_operateurs_et_controle_de_flux_if_boucles.md`

---

## 1. Listes

### 1.1. Qu'est-ce qu'une liste ?

Une **liste** est une collection ordonnée d'éléments.  
Chaque élément a une **position** (index) commençant à 0.

Exemples de listes :

```python
nombres = [10, 20, 30]              # liste d'entiers
noms = ["Nain", "Bruno", "Carla"]   # liste de chaînes
melange = [10, "Nain", True, 3.14]   # liste avec différents types
```

- Les listes sont **mutables** : vous pouvez modifier, ajouter et supprimer des éléments.
- Elles peuvent contenir tout type de données, y compris d'autres listes.

---

### 1.2. Accès par index

Comme pour les chaînes, les index vont de `0` à `len(lista) - 1`.

```python
l = [3, 1, 4]

print(l[0])    # 3 (premier élément)
print(l[1])    # 1
print(l[2])    # 4 (dernier élément)
print(l[-1])   # 4 (compte d'index négatif à partir de la fin)
```

Si vous essayez d'accéder à un index invalide (`l[10]` dans une liste de 3 éléments), vous obtiendrez une erreur `IndexError`.

---

### 1.3. Modifier des éléments

Les listes étant mutables, vous pouvez modifier directement les éléments :

```python
remarques = [12, 15, 9]

remarques[2] = 10    # change le troisième élément (index 2)
print(remarques)    # [12, 15, 10]
```

---

### 1.4. Liste importante des méthodes

Quelques méthodes couramment utilisées :

```python
l = [3, 1, 4]

l.append(1)        # ajoute 1 à la fin -> [3, 1, 4, 1]
l.insert(1, 7)     # insère 7 à l'index 1 -> [3, 7, 1, 4, 1]
dernier = l.pop()   # supprime et renvoie le dernier élément (1)
l.remove(7)        # supprime la PREMIÈRE occurrence de 7
l.clear()          # supprime tous les éléments -> []
```

Regardons de plus près :

- `append(x)` - ajoute `x` à la fin.
- `insert(i, x)` - insère `x` en position `i`, en déplaçant le reste.
- `pop()` - supprime et renvoie le dernier element.
- `pop(i)` - supprime et renvoie l'élément à l'index `i`.
- `remove(x)` - supprime la première occurrence de `x` (si elle n'existe pas, cela donne une erreur).
- `clear()` - vide la liste.

Méthodes d'analyse plus utiles :

```python
l = [3, 1, 4, 1, 5, 9]

comptez_en_quelques_uns = l.count(1)   # Combien de fois 1 apparaît-il ?
idx_quatre = l.index(4)  # indice de la première occurrence de 4

l.sort()                 # trier la liste (sur place)
l.reverse()              # inverser l'ordre (sur place)

print(l)
```

---

### 1.5. Fonctions utiles : `len`, `sum`, `min`, `max`, `sorted`

En plus des méthodes, il existe des fonctions qui fonctionnent avec des listes :

```python
chiffres = [10, 20, 5, 15]

print(len(chiffres))      # 4 (nombre d'éléments)
print(sum(chiffres))      # 50 (somme des éléments)
print(min(chiffres))      # 5 (minimum)
print(max(chiffres))      # 20 (maximum)

ordonne = sorted(chiffres)        # renvoie une NOUVELLE liste ordonnée
print(ordonne)                # [5, 10, 15, 20]
print(chiffres)                    # [10, 20, 5, 15] (pas modifié)
```

- `sorted(lista)` ne modifie pas la liste d'origine ; renvoie une copie ordonnée.
- `lista.sort()` modifie la liste elle-même.

---

### 1.6. Parcourez les listes avec `for`

Le modèle le plus courant est :

```python
nombres = [2, 4, 6, 8]
carres = []

for n in nombres:
    carres.append(n ** 2)

print(carres)   # [4, 16, 36, 64]
```

Vous pouvez également parcourir par **index** :

```python
noms = ["Nain", "Bruno", "Carla"]

for i in range(len(noms)):
    print(i, noms[i])
```

---

### 1.7. Modèles classiques avec listes

1. **Créez une nouvelle liste à partir d'une autre**

```python
nombres = [1, -3, 5, -2, 0, 10]
positif = []

for n in nombres:
    if n > 0:
        positif.append(n)

print(positif)   # [1, 5, 10]
```

2. **Calculez la moyenne**

```python
remarques = [12, 15, 9, 18]

somme = 0
for n in remarques:
    somme += n

moyenne = somme / len(remarques)
print("Moyenne =", moyenne)
```

3. **Trouver le minimum/maximum sans `min`/`max`**

```python
nombres = [10, 3, 7, 2, 9]

plus_petit = nombres[0]
for n in nombres:
    if n < plus_petit:
        plus_petit = n

print("Le plus petit nombre :", plus_petit)
```

---

### 1.8. Compréhensions de listes (fait amusant)

Une **compréhension de liste** est une manière compacte de construire des listes.

Exemples équivalents :

```python
# Forme "normale"
donnees = [1, 2, 3, 4, 5]
double = []

for x in donnees:
    double.append(x * 2)

# Compréhension de la liste
double2 = [x * 2 for x in donnees]

print(double2)   # [2, 4, 6, 8, 10]
```

Sous condition :

```python
paires = [x for x in donnees if x % 2 == 0]   # [2, 4]
```

Pour l'instant, l'important est de comprendre qu'il existe ; utilisez la forme « normale » lorsque vous apprenez et utilisez la compréhension lorsque vous vous sentez plus à l'aise.

---

## 2. Dictionnaires

### 2.1. Idée clé → valeur

Un **dictionnaire** est une collection de `chave: valor` paires.

Exemples :

```python
personne = {
    "nom": "Ana Silva",
    "âge": 28,
    "profession": "Ingénieur"
}

prix_2 = {
    "litière": 0.79,
    "banane": 0.35,
    "poire": 1.05
}
```

- Les **clés** sont normalement des chaînes, mais peuvent être d'autres types immuables.
- Les **valeurs** peuvent être n'importe quoi (nombres, chaînes, listes, dictionnaires, etc.).

---

### 2.2. Accéder et mettre à jour les valeurs

```python
personne = {
    "nom": "Ana Silva",
    "âge": 28,
    "profession": "Ingénieur"
}

print(personne["nom"])    # "Ana Silva"

personne["âge"] = 29     # âge de mise à jour
personne["ville"] = "Lisbonne"  # nouvelle clé/valeur

print(personne)
```

Si vous essayez d'accéder à une clé qui n'existe pas (`pessoa["altura"]`), cela donne l'erreur `KeyError`.

---

### 2.3. La méthode `get`

`get` permet d'accéder à une clé avec une **valeur par défaut** si la clé n'existe pas.

```python
personne = {
    "nom": "Ana Silva",
    "âge": 28
}

nom = personne.get("nom", "Inconnu")
hauteur = personne.get("hauteur", "Non défini")

print(nom)    # "Ana Silva"
print(hauteur)  # "Non défini"
```

---

### 2.4. Supprimer des éléments

```python
personne = {
    "nom": "Ana Silva",
    "âge": 28,
    "profession": "Ingénieur"
}

prof = personne.pop("profession")   # supprime et renvoie la valeur
print(prof)        # "Ingénieur"
print(personne)      # il n'a plus de "métier"

# Une autre façon :
del personne["âge"]    # supprimer la clé "âge"
```

---

### 2.5. Parcourir les dictionnaires : `keys`, `values`, `items`

Exemple avec dictionnaire de prix :

```python
prix_2 = {"litière": 0.79, "banane": 0.35, "poire": 1.05, "raisin": 2.40}

# Parcourir les CLÉS
for fruit in prix_2.keys():
    print(fruit, "->", prix_2[fruit])

# Forme courte (équivalente à precos.keys()) :
for fruit in prix_2:
    print("Clé:", fruit)

# Parcourir les VALEURS
total = 0.0
for valeur in prix_2.values():
    total += valeur

moyenne = total / len(prix_2)
print("Prix ​​moyens :", round(moyenne, 2))

# Parcourez les PAIRES (clé, valeur)
for fruit, valeur in prix_2.items():
    print(f"{fruit} coûte {valeur:.2f} euros")
```

---

### 2.6. Vérifier l'existence des clés (`in`)

```python
prix_2 = {"litière": 0.79, "banane": 0.35, "poire": 1.05}

print("banane" in prix_2)         # Vrai (la clé existe)
print("orange" in prix_2)        # FAUX

if "poire" in prix_2:
    print("Nous avons un prix poire :", prix_2["poire"])
```

---

## 3. Structures de données imbriquées

Combinons maintenant des listes et des dictionnaires pour représenter des informations plus riches.

---

### 3.1. Liste de listes (matrice)

Une **matrice** peut être représentée comme une liste de listes :

```python
quartier_general = [
    [1, 2, 3],   # ligne 0
    [4, 5, 6],   # ligne 1
    [7, 8, 9]    # ligne 2
]

print(quartier_general[0])       # [1, 2, 3]
print(quartier_general[1][2])    # 6 (ligne 1, colonne 2)
```

Parcourir le tableau :

```python
print("Quartier général:")
for doubler in quartier_general:         # chaque ligne est une liste
    print(doubler)
```

Ajouter une nouvelle ligne :

```python
nouvelle_ligne = [10, 11, 12]
quartier_general.append(nouvelle_ligne)

print("Matrice mise à jour :")
for doubler in quartier_general:
    print(doubler)
```

---

### 3.2. Dictionnaire des listes (classes et étudiants)

```python
cours_2 = {
    "10A": ["Nain", "Bruno", "Carla"],
    "10B": ["David", "Veille", "Fabio"]
}

for classe, etudiants in cours_2.items():
    print(f"Classe {classe} :")
    for etudiant in etudiants:
        print(" -", etudiant)
```

Ajouter un nouvel élève et une nouvelle classe :

```python
cours_2["10B"].append("Gabriela")    # nouvel élève en 10B
cours_2["10C"] = ["Hélène", "Igor"]  # nouvelle classe
```

---

### 3.3. Dictionnaire des dictionnaires (notes par sujet)

```python
remarques = {
    "Nain":   {"Mathématiques": 18, "portugais": 16},
    "Bruno": {"Mathématiques": 14, "portugais": 15}
}

note_mathematique = remarques["Nain"]["Mathématiques"]
print("Note mathématique d'Ana :", note_mathematique)
```

Défilement :

```python
for etudiant, disciplines in remarques.items():
    print(f"Notes de {etudiant} :")
    for discipline, avis in disciplines.items():
        print(f" - {discipline} : {avis}")
```

Ajouter un nouveau sujet et un nouvel élève :

```python
remarques["Nain"]["Anglais"] = 17
remarques["Carla"] = {"Mathématiques": 19, "portugais": 18}
```

Calculer la moyenne d'un élève :

```python
cible = "Nain"
ajoute_des_notes = 0
nombre_de_sujets = 0

for discipline, avis in remarques[cible].items():
    ajoute_des_notes += avis
    nombre_de_sujets += 1

moyenne = ajoute_des_notes / nombre_de_sujets
print(f"Moyenne {cible} : {moyenne:.2f}")
```

---

### 3.4. Liste des dictionnaires (livres, étudiants, etc.)

Exemple : liste de livres.

```python
livres = [
    {"titre": "1984", "auteur": "Georges Orwell", "année": 1949, "genre": "Dystopie"},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "année": 1954, "genre": "Fantaisie"},
    {"titre": "don Quichotte", "auteur": "Miguel de Cervantès", "année": 1605, "genre": "Classique"}
]

print("Liste des livres :")
for livre in livres:
    print(f"Titre : {livre['titulo']}, Auteur : {livre['autor']}, Année : {livre['ano']}, Genre : {livre['genero']}")
```

Rechercher un livre par titre (en ignorant les majuscules/minuscules) :

```python
titre_recherche = input("Entrez le titre du livre que vous recherchez : ")

trouve = False
for livre in livres:
    if livre["titre"].lower() == titre_recherche.lower():
        print("Livre trouvé :")
        print(f"Titre : {livre['titulo']}, Auteur : {livre['autor']}, Année : {livre['ano']}, Genre : {livre['genero']}")
        trouve = True
        break

if not trouve:
    print("Livre introuvable.")
```

Autre exemple : liste d'étudiants avec des dictionnaires simples :

```python
etudiants = [
    {"nom": "Nain", "âge": 16},
    {"nom": "Bruno", "âge": 17}
]

for etudiant in etudiants:
    print(f"{etudiant['nome']} a {etudiant['idade']} ans")

nouvel_etudiant = {"nom": "Carla", "âge": 16}
etudiants.append(nouvel_etudiant)
```

---

## 4. Exemples appliqués

### 4.1. Températures mensuelles

Nous utiliserons une liste de températures mensuelles moyennes et une liste de noms de mois.

```python
temperatures = [15.5, 16.0, 18.2, 20.1, 22.5, 25.0, 27.3, 26.8, 24.0, 20.5, 17.8, 15.2]
mois = ["Janvier", "Février", "Mars", "Avril", "Peut", "Juin",
         "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
```

Consulter la température sur un mois :

```python
mois_recherche = int(input("Numéro du mois (1-12) : "))

if 1 <= mois_recherche <= 12:
    indice = mois_recherche - 1
    print(f"La température moyenne à {mois[indice]} est de {temperatures[indice]} °C.")
else:
    print("Mois invalide.")
```

Calculez la moyenne annuelle :

```python
moyenne_annuelle = sum(temperatures) / len(temperatures)
print(f"Température annuelle moyenne : {moyenne_annuelle:.2f} °C")
```

Trouver le mois le plus chaud et le plus froid (avec `max`/`min`) :

```python
indice_chaud = temperatures.index(max(temperatures))
indice_de_froid = temperatures.index(min(temperatures))

print(f"Mois le plus chaud : {mois[indice_chaud]} ({temperatures[indice_chaud]} °C)")
print(f"Mois le plus froid : {mois[indice_de_froid]} ({temperatures[indice_de_froid]} °C)")
```

Vous pouvez également essayer de faire cela **sans** utiliser `max` et `min`, en utilisant un cycle et des comparaisons.

---

### 4.2. Classes et élèves (structure plus complexe)

Exemple plus complet, regroupant le tout : dictionnaire de classe, chaque classe avec :

- liste des élèves (chaque élève est un dictionnaire avec `nome` et `notas`),
- nom de l'enseignant.

```python
cours_2 = {
    "10A": {
        "étudiants": [
            {"nom": "Nain", "remarques": {"Mathématiques": 18, "portugais": 16}},
            {"nom": "Bruno", "remarques": {"Mathématiques": 14, "portugais": 15}},
            {"nom": "Carla", "remarques": {"Mathématiques": 12, "portugais": 14}}
        ],
        "professeur": "M. Silva"
    },
    "10B": {
        "étudiants": [
            {"nom": "David", "remarques": {"Mathématiques": 10, "portugais": 12}},
            {"nom": "Veille", "remarques": {"Mathématiques": 9, "portugais": 11}},
            {"nom": "Fabio", "remarques": {"Mathématiques": 15, "portugais": 14}}
        ],
        "professeur": "Mme Costa"
    }
}
```

Afficher la liste des élèves et les notes par classe :

```python
for classe, infos in cours_2.items():
    print(f"Classe {classe} :")
    for etudiant in infos["étudiants"]:
        print(f"  Élève : {etudiant['nome']}, Notes : {etudiant['notas']}")
    print()
```

Comptez combien d'élèves ont au moins un résultat négatif (note < 10) dans chaque classe :

```python
for classe, infos in cours_2.items():
    nombre_negatif = 0
    for etudiant in infos["étudiants"]:
        for avis in etudiant["remarques"].values():
            if avis < 10:
                nombre_negatif += 1
                break   # Compter l'élève une seule fois
    print(f"La classe {classe} compte {nombre_negatif} élèves avec au moins un point négatif.")
```

Recherchez un élève et indiquez-lui dans quelle classe il se trouve :

```python
nom_recherche = input("Nom de l'étudiant à rechercher : ")
trouve = False

for classe, infos in cours_2.items():
    for etudiant in infos["étudiants"]:
        if etudiant["nom"].lower() == nom_recherche.lower():
            print(f"L'élève {nom_recherche} est en classe {classe} avec les notes : {etudiant['notas']}")
            trouve = True
            break
    if trouve:
        break

if not trouve:
    print("Étudiant introuvable.")
```

---

## 5. Exercices (Listes, dictionnaires et structures imbriquées)

> Essayez de résoudre ces exercices en utilisant uniquement ce qui se trouve dans ce fichier et les précédents.  
> Certains sont des adaptations d'exercices que vous avez déjà réalisés, mais ils sont désormais organisés par thème.

### Exercice 1 - Liste de base et index

Créez une liste avec au moins 5 nombres de votre choix.  
Le programme doit :

1. Afficher la liste complète.
2. Afficher le premier élément.
3. Afficher le dernier élément.
4. Afficher la longueur de la liste avec `len()`.

> Résolution :

```python
nombres = [10, 25, -3, 42, 7]
print("Liste complète :", nombres)
print("Premier élément :", nombres[0])
print("Dernier élément :", nombres[-1])
print("Longueur de la liste :", len(nombres))
```

---

### Exercice 2 - Positifs, négatifs et zéros (liste)

Demande 5 nombres à l'utilisateur et les stocke dans une liste.  
Ensuite, il parcourt la liste et, pour chaque numéro, imprime s'il est :

- positif,
- négatif,
- ou zéro.

> Résolution :

```python
nombres = []
for _ in range(5):
    n = float(input("Entrez un numéro : "))
    nombres.append(n)

for n in nombres:
    if n > 0:
        print(n, "est positif")
    elif n < 0:
        print(n, "est négatif")
    else:
        print(n, "est nul")
```

---

### Exercice 3 - Majeur et mineur sans `max`/`min`

Demande à l'utilisateur 10 nombres et les stocke dans une liste.

- Sans utiliser `max()` ou `min()`, savoir lequel est le le plus grand et le plus petit nombre en utilisant un cycle `for` et des comparaisons.
- À la fin, il affiche les deux valeurs.

> Résolution :

```python
nombres = []
for i in range(10):
    n = float(input("Entrez un numéro : "))
    nombres.append(n)

plus_gros = nombres[0]
plus_petit = nombres[0]

for n in nombres:
    if n > plus_gros:
        plus_gros = n
    if n < plus_petit:
        plus_petit = n
print("Le plus grand nombre :", plus_gros)
print("Le plus petit nombre :", plus_petit)
```

---

### Exercice 4 - Séparer les nombres impairs et pairs

Demande à l'utilisateur de saisir 10 nombres entiers et de les enregistrer dans une liste.  
Après :

1. Crée une nouvelle liste avec uniquement des nombres pairs.
2. Crée une autre liste avec uniquement des nombres impairs.
3. Affiche les deux listes.

> Résolution :

```python
nombres = []
for _ in range(10): # Puisque nous n'aurons pas besoin de l'index, nous utilisons _
    n = int(input("Saisissez un entier : "))
    nombres.append(n)

paires = []
impair = []
for n in nombres:
    if n % 2 == 0:
        paires.append(n)
    else:
        impair.append(n)

print("Nombres pairs :", paires)
print("Nombres impairs :", impair)
```

---

### Exercice 5 - Dictionnaire de personnes simple

Créez un dictionnaire qui représente une personne avec les clés :

- `"nome"`,
- `"idade"`,
- `"profissao"`.

Après :

1. Affiche proprement les informations sur la personne (avec `print` et f-strings).
2. Met à jour l'âge (par exemple, somme 1).
3. Ajoute une clé `"cidade"`.
4. Supprime la clé `"profissao"` avec `pop` ou `del`.
5. Affiche le dictionnaire final.

> Résolution :

```python
personne = {
    "nom": "Jean Silva",
    "âge": 30,
    "profession": "Programmeur"
}

print(f"Nom : {personne['nome']}, Âge : {personne['idade']}, Profession : {personne['profissao']}") # 1
personne["âge"] += 1 # 2
personne["ville"] = "Port" # 3
personne.pop("profession")  # ou : de la personne["profession"] #4
print("Dictionnaire ultime :", personne) # 5
```

---

### Exercice 6 - Festival gastronomique (dictionnaire des dictionnaires)

Utilisez le dictionnaire d'étal suivant lors d'un festival gastronomique :

```python
stalles = {
    "TacoTron":   {"ventes": 184, "prix_moyen": 6.5, "évaluation": 4.6},
    "Bao&Buns":   {"ventes": 149, "prix_moyen": 7.0, "évaluation": 4.8},
    "PokéWave":   {"ventes": 132, "prix_moyen": 9.0, "évaluation": 4.2},
    "PastelPower":{"ventes": 210, "prix_moyen": 2.0, "évaluation": 4.9},
    "VégéVolt": {"ventes": 98,  "prix_moyen": 8.5, "évaluation": 4.4}
}
```

1. Dites-nous quel restaurant a obtenu la **meilleure note**.
2. Calculez, pour chaque restaurant, combien d'argent il a gagné (`vendas * preco_medio`).
3. Dites-nous quel restaurant a gagné **le plus d'argent**.

> Résolution :

```python
stalles = {
    "TacoTron":   {"ventes": 184, "prix_moyen": 6.5, "évaluation": 4.6},
    "Bao&Buns":   {"ventes": 149, "prix_moyen": 7.0, "évaluation": 4.8},
    "PokéWave":   {"ventes": 132, "prix_moyen": 9.0, "évaluation":  4.2},
    "PastelPower":{"ventes": 210, "prix_moyen": 2.0, "évaluation": 4.9},
    "VégéVolt": {"ventes": 98,  "prix_moyen": 8.5, "évaluation": 4.4}
}

# 1. Meilleure note
meilleure_note = 0
meilleur_restaurant = ""
for nom, infos in stalles.items():
    if infos["évaluation"] > meilleure_note:
        meilleure_note = infos["évaluation"]
        meilleur_restaurant = nom
print("Restaurant le mieux noté :", meilleur_restaurant, "avec", meilleure_note)

# 2. L'argent gagné par chaque restaurant
argent_gagne = {}
for nom, infos in stalles.items():
    total = infos["ventes"] * infos["prix_moyen"]
    argent_gagne[nom] = total
    print(f"{nom} a gagné {total:.2f} euros.")

# 3. Le restaurant qui a gagné le plus d'argent
plus_d_argent = 0
restaurant_riche = ""
for nom, total in argent_gagne.items():
    if total > plus_d_argent:
        plus_d_argent = total
        restaurant_riche = nom
print("Restaurant qui a gagné le plus d'argent :", restaurant_riche, "avec", plus_d_argent)
```

---

### Exercice 7 - Matrice 3x3

Créez une matrice 3x3 (liste de listes) avec des entiers de votre choix.

1. Affiche la matrice ligne par ligne.
2. Ajoute une nouvelle ligne à la matrice.
3. Calcule la somme de tous les éléments du tableau (avec cycles imbriqués).

> Résolution :

```python
quartier_general = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Montrez la matrice
print("Quartier général:")
for doubler in quartier_general:
    print(doubler)

# 2. Ajouter une nouvelle ligne
nouvelle_ligne = [10, 11, 12]
quartier_general.append(nouvelle_ligne)
print("Matrice mise à jour :")
for doubler in quartier_general:
    print(doubler)

# 3. Somme de tous les éléments
somme_totale = 0
for doubler in quartier_general:
    for element in doubler:
        somme_totale += element
print("Somme de tous les éléments du tableau :", somme_totale)
```

---

### Exercice 8 - Classes et étudiants (dictionnaire de listes)

Crée un dictionnaire de listes où :

- les clés sont des noms de classe (par exemple, `"10A"`, `"10B"`),
- les valeurs sont des listes d'étudiants noms.

Le programme doit :

1. Afficher la liste des élèves de chaque classe.
2. Ajouter une nouvelle classe avec quelques étudiants.
3. Afficher le dictionnaire mis à jour.

> Résolution :

```python
cours_2 = {
    "10A": ["Nain", "Bruno", "Carla"],
    "10B": ["David", "Veille", "Fabio"]
}

# 1. Afficher la liste des étudiants par classe
for classe, etudiants in cours_2.items():
    print(f"Classe {classe} : {etudiants}")

# 2. Ajouter une nouvelle classe
cours_2["10C"] = ["Gabriela", "Hélène", "Igor"]

# 3. Afficher le dictionnaire mis à jour
print("Dictionnaire de classe mis à jour :")
for classe, etudiants in cours_2.items():
    print(f"Classe {classe} : {etudiants}")
```

---

### Exercice 9 - Classes avec notes (structure imbriquée)

Utilise la structure `turmas` présentée dans la section 4.2 (chaque classe a une liste d'élèves avec des notes et un enseignant).

Le programme doit :

1. Afficher, pour chaque classe, la liste des élèves avec leurs notes respectives.
2. Pour chaque classe, indiquez combien d'élèves ont au moins un point négatif.
3. Demandez à l'utilisateur le nom de l'élève et indiquez :
 - dans quelle classe il se trouve,
 - quelles sont ses notes.

> Résolution :

```python
# Utilisez la structure de classe de l'exemple précédent
# 1. Afficher les élèves et les notes par classe
for classe, infos in cours_2.items():
    print(f"Classe {classe} :")
    for etudiant in infos["étudiants"]:
        print(f"  Élève : {etudiant['nome']}, Notes : {etudiant['notas']}")
    print()
# 2. Comptez les étudiants avec des résultats négatifs
for classe, infos in cours_2.items():
    nombre_negatif = 0
    for etudiant in infos["étudiants"]:
        for avis in etudiant["remarques"].values():
            if avis < 10:
                nombre_negatif += 1
                break
    print(f"La classe {classe} compte {nombre_negatif} élèves avec au moins un point négatif.")
# 3. Rechercher un étudiant
nom_recherche = input("Nom de l'étudiant à rechercher : ")
trouve = False
for classe, infos in cours_2.items():
    for etudiant in infos["étudiants"]:
        if etudiant["nom"].lower() == nom_recherche.lower():
            print(f"L'élève {nom_recherche} est en classe {classe} avec les notes : {etudiant['notas']}")
            trouve = True
            break
    if trouve:
        break
if not trouve:
    print("Étudiant introuvable.")
```

---

### Exercice 10 - Base de données de livres (liste de dictionnaires)

Crée une liste de dictionnaires, où chaque dictionnaire représente un livre avec :

- `"titulo"`,
- `"autor"`,
- `"ano"`,
- `"genero"`.

Le programme doit :

1. Montrez tous les livres de manière organisée.
2. Demandez à l'utilisateur un titre et, si le livre existe dans la liste, affichez ses informations complètes.
3. S'il n'existe pas, indiquez que le livre n'a pas été trouvé.

> Résolution :

```python
livres = [
    {"titre": "1984", "auteur": "Georges Orwell", "année": 1949, "genre": "Dystopie"},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "année": 1954, "genre": "Fantaisie"},
    {"titre": "don Quichotte", "auteur": "Miguel de Cervantès", "année": 1605, "genre": "Classique"}
]

# 1. Afficher tous les livres
print("Liste des livres :")
for livre in livres:
    print(f"Titre : {livre['titulo']}, Auteur : {livre['autor']}, Année : {livre['ano']}, Genre : {livre['genero']}")
# 2. Demander un titre et une recherche
titre_recherche = input("Entrez le titre du livre que vous recherchez : ")
trouve = False
for livre in livres:
    if livre["titre"].lower() == titre_recherche.lower():
        print("Livre trouvé :")
        print(f"Titre : {livre['titulo']}, Auteur : {livre['autor']}, Année : {livre['ano']}, Genre : {livre['genero']}")
        trouve = True
        break
if not trouve:
    print("Livre introuvable.")
```

---

### Exercice 11 - Températures mensuelles

Utilise deux listes :

- `temperaturas` avec 12 valeurs (une par mois),
- `meses` avec les noms de mois.

Le programme doit :

1. Demandez à l'utilisateur le numéro d'un mois (1 à 12) et affichez la température de ce mois.
2. Calculez la température annuelle moyenne.
3. Indiquer le mois le plus chaud et le mois le plus froid :
 - Version A : utilisant `max`, `min` et `index`.
 - Version B (défi) : sans `max`/`min`, uniquement avec cycles et comparaisons.

> Résolution :

```python
temperatures = [15.5, 16.0, 18.2, 20.1, 22.5, 25.0, 27.3, 26.8, 24.0, 20.5, 17.8, 15.2]
mois = ["Janvier", "Février", "Mars", "Avril", "Peut", "Juin",
         "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

# 1. Demandez le numéro du mois et affichez la température
mois_recherche = int(input("Numéro du mois (1-12) : "))
if 1 <= mois_recherche <= 12:
    indice = mois_recherche - 1
    print(f"La température moyenne à {mois[indice]} est de {temperatures[indice]} °C.")
else:
    print("Mois invalide.")

# 2. Calculer la moyenne annuelle
moyenne_annuelle = sum(temperatures) / len(temperatures)
print(f"Température annuelle moyenne : {moyenne_annuelle:.2f} °C")

# 3. Mois le plus chaud et le plus froid (Version A)
indice_chaud = temperatures.index(max(temperatures))
indice_de_froid = temperatures.index(min(temperatures))
print(f"Mois le plus chaud : {mois[indice_chaud]} ({temperatures[indice_chaud]} °C)")
print(f"Mois le plus froid : {mois[indice_de_froid]} ({temperatures[indice_de_froid]} °C)")
# Version B (défi)
plus_de_temps = temperatures[0]
temperature_inferieure = temperatures[0]
indice_plus_eleve = 0
indice_mineur = 0
for i in range(len(temperatures)):
    if temperatures[i] > plus_de_temps:
        plus_de_temps = temperatures[i]
        indice_plus_eleve = i
    if temperatures[i] < temperature_inferieure:
        temperature_inferieure = temperatures[i]
        indice_mineur = i
print(f"(Défi) Mois le plus chaud : {mois[indice_plus_eleve]} ({plus_de_temps} °C)")
print(f"(Défi) Mois le plus froid : {mois[indice_mineur]} ({temperature_inferieure} °C)")
```

---

### Exercice 12 (Défi) - Système de gestion scolaire simple

Créer une structure de données (à l'aide de listes et de dictionnaires) pour représenter :

- plusieurs classes,
- chaque classe avec une liste d'élèves,
- chaque élève avec un nom et un dictionnaire de notes pour diverses matières.

Le programme doit permettre (par menu simple ou séquentiellement) :

1. Afficher toutes les classes et leurs élèves.
2. Afficher les notes d'un étudiant spécifique (demande de l'utilisateur).
3. Pour une classe choisie, indiquez combien d'élèves ont une moyenne ≥ 10.

Vous pouvez commencer avec des données fixes dans le code (sans `input()` pour créer la structure) et vous concentrer sur le parcours et l'analyse de la structure.

> Résolution :

```python
cours_2 = {
    "10A": {
        "étudiants": [
            {"nom": "Nain", "remarques": {"Mathématiques": 18, "portugais": 16}},
            {"nom": "Bruno", "remarques": {"Mathématiques": 14, "portugais": 15}},
            {"nom": "Carla", "remarques": {"Mathématiques": 12, "portugais": 14}}
        ],
        "professeur": "M. Silva"
    },
    "10B": {
        "étudiants": [
            {"nom": "David", "remarques": {"Mathématiques": 10, "portugais": 12}},
            {"nom": "Veille", "remarques": {"Mathématiques": 9, "portugais": 11}},
            {"nom": "Fabio", "remarques": {"Mathématiques": 15, "portugais": 14}}
        ],
        "professeur": "Mme Costa"
    }
}

# 1. Afficher toutes les classes et tous les étudiants
for classe, infos in cours_2.items():
    print(f"Classe {classe} :")
    for etudiant in infos["étudiants"]:
        print(f"  Élève : {etudiant['nome']}, Notes : {etudiant['notas']}")
    print()

# 2. Afficher les notes d'un étudiant spécifique
nom_recherche = input("Nom de l'étudiant à rechercher : ")
trouve = False
for classe, infos in cours_2.items():
    for etudiant in infos["étudiants"]:
        if etudiant["nom"].lower() == nom_recherche.lower():
            print(f"L'élève {nom_recherche} est en classe {classe} avec les notes : {etudiant['notas']}")
            trouve = True
            break
    if trouve:
        break
if not trouve:
    print("Étudiant introuvable.")

# 3. Compter les élèves avec une moyenne ≥ 10 dans une classe choisie
classe_choisie = input("Choisissez une classe (par exemple, 10A) : ")
if classe_choisie in cours_2:
    decompte_approuve = 0
    for etudiant in cours_2[classe_choisie]["étudiants"]:
        ajoute_des_notes = sum(etudiant["remarques"].values())
        nombre_de_sujets = len(etudiant["remarques"])
        moyenne = ajoute_des_notes / nombre_de_sujets
        if moyenne >= 10:
            decompte_approuve += 1
    print(f"Dans la classe {classe_choisie}, {decompte_approuve} les élèves ont une moyenne ≥ 10.")
else:
    print("Classe introuvable.")
```

---

## 6. Changelog

> Journal des modifications importantes apportées à ce fichier.

- **2025-11-17 · v1.2**
 - Ajout de solutions à tous les exercices.
- **2025-11-17 · v1.1**
 - Table des matières mise à jour.
- **2025-11-17 · v1.0**
 - Création initiale du document.
 - Sections : listes (création, accès, méthodes, fonctions, modèles types, compréhensions), dictionnaires (clés/valeurs, méthodes, itération), structures imbriquées (liste de listes, dictionnaire de listes, dictionnaire de dictionnaires, liste de dictionnaires) et exemples appliqués (températures, classes).
 - Ajout de 12 exercices progressifs sur les listes, dictionnaires et structures imbriquées.

```

```
