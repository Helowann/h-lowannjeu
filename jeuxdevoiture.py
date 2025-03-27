import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
bleu = (50, 153, 213)
vert = (0, 255, 0)

# Taille de l'écran
largeur = 800
hauteur = 600

# Créer l'écran de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de Voiture")

# Vitesse et FPS
vitesse = 30
horloge = pygame.time.Clock()

# Taille de la voiture
largeur_voiture = 50
hauteur_voiture = 100

# Police pour le score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Fonction pour afficher le score
def afficher_score(score):
    score_text = font_style.render("Score: " + str(score), True, noir)
    fenetre.blit(score_text, [0, 0])

# Fonction pour dessiner la voiture
def dessiner_voiture(x, y):
    pygame.draw.rect(fenetre, rouge, [x, y, largeur_voiture, hauteur_voiture])

# Fonction pour dessiner l'obstacle
def dessiner_obstacle(obstacle_x, obstacle_y):
    pygame.draw.rect(fenetre, bleu, [obstacle_x, obstacle_y, largeur_voiture, hauteur_voiture])

# Fonction principale du jeu
def jeu():
    x = largeur / 2
    y = hauteur - hauteur_voiture - 10
    x_change = 0

    # Position de l'obstacle
    obstacle_x = random.randrange(0, largeur - largeur_voiture)
    obstacle_y = -600
    obstacle_vitesse = 5

    score = 0

    # Boucle du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # Déplacer la voiture
        x += x_change

        # Contrôler les limites de la voiture
        if x < 0:
            x = 0
        elif x > largeur - largeur_voiture:
            x = largeur - largeur_voiture

        # Déplacer l'obstacle
        obstacle_y += obstacle_vitesse
        if obstacle_y > hauteur:
            obstacle_y = -600
            obstacle_x = random.randrange(0, largeur - largeur_voiture)
            score += 1
            obstacle_vitesse += 0.1  # Augmente la vitesse des obstacles

        # Vérifier la collision
        if y < obstacle_y + hauteur_voiture:
            if x > obstacle_x and x < obstacle_x + largeur_voiture or x + largeur_voiture > obstacle_x and x + largeur_voiture < obstacle_x + largeur_voiture:
                game_over(score)

        # Remplir l'écran avec la couleur de fond
        fenetre.fill(blanc)

        # Dessiner la voiture et l'obstacle
        dessiner_voiture(x, y)
        dessiner_obstacle(obstacle_x, obstacle_y)

        # Afficher le score
        afficher_score(score)

        pygame.display.update()

        # Contrôler la vitesse du jeu
        horloge.tick(vitesse)

# Fonction de fin du jeu
def game_over(score):
    game_over_font = pygame.font.SysFont("comicsansms", 50)
    game_over_text = game_over_font.render("GAME OVER", True, rouge)
    score_text = font_style.render("Score final : " + str(score), True, noir)
    
    fenetre.fill(blanc)
    fenetre.blit(game_over_text, [largeur / 4, hauteur / 4])
    fenetre.blit(score_text, [largeur / 3, hauteur / 2])
    pygame.display.update()

    pygame.time.wait(3000)
    pygame.quit()
    quit()

# Lancer le jeu
jeu()