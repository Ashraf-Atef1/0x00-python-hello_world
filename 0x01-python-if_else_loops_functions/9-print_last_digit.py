#!/usr/bin/python3
def print_last_digit(number):
    number %= 10 if number >= 0 else -10
    print("{}".format(number), end="")
    return number
