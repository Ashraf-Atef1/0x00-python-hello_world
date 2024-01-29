#!/usr/bin/python3
""" Doc """

def print_square(size):
    """ Doc """
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
