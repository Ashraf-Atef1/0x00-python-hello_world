#!/usr/bin/python3
"""
This module contain a function that returns True
if the object is an instance a_class
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance a_class
    """
    if obj.__class__ == a_class:
        return False
    return issubclass(obj.__class__, a_class)
