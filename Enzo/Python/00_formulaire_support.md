# Formulaire de support · Python (10e année)

> Feuille de référence rapide pour les tests.

---

## 1) Entrées/sorties et conversions

```python
# Lire le texte (str)
s = input("Texte: ").strip()

# Convertir en nombre
n_entier = int(input("Entier: ").strip())
nfloat = float(input("Réel: ").strip())

# Normaliser le texte
plus_bas = s.lower()
t_superieur = s.upper()

# f-string
message = f"{s} -> {n_entier} / {nfloat:.2f}"
```

- `type(valor)` pour confirmer le type.
- `bool(...)` interprète `0`, `""`, `[]`, `{}`, `None` comme `False`.

---

## 2) Essentiel opérateurs

- **Arithmétique** : `+ - * / // % **`
- **Comparaison** : `== != > >= < <=`
- **Logique** : `and`, `or`, `not`
- **Pertinence** : `item in seq`, `item not in seq`
- **Identité** : `is`, `is not` (surtout avec `None`)
- **Affectations composées** : `+=`, `-=`, `*=`, ...

N'oubliez pas d'enchaîner les comparaisons : `1 < x <= 10`.

---

## 3) Conditions (`if / elif / else`)

```python
if etat_principal:
    ...
elif une_autre_condition:
    ...
else:
    ...

# Intervalles
if 5 <= avis <= 15:
    ...

# Ternaire
statut = "plus gros" if age >= 18 else "plus petit"
```

Prenez soin de l'indentation (4 espaces).

---

## 4) Cycle `for` et `range`

```python
# plage (inclusive_start, exclusive_end, étape)
for i in range(0, 5):
    ...  # 0,1,2,3,4

for paire in range(2, 11, 2):
    ...  # 2,4,6,8,10

for article in sequence:
    ...  # chaînes, listes, etc.
```

Utile pour les sommations, les décomptes, le parcours des collections.

---

## 5) Cycle `while` et validation

```python
valeur = int(input("0-20 : "))
while valeur < 0 or valeur > 20:
    print("Invalide.")
    valeur = int(input("0-20 : "))
```

- Idéal pour répéter jusqu'à ce qu'une condition ne soit plus vraie.
- Contrôle les variables d'état pour éviter les cycles infinis.

---

## 6) Listes (création et méthodes)

```python
chiffres = [10, 20, 30]
chiffres.append(40)
chiffres.insert(1, 15)
dernier = chiffres.pop()      # supprimer la fin
chiffres.remove(15)          # première occurrence
chiffres.sort()              # changer de liste
ordonne = sorted(chiffres)  # exemplaire commandé
```

- Indices positifs et négatifs (`lista[-1]`).
- Fonctions utiles : `len`, `sum`, `min`, `max`.
- Patterns : accumulation, filtrage, transformation, recherche min/max manuellement.

---

## 7) Dictionnaires

```python
personne = {"nom": "Nain", "âge": 16}
personne["ville"] = "Lisbonne"
age = personne.get("âge", 0)
for cle, valeur in personne.items():
    ...
```

- Clés normalement `str`, valeurs de tout type.
- Méthodes : `keys`, `values`, `items`, `pop`.
- Utilisation des contrôles `in` clés.

---

## 8) Structures et modèles imbriqués (listes/dictionnaires)

