#!/usr/bin/python3
""" Doc """

def mul(a, b):
    """ Doc """
    if (type(a) is int or type(b) is float) and (type(b) is int or type(b) is float):
        return "FAIL"
    else:
        return a * b
