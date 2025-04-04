# Définir une fonction
"""
def greet():
    print("Salut, Luna!")
"""

"""
def greet(name):
    print("Salut, " + name)
"""

"""
def greet(firstname, lastname):
    print("Salut, " + firstname + " " + lastname)


# greet("Lucie", "Liu")
# greet("Lucas")
greet("Lucie", "Liu")
"""

"""
# Paramètre par défaut
def season_pref(season="été"):
    print("Ma saison préferée est " + season + ".")

# season_pref("printemps")
# season_pref()
season_pref("printemps")
"""

"""
# Listes d'arguments
def visit(*countries):
    for country in countries:
        print("J'ai visité ce pays: " + country)

visit("France")
visit("Chine", "América")
visit("Allemagne", "Finlande", "Japon")
"""

def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: " + competitor_1 + " " + competitor_2 + " " + competitor_3)

# Positional argument
# Paramètre positionnel
list_game("Lucas", "Luna", "Alex")
# Paramètre par mot-clé
list_game(competitor_3="Lucas", competitor_2="Luna", competitor_1="Alex")


