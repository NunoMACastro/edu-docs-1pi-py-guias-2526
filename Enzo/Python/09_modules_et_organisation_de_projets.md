# Python (10e année) - 09 · Modules et organisation de projet

> **Objectif de ce fichier** 
> Apprenez à organiser le code dans différents fichiers, à réutiliser les fonctions avec `import` et à créer des projets simples, plus propres et plus faciles à utiliser et à entretenir.

---

## 1) Qu'est-ce qu'un module et pourquoi l'utiliser ?

En Python, **un module est un fichier `.py`** avec du code. Ce code peut avoir :

- des fonctions ;
- des variables;
- des constantes;
- de petites listes/dictionnaires utiles;
- même du code de test.

L'idée est de **séparer les responsabilités**. Au lieu de tout avoir dans un seul fichier :

- un fichier peut gérer les **calculs**;
- un autre peut gérer la **lecture/écriture de fichiers**;
- un autre peut avoir le **programme principal** (menu, `input`, `print`).

Avantages :

- le code est **plus organisé**;
- il est plus facile de **réutiliser des fonctions**;
- il est plus simple de **corriger les erreurs**;
- vous pouvez **tester** des pièces isolées.

---

## 2) Comment créer un module

### Simple exemple

Créez un fichier appelé `math_utils.py` :

```python
# math_utils.py

def somme(a, b):
    return a + b

def moyenne(valeurs):
    if len(valeurs) == 0:
        return 0
    return sum(valeurs) / len(valeurs)
```

Maintenant, dans un autre fichier (par exemple `main.py`), vous pouvez utiliser ces fonctions :

```python
# main.py
import utilitaires_mathematiques

print(utilitaires_mathematiques.soma(3, 5))
print(utilitaires_mathematiques.media([10, 12, 14]))
```

Remarque :

- `import math_utils` lit le fichier `math_utils.py`;
- pour utiliser les fonctions, vous écrivez `math_utils.nome_da_funcao`.

---

## 3) Différentes manières de import

### 3.1 `import modulo`

C'est le moyen le plus sûr et le plus clair :

```python
import utilitaires_mathematiques

total = utilitaires_mathematiques.soma(10, 20)
```

Avantage : vous savez toujours **d'où** vient chaque fonction.

---

### 3.2 `from modulo import funcao`

Peu importe ce que vous voulez :

```python
from utilitaires_mathematiques import somme

print(somme(10, 20))
```

Avantage : code plus court.  
Inconvénient : S'il existe de nombreuses fonctions portant le même nom, cela peut prêter à confusion.

---

### 3.3 `from modulo import *` (à éviter)

```python
from utilitaires_mathematiques import *
```

Cela place **toutes** les fonctions dans votre fichier. C'est rapide, mais dangereux :

- cela peut cacher des noms identiques ;
- ce qui a été importé est moins clair.

Règle générale : **éviter** `import *` dans les projets réels.

---

### 3.4 `import modulo as apelido`

```python
import utilitaires_mathematiques as mu

print(mu.soma(5, 7))
```

Utile pour raccourcir les noms longs.  
Exemple réel : `import random as rd`.

---

### 3.5 Quand utiliser chaque formulaire ?

| Formulaire d'importation | Quand utiliser |
| ---------------------- | ------------------------------------------------- |
| `import modulo` | Projets plus importants, pour plus de clarté.                   |
| `from modulo import f` | Lorsque vous utilisez peu de fonctions et souhaitez un code court. |
| `import modulo as a` | Modules avec des noms longs ou fréquemment utilisés.  |
| `from modulo import *` | À éviter, sauf pour des tests rapides.     |

---

## 4) Que se passe-t-il lorsqu'un module est importé ?

Lorsque vous utilisez `import`, Python **exécute le fichier une fois**, de haut en bas.  
Donc, si le module a `print` ou du code libre, cela s'exécutera en import.

Exemple :

```python
# exemple_module.py
print("Courir peu importe...")

def message_2():
    print("Bonjour!")
```

Si vous le faites :

```python
import exemple_de_module
```

