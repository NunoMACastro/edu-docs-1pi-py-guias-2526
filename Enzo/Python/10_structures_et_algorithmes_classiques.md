# Python (10e année) - 10 · Structures et algorithmes classiques

> **Objectif de ce fichier** 
> Introduire la recherche linéaire, l'ordre de base (bulle et sélection) et une notion simple d'efficacité.

---

## 1) Que sont les algorithmes et pourquoi étudier ?

Un **algorithme** est un ensemble d'étapes claires pour résoudre un problème.  
Exemples du quotidien :

- recette d'un gâteau (étapes dans le bon ordre);
- instructions pour assembler un meuble;
- liste de règles pour décider de quelque chose.

En programmation, un algorithme indique **comment** trouver une réponse, pas seulement **quoi** il s'agit réponse.

---

## 2) Recherche linéaire

### 2.1 Idée principale

La **recherche linéaire** parcourt une liste du début à la fin, élément par élément, jusqu'à ce qu'elle trouve la valeur souhaitée.

- si elle est trouvée, elle se termine;
- s'il n'est pas trouvé, il se termine.

### 2.2 Exemple simple

```python
def recherche_lineaire(valeurs, cible):
    for article in valeurs:
        if article == cible:
            return True
    return False

chiffres = [4, 7, 1, 9, 3]
print(recherche_lineaire(chiffres, 9))   # Vrai
print(recherche_lineaire(chiffres, 10))  # FAUX
```

### 2.3 Exemple avec index

```python
def recherche_lineaire_par_index(valeurs, cible):
    for i in range(len(valeurs)):
        if valeurs[i] == cible:
            return i
    return -1

noms = ["Nain", "Bruno", "Carla"]
print(recherche_lineaire_par_index(noms, "Carla"))  # 2
print(recherche_lineaire_par_index(noms, "Duarte")) # -1
```

---

## 3) Ordre de base

Order une liste signifie placer les éléments dans un **ordre** (croissant ou décroissant).

Nous verrons ici deux ordres classiques :

- **Bulle Tri**
- **Tri par sélection**

Ces tris ne sont pas les plus rapides, mais ils sont **simples** et bons pour l'apprentissage.

---

## 4) Tri à bulles (tri par bulle)

### 4.1 Principal idée

Nous parcourons la liste plusieurs fois et, à chaque passage, **échangeons** les éléments adjacents s'ils sont dans le désordre.

A chaque passage, le plus grand élément "se déplace" jusqu'à la fin.

### 4.2 Exemple d'étape pas à pas (petite liste)

Initial liste : `[5, 2, 4]`

- Compare 5 et 2 -> échange : `[2, 5, 4]`
- Compare 5 et 4 -> échange : `[2, 4, 5]`@

Maintenant, le plus gros (5) est déjà à la fin.  
Nous effectuons une nouvelle passe pour confirmer la commande.

### 4.3 Mise en œuvre

```python
def tri_a_bulles(valeurs):
    n = len(valeurs)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if valeurs[j] > valeurs[j + 1]:
                valeurs[j], valeurs[j + 1] = valeurs[j + 1], valeurs[j]

chiffres = [5, 1, 4, 2, 8]
tri_a_bulles(chiffres)
print(chiffres)  # [1, 2, 4, 5, 8]
```

### 4.4 Version avec détection de changement

S'il n'y a aucun changement dans un passage, la liste est déjà triée et on peut s'arrêter.

```python
def tri_a_bulles_optimise(valeurs):
    n = len(valeurs)
    for i in range(n):
        il_y_a_eu_un_echange = False
        for j in range(0, n - 1 - i):
            if valeurs[j] > valeurs[j + 1]:
                valeurs[j], valeurs[j + 1] = valeurs[j + 1], valeurs[j]
                il_y_a_eu_un_echange = True
        if not il_y_a_eu_un_echange:
            break
```

---

## 5) Tri par sélection (tri par sélection)

### 5.1 Idée principale

A chaque étape, nous trouvons le **plus petit** élément de la pièce non triée et le plaçons en position droite.

### 5.2 Exemple pas à pas (petite liste)

Liste initiale : `[4, 2, 7, 1]`

- la plus petite = 1 -> échange avec le premier élément 
 la liste devient `[1, 2, 7, 4]`
- maintenant nous regardons le reste `[2, 7, 4]` 
 mineur = 2 -> est déjà à droite position
- dernière étape : saisir `[7, 4]`, mineur = 4 -> échange 
 liste finale `[1, 2, 4, 7]`

### 5.3 Mise en œuvre

```python
def tri_par_selection(valeurs):
    n = len(valeurs)
    for i in range(n):
        indice_minimum = i
        for j in range(i + 1, n):
            if valeurs[j] < valeurs[indice_minimum]:
                indice_minimum = j
        valeurs[i], valeurs[indice_minimum] = valeurs[indice_minimum], valeurs[i]

chiffres = [4, 2, 7, 1]
tri_par_selection(chiffres)
print(chiffres)  # [1, 2, 4, 7]
```

---

## 6) Comparer la recherche linéaire et le tri

### Recherche linéaire

- parcourt la liste une fois;
- si la cible est à la fin, voit tous les éléments;
- si elle est au début, se termine bientôt.

### Le tri

- fait beaucoup de comparaisons et d'échanges;
- même avec des petites listes, c'est déjà un peu plus fastidieux.

---

## 7) Notion simple de efficacité

Quand on a **peu de données**, presque tout fonctionne bien.  
Quand on a **beaucoup de données**, le choix de l'algorithme fait beaucoup de différence.

### Idée simple :

- rechercher 1 élément sur 10 éléments -> rapide
- rechercher 1 élément sur 1 000 000 éléments -> cela peut prendre du temps

