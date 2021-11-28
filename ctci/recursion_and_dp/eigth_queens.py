"""
Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        banned_cols = [False for _ in range(n)]
        banned_left_diag = [False for _ in range(2 * n)]
        banned_right_diag = banned_left_diag.copy()
        answer = []

        def play_move(row, col):
            ld, rd = get_diagonals(row, col)
            banned_cols[col] = banned_left_diag[ld] = banned_right_diag[rd] = True
            board[row][col] = 'Q'

        def clear_move(row, col):
            ld, rd = get_diagonals(row, col)
            board[row][col] = '.'
            banned_cols[col] = banned_left_diag[ld] = banned_right_diag[rd] = False

        def get_diagonals(row, col):
            return n + row - col, row + col

        def is_not_safe(row, col):
            ld, rd = get_diagonals(row, col)
            return banned_cols[col] or banned_left_diag[ld] or banned_right_diag[rd]

        def rec(row):
            if row == n:
                answer.append([])
                for x in board:
                    answer[-1].append(''.join(x))
                return

            for col in range(n):
                if is_not_safe(row, col):
                    continue

                play_move(row, col)
                rec(row + 1)
                clear_move(row, col)

        rec(0)

        return answer