Il apparaîtra à l'écran :

```
A correr no import...
```

**Conclusion :** ne laisse que les fonctions/constantes dans le module.  
Si vous avez besoin de tests, utilisez `if __name__ == "__main__":`.

---

## 5) `if __name__ == "__main__":`

Chaque fichier Python a une variable spéciale appelée `__name__`.

- Lorsque le fichier est exécuté directement, `__name__` est `"__main__"`.
- Lors de l'import du fichier, `__name__` porte le nom du module.

Cela permet de placer des **tests simples** à la fin du module, sans qu'ils s'exécutent dans `import`.

Exemple :

```python
# math_utils.py

def somme(a, b):
    return a + b

if __name__ == "__principal__":
    # Tests rapides
    print(somme(2, 3))
```

Lorsque vous importez `math_utils`, le test **ne s'exécute pas**.  
Lorsque vous exécutez `python math_utils.py`, le test **s'exécute**.

---

## 6) Créer des modules pour un projet

### Exemple de projet simple

```
projeto_turma/
├── main.py
├── alunos.py
└── ficheiros.py
```

#### `alunos.py`

```python
def calculer_la_moyenne(remarques):
    if len(remarques) == 0:
        return 0
    return sum(remarques) / len(remarques)

def a_des_points_negatifs(remarques):
    for avis in remarques:
        if avis < 10:
            return True
    return False
```

#### `ficheiros.py`

```python
import json

def sauver_les_etudiants(etudiants, nom_de_fichier):
    with open(nom_de_fichier, "w", codage="utf-8") as f:
        json.dump(etudiants, f, assurer_ascii=False, retrait=4)

def lire_les_etudiants(nom_de_fichier):
    with open(nom_de_fichier, "r", codage="utf-8") as f:
        return json.load(f)
```

#### `main.py`

```python
from etudiants import calculer_la_moyenne, a_des_points_negatifs
from fichiers import sauver_les_etudiants, lire_les_etudiants

def afficher_le_rapport(etudiants):
    for etudiant in etudiants:
        remarques = etudiant["remarques"]
        moyenne = calculer_la_moyenne(remarques)
        negatif = a_des_points_negatifs(remarques)
        etat = "D'ACCORD" if not negatif else "Avec des négatifs"
        print(f"{etudiant['nome']} - média : {moyenne:.1f} - {etat}")

etudiants = [
    {"nom": "Nain", "remarques": [12, 15, 10]},
    {"nom": "Bruno", "remarques": [9, 8, 10]},
]

afficher_le_rapport(etudiants)
sauver_les_etudiants(etudiants, "étudiants.json")
```

Notes pédagogiques :

- `main.py` n'a que **saisie/impression** et flux principal.
- `alunos.py` a **logique** (fonctions de calcul).
- `ficheiros.py` a **I/O**.

---

### 6.1) Organisation des dossiers

Pour les projets plus importants, vous pouvez organiser les modules dans des dossiers :

```projeto_grande/
├── main.py
├── utils/
│   ├── __init__.py
│   ├── alunos.py
│   └── ficheiros.py
└── data/
    └── alunos.json
```

Ensuite, vous devez :

```python
from utilitaires.alunos import calculer_la_moyenne
```

Il faut toujours être cohérent dans l'organisation et cohérent avec les noms.

---

## 7) Bonnes pratiques lors de la création de modules

- choisir des noms clairs et simples (`alunos.py`, `ficheiros.py`, `utils.py`);
- éviter les majuscules et espaces;
- n'écrivez pas de code lâche qui s'exécute automatiquement;
- placez des tests simples dans `if __name__ == "__main__":`;
- séparez la **logique** des **E/S**.

---

## 8) Bibliothèques de langage (modules prêts à l'emploi)

Python est livré avec de nombreuses bibliothèques. Quelques exemples utiles :

- `random` → nombres aléatoires;
- `math` → fonctions mathématiques;
- `datetime` → dates et heures;
- `os` et `os.path` → chemins et dossiers.

Exemple rapide avec `random` :

