import math
import pygame
import sys
import random
import time 
import config
import base

from pygame import image
from pygame import key

# Initialisation

pygame.init()

pygame.display.set_icon(config.iconImg)
pygame.display.set_caption("ResearchPhoenix")

random.seed(time.time())

horloge = pygame.time.Clock()

base.initialisationJeu()

pygame.key.set_repeat(20)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if config.positionStickmanX >= config.dim_win[0]:
                config.positionStickmanX = -30
            else:
                config.positionStickmanX += config.vitesseStickman
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if config.positionStickmanX <= -30:
                config.positionStickmanX = config.dim_win[0]
            else:
                config.positionStickmanX -= config.vitesseStickman
        if pygame.key.get_pressed()[pygame.K_UP]:
            if config.hauteurDeSaut < config.HAUTEUR_DE_SAUT_MAX:
                config.hauteurDeSaut += 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if config.hauteurDeSaut > config.HAUTEUR_DE_SAUT_MIN:
                config.hauteurDeSaut -= 1
        if config.enSaut == False:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                config.enSaut = True
    if config.enSaut:
        base.saut()
    base.mouvementNuage()
    base.actualisation()
    pygame.display.flip()
    horloge.tick(config.images_par_seconde)