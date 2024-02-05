#!/usr/bin/python3
"""
This module contain a function that returns True if the object
is exactly an instance of the specified class ; otherwise False
"""
float()

def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly 
    an instance of the specified class ; otherwise False"""
    return obj.__class__ == a_class
