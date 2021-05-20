import pygame, random, time, config, base

if __name__ == "__main__":
    print("\nCeci est un module, veuillez ne pas l'utiliser seul\n")

numeroDeSalle = 0
ancienNumeroDeSalle = numeroDeSalle

#Position de la planche en X et Y, Longueur et hauteur de la planche
posPlateX, posPlateY, longPlate, hautPLate = ([50], [100], config.dim_win[0]/10, config.dim_win[1]/240) #Juste planche

def dessinsGenere():
    pygame.draw.rect(config.fenetre, config.BRUN_FONCE, (posPlateX[numeroDeSalle], posPlateY[numeroDeSalle], longPlate, hautPLate), 0) #Dessine la planche au bon endroit par salle

def generateurDePiece(): #Permet de générer aléatoirement une planche dans chaque salle et de conserver sa position par salle
    global posPlateX, posPlateY
    if len(posPlateX) < numeroDeSalle+1:
        posPlateX.append(random.randint(200, 600))
        posPlateY.append(random.randint(200, 600))
        print("\n")
        print(posPlateX)
        print(posPlateY)

    print("Ancien num de salle: %d \nNum de salle: %d\n" % (ancienNumeroDeSalle, numeroDeSalle))
    