```python
import random

nombre = random.randint(1, 10)
print(nombre)
```

---

## 10) Utiliser des exceptions avec des modules

Nous pouvons et devons intégrer des exceptions à tous les points d'arrêt du code, même en utilisant des modules.

Exemple

```python
# Fichier avec des fonctions appelées utils.py

def lire_le_fichier(nom_de_fichier):
    try:
        with open(nom_de_fichier, 'r', codage='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_de_fichier} est introuvable.")
        return None
    except IOError:
        print(f"Erreur : Impossible de lire le fichier {nom_de_fichier}.")
        return None

# Fonction qui utilise un `raise` pour déclencher une exception mais l'essai sera effectué dans main
def diviser(a, b):
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b
```

```python
# Fichier principal main.py
import utilitaires
def principal():
    contenu = utilitaires.ler_ficheiro('données.txt')
    if contenu is not None:
        print("Contenu du fichier :")
        print(contenu)

    try:
        resultat = utilitaires.dividir(10, 0)
        print(f"Résultat de la division : {resultat}")
    except ValueError as e:
        print(f"Erreur lors de la division : {e}")
principal()
```

## 11) Exercices

### Exercice 1 - Premier module

1. Crée un fichier `mensagens.py` avec deux fonctions :
 - `ola(nome)` qui renvoie `"Olá, <nome>!"`;
 - `adeus(nome)` qui renvoie `"Até logo, <nome>!"`.
2. Crée un fichier `main.py` qui importe le module et utilise les deux fonctions.

---

### Exercice 2 - Module Opérations

Crée un fichier `operacoes.py` avec :

- `soma(a, b)`
- `subtrai(a, b)`
- `multiplica(a, b)`
- `divide(a, b)` (si `b == 0`, renvoie `None`)

Puis crée `main.py` pour tester chaque fonction.

> Résolution avec exception pour la division par zéro :

```python
# opérations.py
def somme(a, b):
    return a + b
def soustraire_2(a, b):
    return a - b
def multiplier_2(a, b):
    return a * b
def diviser_2(a, b):
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b
```

```python
# main.py
from operations import somme, soustraire_2, multiplier_2, diviser_2
def principal():
    print("Somme:", somme(5, 3))
    print("Soustraction:", soustraire_2(5, 3))
    print("Multiplication:", multiplier_2(5, 3))
    try:
        print("Division:", diviser_2(5, 0))
    except ValueError as e:
        print("Erreur de division :", e)
principal()
```

---

### Exercice 3 - Logique séparée et E/S

1. Crée un module `texto.py` avec une fonction `conta_vogais(texto)`.
2. Dans `main.py`, il demande à l'utilisateur une phrase et indique le nombre de voyelles.

> Résolution :

```python
# texte.py
def compte_les_voyelles(texte):
    voyelles = "aeiouAEIOU"
    comptoir = 0
    for carboniser in texte:
        if carboniser in voyelles:
            comptoir += 1
    return comptoir
```

```python
# main.py
import texte

phrase = input("Écrivez une phrase : ")
num_voyelles = texte.conta_vogais(phrase)
print(f"La phrase contient des voyelles {num_voyelles} .")
```

---

### Exercice 4 - Projet avec deux modules

Créez un petit projet :

- `alunos.py` avec des fonctions pour calculer la moyenne et compter les négatifs ;
- `main.py` avec une liste des étudiants et une impression des résultats report.

> Résolution avec gestion des erreurs sans utiliser de try à chaque itération, c'est-à-dire que le try est dans main :

> Exemple de dictionnaire :

```python

classe = {
    "Diogo": [12, 11, 9, 20],
    "David": [10, "w", 2, 15],
    "les Neves": [16, 15, 17, 18],
    "Kayque": [10, 10, 10, 10]
}
```

---

### Exercice 5 - Module de fichier JSON

1. Crée `dados.py` avec les fonctions `guardar(alunos, ficheiro)` et `ler(ficheiro)`.
2. Dans `main.py`, enregistrez une liste d'élèves puis relisez-la.

---

