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
    choice = int(input("Choisissez une des catégories en tapant un chiffre entre 1 et 5: "))
    if choice == 1:
        shop_info()
    elif choice == 2:
        order_management()
    elif choice == 3:
        tracking_deliveries()
    elif choice == 4:
        service_marketing()
    elif choice == 5:
        others()
    else:
        choose_category()
    return

def others():
    transfer_therese()
    return

def transfer_therese():
    other_info = input("De quoi aimeriez-vous nous informer?")
    return

def service_marketing():
    print("Nous vous remercions pour votre suggestion et allons vous mettre en relation avec le service concerné.")
    transfer_raoul()

def transfer_raoul():
    suggestion_marketing = input("Dites-moi quel autre produit nous devrions proposer: ")
    return

def shop_info():
    address = "148 Boulevard Masséna 75013 PARIS"
    schedule = "du Lundi au Samedi 10h-18h"
    print("Thibault se retrouve au " + address + ".")
    print("La boutique est ouvert " + schedule + ".")
    other = input("Autre chose ? [y/n]")
    if other == 'y':
        choose_category()
        return

def order_management():
    print("Vous êtes au service de gestion des commandes.")
    client_name = input("Nom indiqué sur le bon de commande: ")
    order_number = input("Indiquez le numéro de commande: ")
    transfer_elliot()
    return

def tracking_deliveries():
    print("Nou sommes désolés que vous ayez subi un souci avec votre commande.")
    client_name = input("Nom indiqué sur le bon de commande: ")
    order_number = input("Indiquez le numéro de commande: ")
    follow = input("Décrivez votre problème: ")
    transfer_christine()
    return

def transfer_elliot():
    print("Parfait! Je vérifie le statut de votre commande.")
    return

def transfer_christine():
    print("Merci pour vos déails. Nous vérifons votre commande et vous recontactons au plus vite.")
    return

welcome()
choose_category()