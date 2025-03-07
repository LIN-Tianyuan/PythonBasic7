import random

computer = random.randint(1, 100)
count = 0
while True:
    number = int(input("Veuillez entrer un nombre: "))
    count = count + 1
    if number > computer:
        print("Plus petit.")
    elif number < computer:
        print("Plus grand.")
    else:
        print("Vous avez bien deviné %d fois au total." % count )
        break