### Exercice 6 - Importer avec `as`

1. Crée un module `numeros.py` avec la fonction `dobros(lista)` qui renvoie une nouvelle liste.
2. Cela compte avec un surnom : `import numeros as n`.
3. Utilise `n.dobros(...)`.

> Résolution avec gestion des erreurs ignorant les valeurs invalides et traitant les caractères afin de ne pas être dupliqués :

```python
# nombres.py
def doubles_erreurs(liste):
    resultat = []
    for dans_un in liste:
        try:
            if isinstance(dans_un, str):
                raise TypeError("Mec, il y a une chaîne... Ignore")
            resultat.append(dans_un*2)
        except TypeError as e:
            print("Mec, je veux juste des chiffres.")
            print(str(e))
            continue
    return resultat
```

```python
# main.py
import nombres as n
valeurs = [1, 2, 'le', 4.5, None, 6]
print(n.dobros(valeurs))
```

> Résolution avec gestion globale des erreurs dans main :

```python
# nombres.py
def double(liste):
    return [dans_un * 2 for dans_un in liste]
```

```python
# main.py
import nombres as n

valeurs = [1, 2, 'le', 4.5, None, 6]
resultat = []
for valeur in valeurs:
    try:
        resultat.append(n.dobros([valeur])[0])
    except TypeError:
        continue  # Ignorer les valeurs invalides
print(resultat)
```

> Résolution avec filtrage préalable :

```python
# nombres.py
def double(liste):
    resultat = []
    for dans_un in liste:
        if isinstance(dans_un, (int, float)):
            resultat.append(dans_un * 2)
    return resultat
```

```python
# main.py
import nombres as n
valeurs = [1, 2, 'le', 4.5, None, 6]
print(n.dobros(valeurs))
```

---

### Exercice 7 - `__main__`

Dans un module appelé `teste_modulo.py`:

- crée une fonction `quadrado(n)`;
- à la fin, ajoute un bloc `if __name__ == "__main__":` avec tests.

Après :

- exécute `python teste_modulo.py` et confirme que les tests sont exécutés;
- crée `main.py` qui importe `teste_modulo` et utilise `quadrado` sans exécuter les tests.

---

### Exercice 8 - Module avec constantes

1. Crée `config.py` avec :
 - `ESCOLA = "EPM"`
 - `ANO = 2025`
2. Dans `main.py`, imprimez une phrase en utilisant ces constantes.

> Résolution :

```python
# config.py
ECOLE = "GPE"
ANNEE = 2025
```

```python
# main.py
from configuration import ECOLE, ANNEE
print(f"Bienvenue à {ECOLE} l'année de {ANNEE} !")
```

---

### Exercice 9 - Module avec listes/dictionnaires

Créez `dados_alunos.py` avec une liste d'élèves et de notes.
Dans `main.py`, importez cette liste et calculez la moyenne générale.

> Résolution :

```python
# data_students.py
etudiants = [
    {
        "nom" : "David",
        "remarques" : {
            "LP" : 10,
            "Mathématiques" : 10,
            "Supporter les cacahuètes" : 20
        }
    },
    {
        "nom" : "Kaykay",
        "remarques" : {
            "LP" : 5,
            "Mathématiques" : 5,
            "Arrêtez l'infiltration" : 20
        }
    }
]
```

```python
# main.py
from donnees_sur_les_etudiants import etudiants

notes_totales = 0
dans_une_note = 0

for etudiant in etudiants:
    for avis in etudiant["remarques"].values():
        notes_totales += avis
        dans_une_note += 1

moyenne_generale = notes_totales / dans_une_note if dans_une_note > 0 else 0
print(f"Moyenne générale de la classe : {moyenne_generale:.2f}")
```

---

### Exercice 10 - Module Utilitaires

1. Crée `utilitarios.py` avec les fonctions :
 - `eh_par(n)` qui renvoie `True` si `n` est pair ;
 - `fatorial(n)` qui renvoie la factorielle de `n`.
2. Dans `main.py`, testez ces fonctions.

> Résolution :

