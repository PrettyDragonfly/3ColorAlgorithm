import numpy as np


def readFile():
    num_lines = sum(1 for line in open('graphenc.txt','r'))
    print(num_lines)
    f = open('graphenc.txt','r')

    unary = np.full((num_lines, 3), False)
    constraints = np.full((num_lines, num_lines, 3, 3), False)

    column_counter = 0
    row_counteur = 0
    while 1:

        # read by character
        char = f.read(1)
        if not char:
            break

        elif char != '\n':
            if char == '1':
                constraints[row_counteur][column_counter][0][0] = True
                print("Add constraints[",row_counteur,"][",column_counter,"][0][0]")
                constraints[row_counteur][column_counter][1][1] = True
                print("Add constraints[", row_counteur, "][", column_counter, "][1][1]")
                constraints[row_counteur][column_counter][2][2] = True
                print("Add constraints[", row_counteur, "][", column_counter, "][2][2]")
            if column_counter == (num_lines-1):
                if row_counteur < num_lines-1:
                    row_counteur += 1
                column_counter = 0
            else:
                column_counter += 1

        # print(char)

    f.close()
    return unary, constraints, num_lines