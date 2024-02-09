#!/usr/bin/python3
""" A module contain the base class """


class Base:
    """ The base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initalization"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
