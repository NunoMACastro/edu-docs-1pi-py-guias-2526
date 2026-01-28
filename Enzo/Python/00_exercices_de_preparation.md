# Python (10e année) - 00 · Exercices de préparation

> **Objectif de ce dossier** 
> Préparer les étudiants aux évaluations, à travers des exercices qui font appel aux concepts de base de Python.

## Préparation au test du 15/12/2025

Sujets qui seront évalué :

- Fonctions :

 - Définition et invocation de fonctions
 - Paramètres et arguments
 - Valeurs de retour
 - _\*args et \*\*kwargs_

- Fichiers JSON :
 - Lecture et écriture de JSON fichiers

Sujets précédents qui peuvent être utiles :

- Types de données de base (entiers, chaînes, listes, dictionnaires)
- Structures de contrôle (if, pour, tant que)
- Listes et dictionnaires

### Exercices

**Fonctions simples sans return**

1. Écrivez une fonction appelée `saudacao` qui prend un nom comme paramètre et imprime un message de bienvenue personnalisé.

> Résolution :

```python
def salutation(nom):
    print(f"Bonjour, {nom} ! Bienvenue dans le cours Python.")

# Exemple d'utilisation :
salutation("Marie")
```

2. Écrivez une fonction pour chacune des opérations mathématiques de base (addition, soustraction, multiplication, division) qui prend deux nombres comme paramètres et imprime le résultat de l'opération.

> Résolution :

```python
def ajouter(a, b):
    print(f"La somme de {a} et {b} est {a + b}")
def soustraire(a, b):
    print(f"La soustraction de {a} et {b} est {a - b}")
def multiplier(a, b):
    print(f"La multiplication de {a} et {b} est {a * b}")
def diviser(a, b):
    if b != 0:
        print(f"Diviser {a} par {b} donne {a / b}")
    else:
        print("Erreur : La division par zéro n'est pas autorisée.")

# Exemple d'utilisation :
ajouter(5, 3)
soustraire(10, 4)
multiplier(2, 6)
diviser(8, 2)
diviser(5, 0)
```

3. Crée une fonction qui calcule l'aire d'un rectangle. La fonction doit recevoir la largeur et la hauteur en paramètres et imprimer la zone.

> Résolution :

```python
def zone_rectangulaire(largeur, hauteur):
    zone = largeur * hauteur
    print(f"L'aire du rectangle est {zone}")

# Exemple d'utilisation :
zone_rectangulaire(5, 10)
```

4. Écrivez une fonction qui reçoit une liste de nombres et imprime chaque nombre multiplié par 2.

> Résolution :

```python
def multiplier_par_deux(nombres):
    for nombre in nombres:
        print(nombre * 2)

# Exemple d'utilisation :
multiplier_par_deux([1, 2, 3, 4, 5])
```

---

**Fonctions**

5. Réécrivez les fonctions des exercices 2 et 3 pour qu'elles renvoient le résultat au lieu de l'imprimer. Testez les fonctions en imprimant les valeurs renvoyées.

> Résolution :

```python
def ajouter(a, b):
    return a + b
def soustraire(a, b):
    return a - b
def multiplier(a, b):
    return a * b
def diviser(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : La division par zéro n'est pas autorisée."

def zone_rectangulaire(largeur, hauteur):
    return largeur * hauteur

# Exemple d'utilisation :
print(ajouter(5, 3))
print(soustraire(10, 4))
print(multiplier(2, 6))
print(diviser(8, 2))
print(diviser(5, 0))
print(zone_rectangulaire(5, 10))
```

6. Crée une fonction qui prend une liste de nombres et renvoie la somme de tous les nombres pairs de la liste.

> Résolution :

```python
def paires_de_somme(nombres):
    somme = 0
    for nombre in nombres:
        if nombre % 2 == 0:
            somme += nombre
    return somme

# Exemple d'utilisation :
print(paires_de_somme([1, 2, 3, 4, 5, 6]))  # Devrait revenir 12
```

7. Écrivez une fonction qui reçoit une chaîne et renvoie le nombre de voyelles dans la chaîne.

> Résolution :

