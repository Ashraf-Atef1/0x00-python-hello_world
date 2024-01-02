#!/usr/bin/python3
for letter in reversed(list(range(97, 123))):
    print("{}".format(chr(letter if not letter % 2 else letter - 32)), end="")
