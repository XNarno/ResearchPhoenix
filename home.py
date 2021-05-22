import pygame
import config

menuActive = True

def dessinsHome():
    config.fenetre.fill(config.ROUGE)
    pygame.draw.rect(config.fenetre, config.NOIR, (config.dim_win[0]/3, config.dim_win[1]/2-config.dim_win[1]/24, config.dim_win[0] - (config.dim_win[0]/3)*2, config.dim_win[1]/12), 10)
    config.fenetre.blit(config.textMenu, config.text_rect)