```python
def compter_les_voyelles(texte):
    voyelles = "aeiouAEIOUàáâãäåèéêëìíîïòóôõöùúûüÁÀÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜ"
    comptoir = 0
    for carboniser in texte:
        if carboniser in voyelles:
            comptoir += 1
    return comptoir

# Exemple d'utilisation :
print(compter_les_voyelles("Bonjour le monde!"))  # Devrait revenir 4
```

8. Crée une fonction qui reçoit une liste de mots et renvoie le mot le plus long de la liste.

> Résolution :

```python
def mot_le_plus_long(mots):
    le_plus_long = mots[0]
    for mot in mots:
        if len(mot) > len(le_plus_long):
            le_plus_long = mot
    return le_plus_long

# Exemple d'utilisation :
print(mot_le_plus_long(["maison", "automobile", "vélo", "avion"]))  # Devrait renvoyer "automobile"
```

9. Écrivez une fonction qui prend deux paramètres : une liste de nombres et un nombre. La fonction doit renvoyer `True` si le numéro est dans la liste et `False` sinon.

> Résolution :

```python
def numero_dans_la_liste(nombres, nombre):
    return nombre in nombres # Renvoie True si le numéro est dans la liste, sinon False

# Exemple d'utilisation :
print(numero_dans_la_liste([1, 2, 3, 4, 5], 3))  # Doit renvoyer Vrai
print(numero_dans_la_liste([1, 2, 3, 4, 5], 6))  # Devrait renvoyer Faux
```

10. Crée une fonction qui reçoit un dictionnaire et l'affiche de manière organisée.

> Résolution :

```python
def afficher_le_dictionnaire(dictionnaire):
    for cle, valeur in dictionnaire.items():
        print(f"{cle} : {valeur}")

# Exemple d'utilisation :
afficher_le_dictionnaire({"nom": "John", "âge": 25, "ville": "Lisbonne"})
```

11. Créez une fonction qui reçoit une liste de dictionnaires (chaque dictionnaire représente une personne avec un nom et un âge) et renvoie l'âge moyen.

> Résolution :

```python
def moyen_age(personnes):
    age_total = 0
    for personne in personnes:
        age_total += personne["âge"]
    return age_total / len(personnes)
# Exemple d'utilisation :
personnes = [{"nom": "Nain", "âge": 30}, {"nom": "Bruno", "âge": 25}, {"nom": "Carla", "âge": 35}]
print(moyen_age(personnes))  # Devrait renvoyer 30,0
```

12. Considérons un dictionnaire au format suivant :

```python
{
    1 : {
        "nom": "Nain",
        "remarques": {
            "Mathématiques": 18,
            "Physique": 16,
            "Chimique": 17
        },
        "fautes": {
            "Mathématiques": 2,
            "Physique": 0,
            "Chimique": 1
        }
    }
}
```

Créer des fonctions pour :

- Calculer la moyenne des notes d'un élève.
- Calculer les absences totales d'un élève.
- Afficher tous les étudiants de manière organisée.

> Résolution :

```python

def calculer_les_notes_moyennes(etudiant):
    remarques = etudiant["remarques"].values()
    return sum(remarques) / len(remarques)

# Ou utiliser pour :
# def calculate_average_grades (étudiant):
#     total = 0
#     compte = 0
#     pour la note de student["notes"].values() :
#         total += note
#         compter += 1
#     retourner le total/compte

def calculer_le_total_des_absences(etudiant):
    fautes = etudiant["fautes"].values()
    return sum(fautes)

# Ou utiliser pour :
# def calculate_total_absences(étudiant):
#     total = 0
#     pour absence dans student["fatas"].values() :
#         total += manque
#     retour total

def montrer_aux_etudiants(etudiants):
    for carte_d_etudiant, donnees in etudiants.items():
        print(f"Identifiant : {carte_d_etudiant}")
        print(f"Nom : {donnees['nome']}")
        print(f"Note moyenne : {calculer_les_notes_moyennes(donnees)}")
        print(f"Total des fautes : {calculer_le_total_des_absences(donnees)}")
        print("-" * 20)
```

---

** arguments et kwargs **

13. Crée une fonction qui prend un nombre variable d'arguments et renvoie la somme de tous les arguments.

