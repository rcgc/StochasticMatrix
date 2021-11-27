import numpy as np
import random
import decimal


def generate_stochastic_matrix(dimension):
    matrix = []
    for i in range(dimension):
        res = 100000000
        row = []
        for j in range(dimension):
            value = float(decimal.Decimal(random.randrange(0, res)))
            if j == dimension-1:
                row.append(res/100000000)
            else:
                row.append(value/100000000)
                res = res - value
        matrix.append(row)

    matrix = np.array(matrix)

    return matrix


def check_if_stochastic(matrix, dimension):
    # Checking if given matrix is stochastic
    for i in range(dimension):
        vector_sums = matrix.sum(axis=1)
        res = np.all(vector_sums == 1.0)
    return res


def power_matrix(matrix, exponent):
    return np.linalg.matrix_power(matrix, exponent)


def check_if_steady_state(matrix, dimension):
    m1 = np.linalg.matrix_power(matrix, 100)
    m2 = np.linalg.matrix_power(matrix, 101)

    m1 = np.array(m1)
    m2 = np.array(m2)

    m1 = np.around(m1, 8)
    m2 = np.around(m2, 8)

    # Happens when zeroes change from place every iteration
    if m1.all() != m2.all():
        return False, m2

    return True, m2


def print_menu():
    print("Choose an option: ")
    print("1) Enter matrix by hand")
    print("2) Generate default matrix")
    print("6) Exit")


def print_submenu():
    print("Choose an option")
    print("3) Calculate probability from going to one state to another in n steps")
    print("4) Calculate long-term(steady) state of the matrix")
    print("5) Identify is matrix regular or not")
    print("6) Exit")
