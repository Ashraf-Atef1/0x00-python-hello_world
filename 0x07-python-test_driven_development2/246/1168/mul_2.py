#!/usr/bin/python3
""" Doc """

def mul(a, b):
    """ Doc """
    if (type(a) is list) and (type(b) is int):
        return "FAIL"
    else:
        return a * b
