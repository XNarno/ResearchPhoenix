import random, pygame, config, gen

if __name__ == "__main__":
    print("\nCeci est un module, veuillez ne pas l'utiliser seul\n")

def initialisationJeu(): #Initialise le jeu avec tout ce qu'il faut pour commencer
    for i in range(0, config.nombreDeNuage):
        config.vitesseNuageX.append(2)
        config.positionNuageX.append(random.randint(-69, config.dim_win[0]))
        config.positionNuageY.append(random.randint(config.dim_win[1]/12, config.dim_win[1]/12*5))

    for i in range(len(config.vitesseNuageX)):
        config.vitesseNuageX[i] = random.uniform(1, 4)

    config.fenetre.fill(config.BLEUCLAIR)
    pygame.draw.rect(config.fenetre, config.BRUN_FONCE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/10), 0)
    pygame.draw.rect(config.fenetre, config.VERT_HERBE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/30), 0)
   
    config.fenetre.blit(config.stickRunAnim[config.compteurDePas], (config.positionStickmanX, config.positionStickmanY))

    for i in range(0,config.nombreDeCoeurs):
        config.coeursAfficher.append(config.coeurImg)
        config.fenetre.blit(config.coeursAfficher[i], (config.dim_win[0]-(config.dim_win[0]/12-i*40), 0+config.dim_win[1]/12))

def actualisationPersonnage(): #Fonction actualisant le personnage et sa position (peut être opti par la suite)
    if config.gaucheOuDroite == 0:
        config.fenetre.blit(config.stickRunAnim[config.compteurDePas], (config.positionStickmanX, config.positionStickmanY))
    elif config.gaucheOuDroite == 1:
        config.fenetre.blit(config.stickRunAnimLeft[config.compteurDePas], (config.positionStickmanX, config.positionStickmanY))
    else:    
        config.fenetre.blit(config.stickmanImg, (config.positionStickmanX, config.positionStickmanY)) #stickman debout

def dessinsPlateau(): #Dessine le plateau
    config.fenetre.fill(config.BLEUCLAIR)

    gen.dessinsGenere() #Generation

    actualisationPersonnage()
    
    pygame.draw.rect(config.fenetre, config.BRUN_FONCE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/10), 0)
    pygame.draw.rect(config.fenetre, config.VERT_HERBE, (0, config.dim_win[1]-config.dim_win[0]/10, config.dim_win[0], config.dim_win[0]/30), 0)

    for i in range(len(config.positionNuageX)):
        config.fenetre.blit(config.nuageImg, (config.positionNuageX[i], config.positionNuageY[i]))

    for i in range(len(config.coeursAfficher)):
        config.fenetre.blit(config.coeursAfficher[i], (config.dim_win[0]-(config.dim_win[0]/20+i*40), 0+config.dim_win[1]/20))

def verifMouvementStickman(): #Vérifie si le stickman sort de l'écran par la gauche ou la droite
    if config.positionStickmanX > config.dim_win[0]:
        config.positionStickmanX = -82
        gen.ancienNumeroDeSalle = gen.numeroDeSalle
        gen.numeroDeSalle += 1
        gen.generateurDePiece()
    elif config.positionStickmanX < -82:
        config.positionStickmanX = config.dim_win[0]
        gen.ancienNumeroDeSalle = gen.numeroDeSalle
        gen.numeroDeSalle -= 1
        gen.generateurDePiece()

def saut(): #Fonction calculant les forces, masses et velocite pour sauter
    F =(1/2)*config.masse*(config.velocite**2)*config.hauteurDeSaut

    config.positionStickmanY -= F
    config.velocite -= 1

    if config.velocite<0:
        config.masse -= 0.851111112
    
    if config.velocite == -5:
        config.enSaut = False
        config.velocite = 5
        config.masse = 1

def mouvementNuage(): #Fonction actualisant la position des nuages
    for i in range(len(config.positionNuageX)):
        if config.positionNuageX[i] < -69:
            config.positionNuageX[i] = config.dim_win[0]
            config.positionNuageY[i] = random.randint(config.dim_win[1]/12, config.dim_win[1]/12*5)

        elif config.positionNuageX[i] >= config.dim_win[0]:
            config.positionNuageX[i] = -69
            config.positionNuageY[i] = random.randint(config.dim_win[1]/12, config.dim_win[1]/12*5)

        if config.directionVent == 1:
            config.positionNuageX[i] += config.vitesseNuageX[i]*config.vitesseDuVent

        elif config.directionVent == -1:
            config.positionNuageX[i] -= config.vitesseNuageX[i]*config.vitesseDuVent

def perteDeVie(): #Permet de perdre de la vie et d'afficher les coeurs vides
    config.coeursAfficher[config.nombreDeCoeurs-1] = config.coeurVideImg
    if verifFin() == 0:
        config.nombreDeCoeurs -= 1

def verifFin(): #Permet de verifier si on a encore de la vie
    if config.nombreDeCoeurs > 0:
        return 0
    else:
        print("C'est la fin")
        return -1
        