Si un algorithme fait 100 000 pas et un autre en fait 10 000, le second est plus efficace.

Nous n'avons pas besoin de formules compliquées maintenant, sachez simplement que :

- **plus d'étapes = plus de temps**;
- commander une liste est généralement plus fastidieux que simplement en chercher une. value.

---

## 8) Quand utiliser chaque chose

- **Recherche linéaire** : lorsque la liste n'est pas ordonnée et est petite ou moyenne.
- **Ordre de base** : bon pour l'apprentissage et pour les petites listes.
- Pour les grandes listes, il existe des algorithmes plus rapides (nous verrons plus tard).

---

## 8.1) Pourquoi apprendre ceci s'il y a `sort()` ?

C'est une question excellente et très courante. La réponse courte est : **pour comprendre ce qui se passe derrière `sort()` et acquérir des outils de raisonnement**. Voici l'explication en parties :

### 1) `sort()` existe, mais ce n'est pas magique

`sort()` trie car il **utilise un algorithme de tri interne**. Cet algorithme a été créé, testé et choisi car il est efficace dans la plupart des cas. Si vous ne savez pas ce qu'est un algorithme de tri, vous traiterez `sort()` comme une \"boîte noire\".

Connaître les bases vous permet de :

- comprendre pourquoi le tri coûte du temps;
- comprendre pourquoi les grandes listes prennent plus de temps;
- distinguer quand il est judicieux de trier et quand n°

### 2) Les algorithmes d'apprentissage entraînent le raisonnement

Le tri par bulles et le tri par sélection ne sont pas enseignés car ce sont les meilleurs.  
Ils sont enseignés parce qu'ils sont **simples** et montrent des idées fondamentales :

- comparer les valeurs;
- décider quand échanger;
- répéter les étapes jusqu'à ce qu'elles soient triées;
- mesurer le nombre d'étapes que cela a pris.

Ce raisonnement sera utilisé dans de nombreux problèmes différents, même si vous n'utilisez plus jamais le tri à bulles dans un vrai application.

### 3) Vous ne pouvez pas toujours utiliser `sort()`

Dans certains exercices et projets, l'objectif **est d'apprendre** et pas seulement d'atteindre le résultat.  
Si vous utilisez `sort()` sans vous en rendre compte, vous \"sautez\" un apprentissage.

Il existe également des situations dans lesquelles vous devez :

- trier selon des règles spéciales (par exemple, le plus récent en premier, puis par ordre alphabétique);
- trier des parties spécifiques d'une liste;
- expliquer le processus étape par étape, étape par étape étape.

Sans connaître l'algorithme, il est difficile de s'adapter.

### 4) Le bon algorithme fait la différence

Imaginez deux façons de trier 10 000 nombres :

- on fait environ 1 000 000 comparaisons ;
- un autre n'en fait que 100 000.

Le second est beaucoup plus rapide.  
Savoir qu'il existe différents algorithmes vous aide à comprendre **pourquoi certaines solutions sont lentes**.

### 5) À l'avenir, vous étudierez de meilleurs algorithmes

Plus tard, vous découvrirez des algorithmes comme le **tri par fusion** ou le **tri rapide**.  
Pour comprendre ces algorithmes, vous avez besoin de ces bases :

- comparaison et échange;
- parcourir la liste;
- diviser les problèmes;
- analyser l'efficacité.

### En résumé

- `sort()` est excellent et vous l'utiliserez souvent.
- L'apprentissage des algorithmes classiques vous aide à comprendre **comment** `sort()` fonctionne.
- Cela améliore votre raisonnement et vous prépare à des problèmes plus complexes.

---

## 9) Exercices

### Exercice 1 - Recherche linéaire simple

Créez une fonction `existe(lista, alvo)` qui renvoie `True` si la cible est dans la liste.

---

### Exercice 2 - Rechercher avec index

Créer une fonction `indice(lista, alvo)` qui renvoie l'index cible ou `-1` s'il n'existe pas.

---

### Exercice 3 - Tri à bulles

Crée une fonction `ordenar_bubble(lista)` qui trie la liste par ordre croissant order.

---

### Exercice 4 - Sélection Tri

Crée une fonction `ordenar_selection(lista)` qui trie la liste par ordre croissant.

---

### Exercice 5 - Comparer méthodes

Étant donné la liste :

```
[9, 1, 7, 3, 5]
```

1. Trier avec **tri à bulles**.
2. Trier avec **tri par sélection**.
3. Confirmez que le résultat est le même.

---

### Exercice 6 - Recherche avant et après le tri

1. Recherchez le chiffre 7 dans une liste non ordonnée avec recherche linéaire.
2. Triez la liste.
3. Recherchez à nouveau et comparez le nombre d'étapes (vous pouvez utiliser un compteur).

---

### Exercice 7 - Tri décroissant

Adaptez le **tri à bulles** pour trier en conséquence par ordre décroissant.

---

### Exercice 8 - Trier les noms

Créez une liste de noms et triez-la à l'aide du **tri par sélection**.

---

### Exercice 9 - Recherche par nom (sauter les lettres majuscules)

1. Crée une liste avec des noms.
2. Demande un nom à l'utilisateur.
3. Recherchez dans la liste en ignorant les majuscules/minuscules.

Conseil : utilisez `nome.lower()`.

---

### Exercice 10 - Défi simple

Créez un programme qui :

- demande 5 nombres au l'utilisateur et l'enregistre dans une liste ;
- trie la liste avec **tri à bulles**;
- affiche la liste triée.

---

## 10) Journal des modifications

- `2025-02-XX` · Création de fichiers initiale avec recherche linéaire, tri à bulles/sélection et efficacité de base.
