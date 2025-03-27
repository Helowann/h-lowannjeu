import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Taille de l'écran
largeur = 600
hauteur = 400

# Créer l'écran de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu du Serpent')

# Définir la vitesse du serpent
vitesse = 15
horloge = pygame.time.Clock()

# Définir la taille du serpent
taille_serpent = 10

# Police pour les scores
font_style = pygame.font.SysFont("bahnschrift", 25)
font_score = pygame.font.SysFont("comicsansms", 35)

# Fonction pour afficher le score
def afficher_score(score):
    valeur = font_score.render("Score : " + str(score), True, noir)
    fenetre.blit(valeur, [0, 0])

# Fonction pour afficher le message de fin
def message(msg, couleur):
    mesg = font_style.render(msg, True, couleur)
    fenetre.blit(mesg, [largeur / 6, hauteur / 3])

# Fonction principale du jeu
def jeu():
    game_over = False
    game_close = False

    # Position initiale du serpent
    x1 = largeur / 2
    y1 = hauteur / 2

    # Vitesse initiale du serpent
    x1_change = 0
    y1_change = 0

    # Position de la nourriture
    foodx = round(random.randrange(0, largeur - taille_serpent) / 10.0) * 10.0
    foody = round(random.randrange(0, hauteur - taille_serpent) / 10.0) * 10.0

    serpent = []
    longueur_serpent = 1

    # Boucle du jeu
    while not game_over:

        while game_close:
            fenetre.fill(bleu)
            message("Tu as perdu ! Appuie sur C pour rejouer ou Q pour quitter", rouge)
            afficher_score(longueur_serpent - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -taille_serpent
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = taille_serpent
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -taille_serpent
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = taille_serpent
                    x1_change = 0

        # Vérifier si le serpent touche les bords de l'écran
        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(bleu)
        pygame.draw.rect(fenetre, vert, [foodx, foody, taille_serpent, taille_serpent])
        serpent_tete = []
        serpent_tete.append(x1)
        serpent_tete.append(y1)
        serpent.append(serpent_tete)

        if len(serpent) > longueur_serpent:
            del serpent[0]

        for x in serpent[:-1]:
            if x == serpent_tete:
                game_close = True

        for segment in serpent:
            pygame.draw.rect(fenetre, noir, [segment[0], segment[1], taille_serpent, taille_serpent])

        afficher_score(longueur_serpent - 1)

        pygame.display.update()

        # Vérifier si le serpent a mangé la nourriture
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, largeur - taille_serpent) / 10.0) * 10.0
            foody = round(random.randrange(0, hauteur - taille_serpent) / 10.0) * 10.0
            longueur_serpent += 1

        horloge.tick(vitesse)

    pygame.quit()
    quit()

# Lancer le jeu
jeu()