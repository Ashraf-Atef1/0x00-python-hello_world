#!/usr/bin/python3
for letter in map(chr, range(97, 123)):
    if letter != "e" or letter != "q":
        print("{}".format(letter), end="")
