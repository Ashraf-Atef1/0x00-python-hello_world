#!/usr/bin/python3
"""Doc
"""


def max_integer(list=[]):
    """Doc
    """
    if len(list) == 0:
        return None

    # If one number is negative, exchange it to a positive number
    copy_list = list[:]
    i = 0
    while i < len(copy_list):
        if copy_list[i] < 0:
            copy_list[i] *= -1
        i += 1

    result = copy_list[0]
    i = 1
    while i < len(copy_list):
        if copy_list[i] > result:
            result = copy_list[i]
        i += 1
    return result
