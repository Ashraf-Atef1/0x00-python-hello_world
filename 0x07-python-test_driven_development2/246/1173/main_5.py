#!/usr/bin/python3
""" Doc """
matrix_mul = __import__('100-matrix_mul').matrix_mul

m_a = [[1, 2], [3, 4]]
m_b = [[]]
try:
    print(matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
