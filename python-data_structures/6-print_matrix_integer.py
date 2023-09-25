#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for i in range(len(a)):
            if i == len(a) - 1:
                print("{:d}".format(a[i]))
            else:
                print("{:d} ".format(a[i]), end='')
