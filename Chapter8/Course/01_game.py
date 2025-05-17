# Importation des module requis
import pygame
import sys

# Initialiser
pygame.init()

# Configuration de la fenêtre de l'écran d'accueil
screen = pygame.display.set_mode((400, 400))

# 主要的颜色：白色(255,255,255)  黑色(0,0,0)
# screen.fill((255, 255, 255))
# 主屏幕的颜色（背景色）
screen.fill((255, 182, 193))

# Définir le titre de la fenêtre
pygame.display.set_caption("My first game")

# Introduction des types de polices
f = pygame.font.SysFont('Arial', 50)
# Génèrer un messga texte
"""
1. Le contenu du texte     文本内容
2. La police est lisse ou non    字体是否顺滑
3. La couleur de la police (en mode RGB)   文本的颜色
4. La couleur de fond de la police         文本的背景色
"""
text = f.render("Happy game", True, (255, 0, 0), (0, 0, 255))
# Obtenir les coordonnées de la zone rectangulaire de l'objet affiché
text_rect = text.get_rect()
# Définir l'objet d'affichage pour qu'it soit centré
text_rect.center = (200, 200)
# Prendre le message texte préparé et dessiner-le sur l'écran d'accueil
screen.blit(text, text_rect)
while True:
    # Boucle pour les événements et écoute pour le statut de l'événement
    for event in pygame.event.get():
        # Déterminer si l'utilisateur a cliqué sur le bouton de fermeture "X"
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Mise à jour du contenu du l'écran
    pygame.display.flip()


