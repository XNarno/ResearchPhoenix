import math
import pygame
import sys
import os
import pyautogui

# Constantes
HD = (1280, 720)
FULLHD = (1920, 1080)
QHD = (2560, 1440)
FOUR_K = (3840, 2160)
EIGHT_K = (7680, 4320)

LOW_FPS = 30
FULL_FPS = 60

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
BLEUCLAIR = (127, 191, 255)

# Paramètres

dimensions_fenetre = HD  # en pixels
images_par_seconde = LOW_FPS

# Fonctions

def actualisation():
    fenetre.fill(BLEUCLAIR)
    pygame.draw.circle(fenetre, NOIR, pygame.mouse.get_pos(), 30, 0)

# Initialisation

pygame.init()

fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("ResearchPhoenix")

horloge = pygame.time.Clock()

# Dessin

fenetre.fill(BLEUCLAIR)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    actualisation()
    pygame.display.flip()
    horloge.tick(images_par_seconde)