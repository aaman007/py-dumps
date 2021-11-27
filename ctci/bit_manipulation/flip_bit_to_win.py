"""
Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1 s you could create.

EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8
"""


def count_contiguous(number):
    mx, count = 0, 0
    for bit in range(32):
        if number & (1 << bit):
            count += 1
            mx = max(count, mx)
        else:
            count = 0
    return mx


def flip_bit_to_win(number):
    """ Could be optimized to O(b) TC and O(1) SC using prev_ones_sequence, curr_ones_sequence """
    mx = count_contiguous(number)
    for bit in range(32):
        if not number & (1 << bit):
            mx = max(mx, count_contiguous(number | (1 << bit)))
    return mx

