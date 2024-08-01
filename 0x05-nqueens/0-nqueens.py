#!/usr/bin/python
"""
Python code that produces number of queens.

print every possible solution to the problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Back Tracking
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r + 1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem.

    Args:
        n (int): number of queens. Must be >= 4

    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    columns = set()
    positive_diagonal = set()
    negative_diagonal = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, columns, positive_diagonal, negative_diagonal, board)


if __name__ == "__main__":
    # Get number from system argument
    number: str = sys.argv[1] if len(sys.argv) > 1 else 0
    if not number.isdigit():
        print("N must be a number")
        sys.exit(1)
    number: int = int(number)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Call Number of queens function
    nqueens(number)
