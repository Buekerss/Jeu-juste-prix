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
import tkinter

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

#-----------------------------{ TKinter }--------------------------------#

# Creer la fenetre
WINDOW1 = Tk()

# Creer la FRAME
FRAME = Frame(WINDOW1, bg='#bcf8b1')

# Nommer la fenetre + divers parametres
WINDOW1.title("Le Juste Prix")
WINDOW1.geometry("680x360")
WINDOW1.minsize(680, 360)
WINDOW1.config(background='#bcf8b1')

# MESSAGE de bienvenu dans une frame
MESSAGE_JEU = Label (text="Bienvenue sur le célèbre JEU du juste prix,\n tu dois deviner le prix auquel je pense, il se situe entre 1 et 100", font=("Comic Sans MS", 20), bg='#bcf8b1')
MESSAGE_JEU.pack()

# Zone de texte
MSG_VALEUR = Label (FRAME, text="Choisit une VALEUR entre 1 et 100 :", font=("Comic Sans MS", 15), bg='#bcf8b1')
MSG_VALEUR.pack()
EXPRESSION = StringVar()
VALEUR = Entry (FRAME, textvariable=EXPRESSION)
VALEUR.pack()

# Bouton VALIDER
VALIDER = Button (FRAME, text="VALIDER", bg='white', command=JEU)
VALIDER.pack()

# Intergrer la FRAME a la fenetre
FRAME.pack(expand=YES)

# Afficher la fenetre
WINDOW1.mainloop()
