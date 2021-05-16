import math
import pygame
import sys
import random
import time 

from pygame import image
from pygame import key

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

images_par_seconde = FULL_FPS #Nombre rafraichissement de la fenetre par seconde

niveauEau = dim_win[1]-dim_win[0]/10 #Niveau Y du jeu

positionStickmanX, positionStickmanY = (dim_win[0]/2, niveauEau-60) #Position du personnage

v = 5
m = 1
enSaut = False

vitesseNuageX = []
positionNuageX = []
positionNuageY = []
nombreDeNuage = 10

hauteurDeSaut = 1

vitesseStickman = 10 #Vitesse de pixel parcouru tout les images_par_seconde/20

iconImg = pygame.image.load('phoenix.jpg') #Image de l'icone
iconImg = pygame.transform.scale(iconImg, (32, 32)) #Remise de l'image en 32x32 pixel
stickmanImg = pygame.image.load('stickman.png') #Image du perso
stickmanImg = pygame.transform.scale(stickmanImg, (30, 60)) #Remise de l'image en 30 par 60 pixel
nuageImg = pygame.image.load('whitecloud.png')
nuageImg = pygame.transform.scale(nuageImg, (69, 44))

# Fonctions

def actualisation(): #Fonction actualisant le personnage et sa position (peut être opti par la suite)
    fenetre.fill(BLEUCLAIR)
    pygame.draw.rect(fenetre, BRUN_FONCE, (0, dim_win[1]-dim_win[0]/10, dim_win[0], dim_win[0]/10), 0)
    pygame.draw.rect(fenetre, VERT_HERBE, (0, dim_win[1]-dim_win[0]/10, dim_win[0], dim_win[0]/30), 0)
    fenetre.blit(stickmanImg, (positionStickmanX, positionStickmanY))
    for i in range(len(positionNuageX)):
        fenetre.blit(nuageImg, (positionNuageX[i], positionNuageY[i]))

def saut():
    global v, m, enSaut, positionStickmanY, hauteurDeSaut
    F =(1/2)*m*(v**2)*hauteurDeSaut

    positionStickmanY -= F
    v = v-1

    if v<0:
        m -= 0.851111112
    
    if v == -5:
        enSaut = False
        v = 5
        m = 1

def mouvementNuage():
    global positionNuageX, positionNuageY
    for i in range(len(positionNuageX)):
        if positionNuageX[i] >= dim_win[0]:
            positionNuageX[i] = -69
            positionNuageY[i] = random.randint(dim_win[1]/12, dim_win[1]/12*5)
        else:
            positionNuageX[i] += vitesseNuageX[i]
    

# Initialisation

pygame.init()

pygame.display.set_icon(iconImg)
fenetre = pygame.display.set_mode(dim_win)
pygame.display.set_caption("ResearchPhoenix")

random.seed(time.time())

horloge = pygame.time.Clock()

for i in range(0, nombreDeNuage):
    vitesseNuageX.append(2)
    positionNuageX.append(-69)
    positionNuageY.append(random.randint(dim_win[1]/12, dim_win[1]/12*5))

for i in range(len(vitesseNuageX)):
    vitesseNuageX[i] = random.uniform(1, 4)

# Dessin

fenetre.fill(BLEUCLAIR)
pygame.draw.rect(fenetre, BRUN_FONCE, (0, dim_win[1]-dim_win[0]/10, dim_win[0], dim_win[0]/10), 0)
pygame.draw.rect(fenetre, VERT_HERBE, (0, dim_win[1]-dim_win[0]/10, dim_win[0], dim_win[0]/30), 0)
fenetre.blit(stickmanImg, (positionStickmanX, positionStickmanY))

pygame.key.set_repeat(20)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if positionStickmanX >= dim_win[0]:
                positionStickmanX = -30
            else:
                positionStickmanX += vitesseStickman
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if positionStickmanX <= -30:
                positionStickmanX = dim_win[0]
            else:
                positionStickmanX -= vitesseStickman
        if pygame.key.get_pressed()[pygame.K_UP]:
            if hauteurDeSaut < HAUTEUR_DE_SAUT_MAX:
                hauteurDeSaut += 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if hauteurDeSaut > HAUTEUR_DE_SAUT_MIN:
                hauteurDeSaut -= 1
        if enSaut == False:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                enSaut = True
    if enSaut:
        saut()
    mouvementNuage()
    actualisation()
    pygame.display.flip()
    horloge.tick(images_par_seconde)