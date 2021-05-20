import math
import pygame
import sys
import random
import time
import config
import base
import gen
import phoenix

# Initialisation

pygame.init()

pygame.display.set_icon(config.iconImg)
pygame.display.set_caption("ResearchPhoenix")

random.seed(time.time())

horloge = pygame.time.Clock()

base.initialisationJeu()

pygame.key.set_repeat(20)

while base.verifFin() == 0:
    temps_maintenant = pygame.time.get_ticks()
    for evenement in pygame.event.get():
        config.gaucheOuDroite = 3
        config.vitesseDuVent = 1
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            config.positionStickmanX += config.vitesseStickman #Mettre ici pour avancer le stickman
            #config.vitesseDuVent = 1.8 #Mettre ici pour paralax avec stickman fixe
            config.compteurDePas += 1
            config.gaucheOuDroite = 0

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if gen.numeroDeSalle > -1:
                config.positionStickmanX -= config.vitesseStickman #Mettre ici pour avancer le stickman
            #config.vitesseDuVent = -0.1 #Mettre ici pour paralax avec stickman fixe
            config.compteurDePas += 1
            config.gaucheOuDroite = 1

        if pygame.key.get_pressed()[pygame.K_UP]:
            if config.hauteurDeSaut < config.HAUTEUR_DE_SAUT_MAX:
                config.hauteurDeSaut += 1

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if config.hauteurDeSaut > config.HAUTEUR_DE_SAUT_MIN:
                config.hauteurDeSaut -= 1

        if config.enSaut == False:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                config.enSaut = True

    config.compteurDePas = config.compteurDePas % 9

    if config.enSaut:
        base.saut()
    base.verifMouvementStickman()
    base.mouvementNuage()
    base.dessinsPlateau()
    phoenix.affiche_phoenix(temps_maintenant/120)
    pygame.display.flip()
    horloge.tick(config.images_par_seconde)
