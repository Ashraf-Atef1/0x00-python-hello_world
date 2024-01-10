#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    if my_list:
        sup = 0
        div = 0
        for n1, n2 in my_list:
            sup += n1 * n2
            div += n2
        result = sup / div
    return result
