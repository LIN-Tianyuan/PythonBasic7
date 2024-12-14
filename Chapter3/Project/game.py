import random


player = int(input('Que voulez-vous jouer? Pierre(1) / Ciseaux(2) / Papier(3) : '))
computer = 1
print("Ordinateur joue pierre.")
if player == 2:
    print("L'ordinateur gagne.")
elif player == 1:
    print("Les deux côtés sont à égalité.")
else:
    print("Le joueur gagne.")

# print(random.randint(1, 10))
