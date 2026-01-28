# Python (10e année) - 08 · Exceptions et gestion des erreurs

> **Objectif de ce fichier** 
> Comprendre pourquoi des erreurs se produisent au moment de l'exécution, apprendre à lire les messages d'erreur et utiliser `try`/`except` pour rendre les programmes plus robustes et plus conviviaux.

---

## Index

- [0. Comment utiliser ce fichier](#0-comment-utiliser-ce-fichier)
- [1. Types d'erreurs en Python · \[ESSENTIAL\]](#1-tipos-de-erros-em-python--essencial)
- [2. Comment lire les messages d'erreur · \[ESSENTIAL\]](#2-como-ler-mensagens-de-erro--essencial)
- [3. Introduction à `try`/`except` · \[ESSENTIEL\]](#3-introdução-a-tryexcept--essencial)
- [4. Capturer les exceptions spécifiques · \[ESSENTIAL\]](#4-capturar-exceções-específicas--essencial)
- [5. Clauses multiples `except` et exception générique · \[EXTRA\]](#5-várias-cláusulas-except-e-exceção-genérica--extra)
- [6. `else` et `finally` · \[EXTRA / curiosité\]](#6-else-e-finally--extra--curiosidade)
- [7. Génère des erreurs avec `raise` (et `assert`) · \[EXTRA\]](#7-lançar-erros-com-raise-e-assert--extra)
- [8. Bonnes pratiques de gestion des erreurs](#8-bonnes-pratiques-de-gestion-des-erreurs)
- [9. Exercices - Exceptions et gestion des erreurs](#9-exercices-exceptions-et-gestion-des-erreurs)
- [10. Changelog](#10-changelog)

---

## 0. Comment utiliser ce fichier

1. Assurez-vous d'être au moins à l'aise avec :
 - les types de base (`int`, `float`, `str`, `bool`) et `input`/`print` (`01_introduction_variables_types_strings_io.md`);
 - `if`, `while`, `for`, `range` (`02_operateurs_et_controle_de_flux_if_boucles.md`);
 - listes et dictionnaires (`03_listes_dictionnaires_structures_imbriquees.md`);
 - fonctions de base (`04_fonctions_du_basique_au_avance.md`);
 - fichiers texte/JSON/CSV (`07_fichiers_texte_json_csv.md`).
2. Lisez d'abord les sections marquées **[ESSENTIEL]** :
 - 1, 2, 3 et 4.
3. Ensuite seulement, explorez les sections marquées **[EXTRA]** :
 - 5, 6 et 7.
4. Utilise l'interpréteur ou les fichiers `.py` pour :
 - **provoquer des erreurs** volontairement,
 - visualiser les messages d'erreur et les analyser,
 - réécrire le code avec `try`/`except`.
5. À la fin, résolvez les **exercices**, en commençant par les plus basiques.

---

## 1. Types d'erreurs en Python · [ESSENTIEL]

Lorsque quelque chose ne va pas, Python peut afficher plusieurs types d'erreurs (exceptions).

### 1.1. Erreurs de syntaxe (`SyntaxError`)

Il s'agit d'erreurs dans lesquelles Python **ne peut même pas démarrer** l'exécution du programme.

Exemple :

```python
if x > 0
    print("positif")
```

Le `:` est absent de `if`.  
Si vous essayez d'exécuter, quelque chose comme ceci apparaît :

```text
  File "exemplo.py", line 1
    if x > 0
            ^
SyntaxError: invalid syntax
```

Tant que vous n'aurez pas corrigé ces erreurs, le programme ne démarrera pas.

### 1.2. Erreurs d'exécution (exceptions)

Ce sont des erreurs qui se produisent **après** le démarrage du programme.

Quelques exemples classiques :

- `ZeroDivisionError` → division par zéro :

```python
    x = 10 / 0
```

- `NameError` → utiliser une variable qui n'existe pas :

```python
    print(resultat)  # le résultat n'a jamais été défini
```

- `TypeError` → types incompatibles :

```python
    total = "10" + 5   # chaîne + entier → erreur
```

- `ValueError` → valeur invalide dans la conversion :

```python
    nombre = int("abc")    # "abc" n'est pas un nombre
```

- `IndexError` → index hors des limites d'une liste :

```python
    liste = [1, 2, 3]
    print(liste[5])        # il n'y a pas d'index 5
```

- `KeyError` → clé inexistante dans un dictionnaire :

```python
    etudiant = {"nom": "Nain", "avis": 15}
    print(etudiant["âge"])  # Il n'y a pas "d'âge"
```

Apprenons à **lire** ces messages puis à les **gérer**.

---

## 2. Comment lire les messages d'erreur · [ESSENTIEL]

Lorsqu'une erreur se produit au moment de l'exécution, Python affiche une « trace » (traceback).

Exemple :

```python
nombre = int(input("Entier: "))
print(10 / nombre)
```

Si l'utilisateur tape `0`, quelque chose comme ceci apparaît :

```text
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    print(10 / numero)
ZeroDivisionError: division by zero
```

Choses importantes à réparer :

1. **Fichier et ligne** :
 - `File "exemplo.py", line 2` → où l'erreur s'est produite.
2. **Code de ligne** :
 - `print(10 / numero)` → ce qui était en cours d'exécution.
3. **Type d'erreur** :
 - `ZeroDivisionError` → catégorie de problème.
4. **Message** :
 - `division by zero` → description en anglais.

Lorsque vous déboguez (résoudre des problèmes) :

- lisez toujours la **dernière ligne** du traceback (type d'erreur + message);
- voyez **la ligne de code indiquée**;
- essayez de comprendre **dans quelles valeurs** devaient être utilisées cette ligne.

---

## 3. Introduction à `try`/`except` · [ESSENTIEL]

Ce qui se passe normalement :

- s'il y a une erreur, le programme **s'arrête** immédiatement;
- l'utilisateur voit un message technique (gros tiret en anglais);
- dans les programmes réels, cela n'est pas acceptable.

Avec `try`/`except`, nous pouvons **intercepter** certaines erreurs et réagir de manière contrôlée.

### 3.1. Syntaxe de base

```python
try:
    # code qui peut donner une erreur
    nombre = int(input("Entier: "))
    resultat = 10 / nombre
    print("Résultat:", resultat)
except:
    # que faire si vous avez une erreur
    print("Oups, quelque chose s'est mal passé.")
```

Opération :

- Python entre dans le bloc `try` et exécute les lignes normalement ;
- s'il n'y a pas d'erreur → ignore `except`;
- s'il y a une erreur dans une ligne de `try`:
 - s'arrête là,
 - passe à l'intérieur le bloc `except`,
 - exécute le code `except` au lieu d'arrêter le programme.

**Attention :** 
Dans cet exemple, `except` est **générique** (détecte toute erreur).  
Nous verrons plus loin pourquoi cela doit être utilisé avec précaution.

### 3.2. Exemple : conversion sécurisée avec `int` · [ESSENTIEL]

Nous voulons demander un nombre entier, mais l'utilisateur peut écrire n'importe quoi.

```python
try:
    age = int(input("Âge (en années) : "))
    print("Dans 10 ans tu auras", age + 10, "années.")
except ValueError:
    print("Veuillez saisir un entier valide.")
```

Ici, nous capturons déjà **un type spécifique d'erreur** (`ValueError`).  
C'est mieux que d'attraper "toutes les erreurs" sans savoir laquelle.

---

## 4. Détecter des exceptions spécifiques · [ESSENTIEL]

Il est très important de savoir **quelle erreur nous attendons**.

### 4.1. `ValueError` lors de la conversion `input` · [ESSENTIEL]

Modèle typique : lire le numéro d'utilisateur.

```python
try:
    nombre = int(input("Écrivez un entier : "))
    print("Nombre au carré :", nombre ** 2)
except ValueError:
    print("Cela ne ressemble pas à un nombre entier...")
```

Si l'utilisateur écrit `abc`, nous récupérons `ValueError` et lui montrons un message amical.

### 4.2. `ZeroDivisionError` en divisions · [ESSENTIEL]

Un autre classique : la division par zéro.

```python
try:
    numerateur = float(input("Numérateur: "))
    denominateur = float(input("Dénominateur: "))
    resultat = numerateur / denominateur
    print("Résultat:", resultat)
except ZeroDivisionError:
    print("Il n'est pas possible de diviser par zéro.")
except ValueError:
    print("Veuillez écrire des numéros valides.")
```

> Nous pouvons demander à plusieurs reprises des chiffres à l'utilisateur alors que ce qu'il saisi produit des erreurs :

```python

while True:
    try:
        numerateur = float(input("Numérateur: "))
        denominateur = float(input("Dénominateur: "))
        resultat = numerateur / denominateur
    except ZeroDivisionError:
        print("Il n'est pas possible de diviser par zéro. Essayer à nouveau.")
    except ValueError:
        print("Veuillez écrire des numéros valides. Essayer à nouveau.")
    else:
        # N'arrivez ici que s'il n'y a eu AUCUNE erreur
        print("Résultat:", resultat)
        break  # sortir du cycle si tout s'est bien passé
```

Notez que nous avons déjà **deux `except`** différents :

- un pour la division par zéro,
- un autre pour convertir des chaînes en nombres.

### 4.3. `FileNotFoundError` lors de l'ouverture de fichiers · [ESSENTIEL]

Lien avec le fichier `07_fichiers_texte_json_csv.md`.

```python
nom_de_fichier = input("Nom de fichier: ")

try:
    with open(nom_de_fichier, "r", codage="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Ce fichier est introuvable.")
else:
    # n'arrivez ici que s'il n'y a eu AUCUNE erreur
    print("Contenu du fichier :")
    print(contenu)
```

Ici, nous introduisons également `else` (nous l'expliquerons mieux dans la section 6).

---

## 5. Plusieurs clauses `except` et exception générique · [EXTRA]

### 5.1. Plusieurs `except`

Nous avons déjà vu un exemple avec `ZeroDivisionError` et `ValueError`.  
Nous pouvons l'organiser ainsi :

```python
try:
    nombre = int(input("Entier: "))
    print("10 / nombre =", 10 / nombre)
except ValueError:
    print("Ce n'est pas un entier.")
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro.")
```

Le premier `except` compatible avec l'erreur est celui utilisé.

### 5.2. Détecter plusieurs types d'erreur à la fois

Parfois, nous souhaitons réagir de la même manière à plusieurs types d'erreurs.

```python
try:
    nombre = int(input("Entier: "))
    print("10 / nombre =", 10 / nombre)
except (ValueError, ZeroDivisionError):
    print("Erreur : Écrit un entier non nul.")
```

Remarquez les parenthèses autour des types d'erreurs.

### 5.3. `except Exception` (presque toutes les erreurs) · [attention !]

Nous pouvons utiliser :

```python
try:
    # code
except Exception as e:
    print("Une erreur s'est produite :", e)
```

Problèmes :

- il peut cacher des erreurs de programmation (bugs) qui devraient être corrigées ;
- si vous l'utilisez partout, vous ne saurez pas ce qui s'est passé.

Règle générale pour ceux qui apprennent :

- **préfère détecter les erreurs spécifiques** (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, etc.);
- utiliser `Exception` uniquement dans des cas particuliers et avec beaucoup de précautions.

---

## 6. `else` et `finally` · [EXTRA]

### 6.1. `else` après `try`/`except`

Le bloc `else` est **facultatif** et s'exécute **uniquement s'il n'y a pas d'erreur**.

```python
try:
    nombre = int(input("Entier: "))
except ValueError:
    print("Ce n'est pas un entier.")
else:
    # ne s'exécute que s'il n'y a AUCUNE ValueError
    print("Nombre au carré :", nombre ** 2)
```

Il est utile de séparer :

- la partie qui peut échouer (`try`),
- de la partie qui n'a de sens que si tout s'est bien passé (`else`).

### 6.2. `finally` (toujours exécuté)

Le bloc `finally` est également **facultatif** et s'exécute **toujours** :

- s'il y a une erreur,
- s'il n'y a pas d'erreur.

Exemple plus théorique (les fichiers sont déjà bien traités avec `with`) :

```python
f = open("données.txt", "w", codage="utf-8")

try:
    f.write("Quelques données...\n")
    # plus de code qui peut donner une erreur
finally:
    f.close()   # s'assure que le dossier est fermé
```

Aujourd'hui, nous préférons presque toujours :

```python
with open("données.txt", "w", codage="utf-8") as f:
    f.write("Quelques données...\n")
```

Parce que `with` s'occupe déjà de la partie fermeture du fichier.

> Pourquoi utiliser `finally` et ne pas mettre le code à l'extérieur de `try`/`except`?
> Parce que s'il y a une erreur dans `try`, le code à l'extérieur de `try`/`except` **n'est pas exécuté**.

---

## 7. Générer des erreurs avec `raise` (et `assert`) · [EXTRA]

### 7.1. `raise` pour indiquer des situations interdites

Parfois, nous voulons **nous-mêmes** lancer une erreur, pour indiquer que quelque chose d'inattendu s'est produit.

```python
def diviser(a, b):
    if b == 0:
        raise ValueError("Le dénominateur ne peut pas être nul.")
    return a / b
```

Si quelqu'un appelle `dividir(10, 0)`, un `ValueError` est lancé avec le message indiqué.

Plus tard, cette erreur pourra être gérée avec `try`/`except` ailleurs dans le programme.

Un autre exemple, mais plus utile :

```python
def definit_l_age_de_la_majorite(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    elif age >= 18:
        return True
    else:
        return False
```

Détection d'erreur :

```python
try:
    age = int(input("Âge: "))
    plus_gros = definit_l_age_de_la_majorite(age)
    if plus_gros:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")
except ValueError as e:
    print("Erreur:", e)
```

### 7.2. `assert` pour des vérifications rapides

Cela a déjà été mentionné dans `05_algorithmes_et_modeles_de_programmation.md`, mais voici le résumé :

```python
def moyenne(nombres):
    assert len(nombres) > 0, "La liste ne peut pas être vide"
    return sum(nombres) / len(nombres)
```

- Si la condition est `True`, le programme continue normalement.
- Si c'est `False`, un `AssertionError` est lancé avec le message.

`assert` est utile pour des tests rapides et pour garantir certaines conditions dans fonctions.

---

## 8. Bonnes pratiques lors de la gestion des erreurs

- Essayez de comprendre **pourquoi** l'erreur se produit avant d'utiliser `try`/`except`@.
- N'utilisez pas `except:` ou `except Exception:` partout « juste pour éviter "
- Préfère **capter les exceptions spécifiques** (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, etc.).
- Affiche des messages clairs à l'utilisateur, de préférence en anglais simple.
- N'avalez pas l'erreur sans rien faire :
 - évite `except: pass`.
- Utiliser `try`/`except` pour :
 - valider le `input` de l'utilisateur;
 - gérer les fichiers qui peuvent ne pas exister;
 - gérer les données provenant de l'extérieur du programme (JSON, CSV, etc.).

---

## 9. Normes communes de exceptions

- **Exemple d'utilisation de messages d'erreur** :

```python
    try:
        nombre = int(input("Entier: "))
        print("10 / nombre =", 10 / nombre)
    except Exception as e:
        print("Une erreur s'est produite :", e)
```

- **Lecture entière sécurisée** :

```python
    try:
        nombre = int(input("Entier: "))
    except ValueError:
        print("Ce n'est pas un entier.")
```

- **Division sécurisée** :

```python
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Vous ne pouvez pas diviser par zéro.")
```

- **Lecture de fichiers avec gestion des erreurs** :

```python
    try:
        with open("données.txt", "r", codage="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        print("Fichier introuvable.")
    else:
        print(contenu)
```

- **Conversion sécurisée d'une liste de chaînes en entiers** :

```python
    cordes = ["10", "20", "abc", "30"]
    nombres = []
    for s in cordes:
        try:
            n = int(s)
            nombres.append(n)
        except ValueError:
            print(f"Ignorer la valeur non valide : {s}")
```

---

## 10. Liste des erreurs courantes en Python

- `SyntaxError` → erreur de syntaxe (le programme ne démarre pas).
- `NameError` → variable non définie.
- `TypeError` → fonctionnement avec des types incompatibles.
- `ValueError` → valeur invalide (ex. : convertir une chaîne en nombre).
- `IndexError` → index hors des limites d'une liste.
- `KeyError` → clé inexistante dans un dictionnaire.
- `ZeroDivisionError` → division par zéro.
- `FileNotFoundError` → fichier introuvable.
- `IOError` / `OSError` → erreurs d'entrées/sorties (fichiers, disques, etc.).
- `ImportError` → erreur lors de l'import d'un module.
- `AttributeError` → attribut ou méthode inexistant dans un objet.
- `IndentationError` → erreur d'indentation (incorrecte espaces/tabulations).

---

## 11. Exercices - Exceptions et gestion des erreurs

### Exercice 1 - Lecture sécurisée des entiers · [BASIC]

Écrire un programme qui :

- demande à l'utilisateur pour un nombre entier ;
- utilise `try`/`except` pour :
 - affiche le carré du nombre, **si tout va bien**;
 - affiche un message convivial **si l'utilisateur écrit quelque chose de non valide** (par exemple `abc`).

> Résolution :

```python
try:
    nombre = int(input("Entier: "))
    print("Nombre au carré :", nombre ** 2)
except ValueError:
    print("Ce n'est pas un entier valide.")
```

---

### Exercice 2 - Répéter jusqu'à validité · [BASIC]

Améliore l'exercice précédent :

- utilise un cycle `while True` pour demander un entier;
- si la conversion avec `int` se déroule bien, elle sort du cycle (`break`) et affiche le résultat ;
- s'il donne `ValueError`, il affiche un message et demande à nouveau le numéro.

> Résolution :

```python
while True:
    try:
        nombre = int(input("Entier: "))
        break  # sortir du cycle si tout va bien
    except ValueError:
        print("Ce n'est pas un entier valide. Essayer à nouveau.")

print("Nombre au carré :", nombre ** 2)
```

---

### Exercice 3 - Division sécurisée · [BASIC]

Écrivez un programme qui :

- demande deux nombres (numérateur et dénominateur) ;
- essaie de faire la division ;
- traite séparément :
 - `ValueError` (si l'utilisateur écrit autre chose qu'un nombre),
 - `ZeroDivisionError` (si le dénominateur est zéro).

Affiche des messages différents dans chaque cas.

> Résolution :

```python
try:
    numerateur = float(input("Numérateur: "))
    denominateur = float(input("Dénominateur: "))
    resultat = numerateur / denominateur
    print("Résultat:", resultat)
except ValueError:
    print("Veuillez écrire des numéros valides.")
except ZeroDivisionError:
    print("Il n'est pas possible de diviser par zéro.")
```

---

### Exercice 4 - Lire un fichier avec un message convivial · [BASIC]

Écrire un programme qui :

- demande à l'utilisateur le nom d'un fichier;
- tente d'ouvrir le fichier en mode lecture et de montrer son content;
- si le fichier **n'existe pas**, récupérez `FileNotFoundError` et affichez un message clair (pas de trace).

Conseil : connectez-vous avec ce que vous avez appris dans `07_fichiers_texte_json_csv.md`.

> Résolution :

```python
nom_de_fichier = input("Nom de fichier: ")
try:
    with open(nom_de_fichier, "r", codage="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Ce fichier est introuvable.")
else:
    print("Contenu du fichier :")
    print(contenu)
```

> On peut aussi vérifier si l'extension du fichier est `json` et si ce n'est pas le cas, lancer un `ValueError` avec `raise`.
> Utilisons split pour diviser le nom du fichier par le point et vérifier la dernière partie.:

```python
nom_de_fichier = input("Nom de fichier: ")
try:
    if nom_de_fichier.split('.')[-1] != 'json': # ici nous utilisons l'index -1 pour obtenir la dernière partie après le point
        raise ValueError("Le fichier doit être un .json")
    with open(nom_de_fichier, "r", codage="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Ce fichier est introuvable.")
except ValueError as ve:
    print("Erreur:", ve)
else:
    print("Contenu du fichier :")
    print(contenu)

```

---

### Exercice 5 - Ajouter des nombres dans une ligne · [INTERMÉDIAIRE]

Écrire un programme qui :

- demande à l'utilisateur une ligne avec plusieurs nombres séparés par des espaces, par exemple :

```text
    10 5 -3 7
    ```

- divise la ligne en parties (`split`);
- essaie de convertir chaque partie en un entier et d'ajouter toutes les valeurs;
- si une partie n'est pas un nombre valide, elle prend `ValueError` et :
 - affiche un message indiquant quelle valeur était invalide;
 - ignore cette valeur et continue avec le restant.

> Résolution :

```python
doubler = input("Écrivez plusieurs nombres séparés par des espaces : ")
parties = doubler.split()
somme = 0

for p in parties:
    try:
        n = int(p)
        somme += n
    except ValueError:
        print(f"Ignorer la valeur non valide : {p}")
print("Somme des nombres valides :", somme)
```

---

### Exercice 6 - Lecture de JSON avec gestion des erreurs · [INTERMÉDIAIRE]

Créez un fichier `aluno.json` similaire à :

```json
{
    "nome": "Ana",
    "idade": 16,
    "notas": [14, 15, 12]
}
```

Écrivez un programme qui :

- essaie d'ouvrir et de lire le fichier `aluno.json` avec `json.load`;
- si le fichier n'existe pas, récupère `FileNotFoundError` et affiche un message ;
- si le fichier existe mais que le contenu est corrompu (JSON invalide), récupère `json.JSONDecodeError` et affiche un message approprié message ;
- si tout se passe bien, il affiche le nom de l'élève et la note moyenne.

> Résolution :

```python
import json

try:
    with open("étudiant.json", "r", codage="utf-8") as f:
        donnees = json.load(f)
except FileNotFoundError:
    print("Fichier Student.json introuvable.")
except json.JSONDecodeError:
    print("Le contenu du fichier Student.json n'est pas valide.")
else:
    nom = donnees["nom"]
    remarques = donnees["remarques"]
    moyenne = sum(remarques) / len(remarques) if remarques else 0
    print(f"Étudiant : {nom}")
    print(f"Moyenne : {moyenne:.2f}")
```

---

### Exercice 7 - Menu avec validation d'option · [INTERMÉDIAIRE]

Écrire un petit programme avec menu :

```text
1 - Dizer olá
2 - Mostrar a tabuada do 5
3 - Sair
```

Exigences :

- le programme demande une option à l'utilisateur ;
- utilise `try`/`except` pour s'assurer que l'option est un entier valide ;
- si l'option n'existe pas (par exemple, 10), il affiche un message et demande à nouveau ;
- ne se termine que lorsque l'utilisateur choisit l'option 3.

> Résolution :

```python
while True:
    print("Menu:")
    print("1 - Dites bonjour")
    print("2 - Afficher le tableau de 5 multiplications")
    print("3 - Sortie")
    try:
        option = int(input("Choisissez une option (1-3) : "))
        if option == 1:
            print("Bonjour!")
        elif option == 2:
            print("Tableau de 5 multiplications :")
            for i in range(1, 11):
                print(f"5 x {i} = ​​​​ {5 * i}")
        elif option == 3:
            print("Sortie...")
            break
        else:
            print("Option invalide. Essayer à nouveau.")
    except ValueError:
        print("Veuillez saisir un entier valide.")
```

---

### Exercice 8 (Challenge) - Calculatrice de base avec validation (utilise \*args) · [CHALLENGE]

Écrivez une fonction `calculadora(operacao, *numeros)` qui :

- reçoit une chaîne `operacao` qui peut être `"soma"`, `"subtrai"`, `"multiplica"` ou `"divide"`;
- prend un nombre variable d'arguments `numeros` (au moins deux);
- effectue l'opération indiquée sur tous les nombres donnés;
- utilise `try`/`except` pour gérer :
 - `ValueError` si l'un des arguments n'est pas numérique;
 - `ZeroDivisionError` si vous essayez de diviser par zéro (dans ce cas, renvoie `None`);
 - `TypeError` si l'opération n'est pas reconnue (affiche un message clair).
 - Crée une erreur `ValueError` si moins de deux nombres sont donnés.

Exemples d'utilisation :

```python
print(calculatrice("somme", 10, 5, 3))          # renvoie 18
print(calculatrice("soustraire", 10, 5, 3))       # retour 2
print(calculatrice("multiplier", 2, 3, 4))      # renvoie 24
print(calculatrice("diviser", 10, 2, 0))         # renvoie Aucun (en raison de la division par zéro)
print(calculatrice("diviser", 10, "le"))          # gère ValueError
print(calculatrice("pouvoir", 2, 3))           # gère TypeError
print(calculatrice("somme", 10))                  # gère ValueError (moins de deux nombres)
```

> Résolution :

```python
def calculatrice(operation, *nombres):
    if len(nombres) < 2:
        raise ValueError("Vous devez fournir au moins deux numéros.")

    try:
        if operation == "somme":
            return sum(nombres)
        elif operation == "soustraire":
            resultat = nombres[0]
            for n in nombres[1:]:
                resultat -= n
            return resultat
        elif operation == "multiplier":
            resultat = 1
            for n in nombres:
                resultat *= n
            return resultat
        elif operation == "diviser":
            resultat = nombres[0]
            for n in nombres[1:]:
                resultat /= n
            return resultat
        else:
            raise TypeError(f"Opération '{operation}' non reconnue.")
    except ValueError:
        print("Erreur : tous les arguments doivent être numériques.")
    except ZeroDivisionError:
        print("Erreur : division par zéro détectée.")
    except TypeError as te:
        print(te)
        return None
```

---

### Exercice 9 (Challenge) - Statistiques de JSON · [CHALLENGE]

En supposant un fichier `notas.json` avec :

```json
{
    "alunos": [
        { "nome": "Ana", "notas": [14, 15, 12] },
        { "nome": "Bruno", "notas": [10, 9, 11] },
        { "nome": "Carla", "notas": [16, 18, 17] }
    ]
}
```

Écrire un programme qui :

- essaie de lire le fichier `notas.json`;
- si le fichier n'existe pas, obtient `FileNotFoundError` et affiche un message;
- si le contenu n'est pas valide, obtient `json.JSONDecodeError` et affiche un message;
- si tout se passe bien, calcule et affiche :
 - la moyenne de chaque élève ;
 - la moyenne générale de la classe;
 - le nom de l'élève avec la moyenne la plus élevée.

> Résolution :

```python
import json
try:
    with open("notes.json", "r", codage="utf-8") as f:
        donnees = json.load(f)
except FileNotFoundError:
    print("Fichier Notas.json introuvable.")
except json.JSONDecodeError:
    print("Le contenu du fichier Notas.json n'est pas valide.")
else:
    etudiants = donnees.get("étudiants", [])
    if not etudiants:
        print("Aucun étudiant trouvé.")
    else:
        somme_generale = 0
        notes_totales = 0
        meilleur_eleve = None
        meilleure_moyenne = -1

        for etudiant in etudiants:
            nom = etudiant.get("nom", "Inconnu")
            remarques = etudiant.get("remarques", [])
            if remarques:
                moyenne = sum(remarques) / len(remarques)
                print(f"{nom} : Moyenne = {moyenne:.2f}")
                somme_generale += sum(remarques)
                notes_totales += len(remarques)

                if moyenne > meilleure_moyenne:
                    meilleure_moyenne = moyenne
                    meilleur_eleve = nom
            else:
                print(f"{nom} : Aucune note disponible.")

        if notes_totales > 0:
            moyenne_generale = somme_generale / notes_totales
            print(f"Moyenne générale de la classe : {moyenne_generale:.2f}")
            print(f"Meilleur élève : {meilleur_eleve} avec moyenne {meilleure_moyenne:.2f}")
```

---

### Exercice 10 (Défi) - Journal avec options et gestion des erreurs · [DÉFI]

Rassemblez ce que vous avez appris dans les fichiers et les exceptions.  
Créez un programme qui fonctionne comme un simple « journal » :

```text
1 - Escrever nova entrada
2 - Ver entradas
3 - Sair
```

Exigences :

- toutes les entrées sont enregistrées dans `diario.json`;
- lors du choix de « Ecrire une nouvelle entrée » :
 - demande la date (format `YYYY-MM-DD`);
 - demande le texte de l'entrée;
 - enregistre l'entrée dans le fichier JSON (crée le fichier s'il n'existe pas);
- en choisissant « Afficher les entrées » :
 - essaie de lire le fichier `diario.json`;
 - si le fichier n'existe pas, affiche un message approprié;
 - si le fichier existe, affiche toutes les entrées avec la date et le texte;
- utilise `try`/`except` pour gérer les erreurs de fichier et les non valides JSON.

> Résolution :

```python
import json
import os # Pour vérifier si le fichier existe
FICHIER_JOURNAL = "journal.json"

def journal_de_chargement():
    if not os.path.exists(FICHIER_JOURNAL): # Vérifie si le fichier existe
        return []
    try:
        with open(FICHIER_JOURNAL, "r", codage="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Erreur : Le fichier journal est corrompu.")
        return []
def enregistrer_le_journal(entrees):
    with open(FICHIER_JOURNAL, "w", codage="utf-8") as f:
        json.dump(entrees, f, assurer_ascii=False, retrait=4)
def ecrire_une_entree():
    date = input("Date (AAAA-MM-JJ) : ")
    texte = input("Texte d'entrée : ")
    entrees = journal_de_chargement()
    entrees.append({"date": date, "texte": texte})
    enregistrer_le_journal(entrees)
    print("Entrée enregistrée.")
def voir_les_entrees():
    entrees = journal_de_chargement()
    if not entrees:
        print("Aucune entrée dans le journal.")
        return
    for interdit in entrees:
        print(f"{interdit['data']} : {interdit['texto']}")
def principal():
    while True:
        print("Menu du journal :")
        print("1 - Écrire une nouvelle entrée")
        print("2 - Afficher les entrées")
        print("3 - Sortie")
        try:
            option = int(input("Choisissez une option (1-3) : "))
            if option == 1:
                ecrire_une_entree()
            elif option == 2:
                voir_les_entrees()
            elif option == 3:
                print("Sortie...")
                break
            else:
                print("Option invalide. Essayer à nouveau.")
        except ValueError:
            print("Veuillez saisir un entier valide.")
principal()

---

## 10. Journal des modifications

-   `2025-02-XX` · creation initial do deposer avec introduction a exceptions, en_lisant de messages de erreur e `try`/`except` basique.
```