```python
# utilitaires.py
def he_paire(n):
    return n % 2 == 0

def factorielle(n):
    if n < 0:
        raise ValueError("Factorielle non définie pour les nombres négatifs.")
    if n == 0 or n == 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat
```

Principal avec test d'erreur

```python
# main.py
from utilitaires_2 import he_paire, factorielle

try:
    nombre = int(input("Écrivez un nombre : "))
    if he_paire(nombre):
        print(f"{nombre} est pair.")
    else:
        print(f"{nombre} est étrange.")
    print(f"Factorielle de {nombre} : {factorielle(nombre)}")
except ValueError as e:
    print(f"Erreur : {e}")

```

---

### Exercice 11 - Module de manipulation de chaînes

1. Crée `string_utils.py` avec les fonctions :
 - `inverter(texto)` qui renvoie le texte inversé ;
 - `contar_palavras(texto)` qui renvoie le nombre de mots.
2. Dans `main.py`, il demande à l'utilisateur une phrase et affiche le texte inversé et le nombre de mots.

> Résolution :

```python
# string_utils.py
def inverse_2(texte):
    return texte[::-1]

def compter_les_mots(texte):
    mots = texte.split()
    return len(mots)
```

```python
# main.py
from utilitaires_de_chaine import inverse_2, compter_les_mots

phrase = input("Écrivez une phrase : ")
print("Phrase inversée :", inverse_2(phrase))
print("Nombre de mots :", compter_les_mots(phrase))
```

---

### Exercice 12 - Mini projet organisé

Créez un projet avec 3 fichiers :

- `menu.py` (affiche les options et valide le choix);
- `logica.py` (fonctions qui gèrent tâches);
- `main.py` (assemble tout et exécute).

Objectif : un mini gestionnaire de tâches simple (ajouter, lister, supprimer).

> Résolution à l'aide de fichiers json pour enregistrer les tâches et gestion des erreurs :
> Sauvons les tâches à l'aide d'une liste de dictionnaires.

```python
# logique.py
import json

def charger_des_taches(nom_de_fichier):
    try:
        with open(nom_de_fichier, 'r', codage='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def enregistrer_des_taches(taches, nom_de_fichier):
    with open(nom_de_fichier, 'w', codage='utf-8') as f:
        json.dump(taches, f, assurer_ascii=False, retrait=4)

def ajouter_une_tache(taches, description):
    taches.append({"description": description, "complété": False})

def lister_les_taches(taches):
    for tache in taches:
        statut = "Complété" if tache["complété"] else "En attente"
        print(f"- {tache['descricao']} [{statut}]")

# supprimer en utilisant pop
def supprimer_une_tache(taches, indice):
    if 0 <= indice < len(taches):
        taches.pop(indice)
```

```python
# menu.py
def afficher_le_menu():
    print("Gestionnaire de tâches")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Supprimer la tâche")
    print("4. Déconnectez-vous")
    choix = input("Choisissez une option (1-4) : ")
    return choix
```

```python
# main.py
from logique import charger_des_taches, enregistrer_des_taches, ajouter_une_tache, lister_les_taches, supprimer_une_tache
from menu import afficher_le_menu

def principal():
    nom_de_fichier = 'tâches.json'
    taches = charger_des_taches(nom_de_fichier)

    while True:
        choix = afficher_le_menu()
        if choix == '1':
            description = input("Description de la tâche : ")
            ajouter_une_tache(taches, description)
            enregistrer_des_taches(taches, nom_de_fichier)
        elif choix == '2':
            lister_les_taches(taches)
        elif choix == '3':
            indice = int(input("Index de la tâche à supprimer : "))
            supprimer_une_tache(taches, indice)
            enregistrer_des_taches(taches, nom_de_fichier)
        elif choix == '4':
            print("Sortie...")
            break
        else:
            print("Option invalide. Essayer à nouveau.")

if __name__ == "__principal__":
    principal()
```

---

## 10) Changelog

- `2025-02-XX` · Création initiale du fichier avec introduction aux modules, importations et organisation du projet.

```

```

```

```
