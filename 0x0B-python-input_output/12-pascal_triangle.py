#!/usr/bin/python3
"""
This module contain a Pascal's Triangle maker
"""


def pascal_triangle(n):
    """a Pascal's Triangle maker function"""
    triangle_list = [[1], [1, 1], [1, 2, 1]]
    n -= 1
    new_mid = 0
    old_mid = 1
    if n < 0:
        return []
    elif n < 3:
        return triangle_list[: n + 1]
    for level in range(3, n + 1):
        level_list = [1, level]
        ol_list = triangle_list[level - 1]
        level_list.extend([ol_list[i] + ol_list[i + 1]
                           for i in range(1, old_mid)])
        if level % 2:
            new_mid = level_list[-1] * 2
            level_list = [*level_list, *level_list[::-1]]
        else:
            old_mid += 1
            level_list = [*level_list, new_mid, *level_list[::-1]]
        triangle_list.append(level_list)
    return triangle_list