> Résolution :

```python
def somme_variable(*arguments):
    total = 0
    for nombre in arguments:
        total += nombre
    return total
# Exemple d'utilisation :
print(somme_variable(1, 2, 3, 4, 5))  # Devrait revenir 15
```

14. Crée une fonction qui reçoit un nombre variable d'arguments et renvoie le plus grand et le plus petit nombre parmi eux.

> Résolution :

```python
def le_plus_grand_le_plus_petit(*arguments):
    plus_gros = max(arguments)
    plus_petit = min(arguments)
    return plus_gros, plus_petit

# Exemple d'utilisation :
plus_gros, plus_petit = le_plus_grand_le_plus_petit(3, 1, 4, 1, 5, 9, 2)
print(f"Majeur : {plus_gros}, Mineur : {plus_petit}")  # Doit renvoyer le plus grand : 9, le plus petit : 1
```

15. Crée une fonction qui prend un nombre variable d'arguments et indique combien sont pairs et combien sont impairs.

> Résolution :

```python
def compter_les_paires_impaires(*arguments):
    paires = 0
    impair = 0
    for nombre in arguments:
        if nombre % 2 == 0:
            paires += 1
        else:
            impair += 1
    return paires, impair

# Exemple d'utilisation :
paires, impair = compter_les_paires_impaires(1, 2, 3, 4, 5, 6)
print(f"Pairs : {paires}, Cotes : {impair}")  # Devrait renvoyer Pair : 3, Impair : 3
```

16. Crée une fonction qui prend un nombre variable d'arguments nommés et imprime chaque paire clé-valeur.

> Résolution :

```python
def imprimer_la_valeur_de_la_cle(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")

# Exemple d'utilisation :
imprimer_la_valeur_de_la_cle(nom="John", age=28, ville="Port")
```

---

**Fichiers JSON**

17. Il demande à l'utilisateur de saisir son nom, son âge et sa ville. Enregistrez ces données dans un fichier JSON au format d'un dictionnaire.

> Résolution :

```python
import json

def enregistrer_les_donnees_utilisateur():
    nom = input("Entrez votre nom : ")
    age = input("Entrez votre âge : ")
    ville = input("Entrez votre ville : ")

    donnees = {
        "nom": nom,
        "âge": age,
        "ville": ville
    }

    with open("user_data.json", "w") as deposer:
        json.dump(donnees, deposer, retrait=4)

enregistrer_les_donnees_utilisateur()
```

18. Lit le fichier JSON créé lors de l'exercice précédent et imprime les données de manière organisée.

> Résolution :

```python

import json
def lire_les_donnees_utilisateur():
    with open("user_data.json", "r") as deposer:
        donnees = json.load(deposer)

    print("Données utilisateur :")
    print(f"Nom : {donnees['nome']}")
    print(f"Âge : {donnees['idade']}")
    print(f"Ville : {donnees['cidade']}")

lire_les_donnees_utilisateur()
```

19. Créez une fonction qui reçoit une liste de dictionnaires (chaque dictionnaire représente une personne avec son nom et son âge) et stocke cette liste dans un fichier JSON.

> Résolution :

```python
import json
def enregistrer_la_liste_des_personnes(personnes, nom_de_fichier):
    with open(nom_de_fichier, "w") as deposer:
        json.dump(personnes, deposer, retrait=4)

# Exemple d'utilisation :
personnes = [{"nom": "Nain", "âge": 30}, {"nom": "Bruno", "âge": 25}, {"nom": "Carla", "âge": 35}]
enregistrer_la_liste_des_personnes(personnes, "personnes.json")
```

20. Créez une fonction qui lit le fichier JSON créé dans l'exercice précédent et renvoie la liste des dictionnaires.

> Résolution :

```python
import json
def lire_la_liste_des_personnes(nom_de_fichier):
    with open(nom_de_fichier, "r") as deposer:
        personnes = json.load(deposer)
    return personnes

# Exemple d'utilisation :
personnes = lire_la_liste_des_personnes("personnes.json")
print(personnes)
```

