#!/usr/bin/python3
""" Doc """
import ctypes

lib = ctypes.CDLL('./libPythonHBTN.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = b"There is no spoon"
lib.print_python_string(s)
