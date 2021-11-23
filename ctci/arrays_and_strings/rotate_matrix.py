"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

Sample 1:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Sample 2:
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
"""


def transpose(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def mirror(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

    return matrix


def rotate_matrix(matrix):
    matrix = transpose(matrix)
    return mirror(matrix)

