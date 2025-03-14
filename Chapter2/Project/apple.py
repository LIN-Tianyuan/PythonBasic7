"""
price = input("Veuillez entrer le prix des pommes: ")
weight = input("Veuillez entrer le poids des pommes: ")
int_price = int(price)
int_weight = int(weight)
money = int_price * int_weight
str_money = str(money)
print("Vous devez payer " + str_money + " euros.")
"""
price = float(input("Veuillez entrer le prix des pommes: "))
weight = float(input("Veuillez entrer le poids des pommes: "))
money = price * weight
print("Vous devez payer " + str(money) + " euros.")