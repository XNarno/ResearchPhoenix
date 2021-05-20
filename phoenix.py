import pygame
import random
import math
import config

def affiche_phoenix(temps):
    config.posXPhoenix += random.randint(-1, 1)
    config.posYPhoenix += random.randint(-1, 1)
    distanceX = config.positionStickmanX - config.posXPhoenix
    distanceY = config.positionStickmanY - config.posYPhoenix
    if distanceX > 80:
        config.posXPhoenix += distanceX/50
    if distanceX < -40:
        config.posXPhoenix += distanceX/50
    if distanceY > 70:
        config.posYPhoenix += distanceY/50
    if distanceY < -10:
        config.posYPhoenix -= distanceX/50
    if distanceX <= 0:
        i = 0
    if distanceX > 0:
        i = 3
    config.fenetre.blit(config.phoenixAnim[(int(temps) % 3) + i], (config.posXPhoenix, config.posYPhoenix))
