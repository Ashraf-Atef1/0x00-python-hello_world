#!/usr/bin/python3
"""
This module contain a MyList class that inhert from list class
"""


class MyList(list):
    """
    A list with a custom method
    """
    def print_sorted(self):
        """
            prints a sorted list
        """
        print(sorted(self))
