#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    matrix3 = []
    for i in matrix:
        linea = []
        for j in i:
            linea.append(j)
        matrix2.append(linea)
    for i in matrix2:
        linea2 = []
        for j in i:
            linea2.append(j ** 2)
        matrix3.append(linea2)
    print(matrix3)
