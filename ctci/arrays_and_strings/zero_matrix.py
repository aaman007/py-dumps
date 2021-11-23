"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.

Sample 1:
[[1, 2, 0], [4, 0, 6], [7, 8, 9]]

Sample 2:
[[1, 0, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [13, 14, 15, 16]]
"""


def zero_matrix_v1(matrix):
    """
    Assuming matrix doesn't contain negative numbers,
    otherwise use a number X that won't be in matrix instead of -1
    """

    m, n = len(matrix), len(matrix[0])
    x = -1

    for i in range(m):
        for j in range(1, n):
            if not matrix[i][j]:
                continue
            matrix[i][j] = matrix[i][j] if matrix[i][j-1] not in [x, 0] else x
        for j in range(n-2, -1, -1):
            if not matrix[i][j]:
                continue
            matrix[i][j] = matrix[i][j] if matrix[i][j+1] not in [x, 0] else x

    for j in range(n):
        for i in range(1, m):
            matrix[i][j] = matrix[i][j] if matrix[i-1][j] else 0
        for i in range(m-2, -1, -1):
            matrix[i][j] = matrix[i][j] if matrix[i+1][j] else 0

    for i in range(m):
        for j in range(n):
            matrix[i][j] = matrix[i][j] if matrix[i][j] != x else 0

    return matrix


def zero_matrix_v2(matrix):
    m, n = len(matrix), len(matrix[0])
    marked_rows = set()
    marked_cols = set()

    for row in range(m):
        for col in range(n):
            if not matrix[row][col]:
                marked_rows.add(row)
                marked_cols.add(col)

    for row in range(m):
        for col in range(n):
            if row in marked_rows or col in marked_cols:
                matrix[row][col] = 0

    return matrix


class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])

    def nullify_row(self, row):
        for col in range(self.n):
            self.matrix[row][col] = 0

    def nullify_column(self, col):
        for row in range(self.m):
            self.matrix[row][col] = 0

    def zero_matrix(self):
        row_has_zero = col_has_zero = False
        for col in range(self.n):
            if not self.matrix[0][col]:
                row_has_zero = True
                break

        for row in range(self.m):
            if not self.matrix[row][0]:
                col_has_zero = True
                break

        for row in range(1, self.m):
            for col in range(1, self.n):
                if not self.matrix[row][col]:
                    self.matrix[row][0] = 0
                    self.matrix[0][col] = 0

        for row in range(1, self.m):
            if not self.matrix[row][0]:
                self.nullify_row(row)

        for col in range(1, self.n):
            if not self.matrix[0][col]:
                self.nullify_column(col)

        if row_has_zero:
            self.nullify_row(0)
        if col_has_zero:
            self.nullify_column(0)

        return self.matrix

