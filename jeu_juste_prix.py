#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jeu du juste prix"""

__author__ = "Gaël"
__contact__ = "gael.cottreau@hotmail.fr"
__copyright__ = "Copyleft"
__credits__ = ["Gaël Cottreau"]
__maintainer__ = "Gaël Cottreau"
__status__ = "Production"

# importation des bibliotheques
import random
import time

if __name__ == "__main__":
    # Message de Bienvenue
    print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")

    # L'ordinateur (ou le programme) choisit une valeur aleatoire comprise entre 1 et 100
    NB = random.randint(1, 100)

    # Print pour faciliter les test
    print(NB)

    # Nombre de CHANCEs donné a l'utilisateur pour trouver le nombre
    CHANCE = 5
    MAX = 60
    START = time.time()
    while True:
        DURATION = time.time() - START
        if DURATION >= MAX:
            print("Temps écoulé")
            print("Vous avez perdu")
            break

        # Verification du nombre de CHANCEs
        if CHANCE == 0:
            print("C'est perdu :'(")
            break

        # Récupération de la valeur choisie par  l'utilisateur
        VALEUR = int(input("Entrez un nombre entre 1 et 100 : "))
        print(MAX-DURATION, "s")

        # Boucle permettant de comparer la valeur choisit par l'ordinateur et celle choisie par l'utilisateur
        if VALEUR < NB:
            print("C'est plus..")
            CHANCE -= 1
        if VALEUR > NB:
            print("C'est moins..")
            CHANCE -= 1
        if VALEUR == NB:
            print("Bien joué ! il te restais : ", CHANCE, "CHANCEs")
            break