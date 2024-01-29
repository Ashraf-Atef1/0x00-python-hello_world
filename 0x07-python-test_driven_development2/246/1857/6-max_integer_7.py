#!/usr/bin/python3
"""Doc
"""


def max_integer(list=[]):
    """Doc
    """
    # if empty list
    if len(list) == 0:
        return 1
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
