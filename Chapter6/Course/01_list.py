# Création d'une liste
leisure = ['swim', 'dance', 'sing']
print(leisure)
print(type(leisure))
print('----------')
# Longueur d'une liste
print(len(leisure))
print('----------')
# Test de présence d'un élément
print('basketball' in leisure)
print('sing' in leisure)
print('DANCE' in leisure)
print('----------')
# Index d'un élément
print(leisure.index('swim'))
print(leisure.index('sing'))
print('----------')
# Accéder aux éléments d'une liste
print(leisure[1])
print('----------')
# Modifier la valeur d'un élément de liste
leisure[0] = 'ski'
print(leisure[0])
print(leisure)
print('----------')
# Ajouter un élément à une liste
leisure.append('game')
print(leisure)
print('----------')
# Insérer un élément ailleurs qu'à la fin
leisure.insert(3, 'climb')
print(leisure)
print('----------')
# Enlever un élément de liste
leisure.remove('climb')
print(leisure)
print('----------')
# Enlever un élément ailleurs avec son index
leisure.pop(1)
print(leisure)
print('----------')
# Vider une liste
leisure.clear()
print(leisure)
print('----------')

month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
# Concaténer deux listes
various_times = month + season
print(various_times)
print('----------')
# Étendre une liste
month.extend(season)
print(month)
print(season)
print('----------')

rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(len(rainbow))
# Créer une tranche de liste
print(rainbow[1:4])
# print(rainbow[3:8])
print(rainbow[3:])
print(rainbow[:5])
print(rainbow[-5:-2])




