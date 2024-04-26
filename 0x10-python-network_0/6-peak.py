#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """
    if list_of_integers:
        pre_number = None
        for i in range(len(list_of_integers) - 1):
            current_number = list_of_integers[i]
            next_number = list_of_integers[i + 1]
            if (pre_number is not None and current_number > pre_number)\
            and current_number > next_number:
                return current_number
            pre_number = current_number
        return pre_number
    else:
        return None
