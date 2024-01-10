#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [*map(lambda row: [*map(lambda e: e ** 2, row)], matrix)]
