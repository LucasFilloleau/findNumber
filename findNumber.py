# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:00:41 2025

@author: Lucas
"""

from random import *

# Définition des variables

scores = []
partie = 1

# Définition des fonctions 

def tirerunnombre() :
    """fontion permettant de générer un nombre entier aléatoire entre 1 et 100"""
    return randint(1, 100)

def demandeutilisateur() :
    """fonction qui demande à l'utilisateur et vérifie qu'il s'agit d'un entier entre 1 et 100"""
    nbutil = int(input("entrez un entier entre 1 et 100 :\n"))
    if verif(nbutil) != True :
        print("Le nombre n'est pas compris entre 1 et 100.")
    return nbutil

def plusgrand(nbutil, nbordi):
    """fonction renvoyant True si le plus grand des nombres ordi et util est util"""
    if nbutil>nbordi :
        return True
    
def verif(nbutil):
    if nbutil >= 1 and nbutil <= 100:
        return True
    
# Définition de la fonction jeu

def jeu():
    """Jeu "plus grand plus petit", complet"""
    partie = 1
    try :
        def jeu1() :
            """Jeu "plus grand plus petit", brut"""
            pseudo = str(input("Enterz vote pseudo :\n"))
            nbordi = tirerunnombre()
            nbutil = demandeutilisateur()
            print(nbordi)
            essais=1
        
        while(nbutil != nbordi):
            essais = essais + 1
            if plusgrand(nbutil, nbordi) == True:
                    print("Le chiffre est plus petit\n")
            else:
                print("Le chiifre est plus grand\n")
                nbutil = demandeutilisateur()
            print("Tu as gagné", pseudo, "! Il t'as fallu", essais, "essais.")
    
        # Tableau des scores
    
        scores.append((pseudo,essais))
        scores.sort(key=lambda joueur: joueur[1])  # Tri par nombre d'essais
        print("\nTableau des scores :")
        for i, (nom, score) in enumerate(scores, start=1):
            print(i, nom, " - ", score,"essais")
    except ValueError:
         print("Entrez une réponse valide")
   
    # boucle du jeu
    
    reponse=str(input('''Voulez vous rejouer ? Si oui tapez "Oui" sinon, tapez "Non"\n'''))
    if reponse == "Oui" or reponse == "oui":
        jeu()
    else:
        partie = partie + 1
        None

# Exécution du jeu

jeu()
