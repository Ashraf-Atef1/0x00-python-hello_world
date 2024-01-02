#!/usr/bin/python3
for letter in map(chr, range(97, 123)):
    if letter != "e" and letter != "q":
        print("{}".format(letter), end="")