21. Crée un programme qui permet à l'utilisateur de gérer une liste de tâches. Le programme doit permettre d'ajouter, de supprimer et de lister des tâches. Les données doivent être enregistrées dans un fichier JSON. Sans utiliser d'exceptions.

> Résolution :

```python
import json

def ajouter_une_tache(taches, tache):
    taches.append(tache)

def supprimer_une_tache(taches, tache):
    if tache in taches:
        taches.remove(tache)

def lister_les_taches(taches):
    print("Tâches :")
    for tache in taches:
        print(f"- {tache}")

def enregistrer_des_taches(taches, nom_de_fichier):
    with open(nom_de_fichier, "w") as deposer:
        json.dump(taches, deposer, retrait=4)

def lire_les_taches(nom_de_fichier):
    with open(nom_de_fichier, "r") as deposer:
        taches = json.load(deposer)
    return taches

def menu():
    taches = []
    nom_de_fichier = "tâches.json"

    taches = lire_les_taches(nom_de_fichier)

    while True:
        print("\nMenu :")
        print("1. Ajouter une tâche")
        print("2. Supprimer la tâche")
        print("3. Lister les tâches")
        print("4. Déconnectez-vous")
        choix = input("Choisissez une option : ")

        if choix == "1":
            tache = input("Saisissez la tâche à ajouter : ")
            ajouter_une_tache(taches, tache)
            enregistrer_des_taches(taches, nom_de_fichier)
        elif choix == "2":
            tache = input("Saisissez la tâche à supprimer : ")
            supprimer_une_tache(taches, tache)
            enregistrer_des_taches(taches, nom_de_fichier)
        elif choix == "3":
            lister_les_taches(taches)
        elif choix == "4":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


menu()

```

22. Crée des fonctions pour un programme qui gère les notes des étudiants dans une classe. Le programme doit être capable de stocker les noms des étudiants et leurs notes dans différentes matières. Le programme doit conserver les données dans un fichier JSON. Il doit être possible de consulter la moyenne de chaque élève et si un élève donné a des négatifs (et combien).
 Le programme doit avoir les fonctions suivantes :
 save_student_data -> Fonction qui reçoit une liste des étudiants et l'écrit dans un fichier.
 read_student_data -> Fonction qui renvoie une liste des données des étudiants enregistrées dans un fichier
 calculate_average -> Fonction qui reçoit une liste des étudiants et affiche la moyenne de chaque élève de la liste
 return_negatives -> Fonction qui reçoit un élève et renvoie le nombre de négatifs de cet élève.

> Résolution :

```python
import json
def enregistrer_les_donnees_des_etudiants(etudiants, nom_de_fichier):
    with open(nom_de_fichier, "w") as deposer:
        json.dump(etudiants, deposer, retrait=4)

def lire_les_donnees_des_etudiants(nom_de_fichier):
    with open(nom_de_fichier, "r") as deposer:
        etudiants = json.load(deposer)
    return etudiants

def calculer_la_moyenne(etudiants):
    for etudiant in etudiants:
        remarques = etudiant["remarques"].values()
        moyenne = sum(remarques) / len(remarques)
        print(f"{etudiant['nome']} - Moyenne : {moyenne:.2f}")

def renvoie_un_resultat_negatif(etudiant):
    negatif = 0
    for avis in etudiant["remarques"].values():
        if avis < 10:
            negatif += 1
    return negatif

# Exemple d'utilisation :
etudiants = [
    {"nom": "Nain", "remarques": {"Mathématiques": 18, "Physique": 16, "Chimique": 9}},
    {"nom": "Bruno", "remarques": {"Mathématiques": 12, "Physique": 14, "Chimique": 11}},
    {"nom": "Carla", "remarques": {"Mathématiques": 8, "Physique": 7, "Chimique": 10}}
]

enregistrer_les_donnees_des_etudiants(etudiants, "étudiants.json")
les_etudiants_lisent = lire_les_donnees_des_etudiants("étudiants.json")
calculer_la_moyenne(les_etudiants_lisent)
for etudiant in les_etudiants_lisent:
    negatif = renvoie_un_resultat_negatif(etudiant)
    print(f"{etudiant['nome']} - Négatifs : {negatif}")
```
