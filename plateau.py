import math
import pygame
import sys
import random
import time 
import config, base, gen, home

# Initialisation

pygame.init()

pygame.display.set_icon(config.iconImg)
pygame.display.set_caption("ResearchPhoenix")

random.seed(time.time())

horloge = pygame.time.Clock()

pygame.key.set_repeat(20)

while base.verifFin() == 0:
    home.dessinsHome()
    for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < (config.dim_win[0]/3)*2 and pos[0] > config.dim_win[0]/3:
                    if pos[1] < config.dim_win[1]/2 + config.dim_win[1]/24 and pos[1] > config.dim_win[1]/2 - config.dim_win[1]/24:
                        home.menuActive = False
    base.actuObligatoire()
    while home.menuActive == False and base.verifFin() == 0:
        if config.jeuInitialise == False:
            base.initialisationJeu()
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
                if config.numeroDeSalle > -1:
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
        #gen.generationAll()
        base.actuObligatoire()