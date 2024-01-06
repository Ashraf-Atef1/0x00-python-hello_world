#!/usr/bin/python3
def max_integer(my_list=[]):
    def compare_large(old, new):
        if old > new:
            return old
        else:
            return new
    max_num = None
    for num in my_list:
        max_num = compare_large(max_num if max_num else 0, num)
    return max_num
