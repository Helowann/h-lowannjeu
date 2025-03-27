import pygame
import random
import math

# Initialiser pygame
pygame.init()

# Définir les couleurs (utilisées pour le texte, si nécessaire)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 600
TAILLE_CIBLE = 30
RAYON_LASER = 5
VITESSE_CIBLE = 3

# Créer la fenêtre du jeu
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Laser")

# Charger les images
image_cible = pygame.image.load('cible.png')  # Remplace par le chemin de ton image de cible
image_laser = pygame.image.load('laser.png')  # Remplace par le chemin de ton image de laser


# Redimensionner les images si nécessaire
image_cible = pygame.transform.scale(image_cible, (TAILLE_CIBLE, TAILLE_CIBLE))
image_laser = pygame.transform.scale(image_laser, (RAYON_LASER * 2, 10))  # Ajuste selon la taille souhaitée

# Classe Laser
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = image_laser  # Utiliser l'image du laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 10

    def update(self):
        # Déplacer le laser dans la direction donnée par l'angle
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

        # Supprimer le laser si il sort de l'écran
        if self.rect.x < 0 or self.rect.x > LARGEUR or self.rect.y < 0 or self.rect.y > HAUTEUR:
            self.kill()

# Classe Cible
class Cible(pygame.sprite.Sprite):
    def __init__(self, x, y, moving=False):
        super().__init__()
        self.image = image_cible  # Utiliser l'image de la cible
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.moving = moving
        self.speed = VITESSE_CIBLE

    def update(self):
        # Si la cible se déplace, elle se déplace horizontalement
        if self.moving:
            self.rect.x += self.speed
            if self.rect.x <= 0 or self.rect.x >= LARGEUR - TAILLE_CIBLE:
                self.speed = -self.speed  # Changer de direction

# Fonction principale du jeu
def jouer():
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    # Groupes de sprites
    lasers = pygame.sprite.Group()
    cibles = pygame.sprite.Group()

    score = 0
    game_over = False

    # Créer une première cible
    def ajouter_cible():
        moving = random.choice([True, False])  # Décider si la cible sera mobile ou non
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        cible = Cible(x, y, moving)
        cibles.add(cible)

    # Ajouter initialement des cibles
    for _ in range(3):  # Ajouter trois cibles initiales
        ajouter_cible()

    # Boucle principale du jeu
    while not game_over:
        screen.fill(NOIR)

     

        # Vérifier les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # Tirer un laser à partir de la position de la souris
                pos_souris = pygame.mouse.get_pos()
                angle = math.atan2(pos_souris[1] - HAUTEUR // 2, pos_souris[0] - LARGEUR // 2)
                laser = Laser(LARGEUR // 2, HAUTEUR // 2, angle)
                lasers.add(laser)

        # Mettre à jour les sprites
        lasers.update()
        cibles.update()

        # Vérifier les collisions entre les lasers et les cibles
        for laser in lasers:
            for cible in cibles:
                if laser.rect.colliderect(cible.rect):
                    laser.kill()  # Supprimer le laser
                    cible.kill()  # Supprimer la cible
                    score += 1  # Augmenter le score
                    print(f"Score: {score}")

                    # Ajouter une nouvelle cible après chaque destruction
                    ajouter_cible()

        # Afficher les éléments à l'écran
        lasers.draw(screen)
        cibles.draw(screen)

        # Afficher le score
        score_text = font.render(f"Score: {score}", True, BLANC)
        screen.blit(score_text, (10, 10))

        # Actualiser l'écran
        pygame.display.flip()

        # Limiter les FPS
        clock.tick(60)

    # Fermer pygame après la fin du jeu
    pygame.quit()

# Lancer le jeu
if __name__ == "__main__":
    jouer()