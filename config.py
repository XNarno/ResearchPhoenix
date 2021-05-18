import pygame

if __name__ == "__main__":
    print("\nCeci est un module, veuillez ne pas l'utiliser seul\n")

# Constantes
HD = (1280, 720)
FULLHD = (1920, 1080)
QHD = (2560, 1440)
FOUR_K = (3840, 2160)
EIGHT_K = (7680, 4320)

LOW_FPS = 30
FULL_FPS = 60

NOIR = (0, 0, 0)
BRUN_FONCE = (101, 51, 30)
VERT_HERBE = (39, 187, 34)
BLANC = (255, 255, 255)
BLEUCLAIR = (127, 191, 255)

HAUTEUR_DE_SAUT_MAX = 3
HAUTEUR_DE_SAUT_MIN = 1

# Paramètres
dim_win = HD  # dimension de la fenetre en pixels

fenetre = pygame.display.set_mode(dim_win)

images_par_seconde = FULL_FPS #Nombre rafraichissement de la fenetre par seconde

niveauEau = dim_win[1]-dim_win[0]/10 #Niveau Y du jeu

positionStickmanX, positionStickmanY = (dim_win[0]/2, niveauEau-100) #Position du personnage

velocite = 5
masse = 1
enSaut = False

vitesseNuageX = [] #Liste de vitesse de chaque nuages
positionNuageX = [] #Liste de position de tous les nuages en X
positionNuageY = [] #Liste de position de tous les nuages en Y
nombreDeNuage = 25
directionVent = -1 #Soit -1 soit 1 pour gauche ou droite
vitesseDuVent = 1 #Influe sur les nuages

hauteurDeSaut = 1 #Hauteur de saut du personnage

vitesseStickman = 10 #Vitesse de pixel parcouru tout les images_par_seconde/20

coeursAfficher = [] #Liste des coeurs à afficher
nombreDeCoeurs = 5 #Nombre de coeurs à l'ecran

stickRunAnim = [] #Liste de l'animation du perso à droite
stickRunAnimLeft = [] #Liste de l'animation du perso à gauche

compteurDePas = 0 #Compteur de pas
gaucheOuDroite = 0 #Direction du personnage

iconImg = pygame.image.load('images/phoenix.jpg') #Image de l'icone
iconImg = pygame.transform.scale(iconImg, (32, 32)) #Remise de l'image en 32x32 pixel
stickmanImg = pygame.image.load('images/stickStable.png') #Image du perso
stickmanImg = pygame.transform.scale(stickmanImg, (82, 105)) #Remise de l'image en 30 par 60 pixel
nuageImg = pygame.image.load('images/whitecloud.png')
nuageImg = pygame.transform.scale(nuageImg, (69, 44)) 
coeurImg = pygame.image.load('images/heart.png')
coeurImg = pygame.transform.scale(coeurImg, (32, 32))
coeurVideImg = pygame.image.load('images/voidHeart.png')
coeurVideImg = pygame.transform.scale(coeurVideImg, (32, 32))
for i in range(0,9): #Permet d'attribuer à la liste d'animation les images
    stickRunAnim.append(pygame.image.load('images/animations/stick%d.png' % i))
    stickRunAnim[i] = pygame.transform.scale(stickRunAnim[i], (82, 100))
    stickRunAnimLeft.append(pygame.transform.flip(stickRunAnim[i], True, False))
