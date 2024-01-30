#!/usr/bin/python3
# 101-nqueens.py
# Nwafor Chukwuebuka
"""Solves the N-queens puzzle.
"""
import sys


def initialize_board(size):
    """Initialize an `size`x`size` sized chessboard with empty cells."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board


def deepcopy_board(board):
    """Return a deep copy of a chessboard."""
    return [row[:] for row in board]


def get_queens_positions(board):
    """Return the positions of the queens on the board."""
    queens = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'Q':
                queens.append([row, col])
    return queens


def mark_attacked_positions(board, row, col):
    """Mark all attacked positions on the board."""
    size = len(board)
    # Mark horizontally and vertically
    for i in range(size):
        board[row][i] = 'x'
        board[i][col] = 'x'
    # Mark diagonally
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if i >= 0 and j >= 0:
            board[i][j] = 'x'
    for i, j in zip(range(row-1, -1, -1), range(col+1, size)):
        if i >= 0 and j < size:
            board[i][j] = 'x'
    for i, j in zip(range(row+1, size), range(col-1, -1, -1)):
        if i < size and j >= 0:
            board[i][j] = 'x'
    for i, j in zip(range(row+1, size), range(col+1, size)):
        if i < size and j < size:
            board[i][j] = 'x'


def solve_nqueens(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle."""
    size = len(board)
    if queens == size:
        solutions.append(get_queens_positions(board))
        return

    for col in range(size):
        if board[row][col] == ' ':
            new_board = deepcopy_board(board)
            new_board[row][col] = 'Q'
            mark_attacked_positions(new_board, row, col)
            solve_nqueens(new_board, row + 1, queens + 1, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = initialize_board(n)
    solutions = []
    solve_nqueens(board, 0, 0, solutions)

    for sol in solutions:
        print(sol)