- Liste de listes (tableau) : `matriz[linha][coluna]`.
- Dictionnaire de listes (classe → étudiants).
- Dictionnaire de dictionnaires (étudiant → → discipline grade).
- Liste des dictionnaires (collections d'enregistrements).

Modèles fréquents :

- Cycles imbriqués pour parcourir des tableaux et des collections complexes.
- Comptes conditionnels (négatifs, réussis, etc.).
- Recherche d'éléments par nom/titre en ignorant les majuscules. (`valor.lower()`).

---

## 9) Fonctions (`def`, paramètres, `return`)

```python
def nom_de_la_fonction(parametre1, parametre2=valeur):
    if condition_particuliere:
        return ...
    resultat = parametre1 + parametre2
    return resultat

# Appel
valeur = nom_de_la_fonction(arg1, parametre2=arg2)
```

- Préférez `return` pour réutiliser les résultats.
- Peut renvoyer plusieurs valeurs via des tuples : `return quociente, resto`.
- Paramètres : valeurs positionnelles, nommées, par défaut.

---

## 10) Fonctions avancées (essentielles concepts)

- `*args` et `**kwargs` pour les arguments variables.
- Attention à la mutabilité : modification des listes/dictionnaires passés par référence ; évite les valeurs par défaut mutables (utilise `None` + initialisation interne).
- `lambda` et les fonctions d'ordre supérieur (`map`, `filter`, `sorted(key=...)`) apparaissent comme une curiosité ; appliquer uniquement si cela est confortable.
- Portée : variables locales vs globales (`global`, `nonlocal` uniquement lorsque cela est indispensable).

---

## 11) Découpage et compréhension de listes

```python
sequence_2 = [0, 1, 2, 3, 4, 5]
gros1 = sequence_2[1:4]      # index 1..3
gros2 = sequence_2[:3]       # commencer à indexer 2
gros3 = sequence_2[::2]      # étape 2
inverse = sequence_2[::-1]

double = [x * 2 for x in sequence_2]
paires = [x for x in sequence_2 if x % 2 == 0]
etiquette = ["paire" if x % 2 == 0 else "impair" for x in sequence_2]
```

- Fonctionne également avec des chaînes (`texto[a:b]`).
- Les compréhensions remplacent les simples cycles de construction de listes ; évite les effets secondaires en leur sein.

---

## 12) Fichiers texte (`.txt`)

```python
# Écrire
with open("données.txt", "w", codage="utf-8") as f:
    f.write("ligne 1\n")

# Lire ligne par ligne
with open("données.txt", "r", codage="utf-8") as f:
    for doubler in f:
        contenu = doubler.rstrip("\n")
        ...
```

- Modes : `"r"`, `"w"`, `"a"`.
- `with` garantit la fermeture automatique du fichier.

---

## 13) JSON (`json.dump` / `json.load`)

```python
import json

donnees = {"nom": "Nain", "âge": [16, 17]}
with open("données.json", "w", codage="utf-8") as f:
    json.dump(donnees, f, assurer_ascii=False, retrait=4)

with open("données.json", "r", codage="utf-8") as f:
    infos = json.load(f)
```

- Structures typiques : listes de dictionnaires, dictionnaire de listes.
- Maintient la séparation entre la logique (fonctions qui gèrent `info`) et les E/S (fonctions qui lisent/écrivent).

---

## 14) CSV « manuel »

```python
enregistrements = [
    {"nom": "Nain", "âge": 16, "avis": 15},
    ...
]

with open("étudiants.csv", "w", codage="utf-8") as f:
    f.write("nom;âge;grade\n")
    for reg in enregistrements:
        doubler = f"{reg['nome']};{reg['idade']};{reg['nota']}\n"
        f.write(doubler)

with open("étudiants.csv", "r", codage="utf-8") as f:
    en_tete = f.readline()
    for doubler in f:
        nom, age, avis = doubler.strip().split(";")
        age = int(age)
        avis = int(avis)
        ...
```

- Faites attention à la conversion de type après `split`.
- `newline=""` recommandé lors de l'utilisation du module `csv` (facultatif pour cette fiche).

---

## 15) Planification + tests rapides (révision `00`)

- Identifie les **entrées**, **traitements** et **sorties** avant d'écrire du code.
- Décompose les problèmes en petites fonctions (logique vs interface).
- Utilise les modèles appris (accumulation, comptage, filtrage, transformation).
- Valide les données avant de les enregistrer ou de les écrire dans des fichiers.
- Exécute des tests rapides avec temporaire `assert` ou `print` pour confirmer chaque partie.
- Garde les enregistrements (JSON/CSV) à jour et cohérents tout au long de l'exécution.

Bonne préparation !
