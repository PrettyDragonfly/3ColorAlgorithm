import numpy as np

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
            for i in range(n):
                # case 1
                if unary[i][0] is True and unary[i][1] is True and unary[i][2] is True:
                    print("Il n'y a pas de solution. Good bye!")
                    exit(0)
        for i in range(n):
            # case 2
            if unary[i][0] is True and unary[i][1] is True:
                # i is Color 2
                for j in range(n):
                    for k in range(2):
                        # delete all the constraints useless
                        constraints[i][j][0][k] = False
                        constraints[i][j][1][k] = False
                        if constraints[i][j][2][k] is True:
                            unary[j][k] = True
                            constraints[i][j][2][k] = False
                nbBin = np.count_nonzero(constraints is True)
                break
            elif unary[i][0] is True and unary[i][2] is True:
                # i is Color 1
                for j in range(n):
                    for k in range(2):
                        # delete all the constraints useless
                        constraints[i][j][0][k] = False
                        constraints[i][j][2][k] = False
                        if constraints[i][j][1][k] is True:
                            unary[j][k] = True
                            constraints[i][j][1][k] = False
                nbBin = np.count_nonzero(constraints is True)
                break
            elif unary[i][1] is True and unary[i][2] is True:
                # i is color 0
                for j in range(n):
                    for k in range(2):
                        # delete all the constraints useless
                        constraints[i][j][1][k] = False
                        constraints[i][j][2][k] = False
                        if constraints[i][j][0][k] is True:
                            unary[j][k] = True
                            constraints[i][j][0][k] = False
                nbBin = np.count_nonzero(constraints is True)
                break
        # case 3
        for i in range(n):
            if unary[i][0]:
                for j in range(n):
                    for k in range(2):
                        constraints[i][j][0][k] = False

            elif unary[i][1]:
                for j in range(n):
                    for k in range(2):
                        constraints[i][j][1][k] = False
            elif unary[i][2]:
                for j in range(n):
                    for k in range(2):
                        constraints[i][j][2][k] = False
        nbBin = np.count_nonzero(constraints is True)
        exit(0)
