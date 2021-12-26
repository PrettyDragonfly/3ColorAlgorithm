import numpy as np
from random import *

# number of vertices
n = 10


def initialise_arrays(unary, constraints):
    unary[1][0] = True
    unary[1][2] = True
    constraints[1][2][2][0] = True
    constraints[1][3][0][2] = True
    constraints[1][3][1][1] = True
    constraints[1][5][2][0] = True
    constraints[1][5][1][2] = True
    constraints[1][5][2][1] = True
    constraints[3][4][1][1] = True
    constraints[3][5][2][0] = True


if __name__ == '__main__':
    unary = np.full((n, 3), False)
    constraints = np.full((n, n, 3, 3), False)

    # Initialise C
    initialise_arrays(unary, constraints)

    nbBin = np.count_nonzero(constraints == True)
    print(nbBin)

    nbUn = np.count_nonzero(unary == True)
    print(nbUn)

    while (nbUn > 0) or (nbBin > 0):
        if nbUn >= 3:
            for x in range(n):
                # case 1
                if unary[x][0] is True and unary[x][1] is True and unary[x][2] is True:
                    print("Il n'y a pas de solution. Good bye!")
                    exit(0)
        for x in range(n):
            # case 2
            if unary[x][0] is True and unary[x][1] is True:
                # x is Color 2
                for y in range(n):
                    for c in range(2):
                        # delete all the constraints useless
                        constraints[x][y][0][c] = False
                        constraints[x][y][1][c] = False
                        if constraints[x][y][2][c] is True:
                            unary[y][c] = True
                            constraints[x][y][2][c] = False
                nbBin = np.count_nonzero(constraints is True)
                break
            elif unary[x][0] is True and unary[x][2] is True:
                # x is Color 1
                for y in range(n):
                    for c in range(2):
                        # delete all the constraints useless
                        constraints[x][y][0][c] = False
                        constraints[x][y][2][c] = False
                        if constraints[x][y][1][c] is True:
                            unary[y][c] = True
                            constraints[x][y][1][c] = False
                nbBin = np.count_nonzero(constraints is True)
                break
            elif unary[x][1] is True and unary[x][2] is True:
                # x is color 0
                for y in range(n):
                    for c in range(2):
                        # delete all the constraints useless
                        constraints[x][y][1][c] = False
                        constraints[x][y][2][c] = False
                        if constraints[x][y][0][c] is True:
                            unary[y][c] = True
                            constraints[x][y][0][c] = False
                nbBin = np.count_nonzero(constraints is True)
                break
        # case 3
        for x in range(n):
            if unary[x][0]:
                for y in range(n):
                    for c in range(2):
                        if constraints[x][y][0][c] is True:
                            constraints[x][y][0][c] = False
                        for z in range(n):
                            for c2 in range(2):
                                if (constraints[x][y][1][c] is True and constraints[x][z][2][c2] is True) \
                                        or (constraints[x][y][2][c] is True and constraints[x][z][1][c2] is True):
                                    constraints[y][z][c][c2] = True
                break
            elif unary[x][1]:
                for y in range(n):
                    for c in range(2):
                        if constraints[x][y][1][c] is True:
                            constraints[x][y][1][c] = False
                        for z in range(n):
                            for c2 in range(2):
                                if (constraints[x][y][0][c] is True and constraints[x][z][2][c2] is True) \
                                        or (constraints[x][y][2][c] is True and constraints[x][z][0][c2] is True):
                                    constraints[y][z][c][c2] = True
                break
            elif unary[x][2]:
                for y in range(n):
                    for c in range(2):
                        if constraints[x][y][2][c] is True:
                            constraints[x][y][2][c] = False
                        for z in range(n):
                            for c2 in range(2):
                                if (constraints[x][y][0][c] is True and constraints[x][z][1][c2] is True) \
                                        or (constraints[x][y][1][c] is True and constraints[x][z][0][c2] is True):
                                    constraints[y][z][c][c2] = True
                break
        # case 4
        if nbUn == 0:
            # There are only binaries constraints
            for x in range(n):
                for y in range(n):
                    # tirer un nombre au hasard
                    random = randint(0,3)
                    if constraints[x][y][0][0] is True:
                        if random == 0:
                            unary[x][0] = True
                            unary[y][1] = True
                        elif random == 1:
                            unary[x][0] = True
                            unary[y][2] = True
                        elif random == 2:
                            unary[x][1] = True
                            unary[y][0] = True
                        elif random == 3:
                            unary[x][2] = True
                            unary[y][0] = True
                        break
                    elif constraints[x][y][0][1] is True:
                        if random == 0:
                            unary[x][0] = True
                            unary[y][0] = True
                        elif random == 1:
                            unary[x][0] = True
                            unary[y][2] = True
                        elif random == 2:
                            unary[x][1] = True
                            unary[y][1] = True
                        elif random == 3:
                            unary[x][2] = True
                            unary[y][1] = True
                        break
                    elif constraints[x][y][0][2] is True:
                        if random == 0:
                            unary[x][0] = True
                            unary[y][0] = True
                        elif random == 1:
                            unary[x][0] = True
                            unary[y][1] = True
                        elif random == 2:
                            unary[x][1] = True
                            unary[y][2] = True
                        elif random == 3:
                            unary[x][2] = True
                            unary[y][2] = True
                        break
                    elif constraints[x][y][1][0] is True:
                        if random == 0:
                            unary[x][1] = True
                            unary[y][1] = True
                        elif random == 1:
                            unary[x][1] = True
                            unary[y][2] = True
                        elif random == 2:
                            unary[x][0] = True
                            unary[y][0] = True
                        elif random == 3:
                            unary[x][2] = True
                            unary[y][0] = True
                        break
                    elif constraints[x][y][1][1] is True:
                        if random == 0:
                            unary[x][1] = True
                            unary[y][0] = True
                        elif random == 1:
                            unary[x][1] = True
                            unary[y][2] = True
                        elif random == 2:
                            unary[x][0] = True
                            unary[y][1] = True
                        elif random == 3:
                            unary[x][2] = True
                            unary[y][1] = True
                        break
                    elif constraints[x][y][1][2] is True:
                        if random == 0:
                            unary[x][1] = True
                            unary[y][0] = True
                        elif random == 1:
                            unary[x][1] = True
                            unary[y][1] = True
                        elif random == 2:
                            unary[x][0] = True
                            unary[y][2] = True
                        elif random == 3:
                            unary[x][2] = True
                            unary[y][2] = True
                        break
                    elif constraints[x][y][2][0] is True:
                        if random == 0:
                            unary[x][2] = True
                            unary[y][1] = True
                        elif random == 1:
                            unary[x][2] = True
                            unary[y][1] = True
                        elif random == 2:
                            unary[x][0] = True
                            unary[y][0] = True
                        elif random == 3:
                            unary[x][1] = True
                            unary[y][0] = True
                        break
                    elif constraints[x][y][2][1] is True:
                        if random == 0:
                            unary[x][2] = True
                            unary[y][0] = True
                        elif random == 1:
                            unary[x][2] = True
                            unary[y][2] = True
                        elif random == 2:
                            unary[x][0] = True
                            unary[y][1] = True
                        elif random == 3:
                            unary[x][1] = True
                            unary[y][1] = True
                        break
                    elif constraints[x][y][2][2] is True:
                        if random == 0:
                            unary[x][2] = True
                            unary[y][0] = True
                        elif random == 1:
                            unary[x][2] = True
                            unary[y][1] = True
                        elif random == 2:
                            unary[x][0] = True
                            unary[y][2] = True
                        elif random == 3:
                            unary[x][1] = True
                            unary[y][2] = True
                        break
        nbBin = np.count_nonzero(constraints is True)
        exit(0)

# ne pas oublier de remettre à jour les compteurs de contraintes