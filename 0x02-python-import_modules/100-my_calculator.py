#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv) - 1
    if argc == 3:
        a = int(argv[1])
        b = int(argv[3])
        operation = argv[2]
        if operation == "+":
            print("{} {} {} = {}".format(a, operation, b, add(a, b)))
        elif operation == "-":
            print("{} {} {} = {}".format(a, operation, b, sub(a, b)))
        elif operation == "*":
            print("{} {} {} = {}".format(a, operation, b, mul(a, b)))
        elif operation == "/":
            print("{} {} {} = {}".format(a, operation, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
