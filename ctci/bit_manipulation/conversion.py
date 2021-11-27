"""
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
EXAMPLE
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""


def hamming_distance(a, b):
    count = 0
    for bit in range(32):
        count += (a & (1 << bit) != b & (1 << bit))
    return count


def hamming_distance_xor(a, b):
    return bin((a ^ b)).count('1')


def hamming_distance_optimized(a, b):
    xor = a ^ b
    count = 0
    while xor:
        count += 1
        xor = xor & (xor - 1)
    return count
