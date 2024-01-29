#!/usr/bin/python3
""" Doc """

def mul(a, b):
    """ Doc """
    if ((type(a) is str) and (type(b) is int)) or ((type(a) is int) and (type(b) is str)):
        return "FAIL"
    else:
        return a * b
