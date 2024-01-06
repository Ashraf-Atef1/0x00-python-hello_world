#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    i = 0
    all = [tuple_a, tuple_b]
    while i < 2:
        try:
            sum1 += all[i][0]
        except IndexError:
            sum1 += 0
        try:
            sum2 += all[i][1]
        except IndexError:
            sum2 += 0
        finally:
            i += 1
    return (sum1, sum2)
