#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s = Square(7, 0, 0, [4])
    s.size = 15
    s.x = 8
    s.y = 10
    print("[Square] ([4]) 8/10 - 15", str(s))