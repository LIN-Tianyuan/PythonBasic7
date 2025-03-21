import random

my_collection = ['rouge', 'rose', 'orange', 'rouge',
                 'rose', 'jaune', 'rose', 'jaune']
bag_of_balls = ['rose', 'bleu', 'vert', 'orange', 'rouge',
                'poupre', 'vert', 'bleu', 'bleu', 'rouge',
                'vert', 'poupre', 'jaune', 'rouge', 'rose',
                'rouge', 'vert', 'jaune']

balls_outputs = []
count = 0
while True:
    computer = random.randint(0, 17)
    count = count + 1
    selection = bag_of_balls[computer]
    balls_outputs.append(selection)
    if count > 5:
        break
    elif selection == 'vert':
        my_collection.append(selection)
        print("Excellent! Tu as tiré ta bille verte!")
        print("Il restait " + str(5 - count) + " tirages.")
        break
if not('vert' in my_collection):
    print("Tous les tirages sont faits. Aucune bille verte.")
print("Billes sorties pour ce tirage: ")
print(balls_outputs)
print("La nouvelle collection contient: ")
print(my_collection)

"""
import random
selection = random.choice(bag_of_balls)
print(selection)
"""
