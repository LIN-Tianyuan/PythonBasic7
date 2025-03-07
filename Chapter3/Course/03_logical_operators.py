"""
age = int(input("Veuillez entrer votre âge: "))
if age <= 120:
    if age > 0:
        print("Âge correct.")
    else:
        print("Âge incorrect.")
else:
    print("Âge incorrect.")
"""
"""
age = int(input("Veuillez entrer votre âge: "))
if age <= 120 and age > 0:
    print("Âge correct.")
else:
    print("Âge incorrect.")
"""

"""
score_python = int(input("Veuillez entrer votre score Python: "))
score_c = int(input("Veuillez entrer votre score C: "))
if score_python > 60 or score_c > 60:
    print("Réussir l'examen.")
else:
    print("Continuez à faire du bon travail.")
"""

# print(2 < 3 and 5 > 10)
print(2 < 3) # True
print(5 > 10) # False
print(2 < 3 and 5 > 10) # False
print(2 < 3 or 5 > 10)  # True
print(not(1 == 1))
