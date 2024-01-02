#!/usr/bin/python3
def fizzbuzz():
    to_be_print = ""
    for num in range(1, 101):
        if not num % 3:
            to_be_print += "Fizz"
        elif not num % 5:
            to_be_print += "Buzz"
        else:
            to_be_print += str(num)
        to_be_print += " "
    print(to_be_print)
