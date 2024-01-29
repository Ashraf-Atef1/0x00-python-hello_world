#!/usr/bin/python3
""" Doc """
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

m_a = [[1, 2], [3, 4], [3, 4]]
m_b = [[5, 6, 1], [7, 8, 2]]
print(lazy_matrix_mul(m_a, m_b))
