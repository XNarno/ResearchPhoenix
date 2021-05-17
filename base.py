import random, pygame, config

def initialisationJeu():
    for i in range(0, config.nombreDeNuage):
        config.vitesseNuageX.append(2)
        config.positionNuageX.append(-69)
        config.positionNuageY.append(random.randint(config.dim_win[1]/12, config.dim_win[1]/12*5))

    for i in range(len(config.vitesseNuageX)):
        config.vitesseNuageX[i] = random.uniform(1, 4)

    config.fenetre.fill(config.BLEUCLAIR)
    pygame.draw.rect(config.fenetre, config.BRUN_FONCE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/10), 0)
    pygame.draw.rect(config.fenetre, config.VERT_HERBE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/30), 0)
    config.fenetre.blit(config.stickmanImg, (config.positionStickmanX, config.positionStickmanY))

    for i in range(0,config.nombreDeCoeurs):
        config.coeursAfficher.append(config.coeurImg)
        config.fenetre.blit(config.coeursAfficher[i], (config.dim_win[0]-(config.dim_win[0]/12-i*40), 0+config.dim_win[1]/12))

def actualisation(): #Fonction actualisant le personnage et sa position (peut être opti par la suite)
    config.fenetre.fill(config.BLEUCLAIR)
    pygame.draw.rect(config.fenetre, config.BRUN_FONCE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/10), 0)
    pygame.draw.rect(config.fenetre, config.VERT_HERBE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/30), 0)
    config.fenetre.blit(config.stickmanImg, (config.positionStickmanX, config.positionStickmanY))
    for i in range(len(config.positionNuageX)):
        config.fenetre.blit(config.nuageImg, (config.positionNuageX[i], config.positionNuageY[i]))
    for i in range(len(config.coeursAfficher)):
        config.fenetre.blit(config.coeursAfficher[i], (config.dim_win[0]-(config.dim_win[0]/20+i*40), 0+config.dim_win[1]/20))

def saut():
    F =(1/2)*config.masse*(config.velocite**2)*config.hauteurDeSaut

    config.positionStickmanY -= F
    config.velocite = config.velocite-1

    if config.velocite<0:
        config.masse -= 0.851111112
    
    if config.velocite == -5:
        config.enSaut = False
        config.velocite = 5
        config.masse = 1

def mouvementNuage():
    global positionNuageX, positionNuageY
    for i in range(len(config.positionNuageX)):
        if config.positionNuageX[i] >= config.dim_win[0]:
            config.positionNuageX[i] = -69
            config.positionNuageY[i] = random.randint(config.dim_win[1]/12, config.dim_win[1]/12*5)
        else:
            config.positionNuageX[i] += config.vitesseNuageX[i]

if __name__ == "__main__":
    print("\nCeci est un module, veuillez ne pas l'utiliser seul\n")