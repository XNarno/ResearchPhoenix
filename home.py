import pygame
import config

menuActive = True

posSerpX, posSerpY = (0, 0)

tailleSerp = 10

def dessinsHome():
    config.fenetre.fill(config.ROUGE)
    pygame.draw.rect(config.fenetre, config.NOIR, (config.dim_win[0]/3, config.dim_win[1]/2-config.dim_win[1]/24, config.dim_win[0] - (config.dim_win[0]/3)*2, config.dim_win[1]/12), 10)
    config.fenetre.blit(config.textMenu, config.text_rect)
    serpserp()

def serpserp():
    global posSerpX, posSerpY
    if posSerpX < config.dim_win[0]-tailleSerp and posSerpY <= 0:
        posSerpX += 10

    elif posSerpY < config.dim_win[1]-tailleSerp and posSerpX >= config.dim_win[0]-tailleSerp:
        posSerpY += 10

    elif posSerpX > 0 and posSerpY >= config.dim_win[1]-tailleSerp:
        posSerpX -= 10

    elif posSerpY > 0 and posSerpX <= 0:
        posSerpY -= 10
    pygame.draw.rect(config.fenetre, config.NOIR, (posSerpX, posSerpY, tailleSerp, tailleSerp), 0)
