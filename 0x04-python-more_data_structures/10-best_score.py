#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = (None, None)
    if a_dictionary:
        for key, value in a_dictionary.items():
            if(not max_value[1] or max_value[1] < value):
                max_value = (key, value)
    return max_value[0]
