#!/usr/bin/python3
""" Doc """

def mul(a, b):
    """ Doc """
    if type(b) is float and type(a) is not float:
        return "FAIL"
    else:
        return a * b
