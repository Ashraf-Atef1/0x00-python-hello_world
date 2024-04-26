#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """
    length = len(list_of_integers)
    m = length // 2
    if length == 0:
        return None
    def peak(lst, length, m):
        if (m == 0 or lst[m] >= lst[m - 1]) and (m == length - 1 or lst[m] >= lst[m + 1]):
            return lst[m]
        if m > 0 and lst[m - 1] > lst[m]:
            return peak(lst, m, m // 2)
        return peak(lst, length, m + (length - m) // 2)
    return peak(list_of_integers, length, m)
