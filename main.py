import numpy as np

# number of vertices
n = 10

def initialiseArrays(unaire, contrainte):
    unaire[1][0] = True
    unaire[1][2] = True
    unaire[1][1] = True
    contrainte[1][2][2][0] = True
    contrainte[1][3][0][2] = True
    contrainte[1][3][1][1] = True
    contrainte[1][5][2][0] = True
    contrainte[1][5][1][2] = True
    contrainte[1][5][2][1] = True
    contrainte[3][4][1][1] = True
    contrainte[3][5][2][0] = True

if __name__ == '__main__':
    unaire = np.full((n, 3), False)
    contrainte = np.full((n, n, 3, 3), False)

    # Initialise C
    initialiseArrays(unaire, contrainte)

    nbBin = np.count_nonzero(contrainte == True)
    print(nbBin)

    nbUn = np.count_nonzero(unaire == True)
    print(nbUn)

    while (nbUn > 0) or (nbBin > 0):
        if nbUn >= 3:
            for i in range (n):
                if unaire[i][0] == True and unaire[i][1] == True and unaire[i][2] == True:
                    print("Il n'y a pas de solution. Good bye!")
                    exit(0)
                else:
                    print("Pour l'instant c'est ok!")
        else:
            print("Pour l'instant c'est ok!")