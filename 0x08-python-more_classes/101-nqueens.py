#!/usr/bin/python3
"""N queens puzzle solver"""


from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = 0

try:
    N = int(argv[1])

    if N < 4:
        print("N must be at least 4")
        exit(1)
except Exception:
    print("N must be a number")
    exit(1)

full_cols = set()
full_rows = set()
full_positve_d = set()
full_negtive_d = set()
c_solution = []
solutions = []


def get_solutions(row):
    """get all possible solutions"""
    for col in range(N):
        if (
            col in full_cols
            or (row - col) in full_positve_d
            or (row + col) in full_negtive_d
        ):
            continue
        add_new(row, col)
        if row == N - 1:
            solutions.append(c_solution.copy())
            remove_old(row, col)
            return
        get_solutions(row + 1)
        remove_old(row, col)


def add_new(row, col):
    """add a new node"""
    c_solution.append([row, col])
    full_cols.add(col)
    full_positve_d.add(row - col)
    full_negtive_d.add(row + col)


def remove_old(row, col):
    """remove an old node"""
    c_solution.remove([row, col])
    full_cols.remove(col)
    full_positve_d.remove(row - col)
    full_negtive_d.remove(row + col)


get_solutions(0)
for solution in solutions:
    print(solution)
