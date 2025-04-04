def welcome():
    name_visitor = input("Merci de contacter Thibault! Je peux avoir votre prénom? ")
    print("Bienvenue chez Thibault! " + name_visitor)
    return

def choose_category():
    print("**** Menu général Thibault ****\n"
          "[1] Horaires & Accès \n"
          "[2] Gestion de commande \n"
          "[3] Suivi de livraison \n"
          "[4] Suggestion de produit \n"
          "[5] Autre sujet")

welcome()
choose_category()
