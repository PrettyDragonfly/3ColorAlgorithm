import numpy as np
from random import *

# number of vertices
n = 3


def initialise_arrays(unary, constraints):
    # unary[1][0] = True
    # unary[1][2] = True
    # constraints[1][2][2][0] = True
    # constraints[1][3][0][2] = True
    # constraints[1][3][1][1] = True
    # constraints[1][5][2][0] = True
    # constraints[1][5][1][2] = True
    # constraints[1][5][2][1] = True
    # constraints[3][4][1][1] = True
    # constraints[3][5][2][0] = True
    constraints[0][1][0][0] = True
    constraints[0][1][1][1] = True
    constraints[0][1][2][2] = True
    constraints[1][2][0][0] = True
    constraints[1][2][1][1] = True
    constraints[1][2][2][2] = True
    unary[0][0] = True
    unary[0][1] = True



if __name__ == '__main__':
    unary = np.full((n, 3), False)
    constraints = np.full((n, n, 3, 3), False)

    # Initialise C
    initialise_arrays(unary, constraints)

    nbBin = np.count_nonzero(constraints == True)
    print("Binaires :", nbBin)

    nbUn = np.count_nonzero(unary == True)
    print("Unaires :", nbUn)

    variable_counter = n

    while (variable_counter > 0):
        if nbUn >= 3:
            for x in range(n):
                # case 1
                if unary[x][0] == True and unary[x][1] == True and unary[x][2] == True:
                    print("Il n'y a pas de solution. Good bye!")
                    exit(0)
        for x in range(n):
            print("x : ", x)
            # case 2
            # print("case 2")
            if unary[x][0] == True and unary[x][1] == True:
                # x is Color 2
                print("x is color Blue")
                for y in range(n):
                    for c in range(3):
                        # delete all the constraints useless
                        constraints[x][y][0][c] = False
                        print("Delete constraints[",x,"][",y,"][0][",c,"]")
                        constraints[x][y][1][c] = False
                        print("Delete constraints[", x, "][", y, "][1][", c, "]")
                        if constraints[x][y][2][c] == True:
                            unary[y][c] = True
                            constraints[x][y][2][c] = False
                            print("Delete constraints[", x, "][", y, "][2][", c, "]")
                unary[x][0] = False
                unary[x][1] = False
                nbUn = np.count_nonzero(unary == True)
                nbBin = np.count_nonzero(constraints == True)
                print("Binaires :", nbBin)
                print("Unaire :", nbUn)
                break
            elif unary[x][0] == True and unary[x][2] == True:
                # x is Color 1
                print("x is color Green")
                for y in range(n):
                    for c in range(3):
                        # delete all the constraints useless
                        constraints[x][y][0][c] = False
                        constraints[x][y][2][c] = False
                        if constraints[x][y][1][c] == True:
                            unary[y][c] = True
                            constraints[x][y][1][c] = False
                unary[x][0] = False
                unary[x][2] = False
                nbUn = np.count_nonzero(unary == True)
                nbBin = np.count_nonzero(constraints == True)
                print("Binaires :", nbBin)
                print("Unaire :", nbUn)
                break
            elif unary[x][1] == True and unary[x][2] == True:
                # x is color 0
                print("x is color Red")
                for y in range(n):
                    for c in range(3):
                        # delete all the constraints useless
                        constraints[x][y][1][c] = False
                        constraints[x][y][2][c] = False
                        if constraints[x][y][0][c] == True:
                            unary[y][c] = True
                            nbUn += 1
                            constraints[x][y][0][c] = False
                unary[x][1] = False
                unary[x][2] = False
                nbUn = np.count_nonzero(unary == True)
                nbBin = np.count_nonzero(constraints == True)
                print("Binaires :", nbBin)
                print("Unaire :", nbUn)
                break

            # case 3
            if unary[x][0]:
                print("here")
                for y in range(n):
                    print("y :", y)
                    for c in range(3):
                        print("c :", c)
                        if constraints[x][y][0][c] == True:
                            print("True")
                            constraints[x][y][0][c] = False
                        for z in range(n):
                            for c2 in range(3):
                                if (constraints[x][y][1][c] == True and constraints[x][z][2][c2] == True) \
                                        or (constraints[x][y][2][c] == True and constraints[x][z][1][c2] == True):
                                    constraints[y][z][c][c2] = True
                # Delete the variable
                variable_counter -= 1
                nbBin = np.count_nonzero(constraints == True)
                print("Binaires :", nbBin)
                break
            elif unary[x][1]:
                for y in range(n):
                    for c in range(3):
                        if constraints[x][y][1][c] == True:
                            constraints[x][y][1][c] = False
                        for z in range(n):
                            for c2 in range(3):
                                if (constraints[x][y][0][c] == True and constraints[x][z][2][c2] == True) \
                                        or (constraints[x][y][2][c] == True and constraints[x][z][0][c2] == True):
                                    constraints[y][z][c][c2] = True
                # Delete the variable
                variable_counter -= 1
                nbBin = np.count_nonzero(constraints == True)
                print("Binaires :", nbBin)
                break
            elif unary[x][2]:
                for y in range(n):
                    print("y :", y)
                    for c in range(3):
                        print("c :", c)
                        if constraints[x][y][2][c] == True:
                            constraints[x][y][2][c] = False
                        for z in range(n):
                            print("z :", z)
                            if y != z:
                                for c2 in range(3):
                                    print("c2 :", c2)
                                    if (constraints[x][y][0][c] == True and constraints[x][z][1][c2] == True) \
                                        or (constraints[x][y][1][c] == True and constraints[x][z][0][c2] == True):
                                        constraints[y][z][c][c2] = True
                # Delete the variable
                variable_counter -= 1
                nbBin = np.count_nonzero(constraints == True)
                print("Binaires :", nbBin)
                break

        # case 4
        if nbUn == 0:
            print("case 4")
            # There are only binaries constraints
            for x in range(n):
                for y in range(n):
                    random = randint(0,3)
                    if constraints[x][y][0][0] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][0][1] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][0][2] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][1][0] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][1][1] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][1][2] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][2][0] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][2][1] == True:
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
                        nbUn += 2
                        break
                    elif constraints[x][y][2][2] == True:
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
                        nbUn += 2
                        break
print("Coloriable.")