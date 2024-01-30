#!/usr/bin/python3
"""N queens puzzle solver"""
from sys import argv

argv = [1, 4]
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

# def get_solutions(N):
#     solutions = []
    

#     for i in range(N):
#         full_cols = {i}
#         full_rows = {0}
#         full_positve_d = {0 - i}
#         full_negtive_d = {0 + i}
#         solution = [[0, i]]

#         for row in range(1, N):
#             avalible_rows = []
#             for col in range(N):
#                 if row in full_rows or col in full_cols or row - col in full_positve_d or row + col in full_negtive_d:
#                     continue
#                 avalible_rows.append([row, col])
#             for sol in avalible_rows
#                 row, col = avalible_rows[-1]
#                 solution.append(avalible_rows[-1])
#                 full_cols.add(col)
#                 full_rows.add(row)
#                 full_positve_d.add(row - col)
#                 full_negtive_d.add(row + col)
#         print(solution)
#         if len(solution) == N:
#             solutions.append(solution)
#     print(solutions)

board = [[0] * N for i in range(N)]
full_cols = set()
full_rows = set()
full_positve_d = set()
full_negtive_d = set()
solutions = []
print(board)
def get_solutions(row):
    if row == N -1:
        print(board)
        return
    for col in range(N):
        remove_old(row, col)
        if col in full_cols or (row - col) in full_positve_d or (row + col) in full_negtive_d:
            continue
        add_new(row, col)
        get_solutions(row + 1)
        print(board)
def add_new(row, col):
    board[row][col] = 1
    full_cols.add(col)
    full_positve_d.add(row - col)
    full_negtive_d.add(row + col)
def remove_old(row, col):
    old_col = col - 1
    old_row = row
    if row + 1 < N:
        for i in board[row + 1]:
            if i:
                old_col = N -1
                old_row = row + 1

    if col and board[old_row][old_col]:
        board[old_row][old_col] = 0
        full_cols.remove(old_col)
        full_positve_d.remove(old_row - old_col)
        full_negtive_d.remove(old_row + old_col)
    old_col = col - 1
    old_row = row
    if col and board[old_row][old_col]:
        board[old_row][old_col] = 0
        full_cols.remove(old_col)
        full_positve_d.remove(old_row - old_col)
        full_negtive_d.remove(old_row + old_col)
get_solutions(0)
print(board)