#!/usr/bin/python3
""" Doc """
import ctypes

lib = ctypes.CDLL('./libPythonHBTN.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "没有勺子"
lib.print_python_string(s)
s = "숟가락이 없다"
lib.print_python_string(s)
