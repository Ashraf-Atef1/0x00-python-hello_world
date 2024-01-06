#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for array in matrix:
        while i < len(array):
            if i == len(array) - 1:
                print("{:d}".format(array[i]))
            else:
                print("{:d}".format(array[i]), end=" ")
            i += 1
        i = 0
