# Stochastic Matrix
# Quantitative Methods course final project
# Author: Roberto Carlos Guzmán Cortés

import numpy as np
from stochastic_functions import *

print_menu()
op = input()
op = int(op)

matrix = []

# Manually introduced matrix
if op == 1:
    print("Introduce square matrix dimension")
    n = input()
    n = int(n)

    for i in range(n):
        row = []
        for j in range(n):
            print('a(', i, ',', j, ')')
            a = input()
            a = float(a)
            row.append(a)
        matrix.append(row)
    matrix = np.array(matrix)
    print("\nOriginal matrix")
    print(matrix)
    print("\n")

    if check_if_stochastic(matrix, n):
        while op != 6:
            print_submenu()
            op = input()
            op = int(op)
            if op == 3:
                # (70) probability of going from state to another in n steps
                row = input("Row: ")
                row = int(row)

                column = input("Column: ")
                column = int(column)

                if column <= row < n:
                    exponent = input("Number of steps: ")
                    exponent = int(exponent)

                    aux_matrix = power_matrix(matrix, exponent)
                    print("\nResultant matrix")
                    print(aux_matrix)
                    print("\nmatrix[", row, ",", column, "]", "=", np.round(aux_matrix[row, column], 8))
                else:
                    print("Row/Column out of matrix range (0-", n, ")\n")
            elif op == 4:
                has_steady, aux_matrix = check_if_steady_state(matrix, n)
                # (85) calculate if there's steady state or not
                if has_steady:
                    print("\nYes, it has a steady state: ")
                    print(aux_matrix)
                    print("Steady state: ", aux_matrix[0, ])
                    print("\n")
                else:
                    print("\nNo, it does not have a steady state: ")
                    print(aux_matrix)
                    print("\n")
            elif op == 5:
                # (95) check if regular or not
                isRegular, aux_matrix = check_if_steady_state(matrix, n)
                if isRegular:
                    print("\nYes, it is regular")
                    print(aux_matrix)
                    print("\n")
                else:
                    print("\nNo, it is not regular")
                    print(aux_matrix)
                    print("\n")
            elif op == 6:
                print("Exit selected")
                print("Program ended\n")
                break
            else:
                print("Option not found\n")
    else:
        print("Matrix no stochastic\n")
# 3X3 generated matrix
elif op == 2:
    # (100) Generate 3x3 stochastic matrix (randomly) and let user use steps 3, 4 & 5
    n = 3
    matrix = generate_stochastic_matrix(n)
    print("\n")
    print(matrix)
    print("\n")
    if check_if_stochastic(matrix, n):
        while op != 6:
            print_submenu()
            op = input()
            op = int(op)
            if op == 3:
                # (70) probability of going from state to another in n steps
                row = input("Row: ")
                row = int(row)

                column = input("Column: ")
                column = int(column)

                if column <= row < 3:
                    exponent = input("Number of steps: ")
                    exponent = int(exponent)

                    aux_matrix = power_matrix(matrix, exponent)
                    print("\nResultant matrix")
                    print(aux_matrix)
                    print("\nmatrix[", row, ",", column, "]", "=", np.round(aux_matrix[row, column], 8))
                else:
                    print("Row/Column out of matrix range (0-", n, ")\n")
            elif op == 4:
                has_steady, aux_matrix = check_if_steady_state(matrix, n)
                # (85) calculate if there's steady state or not
                if has_steady:
                    print("\nYes, it has a steady state: ")
                    print(aux_matrix)
                    print("Steady state: ", aux_matrix[0, ])
                    print("\n")
                else:
                    print("\nNo, it does not have a steady state: ")
                    print(aux_matrix)
                    print("\n")
            elif op == 5:
                # (95) check if regular or not
                isRegular, aux_matrix = check_if_steady_state(matrix, n)
                if isRegular:
                    print("\nYes, it is regular")
                    print(aux_matrix)
                    print("\n")
                else:
                    print("\nNo, it is not regular")
                    print(aux_matrix)
                    print("\n")
            elif op == 6:
                print("Exit selected")
                print("Program ended\n")
                break
            else:
                print("Option not found\n")
    else:
        print("Matrix no stochastic\n")
elif op == 6:
    print("Exit selected")
    print("Program ended\n")
else:
    print("No option found")
    print("Program ended\n")
