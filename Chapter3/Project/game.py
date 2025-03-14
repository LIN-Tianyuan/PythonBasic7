import random

player = int(input('Que voulez-vous jouer? Pierre(1) / Ciseaux(2) / Feuille(3) : '))
if player == 1 and player == 2 and player == 3:
    computer = random.randint(1, 3)
    print("L'ordinateur joue:" + str(computer))
    if (player == 1 and computer == 2) or (player == 3 and computer == 1) or (player == 2 and computer == 3):
        print("Le joueur gagne.")
    elif player == computer:
        print("Les deux côtés sont à égalité.")
    else:
        print("L'ordinateur gagne.")
else:
    print("Erreur.")




