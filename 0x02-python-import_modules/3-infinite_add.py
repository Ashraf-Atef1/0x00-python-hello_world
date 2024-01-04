#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    sum = 0
    if argc:
        for num in argv[1:]:
            sum += int(num)
    print(sum)
