"""
Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i and j. Write a method
to insert Minto N such that M starts at bit j and ends at bit i. You can assume that the bits j through
i have enough space to fit all of M. That is, if M = 18811, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
fit between bit 3 and bit 2.
5.1
EXAMPLE
Input:
N = 10000000000,   M = 10011,  i = 2,  j = 6
Output: N = 10001001100

insertion([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1], 2, 6)
"""


def insertion(n, m, i, j):
    offset = len(n) - (j + i - 1)
    for index in range(len(m)):
        n[offset + index] = m[index]
    return n


def update_bits(n, m, i, j):
    all_ones = ~0

    left = all_ones << (j + 1)
    right = (1 << i) - 1

    mask = left | right

    n_cleared = n & mask
    m_shifted = m << i

    return n_cleared | m_shifted

