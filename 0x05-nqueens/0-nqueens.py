#!/usr/bin/python3
"""This module solves the `N` queens problem using a backtracking algorithm to
place N non-attacking queens on an N x N chessboard"""

import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def board(size, row=0, column=[], forward_diagonal=[], backward_diagonal=[]):
    """Prints the chess board on the screen"""

    if row < size:
        for i in range(size):
            if i not in column and row + i not in forward_diagonal and \
                  row - i not in backward_diagonal:
                yield from board(
                    size, row + 1, column + [i],
                    forward_diagonal + [row + i], backward_diagonal + [row - i]
                    )
    else:
        yield column


def solve(size):
    """Solves the `N` queens problem using a backtracking algorithm"""

    k = []
    i = 0
    for solution in board(size, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
