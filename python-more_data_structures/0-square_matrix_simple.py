#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nexo = list(map(lambda i: list(map(lambda x: x * x, i)), matrix))
    return(nexo)
