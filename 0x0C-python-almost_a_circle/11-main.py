#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s = Square(10, 10, 10, 10)
    s.update(id=None, size=7, x=18)
    correct = "[Square] ({}) 18/10 - 7".format(s.id)
    print(correct, str(s))