#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        line = " ".join(map(str,l))
        print("{:s}".format(line))
